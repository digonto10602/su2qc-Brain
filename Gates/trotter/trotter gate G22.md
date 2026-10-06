---
type: "gate"
package: "su2qc-trotter"
gate: "G22"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "trotter", "pass"]
---
# trotter gate G22

Gate of [[su2qc-trotter]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | scripts/gpu_compare.py: the 8 comparison tests for the 22-qubit lean circuit, fp64 |
| runs on | Perlmutter GPU via trotter-ci (60 min, 1 GPU) |
| status | **PASS (job 58879875, 39 s)** |
| evidence / script | validation/ci_G22.json |

## Code it exercises

[[su2trotter.baseline]] · [[su2trotter.circuit]] · [[su2trotter.cudaq_backend]] · [[su2trotter.lean]] · [[su2trotter.physics]] · [[su2trotter.pipeline]] · [[su2trotter.sim]] · [[su2trotter.trotter]]
