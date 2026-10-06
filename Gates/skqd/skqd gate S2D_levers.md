---
type: "gate"
package: "su2qc-skqd"
gate: "S2D_levers"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate S2D_levers

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | 2x2 duration levers on ibm_kingston: compile/schedule levers measured, f predicted at both T2 ends, r_crit (measurement gate; no budget criterion) |
| runs on | laptop |
| status | **PASS (9 criteria, 0 failing, 489 s, 2026-10-02 11:13:55 MDT, commit 782580c)** |
| evidence / script | scripts/gate_S2D_levers.py |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.codec]] · [[skqd.coherence]] · [[skqd.exact]] · [[skqd.hardware]] · [[skqd.idle]] · [[skqd.krylov]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Decoherence (T1 and T2)]] · [[ibm_kingston]]
