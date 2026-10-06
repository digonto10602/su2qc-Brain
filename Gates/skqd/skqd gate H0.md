---
type: "gate"
package: "su2qc-skqd"
gate: "H0"
status: "open"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "open"]
---
# skqd gate H0

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | 2x2 hardware: decoder validity, bit order, parity checks; measured f within 30% of the model |
| runs on | QPU |
| status | **open** |
| evidence / script | scripts/gate_H0.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Codewords and the Gauss-law decoder]]
