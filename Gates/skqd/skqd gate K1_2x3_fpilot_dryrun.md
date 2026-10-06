---
type: "gate"
package: "su2qc-skqd"
gate: "K1_2x3_fpilot_dryrun"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate K1_2x3_fpilot_dryrun

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | the 2x3 clean-fraction pilot on ibm_kingston: two signed k = 1 circuits (largest p_ref per sector), routed as gate K0, ALAP + client XY4 (T3), 1e5 shots each, read by the preregistered GO-B / GO-A / NO-GO rule on f_hat_ideal = f_hit / r_nc (measurement gate) -- DRY RUN (path check) |
| runs on | see validation JSON |
| status | **PASS (9 criteria, 0 failing)** |
| evidence / script | validation/K1_2x3_fpilot_dryrun.json |

## Concepts

[[Baryon-number sectors]] · [[Dynamical decoupling]] · [[Transpilation and CZ count]] · [[Gate-and-evidence discipline]] · [[Preregistration]] · [[ibm_kingston]]
