---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/baseline.py"
lines: 153
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.baseline

Module of [[su2qc-trotter]] · `src/su2trotter/baseline.py` · 153 lines

## What it does (from the module docstring)

> Baseline: the 34-qubit promise-aware circuit of optimized_plaquette_dontcare_lowT.ipynb
> (plan, Sec. IV.A, Eq. 39), re-expressed gate by gate in our IR.
>
> Differences from the notebook are only in how the continuous rotations are lowered:
> C^2 Rx is built as RCCX-compute -> CRx -> RCCX-uncompute on the free scratch qubit ``h``,
> and CRx = H CRz H with CRz = two rz.  Everything else is the notebook's construction.

## Uses

[[su2trotter.circuit]] · [[su2trotter.physics]]

## Used by

`su2trotter.lean`

## Public names

`build`

## Concepts

[[Plaquette and Wilson loop]]

## Checked by gates

[[trotter gate G22]] · [[trotter gate R1]] · [[trotter gate V1]]
