---
type: "concept"
tags: ["concept"]
aliases: ["KC carrier", "chain carrier"]
as_of: "2026-10-05"
---
# Krylov-chain carrier

**Plain words.** [[su2qc-jepa]]'s trick to put the plaquette dynamics on hardware cheaply. [[Krylov subspace and Lanczos|Lanczos]]
compresses the relevant dynamics into $K=12$ basis states with a tridiagonal Hamiltonian; each basis state is
encoded as one excited qubit in a line of 12 ($|0\dots010\dots0\rangle$). Nearest-neighbour hops then implement the
dynamics: 22 CZ per Trotter step, 34 / 56 / 100 / 188 CZ for $r = 1, 2, 4, 8$ steps — a real depth ladder. States with
zero or two excitations are flagged as errors. Code: [[su2qc_jepa.physics.chain]]; qubit line chosen by [[su2qc_jepa.twin.layout]].
