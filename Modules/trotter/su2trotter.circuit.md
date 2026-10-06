---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/circuit.py"
lines: 182
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.circuit

Module of [[su2qc-trotter]] · `src/su2trotter/circuit.py` · 182 lines

## What it does (from the module docstring)

> Minimal circuit IR used to build the plaquette circuits.
>
> Every gadget is lowered at construction time to the gate set
>
>     x, z, h, s, sdg, t, tdg, cx, cz, rz(theta)
>
> (plus ``ccx`` and ``ch`` which are kept as macros only until :meth:`Circuit.lowered`).
> The same gate list is (i) simulated exactly by :mod:`su2trotter.sim`, (ii) emitted as a
> CUDA-Q kernel by :mod:`su2trotter.cudaq_backend`, and (iii) synthesised to Clifford+T by
> :mod:`su2trotter.synth`.  Conventions are CUDA-Q's (= Qiskit's): rz(t) = diag(e^{-it/2}, e^{it/2}).

## Used by

`su2trotter.baseline` · `su2trotter.draw` · `su2trotter.lean` · `su2trotter.optimize` · `su2trotter.pipeline` · `su2trotter.synth` · `su2trotter.trotter`

## Public names

`Gate`, `Circuit`, `is_clifford_t_angle`

## Concepts

[[Plaquette and Wilson loop]] · [[Qiskit]] · [[CUDA-Q]] · [[Clifford+T and T-count]]

## Checked by gates

[[trotter gate G22]]
