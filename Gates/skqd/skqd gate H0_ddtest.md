---
type: "gate"
package: "su2qc-skqd"
gate: "H0_ddtest"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0_ddtest

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | one-job A/B test of client-side DD (context-aware, XY4, XY4-long) against the no-DD baseline on the pilot's two k = 1 circuits; adoption by the preregistered ratio rule (measurement gate) |
| runs on | QPU |
| status | **PASS (8 criteria, 0 failing, 601 s, 2026-10-02 14:37:48 MDT, commit d4b3855)** |
| evidence / script | scripts/gate_H0_ddtest.py |

## Code it exercises

[[skqd.codec]] · [[skqd.idle]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Dynamical decoupling]] · [[Preregistration]]
