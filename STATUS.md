# Status

- OpenReview ID: `aeeo8ZAftQ`
- Submission number: `17938`
- Title: *A³: an Analytical Low-Rank Approximation Framework for Attention*
- Live claim count / maximum points: `6 / 12`
- Selection timestamp: `2026-08-02T08:30:41Z`
- Contract manifest: `contract/contract_manifest.json`
- Source paper/version: arXiv `2505.12942` (source archive and PDF SHA-256 pinned)
- Official implementation: [`DeepWok/a3@f688fc5d270ea9185fe29ea656bf168f0fab787a`](https://github.com/DeepWok/a3/tree/f688fc5d270ea9185fe29ea656bf168f0fab787a), audited from `master`
- Compute policy: local CPU/local GPU only; no HF cpu-upgrade, Jobs, paid/remote compute
- Target GitHub repository: `https://github.com/MachineLearning-Nerd/icml26-a3-analytical-low-rank-attention`
- Former GitHub repository: `https://github.com/MachineLearning-Nerd/icml26-repro-aeeo8ZAftQ-analytical-low-rank-attention`
- Current phase: `claim_ledger_and_official_code_audit`
- Branch policy: normalized collection copy has only `main`; author branches are documented, not edited
- Claim 1: inconclusive — paper-scale LLaMA-3.1-70B/WikiText-2 protocol lacks the weights, calibration artifacts, and complete evaluation pin needed for a source-faithful rerun.
- Claim 2: unverified — LLaMA-2-7B WikiText-2 PPL comparison.
- Claim 3: unverified — LLaMA-3.1-8B WikiText-2 PPL comparison.
- Claim 4: unverified — five-task downstream accuracy comparison.
- Claim 5: toy — five-seed local A3-QK/A3-OV/A3-MLP finite conformance fixture; not theorem verification or a paper-scale benchmark.
- Claim 6: unverified — A100 40GB LLaMA-2-13B throughput comparison.
- GitHub documentation publication: ready after metadata normalization and remote verification
- Trackio reproduction publication: not eligible under the current local-only compute policy

## Selection rationale

Selected from the refreshed official eligible pool after duplicate, local-workspace, DineshAI, coordination, and backlog exclusions. It has six live claims, a public source archive, an official implementation, and a directly executable local matrix-algebra route for the analytical component claim. The large-model benchmark claims remain separately labelled until their required weights, configurations, and accelerator runs are available.
