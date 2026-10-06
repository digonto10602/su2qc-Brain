---
type: "concept"
tags: ["concept", "cross-package"]
aliases: ["82-state plaquette", "one plaquette with quarks"]
as_of: "2026-10-05"
---
# Shared 2x2 plaquette

The single physical system that [[SU2ZX]] Section 8 verified first and that [[su2qc-skqd]] and [[su2qc-jepa]] both study:

- one square plaquette (4 sites, 4 links, open boundaries), [[SU(2) lattice gauge theory|SU(2)]] gauge field truncated at
  $j_{\max}=\tfrac12$ ([[Link truncation (j_max)]]);
- two-colour [[Staggered fermions]] on the 4 sites;
- [[Gauss's law]] imposed exactly → **82 physical states**;
- [[Baryon-number sectors]]: $2/20/38/20/2$; the 38-state sector is where the [[String breaking|string-breaking]] dynamics live;
- at $j_{\max}=1$: 152 states.

| | SU2ZX Section 8 (first, 7 Sept) | su2qc-skqd | su2qc-jepa |
|---|---|---|---|
| what is computed | exact dynamics, then GI-vs-playback circuit cost | ground energies by [[Sample-based Krylov quantum diagonalization (SKQD)]] | real-time dynamics learned by a [[JEPA world model]] |
| qubits on hardware | 12 ([[L12 encoding]]) | 12 (codewords, [[Codewords and the Gauss-law decoder]]) | 12 ([[Krylov-chain carrier]], one-hot) |
| circuit cost | ≈ 2 156 two-qubit gates per Strang step | one coarse step ≈ 588 CZ, 44 µs on ibm_kingston | 22 CZ per Trotter step; 34–188 CZ for $r=1..8$ |
| two independent builders | [[su2qc.ham.route_spinnet]] vs [[su2qc.ham.route_gausskernel]] | [[skqd.hamiltonian]] vs [[skqd.fullspace]] | route A vs route B in [[su2qc_jepa.physics.plaquette]], plus cross-check with SU2ZX |
| hardware so far | none (twin only) | ibm_fez, ibm_kingston | none (emulated) |

All three agree on the state count and sector split. su2qc-jepa ↔ SU2ZX are numerically cross-checked
($7.3\times10^{-14}$); su2qc-skqd has **not** been cross-checked against either (different units: lattice units with
$g^2$, $m=3g^2/16$, versus units of $g_E$) — see [[Cross-package opportunities]].
