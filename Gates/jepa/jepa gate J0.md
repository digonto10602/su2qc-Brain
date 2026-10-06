---
type: "gate"
package: "su2qc-jepa"
gate: "J0"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "jepa", "pass"]
---
# jepa gate J0

Gate of [[su2qc-jepa]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | data |
| runs on | laptop / Perlmutter |
| status | **PASS** |
| evidence / script | configs/gates.yaml |

## Preregistered thresholds (`configs/gates.yaml`)

```yaml
J0_data:
  two_route_agreement_max: 1.0e-12        # |H_A - H_B| on the 82-state basis
  gauss_commutator_max: 1.0e-12           # ||[G^a_n, H]|| on the full space
  estimator_bias_sigma: 4.0               # |mean estimate - exact| <= this many standard errors, all observables
  estimator_trials: 200
  estimator_shots: 1024
  twin_distinct_repeats: 5                # all repeated twin runs must give distinct count dictionaries
  krylov_obs_error_max: 1.0e-3            # K = chain_K reproduces the P-A window to this accuracy
  split_leakage_allowed: 0                # trajectories of a held-out mass found in train
```

## Code it exercises

[[su2qc_jepa.gates.j0_data]]
