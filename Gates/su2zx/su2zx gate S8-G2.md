---
type: "gate"
package: "SU2ZX"
gate: "S8-G2"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "su2zx", "pass"]
---
# su2zx gate S8-G2

Gate of [[SU2ZX]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | Section 8 v0.5.0 overnight run - criteria: expm_vs_krylov, energy_conservation, N_conservation, mass_scan_table, resonance_reported, mass_scan_points, g2_values, timeseries_table, truncation_error_doc, truncation_max_dprob, window_exists, window_g2 |
| runs on | laptop (twin mode, FakeTorino) |
| status | **PASS (20 criteria, 0 not met; attempt 1)** |
| evidence / script | runs/section8_v0.5.0_20260907T0628Z/gates/gate_G2.py |

## Code it exercises

[[su2qc.dynamics.engine]] · [[su2qc.dynamics.scan]]

## Concepts

[[Link truncation (j_max)]]
