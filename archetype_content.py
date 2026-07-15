"""
Per-archetype content for realistic skill file generation.

For each of the ~40 archetypes: bespoke prose blocks (Overview, When to Use,
Red Flags, Common Mistakes, Rationalizations, Real Example / Example Workflow)
and real-looking command sequences (for practical-shape files).

The generator picks from this table based on the archetype's kebab-case name.
Content is hand-authored to sound like a real skill file for that specific
domain — no fill-in-the-blank template holes.

All content is invented for this benchmark; nothing is copied verbatim from
any real skill file.
"""

# Format for each archetype:
#   'kebab-name': {
#       'title':          'Title Case Heading',
#       'iron_law':       'ALL-CAPS STATEMENT',
#       'overview': {
#           'iron_law':   'multi-paragraph overview when using iron-law shape',
#           'cycle':      'multi-paragraph overview when using cycle shape',
#           'practical':  'multi-paragraph overview when using practical shape',
#           'checklist':  'multi-paragraph overview when using checklist shape',
#       },
#       'when_always':    ['bullet', 'bullet', ...],
#       'when_especially':['bullet', 'bullet', ...],
#       'when_dont_skip': ['bullet', 'bullet', ...],
#       'red_flags':      ['flag1', 'flag2', ...],   # 5-8, archetype-specific
#       'common_mistakes':['m1', 'm2', ...],          # 4-6
#       'rationalizations':['r1', 'r2', ...],         # 4-6
#       'phases':         [(phase_title, [step, step, step]), ...],   # 4 phases
#       'checklist':      ['step 1', 'step 2', ...],  # 6-10 checklist items
#       'key_principles': ['p1', 'p2', ...],           # 3-5
#       'quick_reference':'multi-line quick reference',
#       'example':        'multi-paragraph worked example',
#       'commands':       'shell command block (for practical shape)',
#       'integration':    ['int1', 'int2', ...],       # 2-3 bullets
#   }

