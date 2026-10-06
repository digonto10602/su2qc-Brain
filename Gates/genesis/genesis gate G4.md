---
type: "gate"
package: "genesis-su2-lgt"
gate: "G4"
status: "partial"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "partial"]
---
# genesis gate G4

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | native cross-language kernels |
| runs on | NumPy reference |
| status | **PARTIAL; OpenMP/CUDA pass, CUDA-Q unavailable and skipped** |
| tolerance | complex128/double absolute error < 1e-12 |
| evidence / script | CTest OpenMP/CUDA smoke and cross-language checks; `benchmarks/results/native_benchmarks.json` |

## Concepts

[[CUDA-Q]]
