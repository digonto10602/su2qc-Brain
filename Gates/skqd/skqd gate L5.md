---
type: "gate"
package: "su2qc-skqd"
gate: "L5"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate L5

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | CUDA-Q circuits reproduce the numpy reference at 2x2 |
| runs on | laptop GPU |
| status | **PASS (6 criteria, 0 failing, 3 s, 2026-09-15 20:19:58 MDT, commit 0420211)** |
| evidence / script | scripts/laptop_L5_cudaq_check.py |

## Code it exercises

[[skqd.circuits_cudaq]] · [[skqd.circuits_ir]] · [[skqd.codec]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.report]]

## Concepts

[[CUDA-Q]]
