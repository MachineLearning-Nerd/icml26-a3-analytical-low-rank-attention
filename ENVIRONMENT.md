# Environment and reproduction boundary

## Repository contract

- GitHub repository: <code>MachineLearning-Nerd/icml26-a3-analytical-low-rank-attention</code>
- Compute policy: local CPU/local GPU only; no HF Jobs, paid compute, or remote execution.
- Canonical collection branch: <code>main</code>.
- Official implementation environment: documented in the pinned DeepWok/a3 tree; it requires compatible model weights and accelerator resources for the paper benchmarks.

## Finite Claim 5 run

The committed toy was generated with local CPU NumPy:

- d=12, rank r=4;
- qk calibration tokens 96 and kv calibration tokens 80;
- seeds 11, 23, 47, 89, and 131;
- runtime 0.0178266 seconds;
- recorded runtime interpreter: Python 3.14.5;
- verdict: <code>toy</code>.

The command is:

~~~sh
python3 src/claim5_a3_conformance.py \
  --out outputs/claim5_a3_conformance \
  --seeds 11 23 47 89 131
~~~

The raw CSV, configuration, log, summary, source excerpts, and SHA-256
manifests are committed. The conformance result is accepted only as finite
clean-room evidence.

## Unavailable paper-scale requirements

Claims 1–4 require large LLaMA checkpoints, exact calibration and compression
configurations, WikiText-2 and downstream task preprocessing, SVD-LLM
comparator artifacts, and a complete metric output bundle. Claim 6 additionally
requires LLaMA-2-13B profiling on an A100 40GB. None of those requirements is
silently replaced by the finite CPU fixture.
