---
type: "gate"
package: "su2qc-skqd"
gate: "S2D_idle"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "fail"]
---
# skqd gate S2D_idle

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | Gate S2D's 2x2 criterion (mean f >= 0.1, worst f >= 0.05) re-evaluated on the idle-aware clean-shot fraction, at both ends of the T2 bracket |
| runs on | see validation JSON |
| status | **FAIL (15 criteria, 9 failing)** |
| evidence / script | validation/S2D_idle.json |

## Code it exercises

[[skqd.circuits_qiskit]] · [[skqd.device_req]] · [[skqd.idle]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Clean-shot fraction]] · [[Decoherence (T1 and T2)]] · [[Gate-and-evidence discipline]]
