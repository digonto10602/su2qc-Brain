---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/dynamics/run_g2.py"
lines: 37
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "dynamics"]
---
# su2qc.dynamics.run_g2

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/dynamics/run_g2.py` · 37 lines

## What it does (from the module docstring)

> Run the full G2 production sequence and print a summary (OPS lane).
>
> Operating point: g2 = 4.0, m = 3 g2/16 = 0.75 (tree-level resonance).
> Rationale (physics/DISCREPANCIES.md): the W_bar-argmax estimator is
> dominated by the BB-bar channel at small m and does not localize the
> tree-level resonance; the breaking-time estimator argmin t_b does, at g2 >= 4
> where the electric scale dominates hopping and the resonance is sharp.

## Uses

[[su2qc.dynamics.scan]]

## Concepts

[[Electric basis]]
