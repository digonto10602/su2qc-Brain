---
type: "gate"
package: "genesis-su2-lgt"
gate: "G2"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G2

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | two-plaquette exact oracle |
| runs on | independent dense matrix fixture |
| status | **PASS for tested starter observables** |
| tolerance | matrix < 1e-13; eigen residual < 1e-11 |
| evidence / script | `tests/test_su2.py`, `tests/test_pauli.py`, `tests/test_exact.py` |

## Code it exercises

[[genesis_su2.exact]] · [[genesis_su2.pauli]] · [[genesis_su2.su2]]

## Concepts

[[Plaquette and Wilson loop]]
