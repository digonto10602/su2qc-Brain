---
type: "gate"
package: "su2qc-skqd"
gate: "H0_ddtest_dryrun"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0_ddtest_dryrun

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | one-job A/B test of client-side DD (context-aware, XY4, XY4-long) against the no-DD baseline on the pilot's two k = 1 circuits; adoption by the preregistered ratio rule (measurement gate) -- DRY RUN |
| runs on | see validation JSON |
| status | **PASS (8 criteria, 0 failing)** |
| evidence / script | validation/H0_ddtest_dryrun.json |

## Concepts

[[Dynamical decoupling]] · [[Preregistration]]
