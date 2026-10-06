---
type: "gate"
package: "su2qc-qcadvantage"
gate: "M1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "qca", "pass"]
---
# qca gate M1

Gate of [[su2qc-qcadvantage]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | model correctness (locked tests: G1–G5). Outcome: lattice + H (sparse, Pauli, numba matrix-free). Audit PASS. |
| runs on | cloud session (4 vCPU, 16 GB); no GPU cluster yet |
| status | **PASS (locked acceptance tests green; audit PASS)** |
| evidence / script | tests/acceptance/m1; audits: reports/audits/m1_audit.md |

## Code it exercises

[[su2torus.hamiltonian]] · [[su2torus.lattice]]
