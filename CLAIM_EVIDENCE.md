# Claim-to-evidence audit

This repository distinguishes source/protocol availability, exact finite
conformance, and paper-scale empirical reproduction. A toy or finite result
does not verify a universal theorem or a large-model benchmark.

## Claim ledger

| Claim | Paper statement | Production path | Result |
| --- | --- | --- | --- |
| C1 | LLaMA 3.1-70B reaches WikiText-2 PPL 4.69 versus SVD-LLM 7.87 at 10% compression. | Pinned source table plus <code>evidence/claim1_attempt1/source_protocol_audit.md</code>; official pipeline is mapped in <code>evidence/official_code_audit.md</code>. | INCONCLUSIVE: required weights, calibration artifacts, baseline pin, and evaluation outputs are unavailable. |
| C2 | LLaMA-2-7B reaches WikiText-2 PPL 5.96 versus 8.78. | Contract row in <code>contract/live_claims.json</code>; no paper-scale run or accepted output bundle. | UNVERIFIED. |
| C3 | LLaMA 3.1-8B reaches WikiText-2 PPL 7.93 versus 19.12. | Contract row in <code>contract/live_claims.json</code>; no paper-scale run or accepted output bundle. | UNVERIFIED. |
| C4 | A³ has higher average downstream accuracy than SVD-LLM across five tasks. | Contract row in <code>contract/live_claims.json</code>; official <code>eval harness</code> path is documented in <code>evidence/official_code_audit.md</code>. | UNVERIFIED. |
| C5 | Theorems 2–3 and Lemma 4 provide the A³-QK, A³-OV, and A³-MLP analytical routes. | <code>src/claim5_a3_conformance.py</code>, five-seed outputs, source excerpts in <code>evidence/claim5_attempt1/</code>, and <code>logbook/claim-5.md</code>. | TOY_FINITE_CONFORMANCE. |
| C6 | Figure 3 reports A³ throughput speedups on an A100 40GB for LLaMA-2-13B. | Contract row in <code>contract/live_claims.json</code>; profiling path in <code>evidence/official_code_audit.md</code>. | UNVERIFIED. |

## C1 — 70B perplexity protocol

The source reports 4.69 for A³ and 7.87 for SVD-LLM at 10% compression.
The source archive preserves the table and method text, but the audited public
artifacts do not contain the LLaMA 3.1-70B weights, calibration activations,
exact compression configuration, SVD-LLM commit, WikiText-2 preprocessing and
evaluation launcher, seeds, or raw output. The official implementation is
pinned and its workflow is documented, but those missing inputs prevent a
source-faithful rerun.

The result is inconclusive, not falsified and not replaced by a smaller model.

## C2 and C3 — additional perplexity rows

The LLaMA-2-7B and LLaMA-3.1-8B rows remain unverified. No local run is
presented as evidence because the repository does not contain the complete
paper-scale weights, calibration artifacts, and evaluation contract needed to
attribute a result to the source claims.

## C4 — downstream accuracy

The source reports an average across ARC-Challenge, BoolQ, Winogrande, GSM8K,
and MMLU. The official code audit identifies the compressed-state and
lm-eval route, but no complete accepted five-task output bundle is present.
The claim remains unverified.

## C5 — finite analytical conformance

The clean-room fixture uses non-isotropic synthetic matrices with dimension
d=12, rank r=4, and seeds 11, 23, 47, 89, and 131. It implements:

1. A³-QK covariance-square-root weighted truncated SVD.
2. A³-OV per-head autocorrelation-weighted truncated SVD.
3. A³-MLP retained-energy channel selection as a CUR-style finite route.

The five-seed means are:

| Component | Activation-aware / retained-energy route | Negative control |
| --- | ---: | ---: |
| QK relative score error | 0.1033238568 | raw SVD 0.2785479061 |
| OV relative score error | 0.1361070573 | raw SVD 0.2860748917 |
| MLP relative error | 0.2948223031 | low-energy selection 0.9579855232 |

The raw-SVD and low-energy controls are predeclared and degrade on every
fixture. The result is a finite implementation conformance toy. It does not
prove the universal statements in Theorems 2–3 or Lemma 4 and does not
reproduce any LLaMA table.

## C6 — A100 throughput

The paper's Figure 3 route requires LLaMA-2-13B, profiling code, compatible
weights, and an A100 40GB environment. No accepted A100 tokens-per-second or
memory bundle is present. The claim remains unverified.

## Evidence boundary

The source archive, official implementation audit, source excerpts, and finite
outputs are preserved and hash-addressed. The main branch is a documentation
and clean-room conformance entrypoint; absence of a benchmark output is
reported as a limitation rather than silently substituted with a proxy.
