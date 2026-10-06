---
type: "gate"
package: "su2qc-skqd"
gate: "CF_traj"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate CF_traj

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | prompts/28 Part A / prompts/29 Part A': Pauli-trajectory decomposition of the A6 Aer channel on the frozen 2x3 circuits; the near-clean term, f_ideal, r_nc (laptop; 0 HQC) |
| runs on | laptop |
| status | **PASS (7 criteria, 0 failing, 1201 s, 2026-10-05 13:47:33 MDT, commit a8ebbaa)** |
| evidence / script | scripts/gate_CF_traj.py |

## Code it exercises

[[skqd.circuits_qiskit]] · [[skqd.quantinuum_native]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Noise models and digital twin]] · [[Quantinuum H-series]]
