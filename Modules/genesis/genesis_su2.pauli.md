---
type: "module"
package: "genesis-su2-lgt"
file: "src/genesis_su2/pauli.py"
lines: 87
generated: True
as_of: "2026-10-06"
tags: ["module", "genesis"]
---
# genesis_su2.pauli

Module of [[genesis-su2-lgt]] · `src/genesis_su2/pauli.py` · 87 lines

## What it does (from the module docstring)

> Canonical Pauli representation of the two-plaquette SU(2) benchmark.
>
> Physics source: Kavaki and Lewis, Communications Physics 7, 208 (2024),
> Eq. (1). Energies are in units of g^2/2 and x = 2/g^4. The Hilbert space is
> already gauge reduced at j_max=1/2, so every four-vector is physical.

## Used by

`genesis_su2.backends.cudaq_backend` · `genesis_su2.backends.qiskit_backend` · `genesis_su2.exact`

## Public names

`PauliTerm`, `pauli_terms`, `dense_hamiltonian`, `direct_dense_hamiltonian`, `operator_matrix`

## Concepts

[[SU(2) lattice gauge theory]] · [[Link truncation (j_max)]] · [[Plaquette and Wilson loop]] · [[Pauli decomposition]]

## Checked by gates

[[genesis gate G1]] · [[genesis gate G2]] · [[genesis gate G7.1]]
