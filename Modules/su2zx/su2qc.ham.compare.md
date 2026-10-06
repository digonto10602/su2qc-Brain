---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/compare.py"
lines: 115
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "ham"]
---
# su2qc.ham.compare

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/compare.py` · 115 lines

## What it does (from the module docstring)

> Verifier-owned comparison of the two independent Hamiltonian routes (G1).
>
> Basis-independent checks:
>   * sorted spectra at >= 5 coupling points (incl. m = 0),
>   * observable time series from the stretched string on t in [0, 10].
> Owned by the VERIFY lane; neither route builder edits this file.

## Uses

[[su2qc.conventions]] · [[su2qc.ham.route_gausskernel]] · [[su2qc.ham.route_spinnet]]

## Public names

`spectra_comparison`, `time_series_comparison`

## Concepts

[[String breaking]]

## Checked by gates

[[su2zx gate S8-G1]]
