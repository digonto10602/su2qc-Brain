---
type: "gate"
package: "su2qc-skqd"
gate: "H1"
status: "open"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "open"]
---
# skqd gate H1

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | 2x3 B=0: certified interval of width <= 0.1 containing the exact E0; recall >= 0.8 |
| runs on | QPU |
| status | **open** |
| evidence / script | scripts/gate_H0.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Ritz values and certified bounds]]
