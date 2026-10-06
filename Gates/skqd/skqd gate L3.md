---
type: "gate"
package: "su2qc-skqd"
gate: "L3"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "fail"]
---
# skqd gate L3

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | transpiled CZ counts (S2 measurement) |
| runs on | laptop |
| status | **FAIL (2 criteria, 2 failing, 14 s, 2026-09-15 15:04:26 MDT, commit 5d60461)** |
| evidence / script | scripts/laptop_L3_cz_counts.py |

## Code it exercises

[[skqd.circuits_ir]] · [[skqd.circuits_qiskit]] · [[skqd.codec]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.report]]

## Concepts

[[Transpilation and CZ count]]
