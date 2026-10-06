---
type: "gate"
package: "SU2ZX"
gate: "C0"
status: "partial"
generated: True
as_of: "2026-10-06"
tags: ["gate", "su2zx", "partial"]
---
# su2zx gate C0

Gate of [[SU2ZX]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | GI-cost campaign v0.6.x: V1, V11, Tier 2 pass; V10 distinctness at both r; variance band at r = 0; r = 1 variance recorded not evaluable with kept counts; git status empty after the gate commit |
| runs on | laptop / cluster (Hermes) |
| status | **PARTIAL - open: V10 variance band at r=0: dC ratio 0.2381, open finding; V10 variance band at r=1: not evaluable at 2.6 kept shots; Empty-repeat bootstrap contamination (open finding)** |
| evidence / script | runs/campaign_v060/CAMPAIGN_STATE.json |
