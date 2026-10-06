---
type: "gate"
package: "genesis-su2-lgt"
gate: "G7.2-G7.4"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G7.2-G7.4

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | encoding/Gauss fixture |
| runs on | electric representation and fixed-occupation rishon constructions |
| status | **PASS at validation scale** |
| tolerance | exact algebra/projector residuals < `1e-12`; boundary defects recorded |
| evidence / script | `tests/test_encodings.py`, `docs/ENCODING_DECISION_RECORD_v1.1.0.md` |

## Code it exercises

[[genesis_su2.encodings]]

## Concepts

[[Gauss's law]]
