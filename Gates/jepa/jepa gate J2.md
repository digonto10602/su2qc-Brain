---
type: "gate"
package: "su2qc-jepa"
gate: "J2"
status: "not-run"
generated: True
as_of: "2026-10-06"
tags: ["gate", "jepa", "not-run"]
---
# jepa gate J2

Gate of [[su2qc-jepa]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | forecast |
| runs on | laptop / Perlmutter |
| status | **NOT RUN** |
| evidence / script | configs/gates.yaml |

## Preregistered thresholds (`configs/gates.yaml`)

```yaml
J2_forecast:
  context_step: 4                         # context = noisy observation at step 4 (t = 1/g_E for dt = 0.25)
  context_shots: 512
  targets: [P_baryonic, P_meson, C_string]
  eval_steps: [4, 8]                      # score 4 and 8 steps after the context (t = 2, 3 for dt = 0.25)
  mae_max: 0.05                           # on the held-out split of each family
  must_beat_baselines: [ridge, autoregressive]
  beat_on_at_least: 2                     # of 3 targets (per time)
  beat_margin: 1.1                        # JEPA MAE <= 1.1 x baseline MAE counts as "not worse" (non-inferiority)
  masked_mass_task: true                  # also evaluate with the couplings hidden from the model (system identification)
```

## Code it exercises

[[su2qc_jepa.gates.j2_forecast]]
