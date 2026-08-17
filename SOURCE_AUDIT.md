# Source and provenance audit

## Paper identity

- Title: **A³: an Analytical Low-Rank Approximation Framework for Attention**
- Authors: Jeffrey T. H. Wong, Cheng Zhang, Xinye Cao, Pedro Gimenes, Christos-Savvas Bouganis, George Anthony Constantinides, Wayne Luk, and Yiren Zhao
- arXiv: [2505.12942](https://arxiv.org/abs/2505.12942)
- OpenReview: [aeeo8ZAftQ](https://openreview.net/forum?id=aeeo8ZAftQ)
- Project page: [jeffreywong20.github.io/a3.github.io](https://jeffreywong20.github.io/a3.github.io/)
- Former collection repository: <code>icml26-repro-aeeo8ZAftQ-analytical-low-rank-attention</code>
- Current collection repository: <code>icml26-a3-analytical-low-rank-attention</code>

## Pinned source

The source archive and PDF are retained under <code>evidence/source/</code>:

| Artifact | SHA-256 |
| --- | --- |
| arxiv_source.tar.gz | <code>98b5c258ec9f331d44d748afa1681058849f4b25a52fc4a8d8238abe82e325c0</code> |
| paper.pdf | <code>6fcb09f188b7c8723c9fc8e8afbf8447837ace219377b9c4147c0fe5bdf46e2b</code> |

The source locations used by the audit are the method equations in
<code>sections/03_method.tex</code>, the PPL and accuracy tables, and the
throughput figure/profiling description. The source archive contains reported
numbers and method text but not every model checkpoint, calibration dump,
baseline pin, or raw benchmark output required to independently rerun the
tables.

## Official implementation

The paper links [DeepWok/a3](https://github.com/DeepWok/a3). This audit pins
its <code>master</code> tip to:

    f688fc5d270ea9185fe29ea656bf168f0fab787a

The official workflow is:

    collect calibration activations -> approximate component state dictionaries -> eval PPL/lm-eval/profiling

The read-only audit found the CLI, model configurations, approximation
modules, harness task configuration, and profiling utilities. It did not find
the large model checkpoints or a complete source-faithful bundle of the
reported experiments. The author repository and its branches are provenance
only; this collection repository does not edit or rename them.

## Target and metric boundary

The paper's benchmark claims depend on model architecture, calibration data,
compression ratios, tokenizer/dataset preprocessing, baseline implementation,
hardware, and metric configuration. The local Claim 5 fixture intentionally
uses finite synthetic matrices and reports relative errors, so it is not a
substitute for WikiText-2 perplexity, five-task accuracy, or A100 throughput.
