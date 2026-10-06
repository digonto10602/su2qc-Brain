---
type: "gate"
package: "su2qc-trotter"
gate: "G34"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "trotter", "pass"]
---
# trotter gate G34

Gate of [[su2qc-trotter]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | the 8 comparison tests for the 34-qubit reference, fp64, 32 A100s |
| runs on | Perlmutter GPU via trotter-ci (up to 6 h, 8 nodes, regular queue) |
| status | **PASS (job 58918087, 5066 s, 8 nodes)** |
| evidence / script | validation/ci_G34.json |

## Concepts

[[NERSC Perlmutter]]
