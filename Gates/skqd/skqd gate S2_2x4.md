---
type: "gate"
package: "su2qc-skqd"
gate: "S2_2x4"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate S2_2x4

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | 2x4 coarse step compiled to exact circuits and verified (measurement gate: counts, duration, idle budget, T2/t_2q requirement; no budget criterion) |
| runs on | laptop |
| status | **PASS (12 criteria, 0 failing, 0 s, 2026-10-01 09:15:29 PDT, commit n/a)** |
| evidence / script | scripts/gate_S2_2x4.py |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.coherence]] · [[skqd.device_req]] · [[skqd.exact]] · [[skqd.hpc]] · [[skqd.idle]] · [[skqd.krylov]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.sparse_sim]]

## Concepts

[[Trotter and Strang splitting]] · [[Decoherence (T1 and T2)]]
