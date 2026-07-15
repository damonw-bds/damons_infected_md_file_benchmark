#!/usr/bin/env python3
"""
Regenerate the damons_infected_md_file_benchmark corpus from upstream repos.

Usage:
  1. Clone the six upstream repos into --tmp (default: ~/md-eval-corpus/_tmp):
       verazuo/jailbreak_llms
       yunwei37/prompt-hacker-collections
       JailbreakBench/artifacts
       centerforaisafety/HarmBench
       microsoft/promptbench
       Libr-AI/do-not-answer
  2. Run:  python3 extract.py [--tmp DIR] [--out DIR] [--cap N]

Each source becomes one directory of .md files under --out. Existing
per-source directories are wiped and rewritten on every run.
"""
import argparse, csv, glob, json, os, re, shutil, sys
from pathlib import Path

DEFAULT_CAP = 3000
csv.field_size_limit(sys.maxsize)


def safe_slug(s: str, maxlen: int = 60) -> str:
    s = re.sub(r'[^A-Za-z0-9_.-]+', '_', (s or '').strip())[:maxlen]
    return s or 'item'


def write_md(out_dir: Path, idx: int, front: dict, body: str, slug_hint: str = ''):
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = safe_slug(slug_hint) if slug_hint else 'item'
    path = out_dir / f"{idx:05d}_{slug}.md"
    lines = ['---']
    for k, v in front.items():
        vs = str(v).replace('\n', ' ').replace('"', '\\"')
        lines.append(f'{k}: "{vs}"')
    lines.append('---')
    lines.append('')
    path.write_text('\n'.join(lines) + body.rstrip() + '\n', encoding='utf-8')


def do_jailbreak_llms(tmp: Path, out_root: Path, cap: int):
    """
    Ingest the FULL set of adversarial content from Xu et al.'s jailbreak_llms:
      - jailbreak_prompts_2023_12_25.csv  (~24,853 rows)  — latest snapshot
      - jailbreak_prompts_2023_05_07.csv  (~7,678 rows)   — earlier snapshot
      - forbidden_question/forbidden_question_set.csv     — canonical forbidden-Q set
    Prompt text is deduplicated by SHA-1 across all three sources so we don't
    emit the same payload twice when it appears in both snapshots.

    The `--cap` argument is IGNORED for this source when it's the default
    (3000) so the full set lands. Pass a small cap explicitly to sample.
    """
    import hashlib
    out = out_root / 'bad_jailbreak_llms'
    if out.exists(): shutil.rmtree(out)
    # Cap semantics: if user left the default (3000), interpret as "no cap".
    # If they set anything else, respect it.
    effective_cap = None if cap == DEFAULT_CAP else cap

    seen = set()   # SHA-1 of prompt text, for dedup across snapshots
    n = 0

    def _hash(s: str) -> str:
        return hashlib.sha1(s.encode('utf-8', errors='replace')).hexdigest()

    # 1) jailbreak_prompts CSVs (latest first, so the newer metadata wins on ties)
    prompt_csvs = [
        ('jailbreak_prompts_2023_12_25.csv', '2023_12_25'),
        ('jailbreak_prompts_2023_05_07.csv', '2023_05_07'),
    ]
    for fname, snapshot in prompt_csvs:
        src = tmp / f'jailbreak_llms/data/prompts/{fname}'
        if not src.exists():
            print(f'  WARN: {src} missing; skipping')
            continue
        with open(src, newline='', encoding='utf-8', errors='replace') as f:
            for i, row in enumerate(csv.DictReader(f)):
                if effective_cap is not None and n >= effective_cap: break
                prompt = (row.get('prompt') or '').strip()
                if not prompt: continue
                h = _hash(prompt)
                if h in seen: continue
                seen.add(h)
                front = {
                    'source': 'jailbreak_llms',
                    'source_url': 'https://github.com/verazuo/jailbreak_llms',
                    'source_file': f'prompts/{fname}',
                    'snapshot': snapshot,
                    'source_row_index': i,
                    'platform': row.get('platform', ''),
                    'community': row.get('community', ''),
                    'created_at': row.get('created_at', ''),
                    'is_jailbreak': row.get('jailbreak', ''),
                    'license': 'MIT (see upstream)',
                    'category': 'jailbreak_prompt',
                }
                write_md(out, n, front, prompt, slug_hint=row.get('community', ''))
                n += 1

    # 2) forbidden_question_set — different schema, question-shaped rows
    fqs = tmp / 'jailbreak_llms/data/forbidden_question/forbidden_question_set.csv'
    if fqs.exists():
        with open(fqs, newline='', encoding='utf-8', errors='replace') as f:
            for i, row in enumerate(csv.DictReader(f)):
                if effective_cap is not None and n >= effective_cap: break
                # column is typically 'question'; fall back to any long text col
                q = (row.get('question') or row.get('prompt') or '').strip()
                if not q: continue
                h = _hash(q)
                if h in seen: continue
                seen.add(h)
                front = {
                    'source': 'jailbreak_llms',
                    'source_url': 'https://github.com/verazuo/jailbreak_llms',
                    'source_file': 'forbidden_question/forbidden_question_set.csv',
                    'source_row_index': i,
                    'content_policy_name': row.get('content_policy_name', ''),
                    'content_policy_id': row.get('content_policy_id', ''),
                    'q_id': row.get('q_id', ''),
                    'license': 'MIT (see upstream)',
                    'category': 'forbidden_question',
                }
                write_md(out, n, front, q,
                         slug_hint=row.get('content_policy_name', 'forbidden_q'))
                n += 1
    print(f'jailbreak_llms: {n} files -> {out}')


