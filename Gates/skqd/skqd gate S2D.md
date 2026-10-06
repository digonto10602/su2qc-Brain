---
type: "gate"
package: "su2qc-skqd"
gate: "S2D"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "fail"]
---
# skqd gate S2D

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | device-resolved budget (prompts/12): mean clean-shot fraction f >= 0.1 (worst >= 0.05) per lattice and device; k=1 counts reproduce S2; shot rule of eq. (5) |
| runs on | laptop |
| status | **FAIL (8 criteria, 2 failing, 213 s, 2026-09-16 07:02:12 MDT, commit 89102d2)** |
| evidence / script | scripts/gate_S2D.py |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.codec]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Clean-shot fraction]]
