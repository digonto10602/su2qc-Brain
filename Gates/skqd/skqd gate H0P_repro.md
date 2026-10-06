---
type: "gate"
package: "su2qc-skqd"
gate: "H0P_repro"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0P_repro

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | H0 preparation on the FakeFez calibration snapshot: frozen circuit set, predicted yield curve by repetition, readout confusion, Ritz consistency |
| runs on | see validation JSON |
| status | **PASS (15 criteria, 0 failing)** |
| evidence / script | validation/H0P_repro.json |

## Concepts

[[Ritz values and certified bounds]] · [[Clean-shot fraction]] · [[Readout error and confusion matrix]] · [[ibm_fez]]
