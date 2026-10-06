---
type: "module"
package: "SU2ZX"
file: "src/su2zx/core.py"
lines: 416
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx"]
---
# su2zx.core

Module of [[SU2ZX]] · `src/su2zx/core.py` · 416 lines

## What it does (from the module docstring)

> Physics, circuits, and observables for the j_max=1/2 SU(2) plaquette chain.
>
> Conventions:
> * H_tilde = 2 H / g^2 and x = 2 / g^4.
> * Qiskit Pauli labels and bitstrings are q_(N-1) ... q_0.
> * Each qubit is one gauge-reduced spatial plaquette-loop degree of freedom.

## Used by

`su2zx.compiler_study` · `su2zx.qpu` · `su2zx.qpu_analysis` · `su2zx.robust_study` · `su2zx.scaling_study` · `su2zx.study` · `su2zx.tn_study`

## Public names

`PauliTerm`, `pauli_word`, `plaquette_chain_terms`, `hamiltonian`, `hamiltonian_components`, `pauli_rotation`, `ordered_hamiltonian_terms`, `strang_evolution`, `circuit_hash`, `circuit_structure_hash`, `initial_state`, `exact_state`, `circuit_state`, `expectation`, `probabilities`, `local_occupations`, `total_variation`, `measurement_circuit`, `measurement_family`, `normalized_counts`, `diagonal_pauli_expectation`, `ideal_measurement_distributions`, `reconstruct_energy`, `project_to_probability_simplex`, `optimize_with_pyzx`

## Concepts

[[SU(2) lattice gauge theory]] · [[Link truncation (j_max)]] · [[Plaquette and Wilson loop]] · [[Qiskit]]
