---
type: "gate"
package: "su2qc-qcadvantage"
gate: "M2"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "qca", "pass"]
---
# qca gate M2

Gate of [[su2qc-qcadvantage]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | exact dynamics, Trotter circuits, gate counts (locked tests: G6–G8). Outcome: order-1 step = 9.5n (native ZZ) / 11n (CZ), exactly as claimed; order 2: 15n/18n (13.5n/15n fused). Audit PASS. |
| runs on | cloud session (4 vCPU, 16 GB); no GPU cluster yet |
| status | **PASS (locked acceptance tests green; audit PASS)** |
| evidence / script | tests/acceptance/m2; audits: reports/audits/m2_m5_audit.md |

## Code it exercises

[[su2torus.exact]] · [[su2torus.hamiltonian]] · [[su2torus.lattice]] · [[su2torus.trotter]]

## Concepts

[[Trotter and Strang splitting]] · [[Transpilation and CZ count]]
