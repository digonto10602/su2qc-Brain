---
type: "gate"
package: "su2qc-jepa"
gate: "J1"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "jepa", "fail"]
---
# jepa gate J1

Gate of [[su2qc-jepa]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | training |
| runs on | laptop / Perlmutter |
| status | **FAIL (latest of 9 ledger entries: 9 FAIL)** |
| evidence / script | configs/gates.yaml |

## Preregistered thresholds (`configs/gates.yaml`)

```yaml
J1_training:
  effective_rank_min: 8.0                 # of latent_dim 16
  grounding_r2_min: {energy: 0.887, C_string: 0.99, P_meson: 0.95, P_baryonic: 0.98}  # energy = 0.97 x measured ceiling 0.9145 (decisions/005)
  semigroup_residual_max: 1.0e-3          # relative latent residual of P(2dt) vs P(dt)oP(dt)
  nan_allowed: false
  seeds: 5
```

## Code it exercises

[[su2qc_jepa.gates.j1_training]]

## Concepts

[[Gate-and-evidence discipline]]
