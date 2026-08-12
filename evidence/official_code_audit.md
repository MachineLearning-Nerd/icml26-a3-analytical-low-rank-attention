# Official implementation and branch audit

Audited repository: [`DeepWok/a3`](https://github.com/DeepWok/a3)

Audited default branch: [`master@f688fc5d270ea9185fe29ea656bf168f0fab787a`](https://github.com/DeepWok/a3/tree/f688fc5d270ea9185fe29ea656bf168f0fab787a)

Audit date: 2026-08-13

The paper links this repository as the official implementation. The audit was read-only. No author branch was renamed, rewritten, or pushed to.

## Default branch

`master` at `f688fc5d270ea9185fe29ea656bf168f0fab787a` contains the current implementation and documentation audited for this reproduction. Its relevant workflow is:

1. `experiments/llm/run.py collect` runs the original model over calibration sequences and writes `Rxx` statistics.
2. `experiments/llm/run.py approx` loads the statistics and original state dictionary, then writes reduced QK, VO, and/or FFN state dictionaries.
3. `experiments/llm/run.py eval ppl` or `eval harness` evaluates the resulting model; profiling scripts measure throughput and memory.

The tree includes model configs for LLaMA, MPT, and TinyLlama, approximation modules under `src/a3/`, `lm-eval` task configuration, and documentation under `docs/`. It does not include the paper's large model checkpoints or all reported benchmark artifacts.

## Branches and observed purposes

The purpose descriptions below are based on each branch's tip commit and its file diff against the audited `master` tip. They describe provenance, not claims that every branch is a maintained release.

| Branch | Tip commit | Observed contents / purpose |
| --- | --- | --- |
| `master` | [`f688fc5d`](https://github.com/DeepWok/a3/tree/f688fc5d270ea9185fe29ea656bf168f0fab787a) | Current official implementation, CLI, model/configuration support, documentation, and profiling utilities. |
| `ChengZhang-98-patch-1` | [`0b176828`](https://github.com/DeepWok/a3/tree/0b176828eeeaa19738e49763fd985cffec7bff61) | Historical small patch whose tip is `Update __init__.py`; the relevant change is already reachable from the current `master` history. |
| `cz/iclr25` | [`bf8b6212`](https://github.com/DeepWok/a3/tree/bf8b621221f4c5813466a508113fbecfa075d346) | ICLR-era performance work: token-per-second collection, compression-time profiling, throughput histograms, plots, and a sweep script. |
| `jf` | [`8c9d47cc`](https://github.com/DeepWok/a3/tree/8c9d47cce606ad4101979244ac5022d0a3c85bb7) | Causal-tracer and interpretability experiments, scripts, plots, token-output text, and additional evaluation/rank-search helpers. |
| `phi` | [`082abba2`](https://github.com/DeepWok/a3/tree/082abba25daf92f86821ef52b45398d4f24632b7) | Extended model support and experiments: GPT-2 XL, Phi, PALU/LoRA-related evaluation and fine-tuning, datasets, configs, and model code. |
| `rank-search` | [`d1708a82`](https://github.com/DeepWok/a3/tree/d1708a8286f6d0f81940ac7708c3e5275ab7210c) | Adds a rank-search experiment script for exploring layer/rank allocations. |
| `vc` | [`40afe5de`](https://github.com/DeepWok/a3/tree/40afe5dea977259b9d56759a2289a2fefb22d28b) | Configuration-only updates for the LLaMA-2-7B, LLaMA-3.1-8B, and LLaMA-7B experiments. |

## Claim-to-code map

| Claim | Paper source | Official code path | Produced evidence |
| --- | --- | --- | --- |
| C1–C3 | `tables/tab-main-ppl-full.tex` | model config → `collect` → `approx` → `eval ppl` | WikiText-2/C4/SlimPajama PPL tables |
| C4 | `tables/tab-main-acc-full.tex` | compressed state dictionaries → `eval harness` → `src/harness_tasks/a3_classic.yaml` | ARC-Challenge, BoolQ, Winogrande, GSM8K, MMLU scores and average |
| C5 | `sections/03_method.tex` | `src/a3/approximate/a3/` implementations; this copy also has a finite clean-room fixture | QK/OV/MLP approximation outputs and local error/control metrics |
| C6 | `sections/04_eval.tex`, `figures/fig_tps-llama-2-13b_a100.tex` | `experiments/llm/profile_a3_tps.py` and related profiling scripts | tokens/second, speedup, FLOPs, and peak memory |

The source-to-output path is intentionally kept explicit so a future run can be attached to the exact claim rather than being reported as a generic benchmark.
