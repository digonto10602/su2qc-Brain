---
type: "gate"
package: "SU2ZX"
gate: "S8-G3"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "su2zx", "pass"]
---
# su2zx gate S8-G3

Gate of [[SU2ZX]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | Section 8 v0.5.0 overnight run - criteria: l12_test_suite, l12_physical_codes, s8_encoding, c7_encoding, block_unitary_dev, block_unitary_leak_prob, noiseless_leakage_prob, trotter_slope_Psurv, trotter_slope_E2, resources_logical, export_l12_r0_qpy, export_l12_r0_qasm |
| runs on | laptop (twin mode, FakeTorino) |
| status | **PASS (18 criteria, 2 not met; attempt 1)** |
| evidence / script | runs/section8_v0.5.0_20260907T0628Z/gates/gate_G3.py |

## Code it exercises

[[su2qc.circuits.strang_l12]] · [[su2qc.encodings.l12]]

## Concepts

[[Leakage-safe data splits]] · [[L12 encoding]]
