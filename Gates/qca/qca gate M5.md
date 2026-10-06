---
type: "gate"
package: "su2qc-qcadvantage"
gate: "M5"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "qca", "pass"]
---
# qca gate M5

Gate of [[su2qc-qcadvantage]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | classical-campaign code ready for the cluster (reviewer writes tests). Outcome: MPS (quimb) N=24 chi=256 1-F=1.1e-9; resource table N=48–96; config entry point + Slurm placeholders. Audit PASS. |
| runs on | cloud session (4 vCPU, 16 GB); no GPU cluster yet |
| status | **PASS (locked acceptance tests green; audit PASS)** |
| evidence / script | tests/acceptance/m5; audits: reports/audits/m2_m5_audit.md |

## Code it exercises

[[su2torus.lattice]] · [[su2torus.mps]] · [[su2torus.trotter]]

## Concepts

[[Tensor networks (MPS and TEBD)]] · [[Agent routing (planner, executor, reviewer, runner, scribe)]] · [[Perlmutter job queue]]
