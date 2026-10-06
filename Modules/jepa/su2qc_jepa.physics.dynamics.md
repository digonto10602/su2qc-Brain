---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/physics/dynamics.py"
lines: 104
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "physics"]
---
# su2qc_jepa.physics.dynamics

Module of [[su2qc-jepa]] · `src/su2qc_jepa/physics/dynamics.py` · 104 lines

## What it does (from the module docstring)

> Exact real-time evolution and Lanczos/Krylov compression.
>
> `evolve` uses an eigendecomposition of the (small, real symmetric) Hamiltonian.
> `lanczos` returns the tridiagonal (alpha, beta) coefficients and the orthonormal
> Krylov vectors Q_K obtained from a start vector, with full reorthogonalisation.
> `krylov_error` quantifies the truncation error of propagating inside the
> K-dimensional Krylov subspace against the exact evolution.

## Used by

`su2qc_jepa.data.records` · `su2qc_jepa.data.trajectories` · `su2qc_jepa.gates.j0_data` · `su2qc_jepa.physics.chain`

## Public names

`sector_restrict`, `evolve`, `Krylov`, `lanczos`, `krylov_error`

## Concepts

[[Link truncation (j_max)]] · [[Krylov subspace and Lanczos]] · [[Exact diagonalization]]
