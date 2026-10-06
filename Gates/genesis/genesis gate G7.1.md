---
type: "gate"
package: "genesis-su2-lgt"
gate: "G7.1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G7.1

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | independent frozen-oracle validation |
| runs on | independently entered basis-action matrix |
| status | **PASS** |
| tolerance | matrix <= `1e-12`; spectrum <= `1e-11`; states <= `1e-10` |
| evidence / script | `tests/test_independent_oracle.py`, `benchmarks/results/independent_oracle.json` |

## Code it exercises

[[genesis_su2.exact]] · [[genesis_su2.pauli]]
