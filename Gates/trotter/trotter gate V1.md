---
type: "gate"
package: "su2qc-trotter"
gate: "V1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "trotter", "pass"]
---
# trotter gate V1

Gate of [[su2qc-trotter]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | scripts/run_cudaq_verify.py --target nvidia-fp64: GPU state-vector verification of the lean circuit (exact and Clifford+T) |
| runs on | Perlmutter GPU via trotter-ci (30 min) |
| status | **PASS (job 58843915, 21 s)** |
| evidence / script | validation/ci_V1.json |

## Code it exercises

[[su2trotter.baseline]] · [[su2trotter.cudaq_backend]] · [[su2trotter.lean]] · [[su2trotter.physics]] · [[su2trotter.pipeline]]

## Concepts

[[CUDA-Q]] · [[Clifford+T and T-count]]
