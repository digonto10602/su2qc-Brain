---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/compute.py"
lines: 63
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa"]
---
# su2qc_jepa.compute

Module of [[su2qc-jepa]] · `src/su2qc_jepa/compute.py` · 63 lines

## What it does (from the module docstring)

> Device selection and the measured unit costs used by the laptop runner (su2qc_jepa.localrun, decisions/004).
>
> `pick_device()` returns "cuda" only when a CUDA device exists *and* the installed PyTorch has kernels for its
> architecture *and* a tiny kernel actually runs; otherwise "cpu".  On the laptop this is always "cpu" (its GTX 1060
> is a Pascal card that current PyTorch CUDA builds do not support); on Perlmutter it is "cuda".  Override with
> SU2QC_DEVICE.  Routing (laptop or Perlmutter) lives in su2qc_jepa.localrun and scripts/run.py.

## Used by

`su2qc_jepa.localrun`

## Public names

`pick_device`, `load_compute`, `estimate_hours`

## Concepts

[[Perlmutter job queue]] · [[Laptop admission-controlled runner]] · [[NERSC Perlmutter]] · [[Laptop (Dell G7)]]
