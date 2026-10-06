---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/route_gausskernel.py"
lines: 488
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "ham"]
---
# su2qc.ham.route_gausskernel

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/route_gausskernel.py` · 488 lines

## What it does (from the module docstring)

> Route 2: redundant Kogut-Susskind space followed by Gauss-law projection.
>
> Construction:
>   * Each link is a truncated rigid rotor |j, mL, mR> (dim 5 at jmax=1/2).
>   * Matter: 8 Jordan-Wigner fermionic modes in the frozen order (v-major).
>   * The physical basis is built from vertex-local Gauss singlets (codex-built,
>     verified: dims 82/152, sector dims 2,20,38,20,2, electric clusters).
>   * H is built on the FULL redundant space (electric, mass, 4 hoppings with JW
>     strings, plaquette trace) and projected: H_phys = P^dag H_red P.
>   * The U matrix-element convention (which color index is conjugated) is
>     selected NUMERICALLY as the unique variant that makes [G^a_v, H_hop] = 0;
>     the choice is recorded in U_CONVENTION after first build.
>
> Limitation (recorded in run/DECISIONS.md): at jmax=1 only the kernel dimension
> (152) is computed by this route; the projected H_1 matrix is route-1-only
> (redundant dim 14^4*256 ~ 9.8M exceeds the night's memory/time budget).
> Route agreement is gated at jmax=1/2 per the run prompt (G1 criterion 3).

## Uses

[[su2qc.conventions]]

## Used by

`su2qc.ham.compare` · `su2qc.ham.limits`

## Public names

`kernel_dimension`, `gauss_commutator_norms`, `build_hamiltonian`, `build_hamiltonian_no_magnetic`, `get_state`, `E2_link`, `n_op`, `N_total`, `P_surv`, `P_meson`, `P_BBbar`

## Concepts

[[Kogut-Susskind Hamiltonian]] · [[Gauss's law]] · [[Link truncation (j_max)]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Baryon-number sectors]] · [[Electric basis]] · [[Jordan-Wigner mapping]]

## Checked by gates

[[su2zx gate S8-G1]]
