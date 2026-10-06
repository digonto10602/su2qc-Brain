---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/cudaq_backend.py"
lines: 96
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.cudaq_backend

Module of [[su2qc-trotter]] · `src/su2trotter/cudaq_backend.py` · 96 lines

## What it does (from the module docstring)

> CUDA-Q backend: build kernels from the gate IR, count resources, simulate.
>
> * :func:`to_kernel` emits a ``cudaq.make_kernel`` kernel gate by gate.
> * :func:`resources` uses ``cudaq.estimate_resources`` (CUDA-Q's own counter) for the
>   final tally: total gates, depth, qubits, and per-gate counts (T/Tdg, CX, ...).
> * :func:`encoded_state_check` prepares random superpositions of the 625 encoded states
>   (ancillas |0>) as a ``cudaq.State`` argument, runs the circuit with
>   ``cudaq.get_state`` and compares with the exact exp(i alpha B) image.

## Uses

[[su2trotter.physics]]

## Used by

`su2trotter.pipeline`

## Public names

`to_kernel`, `resources`, `encoded_state_check`

## Concepts

[[CUDA-Q]] · [[Clifford+T and T-count]]

## Checked by gates

[[trotter gate B1]] · [[trotter gate G22]] · [[trotter gate R1]] · [[trotter gate V1]]
