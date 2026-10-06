---
type: "gate"
package: "su2qc-trotter"
gate: "B1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "trotter", "pass"]
---
# trotter gate B1

Gate of [[su2qc-trotter]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | scripts/run_benchmark.py: 60-step Trotter evolution of the plaquette on nvidia-fp64 and nvidia, vs exact |
| runs on | Perlmutter GPU via trotter-ci (30 min) |
| status | **PASS (job 58851443, 38 s)** |
| evidence / script | validation/ci_B1.json |

## Code it exercises

[[su2trotter.cudaq_backend]] · [[su2trotter.physics]] · [[su2trotter.pipeline]] · [[su2trotter.trotter]]

## Concepts

[[Plaquette and Wilson loop]] · [[Trotter and Strang splitting]]
