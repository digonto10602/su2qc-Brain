---
type: "gate"
package: "SU2ZX"
gate: "S8-G1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "su2zx", "pass"]
---
# su2zx gate S8-G1

Gate of [[SU2ZX]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | Section 8 v0.5.0 overnight run - criteria: dim_route1_jmax0.5, dim_route2_jmax0.5, dim_route1_jmax1.0, dim_route2_jmax1.0, sectors_route1, HN_commutator_route1, hermiticity_route1, sectors_route2, HN_commutator_route2, hermiticity_route2, route_spectra_rel_dev, route_time_series_dev |
| runs on | laptop (twin mode, FakeTorino) |
| status | **PASS (17 criteria, 0 not met; attempt 3)** |
| evidence / script | runs/section8_v0.5.0_20260907T0628Z/gates/gate_G1.py |

## Code it exercises

[[su2qc.conventions]] · [[su2qc.ham.compare]] · [[su2qc.ham.limits]] · [[su2qc.ham.route_gausskernel]] · [[su2qc.ham.route_spinnet]]

## Concepts

[[Link truncation (j_max)]] · [[Baryon-number sectors]]
