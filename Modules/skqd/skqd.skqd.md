---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/skqd.py"
lines: 559
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.skqd

Module of [[su2qc-skqd]] · `src/skqd/skqd.py` · 559 lines

## What it does (from the module docstring)

> HPC post-processing of a support: projected diagonalization, certification
> and support-quality metrics (Step 5 of the SKQD manual).
>
> Rigorous for any support B:
>     E_R >= E_0                                  (variational)
>     some exact eigenvalue lies in [E_R - r_H, E_R + r_H]     (Weinstein)
> with the Hamiltonian residual r_H = || (H - E_R) psi_R ||, computed with the
> exact H (support B u N(B)).
> Gap-assumed two-sided intervals for E_0:
>     Weinstein:   E_0 in [E_R - r_H, E_R]        if the level nearest E_R is E_0
>     Kato-Temple: E_0 >= E_R - r_H^2 / (alpha - E_R)   if E_R < alpha <= E_1
> The manual uses alpha = second Ritz value (an upper bound of E_1, so the
> interval is labelled gap-assumed); on the simulator we also evaluate the
> rigorous version with alpha = exact E_1 and check whether E_0 lies inside.
>
> Support metrics against the exact ground state |Omega>:
>     recall R_eps = |B n S_eps| / |S_eps|,  S_eps = smallest set carrying 1 - eps,
>     false positives = |{ b in B : |<b|Omega>|^2 < 1e-8 }|,
>     error = E_R - E_0.
>
> Symbols: B = support (set of basis indices), H_B = P_B H P_B, psi_R = Ritz vector.

## Uses

[[skqd.controls]]

## Used by

`skqd.controls`

## Public names

`RitzResult`, `ritz`, `closure_diagnostic`, `Certificate`, `certify`, `exact_support`, `support_metrics`, `interval_difference`, `poisson_lambda_star`, `shot_rule`, `yield_model`, `clean_fraction_from_yield`, `near_clean_yield`, `clean_fraction_mixture`, `reference_string_test`, `pooled_reference_string_test`, `corrected_clean_fraction`, `h1_energy_tolerance`

## Concepts

[[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Ritz values and certified bounds]] · [[Exact diagonalization]]

## Checked by gates

[[skqd gate CF_traj]] · [[skqd gate H0]] · [[skqd gate H0P]] · [[skqd gate H0P_ibm_fez]] · [[skqd gate H0P_rehearsal]] · [[skqd gate H0_2x2]] · [[skqd gate H0_canary]] · [[skqd gate H0_ddrep]] · [[skqd gate H0_ddtest]] · [[skqd gate H0_diag]] · [[skqd gate H0_dryrun]] · [[skqd gate H0_kpilot]] · [[skqd gate H0_model]] · [[skqd gate H1]] · [[skqd gate H2]] · [[skqd gate K1_2x3_fpilot]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate Q0P_2x3]] · [[skqd gate S1]] · [[skqd gate S2D]] · [[skqd gate S2D_idle]] · [[skqd gate S2D_levers]]
