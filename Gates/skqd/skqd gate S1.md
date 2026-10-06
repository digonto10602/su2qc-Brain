---
type: "gate"
package: "su2qc-skqd"
gate: "S1"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate S1

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | emulated support recall >= 0.9 at f >= 0.1 with the production budget; controls table |
| runs on | cloud/laptop CPU |
| status | **PASS (12 criteria, 0 failing, 223 s, 2026-09-14 16:48:20 MDT, commit 57b3bff)** |
| evidence / script | scripts/gate_S1.py |

## Code it exercises

[[skqd.codec]] · [[skqd.controls]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.ml]] · [[skqd.noise]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Noise models and digital twin]]
