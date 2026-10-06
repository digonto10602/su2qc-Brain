---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/circuits/synth_l12.py"
lines: 308
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "circuits"]
---
# su2qc.circuits.synth_l12

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/circuits/synth_l12.py` · 308 lines

## What it does (from the module docstring)

> Structured synthesis of the L12 block unitaries.
>
> The implementation deliberately keeps the code-space structure visible: the
> small connected components of each local matrix are synthesized independently
> and the diagonal term is a degree-three phase polynomial.

## Uses

[[su2qc.circuits.strang_l12]] · [[su2qc.encodings.l12]]

## Used by

`su2qc.compile.run_g4`

## Public names

`synth_unitary`, `synth_strang_step`, `synth_full_circuit`, `write_resources`

## Concepts

[[L12 encoding]]
