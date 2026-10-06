---
type: "gate"
package: "su2qc-skqd"
gate: "K0_2x3_2x4"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate K0_2x3_2x4

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | ibm_kingston readiness of 2x3 and 2x4 on a calibration record: routed CZ, gate-only, idle-aware and XY4-transfer f (prompts/25 Part A) |
| runs on | see validation JSON |
| status | **PASS (6 criteria, 0 failing)** |
| evidence / script | validation/K0_2x3_2x4.json |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.codec]] · [[skqd.exact]] · [[skqd.hardware]] · [[skqd.idle]] · [[skqd.krylov]] · [[skqd.reference_sim]] · [[skqd.report]]

## Concepts

[[Dynamical decoupling]] · [[Decoherence (T1 and T2)]] · [[Transpilation and CZ count]] · [[ibm_kingston]]