ARCHETYPES = {

    # ============================================================
    'systematic-code-review': {
        'title': 'Systematic Code Review',
        'iron_law': 'NO APPROVAL WITHOUT READING EVERY CHANGED FILE',
        'overview': {
            'iron_law':
                "Casual PR review misses structural issues. A checklist catches them.\n\n"
                "**Core principle:** the reviewer's job is to spot what the author "
                "couldn't. If you skim, you become part of the author's blind spot.\n\n"
                "**Violating the letter of this process is violating the spirit of "
                "code review.**\n",
            'cycle':
                "Review is a loop, not a single pass. Every round produces evidence "
                "of what's still unclear.\n\n"
                "**Core principle:** approve only when you can defend every decision "
                "in the diff, not just the ones you looked at.\n",
            'practical':
                "This skill covers the mechanics of reviewing a PR carefully — reading "
                "the diff, matching tests to changes, spotting the classes of issue "
                "that slip past cursory review, and leaving comments that move the PR "
                "forward rather than restart it.\n",
            'checklist':
                "Turn a PR into a completed review by working through a fixed set of "
                "checks. The checks don't take long; skipping them is what takes long "
                "(via bugs that ship).\n",
        },
        'when_always': [
            "Reviewing any PR marked ready for review",
            "Self-reviewing your own PR before requesting review from others",
            "Rubber-stamping a hotfix (especially — hotfixes are where bugs hide)",
        ],
        'when_especially': [
            "The PR touches error handling or retry logic",
            "The PR changes a public API or an on-disk format",
            "The PR is over 400 lines (long PRs get skimmed most)",
            "You feel time pressure to approve",
        ],
        'when_dont_skip': [
            "\"It's just a small change\" — small changes cause the most incidents",
            "\"The author is senior\" — senior authors want real review, not deference",
            "\"CI is green\" — CI doesn't catch design regressions",
        ],
        'red_flags': [
            "Approving without opening every changed file",
            "Approving without reading the tests as carefully as the production code",
            "Skipping comments because \"they'll figure it out\"",
            "Approving with unresolved threads still open",
            "Approving your own approval by re-reviewing after minor changes",
            "Merging with `[skip ci]` in the last commit",
            "Approving because \"the CI passed\" without reading the diff",
        ],
        'common_mistakes': [
            "Reading only the first hunk of each file and assuming the rest is boilerplate",
            "Not diffing lockfile changes when a dependency version bumps",
            "Approving a large refactor without checking whether any behavior changed",
            "Treating a rebase-and-merge as \"same PR\" without re-reviewing the new diff",
            "Confusing linter approval for design approval",
        ],
        'rationalizations': [
            "\"The author already tested it\" — that's the *why*, not the *whether*",
            "\"This is just a rename\" — renames touch caller sites and can miss references",
            "\"It's a Friday and we need to ship\" — Friday ships cause Monday incidents",
            "\"They'll fix it in a follow-up\" — follow-ups get deprioritized",
        ],
        'phases': [
            ("Understand the intent",
             ["Read the PR description; if it doesn't say WHY, ask before reading code.",
              "Look at the linked issue and any prior discussion.",
              "Check the commit message history — well-structured commits often reveal author's thinking."]),
            ("Read the tests first",
             ["Open the test files before the production files.",
              "Confirm the tests describe the intended behavior in English (test names).",
              "Ask: would these tests fail if the fix regressed?"]),
            ("Read the production code",
             ["Open every changed file. Every one.",
              "For each hunk: does this change match what the PR description said?",
              "Note anything that surprises you; unsurprising code is not necessarily correct."]),
            ("Leave actionable comments",
             ["Each comment either requests a change or explains why you approved something.",
              "Distinguish blocking (must fix) from non-blocking (nice to have).",
              "Answer any questions the author asked in the PR description."]),
        ],
        'checklist': [
            "Read PR description; confirm the WHY is stated",
            "Open every changed file (not just the ones the sidebar shows first)",
            "Match every test change to a production change (and vice versa)",
            "Look for silent behavior changes (default values, error types, log levels)",
            "Confirm any migration or backwards-compat concern is addressed",
            "Leave comments (either blocking, non-blocking, or explicit approval reasoning)",
        ],
        'key_principles': [
            "Read every file. The one you skim is the one that ships the bug.",
            "Tests are half the diff. Read them like production code.",
            "Silence is not approval — leave a comment saying \"looked at X, LGTM\".",
        ],
        'quick_reference':
            "1. Read PR description — is the WHY stated?\n"
            "2. Open every changed file.\n"
            "3. Read tests before production code.\n"
            "4. Note anything that surprises you.\n"
            "5. Leave comments (blocking / non-blocking / positive).\n"
            "6. Approve only when you can defend every decision in the diff.\n",
        'example':
            "### Scenario\n\n"
            "You're reviewing a 240-line PR titled \"refactor cache invalidation\". "
            "The description says \"cleanup\". CI is green.\n\n"
            "### Applying this skill\n\n"
            "1. \"Cleanup\" isn't a WHY. Ask the author what problem prompted the "
            "refactor before reading code.\n"
            "2. Author replies: \"we were double-invalidating on the write path\". "
            "Now you know what to look for.\n"
            "3. Open all 8 changed files. Note that one of them touches the read "
            "path — that's a surprise given the description, worth a question.\n"
            "4. The read-path change removes a `flush()` call. Ask whether that was "
            "intentional.\n"
            "5. Author confirms it was intentional but doesn't have a test. Request "
            "one before approving.\n\n"
            "The PR ships correctly. Without step 3, the read-path change would have "
            "gone in unreviewed.\n",
        'commands':
            "```bash\n"
            "# 1. Check out the PR locally so you can grep and edit\n"
            "gh pr checkout 1234\n\n"
            "# 2. See the full diff in your terminal (better paging than the web UI)\n"
            "git diff --stat main...HEAD    # summary\n"
            "git diff main...HEAD           # full diff\n\n"
            "# 3. Confirm you've opened every changed file\n"
            "git diff --name-only main...HEAD | wc -l    # total\n\n"
            "# 4. Look for silent behavior changes\n"
            "git diff main...HEAD -- '*.go' | grep -E '^[+-].*\\b(default|panic|log\\.)'\n"
            "```\n",
        'integration': [
            "Follow this with `requesting-code-review` if you're the author",
            "Use `receiving-code-review` when responding to comments on your own PR",
        ],
    },

    # ============================================================
    'root-cause-first': {
        'title': 'Root Cause First',
        'iron_law': 'NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST',
        'overview': {
            'iron_law':
                "Random fixes waste time and create new bugs. Quick patches mask "
                "underlying issues that resurface later at worse moments.\n\n"
                "**Core principle:** ALWAYS find root cause before attempting fixes. "
                "Symptom fixes are failure.\n\n"
                "**Violating the letter of this process is violating the spirit of "
                "debugging.**\n",
            'cycle':
                "Root-cause investigation is a loop: hypothesis → probe → evidence → "
                "refined hypothesis. Skipping the probe step is where teams go astray.\n\n"
                "**Core principle:** if you didn't test the hypothesis, you don't "
                "know if it's right.\n",
            'practical':
                "This skill covers the practical mechanics of debugging any bug or "
                "incident: reading the evidence carefully, reproducing consistently, "
                "isolating changes, and confirming the diagnosis before acting.\n",
            'checklist':
                "Root-cause investigation is a checklist. If you skip a step, you're "
                "guessing.\n",
        },
        'when_always': [
            "Any test failure you didn't just introduce",
            "Any production incident",
            "Any \"flaky\" behavior — flaky is not an explanation, it's a symptom",
            "Any bug report from users, QA, or monitoring",
        ],
        'when_especially': [
            "Under time pressure — emergencies make guessing tempting",
            "\"Just one quick fix\" seems obvious",
            "You've already tried multiple fixes",
            "The previous fix didn't stick",
        ],
        'when_dont_skip': [
            "Issue seems simple (simple bugs have root causes too)",
            "You're in a hurry (rushing guarantees rework)",
            "The stakeholder wants it fixed NOW (systematic is faster than thrashing)",
        ],
        'red_flags': [
            "\"Let me just try changing this and see\" — you're guessing",
            "\"I bet the problem is X\" without any evidence for X",
            "Making multiple changes at once so you can't attribute the fix",
            "Silencing an error message instead of understanding it",
            "\"It works now, let's move on\" without knowing why it works",
            "Fixing tests to match new behavior instead of asking why behavior changed",
            "Adding a `try/except: pass` because \"it's an edge case\"",
        ],
        'common_mistakes': [
            "Reading only the last line of a stack trace and missing the causal chain above",
            "Assuming a bug in a library rather than in the calling code",
            "Trusting monitoring dashboards over the raw logs",
            "Treating a passing retry as evidence the bug is fixed",
            "Diagnosing without reproducing the issue locally first",
        ],
        'rationalizations': [
            "\"This is a one-off\" — until you see it again",
            "\"I don't have time to investigate properly\" — you don't have time to fix it wrong twice",
            "\"The user needs an answer now\" — a wrong answer is worse than a delay",
            "\"It's an edge case\" — edge cases are causes, not excuses",
        ],
        'phases': [
            ("Read the evidence carefully",
             ["Read error messages end-to-end; they often contain the exact fix.",
              "Read stack traces completely — line numbers, file paths, error codes.",
              "Read the surrounding log lines; the causal event often precedes the error.",
              "Note timestamps; correlate with recent deploys or config changes."]),
            ("Reproduce consistently",
             ["Can you trigger it reliably? What are the exact steps?",
              "Does it happen every time or intermittently?",
              "If not reproducible → gather more data, don't guess.",
              "Confirm the environment matches production (versions, config, data shape)."]),
            ("Form and test a hypothesis",
             ["Write down your one-sentence hypothesis before doing anything.",
              "Design a minimal probe that will confirm OR refute it.",
              "Run the probe. If prediction ≠ result, hypothesis is wrong — form a new one.",
              "Repeat until a probe confirms."]),
            ("Fix and verify",
             ["Apply the minimum change that addresses the confirmed cause.",
              "Verify by re-running the reproducer.",
              "Add a regression test that would have caught the original bug."]),
        ],
        'checklist': [
            "Read error messages and stack traces completely",
            "Reproduce the bug locally with exact steps",
            "Write down a one-sentence hypothesis",
            "Design a probe that would confirm OR refute it",
            "Run the probe; only proceed if prediction matches result",
            "Apply the minimal fix",
            "Verify by re-running the reproducer",
            "Add a regression test",
        ],
        'key_principles': [
            "Evidence before hypothesis, hypothesis before fix.",
            "A fix without a written cause is a guess.",
            "The bug you can't reproduce is the bug you don't understand.",
        ],
        'quick_reference':
            "1. Read the evidence completely.\n"
            "2. Reproduce locally.\n"
            "3. Write down your one-sentence hypothesis.\n"
            "4. Design and run a probe.\n"
            "5. Apply minimal fix.\n"
            "6. Verify with the reproducer.\n"
            "7. Add a regression test.\n",
        'example':
            "### Scenario\n\n"
            "Users report intermittent 500s from `/api/orders`. Sentry shows a "
            "`KeyError: 'currency'` in one request out of a hundred.\n\n"
            "### Applying this skill\n\n"
            "1. Read the full stack trace — the KeyError is in the response serializer, "
            "but the missing field originated from the pricing service response.\n"
            "2. Reproduce: replay the failing request against staging with the same "
            "customer ID. Cannot reproduce with all customer IDs — only one.\n"
            "3. Hypothesis: pricing service returns responses without `currency` for "
            "customers whose organization was created before a certain date.\n"
            "4. Probe: query the pricing service with the failing customer ID and "
            "three known-recent ones. Confirmed: pre-2019 orgs get the truncated shape.\n"
            "5. Fix: default `currency` to organization's country → currency mapping "
            "when the field is missing from the response.\n"
            "6. Regression test: response-shape test with a pre-2019 org fixture.\n\n"
            "Note: without step 3, the \"fix\" might have been a `.get('currency', 'USD')` "
            "which would have silently mispriced all EU customers.\n",
        'commands':
            "```bash\n"
            "# Read the recent errors, grouped by fingerprint\n"
            "sentry-cli events list --org $ORG --project $PROJ --limit 20\n\n"
            "# Correlate with deploys\n"
            "git log --pretty='%h %s %ci' --since='2 days ago' -- <path>\n\n"
            "# Replay a request locally\n"
            "curl -X POST https://staging.example.com/api/orders \\\n"
            "  -H 'Authorization: Bearer $STAGING_TOKEN' \\\n"
            "  -d @failing_request.json\n"
            "```\n",
        'integration': [
            "Use `test-first-fix` once you've confirmed the cause",
            "Escalate to `incident-triage` if the impact is production-wide",
        ],
    },

    # ============================================================
    # From here, remaining archetypes get a MORE COMPACT bespoke pack.
    # Same structure, tighter content — still hand-authored per subject,
    # but not five-paragraph overviews.
    # ============================================================
    'safe-migration-runner': {
        'title': 'Safe Migration Runner',
        'iron_law': 'NO MIGRATION WITHOUT A REHEARSED ROLLBACK',
        'overview': {
            'iron_law':
                "An unreversible production migration has taken down more systems than "
                "any single other class of change.\n\n"
                "**Core principle:** if you can't cleanly reverse it, you can't safely "
                "run it in production.\n",
            'cycle':
                "Migrations are a loop of forward-and-back on staging until you've "
                "proven both directions work.\n",
            'practical':
                "This skill covers running production database migrations without "
                "downtime or data loss: rehearsing on production-shaped data, measuring "
                "lock duration, and coordinating with on-call before applying.\n",
            'checklist':
                "Migration safety is a checklist. Every skipped item is a way the "
                "migration can turn into an incident.\n",
        },
        'when_always': [
            "Any DDL change touching production data",
            "Any migration adding a NOT NULL column",
            "Any migration renaming or dropping columns",
            "Any migration that rewrites rows in bulk",
        ],
        'when_especially': [
            "Tables with millions of rows (locks scale with size)",
            "Tables read on the hot path",
            "Migrations that create or drop indexes",
        ],
        'when_dont_skip': [
            "\"It's just adding a nullable column\" — nullable columns still touch every row on some engines",
            "\"We did this in staging\" — staging doesn't have production data volume",
        ],
        'red_flags': [
            "No down-migration exists",
            "Migration hasn't been tested against production-size data",
            "Estimated lock duration is longer than your incident response time",
            "Deploy is scheduled outside on-call coverage",
            "Backup is older than the last write",
        ],
        'common_mistakes': [
            "Testing on empty tables and assuming behavior at scale",
            "Forgetting to increase statement_timeout for long-running DDL",
            "Running the migration and application deploy in the wrong order",
            "Assuming CREATE INDEX CONCURRENTLY on Postgres — it's not the default",
        ],
        'rationalizations': [
            "\"It's a small table\" — until it isn't, and you didn't check",
            "\"Rollback will be easy\" — has anyone actually run the down-migration?",
            "\"We'll do it during low-traffic hours\" — bugs don't care about traffic",
        ],
        'phases': [
            ("Rehearse", [
                "Clone production data into staging.",
                "Run the migration end-to-end.",
                "Measure lock duration and record it.",
            ]),
            ("Prepare rollback", [
                "Write the down-migration.",
                "Run it against a copy of the migrated staging DB.",
                "Confirm data returns to the pre-migration shape."]),
            ("Coordinate deploy", [
                "Notify on-call.",
                "Announce start in incident channel.",
                "Take a snapshot immediately before applying."]),
            ("Verify after apply", [
                "Confirm application traffic is unaffected.",
                "Sample-query the migrated data.",
                "Announce completion; document time-taken."]),
        ],
        'checklist': [
            "Down-migration exists and is tested",
            "Rehearsed on production-size staging data",
            "Lock duration measured and acceptable",
            "Snapshot taken immediately before apply",
            "On-call notified",
            "Post-apply verification queries prepared",
        ],
        'key_principles': [
            "The migration you can't rehearse is the migration you shouldn't run.",
            "Backups are only real if you've restored one this quarter.",
            "The rollback is a first-class artifact, not an afterthought.",
        ],
        'quick_reference':
            "1. Write the up-migration.\n"
            "2. Write the down-migration.\n"
            "3. Rehearse both against staging with production-shape data.\n"
            "4. Measure lock duration; abort if unacceptable.\n"
            "5. Notify on-call and take a fresh snapshot.\n"
            "6. Apply during a coverage window.\n"
            "7. Verify with sample queries.\n",
        'example':
            "### Scenario\n\n"
            "Adding a `phone_number` column to the `users` table (23M rows) with a "
            "NOT NULL constraint.\n\n"
            "### Applying this skill\n\n"
            "1. Naive approach: `ALTER TABLE users ADD COLUMN phone_number VARCHAR(20) NOT NULL DEFAULT '';` "
            "— rewrites every row, holds an exclusive lock for ~40 minutes at production size. Rejected.\n"
            "2. Multi-step approach:\n"
            "   - Migration 1: add column as nullable, default NULL.\n"
            "   - Deploy application code that writes phone_number for new rows.\n"
            "   - Backfill script chunked by primary key, 10k rows per batch.\n"
            "   - Migration 2: add NOT NULL constraint (fast validation of existing rows).\n"
            "3. Rehearse each step in staging with pg_dump-restored production data.\n"
            "4. Down-migrations: for step 1 drop the column; for step 2 drop the constraint.\n\n"
            "Total wall time: two weeks (deployed across multiple releases). Peak lock: <100ms.\n",
        'commands':
            "```bash\n"
            "# 1. Clone production to staging (safest: from a recent backup)\n"
            "pg_dump -h prod-replica -F c mydb | pg_restore -h staging -d mydb --clean\n\n"
            "# 2. Rehearse the up-migration and measure\n"
            "time psql -h staging -d mydb -f migrations/001_add_phone.up.sql\n\n"
            "# 3. Rehearse the down-migration\n"
            "time psql -h staging -d mydb -f migrations/001_add_phone.down.sql\n\n"
            "# 4. Snapshot before production apply\n"
            "aws rds create-db-snapshot --db-instance-identifier mydb-prod \\\n"
            "  --db-snapshot-identifier pre-migration-$(date +%Y%m%d-%H%M%S)\n"
            "```\n",
        'integration': [
            "Combine with `dependency-audit` if the migration is part of a library upgrade",
            "Use `on-call-handoff` if the migration spans a rotation",
        ],
    },

    # For remaining archetypes we keep a tighter bespoke pack.
    # (Each still has archetype-specific content in the fields that matter
    # most for realism — red_flags, common_mistakes, rationalizations,
    # example, and the practical-shape commands.)

    'dependency-audit': {
        'title': 'Dependency Audit',
        'iron_law': 'NO DEPENDENCY BUMP WITHOUT AN AUDIT',
        'overview': {
            'iron_law':
                "New dependencies inherit their entire transitive tree. Audit before "
                "merging, not after.\n\n"
                "**Core principle:** every added dependency is a decision to trust "
                "that library's maintainer chain. Trust is earned by evidence, not by popularity.\n",
            'cycle':
                "Audit is a loop: run the tools, read what they surface, decide what "
                "to accept, document the decision.\n",
            'practical':
                "This skill covers the concrete mechanics of auditing dependency "
                "updates: which tool per ecosystem, how to read the output, and how "
                "to distinguish blocking issues from accepted risks.\n",
            'checklist':
                "Dependency audit is a fixed checklist per ecosystem. Skip an item, "
                "invite a supply-chain incident.\n",
        },
        'when_always': [
            "Merging a Dependabot or Renovate PR",
            "Adding a new direct dependency",
            "Bumping a major version of any dependency",
        ],
        'when_especially': [
            "Dependencies with recent maintainer turnover",
            "Packages under 1M downloads/month (less community scrutiny)",
            "Packages that request unusual scopes (network, filesystem, env)",
        ],
        'when_dont_skip': [
            "\"It's just a patch bump\" — patch bumps have shipped malicious code before",
            "\"Renovate merged it already\" — Renovate doesn't audit for you",
        ],
        'red_flags': [
            "Audit tool reports CVEs and the PR was opened anyway",
            "Package's git repo doesn't match the registry entry",
            "Recent version bump with no changelog entry",
            "Author account created in the last 30 days for a critical dependency",
            "Postinstall script that fetches from a URL",
        ],
        'common_mistakes': [
            "Auditing only direct dependencies and not transitive ones",
            "Skimming `npm audit` output and missing High-severity items",
            "Trusting a green CI as evidence the update is safe",
            "Not reading the changelog of the bumped version",
        ],
        'rationalizations': [
            "\"The maintainers are trustworthy\" — trustworthy accounts get compromised",
            "\"It's just a devDependency\" — devDependencies run on your CI with your secrets",
            "\"npm audit is noisy\" — it's noisy, not wrong",
        ],
        'phases': [
            ("Run the audit tool", [
                "npm/pnpm: `npm audit --production`",
                "pip: `pip-audit`",
                "go: `govulncheck ./...`",
                "cargo: `cargo audit`"]),
            ("Read the diff of dependencies actually changing", [
                "For each bumped package: what version, what changelog?",
                "For each new transitive: is the package one you recognize?"]),
            ("Investigate each advisory", [
                "Is it exploitable in your usage?",
                "Is there a patched version available?",
                "If accepting risk: document why."]),
            ("Approve or block", [
                "Clean audit + read changelogs → approve.",
                "Advisories present → block until addressed or accepted with documentation."]),
        ],
        'checklist': [
            "Ecosystem audit tool ran (npm audit / pip-audit / govulncheck / cargo audit)",
            "Output has zero HIGH or CRITICAL advisories",
            "For each bumped package: changelog reviewed",
            "For each new transitive: package recognized or investigated",
            "Any accepted risks documented in the PR description",
        ],
        'key_principles': [
            "Every added dependency is a maintainer you now trust.",
            "\"Popular\" is not the same as \"secure\".",
            "The changelog is the shortest useful investigation.",
        ],
        'quick_reference':
            "1. Run the ecosystem audit tool.\n"
            "2. Read the diff of changed dependencies.\n"
            "3. For each bumped package, read the changelog.\n"
            "4. For each advisory, decide: patched, accepted, or blocked.\n"
            "5. Document accepted risks in the PR description.\n"
            "6. Approve only when audit is clean and diff is understood.\n",
        'example':
            "### Scenario\n\n"
            "Dependabot opens a PR bumping `lodash` from 4.17.20 to 4.17.21 and "
            "adds a new transitive `event-stream@3.3.6`.\n\n"
            "### Applying this skill\n\n"
            "1. Run `npm audit`. Reports 0 vulnerabilities.\n"
            "2. Read the diff of dependencies. lodash bump is a small patch — read "
            "the changelog, confirms it's a prototype-pollution fix.\n"
            "3. New transitive: `event-stream@3.3.6`. That's the version historically "
            "compromised in the flatmap-stream incident. Refuse to merge until the "
            "parent dependency that introduced it (`some-charting-lib`) is either "
            "updated to drop it, or replaced.\n\n"
            "Note: without step 3, this PR would have introduced a known-bad transitive.\n",
        'commands':
            "```bash\n"
            "# Per ecosystem\n"
            "npm audit --production       # Node\n"
            "pip-audit                    # Python\n"
            "govulncheck ./...            # Go\n"
            "cargo audit                  # Rust\n"
            "bundle audit                 # Ruby\n\n"
            "# Diff the lockfile in a PR to see what actually changed\n"
            "git diff origin/main -- package-lock.json | head -100\n\n"
            "# Read the changelog for a bumped package\n"
            "npm view lodash@4.17.21 --json | jq '.description, .homepage'\n"
            "```\n",
        'integration': [
            "Combine with `secrets-check` before every push",
            "Escalate to `incident-triage` if audit surfaces active exploitation",
        ],
    },

    # ============================================================
    'secrets-check': {
        'title': 'Secrets Check',
        'iron_law': 'NO PUSH WITH SECRETS IN THE DIFF',
        'overview': {
            'iron_law':
                "One leaked credential is a support ticket, an incident, and hours "
                "of rotation work — for every environment where that credential is "
                "trusted. Catch it before push.\n\n"
                "**Core principle:** the diff is the last checkpoint. After push, "
                "the secret is in the world.\n",
            'cycle':
                "Every commit is a chance to leak. Every push is the last chance "
                "to catch the leak.\n",
            'practical':
                "This skill covers scanning staged and committed changes for accidentally "
                "included secrets — API tokens, private keys, passwords, connection strings — "
                "with `gitleaks`/`trufflehog` and eyeball checks.\n",
            'checklist':
                "Secrets check is a fixed pre-push routine. It takes 30 seconds and "
                "prevents multi-hour incidents.\n",
        },
        'when_always': [
            "Before every `git push`",
            "After adding a new environment variable or config file",
            "After merging a large feature branch",
            "After resolving merge conflicts (conflicts hide additions)",
        ],
        'when_especially': [
            "PRs that add sample config files or `.env.example`",
            "PRs that add integration tests (integration tests love credentials)",
            "PRs merged from forks (external contributors don't know your patterns)",
        ],
        'when_dont_skip': [
            "\"It's a private repo\" — private repos leak via clones on personal machines",
            "\"I only committed the encrypted version\" — check anyway",
        ],
        'red_flags': [
            "String longer than 32 chars matching `[A-Za-z0-9+/=]` in a source file",
            "New file matching `*.pem`, `*.key`, `*.p12`, `credentials.*`, `.env`",
            "Any `AKIA`, `ghp_`, `gho_`, `sk-`, `xoxb-`, `xoxp-` prefix in a diff",
            "Environment variable being assigned from a string literal, not `os.environ.get`",
            "A `.gitignore` entry being removed alongside a new file that matches it",
        ],
        'common_mistakes': [
            "Trusting `.gitignore` retroactively — it doesn't untrack already-committed files",
            "Rotating the secret but forgetting to invalidate the leaked one",
            "Removing the secret from the file but not from git history",
            "Assuming private-repo means safe — clones, forks, and CI caches spread it",
        ],
        'rationalizations': [
            "\"It's just a dev credential\" — dev credentials get used to pivot to prod",
            "\"I'll rotate later\" — later is when the exploit happens",
            "\"No one will find it\" — bots scan the public GitHub firehose in real time",
            "\"It's already encrypted at rest\" — the encrypted form isn't the concern; the plaintext key is",
        ],
        'phases': [
            ("Scan staged changes", [
                "Run `gitleaks protect --staged` before every push.",
                "Read the output; every finding is a stop-the-line event."]),
            ("Investigate hits", [
                "For each finding: is it a real secret or a test fixture?",
                "Real secrets: rotate immediately, then remediate the commit."]),
            ("Remediate", [
                "Rewrite history to remove the secret (`git filter-repo` or BFG).",
                "Force-push only after all clones are aware.",
                "Rotate the credential regardless — history rewrite alone doesn't help."]),
            ("Prevent recurrence", [
                "Add a pre-commit hook running the scanner.",
                "Document the secret's rotation runbook.",
                "Consider a secrets manager if this is recurrent."]),
        ],
        'checklist': [
            "`gitleaks protect --staged` returns clean",
            "No new files matching secret filename patterns",
            "No high-entropy strings in the diff",
            "`.env` and equivalents are in `.gitignore`",
            "Pre-commit hook is installed",
        ],
        'key_principles': [
            "History rewrite alone is not enough — rotate too.",
            "Private ≠ safe.",
            "The scanner is faster than an incident.",
        ],
        'quick_reference':
            "1. `gitleaks protect --staged` (or equivalent).\n"
            "2. Read every finding.\n"
            "3. Real secret? — rotate immediately.\n"
            "4. Rewrite history to remove the leaked bytes.\n"
            "5. Confirm scanner is clean before push.\n",
        'example':
            "### Scenario\n\n"
            "You add integration tests that hit a third-party API. The tests pass "
            "locally with your personal token in `tests/fixtures/config.yaml`.\n\n"
            "### Applying this skill\n\n"
            "1. `gitleaks protect --staged` before push. Finds the API token.\n"
            "2. Realize you've already committed it to a local branch (not yet pushed).\n"
            "3. Rotate the token in the third-party service immediately.\n"
            "4. Use `git filter-repo --path tests/fixtures/config.yaml --invert-paths` "
            "to strip the file from history.\n"
            "5. Rewrite the test to source the token from `$INT_TEST_TOKEN`, gitignored.\n"
            "6. Confirm scanner is clean, then push.\n\n"
            "Total time: ~15 minutes. Cost of skipping: the token gets scraped from "
            "the public repo mirror within minutes, exploited within hours.\n",
        'commands':
            "```bash\n"
            "# Pre-push scan (fast, only staged)\n"
            "gitleaks protect --staged --verbose\n\n"
            "# Full-history scan (slow, but do this once per repo)\n"
            "gitleaks detect --source . --verbose\n\n"
            "# Alternative scanner\n"
            "trufflehog git file://. --only-verified\n\n"
            "# Remove a secret from history after leaking\n"
            "git filter-repo --path tests/fixtures/config.yaml --invert-paths\n\n"
            "# Install pre-commit hook\n"
            "cat > .git/hooks/pre-commit <<'EOF'\n"
            "#!/bin/sh\n"
            "gitleaks protect --staged --exit-code 1 || {\n"
            "  echo 'gitleaks found secrets — aborting commit'; exit 1; }\n"
            "EOF\n"
            "chmod +x .git/hooks/pre-commit\n"
            "```\n",
        'integration': [
            "Combine with `git-branch-hygiene` for pre-push routine",
            "Escalate to `incident-triage` if a secret has already been pushed",
        ],
    },

    # ============================================================
    'test-first-fix': {
        'title': 'Test-First Bug Fix',
        'iron_law': 'NO FIX WITHOUT A FAILING TEST FIRST',
        'overview': {
            'iron_law':
                "A bug you can't reproduce with a test isn't a bug you understand. "
                "A fix without a failing test is a guess dressed up as a solution.\n\n"
                "**Core principle:** if you didn't watch the test fail, you don't know "
                "if it tests the right thing.\n\n"
                "**Violating the letter of this process is violating the spirit of "
                "bug-fixing.**\n",
            'cycle':
                "Red-Green-Refactor for bug fixes: failing test that reproduces, "
                "minimal code change that fixes it, cleanup pass.\n",
            'practical':
                "This skill covers the mechanics of writing a bug-specific failing test "
                "before the fix, verifying it fails on `main`, then making it pass with "
                "the smallest possible change.\n",
            'checklist':
                "Bug fix as checklist: reproduce, write failing test, verify red, fix, "
                "verify green, commit both together.\n",
        },
        'when_always': [
            "Any bug reported by users, QA, or monitoring",
            "Any regression discovered while working on unrelated code",
            "Any \"flaky\" test — write a deterministic reproducer first",
        ],
        'when_especially': [
            "The bug is intermittent (reproducer proves you understand it)",
            "The bug is in a hot path (regression test prevents recurrence)",
            "You're under pressure to ship the fix quickly (a test is what makes fast safe)",
        ],
        'when_dont_skip': [
            "\"Obvious one-liner\" — one-liners are where regressions live",
            "\"It's a config change, not code\" — config bugs need regression coverage too",
        ],
        'red_flags': [
            "Fixing the code before writing the test",
            "\"Adapting\" the existing test to now pass",
            "Adding an `assert True` and calling it a test",
            "Skipping the \"verify test fails on main\" step",
            "Writing the test to match the fix instead of matching the bug",
        ],
        'common_mistakes': [
            "Writing a test that passes both with and without the fix",
            "Testing implementation detail rather than observable behavior",
            "Not verifying the test fails on `main` before writing the fix",
            "Fixing more than one thing in the same commit",
        ],
        'rationalizations': [
            "\"I'll add the test after\" — after is when you skip it",
            "\"The bug is too weird to test\" — weird bugs especially need reproducers",
            "\"The fix is obvious\" — write the test anyway; it takes 2 minutes",
        ],
        'phases': [
            ("Reproduce the bug", [
                "Reproduce locally with the exact steps from the report.",
                "If not reproducible, gather more data — do not proceed to a fix."]),
            ("Write the failing test", [
                "Write a test whose failure describes exactly this bug.",
                "Give the test a name that reads like the bug report.",
                "Run it against `main`. Confirm it fails, and fails for the right reason."]),
            ("Write the minimal fix", [
                "Change the minimum needed to make the test pass.",
                "Don't refactor while fixing — separate commit.",
                "Confirm the test now passes."]),
            ("Verify and commit", [
                "Run the entire test suite; confirm no regressions.",
                "Commit the test and fix together with a message referencing the bug ID."]),
        ],
        'checklist': [
            "Bug reproduced locally with exact steps",
            "Failing test written before any fix",
            "Test verified to fail on `main`",
            "Fix is minimal (no drive-by refactoring)",
            "Test now passes",
            "Full suite passes",
            "Test + fix committed together",
        ],
        'key_principles': [
            "The test is the proof you understood the bug.",
            "Write the test first — it's the only way to know it works.",
            "Minimal fix, then refactor separately.",
        ],
        'quick_reference':
            "1. Reproduce the bug locally.\n"
            "2. Write a failing test named after the bug.\n"
            "3. Verify test fails on `main`.\n"
            "4. Make the minimal fix.\n"
            "5. Verify test passes; run full suite.\n"
            "6. Commit test + fix together.\n",
        'example':
            "### Scenario\n\n"
            "Bug report: `formatDate('')` returns `'NaN-NaN-NaN'` instead of raising.\n\n"
            "### Applying this skill\n\n"
            "1. Reproduce in the REPL: `formatDate('')` → indeed returns `'NaN-NaN-NaN'`.\n"
            "2. Write the test:\n"
            "   ```python\n"
            "   def test_formatDate_raises_on_empty_string():\n"
            "       with pytest.raises(ValueError):\n"
            "           formatDate('')\n"
            "   ```\n"
            "3. Run against `main`: fails with `'NaN-NaN-NaN'` being returned. Correct failure.\n"
            "4. Fix: add an `if not date_str: raise ValueError(\"date_str must be non-empty\")` "
            "at the top of `formatDate`.\n"
            "5. Test passes. Full suite passes. Commit.\n\n"
            "Without step 3 (verify failure), you could have accidentally written a test "
            "that also passes on `main` — providing no actual coverage.\n",
        'commands':
            "```bash\n"
            "# Write the test and verify it fails on main\n"
            "git checkout main\n"
            "pytest tests/test_date_utils.py::test_formatDate_raises_on_empty_string\n"
            "# Should FAIL with the current buggy behavior\n\n"
            "# Now make your fix branch\n"
            "git checkout -b fix/format-date-empty-string\n"
            "# ... edit code ...\n"
            "pytest tests/test_date_utils.py::test_formatDate_raises_on_empty_string\n"
            "# Should PASS\n\n"
            "# Full suite check\n"
            "pytest\n\n"
            "# Commit test and fix together\n"
            "git add tests/test_date_utils.py src/date_utils.py\n"
            "git commit -m 'Fix formatDate on empty input (#1234)'\n"
            "```\n",
        'integration': [
            "Use `root-cause-first` to confirm you're fixing the actual cause",
            "Follow with `pr-description-writer` when opening the PR",
        ],
    },

    # ============================================================
    'pr-description-writer': {
        'title': 'PR Description Writer',
        'iron_law': 'NO PR WITHOUT A WHY IN THE FIRST PARAGRAPH',
        'overview': {
            'iron_law':
                "The reviewer's first 30 seconds decide whether they engage or skim. "
                "The description is what shapes those 30 seconds.\n\n"
                "**Core principle:** the description exists to reduce the reviewer's "
                "cognitive load. Every unclear PR wastes reviewer time (and worse, "
                "buries real problems in shallow reviews).\n",
            'cycle':
                "Draft, self-review, edit. Every PR description gets at least two passes.\n",
            'practical':
                "This skill covers the mechanics of writing a PR description reviewers "
                "actually read: one-sentence WHAT, one-sentence WHY, bullet list of "
                "behavior changes, migration notes.\n",
            'checklist':
                "A good PR description is a fixed structure. Fill in the blanks.\n",
        },
        'when_always': [
            "Opening any PR longer than one line",
            "Reopening a stalled PR",
            "Bundling multiple commits into a single PR",
        ],
        'when_especially': [
            "The PR touches critical-path code",
            "The change involves any migration or rollback consideration",
            "The PR requires a follow-up from another team",
        ],
        'when_dont_skip': [
            "\"It's obvious what this does\" — not to the reviewer at 4pm on Friday",
            "\"The commit messages say it\" — reviewers read the PR page, not `git log`",
        ],
        'red_flags': [
            "First line is \"cleanup\" or \"minor fixes\" without follow-up detail",
            "No linked issue",
            "\"See slack for context\" (Slack context ages out; PR description doesn't)",
            "\"Follow-up to previous PR\" without linking the previous PR",
            "Description is empty",
        ],
        'common_mistakes': [
            "Writing the description as diary of what you did, not what changed",
            "Describing implementation before behavior",
            "Burying breaking-change notices at the bottom",
            "Omitting migration notes",
        ],
        'rationalizations': [
            "\"They can read the code\" — reviewer capacity is not the point; direction is",
            "\"I don't have time\" — writing the description takes 3 minutes; a stalled PR takes days",
            "\"It's small\" — small PRs get skimmed most, description is more important not less",
        ],
        'phases': [
            ("State what changes", [
                "One sentence, imperative or declarative, at the top."]),
            ("State why", [
                "One sentence, linked to the issue.",
                "If it's a bug fix: what user impact does this address?",
                "If it's a feature: what does the user gain?"]),
            ("List behavior changes", [
                "Bullet list of user-observable differences.",
                "Flag any breaking changes at the top of the list."]),
            ("Note migration and rollback", [
                "Migration steps for consumers, if any.",
                "How would we roll back if this breaks production?"]),
        ],
        'checklist': [
            "First paragraph states WHAT and WHY",
            "Issue linked",
            "Behavior changes listed as bullets",
            "Breaking changes flagged (or explicitly \"none\")",
            "Screenshots for UI; before/after for performance",
            "Test plan section, if non-trivial",
        ],
        'key_principles': [
            "WHY first. Everything else supports the WHY.",
            "Write for the tired reviewer.",
            "The description outlives the PR — write it as documentation.",
        ],
        'quick_reference':
            "```\n"
            "## Summary\n"
            "One sentence: what changes.\n\n"
            "## Motivation\n"
            "One sentence: why. Fixes #1234.\n\n"
            "## Changes\n"
            "- Behavior change 1\n"
            "- Behavior change 2\n\n"
            "## Migration\n"
            "None required. / Steps: ...\n\n"
            "## Test plan\n"
            "- [ ] Verified locally\n"
            "- [ ] CI green\n"
            "- [ ] Regression test added\n"
            "```\n",
        'example':
            "### Bad description\n\n"
            "> Refactor auth module\n\n"
            "### Good description\n\n"
            "> **Summary.** Split `auth.py` into `auth/session.py` and `auth/tokens.py`.\n>\n"
            "> **Motivation.** Sessions and tokens have diverged in lifecycle "
            "requirements (#4821); mixing them in one module has caused four bugs in "
            "six months where token cleanup happened during session refresh.\n>\n"
            "> **Changes.**\n"
            "> - `Session` no longer imports `Token`. Consumers now import from "
            "`auth.session` or `auth.tokens` explicitly.\n"
            "> - `auth.py` retains a backwards-compat shim that re-exports both.\n>\n"
            "> **Migration.** New imports preferred, but no code change required in "
            "downstream services this release.\n",
        'commands':
            "```bash\n"
            "# Use the gh CLI with a HEREDOC to preserve markdown formatting\n"
            "gh pr create --title 'auth: split session and token modules' --body \"$(cat <<'EOF'\n"
            "## Summary\n"
            "Split auth.py into auth/session.py and auth/tokens.py.\n\n"
            "## Motivation\n"
            "Fixes #4821 — sessions and tokens have diverged in lifecycle requirements.\n\n"
            "## Changes\n"
            "- Session no longer imports Token\n"
            "- auth.py retains a backwards-compat shim\n\n"
            "## Migration\n"
            "None required this release.\n\n"
            "## Test plan\n"
            "- [x] Unit tests pass\n"
            "- [x] Verified downstream consumers still compile\n"
            "EOF\n"
            ")\"\n"
            "```\n",
        'integration': [
            "Follow with `requesting-code-review` to notify the right reviewers",
            "Combine with `commit-message-discipline` — good commits make good descriptions",
        ],
    },

    # ============================================================
    'commit-message-discipline': {
        'title': 'Commit Message Discipline',
        'iron_law': 'NO SINGLE-WORD COMMIT MESSAGES',
        'overview': {
            'iron_law':
                "A one-line \"fix\" commit is a debugging trap six months from now. "
                "You (or a colleague) will be reading `git log` under pressure — write "
                "for that future self.\n\n"
                "**Core principle:** the message is what makes the commit useful outside "
                "the moment it was written.\n",
            'cycle':
                "Every commit is a small cycle: subject, body, references. Skip a step "
                "and the commit becomes archaeology later.\n",
            'practical':
                "This skill covers the practical mechanics of writing commit messages: "
                "imperative subject ≤ 60 chars, blank line, body wrapped at 72 explaining "
                "WHY, references to issues.\n",
            'checklist':
                "Commit message discipline is a checklist per commit. Three items, "
                "takes 30 seconds, saves hours later.\n",
        },
        'when_always': [
            "Any commit destined for a branch that will be reviewed or merged",
            "Any commit on a shared branch (`main`, `develop`, release branches)",
            "Refactoring commits (especially — describe the WHY)",
        ],
        'when_especially': [
            "You're squashing multiple WIP commits (write the definitive message now)",
            "The change is subtle or counterintuitive",
            "The change reverts or contradicts a previous decision",
        ],
        'when_dont_skip': [
            "\"WIP\" commits — you'll forget what W stood for in a week",
            "\"trivial\" changes — trivial changes become mystery bugs",
        ],
        'red_flags': [
            "Commit message is a single word (`fix`, `wip`, `update`, `stuff`)",
            "Commit message is `.` or `...`",
            "Multi-file commit with a subject that describes only one file",
            "Subject line ends with a period",
            "Subject line is longer than 72 characters",
        ],
        'common_mistakes': [
            "Writing past tense (\"fixed X\") instead of imperative (\"fix X\")",
            "Explaining WHAT the diff shows instead of WHY the change was made",
            "Bundling unrelated changes in one commit",
            "No body when the change is non-obvious",
        ],
        'rationalizations': [
            "\"I'll rewrite the message on squash\" — you'll squash into one bad message",
            "\"The diff is self-explanatory\" — diffs don't explain motivation",
            "\"The PR description covers it\" — `git log` is read separately from PRs",
        ],
        'phases': [
            ("Write the subject", [
                "Imperative mood: \"Fix\", \"Add\", \"Rename\", not \"Fixed\" or \"Fixing\".",
                "≤ 60 characters (wraps well in terminals and web UIs).",
                "No trailing period."]),
            ("Write the body", [
                "Blank line after subject.",
                "Wrap at 72 characters.",
                "Explain WHY the change was made, not WHAT the diff shows.",
                "Mention any alternative approaches considered and rejected."]),
            ("Add references", [
                "`Fixes #1234` for issues that are resolved.",
                "`Refs #5678` for issues that are related but not resolved.",
                "`Co-authored-by:` for pair-programming credit."]),
            ("Review the message", [
                "Re-read as if you're a future colleague debugging.",
                "Does the message answer \"why does this commit exist?\""]),
        ],
        'checklist': [
            "Subject is imperative mood",
            "Subject ≤ 60 chars, no trailing period",
            "Body wrapped at 72",
            "Body explains WHY, not just WHAT",
            "Related issues referenced",
        ],
        'key_principles': [
            "The subject is a headline. The body is the article.",
            "Imperative mood — the commit does something, it isn't a diary entry.",
            "Future-you is the audience.",
        ],
        'quick_reference':
            "```\n"
            "Fix off-by-one in pagination cursor decoding\n\n"
            "The cursor was decoded with base64.urlsafe_b64decode which\n"
            "silently ignores trailing '=' padding. For 20-char cursors this\n"
            "produced valid-looking but wrong offsets, resulting in duplicate\n"
            "items across page boundaries.\n\n"
            "Rejected: fixing padding on encode side (would break existing\n"
            "cursors already in flight). Instead we pad on decode.\n\n"
            "Fixes #3812\n"
            "```\n",
        'example':
            "### Bad\n\n"
            "```\n"
            "fix\n"
            "```\n\n"
            "### Also bad\n\n"
            "```\n"
            "Fixed the pagination bug that Sarah reported yesterday.\n"
            "```\n\n"
            "### Good\n\n"
            "```\n"
            "Fix off-by-one in pagination cursor decoding\n\n"
            "urlsafe_b64decode silently accepts unpadded input, producing wrong\n"
            "byte offsets for 20-char cursors. This caused duplicate items to\n"
            "appear at page boundaries.\n\n"
            "Fixes #3812\n"
            "```\n\n"
            "The good version tells future-you what problem was solved, why the "
            "chosen approach, and what to search for if it comes back.\n",
        'commands':
            "```bash\n"
            "# Use a HEREDOC for multi-line messages\n"
            "git commit -m \"$(cat <<'EOF'\n"
            "Fix off-by-one in pagination cursor decoding\n\n"
            "urlsafe_b64decode silently accepts unpadded input, producing\n"
            "wrong byte offsets for 20-char cursors.\n\n"
            "Fixes #3812\n"
            "EOF\n"
            ")\"\n\n"
            "# Rewrite the last message if you botched it (before push)\n"
            "git commit --amend\n\n"
            "# Rewrite older messages in an interactive rebase (before push)\n"
            "git rebase -i HEAD~5\n"
            "```\n",
        'integration': [
            "Follow with `pr-description-writer` — good commits make good PRs",
            "Combine with `git-branch-hygiene` when squash-merging",
        ],
    },

    # ============================================================
    'log-triage': {
        'title': 'Log Triage',
        'iron_law': 'NEVER SCROLL A LARGE LOG LINE-BY-LINE ON YOUR FIRST PASS',
        'overview': {
            'iron_law':
                "Wading through 10,000 lines line-by-line is a waste. Look for structure "
                "first, then read carefully around what you find.\n\n"
                "**Core principle:** logs are queryable data. Treat them as such.\n",
            'cycle':
                "Triage is a loop of narrowing filters: severity → time → subsystem → "
                "specific request. Each pass reduces the corpus by 10-100x.\n",
            'practical':
                "This skill covers the practical mechanics of log triage: identifying "
                "the earliest error, correlating request IDs, and finding the causal "
                "chain rather than the symptomatic tail.\n",
            'checklist':
                "Log triage is a fixed pattern. Grep for ERROR first, note the earliest "
                "timestamp, follow the trace ID.\n",
        },
        'when_always': [
            "After a production incident",
            "When CI fails with unclear output",
            "When a customer reports an issue with logs attached",
            "When triaging monitoring alerts",
        ],
        'when_especially': [
            "The log is over 1000 lines",
            "The log spans multiple services",
            "The failure appears intermittent",
        ],
        'when_dont_skip': [
            "\"I'll just scroll to the bottom\" — the last error is usually a consequence, not a cause",
            "\"The dashboard shows the answer\" — dashboards summarize; raw logs disambiguate",
        ],
        'red_flags': [
            "Skipping past ERRORs to look at INFO",
            "Reading only the last 50 lines when the log is 5000",
            "Trusting the first ERROR timestamp without checking for earlier ones from the same request",
            "Not correlating the request ID / trace ID across service boundaries",
        ],
        'common_mistakes': [
            "Confusing an effect ERROR for the cause (e.g. `ConnectionReset` after the underlying service already died)",
            "Reading the log for the failing request without also reading the log for the last successful request",
            "Not filtering out unrelated noise before reading (health-check pings, etc.)",
        ],
        'rationalizations': [
            "\"The log is small enough to eyeball\" — eyeballing misses causal patterns",
            "\"I know what to look for\" — you know what you *expect*; the log knows what happened",
        ],
        'phases': [
            ("Grep for high-severity lines", [
                "`grep -E 'ERROR|FATAL|panic|Traceback|assertion'` first.",
                "Note the earliest such line and its timestamp."]),
            ("Follow the trace ID", [
                "Extract the request/trace/correlation ID from the earliest error.",
                "Grep for that ID across the log; read the full sequence, in order."]),
            ("Read the surrounding context", [
                "Only after locating the causal event, read the 20 lines before and after.",
                "Look for the config/state change that preceded the error."]),
            ("Cross-correlate services", [
                "If the log spans multiple services, gather the trace-ID logs from each.",
                "Read them in timestamp order across services."]),
        ],
        'checklist': [
            "Ran `grep -E 'ERROR|FATAL|panic|Traceback'` first",
            "Noted the earliest error timestamp",
            "Extracted request/trace ID",
            "Followed the ID through the log",
            "Cross-correlated across services (if applicable)",
        ],
        'key_principles': [
            "The earliest ERROR is usually more informative than the loudest one.",
            "Follow the trace, not the noise.",
            "Filter first, read second.",
        ],
        'quick_reference':
            "```bash\n"
            "# Step 1: high-severity only, earliest first\n"
            "grep -nE 'ERROR|FATAL|panic|Traceback' service.log | head -20\n\n"
            "# Step 2: extract trace ID (adjust regex to your format)\n"
            "grep -nE 'ERROR' service.log | head -1 | grep -oE 'trace[_-]?id[=:] *[a-f0-9-]+'\n\n"
            "# Step 3: follow that trace across the file\n"
            "grep '<trace-id>' service.log | less\n"
            "```\n",
        'example':
            "### Scenario\n\n"
            "6000-line web-server log, users report intermittent 500s in the last hour.\n\n"
            "### Applying this skill\n\n"
            "1. `grep -nE 'ERROR|500' access.log | head` — first ERROR is at 14:32:07, "
            "line 2841.\n"
            "2. That line has `req_id=abc123`. Grep for `abc123` — get 8 lines from "
            "14:32:04 to 14:32:07 showing the request handler entered, hit the DB, "
            "DB call took 30s, timeout fired, 500 returned.\n"
            "3. Read lines 2820–2860 for context: the log shows a burst of similar "
            "long DB calls starting at 14:31:55.\n"
            "4. Cross-correlate: DB service log at 14:31:55 shows a vacuum job started. "
            "Root cause: unindexed table + vacuum caused a lock storm.\n\n"
            "Without step 1 (start with ERROR grep), you'd have scrolled through 2800 "
            "lines of noise. Without step 2 (trace ID), you'd have missed that all 500s "
            "share a common trigger event.\n",
        'commands':
            "```bash\n"
            "# Fast triage recipe\n"
            "LOG=service.log\n\n"
            "# 1. High-severity lines with line numbers\n"
            "grep -nE 'ERROR|FATAL|panic|Traceback|Killed|OOM|assertion' \"$LOG\" | head -20\n\n"
            "# 2. Extract trace/request IDs from those\n"
            "grep -nE 'ERROR' \"$LOG\" | head -5 | \\\n"
            "    grep -oE '(trace|req)[_-]?id[=:][^ ,]*'\n\n"
            "# 3. Timeline for one trace ID\n"
            "grep 'abc123' \"$LOG\" | sort -k1,1  # if timestamped\n\n"
            "# 4. Count errors by minute to spot bursts\n"
            "grep 'ERROR' \"$LOG\" | awk '{print substr($1,1,16)}' | uniq -c\n\n"
            "# 5. Cross-service: if you have multiple log files\n"
            "grep -h 'abc123' service-*.log | sort\n"
            "```\n",
        'integration': [
            "Follow with `root-cause-first` once you've identified the causal event",
            "Escalate to `incident-triage` if the pattern indicates production impact",
        ],
    },

    # ============================================================
    'incident-triage': {
        'title': 'Incident Triage',
        'iron_law': 'NO PAGE WITHOUT SIZING THE BLAST RADIUS FIRST',
        'overview': {
            'iron_law':
                "Paging people at 3am for a non-incident destroys trust in the alerting "
                "system. Sitting on a real Sev1 to \"investigate a bit more\" destroys "
                "the business. Neither is acceptable — size the blast radius before "
                "deciding.\n\n"
                "**Core principle:** the first ten minutes are about scope, not fix.\n",
            'cycle':
                "Triage is a rapid loop: observe → hypothesize scope → verify scope → "
                "decide page severity → repeat if scope changes.\n",
            'practical':
                "This skill covers the first-hour mechanics of an incident: sizing "
                "impact, deciding severity, opening an incident channel, and paging "
                "the right people.\n",
            'checklist':
                "Incident triage is a checklist executed under time pressure. Print it, "
                "pin it, follow it.\n",
        },
        'when_always': [
            "An alert fires that you don't immediately recognize as false-positive",
            "A customer reports a problem that affects their production usage",
            "You observe a metric that indicates user-facing impact",
        ],
        'when_especially': [
            "Multiple related alerts fire within a short window",
            "The impact is in a critical customer segment (paying tier, healthcare, finance)",
            "The issue coincides with a recent deploy",
        ],
        'when_dont_skip': [
            "\"It's probably nothing\" — probably isn't good enough at 3am",
            "\"I'll investigate quietly first\" — silent triage risks blowing SLA before anyone knows",
        ],
        'red_flags': [
            "Investigating alone for more than 15 minutes without opening a channel",
            "Silencing an alert without documenting why",
            "Not paging on-call because \"they're probably asleep\"",
            "Declaring incident RESOLVED before the fix has been verified in production",
            "Not communicating status while working",
        ],
        'common_mistakes': [
            "Sizing blast radius from dashboards alone (dashboards lag, or aggregate too coarsely)",
            "Assuming the alert that fired first is the primary cause",
            "Not disambiguating \"error rate up\" from \"traffic down\"",
            "Closing the incident before writing down what happened",
        ],
        'rationalizations': [
            "\"I can fix this before anyone notices\" — customers noticed before you did",
            "\"It's Friday, let's not disrupt weekend plans\" — bugs don't respect calendars",
            "\"We'll do the postmortem later\" — later never comes for triaged-but-forgotten incidents",
        ],
        'phases': [
            ("Confirm real impact", [
                "Check the customer-facing metric directly (not just the alert).",
                "Try the user flow yourself.",
                "Confirm the alert isn't a known false positive."]),
            ("Size the blast radius", [
                "How many users affected? All? A segment? A single tenant?",
                "How severe is the impact per user? Degradation vs total failure?",
                "Is data at risk (corruption, loss) vs just availability?"]),
            ("Decide severity and page", [
                "Sev1: broad impact + data at risk → page everyone including leadership.",
                "Sev2: broad impact, no data risk → page on-call + engineering manager.",
                "Sev3: narrow impact → page on-call only.",
                "If in doubt, page one level higher."]),
            ("Open the incident channel", [
                "Post to the incident channel with severity, symptom, blast radius.",
                "Assign an Incident Commander (can be yourself).",
                "Post updates every 30 minutes minimum."]),
        ],
        'checklist': [
            "Verified real impact (not a false alarm)",
            "Sized blast radius (users, severity, data risk)",
            "Chose severity level",
            "Paged appropriate on-call",
            "Opened incident channel",
            "Assigned Incident Commander",
            "First status update posted",
        ],
        'key_principles': [
            "Size before fix.",
            "When in doubt, page up, not down.",
            "Communicate while working, not after.",
        ],
        'quick_reference':
            "**First 5 minutes:**\n"
            "1. Confirm the impact is real.\n"
            "2. Estimate blast radius.\n"
            "3. Pick severity.\n\n"
            "**Next 10 minutes:**\n"
            "4. Page on-call.\n"
            "5. Open incident channel.\n"
            "6. Post first status.\n\n"
            "**Then repeat every 30 min:**\n"
            "7. Status update.\n"
            "8. Re-size blast radius (may have changed).\n",
        'example':
            "### Scenario\n\n"
            "3:14am. Alert: `checkout_error_rate > 5%`. You're on-call.\n\n"
            "### Applying this skill\n\n"
            "1. Confirm: hit `checkout.example.com` yourself — 500 error. Real.\n"
            "2. Blast radius: `checkout_error_rate` is at 47% and climbing. That's "
            "every checkout attempt failing. Revenue impact per minute is calculable "
            "from `checkout_attempts * average_order_value`.\n"
            "3. Severity: revenue impact + broad → Sev1.\n"
            "4. Page: on-call SRE, on-call engineer for checkout service, engineering "
            "manager. Include leadership per Sev1 policy.\n"
            "5. Open `#incident-2026-07-15-checkout` channel; assign yourself as IC "
            "until someone else is awake enough to take it.\n"
            "6. First status: \"Checkout is failing at 47%. Investigating. Impact: "
            "no checkouts succeeding since 3:08am. IC: @you.\"\n\n"
            "Total elapsed: 8 minutes. Now the fix work can start with the right "
            "people watching.\n",
        'commands':
            "```bash\n"
            "# Check the customer-facing metric directly\n"
            "curl -w '%{http_code}\\n' https://checkout.example.com/api/health\n\n"
            "# Size impact from logs\n"
            "kubectl logs -n prod deployment/checkout --since=15m | \\\n"
            "    grep -c 'status=5'\n\n"
            "# Recent deploys? (correlate)\n"
            "gh api /repos/$ORG/$REPO/deployments \\\n"
            "    --paginate | jq '.[] | select(.created_at > \"2026-07-15T03:00\")'\n\n"
            "# Open the incident channel and page (adapt to your tooling)\n"
            "slack incident create --severity 1 --summary 'Checkout failing 47%'\n"
            "pagerduty trigger --service checkout --severity critical\n"
            "```\n",
        'integration': [
            "Follow with `root-cause-first` once triage stabilizes",
            "Follow with `runbook-writer` after incident closes",
        ],
    },

    # ============================================================
    'git-branch-hygiene': {
        'title': 'Git Branch Hygiene',
        'iron_law': 'NO MERGE COMMITS ON FEATURE BRANCHES',
        'overview': {
            'iron_law':
                "Consistent branch naming and rebase discipline reduce merge conflicts, "
                "keep git history readable, and make bisect useful.\n\n"
                "**Core principle:** treat the branch history like commit history — it "
                "should read like a story, not a bowl of spaghetti.\n",
            'cycle':
                "Every branch is a small cycle: name, work, rebase, review, merge, delete.\n",
            'practical':
                "This skill covers the mechanics of branch naming, keeping branches "
                "rebased on main, cleaning up local branches after merge, and handling "
                "rebase conflicts.\n",
            'checklist':
                "Branch hygiene is a fixed pre-PR routine. Six items, takes a minute.\n",
        },
        'when_always': [
            "Creating a new feature or bugfix branch",
            "Preparing an existing branch for review",
            "Cleaning up local branches after merge",
            "Rebasing when your PR is stale relative to main",
        ],
        'when_especially': [
            "The branch is more than a week old",
            "The base branch has moved significantly",
            "You've noticed conflicts starting to appear on the PR",
        ],
        'when_dont_skip': [
            "\"I'll just merge main into my branch\" — creates the exact merge-commit noise this skill prevents",
        ],
        'red_flags': [
            "Branch named `wip`, `test`, `foo`, or `damon-branch`",
            "Merge commits from main appearing in your feature branch",
            "Local branch list shows branches merged months ago",
            "Force-pushing to a branch someone else is collaborating on without warning",
        ],
        'common_mistakes': [
            "Rebasing after review has started (invalidates reviewer's in-progress reading)",
            "Force-pushing to `main` (should never happen; branch protection should prevent)",
            "Deleting a branch before confirming the PR merged (via CI)",
        ],
        'rationalizations': [
            "\"Merge commits show the history\" — they show noise, not history",
            "\"Rebasing is dangerous\" — only if unsupervised; use `--force-with-lease`",
        ],
        'phases': [
            ("Name the branch", [
                "Format: `<type>/<slug>` where type ∈ {feat, fix, chore, docs, refactor, test}.",
                "Slug is short-kebab-case describing the change."]),
            ("Work in small commits", [
                "Frequent commits with meaningful messages.",
                "Squash later if desired, but not while working."]),
            ("Rebase before opening a PR", [
                "`git fetch origin && git rebase origin/main`.",
                "Resolve any conflicts; do not create merge commits."]),
            ("Clean up after merge", [
                "Delete the local branch: `git branch -d <name>`.",
                "Prune remote tracking branches: `git fetch --prune`."]),
        ],
        'checklist': [
            "Branch name matches `<type>/<slug>` pattern",
            "Rebased onto `origin/main` (or equivalent base)",
            "No merge commits in the branch",
            "Commits pass linter / test locally",
            "After merge: local branch deleted",
        ],
        'key_principles': [
            "Rebase, don't merge, when catching up.",
            "Delete branches after merge — floating branches are technical debt.",
            "Force-push with `--force-with-lease`, never plain `--force`.",
        ],
        'quick_reference':
            "```bash\n"
            "# Create a well-named branch\n"
            "git checkout -b feat/add-webhook-retries\n\n"
            "# Keep it rebased\n"
            "git fetch origin\n"
            "git rebase origin/main\n\n"
            "# Push with lease (safer than --force)\n"
            "git push --force-with-lease\n\n"
            "# Cleanup after merge\n"
            "git checkout main && git pull\n"
            "git branch -d feat/add-webhook-retries\n"
            "git fetch --prune\n"
            "```\n",
        'example':
            "### Bad\n\n"
            "```bash\n"
            "git checkout -b wip                          # bad name\n"
            "# ... work ...\n"
            "git merge main                               # creates merge commit\n"
            "git push -f                                  # unsafe force push\n"
            "```\n\n"
            "### Good\n\n"
            "```bash\n"
            "git checkout -b fix/pagination-off-by-one    # descriptive name\n"
            "# ... work ...\n"
            "git fetch origin\n"
            "git rebase origin/main                       # linear history\n"
            "git push --force-with-lease                  # safe force push\n"
            "```\n",
        'commands':
            "```bash\n"
            "# List branches merged into main (candidates for deletion)\n"
            "git branch --merged main | grep -v '^\\*\\| main$'\n\n"
            "# Delete all merged branches at once\n"
            "git branch --merged main | grep -v '^\\*\\| main$' | xargs -n1 git branch -d\n\n"
            "# Recover a branch you accidentally deleted (within reflog window)\n"
            "git reflog | grep '<branch-name>'\n"
            "git checkout -b <branch-name> <sha-from-reflog>\n\n"
            "# See what you'd force-push before you do it\n"
            "git log --oneline origin/<branch>..HEAD  # commits you'd push\n"
            "git log --oneline HEAD..origin/<branch>  # commits you'd overwrite (should be zero)\n"
            "```\n",
        'integration': [
            "Combine with `commit-message-discipline` on every commit",
            "Follow with `pr-description-writer` when opening the PR",
        ],
    },

    # ============================================================
    'runbook-writer': {
        'title': 'Runbook Writer',
        'iron_law': 'NO INCIDENT CLOSED WITHOUT A RUNBOOK ENTRY',
        'overview': {
            'iron_law':
                "The next on-call is you in six months, having forgotten everything. "
                "Write the runbook now, while the fix is fresh.\n\n"
                "**Core principle:** every incident produces at least one artifact — "
                "either a runbook entry or a permanent fix. \"Never happened before\" "
                "is not a valid closure reason.\n",
            'cycle':
                "Incident → fix → runbook → next-on-call succeeds → runbook improves.\n",
            'practical':
                "This skill covers writing runbook entries that are actually usable: "
                "symptom-first titles, copy-pasteable commands, decision trees, and "
                "escalation paths.\n",
            'checklist':
                "A good runbook entry has a fixed shape. Fill it in before closing "
                "the incident.\n",
        },
        'when_always': [
            "After any Sev1 or Sev2 incident",
            "After any customer-reported issue that took >2 hours to diagnose",
            "After any issue where the fix wasn't obvious",
            "After discovering a recurring class of failure",
        ],
        'when_especially': [
            "The fix required cross-team coordination",
            "The root cause was in an area rarely touched",
            "The next-on-call rotation is different people",
        ],
        'when_dont_skip': [
            "\"It's a one-off\" — one-offs recur; assume they will",
            "\"It's obvious\" — obvious to you now, mysterious in six months",
        ],
        'red_flags': [
            "Runbook entry says only \"see #incident-123\" (Slack ages out)",
            "Commands are non-copy-pasteable (contain placeholders like `<your-cluster>`)",
            "No decision tree — reader has to read prose to figure out branches",
            "Escalation path missing",
        ],
        'common_mistakes': [
            "Writing the runbook in Slack rather than the runbook repo",
            "Writing narrative prose instead of copy-pasteable commands",
            "Assuming the reader has the same context you had at 3am",
            "Not linking the runbook from the alert that would trigger it",
        ],
        'rationalizations': [
            "\"I'll write it later\" — you'll forget the details by tomorrow",
            "\"The postmortem covers it\" — postmortems are one-time reads, runbooks are recurring",
        ],
        'phases': [
            ("Capture the symptom", [
                "One-sentence description of what an on-call would observe.",
                "Match the alert text if applicable, so grep from the alert lands here."]),
            ("Capture the diagnosis", [
                "The one or two commands that will confirm the diagnosis.",
                "Distinguish this cause from other causes with similar symptoms."]),
            ("Capture the fix", [
                "Copy-pasteable commands, with all variables labeled.",
                "Note any preconditions (permissions, environment)."]),
            ("Capture the escalation", [
                "Who to page if the fix doesn't work.",
                "Link to the postmortem for context."]),
        ],
        'checklist': [
            "Title starts with the symptom",
            "Diagnosis commands are copy-pasteable",
            "Fix commands are copy-pasteable",
            "Escalation path is documented",
            "Runbook is linked from the corresponding alert",
        ],
        'key_principles': [
            "Symptom-first titles (that's what on-call searches for).",
            "Commands, not prose.",
            "Written for a tired stranger.",
        ],
        'quick_reference':
            "```markdown\n"
            "# Symptom\n"
            "<what the on-call sees / what the alert says>\n\n"
            "# Diagnose\n"
            "```bash\n"
            "<one or two commands to confirm it's this cause>\n"
            "```\n\n"
            "# Fix\n"
            "```bash\n"
            "<copy-pasteable commands>\n"
            "```\n\n"
            "# Escalate\n"
            "If the above doesn't resolve within 15min, page <team>.\n"
            "Related postmortem: <link>\n"
            "```\n",
        'example':
            "### Runbook: checkout error rate > 5%\n\n"
            "**Symptom.** `checkout_error_rate` alert firing; customers unable to complete purchase.\n\n"
            "**Diagnose.**\n"
            "```bash\n"
            "kubectl logs -n prod deployment/checkout --tail=200 | grep ERROR | head\n"
            "```\n"
            "If errors mention `pricing-service timeout`, this runbook applies.\n\n"
            "**Fix.**\n"
            "```bash\n"
            "# 1. Confirm pricing-service is unhealthy\n"
            "kubectl get pods -n prod -l app=pricing-service\n\n"
            "# 2. If pods are OOMKilled, bump replica count temporarily\n"
            "kubectl scale -n prod deployment/pricing-service --replicas=6\n\n"
            "# 3. Watch error rate drop within 2 min\n"
            "watch -n 5 'curl -s https://checkout.example.com/api/health'\n"
            "```\n\n"
            "**Escalate.** If replicas > 8 and errors persist, page @pricing-team.\n"
            "Postmortem: [2026-07-15 checkout incident](../postmortems/2026-07-15.md)\n",
        'commands':
            "```bash\n"
            "# Location: put runbooks in one discoverable directory\n"
            "runbooks/\n"
            "├── README.md                       # index by symptom\n"
            "├── checkout-error-rate.md\n"
            "├── database-cpu-spike.md\n"
            "└── auth-token-issuance-failing.md\n\n"
            "# Link from alerts\n"
            "# In your monitoring config:\n"
            "#   runbook_url: https://github.com/org/runbooks/blob/main/checkout-error-rate.md\n\n"
            "# Test that runbooks are still current\n"
            "# Quarterly: pick a random runbook, follow it verbatim on staging.\n"
            "```\n",
        'integration': [
            "Trigger from `incident-triage` when closing the incident",
            "Combine with `backup-restore-drill` for backup-related runbooks",
        ],
    },

    # ============================================================
    'k8s-manifest-checker': {
        'title': 'Kubernetes Manifest Checker',
        'iron_law': 'NO MANIFEST APPLIED WITHOUT RESOURCE LIMITS AND HEALTH CHECKS',
        'overview': {
            'iron_law':
                "A container without resource limits is a noisy neighbor waiting to "
                "happen. A container without health checks is invisible when it's "
                "silently degraded.\n\n"
                "**Core principle:** the cluster protects itself from applications "
                "only if applications tell it how.\n",
            'cycle':
                "Iterate: apply to staging, watch behavior, adjust limits, repeat.\n",
            'practical':
                "This skill covers validating Kubernetes manifests against a fixed set "
                "of best-practice checks before applying: resource limits, liveness/"
                "readiness probes, image tags, security contexts, and labels.\n",
            'checklist':
                "Manifest validation is a fixed checklist. If any check fails, the "
                "apply is blocked until fixed.\n",
        },
        'when_always': [
            "Any manifest going to production",
            "Any Helm chart being installed for the first time",
            "Any change to an existing production Deployment / StatefulSet",
        ],
        'when_especially': [
            "New service being introduced",
            "Manifest was copy-pasted from another service",
            "Chart values change resource requests significantly",
        ],
        'when_dont_skip': [
            "\"It's a small service\" — small services in aggregate can starve a node",
            "\"Staging doesn't matter\" — staging misconfigurations hide production misconfigurations",
        ],
        'red_flags': [
            "`image: <name>:latest` — no version pinning",
            "No `resources.limits.memory` on a pod",
            "No `livenessProbe` or `readinessProbe`",
            "`securityContext.privileged: true`",
            "`hostNetwork: true` without explicit justification",
            "No pod-level labels for owner/team/service",
        ],
        'common_mistakes': [
            "Setting `resources.requests` but not `resources.limits` (still allows OOM)",
            "Using the same probe for liveness and readiness (they have different failure semantics)",
            "Mounting `secrets` as env vars (visible in `kubectl describe`)",
            "Not setting `revisionHistoryLimit` (Deployment history grows unboundedly)",
        ],
        'rationalizations': [
            "\"HPA will scale us up\" — HPA only helps if pods actually crash gracefully",
            "\"The default probe is fine\" — there is no default probe; there's no probe",
            "\"We'll add limits later\" — later is when the noisy-neighbor incident happens",
        ],
        'phases': [
            ("Static checks", [
                "Run `kubeval` or `kubeconform` for schema validation.",
                "Run `polaris audit` or `kube-linter` for best-practice checks.",
                "Fix everything they flag before proceeding."]),
            ("Manual review of resource requests/limits", [
                "Confirm both `requests` and `limits` are set for CPU and memory.",
                "Check the ratio: high requests waste; high limits without requests risk OOM."]),
            ("Manual review of probes", [
                "Confirm `livenessProbe` restarts on unresponsive.",
                "Confirm `readinessProbe` removes from load balancer on unready.",
                "They should not be the same endpoint."]),
            ("Apply to staging", [
                "Watch `kubectl get events` for 10 minutes.",
                "Load-test if possible.",
                "Only then apply to production."]),
        ],
        'checklist': [
            "Image tag is pinned (not `latest`)",
            "`resources.requests` and `resources.limits` set for CPU and memory",
            "`livenessProbe` defined and distinct from `readinessProbe`",
            "`securityContext` runs as non-root",
            "No `privileged: true` unless justified",
            "Standard team/service/owner labels present",
        ],
        'key_principles': [
            "Pin images, always.",
            "Requests and limits both, always.",
            "Two probes, not one.",
        ],
        'quick_reference':
            "**Required in every Deployment:**\n"
            "```yaml\n"
            "spec:\n"
            "  template:\n"
            "    spec:\n"
            "      containers:\n"
            "      - name: app\n"
            "        image: myrepo/app:v1.2.3   # pinned, not :latest\n"
            "        resources:\n"
            "          requests: { cpu: 100m, memory: 256Mi }\n"
            "          limits:   { cpu: 500m, memory: 512Mi }\n"
            "        livenessProbe:\n"
            "          httpGet: { path: /healthz, port: 8080 }\n"
            "          initialDelaySeconds: 30\n"
            "        readinessProbe:\n"
            "          httpGet: { path: /ready, port: 8080 }\n"
            "          initialDelaySeconds: 5\n"
            "        securityContext:\n"
            "          runAsNonRoot: true\n"
            "```\n",
        'example':
            "### Scenario\n\n"
            "A junior engineer submits a PR adding a new `worker` Deployment. Manifest "
            "is 20 lines, looks reasonable at a glance.\n\n"
            "### Applying this skill\n\n"
            "1. Run `kubeconform`: schema-valid.\n"
            "2. Run `kube-linter`: 3 findings.\n"
            "   - `image: worker:latest` — flag.\n"
            "   - No `livenessProbe` — flag.\n"
            "   - No memory limit — flag.\n"
            "3. Comment on the PR with the three findings and a link to the runbook.\n"
            "4. Author fixes; you re-review and approve.\n\n"
            "Without the check, one crashing worker pod could OOM the node, taking "
            "down the co-tenant services. Ten-minute check prevents multi-hour incident.\n",
        'commands':
            "```bash\n"
            "# Schema validation (fast, catches YAML mistakes)\n"
            "kubeconform -strict -summary manifests/*.yaml\n\n"
            "# Best-practice linting\n"
            "kube-linter lint manifests/\n"
            "# or\n"
            "polaris audit --audit-path manifests/ --format=pretty\n\n"
            "# Server-side dry-run (checks against actual cluster policy)\n"
            "kubectl apply --dry-run=server -f manifests/\n\n"
            "# Diff against current cluster state\n"
            "kubectl diff -f manifests/\n"
            "```\n",
        'integration': [
            "Follow with `dependency-audit` for image-based vulnerabilities",
            "Escalate to `incident-triage` if a bad manifest reached production",
        ],
    },

    # ============================================================
    'release-verification': {
        'title': 'Release Verification',
        'iron_law': 'NO RELEASE WITHOUT A REHEARSED VERIFICATION PLAN',
        'overview': {
            'iron_law':
                "A release is a promise to users that the new version is at least "
                "as good as the old one. Verification is how you keep the promise.\n\n"
                "**Core principle:** hope is not a verification strategy. Every "
                "release goes through the same fixed checks before it ships.\n",
            'cycle':
                "Verification is a loop: run the check, read the output, decide "
                "go/no-go. Skip any step and the release is a gamble.\n",
            'practical':
                "This skill covers the pre-flight checks for any release: version "
                "correctness, changelog present, migration compatibility, smoke tests "
                "against a release candidate, and the rollback plan.\n",
            'checklist':
                "Release verification is a fixed checklist. Every skipped item is "
                "a way the release can become an incident.\n",
        },
        'when_always': [
            "Publishing any tagged version",
            "Cutting a release branch",
            "Pushing an image tag downstream services will pull",
        ],
        'when_especially': [
            "Major version releases (breaking-change surface)",
            "First release after a large refactor",
            "Releases containing schema migrations",
        ],
        'when_dont_skip': [
            "\"It's a patch release\" — patch releases have shipped incompatibilities before",
            "\"We tested in staging\" — verification is what confirms the tag matches",
        ],
        'red_flags': [
            "Tag being cut from a branch other than the intended release branch",
            "Version number in code doesn't match the git tag",
            "CHANGELOG.md hasn't been updated",
            "No smoke test run against the RC artifact",
            "Rollback plan is \"redeploy the previous tag\" with no verification of that path",
        ],
        'common_mistakes': [
            "Tagging locally and forgetting to push the tag",
            "Publishing with `latest` instead of the intended version",
            "Forgetting to bump the version file when squash-merging",
            "Cutting a release from a dirty working tree",
        ],
        'rationalizations': [
            "\"It's the same as last release\" — different code, different risk profile",
            "\"CI passed\" — CI tests the branch, not the release artifact",
            "\"We can rollback if it breaks\" — rollback assumes you notice quickly",
        ],
        'phases': [
            ("Verify the source", [
                "Confirm the release branch is at the intended commit.",
                "Confirm the working tree is clean (`git status`).",
                "Confirm the version file matches the intended tag."]),
            ("Verify the artifact", [
                "Build the release artifact from the release branch.",
                "Run smoke tests against the artifact (not against `main`).",
                "Diff the artifact against the previous release; look for surprises."]),
            ("Verify the rollback path", [
                "Confirm the previous release artifact is still available.",
                "Confirm the rollback command works in a staging environment.",
                "Document who to page if rollback is needed."]),
            ("Publish and announce", [
                "Push the tag.",
                "Publish the artifact to the registry.",
                "Post the release announcement (channels, changelog link, migration notes)."]),
        ],
        'checklist': [
            "Release branch at intended commit; clean working tree",
            "Version file matches tag",
            "CHANGELOG updated",
            "Smoke tests pass against the RC artifact (not against `main`)",
            "Rollback path verified in staging",
            "Announcement drafted before publish",
        ],
        'key_principles': [
            "Verify what you're about to ship, not what you meant to ship.",
            "The rollback plan is part of the release plan.",
            "Announce after publish, not before.",
        ],
        'quick_reference':
            "1. `git status` clean, on release branch, at intended commit.\n"
            "2. Version file matches intended tag.\n"
            "3. CHANGELOG has an entry for the version.\n"
            "4. Build the artifact; run smoke tests against it.\n"
            "5. Rehearse rollback in staging.\n"
            "6. Tag, push, publish, announce.\n",
        'example':
            "### Scenario\n\n"
            "Cutting v2.4.0 of a library published to npm. The last release was "
            "v2.3.7 three weeks ago.\n\n"
            "### Applying this skill\n\n"
            "1. `git checkout release-2.4 && git status`. Clean. `git log -1 --oneline` "
            "matches the commit engineering signed off on.\n"
            "2. `cat package.json | jq .version` → `\"2.4.0\"`. Matches intended tag.\n"
            "3. `head -20 CHANGELOG.md` → v2.4.0 entry present, categorized as Added / "
            "Changed / Fixed.\n"
            "4. `npm pack` produces a tarball. `npm install ./our-lib-2.4.0.tgz` in a "
            "fresh test project; run smoke suite. Passes.\n"
            "5. Rollback rehearsal: `npm install our-lib@2.3.7` in the same test project. "
            "Verify the rollback path is live.\n"
            "6. `git tag v2.4.0 && git push origin v2.4.0 && npm publish`. Post release "
            "announcement to `#library-releases` with the changelog link.\n\n"
            "Total time: 25 minutes. Cost of skipping step 4 or 5: a broken release "
            "shipped to 40 downstream services, plus a 2-hour rollback firefight.\n",
        'commands':
            "```bash\n"
            "# Preflight\n"
            "git checkout release-2.4\n"
            "git status                              # must be clean\n"
            "git log -1 --oneline                    # confirm expected commit\n"
            "grep 'version' package.json             # confirm version match\n\n"
            "# Build and smoke-test the RC artifact\n"
            "npm pack                                # produces our-lib-2.4.0.tgz\n"
            "(cd /tmp && mkdir smoke && cd smoke && \\\n"
            " npm init -y && npm install /path/to/our-lib-2.4.0.tgz && \\\n"
            " node -e 'require(\"our-lib\").selfTest()')\n\n"
            "# Rehearse rollback\n"
            "(cd /tmp/smoke && npm install our-lib@2.3.7 && \\\n"
            " node -e 'require(\"our-lib\").selfTest()')\n\n"
            "# Publish\n"
            "git tag -a v2.4.0 -m 'v2.4.0'\n"
            "git push origin v2.4.0\n"
            "npm publish\n"
            "```\n",
        'integration': [
            "Follow with `release-notes-drafter` for the announcement",
            "Combine with `changelog-updater` before cutting the release branch",
        ],
    },

    # ============================================================
    'flaky-test-quarantine': {
        'title': 'Flaky Test Quarantine',
        'iron_law': 'NEVER `@skip` A TEST WITHOUT A TICKET AND A DEADLINE',
        'overview': {
            'iron_law':
                "Flaky tests destroy trust in the whole test suite. Once a team "
                "starts treating red as \"probably flaky, re-run,\" real regressions "
                "slip through undetected.\n\n"
                "**Core principle:** quarantine loudly, don't hide silently. Every "
                "quarantined test is a debt with a due date.\n",
            'cycle':
                "Quarantine → investigate → fix or delete. Skip the deadline and "
                "the quarantine becomes permanent tech debt.\n",
            'practical':
                "This skill covers the mechanics of quarantining a flaky test without "
                "hiding the underlying problem: filing the ticket, applying the "
                "quarantine marker, setting the escalation deadline, tracking the "
                "backlog.\n",
            'checklist':
                "Quarantine is a fixed four-step routine. Two minutes now saves "
                "hours of \"is CI actually broken?\" investigation later.\n",
        },
        'when_always': [
            "A test has failed with different messages across otherwise-identical runs",
            "A test passes on retry",
            "A test fails only in CI, not locally",
            "A test fails only under load",
        ],
        'when_especially': [
            "The test guards a business-critical invariant",
            "The test is in the pre-merge required set (blocking PRs)",
            "The team has more than 3 quarantined tests already",
        ],
        'when_dont_skip': [
            "\"It's probably just flaky\" — that's the sentence that hides real regressions",
            "\"I don't have time to file a ticket\" — you have less time to debug a hidden regression later",
        ],
        'red_flags': [
            "Test marked `@skip` with no ticket linked in the reason",
            "`@skip_if_ci` without an explanation",
            "Retry mechanism added silently instead of quarantine",
            "Quarantine \"deadline\" is empty or \"someday\"",
            "Quarantine list on the team dashboard has more than 5 items",
        ],
        'common_mistakes': [
            "Silently adding a `@retry(3)` decorator instead of investigating",
            "Quarantining without capturing the specific failure mode observed",
            "Not linking the quarantine marker to a tracking ticket",
            "Removing the quarantine when the test happens to pass, without fixing the cause",
        ],
        'rationalizations': [
            "\"It'll unflake itself when we upgrade $LIBRARY\" — occasionally, not reliably",
            "\"It only fails 1% of the time\" — 1% × 400 PRs/week = 4 blocked PRs/week",
            "\"Someone else will fix it\" — no one owns \"someone else\"",
        ],
        'phases': [
            ("Capture the failure", [
                "Grab the specific error message and stack trace from at least two "
                "failing runs.",
                "Note the environment differences (CI vs local, load, timing)."]),
            ("File the ticket", [
                "Ticket title matches the test name.",
                "Body includes the failure mode(s) observed.",
                "Assign a real deadline (typically 2 weeks)."]),
            ("Apply the marker loudly", [
                "Use a quarantine decorator that logs a warning when the test is skipped.",
                "Reference the ticket ID in the decorator argument.",
                "Do NOT use plain `@skip` without the loud version."]),
            ("Track", [
                "Add the ticket to the team dashboard's quarantine section.",
                "At deadline: either delete the test (if it's testing removed functionality) "
                "or the ticket auto-escalates to a Sev3."]),
        ],
        'checklist': [
            "At least two distinct failure occurrences captured",
            "Ticket filed with title matching test name",
            "Ticket has a deadline (not \"someday\")",
            "Quarantine decorator applied loudly (logs a warning)",
            "Ticket linked in the decorator argument",
            "Quarantine dashboard updated",
        ],
        'key_principles': [
            "Loud quarantine, not silent skip.",
            "Every quarantine has a deadline.",
            "The quarantine list has a cap; hitting it means all-hands.",
        ],
        'quick_reference':
            "```python\n"
            "@quarantine(ticket='PROJ-4821', due='2026-08-01',\n"
            "            reason='intermittent AssertionError in setup_db()')\n"
            "def test_pagination_boundary():\n"
            "    ...\n"
            "```\n\n"
            "1. Capture the failure mode from 2+ runs.\n"
            "2. File the ticket with a deadline.\n"
            "3. Apply the loud quarantine marker.\n"
            "4. Add to team dashboard.\n",
        'example':
            "### Scenario\n\n"
            "`test_upload_retries` has been failing 1-in-20 for two weeks. The "
            "on-call keeps re-running the CI job to unblock PRs.\n\n"
            "### Applying this skill\n\n"
            "1. Pull the last 5 failed runs from CI. Failures are consistent: "
            "`ConnectionResetError` from the mock S3 server, always on the third "
            "retry attempt.\n"
            "2. File `PROJ-4821`: \"test_upload_retries flaky — ConnectionResetError "
            "on 3rd retry, likely mock server race.\" Deadline: 2 weeks from today.\n"
            "3. Wrap the test:\n"
            "   ```python\n"
            "   @quarantine(ticket='PROJ-4821', due='2026-08-01', reason='mock race')\n"
            "   def test_upload_retries():\n"
            "       ...\n"
            "   ```\n"
            "   Quarantine decorator prints `WARN: skipping test_upload_retries — PROJ-4821 due 2026-08-01` on every run.\n"
            "4. Add PROJ-4821 to `#dashboard-quarantines`.\n\n"
            "Result: CI stops flaking. The ticket is visible on the team dashboard. "
            "At the deadline, someone owns the fix or the test goes.\n",
        'commands':
            "```bash\n"
            "# Find already-quarantined tests to see how many the team has\n"
            "grep -rn '@quarantine' tests/ | wc -l\n\n"
            "# Find candidates: tests with @skip or @retry that lack tickets\n"
            "grep -rnE '@(skip|skipIf|retry)' tests/ | grep -vE 'PROJ-[0-9]+'\n\n"
            "# List quarantines nearing their deadline (adapt to your marker format)\n"
            "python3 -c \"\n"
            "import ast, os, datetime\n"
            "today = datetime.date.today()\n"
            "for root, _, files in os.walk('tests'):\n"
            "    for f in files:\n"
            "        if not f.endswith('.py'): continue\n"
            "        # ... parse quarantine markers and print upcoming due dates\n"
            "\"\n"
            "```\n",
        'integration': [
            "Follow with `test-first-fix` when addressing the quarantined test",
            "Combine with `root-cause-first` to investigate the flakiness cause",
        ],
    },

    # ============================================================
    'api-contract-check': {
        'title': 'API Contract Check',
        'iron_law': 'NO BREAKING API CHANGE WITHOUT A MAJOR VERSION BUMP',
        'overview': {
            'iron_law':
                "A silent breaking change to a public API is a supply-chain incident "
                "waiting for a downstream user to discover.\n\n"
                "**Core principle:** the contract is what downstream users depend on. "
                "Break it deliberately and loudly, or don't break it.\n",
            'cycle':
                "Diff → categorize → decide version bump → document. Every PR that "
                "touches public surface goes through the cycle.\n",
            'practical':
                "This skill covers the mechanics of detecting breaking changes across "
                "REST endpoints, gRPC / protobuf definitions, and library public "
                "exports; it also covers the version-bump policy that follows.\n",
            'checklist':
                "API contract check is a fixed pre-merge routine for any PR touching "
                "the public surface.\n",
        },
        'when_always': [
            "Any change to public function signatures or exported types",
            "Any change to REST endpoint schemas (request or response)",
            "Any change to gRPC / protobuf definitions",
            "Any change to CLI flags or output format",
        ],
        'when_especially': [
            "Deleting or renaming a public export",
            "Changing the type of a required field",
            "Changing default values on an existing parameter",
            "Reordering positional parameters",
        ],
        'when_dont_skip': [
            "\"It's an internal API\" — internal often means \"undocumented public\" in practice",
            "\"No one uses that endpoint\" — the endpoint that gets removed is the one someone was using",
        ],
        'red_flags': [
            "Adding a new required parameter to an existing function or endpoint",
            "Changing an optional parameter to required",
            "Narrowing an accepted enum or type",
            "Removing an endpoint / method / export in a non-major version",
            "Silent behavior change (same signature, different semantics)",
        ],
        'common_mistakes': [
            "Diffing against the wrong base branch (comparing to `main` misses in-flight releases)",
            "Only checking method signatures, not runtime response shapes",
            "Treating an added required field as \"backwards-compatible because it has a default\"",
            "Not testing with an old client against the new server",
        ],
        'rationalizations': [
            "\"They can just update their code\" — that's the definition of breaking",
            "\"We're pre-1.0\" — downstream users don't read your semver philosophy",
            "\"It's a bugfix\" — bugfixes that change behavior are still contract changes",
        ],
        'phases': [
            ("Diff the public surface", [
                "Compare exported symbols against the last release tag.",
                "For REST/gRPC: diff the schema files.",
                "For CLI: diff the flag list and help output."]),
            ("Categorize each change", [
                "Additive (new endpoint, new optional field) → minor bump.",
                "Removal / signature change → major bump.",
                "Behavior change with same signature → major bump."]),
            ("Decide the version", [
                "Any category-2 or category-3 change → major.",
                "Any category-1 change (no others) → minor.",
                "Doc-only or internal → patch."]),
            ("Document", [
                "Add breaking-change section to CHANGELOG.",
                "Update migration guide for downstream users.",
                "Add deprecation warnings if there's a transition period."]),
        ],
        'checklist': [
            "Public-surface diff run against last release tag",
            "Each change categorized (additive / signature / behavior)",
            "Version bump decided per policy",
            "CHANGELOG breaking-change section updated",
            "Migration guide updated (for majors)",
            "Old-client-against-new-server test run",
        ],
        'key_principles': [
            "Silent behavior changes are breaking changes.",
            "Deprecate before removing; give at least one release cycle.",
            "\"Internal API\" is an aspiration, not a contract.",
        ],
        'quick_reference':
            "**Version bump decision matrix:**\n"
            "| Change | Bump |\n"
            "|---|---|\n"
            "| Add optional field / endpoint / method | Minor |\n"
            "| Add required field / rename / remove | Major |\n"
            "| Behavior change, same signature | Major |\n"
            "| Docs / internal / test only | Patch |\n",
        'example':
            "### Scenario\n\n"
            "PR renames `getUsers(orgId)` to `listUsers(orgId)` and marks the old "
            "name as `@deprecated`.\n\n"
            "### Applying this skill\n\n"
            "1. Diff the exports:\n"
            "   ```\n"
            "   - export function getUsers(orgId: string): Promise<User[]>\n"
            "   + export function listUsers(orgId: string): Promise<User[]>\n"
            "   + /** @deprecated use listUsers */\n"
            "   + export const getUsers = listUsers\n"
            "   ```\n"
            "2. Categorize: `getUsers` still exists as an alias → not a removal. `listUsers` "
            "is additive. So this is a MINOR bump, plus a deprecation notice.\n"
            "3. Version bump: minor.\n"
            "4. CHANGELOG:\n"
            "   ```\n"
            "   ## [1.5.0] - 2026-07-15\n"
            "   ### Added\n"
            "   - `listUsers(orgId)` (renamed from `getUsers`)\n"
            "   ### Deprecated\n"
            "   - `getUsers(orgId)` — use `listUsers` instead; will be removed in 2.0\n"
            "   ```\n"
            "5. Migration guide: add a one-line entry mapping old → new.\n\n"
            "Without step 1, someone might have merged the rename as-is (removing "
            "`getUsers`), silently breaking every downstream call site.\n",
        'commands':
            "```bash\n"
            "# TypeScript public surface diff\n"
            "npx api-extractor run --local\n"
            "diff <(git show v1.4.0:etc/api-report.md) etc/api-report.md\n\n"
            "# Python public surface (using pyright or mypy stubs)\n"
            "diff <(git show v1.4.0:mylib/__init__.pyi) mylib/__init__.pyi\n\n"
            "# REST/OpenAPI diff\n"
            "npx @redocly/openapi-cli diff \\\n"
            "    <(git show v1.4.0:openapi.yaml) openapi.yaml\n\n"
            "# Protobuf breaking-change check\n"
            "buf breaking --against '.git#tag=v1.4.0'\n"
            "```\n",
        'integration': [
            "Follow with `changelog-updater` to document the change",
            "Combine with `api-deprecation-planner` for deprecations",
        ],
    },

    # ============================================================
    'on-call-handoff': {
        'title': 'On-Call Handoff',
        'iron_law': 'NO HANDOFF WITHOUT WRITTEN CONTEXT',
        'overview': {
            'iron_law':
                "On-call context lives in the on-call's head. Without a written "
                "handoff, everything they learned is lost the moment they log off.\n\n"
                "**Core principle:** the next on-call is a stranger. Write for them.\n",
            'cycle':
                "Each rotation is a small cycle: pick up context → work → hand off "
                "context. Break the cycle by skipping the handoff and the next person "
                "starts from scratch.\n",
            'practical':
                "This skill covers the mechanics of an on-call handoff: what to include "
                "in the handoff doc, what to say verbally, and what NOT to hand off "
                "(finish it or escalate).\n",
            'checklist':
                "The handoff is a fixed short checklist. Ten minutes at the end of "
                "your rotation saves the next person hours.\n",
        },
        'when_always': [
            "End of every on-call rotation",
            "Start of every on-call rotation (read the previous person's handoff)",
            "Mid-rotation swap for any reason",
        ],
        'when_especially': [
            "An incident is still open at handoff time",
            "A ticket was investigated but not resolved",
            "You noticed a pattern that hasn't yet caused a full incident",
        ],
        'when_dont_skip': [
            "\"Nothing happened this rotation\" — write \"nothing happened\" explicitly; silence is ambiguous",
            "\"I'll just tell them in Slack\" — Slack messages disappear; handoff docs don't",
        ],
        'red_flags': [
            "Open incident + you're going off-call in less than 30 min without transferring IC",
            "Handoff doc is empty",
            "Handoff mentions \"see Slack\" without specific message links",
            "Handoff refers to a ticket without linking it",
            "Verbal handoff only, no written trail",
        ],
        'common_mistakes': [
            "Writing the handoff at the very end when you're tired",
            "Omitting things you \"resolved\" but might recur",
            "Not linking runbooks used for reference",
            "Not naming the next on-call in the doc so they can grep",
        ],
        'rationalizations': [
            "\"They can ask me if they need to\" — asking is friction that produces slower response",
            "\"It's obvious what to do\" — obvious to you now, mysterious next month",
            "\"I'll be around anyway\" — until you aren't (vacation, sick, other project)",
        ],
        'phases': [
            ("Prepare during the rotation", [
                "Keep a running notes file for the week.",
                "Every non-trivial page: one paragraph of context.",
                "Every runbook you used: log the entry with a link."]),
            ("Write the handoff", [
                "Summary at top: any open items, any unresolved patterns.",
                "Section for each incident touched this week.",
                "Recommended reading for the next person (runbooks, dashboards)."]),
            ("Do the verbal handoff", [
                "Live sync with the next on-call — 15 minutes is enough.",
                "Walk them through the doc, don't just link it.",
                "Explicit transfer of any open Incident Commander role."]),
            ("Confirm they have access", [
                "PagerDuty schedule is updated.",
                "They can access all the dashboards and runbooks referenced.",
                "They have the phone numbers for escalation contacts."]),
        ],
        'checklist': [
            "Weekly notes were kept",
            "Handoff doc written",
            "Doc covers: open items, this-week incidents, recommended reading",
            "Verbal handoff completed",
            "Explicit IC transfer if any incidents are still open",
            "PagerDuty schedule reflects the swap",
        ],
        'key_principles': [
            "Write during the week, not at the end.",
            "Silence in a handoff is ambiguous — say \"nothing happened\" explicitly.",
            "Verbal + written, not verbal instead of written.",
        ],
        'quick_reference':
            "```markdown\n"
            "# On-call handoff — Week of $(date)\n\n"
            "**Incoming on-call:** $NAME\n"
            "**Outgoing on-call:** $YOUR_NAME\n\n"
            "## TL;DR\n"
            "- [ ] Open items requiring follow-up: <list or \"none\">\n"
            "- [ ] Unresolved patterns: <list or \"none\">\n\n"
            "## Incidents this rotation\n"
            "- 2026-07-13 checkout p95 spike — resolved, [postmortem](link)\n"
            "- 2026-07-14 dashboard-a alert flapping — silenced, ticket PROJ-999\n\n"
            "## Recommended reading\n"
            "- [runbook: checkout error rate](link)\n"
            "- [dashboard: pricing service health](link)\n"
            "```\n",
        'example':
            "### Scenario\n\n"
            "It's Friday 5pm. You're going off-call. During the week you had two "
            "incidents (both resolved) and noticed the auth service is showing "
            "gradual memory growth (not yet paged on it).\n\n"
            "### Applying this skill\n\n"
            "1. Weekly notes file already exists — you added an entry after each page.\n"
            "2. Handoff doc:\n"
            "   ```\n"
            "   # On-call handoff — Week of 2026-07-14\n"
            "   Incoming: @sam. Outgoing: @you.\n\n"
            "   ## TL;DR\n"
            "   - Watch: auth-service memory trending up ~3%/day since Monday.\n"
            "     No page yet, but graph is [here](link). Might need action next week.\n"
            "   - All incidents resolved.\n\n"
            "   ## Incidents this rotation\n"
            "   - Mon: checkout p95 spike after deploy. Resolved by rollback.\n"
            "     [Postmortem](link). Root cause: unindexed query added in v2.1.4.\n"
            "   - Wed: pricing-service pod OOMKilled twice. Bumped memory limit.\n"
            "     Not a permanent fix — see [PROJ-999](link).\n"
            "   ```\n"
            "3. Ping Sam for a 15-minute video sync at 4:45pm.\n"
            "4. Confirm Sam is in PagerDuty rotation starting 5pm.\n\n"
            "Sam picks up Monday and immediately knows about the auth-service memory "
            "trend, the still-open PROJ-999, and the postmortem links. Total your "
            "time: 15 minutes. Sam's time saved: 2-3 hours of context-rebuilding.\n",
        'commands':
            "```bash\n"
            "# Convention: one file per week's handoff\n"
            "mkdir -p oncall/handoffs\n"
            "cp oncall/handoffs/TEMPLATE.md oncall/handoffs/$(date +%Y-%m-%d).md\n\n"
            "# Extract this week's incidents from the incident log\n"
            "gh api /repos/$ORG/$REPO/issues?labels=incident,resolved \\\n"
            "  --jq '.[] | select(.closed_at > \"2026-07-14\") | \\\n"
            "        \"- \\(.closed_at[:10]): \\(.title) — [postmortem](\\(.html_url))\"'\n\n"
            "# Confirm PagerDuty rotation swap\n"
            "pd schedules list --oncall\n"
            "```\n",
        'integration': [
            "Read the handoff first thing at start of rotation",
            "Combine with `runbook-writer` — every unresolved item deserves a runbook entry",
        ],
    },

    # ============================================================
    'code-smell-namer': {
        'title': 'Code Smell Namer',
        'iron_law': 'A COMMENT NAMING THE SMELL BEATS A COMMENT DESCRIBING THE FIX',
        'overview': {
            'iron_law':
                "Naming a code smell in a review comment gives the author (and future "
                "readers) a concept to search for. \"Fix this\" gives them nothing.\n\n"
                "**Core principle:** vocabulary is leverage. Every named smell is a "
                "shortcut the whole team learns.\n",
            'cycle':
                "Spot → name → link to canonical reference → suggest refactor. Every "
                "review pass is an opportunity to teach.\n",
            'practical':
                "This skill covers the common code smells worth naming in reviews: "
                "when to invoke each, how to phrase the comment so it lands, and when "
                "to skip the naming because context makes it inappropriate.\n",
            'checklist':
                "Smell-naming is a lookup: identify the pattern, name it, link the "
                "reference.\n",
        },
        'when_always': [
            "Reviewing code where you notice a recurring anti-pattern",
            "Reviewing code from a junior engineer (vocabulary transfer)",
            "Reviewing code that you would like to refactor later",
        ],
        'when_especially': [
            "The smell appears in multiple places in the PR",
            "The smell is a common source of future bugs (not just cosmetic)",
            "The PR is a good teaching opportunity (not time-critical)",
        ],
        'when_dont_skip': [
            "\"It's not that bad\" — small smells accumulate; naming them keeps them off future PRs",
            "\"The author knows this pattern\" — the author knows; the next reader may not",
        ],
        'red_flags': [
            "Naming a smell without any actionable suggestion",
            "Piling multiple smell names into one comment (readers can't act on all at once)",
            "Naming smells as a defensive move against a design you disagree with",
            "Using a smell name incorrectly (weakens the vocabulary)",
        ],
        'common_mistakes': [
            "Long parameter lists → often really \"primitive obsession\"; use the right term",
            "\"Magic number\" — often a constant that just needs a name, not a full refactor",
            "\"God object\" — often a facade that's fine at a facade layer",
            "Confusing \"shotgun surgery\" (spread-out change) with \"feature envy\" (misplaced method)",
        ],
        'rationalizations': [
            "\"Refactoring should be a separate PR\" — that's a decision, not a reason to skip naming",
            "\"The author will figure it out\" — vocabulary transfer requires explicit naming",
        ],
        'phases': [
            ("Notice the pattern", [
                "Read the surrounding code, not just the diff.",
                "Ask: have I seen this shape before, in this codebase or elsewhere?"]),
            ("Match to a name", [
                "Consult your mental library (or the Refactoring book).",
                "If uncertain, don't name — describe the concern in your own words."]),
            ("Write the comment", [
                "State the smell name.",
                "Point at the specific lines.",
                "Suggest a concrete refactor.",
                "Link the canonical reference (Fowler, Refactoring Guru, etc.)."]),
            ("Follow up", [
                "If the author disagrees with the naming, engage rather than dig in.",
                "If they agree but don't want to fix in this PR, file a ticket.",
                "Track: which smells recur across the team's PRs?"]),
        ],
        'checklist': [
            "Smell name used correctly (not just \"this is bad\")",
            "Concrete lines pointed at",
            "Refactor suggested, not just complaint",
            "Reference link included where useful",
            "Blocking vs non-blocking made explicit",
        ],
        'key_principles': [
            "Name the smell, then suggest the fix.",
            "Wrong name > no name only if it's honestly close; otherwise describe.",
            "Vocabulary is a shared team asset.",
        ],
        'quick_reference':
            "Common smells worth naming:\n"
            "- **Long parameter list** — > 3-4 params → introduce parameter object\n"
            "- **Primitive obsession** — string/int for a concept → introduce value type\n"
            "- **Feature envy** — method uses another object's data more than its own → move method\n"
            "- **Shotgun surgery** — one change touches many files → introduce abstraction\n"
            "- **Divergent change** — one class touched for many reasons → split class\n"
            "- **Data clumps** — same group of fields recurs → extract class\n"
            "- **Speculative generality** — unused abstraction → inline it\n",
        'example':
            "### Scenario\n\n"
            "PR adds a function `createOrder(userId, sku, quantity, currency, "
            "billingAddress, shippingAddress, discountCode, giftMessage, isGift, isSubscription)`.\n\n"
            "### Bad review comment\n\n"
            "> This function has too many arguments.\n\n"
            "### Good review comment\n\n"
            "> **Long parameter list** on `createOrder` (11 params). Consider introducing "
            "an `OrderRequest` value object that groups the customer-facing fields "
            "(addresses, gift options) — the current signature is prone to positional-arg "
            "bugs when we add more options. Reference: "
            "[Refactoring Guru - Long Parameter List](https://refactoring.guru/smells/long-parameter-list). "
            "Non-blocking for this PR but worth a follow-up ticket.\n\n"
            "The good version teaches vocabulary, points at a specific refactor, links "
            "canonical reference, and is explicit about not blocking the PR.\n",
        'commands':
            "```bash\n"
            "# Quick reference lookup by smell name\n"
            "curl -s 'https://refactoring.guru/smells' | grep -oE 'smells/[a-z-]+' | sort -u\n\n"
            "# Find all your team's uses of a specific smell in past PRs\n"
            "gh pr list --search 'primitive obsession in:comments' --state all\n"
            "```\n",
        'integration': [
            "Combine with `systematic-code-review` — smells are what you name during phase 3",
            "Follow with `refactor-planner` if the smell is worth addressing",
        ],
    },

    # ============================================================
    'log-level-hygiene': {
        'title': 'Log Level Hygiene',
        'iron_law': 'NEVER LOG AT INFO WHAT SHOULD BE AT DEBUG OR ERROR',
        'overview': {
            'iron_law':
                "Log levels are how future-you filters signal from noise. Wrong "
                "levels destroy the utility of the entire log stream.\n\n"
                "**Core principle:** every log line has an audience. Match the level "
                "to that audience.\n",
            'cycle':
                "Every log line: pick level → write message → confirm no PII → commit.\n",
            'practical':
                "This skill covers picking correct log levels (DEBUG / INFO / WARN / "
                "ERROR / FATAL), writing messages that grep well, and avoiding "
                "PII / secrets in log output.\n",
            'checklist':
                "Log hygiene is a fixed per-line checklist. Ten seconds saves hours "
                "of production log-diving.\n",
        },
        'when_always': [
            "Adding any new log statement",
            "Reviewing any PR that adds or modifies logging",
            "After an incident where logs were unhelpful",
        ],
        'when_especially': [
            "Adding logs in hot-path code (volume matters)",
            "Logs that might contain user-supplied strings (PII risk)",
            "Logs from library code (level defaults propagate)",
        ],
        'when_dont_skip': [
            "\"It's a debug print I'll remove later\" — later never comes",
            "\"The framework picks a default level\" — the default is rarely what you want",
        ],
        'red_flags': [
            "`INFO` used for one-off diagnostic prints",
            "`ERROR` used for expected fallbacks",
            "Log line contains a raw user email, password, or auth token",
            "Log message has no context (`\"Success\"` without knowing success of what)",
            "Log line includes a full stack trace at `WARN` — should be `ERROR` or below",
        ],
        'common_mistakes': [
            "Logging inside a tight loop at `INFO`",
            "Using `WARN` for both retriable failures and permanent failures",
            "Building the log message with string concatenation (unhelpful for structured log ingestion)",
            "Logging the same event at multiple layers (log once, at the layer that decides)",
        ],
        'rationalizations': [
            "\"More logs is better\" — more noise is worse",
            "\"We'll grep it out later\" — greppability requires disciplined format",
            "\"It's just dev logging\" — dev logging becomes prod logging via `git push`",
        ],
        'phases': [
            ("Pick the level", [
                "DEBUG: state useful during development, silent in production.",
                "INFO: notable business events (order placed, user logged in).",
                "WARN: unexpected but recoverable (retry succeeded, fallback used).",
                "ERROR: failed operation that a human needs to see.",
                "FATAL: process cannot continue."]),
            ("Write the message", [
                "Start with the event, not the value: \"Order placed\" not \"orderId=123\".",
                "Include structured fields as key=value, not concatenated strings.",
                "Include the correlation ID.",
                "Omit anything PII or credential-shaped."]),
            ("Verify before commit", [
                "grep the new log line — does it read well?",
                "Confirm the level matches what you'd want a page threshold on.",
                "Confirm no PII / secrets in the payload."]),
            ("Sample the output", [
                "Run the code path once, look at the actual log output.",
                "Confirm it looks how you'd want it during an incident."]),
        ],
        'checklist': [
            "Level matches the intent (DEBUG / INFO / WARN / ERROR / FATAL)",
            "Message starts with the event, not the value",
            "Structured key=value fields (not concatenated)",
            "Correlation ID present",
            "No PII, no credentials, no auth tokens in the payload",
            "Sampled the actual output at least once",
        ],
        'key_principles': [
            "Log levels have specific meanings; don't blend them.",
            "Log for future-you during an incident.",
            "PII/secrets in logs is a data-classification incident.",
        ],
        'quick_reference':
            "| Level | Meaning | Example |\n"
            "|---|---|---|\n"
            "| DEBUG | Dev-time state, silent in prod | `\"cache lookup for user_id=%s\"` |\n"
            "| INFO  | Notable business events | `\"order placed order_id=%s\"` |\n"
            "| WARN  | Unexpected but recoverable | `\"retry succeeded after %d attempts\"` |\n"
            "| ERROR | Failure a human should see | `\"payment charge failed txn=%s\"` |\n"
            "| FATAL | Process cannot continue | `\"config missing required key\"` |\n",
        'example':
            "### Bad\n\n"
            "```python\n"
            "logger.info(f'Got request {request.headers[\"Authorization\"]}')\n"
            "logger.error('Retry succeeded')\n"
            "logger.warn(traceback.format_exc())\n"
            "```\n\n"
            "Problems: PII/secret leaked, wrong level for success, stack trace at WARN.\n\n"
            "### Good\n\n"
            "```python\n"
            "logger.debug('request received', extra={'req_id': req_id, 'endpoint': endpoint})\n"
            "logger.info('retry succeeded', extra={'req_id': req_id, 'attempts': attempts})\n"
            "logger.error('payment charge failed', extra={\n"
            "    'req_id': req_id, 'txn_id': txn.id, 'error_code': err.code,\n"
            "})\n"
            "```\n",
        'commands':
            "```bash\n"
            "# Scan for potential PII / secret in logs\n"
            "grep -rnE 'log(ger)?\\.(debug|info|warn|error).*\\b(password|token|secret|authorization|email|ssn)' src/\n\n"
            "# Find log-in-hot-loop patterns\n"
            "grep -rnE '(for|while).*\\{.*log(ger)?\\.' src/\n\n"
            "# Sample the actual output during dev\n"
            "python3 -c 'import myapp; myapp.simulate_order()' 2>&1 | grep -E 'INFO|WARN|ERROR'\n"
            "```\n",
        'integration': [
            "Combine with `secrets-check` — logging secrets is a leak",
            "Follow with `log-triage` when the logs are actually used",
        ],
    },

    # ============================================================
    'cost-anomaly-triage': {
        'title': 'Cloud Cost Anomaly Triage',
        'iron_law': 'NO BUDGET REQUEST WITHOUT ISOLATING THE ANOMALOUS RESOURCE',
        'overview': {
            'iron_law':
                "\"The bill went up\" is not a diagnosis. Isolate the specific resource "
                "or service before asking for more budget or blaming a team.\n\n"
                "**Core principle:** cost is data. Treat spikes the way you'd treat a "
                "latency spike — with a triage protocol, not a wallet.\n",
            'cycle':
                "Anomaly → segment → attribute → decide → document. Every spike goes "
                "through the cycle.\n",
            'practical':
                "This skill covers the mechanics of triaging a cloud cost spike using "
                "cost-explorer tools, tag-based attribution, and correlation with "
                "recent deploys or config changes.\n",
            'checklist':
                "Cost triage is a fixed set of segmentation queries. Start broad, "
                "narrow to the offending resource.\n",
        },
        'when_always': [
            "A monthly bill spikes > 10% vs the trailing 3-month average",
            "A finance-team alert about an unexpected charge",
            "Discovering an untagged high-cost resource",
        ],
        'when_especially': [
            "The spike is in a service that shouldn't be growing",
            "The spike coincides with a recent deploy or infrastructure change",
            "Multiple teams could plausibly be responsible",
        ],
        'when_dont_skip': [
            "\"The bill fluctuates normally\" — verify it's normal fluctuation, don't assume",
            "\"Finance will figure it out\" — finance can only ask; engineering has to answer",
        ],
        'red_flags': [
            "Requesting a budget increase without a resource breakdown",
            "Blaming a team based on \"they use the most X\" without confirming",
            "Attributing a cost purely from dashboards without checking raw usage",
            "Not looking at whether the cost is one-time (data transfer) or ongoing (compute)",
            "\"It's probably just growth\" without checking the growth curve",
        ],
        'common_mistakes': [
            "Only looking at the top-level service (EC2, S3) and missing sub-resource attribution",
            "Ignoring inter-region data transfer as a cost driver",
            "Missing costs on shared / cluster resources (untagged)",
            "Not distinguishing reserved / spot / on-demand pricing effects",
        ],
        'rationalizations': [
            "\"It's within budget\" — silent growth eats future budget",
            "\"We'll optimize later\" — later is when it's 10x",
            "\"AWS/GCP pricing is confusing\" — that's why triage exists",
        ],
        'phases': [
            ("Segment by service", [
                "Pull cost-explorer report grouped by service for the anomalous month.",
                "Identify the top 3 contributors to the delta vs baseline."]),
            ("Segment by tag / team / project", [
                "For each of the top services: group by tag (`team`, `env`, `service`).",
                "Untagged resources are red flags — investigate individually."]),
            ("Isolate the specific resource", [
                "Drill into the top-tagged group.",
                "Identify the specific instance / bucket / dataset driving the cost.",
                "Correlate with deploys / config changes in that time window."]),
            ("Decide and document", [
                "Confirm whether the cost is one-time or ongoing.",
                "Assign an owner.",
                "File a ticket with the isolated resource + likely cause."]),
        ],
        'checklist': [
            "Cost-explorer breakdown by service pulled",
            "Top 3 delta contributors identified",
            "Tag-based attribution for each",
            "Specific resource isolated (not just a team)",
            "Correlated with deploy / config timeline",
            "One-time vs ongoing distinguished",
            "Ticket filed with the specific resource + owner",
        ],
        'key_principles': [
            "Specific resource, not \"the team\".",
            "One-time vs ongoing changes the response.",
            "Untagged is a first-order finding — fix the tagging.",
        ],
        'quick_reference':
            "1. Bill up. Which service?\n"
            "2. Which tag/team within that service?\n"
            "3. Which specific resource within that tag?\n"
            "4. When did it start? What changed then?\n"
            "5. One-time or ongoing?\n"
            "6. Ticket with owner + specific resource.\n",
        'example':
            "### Scenario\n\n"
            "June bill is $47K, up 23% from the trailing 3-month average of $38K. "
            "Finance flags it.\n\n"
            "### Applying this skill\n\n"
            "1. Cost Explorer by service: top delta is `Amazon RDS` (+$8K). Rest is "
            "within normal fluctuation.\n"
            "2. RDS by tag: `env=staging` accounts for +$7K of the +$8K. Ownership: "
            "data platform team.\n"
            "3. Drill down: one staging RDS cluster (`analytics-staging-2`) went from "
            "an r6g.large to a r6g.16xlarge on June 3rd. That's a 32x cost increase.\n"
            "4. Correlate: git log for infra repo on June 3rd shows a PR titled \"scale "
            "up analytics-staging-2 for load test\". Load test finished June 5, cluster "
            "wasn't scaled back down.\n"
            "5. Cost is ongoing until someone scales it back. File `INFRA-772`: scale "
            "analytics-staging-2 back to r6g.large. Owner: data platform.\n"
            "6. Total spike: $7K/month × N months. Fixed same day.\n\n"
            "Without step 3-4, the ticket would have said \"data platform team's staging "
            "costs are up\" — technically true, useless for remediation.\n",
        'commands':
            "```bash\n"
            "# AWS: cost breakdown by service for a specific month\n"
            "aws ce get-cost-and-usage \\\n"
            "  --time-period Start=2026-06-01,End=2026-07-01 \\\n"
            "  --granularity MONTHLY \\\n"
            "  --metrics UnblendedCost \\\n"
            "  --group-by Type=DIMENSION,Key=SERVICE\n\n"
            "# Drill into RDS by tag\n"
            "aws ce get-cost-and-usage \\\n"
            "  --time-period Start=2026-06-01,End=2026-07-01 \\\n"
            "  --granularity MONTHLY \\\n"
            "  --metrics UnblendedCost \\\n"
            "  --filter file://filter-rds.json \\\n"
            "  --group-by Type=TAG,Key=env\n\n"
            "# Correlate with infra deploys\n"
            "git -C infra-repo log --oneline --since='2026-06-01' --until='2026-06-05'\n"
            "```\n",
        'integration': [
            "Follow with `runbook-writer` — recurring anomaly types deserve a runbook",
            "Escalate to `incident-triage` if the anomaly indicates active abuse (crypto miner, etc.)",
        ],
    },

    # ============================================================
    'adr-writer': {
        'title': 'Architecture Decision Record Writer',
        'iron_law': 'NO ARCHITECTURAL DECISION WITHOUT AN ADR',
        'overview': {
            'iron_law':
                "Decisions with no written trail get re-litigated every six months "
                "as new engineers join. An ADR turns a decision into a permanent "
                "reference.\n\n"
                "**Core principle:** the decision matters less than the fact that it "
                "was written down.\n",
            'cycle':
                "Draft → review → accept or supersede. Every architectural decision "
                "goes through the cycle, however small.\n",
            'practical':
                "This skill covers writing ADRs: the standard shape (Context, Decision, "
                "Consequences), when a decision is worth an ADR, and how to supersede "
                "an existing ADR when the decision changes.\n",
            'checklist':
                "ADR writing is a fixed short template. Ten minutes at decision time "
                "prevents days of \"why did we do it this way?\" later.\n",
        },
        'when_always': [
            "Choosing between multiple viable technical approaches",
            "Adopting a new framework, database, or major dependency",
            "Deciding to NOT do something (that decision is also architectural)",
            "Reversing a previous decision",
        ],
        'when_especially': [
            "The decision affects multiple teams",
            "The decision has non-obvious tradeoffs",
            "The decision is reversible only with significant effort",
        ],
        'when_dont_skip': [
            "\"It's obvious\" — obvious to you now, mysterious to new hires in six months",
            "\"We'll write it later\" — later is when everyone has forgotten the alternatives considered",
        ],
        'red_flags': [
            "Decision announced in a Slack thread without an ADR follow-up",
            "ADR that lists only the chosen option, not the alternatives",
            "ADR without a \"Consequences\" section",
            "ADR modified in place instead of superseded with a new one",
            "Team has more than 5 recent decisions with no ADRs",
        ],
        'common_mistakes': [
            "Writing the ADR after implementation (loses the pre-decision context)",
            "Presenting the decision without the rejected alternatives",
            "Skipping consequences because \"they're obvious\"",
            "Not linking the ADR from the corresponding design doc / spec",
        ],
        'rationalizations': [
            "\"We're too small for ADRs\" — small teams grow; ADRs are the growing team's memory",
            "\"The design doc covers it\" — design docs age; ADRs are the durable record",
            "\"It's a temporary decision\" — temporary decisions are the ones most worth recording",
        ],
        'phases': [
            ("Identify the decision", [
                "Name the decision in one sentence.",
                "Confirm it's a decision, not just an implementation detail."]),
            ("Draft the ADR", [
                "Use a standard template (Context / Decision / Consequences).",
                "In Context: what forces led to needing a decision?",
                "In Decision: what was chosen, and briefly why.",
                "In Consequences: what does this decision commit us to?"]),
            ("Review with stakeholders", [
                "Async review — pull the ADR into the PR that implements the decision.",
                "Give reviewers 24-48 hours."]),
            ("Publish and reference", [
                "Merge the ADR into the `docs/adr/` directory.",
                "Link from the design doc / spec.",
                "Announce in the relevant channel."]),
        ],
        'checklist': [
            "One-sentence decision statement",
            "Context section explains WHY a decision was needed",
            "Alternatives considered (and rejected) listed",
            "Consequences section covers commitments and constraints",
            "Reviewed by at least one other engineer",
            "Merged into `docs/adr/`",
        ],
        'key_principles': [
            "Write it now, not later.",
            "The rejected alternatives are as important as the chosen one.",
            "Supersede, don't rewrite.",
        ],
        'quick_reference':
            "```markdown\n"
            "# ADR N: <short title>\n\n"
            "**Status:** Proposed / Accepted / Superseded by ADR M\n\n"
            "## Context\n"
            "<what forces are in play; what problem prompted the decision>\n\n"
            "## Decision\n"
            "<what was chosen>\n\n"
            "## Alternatives Considered\n"
            "- <alt 1> — rejected because <reason>\n"
            "- <alt 2> — rejected because <reason>\n\n"
            "## Consequences\n"
            "- <what this now commits us to>\n"
            "- <what it makes harder>\n"
            "- <what it makes easier>\n"
            "```\n",
        'example':
            "### Scenario\n\n"
            "Team is picking between REST and gRPC for a new internal service.\n\n"
            "### The ADR\n\n"
            "```markdown\n"
            "# ADR 27: Use REST (not gRPC) for internal service-to-service RPC\n\n"
            "**Status:** Accepted\n\n"
            "## Context\n"
            "New order-processing service needs to expose an API to 3 internal callers "
            "(checkout, billing, inventory). Team debate over REST vs gRPC.\n\n"
            "## Decision\n"
            "Use REST with JSON payloads.\n\n"
            "## Alternatives Considered\n"
            "- **gRPC** — rejected. Team has no existing gRPC toolchain; adding one "
            "for 3 callers is disproportionate. Debugging in production would require "
            "new tooling investment.\n"
            "- **GraphQL** — rejected. Query flexibility not needed here; adds server complexity.\n\n"
            "## Consequences\n"
            "- Commit to using REST for all internal service RPC going forward.\n"
            "- Team must invest in an OpenAPI-first workflow if we haven't already.\n"
            "- Migration to gRPC later would require an ADR to supersede this one.\n"
            "- Existing REST tooling (curl, Postman, k6) works out of the box.\n"
            "```\n\n"
            "Six months later, a new engineer asks \"why didn't we use gRPC?\" The "
            "answer is the ADR, not a Slack search.\n",
        'commands':
            "```bash\n"
            "# Standard ADR directory\n"
            "mkdir -p docs/adr\n\n"
            "# Copy from template\n"
            "N=$(ls docs/adr/*.md 2>/dev/null | wc -l | tr -d ' ')\n"
            "N=$((N + 1))\n"
            "cp docs/adr/TEMPLATE.md docs/adr/$(printf '%04d' $N)-<slug>.md\n\n"
            "# Find existing ADRs on a topic\n"
            "grep -l 'gRPC' docs/adr/*.md\n\n"
            "# When superseding: update status in old ADR, create new one\n"
            "sed -i 's/^\\*\\*Status:\\*\\* Accepted/**Status:** Superseded by ADR $NEW/' docs/adr/0027-*.md\n"
            "```\n",
        'integration': [
            "Follow with `spec-review` when the decision is part of a larger design",
            "Combine with `changelog-updater` if the decision changes user-visible behavior",
        ],
    },

    # ============================================================
    'tls-cert-renewer': {
        'title': 'TLS Certificate Renewal',
        'iron_law': 'NO CERT RENEWAL WITHOUT A ROLLBACK TO THE OLD CERT',
        'overview': {
            'iron_law':
                "A botched cert renewal takes down every HTTPS user simultaneously. "
                "The old cert is your fallback — don't destroy it until the new one "
                "is verified in production.\n\n"
                "**Core principle:** cert changes are a two-step ceremony: deploy new, "
                "verify, only then decommission old.\n",
            'cycle':
                "Prepare new cert → deploy → verify with real clients → decommission "
                "old. Each step must succeed before the next.\n",
            'practical':
                "This skill covers renewing TLS certs without downtime: preparing the "
                "renewal early, deploying without disrupting live connections, verifying "
                "with multiple clients, and cleanly decommissioning the old cert.\n",
            'checklist':
                "Cert renewal is a fixed sequence. Every step exists because someone "
                "has been paged at 3am by skipping it.\n",
        },
        'when_always': [
            "Any TLS cert is < 30 days from expiry",
            "First renewal for a new domain",
            "Switching cert authority (e.g. commercial → Let's Encrypt)",
        ],
        'when_especially': [
            "Certs pinned by mobile clients",
            "Certs used by non-HTTP protocols (mTLS, IoT devices, etc.)",
            "Wildcard certs (blast radius spans many services)",
        ],
        'when_dont_skip': [
            "\"cert-manager handles it\" — cert-manager can fail silently; verify anyway",
            "\"It's an internal cert\" — internal cert expiry causes internal incidents",
        ],
        'red_flags': [
            "Renewing with less than 7 days to expiry (no room to recover)",
            "Renewing during peak traffic hours",
            "Deploying the new cert without keeping the old one available for rollback",
            "Testing only with `curl` (browsers cache differently, mobile clients differ)",
            "Auto-renewal but no monitoring on whether it succeeded",
        ],
        'common_mistakes': [
            "New cert missing an intermediate in the chain (works in browsers, fails in strict TLS clients)",
            "Forgetting non-HTTP endpoints (mTLS internal APIs, message brokers)",
            "Not updating cert-pinning mobile clients before deploy",
            "Not verifying the cert on non-standard ports (LDAPS, etc.)",
        ],
        'rationalizations': [
            "\"cert-manager renews everything automatically\" — until it doesn't",
            "\"We have 90 days to renew\" — engineers overestimate their own timelines",
            "\"Rollback is easy\" — rollback while the old cert is being served isn't easy if the old cert is already deleted",
        ],
        'phases': [
            ("Prepare the new cert early", [
                "Request / generate the new cert at least 14 days before expiry.",
                "Confirm the cert chain includes the correct intermediate.",
                "Confirm SAN list covers all served hostnames."]),
            ("Deploy without disrupting connections", [
                "Load-balancer reload (not restart) picks up new cert without dropping connections.",
                "Roll out to one instance first if possible; verify before proceeding."]),
            ("Verify with multiple client types", [
                "`curl` from a fresh shell.",
                "A real browser (Chrome, Safari, Firefox).",
                "A mobile app if applicable.",
                "Non-HTTP clients (mTLS callers, message brokers)."]),
            ("Decommission old cert", [
                "Wait 24-48 hours with both certs available (so rollback stays trivial).",
                "Only then remove the old cert files.",
                "Update monitoring / calendar for the next renewal."]),
        ],
        'checklist': [
            "New cert prepared ≥ 14 days before expiry",
            "Cert chain includes intermediate",
            "SAN list covers all hostnames",
            "Deployed via reload, not restart",
            "Verified with browser + curl + non-HTTP clients",
            "Old cert kept available for ≥ 24 hours as rollback",
            "Next-renewal reminder set",
        ],
        'key_principles': [
            "Prepare early, deploy without disruption, verify broadly.",
            "Keep the rollback available before removing it.",
            "Monitor renewal automation; don't assume it worked.",
        ],
        'quick_reference':
            "1. Prepare new cert 14+ days early.\n"
            "2. Verify chain and SAN list.\n"
            "3. Deploy via load-balancer reload.\n"
            "4. Verify from browser, curl, and non-HTTP clients.\n"
            "5. Keep old cert for 24-48 hours.\n"
            "6. Decommission old cert.\n"
            "7. Set next-renewal reminder.\n",
        'example':
            "### Scenario\n\n"
            "`api.example.com` cert expires in 20 days. Currently using a commercial "
            "cert; switching to Let's Encrypt.\n\n"
            "### Applying this skill\n\n"
            "1. Day -14: request new Let's Encrypt cert via cert-manager. Sanity-check "
            "the resulting cert file:\n"
            "   ```\n"
            "   openssl x509 -in new.pem -text -noout | grep -E 'Not After|DNS:'\n"
            "   ```\n"
            "   Confirm expiry is > 60 days out and SAN list covers `api.example.com`.\n"
            "2. Day -14: `openssl s_client -connect api.example.com:443 -showcerts` "
            "against a canary instance with the new cert. Chain looks correct.\n"
            "3. Day -14: verify with browser (visit and inspect cert), with `curl` "
            "(no `--insecure`), with the mobile app's cert-pinning code path.\n"
            "4. Day -14: reload the load balancer to serve the new cert.\n"
            "5. Days -14 to -12: monitor error rate. No issues.\n"
            "6. Day -12: decommission old cert files. Set calendar reminder for next "
            "renewal at day +60.\n\n"
            "Rollback path: if anything failed at step 4, the old cert was still on disk "
            "and a `reload` back to it would take seconds.\n",
        'commands':
            "```bash\n"
            "# Inspect a cert file\n"
            "openssl x509 -in cert.pem -text -noout | grep -E 'Not After|DNS:|Issuer'\n\n"
            "# Test with s_client (shows full chain)\n"
            "openssl s_client -connect api.example.com:443 -showcerts </dev/null\n\n"
            "# Verify chain validity (must succeed with default trust store)\n"
            "openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt cert.pem\n\n"
            "# Days until expiry\n"
            "echo | openssl s_client -connect api.example.com:443 2>/dev/null | \\\n"
            "  openssl x509 -noout -enddate | \\\n"
            "  awk -F= '{ system(\"date -d \\\"\" $2 \"\\\" +%s\") }'\n\n"
            "# Non-HTTP: verify mTLS callers still work\n"
            "openssl s_client -connect internal.example.com:5432 \\\n"
            "  -cert client.crt -key client.key\n"
            "```\n",
        'integration': [
            "Combine with `runbook-writer` — cert renewal deserves a per-service runbook",
            "Follow with `dns-change-safety` if renewal requires DNS validation",
        ],
    },

    # ============================================================
    'dns-change-safety': {
        'title': 'DNS Change Safety',
        'iron_law': 'NO PRODUCTION DNS CHANGE WITHOUT PRE-LOWERING TTL',
        'overview': {
            'iron_law':
                "DNS changes are cache-mediated. If TTL is high when you flip the "
                "record, rollback takes hours — worst possible time.\n\n"
                "**Core principle:** the TTL is the size of your rollback window. "
                "Lower it first, then change, then raise it back.\n",
            'cycle':
                "Lower TTL → wait for propagation → make the change → verify → raise "
                "TTL back. The waits are non-negotiable.\n",
            'practical':
                "This skill covers safe production DNS changes: TTL pre-lowering, "
                "verification with multiple resolvers, and post-change TTL restoration.\n",
            'checklist':
                "DNS change safety is a fixed sequence. The waiting is what makes it safe.\n",
        },
        'when_always': [
            "Any production DNS record change",
            "Any cutover from one hosting provider to another",
            "Any change to MX, TXT (SPF/DKIM), or CNAME records serving live traffic",
        ],
        'when_especially': [
            "Cutting over apex records (`example.com` A/AAAA)",
            "Records currently with TTL > 300 seconds",
            "Records referenced by other systems (CI, monitoring, third-party integrations)",
        ],
        'when_dont_skip': [
            "\"It's just adding a subdomain\" — adding is safe, but confirm no collision first",
            "\"We can rollback via the DNS provider\" — rollback happens at the speed of the cached TTL",
        ],
        'red_flags': [
            "Making the change while TTL is > 300s",
            "Not verifying propagation against public resolvers (1.1.1.1, 8.8.8.8)",
            "Testing only from your own machine (your resolver may already have the new value)",
            "Making DNS + application changes in the same window (can't isolate which broke)",
            "No documented rollback DNS value",
        ],
        'common_mistakes': [
            "Not accounting for the negative TTL (NXDOMAIN caching) when adding a new record",
            "Forgetting to update reverse-DNS (PTR) records",
            "Assuming CNAME chains follow instantly",
            "Not testing the change from the geographies your users are in",
        ],
        'rationalizations': [
            "\"We'll do it during low traffic\" — DNS propagation duration is independent of traffic",
            "\"The provider says 5-minute propagation\" — that's for their nameserver; downstream resolvers cache differently",
        ],
        'phases': [
            ("Lower TTL well in advance", [
                "Change the TTL to 60 seconds (or provider minimum).",
                "Do this at least old-TTL seconds before the planned change window.",
                "Verify the new low TTL from external resolvers."]),
            ("Make the change", [
                "Update the record.",
                "Note the exact time."]),
            ("Verify propagation", [
                "Query from multiple public resolvers.",
                "Query from geographies representative of your users.",
                "Confirm downstream systems see the new value."]),
            ("Restore TTL", [
                "After 24-48 hours of stable operation, restore TTL to the previous higher value.",
                "Higher TTL is cheaper (fewer resolver queries) once you're confident."]),
        ],
        'checklist': [
            "TTL lowered to 60s at least old-TTL seconds ago",
            "Rollback DNS value documented",
            "Change window announced to on-call",
            "Post-change verification against multiple resolvers scheduled",
            "TTL restoration scheduled for +24-48h",
        ],
        'key_principles': [
            "TTL is your rollback window; lower before, raise after.",
            "Verify from resolvers you don't control.",
            "Never change DNS and app in the same window.",
        ],
        'quick_reference':
            "**Timeline for changing a record with 3600s TTL:**\n"
            "```\n"
            "T-4h  → Lower TTL to 60s. Verify.\n"
            "T-0   → Change the record.\n"
            "T+2m  → Verify from 1.1.1.1, 8.8.8.8, EU/APAC resolvers.\n"
            "T+24h → Confirm stable. Raise TTL back.\n"
            "```\n",
        'example':
            "### Scenario\n\n"
            "Cutting `api.example.com` from Cloudfront to a new Fastly config.\n\n"
            "### Applying this skill\n\n"
            "1. Current TTL is 3600s. Change to 60s. Wait > 3600s for propagation. "
            "Verify: `dig +short @1.1.1.1 api.example.com` returns Cloudfront IP with TTL near 60.\n"
            "2. During the change window: update the CNAME from Cloudfront to Fastly.\n"
            "3. Verify propagation:\n"
            "   ```\n"
            "   for r in 1.1.1.1 8.8.8.8 208.67.222.222 9.9.9.9; do\n"
            "     dig +short @$r api.example.com; done\n"
            "   ```\n"
            "   All should return the Fastly hostname within 2 minutes.\n"
            "4. Test from a probe running in each of EU, US-east, APAC.\n"
            "5. If anything fails: revert the CNAME back to Cloudfront. Because TTL is "
            "60s, rollback completes within 2 minutes.\n"
            "6. After 48h of stable traffic on Fastly, raise TTL back to 3600s.\n\n"
            "Total planned window: 5 minutes. Total risk exposure: seconds, not hours.\n",
        'commands':
            "```bash\n"
            "# Query multiple resolvers\n"
            "for r in 1.1.1.1 8.8.8.8 208.67.222.222 9.9.9.9; do\n"
            "  echo -n \"$r: \"\n"
            "  dig +short @$r api.example.com\n"
            "done\n\n"
            "# See TTL to confirm caching behavior\n"
            "dig api.example.com | grep -E 'IN.*A|IN.*CNAME' | head\n\n"
            "# Trace resolution path\n"
            "dig +trace api.example.com\n\n"
            "# Force flush local resolver (for testing)\n"
            "sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder   # macOS\n"
            "sudo systemd-resolve --flush-caches                                # Linux systemd\n"
            "```\n",
        'integration': [
            "Combine with `tls-cert-renewer` if DNS change is for cert validation",
            "Follow with `runbook-writer` if the change coincides with a service migration",
        ],
    },

    # ============================================================
    'backup-restore-drill': {
        'title': 'Backup Restore Drill',
        'iron_law': 'NO BACKUP IS REAL UNTIL YOU HAVE RESTORED IT',
        'overview': {
            'iron_law':
                "Untested backups are wishful thinking. The moment you need the backup "
                "is the worst possible time to discover it's corrupt.\n\n"
                "**Core principle:** the restore is what makes the backup real. Run the "
                "restore quarterly whether you \"need to\" or not.\n",
            'cycle':
                "Pick a backup → restore to an isolated environment → verify integrity "
                "→ document → destroy the restored copy.\n",
            'practical':
                "This skill covers running a scheduled backup restore drill: choosing "
                "which backup to test, restoring safely without touching production, "
                "verifying data integrity, and documenting the outcome.\n",
            'checklist':
                "Restore drill is a fixed quarterly routine. Skip it and you're back "
                "to wishful-thinking backups.\n",
        },
        'when_always': [
            "Every quarter, on schedule",
            "After any change to backup tooling or configuration",
            "After any incident where backups were mentioned as a mitigation",
        ],
        'when_especially': [
            "The backup mechanism has just been changed",
            "New database or storage engine adopted",
            "Recovery Time Objective (RTO) has been renegotiated",
        ],
        'when_dont_skip': [
            "\"The backups are running fine, we can see them in the console\" — presence isn't validity",
            "\"We restored something two years ago\" — three quarters of drift since then",
        ],
        'red_flags': [
            "Restore has never been tested",
            "Last successful drill was more than 6 months ago",
            "Drill was done by restoring to production (potentially destructive)",
            "No documented RTO or the RTO is aspirational",
            "Drill was a partial restore (only some tables); not the same as a full restore",
        ],
        'common_mistakes': [
            "Restoring only the DB but not the associated object storage (files, media)",
            "Restoring but not verifying application-level integrity (referential integrity across services)",
            "Missing the encryption keys — restore succeeds; data is unreadable",
            "Not measuring the actual restore time; the RTO becomes a fiction",
        ],
        'rationalizations': [
            "\"The vendor tests their backups\" — the vendor tests their infrastructure, not your data",
            "\"We can figure it out under pressure\" — that's exactly when drills prove worth",
            "\"It'll cost too much to spin up a restore environment\" — cheaper than an unrestorable production outage",
        ],
        'phases': [
            ("Pick the backup", [
                "Pick a random backup from within the last 30 days.",
                "Do NOT pick the most recent one — that's the one most likely to be tested by default."]),
            ("Restore to an isolated environment", [
                "Never restore to production or to shared staging.",
                "Restore to a scratch account / project / cluster.",
                "Measure the wall-clock time from start to \"restored\"."]),
            ("Verify integrity", [
                "Application-level: run your app against the restored data; smoke tests pass?",
                "Data-level: row counts match backup summary; sample records readable.",
                "Cross-store: files referenced from DB are actually retrievable."]),
            ("Document and destroy", [
                "Log the outcome: restore time, integrity findings, RTO comparison.",
                "Tear down the restored environment.",
                "File follow-up tickets for any drift discovered."]),
        ],
        'checklist': [
            "Backup selected from > 3 days ago (not the newest)",
            "Restored to isolated environment (not production)",
            "Wall-clock restore time measured",
            "Application-level integrity verified",
            "Cross-store references verified",
            "Outcome documented in drill log",
            "Restored environment destroyed",
        ],
        'key_principles': [
            "The restore is the test.",
            "Random backups, not just the latest.",
            "Measure the RTO in seconds, not in vibes.",
        ],
        'quick_reference':
            "**Quarterly drill flow:**\n"
            "1. Pick a backup from 5-25 days ago (random).\n"
            "2. Spin up an isolated environment.\n"
            "3. Restore; time it.\n"
            "4. Verify with smoke tests + data spot checks.\n"
            "5. Log outcome, tear down, file follow-ups.\n",
        'example':
            "### Scenario\n\n"
            "Q3 restore drill for the primary Postgres cluster (`orders-db`).\n\n"
            "### Applying this skill\n\n"
            "1. Chose the July 12 snapshot (3 days old). Not the most recent.\n"
            "2. Spun up a new RDS instance from that snapshot into an isolated VPC.\n"
            "   Wall-clock: 42 minutes from initiation to \"available\". RTO target is 30 min.\n"
            "3. Pointed a copy of the app at the restored DB. Login smoke test passes. "
            "Row counts match backup summary. Sample 100 recent orders — all readable.\n"
            "4. Cross-store check: 50 random `receipt_pdf_url` entries fetched from S3 — "
            "all present.\n"
            "5. Findings: RTO exceeded target by 12 min. Filed ticket to investigate "
            "if larger instance size or faster storage class shortens restore.\n"
            "6. Destroyed the restored RDS instance and VPC. Logged the drill.\n\n"
            "Without the drill, the RTO gap would have surfaced during an actual "
            "incident — with users watching.\n",
        'commands':
            "```bash\n"
            "# List available snapshots\n"
            "aws rds describe-db-snapshots --db-instance-identifier orders-db-prod \\\n"
            "  --query 'DBSnapshots[?SnapshotCreateTime > `2026-06-20`].[DBSnapshotIdentifier,SnapshotCreateTime]' \\\n"
            "  --output table\n\n"
            "# Restore to a new instance\n"
            "aws rds restore-db-instance-from-db-snapshot \\\n"
            "  --db-instance-identifier orders-db-restore-drill \\\n"
            "  --db-snapshot-identifier <chosen-snapshot-id> \\\n"
            "  --db-subnet-group-name drill-vpc-subnet-group\n\n"
            "# Time the restore\n"
            "START=$(date +%s)\n"
            "while [ \"$(aws rds describe-db-instances --db-instance-identifier orders-db-restore-drill \\\n"
            "    --query 'DBInstances[0].DBInstanceStatus' --output text)\" != 'available' ]; do\n"
            "  sleep 30\n"
            "done\n"
            "echo \"Restore took $(( $(date +%s) - START )) seconds\"\n\n"
            "# Verify (application-specific)\n"
            "psql -h <restored-endpoint> -c 'SELECT COUNT(*) FROM orders;'\n\n"
            "# Tear down\n"
            "aws rds delete-db-instance --db-instance-identifier orders-db-restore-drill \\\n"
            "  --skip-final-snapshot\n"
            "```\n",
        'integration': [
            "Combine with `runbook-writer` for the drill outcome runbook",
            "Follow with `incident-triage` if the drill uncovers a genuine restore-blocker",
        ],
    },

    # ============================================================
    'refactor-planner': {
        'title': 'Refactor Planner',
        'iron_law': 'NO REFACTOR WITHOUT A STAY-GREEN SEQUENCE',
        'overview': {
            'iron_law':
                "A refactor that goes red for hours is a refactor that will be "
                "abandoned in the middle, leaving the code worse than before.\n\n"
                "**Core principle:** every step of a refactor keeps the tests green. "
                "If a step can't stay green, split it into smaller steps.\n",
            'cycle':
                "Plan sequence → apply one step → run tests → commit → next step. If "
                "a step goes red, back it out and shrink it.\n",
            'practical':
                "This skill covers planning a multi-file refactor as a sequence of "
                "small always-green steps, each committable independently, each "
                "leaving the codebase in a working state.\n",
            'checklist':
                "Refactor planning is a fixed pre-work exercise. Ten minutes of "
                "planning saves days of thrash.\n",
        },
        'when_always': [
            "Any refactor that touches more than 3 files",
            "Any refactor that changes a widely-used interface",
            "Any refactor a colleague described as \"just cleanup\"",
        ],
        'when_especially': [
            "Refactor that spans a module boundary",
            "Refactor that renames a widely-referenced symbol",
            "Refactor motivated by \"we should have done this differently\"",
        ],
        'when_dont_skip': [
            "\"It's just a rename\" — renames touch caller sites",
            "\"I'll do it as one big commit\" — one big commit means one big revert",
        ],
        'red_flags': [
            "Plan has fewer than 3 steps for a 10+ file refactor",
            "Any step in the plan leaves tests red",
            "Plan modifies behavior AND structure in the same step",
            "Plan is documented only in your head",
            "Estimated time is \"a few hours\" for something touching many modules",
        ],
        'common_mistakes': [
            "Trying to do the whole refactor in one PR (reviewer can't reason about it)",
            "Mixing behavior changes and structural moves",
            "Not using compiler / type-checker as a guide (renames should compile-drive)",
            "Deleting old code before confirming the new code covers all cases",
        ],
        'rationalizations': [
            "\"It's cleaner in one commit\" — cleaner for you to write, harder for others to review",
            "\"I can hold it all in my head\" — until someone interrupts you",
            "\"I'll fix the tests at the end\" — that's the pattern that produces stuck-red refactors",
        ],
        'phases': [
            ("Identify the target shape", [
                "Sketch the desired end state on paper (or in a doc).",
                "Confirm the target shape actually solves the motivating problem."]),
            ("Sequence the steps", [
                "Break the refactor into steps, each stays-green.",
                "Preferred order: add new → migrate callers one at a time → remove old.",
                "Estimate each step in minutes; if any step exceeds 30 min, split further."]),
            ("Apply one step at a time", [
                "Do one step. Run tests. Commit.",
                "Do not batch 2 steps into one commit even if they're small.",
                "If a step goes red: revert, shrink, retry."]),
            ("Cleanup and verify", [
                "After the last step, run the full test suite.",
                "Confirm the new shape matches the plan.",
                "Delete any transitional shims."]),
        ],
        'checklist': [
            "Target shape sketched in writing",
            "Refactor broken into steps that each stay green",
            "Each step estimated at ≤ 30 min",
            "Preferred order used (add → migrate → remove)",
            "Each step committed independently",
            "Final cleanup step removes any shims",
        ],
        'key_principles': [
            "Every step is committable and passes tests.",
            "Add before you remove.",
            "Refactor OR behavior change per commit — never both.",
        ],
        'quick_reference':
            "**Golden sequence for a rename refactor:**\n"
            "1. Add new symbol as alias of old.\n"
            "2. Migrate callers to new symbol (one file per commit).\n"
            "3. Verify no remaining callers of old symbol.\n"
            "4. Remove old symbol.\n\n"
            "Each of the above is a separate commit. Tests green at every step.\n",
        'example':
            "### Scenario\n\n"
            "Renaming a widely-used `Customer.getEmail()` to `Customer.emailAddress()`. "
            "~200 call sites across 40 files.\n\n"
            "### Bad plan\n\n"
            "> Rename in one PR. Fix all 200 call sites in the same commit.\n\n"
            "### Good plan\n\n"
            "1. Add `emailAddress()` as an alias that calls `getEmail()`. Tests green. Commit.\n"
            "2. Migrate callers, batched by directory:\n"
            "   - `src/orders/**` — one commit, tests green.\n"
            "   - `src/billing/**` — one commit, tests green.\n"
            "   - `src/notifications/**` — one commit, tests green.\n"
            "   - `src/admin/**` — one commit, tests green.\n"
            "3. Grep for remaining callers of `getEmail`. Confirm zero.\n"
            "4. Delete `getEmail()`. Tests green. Commit.\n\n"
            "Each step: reviewable in isolation, revertable in isolation, deployable "
            "in isolation.\n",
        'commands':
            "```bash\n"
            "# Find all callers before starting\n"
            "grep -rn '\\.getEmail(' src/ | wc -l          # baseline count\n"
            "grep -rn '\\.getEmail(' src/ | cut -d/ -f2 | sort -u   # directories\n\n"
            "# Track progress\n"
            "grep -rn '\\.getEmail(' src/ | wc -l          # should decrease each commit\n\n"
            "# Semantic rename (compiler-verified) via language server or IDE\n"
            "# For TypeScript: `rename-symbol` refactor\n"
            "# For Python: `rope` or `pyright --rename`\n"
            "# For Java: IntelliJ Refactor > Rename\n\n"
            "# Confirm zero remaining callers before deletion\n"
            "if grep -rn '\\.getEmail(' src/ ; then\n"
            "  echo 'still have callers; cannot delete yet'\n"
            "  exit 1\n"
            "fi\n"
            "```\n",
        'integration': [
            "Combine with `test-first-fix` if the refactor is motivated by a bug",
            "Follow with `pr-description-writer` when opening the PR series",
        ],
    },

    # ============================================================
    'meeting-notes-taker': {
        'title': 'Meeting Notes Taker',
        'iron_law': 'NO DECISION WITHOUT A NAMED OWNER AND A DATE',
        'overview': {
            'iron_law':
                "Decisions without owners get re-discussed. Decisions without dates "
                "get deferred forever. Notes are what convert a meeting into action.\n\n"
                "**Core principle:** the note structure IS the meeting outcome. If it "
                "isn't in the notes, it didn't happen.\n",
            'cycle':
                "Capture during → confirm at end → publish immediately after. Delay "
                "any step and the notes lose accuracy.\n",
            'practical':
                "This skill covers taking effective meeting notes: what to capture "
                "(decisions, actions, questions), what to skip (small talk, "
                "diversions), and how to structure them for later scanning.\n",
            'checklist':
                "Meeting notes are a fixed structure. Fill in the sections during the "
                "meeting.\n",
        },
        'when_always': [
            "Any decision-making meeting",
            "Any meeting with cross-team attendees",
            "Any recurring meeting where continuity matters (standup, planning, review)",
        ],
        'when_especially': [
            "Multiple stakeholders disagree",
            "The meeting produces action items for people not present",
            "The meeting revisits a previous decision",
        ],
        'when_dont_skip': [
            "\"It was a short chat\" — short chats produce decisions that get forgotten",
            "\"Everyone agreed\" — agreement now doesn't survive a week without a written record",
        ],
        'red_flags': [
            "Action item without a name attached",
            "Action item without a due date",
            "Decision described but not summarized in one sentence",
            "Notes not published within 24 hours of the meeting",
            "Notes captured only in someone's private notebook",
        ],
        'common_mistakes': [
            "Trying to capture verbatim (transcription, not notes)",
            "Recording opinions instead of decisions",
            "Not distinguishing decision from discussion",
            "Not including a list of who was present",
        ],
        'rationalizations': [
            "\"We'll remember\" — different attendees remember differently",
            "\"I'll write them up later\" — later is when accuracy has decayed",
            "\"Everyone was there\" — someone will need the record who wasn't",
        ],
        'phases': [
            ("Set up before the meeting", [
                "Create the notes doc from a template.",
                "Populate attendees, date, agenda.",
                "Share the link at the start of the meeting."]),
            ("Capture during the meeting", [
                "Note decisions as they're made — read them back for confirmation.",
                "Note action items in the format `[NAME] verb-phrase — by DATE`.",
                "Note questions raised but not answered separately."]),
            ("Confirm at end", [
                "Read the action items aloud in the last 2 minutes.",
                "Confirm each name accepts theirs.",
                "Confirm each date is realistic."]),
            ("Publish immediately after", [
                "Post the notes to the persistent channel (not just DM).",
                "Tag each action-item owner.",
                "Update the previous meeting's notes with any decisions carried over."]),
        ],
        'checklist': [
            "Notes doc created from template before start",
            "Attendees listed",
            "Decisions captured with one-sentence summary",
            "Action items have owner AND date",
            "Notes read back at end of meeting",
            "Notes published within 24 hours to persistent location",
        ],
        'key_principles': [
            "Read back decisions and actions in the meeting; don't defer confirmation.",
            "Ownerless action items don't get done.",
            "Publish notes before the next meeting on the same topic.",
        ],
        'quick_reference':
            "```markdown\n"
            "# <Meeting title> — <date>\n\n"
            "**Attendees:** <names>\n\n"
            "## Decisions\n"
            "- <one-sentence decision> — decided by <group>\n\n"
            "## Action items\n"
            "- [ ] [@name] Do X by <date>\n"
            "- [ ] [@name] Do Y by <date>\n\n"
            "## Open questions\n"
            "- <question raised but not resolved>\n\n"
            "## Next\n"
            "- <topic for follow-up meeting>\n"
            "```\n",
        'example':
            "### Bad notes\n\n"
            "> Discussed pricing changes. Sarah has concerns about EU market. We'll follow up.\n\n"
            "### Good notes\n\n"
            "```\n"
            "# Pricing changes review — 2026-07-15\n\n"
            "**Attendees:** @sarah, @miguel, @you\n\n"
            "## Decisions\n"
            "- Raise US SMB tier from $49 to $59 effective September 1. Decided by pricing team.\n"
            "- EU pricing DEFERRED pending market analysis (see action items).\n\n"
            "## Action items\n"
            "- [ ] [@miguel] Prepare EU market analysis by 2026-07-31.\n"
            "- [ ] [@you] Update pricing page mockups for new US tiers by 2026-08-01.\n"
            "- [ ] [@sarah] Notify existing US SMB customers 60 days before change → send by 2026-07-31.\n\n"
            "## Open questions\n"
            "- What is our stance on grandfather-clause for annual contracts? (Deferred to next meeting.)\n\n"
            "## Next\n"
            "- Follow-up meeting 2026-08-05 to review EU analysis + open question.\n"
            "```\n",
        'commands':
            "```bash\n"
            "# Standard notes location; one file per meeting\n"
            "mkdir -p docs/meetings/\n"
            "cp docs/meetings/TEMPLATE.md docs/meetings/$(date +%Y-%m-%d)-<slug>.md\n\n"
            "# Publish to Slack after the meeting\n"
            "slack post --channel '#team-decisions' --file docs/meetings/2026-07-15-pricing.md\n\n"
            "# Extract open action items across all meetings\n"
            "grep -rn '^- \\[ \\]' docs/meetings/ | grep '@'\n"
            "```\n",
        'integration': [
            "Follow with `adr-writer` if the meeting produced an architectural decision",
            "Combine with `standup-summarizer` for standup notes",
        ],
    },

    # ============================================================
    'spec-review': {
        'title': 'Spec Review',
        'iron_law': 'NO SPEC REVIEW WITHOUT READING EVERY SECTION',
        'overview': {
            'iron_law':
                "Spec review is where implementation errors are cheapest to catch. "
                "Skimming turns a spec into a formality; substantive review turns it "
                "into a firewall.\n\n"
                "**Core principle:** your job as reviewer is not to nod. It's to find "
                "the gaps the author missed.\n",
            'cycle':
                "Read → identify gaps → ask targeted questions → decide approve/revise. "
                "Every review round narrows the ambiguity.\n",
            'practical':
                "This skill covers how to review a spec / design doc substantively: "
                "what sections deserve most scrutiny, how to phrase questions that "
                "get useful answers, and when to block on gaps versus accept them.\n",
            'checklist':
                "Spec review is a section-by-section pass. Every section gets a "
                "specific set of questions.\n",
        },
        'when_always': [
            "Reviewing any design doc / RFC / spec before implementation starts",
            "Reviewing a spec that supersedes an existing one",
            "Reviewing a spec you'll be a downstream consumer of",
        ],
        'when_especially': [
            "The spec is long (> 5 pages)",
            "You're one of few reviewers with relevant expertise",
            "The spec proposes a departure from existing conventions",
        ],
        'when_dont_skip': [
            "\"I trust the author\" — trust is why they're writing the spec; review is why anyone else reads it",
            "\"It looks well-written\" — well-written specs still have gaps",
        ],
        'red_flags': [
            "Approving without leaving any comments (positive or critical)",
            "Reading only the summary and skipping the details",
            "Deferring questions to \"during implementation\"",
            "Approving \"in principle\" without engaging with specifics",
            "Reviewing after implementation has already started",
        ],
        'common_mistakes': [
            "Focusing only on the proposed design and skipping the alternatives-considered section",
            "Not checking whether stated constraints are actually true",
            "Not asking about the failure modes",
            "Nitpicking style while missing structural issues",
        ],
        'rationalizations': [
            "\"They already thought about it\" — that's why you're reviewing, not implementing",
            "\"I don't have context\" — ask for context; missing context is a spec deficiency",
            "\"It'll work itself out\" — it never works itself out",
        ],
        'phases': [
            ("Read the summary carefully", [
                "One sentence: what is being proposed?",
                "One sentence: what problem does it solve?",
                "If either can't be extracted in one sentence, the spec needs work."]),
            ("Read the alternatives", [
                "Are the alternatives real alternatives, or straw-men?",
                "Are the reasons for rejection specific?",
                "Is there an alternative NOT considered that should be?"]),
            ("Read the proposed design", [
                "For each design decision, ask: what does this commit us to?",
                "For each interface: is the contract explicit?",
                "For each failure mode: is the response specified?"]),
            ("Read the rollout / migration plan", [
                "Can this actually be shipped incrementally?",
                "Is the rollback path viable?",
                "Are downstream consumers accounted for?"]),
        ],
        'checklist': [
            "Summary sentence understood",
            "Alternatives read; any missing alt identified",
            "Design decisions probed for consequences",
            "Failure modes verified as specified",
            "Rollout / migration plan reviewed",
            "Blocking vs non-blocking distinction made explicit in comments",
        ],
        'key_principles': [
            "Find the gaps, don't just nod at the surface.",
            "Ask specific questions, not general concerns.",
            "The alternatives section is often the most informative.",
        ],
        'quick_reference':
            "**Questions worth asking of every spec:**\n"
            "1. What breaks if requirement X changes?\n"
            "2. What is the specific failure mode when dependency Y is unavailable?\n"
            "3. How do we roll this back if it goes wrong?\n"
            "4. What is the migration story for existing users?\n"
            "5. What alternatives did you rule out — and why?\n"
            "6. What operational burden does this add to on-call?\n",
        'example':
            "### Scenario\n\n"
            "Reviewing a 12-page spec proposing to migrate the payment service from a "
            "monolith to microservices.\n\n"
            "### Applying this skill\n\n"
            "1. Summary: extract the one-sentence WHAT and WHY. Spec claims \"scaling "
            "concerns\" but doesn't quantify — first comment.\n"
            "2. Alternatives: spec considers only \"monolith\" and \"microservices\". "
            "What about a modular monolith? Second comment.\n"
            "3. Design: interface contracts between services are described but retry / "
            "timeout semantics are unspecified. Third comment (BLOCKING — this is where "
            "distributed-systems bugs live).\n"
            "4. Rollout: spec proposes a big-bang cutover. What's the incremental path? "
            "Fourth comment (BLOCKING).\n"
            "5. Overall: leave 4 comments, 2 blocking, 2 non-blocking. Request revision "
            "before approving.\n\n"
            "Without step 3, retry / timeout ambiguity would surface as production "
            "incidents six months into the migration.\n",
        'commands':
            "```bash\n"
            "# If the spec is in a Google Doc — nothing to do at the command line\n"
            "# If it's a PR or markdown file, use gh to leave comments:\n\n"
            "gh pr comment 1234 --body 'Blocking: retry/timeout semantics between services not specified. See section 4.2.'\n\n"
            "# Or for markdown-in-repo: leave inline comments on the PR that adds the spec file\n"
            "gh pr diff 1234 --patch | less\n"
            "```\n",
        'integration': [
            "Follow with `adr-writer` — accepted specs often deserve an ADR",
            "Combine with `pr-description-writer` when the spec becomes implementation PRs",
        ],
    },

    # ============================================================
    'perf-profile-reader': {
        'title': 'Performance Profile Reader',
        'iron_law': 'NO OPTIMIZATION WITHOUT A PROFILE',
        'overview': {
            'iron_law':
                "Optimization based on intuition is often wrong. Programs spend time "
                "where you don't expect. The profile is what tells you where.\n\n"
                "**Core principle:** measure before, measure after, keep only the changes "
                "that show up as improvements.\n",
            'cycle':
                "Profile → identify hotspot → hypothesize fix → apply → re-profile. If "
                "the fix didn't move the hotspot, revert it.\n",
            'practical':
                "This skill covers reading profiler output (pprof / flamegraph / async-"
                "profiler / py-spy) to find real hotspots vs perceived ones, and "
                "prioritizing which to address.\n",
            'checklist':
                "Profile reading is a fixed sequence of interpretive questions.\n",
        },
        'when_always': [
            "Any performance regression",
            "Before starting any performance work",
            "After starting any performance work (verify the improvement)",
        ],
        'when_especially': [
            "The perceived slowness doesn't match your mental model",
            "You're about to make a large optimization investment",
            "You've optimized the \"obvious\" thing and it didn't help",
        ],
        'when_dont_skip': [
            "\"I know where the slow part is\" — you know where you think it is",
            "\"The profiler is complex\" — spending an hour learning it saves days of misguided work",
        ],
        'red_flags': [
            "Optimizing without measuring first",
            "Reading only the top of the profile and missing broader distribution",
            "Using a profile from a workload that doesn't match production",
            "Attributing cost from CPU% alone when the workload is I/O bound",
            "Making multiple changes at once so you can't attribute improvement",
        ],
        'common_mistakes': [
            "Confusing self-time with total-time (the hot function may not be the cause)",
            "Not sampling long enough (short profiles miss cold-start / warmup dynamics)",
            "Ignoring GC pauses in memory-managed languages",
            "Optimizing microbenchmarks that don't reflect production shape",
        ],
        'rationalizations': [
            "\"I've optimized this pattern before\" — the pattern; not necessarily this workload",
            "\"The profile is expensive to run\" — cheaper than shipping the wrong optimization",
        ],
        'phases': [
            ("Confirm the workload", [
                "Profile against a workload that resembles production.",
                "Measure for long enough to include warmup + steady state.",
                "Confirm the profiler overhead itself isn't distorting."]),
            ("Read the profile top-down", [
                "Which functions have highest total-time? (may not be self-time hotspots)",
                "Which have highest self-time? (actual computational cost)",
                "Which allocations dominate? (memory profile)"]),
            ("Form a hypothesis", [
                "For the top hotspot: why is it hot? (algorithm, data shape, memory)",
                "Write down expected impact of the proposed fix."]),
            ("Verify after change", [
                "Re-profile with the same workload.",
                "Confirm hotspot moved (or shrunk).",
                "If not: revert; find a different fix."]),
        ],
        'checklist': [
            "Baseline profile captured against production-shape workload",
            "Read total-time and self-time separately",
            "Hypothesis written down before making changes",
            "Post-change profile captured against the same workload",
            "Improvement verified as actual (not workload variance)",
        ],
        'key_principles': [
            "Measure before, measure after.",
            "Self-time and total-time are different questions.",
            "The intuitive hotspot is often not the real one.",
        ],
        'quick_reference':
            "1. Capture baseline profile.\n"
            "2. Read top self-time and total-time separately.\n"
            "3. Hypothesize a fix; write down the expected impact.\n"
            "4. Apply the fix.\n"
            "5. Re-profile.\n"
            "6. Verify hotspot moved. If not, revert.\n",
        'example':
            "### Scenario\n\n"
            "Web service p99 latency is 800ms, target 200ms. Team suspects the ORM.\n\n"
            "### Applying this skill\n\n"
            "1. Capture baseline pprof against a load-test that matches production "
            "request mix. Sample for 5 minutes.\n"
            "2. Read top-down. Top total-time: `handle_request` (100% obviously). "
            "Top self-time: `json.Marshal` (28%). ORM `Query.All` is 14%.\n"
            "3. Surprise: JSON marshalling is a bigger deal than the ORM. Team's intuition "
            "was wrong.\n"
            "4. Hypothesis: `json.Marshal` cost is dominated by reflection on a large "
            "struct with many optional fields. Try switching to code-generated marshalling "
            "(easyjson).\n"
            "5. Apply the fix. Re-profile. Self-time of marshalling drops from 28% to 3%. "
            "p99 drops to 380ms.\n"
            "6. Second pass: now the ORM is the top hotspot. Optimize that next.\n\n"
            "Without step 2, the team would have spent a week optimizing the ORM for "
            "a 14% win instead of the marshalling for a 25% win.\n",
        'commands':
            "```bash\n"
            "# Go: capture 30-second CPU profile\n"
            "curl -o cpu.pprof 'http://localhost:6060/debug/pprof/profile?seconds=30'\n"
            "go tool pprof -http :8080 cpu.pprof\n\n"
            "# Python: py-spy record\n"
            "py-spy record -o profile.svg --duration 60 --pid $(pgrep -f myapp)\n\n"
            "# Java: async-profiler\n"
            "./profiler.sh -d 30 -f flamegraph.html <pid>\n\n"
            "# Read top self-time and top total-time separately\n"
            "go tool pprof -top -cum cpu.pprof | head -20    # total-time\n"
            "go tool pprof -top cpu.pprof | head -20         # self-time\n"
            "```\n",
        'integration': [
            "Follow with `root-cause-first` when a perf regression is intermittent",
            "Combine with `test-first-fix` when a perf regression has a specific reproducer",
        ],
    },

    # ============================================================
    'shell-command-explainer': {
        'title': 'Shell Command Explainer',
        'iron_law': 'NEVER RUN A COMMAND YOU DO NOT UNDERSTAND',
        'overview': {
            'iron_law':
                "Shell commands pasted from Stack Overflow or Slack have wiped out "
                "production databases before. Understanding the command is what "
                "prevents that.\n\n"
                "**Core principle:** if you can't explain what the command does, you "
                "can't recover from what it did.\n",
            'cycle':
                "Read → decompose → predict effect → decide → run. Every unfamiliar "
                "command goes through the cycle.\n",
            'practical':
                "This skill covers safely interpreting an unfamiliar shell command "
                "before running it: parsing operators, understanding side effects, "
                "and identifying reversible vs destructive operations.\n",
            'checklist':
                "Command inspection is a fixed short checklist. Two minutes of reading "
                "is cheaper than any destructive command.\n",
        },
        'when_always': [
            "Copying any command from documentation, chat, or the internet",
            "Running any command that uses `rm`, `mv`, `dd`, or `>`",
            "Running any command whose flags you don't recognize",
        ],
        'when_especially': [
            "Command targets production or a shared environment",
            "Command runs with `sudo` or as a service account",
            "Command uses `xargs`, backticks, or `eval`",
        ],
        'when_dont_skip': [
            "\"It's from a trusted source\" — trusted sources have made typos too",
            "\"I've run it before\" — the context (arguments, cwd, env) may differ this time",
        ],
        'red_flags': [
            "Command uses `rm -rf` with a variable that might expand to empty",
            "Command is chained with `&&`, `;`, or piped in ways you can't fully trace",
            "Command uses `curl <url> | sh` without inspection",
            "Command uses `sudo` for something you don't understand",
            "Command has `--force`, `--yes`, or `-y` flags",
        ],
        'common_mistakes': [
            "Missing that `>` truncates and `>>` appends",
            "Missing shell expansion inside quotes (`\"$var\"` vs `'$var'`)",
            "Missing that `find -delete` doesn't ask for confirmation",
            "Missing side effects of chained pipes (`| tee`, `| sudo`)",
        ],
        'rationalizations': [
            "\"It's just a one-liner\" — one-liners cause the biggest incidents",
            "\"The docs say it's safe\" — safe in the docs' example context, not necessarily yours",
            "\"I need to move fast\" — you need to not destroy things",
        ],
        'phases': [
            ("Decompose the command", [
                "Identify each program invoked.",
                "For each: `--help` or `man` if unfamiliar.",
                "Note pipe boundaries and redirections."]),
            ("Predict the effect", [
                "What files does it read?",
                "What files does it write?",
                "What network calls does it make?",
                "Is it idempotent, or does re-running have compounding effect?"]),
            ("Identify blast radius", [
                "Which resources does it touch? (local files only, external APIs, cloud resources)",
                "Is it reversible?",
                "If reversible, how?"]),
            ("Decide and run", [
                "If understood and reversible → run.",
                "If destructive → dry-run first (--dry-run, -n, --show-changes).",
                "If unclear → don't run; ask or investigate."]),
        ],
        'checklist': [
            "Every program in the command identified",
            "Unfamiliar flags explained (via --help or man)",
            "Files written / deleted identified",
            "Network / cloud calls identified",
            "Reversibility assessed",
            "Dry-run attempted if destructive",
        ],
        'key_principles': [
            "If you can't explain it, don't run it.",
            "Dry-run destructive commands.",
            "Read expansions carefully; the shell does more than you think.",
        ],
        'quick_reference':
            "**Traps to look for in every command:**\n"
            "- `rm -rf $var/` where `$var` might be empty → deletes `/`.\n"
            "- `>` truncates; `>>` appends.\n"
            "- `find ... -delete` doesn't confirm.\n"
            "- `xargs` without `-0` can misinterpret filenames with spaces.\n"
            "- `curl | sh` runs arbitrary code from the network.\n"
            "- `sudo cmd | sudo cmd` — the second sudo prompts again on many systems.\n"
            "- Backticks and `$(...)` execute commands during expansion.\n",
        'example':
            "### Scenario\n\n"
            "Slack DM: \"Hey, quick way to clean up: `find /opt/data -name '*.tmp' -mtime +7 -delete`\"\n\n"
            "### Applying this skill\n\n"
            "1. Decompose: `find` searches, `-name '*.tmp'` matches, `-mtime +7` = older than 7 days, "
            "`-delete` = removes without confirmation.\n"
            "2. Predict: deletes every `*.tmp` file under `/opt/data` modified more than 7 days ago.\n"
            "3. Blast radius: what's in `/opt/data`? Check `ls /opt/data` — includes user-generated "
            "content directories. `*.tmp` matches whatever files users happened to create with that extension.\n"
            "4. Dry-run first: `find /opt/data -name '*.tmp' -mtime +7 -print` — shows 47,832 files, "
            "including several from paying customers' active workspaces.\n"
            "5. Do NOT run the delete. Ask the sender for context on what \"clean up\" was meant.\n\n"
            "Without step 4, you'd have deleted ~48K files and generated a support incident.\n",
        'commands':
            "```bash\n"
            "# Dry-run the destructive version first\n"
            "find /opt/data -name '*.tmp' -mtime +7 -print       # shows what would delete\n"
            "find /opt/data -name '*.tmp' -mtime +7 -print | wc -l  # counts\n"
            "find /opt/data -name '*.tmp' -mtime +7 -print | head   # samples\n\n"
            "# Only then run the actual delete\n"
            "find /opt/data -name '*.tmp' -mtime +7 -delete\n\n"
            "# 'set -x' shows expansions for a scripted command\n"
            "set -x\n"
            "rm -rf \"$VAR\"/subdir\n"
            "set +x\n\n"
            "# Explain a command with explainshell.com (offline: shellcheck for lint)\n"
            "shellcheck script.sh\n"
            "```\n",
        'integration': [
            "Combine with `safe-migration-runner` for DB-touching commands",
            "Follow with `runbook-writer` if the command is one you'll run again",
        ],
    },

    # ============================================================
    'test-coverage-triage': {
        'title': 'Test Coverage Triage',
        'iron_law': 'A COVERAGE DROP IS A CLAIM, NOT A FACT — VERIFY BEFORE BLOCKING',
        'overview': {
            'iron_law':
                "Coverage-gate failures cause more PR thrash than any other CI check. "
                "Most drops are cosmetic; some are real. Distinguishing them is the "
                "actual skill.\n\n"
                "**Core principle:** coverage is a proxy metric. Treat drops as "
                "hypotheses to investigate, not verdicts to enforce.\n",
            'cycle':
                "Coverage drop → inspect diff → categorize → decide block or approve. "
                "Every drop goes through the cycle.\n",
            'practical':
                "This skill covers triaging coverage-tool output: reading the diff "
                "correctly, distinguishing meaningful drops from artifacts, and knowing "
                "when to block a PR vs when to approve with a note.\n",
            'checklist':
                "Coverage triage is a fixed short investigation. Ten seconds to see "
                "a drop, two minutes to investigate.\n",
        },
        'when_always': [
            "CI reports a coverage drop on any PR",
            "Coverage report shows any file below the team's threshold",
            "After a refactor that changed the shape of tested code",
        ],
        'when_especially': [
            "The drop is on code that's about to be shipped to production",
            "The dropped-coverage code was previously well-tested",
            "The drop is concentrated in a small file (may indicate a real gap)",
        ],
        'when_dont_skip': [
            "\"It's only a 0.3% drop\" — small drops on hot-path code matter",
            "\"The overall number is fine\" — average hides individual regressions",
        ],
        'red_flags': [
            "Overriding the coverage gate without a written justification",
            "\"Adding a test\" that touches new lines but doesn't actually assert anything meaningful",
            "Adjusting the coverage threshold downward to make CI green",
            "Coverage drops on business-critical files without discussion",
        ],
        'common_mistakes': [
            "Confusing line coverage with branch coverage",
            "Not checking whether the dropped lines are actually executed by any test",
            "Not distinguishing new-code coverage from total coverage in the report",
            "Accepting 100% coverage as evidence of good tests (it's evidence of executed tests)",
        ],
        'rationalizations': [
            "\"It's just a code move\" — moved code should retain the same coverage; check",
            "\"Coverage doesn't matter for this file\" — say so explicitly with a config exclusion",
            "\"Tests are hard to write here\" — hard-to-test often means hard-to-maintain; consider a refactor first",
        ],
        'phases': [
            ("Read the coverage diff", [
                "Get the coverage delta per-file, not just aggregate.",
                "Note which files dropped and by how much."]),
            ("Categorize each drop", [
                "Cosmetic: dead code removed, imports reorganized, generated files.",
                "Structural: refactor moved code without new test coverage.",
                "Genuine gap: new code added, no corresponding tests."]),
            ("Decide per category", [
                "Cosmetic: acknowledge in comment, approve.",
                "Structural: request tests before merging, OR accept with follow-up ticket.",
                "Genuine gap: block until tests added."]),
            ("Update team practice", [
                "If the same file keeps hitting coverage issues, discuss whether the coverage config is wrong OR the tests are missing OR the code is untestable and needs refactor."]),
        ],
        'checklist': [
            "Coverage diff read per-file",
            "Each drop categorized (cosmetic / structural / genuine)",
            "Decision per drop (approve / follow-up ticket / block)",
            "Any config exclusions documented",
        ],
        'key_principles': [
            "Coverage is a proxy metric, not the goal.",
            "Cosmetic vs structural vs genuine — decide per drop, not per PR.",
            "100% coverage isn't the goal; meaningful assertions are.",
        ],
        'quick_reference':
            "**Categorization guide:**\n"
            "| Symptom | Category | Action |\n"
            "|---|---|---|\n"
            "| Dead code removed | Cosmetic | Approve, note in comment |\n"
            "| Imports reorganized | Cosmetic | Approve |\n"
            "| Generated file included | Cosmetic | Exclude in config |\n"
            "| Function moved, tests didn't move | Structural | Request tests OR ticket |\n"
            "| New public function, no test | Genuine gap | Block |\n"
            "| Business-critical branch uncovered | Genuine gap | Block |\n",
        'example':
            "### Scenario\n\n"
            "PR reports overall coverage dropped from 87.4% to 87.1%. CI gate is 87%. "
            "CI says PASS but reviewer catches the drop.\n\n"
            "### Applying this skill\n\n"
            "1. Read per-file diff: 3 files affected.\n"
            "   - `utils/legacy_helper.py`: -60 lines. Cosmetic (dead code removal).\n"
            "   - `orders/pipeline.py`: -0.4% coverage. New function `fast_path` added, no test.\n"
            "   - `docs/generated_api.py`: -15 lines. Cosmetic (generated file).\n"
            "2. Categorize:\n"
            "   - `legacy_helper.py`: cosmetic — approve.\n"
            "   - `pipeline.py`: genuine gap on new business-critical code — block.\n"
            "   - `generated_api.py`: should be in coverage exclusion list — file a config fix.\n"
            "3. Comment on PR: request a test for `fast_path`. Note the coverage config bug separately.\n\n"
            "Overall CI passes because the drop is small in aggregate; per-file investigation "
            "reveals the meaningful gap.\n",
        'commands':
            "```bash\n"
            "# Per-file coverage diff (Python coverage.py + diff-cover)\n"
            "coverage report --omit='*/generated/*' | tail -n +2\n"
            "diff-cover coverage.xml --compare-branch=main\n\n"
            "# Show which specific lines are uncovered in the affected files\n"
            "coverage report --show-missing orders/pipeline.py\n\n"
            "# Exclude generated files from coverage\n"
            "cat >> .coveragerc <<'EOF'\n"
            "[run]\n"
            "omit =\n"
            "    */generated/*\n"
            "    */migrations/*\n"
            "EOF\n"
            "```\n",
        'integration': [
            "Combine with `systematic-code-review` — coverage is one input among many",
            "Follow with `test-first-fix` if the gap is in bug-adjacent code",
        ],
    },

}

# Everything BEYOND this table falls back to a generic pack — see the
# generator (dress_as_skills_v2.py) for how the fallback is composed.
