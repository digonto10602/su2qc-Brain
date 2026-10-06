---
type: "gate"
package: "su2qc-skqd"
gate: "Q0P_2x3"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate Q0P_2x3

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | prompts/26 Stage A: the signed 2x3 circuits compiled to the Quantinuum native gate set (Rz, PhasedX, ZZPhase) for H2-2 / H1-1, verified exactly against the IR, costed in HQC, packaged with the submission path (0 HQC; Stage E emulator and Stage P pilot NOT run: no Nexus login, no budget) |
| runs on | laptop |
| status | **PASS (7 criteria, 0 failing, 926 s, 2026-10-02 21:36:57 MDT, commit 8072b8d)** |
| evidence / script | scripts/gate_Q0P_2x3.py |

## Code it exercises

[[skqd.circuits_qiskit]] · [[skqd.device_req]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.quantinuum_native]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Noise models and digital twin]] · [[Quantinuum H-series]]
