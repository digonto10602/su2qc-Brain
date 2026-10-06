---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/exact.py"
lines: 104
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.exact

Module of [[su2qc-skqd]] · `src/skqd/exact.py` · 104 lines

## What it does (from the module docstring)

> Exact sector references (Step 1.3 / Table 1 of the SKQD manual).
>
> For a sector block H_B (baryon number B) we report
>     E0, the next levels, the spectral width W = Emax - Emin, the Krylov time
>     step Delta_t = pi / W (anti-aliasing condition), the ground-state support
>     sizes S_eps (smallest set of configurations carrying 1 - eps of the
>     ground-state weight, eps = 1e-2 and 1e-3) and the participation ratio
>     PR = 1 / sum_b |<b|Omega>|^4.
>
> Dense diagonalization for dim <= DENSE_MAX, Lanczos (scipy eigsh) above.

## Uses

[[skqd.basis]] · [[skqd.hamiltonian]] · [[skqd.lattice]]

## Used by

`skqd.circuits_ir` · `skqd.krylov` · `skqd.reference_sim`

## Public names

`mass_default`, `SectorReference`, `support_size`, `sector_reference`, `Model`

## Concepts

[[Baryon-number sectors]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Krylov subspace and Lanczos]] · [[Exact diagonalization]]

## Checked by gates

[[skqd gate E3]] · [[skqd gate H0]] · [[skqd gate H0P]] · [[skqd gate H0P_ibm_fez]] · [[skqd gate H0P_rehearsal]] · [[skqd gate H0_canary]] · [[skqd gate H0_diag]] · [[skqd gate H0_dryrun]] · [[skqd gate H0_model]] · [[skqd gate H1]] · [[skqd gate H2]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate L2]] · [[skqd gate L3]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate L5]] · [[skqd gate Q0P_2x3]] · [[skqd gate S1]] · [[skqd gate S2]] · [[skqd gate S2D]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
