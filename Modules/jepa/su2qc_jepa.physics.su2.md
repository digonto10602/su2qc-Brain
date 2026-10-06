---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/physics/su2.py"
lines: 84
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "physics"]
---
# su2qc_jepa.physics.su2

Module of [[su2qc-jepa]] · `src/su2qc_jepa/physics/su2.py` · 84 lines

## What it does (from the module docstring)

> SU(2) building blocks: spin matrices and Clebsch-Gordan coefficients.
>
> Everything here is plain NumPy; spins are given as floats (0, 0.5, 1, ...).
> The Clebsch-Gordan coefficient uses the Racah closed form, which is exact for
> the small spins used in this package (j <= 2 in practice).

## Used by

`su2qc_jepa.physics.plaquette`

## Public names

`is_half_int`, `m_values`, `spin_matrices`, `clebsch_gordan`

## Concepts

[[SU(2) lattice gauge theory]] · [[Clebsch-Gordan coefficients]]
