---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/circuits_qiskit.py"
lines: 381
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.circuits_qiskit

Module of [[su2qc-skqd]] · `src/skqd/circuits_qiskit.py` · 381 lines

## What it does (from the module docstring)

> Qiskit translation of the IR circuits (circuits_ir.py) and the laptop-side
> helpers: statevector check against the numpy reference, transpiled CZ counts
> (gate S2), Aer noise-model sampling (gate S3).
>
> NOT executed in the cloud sandbox where this package was assembled (PyPI was
> not reachable there): the first laptop gate, scripts/laptop_L2_qiskit_check.py,
> verifies this module against skqd.reference_sim / skqd.circuits_ir, which are
> the validated ground truth.  Keep the API surface small and standard
> (QuantumCircuit, transpile, Statevector, UnitaryGate, AerSimulator, NoiseModel).
>
> Conventions.  IR qubit k = Qiskit qubit k.  A `unitary` IR gate on qubits
> [q_0, ..., q_{k-1}] with matrix U (q_0 = least significant bit) is
> qc.unitary(U, [q_0, ..., q_{k-1}]), which is Qiskit's own little-endian
> convention.  Counts keys from Qiskit have qubit 0 at the right end; use
> skqd.reference_sim.qiskit_key_to_bits to convert them to this package's bit tuples.

## Uses

[[skqd.reference_sim]]

## Public names

`ir_to_qiskit`, `statevector`, `statevector_aer`, `transpile_counts`, `generic_noise_model`, `sample`, `shot_chunk_for`, `sample_many`

## Concepts

[[Noise models and digital twin]] · [[Transpilation and CZ count]] · [[Gate-and-evidence discipline]] · [[Qiskit]]

## Checked by gates

[[skqd gate CF_traj]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate L2]] · [[skqd gate L3]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate Q0P_2x3]] · [[skqd gate S2]] · [[skqd gate S2D]] · [[skqd gate S2D_idle]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
