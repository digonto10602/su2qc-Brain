---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/physics/conventions.py"
lines: 81
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "physics"]
---
# su2qc_jepa.physics.conventions

Module of [[su2qc-jepa]] · `src/su2qc_jepa/physics/conventions.py` · 81 lines

## What it does (from the module docstring)

> Frozen conventions for the hard-core SU(2) Kogut-Susskind plaquette with
> two-colour staggered fermions.  These follow the SU2QC physics-setup notes
> (9 Sept 2026) so that every number produced here can be compared with the
> project's verified `su2qc` code.  Do not edit without a new ADR in docs/.
>
> Geometry (one square plaquette, open boundaries):
>
>     v3=(0,1) ---l2---> v2=(1,1)
>        ^                 ^
>        |l1               |l3
>        |                 |
>     v0=(0,0) ---la---> v1=(1,0)
>
> Links are stored in the order (la, l1, l2, l3) = indices (0, 1, 2, 3).
> Loop orientation for the plaquette: U_sq = U_a U_3 U_2^dag U_1^dag.
> Staggered phases: eta_x = 1, eta_y(n) = (-1)^{n_x}; product around the loop = -1.
> Jordan-Wigner mode order: (v0-, v0+, v1-, v1+, v2-, v2+, v3-, v3+) where the
> colour index is the magnetic number m in {-1/2, +1/2} of the fundamental.

## Used by

`su2qc_jepa.data.trajectories` · `su2qc_jepa.gates.j0_data` · `su2qc_jepa.physics.observables` · `su2qc_jepa.physics.plaquette`

## Public names

`Couplings`

## Concepts

[[SU(2) lattice gauge theory]] · [[Kogut-Susskind Hamiltonian]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Jordan-Wigner mapping]]
