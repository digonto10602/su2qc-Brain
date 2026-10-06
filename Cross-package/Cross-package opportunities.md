---
type: "hub"
tags: ["cross-package", "claude-note"]
as_of: "2026-10-05"
---
# Cross-package opportunities

*These are Claude's own observations from reading the repositories side by side (2026-10-05), not decisions you have made.*

1. **Reuse skqd's ibm_kingston knowledge in jepa's hardware campaign.** su2qc-skqd found that the Aer model at the
   echo $T_2$ was 5.1× too optimistic, and (updated 6 Oct) that the device's no-DD clean fraction changed by a factor ≈ 2
   between two days, larger than any [[Dynamical decoupling]] effect. [[jepa gate J3]] relies on an Aer twin of the
   same device class — it should inherit skqd's $T_2^\*$ bracket and plan same-day controls, not one-day A/B tests.
   Links: [[Result - client-side XY4 gain did not replicate]], [[su2qc_jepa.twin.noise]], [[skqd.idle]].
2. **A three-way cross-check of the 82-state Hamiltonian.** su2qc-jepa already matches SU2ZX's `su2qc` to $7\times10^{-14}$.
   Mapping su2qc-skqd's 2×2 Hamiltonian (lattice units) onto jepa's units of $g_E$ would tie all three codes
   together. See [[Shared 2x2 plaquette]].
3. **The chain carrier is ~25× cheaper per step than an SKQD coarse step** (22 CZ vs ≈588 CZ). If the 2×3 SKQD run
   stays out of reach, a Krylov-chain-style circuit for SKQD support generation might be worth one planner question.
   Links: [[Krylov-chain carrier]], [[Result - 2x3 needs a different device]].
4. **Shared calibration guard.** skqd keys submissions on calibration content; jepa's
   [[su2qc_jepa.hardware.ibm]] has a dry-run-first budget guard. One shared module would avoid two
   implementations drifting.
5. **The GI-cost question is half-answered elsewhere.** SU2ZX's campaign asked what exact gauge invariance costs on
   hardware (GI arm vs playback). su2qc-skqd's structured codeword circuits (≈588 CZ, exact, leak-free) and su2qc-jepa's
   chain carrier (22 CZ/step) are two more data points on the same plaquette; a one-page comparison could close the
   campaign's C-gates without new QPU time. Links: [[Result - GI-cost campaign stalled at C0]].
6. **genesis-su2-lgt as a regression test.** Its two-qubit benchmark is cheap; running it on each new IBM backend
   before a real session is a fast health check.
7. *(added 2026-10-06)* **Three 12-qubit encodings of one plaquette now exist** — [[L12 encoding]] (3 qubits per vertex,
   with quarks), skqd codewords, and su2qc-trotter's 3 qubits per link (pure gauge). su2qc-trotter's flag/bright-pair
   tricks (4 rotations, Margolus Toffolis on don't-care inputs) might cut the L12 Strang step cost; worth one question
   to a planner. Links: [[Result - lean 22-qubit plaquette Trotter step]].
8. *(added 2026-10-06)* **qcadvantage's MPS frontier and SU2ZX's MPS study measure the same thing on different
   models.** SU2ZX v0.4.0 scaled a plaquette chain to $N=32$ at short times; [[su2qc-qcadvantage]] found MPS fails after
   2–3 steps at $N=48$ on a 2D torus. Quoting both in one table would show reviewers why 2D matters.
