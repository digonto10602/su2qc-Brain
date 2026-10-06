---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/physics/plaquette.py"
lines: 520
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "physics"]
---
# su2qc_jepa.physics.plaquette

Module of [[su2qc-jepa]] · `src/su2qc_jepa/physics/plaquette.py` · 520 lines

## What it does (from the module docstring)

> Hard-core SU(2) Kogut-Susskind plaquette with two-colour staggered fermions.
>
> Two independent constructions are provided and cross-checked in the tests:
>
> * **Route A (vertex singlets, block tensors)** - `PlaquetteModel` builds the
>   gauge-invariant (GI) basis as a configuration basis labelled by the four link
>   spins and the four site occupations, with the colour structure fixed by the
>   unique singlet at every vertex.  Hamiltonian matrix elements are computed by
>   applying each term to the block tensor of a basis state.  Works for any j_max.
> * **Route B (full gauge-redundant space)** - `FullSpaceOperators` builds every
>   operator as a sparse matrix on the full link (x) matter space and lets the
>   tests check (i) that H commutes with all Gauss-law generators, (ii) that the
>   route-A basis vectors are annihilated by the generators and (iii) that
>   Q^dag H Q reproduces route A.  Practical for j_max = 1/2 (160,000 states).
>
> Units: H is measured in units of g_E (see conventions.Couplings).

## Uses

[[su2qc_jepa.physics.conventions]] · [[su2qc_jepa.physics.su2]]

## Used by

`su2qc_jepa.data.trajectories` · `su2qc_jepa.gates.j0_data` · `su2qc_jepa.physics.observables`

## Public names

`LinkSpace`, `MatterSpace`, `GIBasisState`, `PlaquetteModel`, `FullSpaceOperators`

## Concepts

[[SU(2) lattice gauge theory]] · [[Kogut-Susskind Hamiltonian]] · [[Gauss's law]] · [[Link truncation (j_max)]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]]
