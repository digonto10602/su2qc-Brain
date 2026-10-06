---
type: "module"
package: "su2qc-qcadvantage"
file: "su2torus/trotter.py"
lines: 90
generated: True
as_of: "2026-10-06"
tags: ["module", "qca"]
---
# su2torus.trotter

Module of [[su2qc-qcadvantage]] · `su2torus/trotter.py` · 90 lines

## What it does (from the module docstring)

> Trotter circuits (docs/METHODS.md, section 3).
>
> Step ordering, with U_X(t) = exp(-i H_X t):
>     order 1:  U_step(dt) = U_BB(dt) U_BA(dt) U_E(dt)      (U_E acts first)
>     order 2:  U_step(dt) = U_E(dt/2) U_BA(dt/2) U_BB(dt) U_BA(dt/2) U_E(dt/2)
> Equality is required up to a global phase.
>
> Allowed gates: rx ry rz h x y z s sdg sx sxdg p u cx rzz (and barrier).
> Each flip exp(-i a_p(Z_nb) X_p dt) is a uniformly controlled rotation on qubit p
> controlled by its neighbours (Gray-code construction: 2**(#neighbours) cx gates).

## Used by

`su2torus.mps` · `su2torus.noise`

## Public names

`trotter_step`, `trotter_circuit`, `two_qubit_counts`

## Concepts

[[Trotter and Strang splitting]]

## Checked by gates

[[qca gate M2]] · [[qca gate M4]] · [[qca gate M5]]
