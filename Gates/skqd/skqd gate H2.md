---
type: "gate"
package: "su2qc-skqd"
gate: "H2"
status: "open"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "open"]
---
# skqd gate H2

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | 2x3 B=1: cluster energy certified to +-rH <= 0.15; V(1), V(2) intervals containing exact values |
| runs on | QPU |
| status | **open** |
| evidence / script | scripts/gate_H0.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Ritz values and certified bounds]]
