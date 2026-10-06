---
type: "gate"
package: "su2qc-skqd"
gate: "H0_model"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0_model

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | post-diction of the H0 hardware counts by the scheduled-Aer model at both ends of the T2 bracket; the clean-yield statistic |
| runs on | laptop |
| status | **PASS (5 criteria, 0 failing, 2 s, 2026-09-30 15:31:18 MDT, commit 6180c6a)** |
| evidence / script | scripts/gate_H0_model.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Clean-shot fraction]] · [[Decoherence (T1 and T2)]] · [[Noise models and digital twin]]
