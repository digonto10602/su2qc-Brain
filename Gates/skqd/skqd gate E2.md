---
type: "gate"
package: "su2qc-skqd"
gate: "E2"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate E2

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | counts of Table 2; codec round trip on all 2x3 states; random-bitstring acceptance ~0.15% |
| runs on | cloud/laptop CPU |
| status | **PASS (51 criteria, 0 failing, 15 s, 2026-09-14 16:44:00 MDT, commit 57b3bff)** |
| evidence / script | scripts/gate_E2.py |

## Code it exercises

[[skqd.basis]] · [[skqd.codec]] · [[skqd.lattice]] · [[skqd.report]] · [[skqd.vertex]]

## Concepts

[[Codewords and the Gauss-law decoder]]
