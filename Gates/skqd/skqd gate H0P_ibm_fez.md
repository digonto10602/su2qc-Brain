---
type: "gate"
package: "su2qc-skqd"
gate: "H0P_ibm_fez"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0P_ibm_fez

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | H0P re-predicted on the live ibm_fez calibration of the session day (prompts/15 D1: the circuits stay frozen, only the prediction is recomputed; prompts/17: submission is keyed on the calibration content) |
| runs on | laptop |
| status | **PASS (18 criteria, 0 failing, 319 s, 2026-09-22 11:46:55 MDT, commit 1e6d7d3) — CALIBRATION RUN (throughput only): the gate criterion was NOT evaluated** |
| evidence / script | scripts/gate_H0.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[ibm_fez]]
