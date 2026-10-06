---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/device_req.py"
lines: 243
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.device_req

Module of [[su2qc-skqd]] · `src/skqd/device_req.py` · 243 lines

## What it does (from the module docstring)

> Device-requirement algebra for the amended budget criterion.
>
> The amended criterion (amendment 01, section 1(c); gate S2D) is a condition on the
> clean-shot fraction of a circuit executed on a device,
>
>     f = prod_{2q gates} (1 - eps2) x prod_{1q gates} (1 - eps1) x prod_{measured} (1 - eps_ro)
>       = (1 - eps2)^n_2q (1 - eps1)^n_1q (1 - eps_ro)^n_meas ,
>
> with `mean f >= 0.1` over the circuit set and `worst f >= 0.05`.  Gate S2D evaluates f at
> one declared error triple; this module inverts the same expression, so that a *requirement*
> can be stated as a region in (eps2, eps1, eps_ro) instead of a single number.
>
> Nothing here is a new physics model: `clean_shot_fraction` is the f of `gate_S2D.analyse_rzz`
> written as a function of the gate counts, and every inversion is exact.
>
> Two exact facts are used throughout.
>
> * f depends on the error triple only through the *log-error budget*: taking -log of the
>   expression above, f >= f_target is the half-space
>
>       n_2q eps2~ + n_1q eps1~ + n_meas eps_ro~ <= log(1 / f_target),   eps~ := -log(1 - eps),
>
>   linear in the log-errors eps~ (and, to first order in eps, in the errors themselves).
>   `log_error_budget` returns the weights and the budget of that half-space.
> * f is strictly decreasing in each error, so the requirement on one channel with the other
>   two fixed has a closed form (`required_error`), and the requirement that a *statistic* of f
>   over a circuit set reach a target is found by bisection (`required_error_for_set`).

## Public names

`CircuitCounts`, `clean_shot_fraction`, `circuit_f`, `set_f`, `channel_factor`, `required_error`, `marginal_requirement`, `required_error_for_set`, `uniform_scale_for_set`, `target_with_idle`, `log_error_budget`, `budget_shares`

## Concepts

[[Clean-shot fraction]] · [[Gate-and-evidence discipline]]

## Checked by gates

[[skqd gate Q0P_2x3]] · [[skqd gate S2D_idle]] · [[skqd gate S2_2x4]]
