---
type: "module"
package: "su2qc-qcadvantage"
file: "su2torus/lattice.py"
lines: 90
generated: True
as_of: "2026-10-06"
tags: ["module", "qca"]
---
# su2torus.lattice

Module of [[su2qc-qcadvantage]] · `su2torus/lattice.py` · 90 lines

## What it does (from the module docstring)

> Plaquette graph of the triangular lattice (= honeycomb graph).
>
> Conventions (see docs/METHODS.md, section 1):
> - Triangular-lattice sites (i, j), 0 <= i < L1, 0 <= j < L2.
> - Each cell (i, j) owns two triangular plaquettes:
>     kind 0 = "up"   triangle with vertices (i,j), (i+1,j), (i,j+1)      -> sublattice A
>     kind 1 = "down" triangle with vertices (i+1,j), (i,j+1), (i+1,j+1)  -> sublattice B
> - Plaquette index p = 2*(i*L2 + j) + kind, so n = 2*L1*L2 plaquettes.
> - up(i,j) shares a link with down(i,j), down(i-1,j), down(i,j-1).
>   Periodic: indices wrap mod L1, L2. Open: neighbours outside the patch are dropped.
> - A hexagon is the set of 6 plaquettes touching one triangular-lattice site (i,j):
>   up(i,j), up(i-1,j), up(i,j-1), down(i-1,j), down(i,j-1), down(i-1,j-1),
>   returned in cyclic order (consecutive entries share a link, last-first too).

## Public names

`HoneycombTorus`, `initial_state`

## Concepts

[[Plaquette and Wilson loop]] · [[One-qubit-per-plaquette SU(2) model]]

## Checked by gates

[[qca gate M1]] · [[qca gate M2]] · [[qca gate M3]] · [[qca gate M4]] · [[qca gate M5]]
