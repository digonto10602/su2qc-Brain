---
type: "module"
package: "su2qc-qcadvantage"
file: "su2torus/hamiltonian.py"
lines: 246
generated: True
as_of: "2026-10-06"
tags: ["module", "qca"]
---
# su2torus.hamiltonian

Module of [[su2qc-qcadvantage]] · `su2torus/hamiltonian.py` · 246 lines

## What it does (from the module docstring)

> Minimal (one qubit per plaquette) SU(2) Hamiltonian, arXiv:2608.28752.
>
> Basis convention (docs/METHODS.md, section 2): qubit p <-> plaquette p; |1> = excited
> (n_p = 1, Z_p = -1). Basis index b = sum_p n_p 2**p (Qiskit little-endian).
>
>     H_E = (3 g^2 / 8) sum_p ( 3 n_p - sum_{q in nb(p)} n_p n_q )
>         = (3 g^2 / 16) sum_{bonds} (1 - Z_p Z_q)
>     H_B = sum_p a_p X_p,   a_p = -(1/g^2) prod_{q in nb(p)} c(n_q),  c(0)=1, c(1)=1/2
>     Abelian twin (abelian=True): c == 1, i.e. a_p = -(1/g^2).
>     H_B^A / H_B^B : the X terms on sublattice A (up) / B (down) only.

## Used by

`su2torus.exact` · `su2torus.observables`

## Public names

`flip_amplitude`, `electric_diagonal`, `split_sparse`, `build_sparse`, `flip_pauli_terms`, `build_pauli`, `cheb_recur`, `axpy`, `apply_h`

## Concepts

[[SU(2) lattice gauge theory]] · [[Plaquette and Wilson loop]] · [[Noise models and digital twin]] · [[Qiskit]] · [[One-qubit-per-plaquette SU(2) model]]

## Checked by gates

[[qca gate M1]] · [[qca gate M2]] · [[qca gate M3]]
