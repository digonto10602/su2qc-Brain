---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/dynamics/scan.py"
lines: 317
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "dynamics"]
---
# su2qc.dynamics.scan

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/dynamics/scan.py` · 317 lines

## What it does (from the module docstring)

> Mass scan / resonance finder, truncation comparison, Trotter-window selector.
>
> Rewritten by the OPS lane after the delegated builder timed out (partial file);
> classification bugs fixed: P_surv is the EXACT charge pattern (+1,-1,0,0), not
> a sorted-|q| match.

## Uses

[[su2qc.conventions]] · [[su2qc.dynamics.engine]] · [[su2qc.ham.route_spinnet]]

## Used by

`su2qc.circuits.strang_l12` · `su2qc.compile.run_g4` · `su2qc.dynamics.run_g2`

## Public names

`channel_probs`, `mass_scan`, `timeseries_at`, `truncation`, `strang_step_matrix`, `strang_error`, `select_window`, `verify_window`

## Concepts

[[Link truncation (j_max)]] · [[Trotter and Strang splitting]]

## Checked by gates

[[su2zx gate S8-G2]]
