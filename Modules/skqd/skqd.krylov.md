---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/krylov.py"
lines: 191
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.krylov

Module of [[su2qc-skqd]] · `src/skqd/krylov.py` · 191 lines

## What it does (from the module docstring)

> Support-generating states (Step 4 of the SKQD manual), emulated exactly in
> the gauge-invariant basis.
>
>   * exact Krylov states      |psi_k> = exp(-i k H dt) |b0>,  k = 0 .. d-1
>   * first-order Trotter      |psi_k> = [ prod_gamma exp(-i H_gamma dt) ]^k |b0>
>   * coarse single-step       |psi_k> =   prod_gamma exp(-i H_gamma k dt)   |b0>   (one step per circuit)
> with the term groups gamma = diagonal (mass + electric), one group per hopping
> link, one per plaquette, applied in that order (the order is a convention of
> this package; it matters for the Trotterised and coarse states, not for the
> exact Krylov states).
>
> Reference configurations (Step 4.2): the Dirac sea, the one-meson
> configurations (quark on the even end, hole on the odd end, flux on the link),
> the diquark on each even site (B = 1), and for static sectors the flux string
> along the bottom row plus its one-plaquette deformations.
>
> Symbols: dt = pi / W_B Krylov time step, d = number of Krylov states,
> b0 = reference configuration, H_gamma = term group.

## Uses

[[skqd.basis]] · [[skqd.exact]] · [[skqd.hamiltonian]]

## Used by

`skqd.circuits_ir` · `skqd.ml`

## Public names

`basis_vector`, `exact_krylov_states`, `apply_groups`, `trotter_states`, `coarse_states`, `term_groups`, `sample_counts`, `dirac_sea`, `one_meson_references`, `diquark_references`, `string_references`, `references`, `ideal_sector_distribution`

## Concepts

[[Gauss's law]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Baryon-number sectors]] · [[String breaking]] · [[Electric basis]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Krylov subspace and Lanczos]] · [[Trotter and Strang splitting]] · [[Noise models and digital twin]]

## Checked by gates

[[skqd gate H0P]] · [[skqd gate H0_2x2]] · [[skqd gate H0_model]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate L2]] · [[skqd gate L3]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate L5]] · [[skqd gate Q0P_2x3]] · [[skqd gate S1]] · [[skqd gate S2]] · [[skqd gate S2D]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
