---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/dynamics/engine.py"
lines: 130
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "dynamics"]
---
# su2qc.dynamics.engine

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/dynamics/engine.py` · 130 lines

## What it does (from the module docstring)

> Exact-dynamics engine for the 82-state (jmax=0.5) / 152-state (jmax=1) SU(2) plaquette.
>
> evolve(H, psi0, times) -> array of states (dense expm on 82-dim; use scipy.linalg.expm
> of -iH dt step matrix, cumulative).
> self_check(g2, m, jmax, t_max) -> dict with expm_krylov_dev, energy_drift, N_drift.

## Uses

[[su2qc.conventions]] · [[su2qc.ham.route_spinnet]]

## Used by

`su2qc.dynamics.scan`

## Public names

`evolve`, `self_check`

## Concepts

[[SU(2) lattice gauge theory]] · [[Link truncation (j_max)]] · [[Plaquette and Wilson loop]]

## Checked by gates

[[su2zx gate S8-G2]]
