---
type: "gate"
package: "su2qc-skqd"
gate: "L4_fez"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate L4_fez

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | L4 with NoiseModel.from_backend(FakeFez) and transpilation onto the snapshot (H0 rehearsal) |
| runs on | laptop |
| status | **PASS (4 criteria, 0 failing, 450 s, 2026-09-16 12:28:26 MDT, commit 3722018)** |
| evidence / script | scripts/laptop_L4_aer_noise.py |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.codec]] · [[skqd.exact]] · [[skqd.hpc]] · [[skqd.krylov]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Noise models and digital twin]] · [[Transpilation and CZ count]] · [[ibm_fez]]
