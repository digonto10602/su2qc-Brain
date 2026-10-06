---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/lattice.py"
lines: 120
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.lattice

Module of [[su2qc-skqd]] · `src/skqd/lattice.py` · 120 lines

## What it does (from the module docstring)

> Open 2 x Lx ladder (Ly = 2 rows), the geometry of the SKQD manual (Step 1.1).
>
> Sites x = (x1, x2), x1 = 0..Lx-1 (column), x2 = 0..Ly-1 (row), site index
> x1*Ly + x2.  Links are oriented in +x and +y and are listed in the order of their
> start site (x-link before y-link at the same site).  Every link goes from a
> lower site index to a higher one, which is what the Jordan-Wigner sign rule
> of the builder assumes.
>
> eta_l = i on x-links, (-1)^{x1+x2} of the start site on y-links (staggered
> hopping phases; the product of phases around a plaquette is -1).
>
> A plaquette P with lower-left corner (x1, x2) is described by its four links
> (bottom, right, top, left) counter-clockwise from the lower-left corner:
>     bottom = (x1,x2) -> (x1+1,x2)      traversed forward
>     right  = (x1+1,x2) -> (x1+1,x2+1)  traversed forward
>     top    = (x1,x2+1) -> (x1+1,x2+1)  traversed backward (U^dag)
>     left   = (x1,x2) -> (x1,x2+1)      traversed backward (U^dag)
>
> Static charges: a set of site indices that carry an extra static spin-1/2 in
> Gauss's law (Step 1.3, Table 2 of the manual).

## Used by

`skqd.basis` · `skqd.exact` · `skqd.fullspace` · `skqd.ml`

## Public names

`Ladder`

## Concepts

[[Gauss's law]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Jordan-Wigner mapping]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Agent routing (planner, executor, reviewer, runner, scribe)]]

## Checked by gates

[[skqd gate E1]] · [[skqd gate E2]]
