---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/encodings/l12.py"
lines: 70
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "encodings"]
---
# su2qc.encodings.l12

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/encodings/l12.py` · 70 lines

## What it does (from the module docstring)

> The 12-qubit, three-bits-per-vertex L12 encoding.
>
> Qubit ``3*v,3*v+1,3*v+2`` is respectively (first link, second link,
> matter).  Integers use q0 as the least significant bit; displayed Qiskit
> strings consequently read q11 ... q0.

## Uses

[[su2qc.ham.route_spinnet]]

## Used by

`su2qc.circuits.strang_l12` · `su2qc.circuits.synth_l12` · `su2qc.twin.twin`

## Public names

`encode`, `decode`, `physical_codes`, `leakage_flags`, `is_physical`

## Concepts

[[Qiskit]] · [[L12 encoding]]

## Checked by gates

[[su2zx gate S8-G3]]