def do_harmbench(tmp: Path, out_root: Path, cap: int):
    src = tmp / 'HarmBench/data/behavior_datasets/harmbench_behaviors_text_all.csv'
    out = out_root / 'bad_harmbench'
    if out.exists(): shutil.rmtree(out)
    n = 0
    with open(src, newline='', encoding='utf-8', errors='replace') as f:
        for i, row in enumerate(csv.DictReader(f)):
            if n >= cap: break
            behavior = (row.get('Behavior') or '').strip()
            if not behavior: continue
            body = behavior
            if row.get('ContextString'):
                body += '\n\n---\n\nContext:\n\n' + row['ContextString']
            front = {
                'source': 'HarmBench',
                'source_url': 'https://github.com/centerforaisafety/HarmBench',
                'source_row_index': i,
                'behavior_id': row.get('BehaviorID', ''),
                'functional_category': row.get('FunctionalCategory', ''),
                'semantic_category': row.get('SemanticCategory', ''),
                'tags': row.get('Tags', ''),
                'license': 'MIT (see upstream)',
                'category': 'harmful_behavior',
            }
            write_md(out, n, front, body, slug_hint=row.get('BehaviorID', ''))
            n += 1
    print(f'HarmBench: {n} files -> {out}')


def do_do_not_answer(tmp: Path, out_root: Path, cap: int):
    src = tmp / 'do-not-answer/datasets/data_en.csv'
    out = out_root / 'bad_do_not_answer'
    if out.exists(): shutil.rmtree(out)
    n = 0
    with open(src, newline='', encoding='utf-8', errors='replace') as f:
        for i, row in enumerate(csv.DictReader(f)):
            if n >= cap: break
            q = (row.get('question') or '').strip()
            if not q: continue
            front = {
                'source': 'do-not-answer',
                'source_url': 'https://github.com/Libr-AI/do-not-answer',
                'source_row_index': i,
                'risk_area': row.get('risk_area', ''),
                'types_of_harm': row.get('types_of_harm', ''),
                'specific_harms': row.get('specific_harms', ''),
                'license': 'Apache-2.0 (see upstream)',
                'category': 'should_refuse_question',
            }
            slug = (row.get('types_of_harm') or '')[:30]
            write_md(out, n, front, q, slug_hint=slug)
            n += 1
    print(f'do-not-answer: {n} files -> {out}')


def do_jailbreakbench(tmp: Path, out_root: Path, cap: int):
    out = out_root / 'bad_jailbreakbench'
    if out.exists(): shutil.rmtree(out)
    n = 0
    files = sorted(glob.glob(str(tmp / 'artifacts/attack-artifacts/**/*.json'), recursive=True))
    for fpath in files:
        if n >= cap: break
        if 'attack-info' in fpath or 'test-artifact' in fpath: continue
        parts = fpath.split('attack-artifacts/', 1)[1].split('/')
        attack = parts[0] if parts else 'unknown'
        threat = parts[1] if len(parts) > 1 else ''
        model  = parts[2].replace('.json', '') if len(parts) > 2 else ''
        try:
            data = json.load(open(fpath, encoding='utf-8'))
        except Exception:
            continue
        for jb in data.get('jailbreaks', []):
            if n >= cap: break
            prompt = (jb.get('prompt') or '').strip()
            if not prompt: continue
            front = {
                'source': 'JailbreakBench',
                'source_url': 'https://github.com/JailbreakBench/artifacts',
                'source_file': f'{attack}/{threat}/{model}',
                'attack_method': attack,
                'threat_model': threat,
                'target_model': model,
                'goal': jb.get('goal', ''),
                'behavior': jb.get('behavior', ''),
                'category': jb.get('category', ''),
                'jailbroken': jb.get('jailbroken', ''),
                'index_in_file': jb.get('index', ''),
                'license': 'MIT (see upstream)',
            }
            write_md(out, n, front, prompt,
                     slug_hint=f'{attack}_{model}_{jb.get("index","")}')
            n += 1
    print(f'JailbreakBench: {n} files -> {out}')


