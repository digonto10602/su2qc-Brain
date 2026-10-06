---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/compare.py"
lines: 130
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.compare

Module of [[su2qc-trotter]] · `src/su2trotter/compare.py` · 130 lines

## What it does (from the module docstring)

> Gate-level comparison data for the two techniques (reference 34-qubit, lean 22-qubit).
>
> For a circuit C, every one of the 625 physical basis states is run through C's actual gates
> (exact sparse simulation, helper qubits starting in |0>).  The output of input j splits into
>
> * M[:, j]      amplitudes on the 625 physical states with all helper qubits back at 0;
> * dirty_j      amplitudes on any state with at least one helper qubit left at 1;
> * unphys_j     amplitudes with clean helpers but a link in an unused pattern (001, 010, 011).
>
> Multi-step evolution in the physical space is c_k = M c_{k-1}.  The weight that escapes at step
> k is |dirty c_{k-1}|^2 (resp. unphys); it is accumulated.  This is exact only when nothing escapes
> (all exact-rotation circuits here).  For the Clifford+T circuits the escaped amplitude persists and
> adds up coherently, so multi-step results must use `full_series` / `full_echo` below (E9).

## Uses

[[su2trotter.physics]] · [[su2trotter.sim]]

## Public names

`circuit_blocks`, `evolve`, `link_excitation`, `n_excited`, `split_state`, `to_state`, `full_series`, `full_echo`

## Concepts

[[Leakage-safe data splits]] · [[Clifford+T and T-count]]
