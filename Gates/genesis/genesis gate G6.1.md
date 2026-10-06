---
type: "gate"
package: "genesis-su2-lgt"
gate: "G6.1"
status: "completed-negative"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "completed-negative"]
---
# genesis gate G6.1

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | finite-shot kernel |
| runs on | analytic FidelityStatevectorKernel |
| status | **COMPLETED-NEGATIVE; 512-shot QSVR unstable** |
| tolerance | seeded uncertainty and matrix error recorded |
| evidence / script | `tests/test_qml_finite_shot.py`, `benchmarks/results/qml_finite_shot.json` |

## Code it exercises

[[genesis_su2.qml.energy_surrogate]]

## Concepts

[[Quantum kernel methods]]
