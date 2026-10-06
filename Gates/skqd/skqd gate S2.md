---
type: "gate"
package: "su2qc-skqd"
gate: "S2"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "fail"]
---
# skqd gate S2

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | routed CZ per coarse step <= 500 on the target map (<= 250 at 2x2); compiled circuits leak-free |
| runs on | laptop |
| status | **FAIL (5 criteria, 2 failing, 436 s, 2026-09-15 15:12:59 MDT, commit 5d60461)** |
| evidence / script | scripts/gate_S2.py |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.reference_sim]] · [[skqd.report]]

## Concepts

[[Trotter and Strang splitting]] · [[Transpilation and CZ count]]
