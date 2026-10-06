---
type: "gate"
package: "su2qc-qcadvantage"
gate: "M3"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "qca", "pass"]
---
# qca gate M3

Gate of [[su2qc-qcadvantage]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | small-torus physics (locked tests). Outcome: 18 N=12 + 6 N=24 runs + open string; E conserved < 1e-7. Audit: report wording fixed (B1–B3). Key finding: stripe/neel_half have β=0 on even-L1 tori (incl. N=48 frontier torus); abelian <H_E>(t) exactly constant there (symmetry). |
| runs on | cloud session (4 vCPU, 16 GB); no GPU cluster yet |
| status | **PASS (locked acceptance tests green)** |
| evidence / script | tests/acceptance/m3; audits: reports/audits/m2_m5_audit.md |

## Code it exercises

[[su2torus.hamiltonian]] · [[su2torus.lattice]] · [[su2torus.observables]] · [[su2torus.thermal]]
