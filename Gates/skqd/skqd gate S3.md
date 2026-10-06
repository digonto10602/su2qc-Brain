---
type: "gate"
package: "su2qc-skqd"
gate: "S3"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate S3

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | Aer device-model recall >= 0.9 for the production set; shot budget fixed |
| runs on | desktop GPU |
| status | **PASS (4 criteria, 0 failing, 248 s, 2026-09-22 18:01:22 PDT, commit n/a) — CALIBRATION RUN (throughput only): the gate criterion was NOT evaluated** |
| evidence / script | scripts/gate_S3.py |

## Concepts

[[Noise models and digital twin]]
