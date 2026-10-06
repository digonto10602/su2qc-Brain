---
type: "gate"
package: "genesis-su2-lgt"
gate: "G1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G1

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | SU(2) fundamental algebra |
| runs on | explicit 2x2 Pauli generators |
| status | **PASS** |
| tolerance | Frobenius < 1e-12 |
| evidence / script | `tests/test_su2.py` |

## Code it exercises

[[genesis_su2.exact]] · [[genesis_su2.pauli]] · [[genesis_su2.su2]]

## Concepts

[[SU(2) lattice gauge theory]]
