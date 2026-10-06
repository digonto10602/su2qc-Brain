---
type: "gate"
package: "su2qc-skqd"
gate: "K1_2x3_fpilot"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate K1_2x3_fpilot

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | prompts/27 stage 0b / prompts/32 B: the 2x3 clean-fraction pilot on ibm_kingston, the two signed k = 1 circuits routed as gate K0 with client XY4 (T3), one job of 4 pubs x 1e5; GO-B / GO-A / NO-GO on f_hat_ideal = f_hit / r_nc (measurement gate; no criterion on f) |
| runs on | QPU |
| status | **PASS (8 criteria, 0 failing, 422 s, 2026-10-06 02:33:45 MDT, commit 504d452)** |
| evidence / script | scripts/gate_K1_2x3_fpilot.py |

## Code it exercises

[[skqd.codec]] · [[skqd.hardware]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Dynamical decoupling]] · [[Transpilation and CZ count]] · [[Gate-and-evidence discipline]] · [[ibm_kingston]]
