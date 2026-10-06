---
type: "gate"
package: "su2qc-jepa"
gate: "J3"
status: "not-run"
generated: True
as_of: "2026-10-06"
tags: ["gate", "jepa", "not-run"]
---
# jepa gate J3

Gate of [[su2qc-jepa]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | hardware |
| runs on | laptop / Perlmutter |
| status | **NOT RUN** |
| evidence / script | configs/gates.yaml |

## Preregistered thresholds (`configs/gates.yaml`)

```yaml
J3_hardware:
  residual_spearman_min: 0.7              # Spearman(jepa_twin, exact error) at the low-shot level (512)
  noninferiority_margin: 0.05             # jepa_twin Spearman >= raw_twin Spearman - margin at the low-shot level
  auroc_min: 0.8                          # jepa_twin separates the degraded arm/day from the nominal one (full shots)
  min_points: 24
  low_shot_level: 512
  must_report_baselines: [raw_twin, flag_rate, jepa_self, jepa_t0]
  calibration_days: 3
```

## Code it exercises

[[su2qc_jepa.gates.j3_hardware]]
