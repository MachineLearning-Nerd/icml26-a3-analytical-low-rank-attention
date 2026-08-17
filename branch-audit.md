# Branch audit

## Collection repository

| Ref | Purpose | Policy |
| --- | --- | --- |
| main | Documentation, pinned source and official-code audit, finite Claim 5 conformance, and verifier. | Canonical public branch. |

The live collection state is intentionally main-only. The former collection
name is retained in the README and source audit for provenance.

## Separate author repository

The linked author implementation <code>DeepWok/a3</code> retains its own
<code>master</code>, <code>ChengZhang-98-patch-1</code>, <code>cz/iclr25</code>,
<code>jf</code>, <code>phi</code>, <code>rank-search</code>, and <code>vc</code>
branches. Their observed tips and purposes are recorded in
<code>evidence/official_code_audit.md</code>. This collection does not modify
those refs.
