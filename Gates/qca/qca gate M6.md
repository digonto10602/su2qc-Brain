---
type: "gate"
package: "su2qc-qcadvantage"
gate: "M6"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "qca", "pass"]
---
# qca gate M6

Gate of [[su2qc-qcadvantage]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | convergence evidence and collaborator package (reviewer writes tests). Outcome: N=48 stripe chi 32–256 (chi=256: 6935 s, under the 2 h cap). Converged through step 2, marginal at 3, unconverged from 4; chi=256 cumulative error 0.79 at step 8. Audit PASS after text fixes. Summary: 21 verified numbers. |
| runs on | cloud session (4 vCPU, 16 GB); no GPU cluster yet |
| status | **PASS (locked acceptance tests green; audit PASS)** |
| evidence / script | tests/acceptance/m6; audits: reports/audits/m6_audit.md |

## Concepts

[[Agent routing (planner, executor, reviewer, runner, scribe)]]
