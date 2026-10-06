---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/fermions.py"
lines: 48
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.fermions

Module of [[su2qc-skqd]] · `src/skqd/fermions.py` · 48 lines

## What it does (from the module docstring)

> Two-colour staggered-fermion site.
>
> Local Fock space F = span{|n_1 n_2>} with the ordering (0,0), (1,0), (0,1), (1,1)
> (index c = n_1 + 2 n_2).  Local annihilators with the intra-site Jordan-Wigner
> sign:  psi_1 = a (x) 1,  psi_2 = P (x) a,  P = (-1)^n on one mode.
>
> Global operators on a chain of sites (JW ordering = site index order):
>     psi_{x,i} = (prod_{z<x} P_z) (x) psi^loc_{x,i},   P_z = (-1)^{n_z}.
>
> Matter charge  Q_a = psi^dag (sigma_a/2) psi  (see su2.py for why sigma_a/2 and
> not -sigma_a^T/2: it is tied to the convention L_a = -J_a^T, R_a = +J_a of the
> link generators).
>
> n = occupation number (0, 1, 2), c = Fock index, P = parity operator.

## Uses

[[skqd.su2]]

## Used by

`skqd.fullspace` · `skqd.hamiltonian` · `skqd.vertex`

## Public names

`check_algebra`

## Concepts

[[Staggered fermions]] · [[Jordan-Wigner mapping]]
