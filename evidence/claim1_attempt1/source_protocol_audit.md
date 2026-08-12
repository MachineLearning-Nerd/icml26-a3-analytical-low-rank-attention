# Claim 1 — source/protocol audit

## Exact live claim

A3's low-rank approximated LLaMA 3.1-70B achieves WikiText-2 perplexity 4.69 at 10% compression versus SVD-LLM 7.87 (Table 1).

## Pinned evidence

- arXiv `2505.12942`, source archive and PDF: `evidence/source/SHA256SUMS`.
- Retained source table: `tables/tab-main-ppl-full.tex` in the pinned archive.
- Method source: `sections/03_method.tex` in the pinned archive.

## Protocol availability finding

The pinned paper source supplies tables and method TeX but no LLaMA-3.1-70B weights, WikiText-2 preprocessing/evaluation launcher, SVD-LLM pin, compression configuration, calibration activations, seed list, or benchmark outputs. The paper does link the official implementation [`DeepWok/a3`](https://github.com/DeepWok/a3), which is pinned for this audit at commit [`f688fc5d270ea9185fe29ea656bf168f0fab787a`](https://github.com/DeepWok/a3/tree/f688fc5d270ea9185fe29ea656bf168f0fab787a). That repository supplies the collection, approximation, and evaluation code, but its audited tree does not include the 70B checkpoint, calibration statistics, SVD-LLM artifact, or the exact paper run outputs. A claimed 70B perplexity number therefore cannot be independently rerun source-faithfully from the currently available artifacts.

## Outcome

**Inconclusive.** This is a source/protocol audit, not a numerical reproduction, toy, verification, or falsification. The direct local next step targets the separately live mathematical A3-QK/OV/MLP claim with finite matrix conformance tests.
