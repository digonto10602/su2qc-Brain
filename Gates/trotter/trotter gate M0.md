---
type: "gate"
package: "su2qc-trotter"
gate: "M0"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "trotter", "pass"]
---
# trotter gate M0

Gate of [[su2qc-trotter]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | multi-node smoke: the 34-qubit reference in fp64 spread over 32 A100s, 2 steps + 1 echo |
| runs on | Perlmutter GPU via trotter-ci (30 min, 8 nodes, debug queue) |
| status | **PASS (job 58900924, 223 s, 8 nodes)** |
| evidence / script | validation/ci_M0.json |

## Concepts

[[NERSC Perlmutter]]
