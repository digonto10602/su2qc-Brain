---
type: "gate"
package: "genesis-su2-lgt"
gate: "G3"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G3

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | Qiskit V2 product formula |
| runs on | SciPy exact evolution |
| status | **PASS locally with Qiskit 2.5.1; hardware not run** |
| tolerance | statevector convergence; circuit metrics recorded |
| evidence / script | `tests/test_qiskit_product_formula.py`, `benchmarks/results/qiskit_product_formula.json` |

## Code it exercises

[[genesis_su2.backends.qiskit_backend]] · [[genesis_su2.exact]]

## Concepts

[[Trotter and Strang splitting]] · [[Qiskit]]
