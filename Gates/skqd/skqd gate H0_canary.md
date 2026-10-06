---
type: "gate"
package: "su2qc-skqd"
gate: "H0_canary"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "fail"]
---
# skqd gate H0_canary

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | the 3-pub canary of prompts/15 D5 on ibm_fez (one frozen r=1 circuit + the two patch-1 readout circuits): the go rule before the main submission |
| runs on | QPU |
| status | **FAIL (6 criteria, 3 failing, 11 s, 2026-09-30 15:41:49 MDT, commit 6180c6a)** |
| evidence / script | scripts/gate_H0.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Readout error and confusion matrix]] · [[ibm_fez]]
