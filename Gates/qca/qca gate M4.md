---
type: "gate"
package: "su2qc-qcadvantage"
gate: "M4"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "qca", "pass"]
---
# qca gate M4

Gate of [[su2qc-qcadvantage]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | noisy emulation and error mitigation (reviewer writes tests). Outcome: N=12 exact density matrix; ZNE cuts <H_E> error 5.8–15.5x (4/4); echo F within 3–13% of prod(1-15p2/16); global rescaling makes errors worse. Audit PASS. |
| runs on | cloud session (4 vCPU, 16 GB); no GPU cluster yet |
| status | **PASS (locked acceptance tests green; audit PASS)** |
| evidence / script | tests/acceptance/m4; audits: reports/audits/m2_m5_audit.md |

## Code it exercises

[[su2torus.lattice]] · [[su2torus.noise]] · [[su2torus.trotter]]

## Concepts

[[Noise models and digital twin]] · [[Agent routing (planner, executor, reviewer, runner, scribe)]] · [[Zero-noise extrapolation]]
