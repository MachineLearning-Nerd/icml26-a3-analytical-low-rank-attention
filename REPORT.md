# Scoped reproduction report

## Final verdict

| Claim | Verdict | Meaning |
| --- | --- | --- |
| C1 | INCONCLUSIVE_SOURCE_PROTOCOL | The 70B PPL row cannot be rerun from the available pinned artifacts. |
| C2 | UNVERIFIED | No accepted LLaMA-2-7B PPL reproduction. |
| C3 | UNVERIFIED | No accepted LLaMA-3.1-8B PPL reproduction. |
| C4 | UNVERIFIED | No accepted five-task downstream accuracy bundle. |
| C5 | TOY_FINITE_CONFORMANCE | Five-seed synthetic matrix route with negative controls. |
| C6 | UNVERIFIED | No accepted A100 throughput profile. |

The collection status is a **partial scoped audit**, not a complete
reproduction of the paper's LLaMA benchmarks.

## What is established

The source and official implementation are pinned. The official branch and
workflow are audited, and the finite clean-room fixture follows the stated
activation-aware QK, autocorrelation-weighted OV, and channel-selection MLP
routes on a declared five-seed synthetic matrix contract. Its negative
controls support the local direction of the implementation.

## What is not established

No paper-scale PPL, downstream accuracy, or A100 throughput claim is
independently reproduced here. The finite fixture does not discharge
universal theorem quantifiers or substitute for the missing model weights,
calibration artifacts, baseline pin, data preprocessing, and hardware profile.

## Publication policy

The repository documentation is published for transparent review, but
<code>publication_allowed</code> remains false for a complete-reproduction
conclusion. A future benchmark release must include the exact source-faithful
inputs, accepted raw outputs, configuration, and independently readable hash
manifest for each promoted claim.
