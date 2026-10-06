---
type: "gate"
package: "su2qc-skqd"
gate: "H0P"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0P

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | H0 preparation on a calibration snapshot: frozen circuit set leak-free, predicted yield per repetition, readout confusion, Ritz consistency |
| runs on | laptop |
| status | **PASS (16 criteria, 0 failing, 1179 s, 2026-09-16 13:15:46 MDT, commit 2392fb3)** |
| evidence / script | scripts/gate_H0P.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.hardware]] · [[skqd.idle]] · [[skqd.krylov]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Ritz values and certified bounds]] · [[Clean-shot fraction]] · [[Readout error and confusion matrix]]
