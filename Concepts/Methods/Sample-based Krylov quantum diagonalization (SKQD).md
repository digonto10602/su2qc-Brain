---
type: "concept"
tags: ["concept"]
aliases: ["SKQD", "SQD"]
as_of: "2026-10-05"
---
# Sample-based Krylov quantum diagonalization (SKQD)

**Plain words.** A hybrid quantum–classical way to find ground energies ([[Yu et al. 2025 SKQD]]; parent method
SQD, [[Robledo-Moreno et al. 2024]]). The quantum computer prepares time-evolved states
$e^{-iHk\Delta t}|b_0\rangle$ and is measured in the configuration basis; the distinct, valid configurations form a
subspace $B$; a classical computer diagonalizes the exact $H$ inside $B$. The quantum part only *chooses* the
subspace, so the energy is always an upper bound ([[Ritz values and certified bounds]]).

**The fairness trap.** If the subspace is a large fraction of the sector, random strings find it too — then the
device contributes nothing ([[van Rossum et al. 2026]]; [[Result - 2x2 SKQD run on ibm_kingston]]).

Implemented in [[su2qc-skqd]]: [[skqd.krylov]], [[skqd.skqd]], [[skqd.controls]].
