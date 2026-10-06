---
type: "concept"
tags: ["concept"]
as_of: "2026-10-05"
---
# Krylov subspace and Lanczos

**Plain words.** Start from one state and repeatedly apply the Hamiltonian (or time evolution); the states you
generate span a *Krylov subspace*, which captures the low-energy physics surprisingly fast. **Lanczos** builds an
orthonormal basis of it in which $H$ becomes tridiagonal (only diagonal and next-to-diagonal entries).

[[su2qc-skqd]] uses time-evolved Krylov states to generate samples ([[skqd.krylov]]). [[su2qc-jepa]] uses Lanczos to
compress the dynamics into $K=12$ states that fit on 12 qubits ([[Krylov-chain carrier]], [[su2qc_jepa.physics.dynamics]]).
