---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/limits.py"
lines: 129
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "ham"]
---
# su2qc.ham.limits

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/limits.py` · 129 lines

## What it does (from the module docstring)

> Verifier-owned limit tests for gate G1.
>
> * pure_electric_check: g2 -> infinity degeneracy pattern 16,16,18,16,16.
> * frozen_matter_check: m -> infinity 2x2 block equals the monograph's
>   one-plaquette H~1 after a documented normalization reconciliation.
> * magnetic_off_check: B = 0 spectrum equals an independently constructed
>   4-site periodic 1+1D SU(2) chain (built in limits_1d.py by a separate
>   builder; falls back to a cross-route B-off comparison if absent, and
>   reports which was used).

## Uses

[[su2qc.conventions]] · [[su2qc.ham.route_gausskernel]] · [[su2qc.ham.route_spinnet]]

## Public names

`pure_electric_check`, `frozen_matter_check`, `magnetic_off_check`

## Concepts

[[SU(2) lattice gauge theory]] · [[Plaquette and Wilson loop]] · [[Electric basis]] · [[Gate-and-evidence discipline]]

## Checked by gates

[[su2zx gate S8-G1]]