def do_promptbench(tmp: Path, out_root: Path, cap: int):
    out = out_root / 'bad_promptbench'
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    n = 0

    adv_dir = tmp / 'promptbench/promptbench/prompts/adv_prompts'
    for adv_md in sorted(adv_dir.glob('*.md')):
        if adv_md.name.lower().startswith('readme'):
            continue
        text = adv_md.read_text(encoding='utf-8', errors='replace')
        for i, line in enumerate(text.splitlines()):
            if n >= cap: break
            line = line.strip().lstrip('-').lstrip('*').strip()
            if not line or len(line) < 15: continue
            front = {
                'source': 'promptbench',
                'source_url': 'https://github.com/microsoft/promptbench',
                'source_file': f'adv_prompts/{adv_md.name}',
                'source_line': i,
                'license': 'MIT (see upstream)',
                'category': 'adversarial_prompt',
            }
            write_md(out, n, front, line, slug_hint=adv_md.stem)
            n += 1
        if n >= cap: break

    sap = tmp / 'promptbench/promptbench/prompts/semantic_atk_prompts.py'
    if sap.exists() and n < cap:
        content = sap.read_text(encoding='utf-8', errors='replace')
        strings = re.findall(
            r'"""(.*?)"""|\'\'\'(.*?)\'\'\'|"([^"\n]{20,})"|\'([^\'\n]{20,})\'',
            content, flags=re.DOTALL)
        for i, quad in enumerate(strings):
            if n >= cap: break
            s = next((x for x in quad if x), '').strip()
            if not s or len(s) < 20: continue
            front = {
                'source': 'promptbench',
                'source_url': 'https://github.com/microsoft/promptbench',
                'source_file': 'semantic_atk_prompts.py',
                'source_index': i,
                'license': 'MIT (see upstream)',
                'category': 'semantic_attack_prompt',
            }
            write_md(out, n, front, s, slug_hint='semantic_atk')
            n += 1
    print(f'promptbench: {n} files -> {out}')


def do_prompt_hacker(tmp: Path, out_root: Path, cap: int):
    out = out_root / 'bad_prompt_hacker'
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    n = 0
    src_root = tmp / 'prompt-hacker-collections'
    for md in src_root.rglob('*.md'):
        if n >= cap: break
        rel = md.relative_to(src_root)
        slug = safe_slug(str(rel).replace('/', '__').replace('.md', ''), maxlen=80)
        text = md.read_text(encoding='utf-8', errors='replace')
        front = {
            'source': 'prompt-hacker-collections',
            'source_url': 'https://github.com/yunwei37/prompt-hacker-collections',
            'source_file': str(rel),
            'license': 'MIT (see upstream)',
            'category': 'curated_jailbreak_notes',
        }
        write_md(out, n, front, text, slug_hint=slug)
        n += 1
    print(f'prompt-hacker-collections: {n} files -> {out}')


def write_manifest(out_root: Path, cap: int):
    lines = ['# Corpus manifest',
             '',
             f'Generated with cap={cap} per source.',
             '',
             '## Directories', '']
    for d in sorted(out_root.iterdir()):
        if not d.is_dir() or d.name.startswith('_') or not d.name.startswith('bad_'):
            continue
        count = len(list(d.glob('*.md')))
        lines.append(f'- `{d.name}/` — {count} files')
    (out_root / 'MANIFEST.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'MANIFEST -> {out_root / "MANIFEST.md"}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tmp', default=os.path.expanduser('~/md-eval-corpus/_tmp'),
                    help='Directory containing upstream git clones')
    ap.add_argument('--out', default=str(Path(__file__).parent),
                    help='Output root (default: this repo)')
    ap.add_argument('--cap', type=int, default=DEFAULT_CAP,
                    help=f'Max files per source (default: {DEFAULT_CAP})')
    args = ap.parse_args()

    tmp = Path(args.tmp); out = Path(args.out)
    if not tmp.exists():
        sys.exit(f'--tmp {tmp} does not exist; clone the six upstream repos there first')

    do_jailbreak_llms(tmp, out, args.cap)
    do_harmbench(tmp, out, args.cap)
    do_do_not_answer(tmp, out, args.cap)
    do_jailbreakbench(tmp, out, args.cap)
    do_promptbench(tmp, out, args.cap)
    do_prompt_hacker(tmp, out, args.cap)
    write_manifest(out, args.cap)


if __name__ == '__main__':
    main()
