# License

This repository **aggregates** content from six upstream research datasets.
Each upstream dataset carries its own license, which continues to apply to
the derived files in this repo.

## Aggregation layer

The **organization, frontmatter schema, extract script, and README** in this
repository are released under the **MIT License** (below).

The **payload text inside each `.md` file** remains under the license of
its upstream source. Redistribution here is done under the terms of those
upstream licenses. If you redistribute this repo further, you must
preserve attribution to the upstream sources listed below.

---

## Upstream sources — attribution & citations

### jailbreak_llms  (bad_jailbreak_llms/)

- **URL:** https://github.com/verazuo/jailbreak_llms
- **License:** MIT
- **Citation:**
  ```
  @inproceedings{shen2024donowknowcharacterizing,
    title  = {"Do Anything Now": Characterizing and Evaluating In-The-Wild
              Jailbreak Prompts on Large Language Models},
    author = {Shen, Xinyue and Chen, Zeyuan and Backes, Michael and
              Shen, Yun and Zhang, Yang},
    booktitle = {ACM Conference on Computer and Communications Security (CCS)},
    year   = {2024}
  }
  ```

### JailbreakBench  (bad_jailbreakbench/)

- **URL:** https://github.com/JailbreakBench/artifacts
- **License:** MIT
- **Citation:**
  ```
  @inproceedings{chao2024jailbreakbench,
    title  = {JailbreakBench: An Open Robustness Benchmark for Jailbreaking
              Large Language Models},
    author = {Chao, Patrick and Debenedetti, Edoardo and Robey, Alexander
              and Andriushchenko, Maksym and Croce, Francesco and Sehwag,
              Vikash and Dobriban, Edgar and Flammarion, Nicolas and
              Pappas, George J. and Tramer, Florian and Hassani, Hamed
              and Wong, Eric},
    booktitle = {NeurIPS Datasets and Benchmarks Track},
    year   = {2024}
  }
  ```

### promptbench  (bad_promptbench/)

- **URL:** https://github.com/microsoft/promptbench
- **License:** MIT
- **Citation:**
  ```
  @article{zhu2023promptbench,
    title  = {PromptBench: Towards Evaluating the Robustness of Large
              Language Models on Adversarial Prompts},
    author = {Zhu, Kaijie and Wang, Jindong and Zhou, Jiaheng and Wang,
              Zichen and Chen, Hao and Wang, Yidong and Yang, Linyi and
              Ye, Wei and Gong, Neil Zhenqiang and Zhang, Yue and Xie,
              Xing},
    journal = {arXiv preprint arXiv:2306.04528},
    year   = {2023}
  }
  ```

### HarmBench  (bad_harmbench/)

- **URL:** https://github.com/centerforaisafety/HarmBench
- **License:** MIT
- **Citation:**
  ```
  @article{mazeika2024harmbench,
    title  = {HarmBench: A Standardized Evaluation Framework for
              Automated Red Teaming and Robust Refusal},
    author = {Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou,
              Andy and Wang, Zifan and Mu, Norman and Sakhaee, Elham
              and Li, Nathaniel and Basart, Steven and Li, Bo and
              Forsyth, David and Hendrycks, Dan},
    journal = {arXiv preprint arXiv:2402.04249},
    year   = {2024}
  }
  ```

### do-not-answer  (bad_do_not_answer/)

- **URL:** https://github.com/Libr-AI/do-not-answer
- **License:** Apache-2.0
- **Citation:**
  ```
  @article{wang2023donotanswer,
    title  = {Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs},
    author = {Wang, Yuxia and Li, Haonan and Han, Xudong and Nakov,
              Preslav and Baldwin, Timothy},
    journal = {arXiv preprint arXiv:2308.13387},
    year   = {2023}
  }
  ```

### prompt-hacker-collections  (bad_prompt_hacker/)

- **URL:** https://github.com/yunwei37/prompt-hacker-collections
- **License:** MIT
- **Citation:** Curated by yunwei37 on GitHub; no formal paper.

---

## MIT License (aggregation layer)

```
MIT License

Copyright (c) 2026 Damon Wischik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
