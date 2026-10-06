---
type: "gate"
package: "su2qc-trotter"
gate: "smoke"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "trotter", "pass"]
---
# trotter gate smoke

Gate of [[su2qc-trotter]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | CUDA-Q nvidia (12-qubit GHZ) and nvidia-fp64 (22-qubit state), package import |
| runs on | Perlmutter GPU via trotter-ci (15 min) |
| status | **PASS (3 checks, job 58841623)** |
| evidence / script | validation/ci_smoke.json |

## Concepts

[[CUDA-Q]]
