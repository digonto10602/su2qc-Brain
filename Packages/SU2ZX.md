---
type: "package"
package: "SU2ZX"
status: "paused"
tags: ["package"]
repo: "https://github.com/digonto10602/genesis-su2-zx-observables"
last_commit: "2026-09-10"
commits: 27
aliases: ["genesis-su2-zx-observables", "su2qc package", "SU2ZX Foundation Code Package", "GI-cost campaign"]
as_of: "2026-10-05"
---
# SU2ZX

**Repository:** `genesis-su2-zx-observables` (public, 27 commits, last push 2026-09-10). It holds three layers of work,
oldest first:

1. **`su2zx` package, v0.4.0 (Sept 5–6, Codex).** Pure-gauge SU(2) *plaquette chain* ($j_{\max}=\tfrac12$, gauge-reduced),
   used to study **which compiler wins** ([[ZX-calculus circuit optimization]]: six strategies, Basic vs Teleport) and to
   scale observables with [[Tensor networks (MPS and TEBD)|MPS]] to $N=32$. See [[Result - SU2ZX v0.4.0 compiler and MPS study]].
   Code: [[su2zx.core]] (the Hamiltonian, source of truth), [[su2zx.compiler_study]], [[su2zx.robust_study]],
   [[su2zx.scaling_study]], [[su2zx.tn_study]], [[su2zx.qpu]].
2. **`su2qc` package, Section 8 v0.5.0 (overnight Hermes run, 7 Sept).** SU(2) *with dynamical matter on one plaquette* —
   the [[Shared 2x2 plaquette]] (82 states). Two independent builders: route 1 spin network ([[su2qc.ham.route_spinnet]]),
   route 2 Gauss-kernel projection on the 160 000-dimensional redundant space ([[su2qc.ham.route_gausskernel]]); the
   12-qubit [[L12 encoding]] and Strang circuits ([[su2qc.circuits.strang_l12]]); the Aer twin ([[su2qc.twin.twin]]).
   Gates S8-G0…G3 PASS, G4 never run. See [[Result - SU2ZX section 8 verified plaquette]].
3. **GI-cost campaign v0.6.0–v0.6.4 (8–10 Sept, Hermes).** "The measured price of exact gauge invariance": exactly
   gauge-invariant Strang circuits (arm GI) versus Krylov playback (arm KR) on the same Hamiltonian and device, gates
   C0–C8. Stuck at **C0 partial** (C1 pass); hardware disabled, 0 QPU jobs. See [[Result - GI-cost campaign stalled at C0]].

## Why it matters to the other packages

- [[su2qc-jepa]] cross-checks its physics against the `su2qc` package from layer 2 (max deviation $7.3\times10^{-14}$) and
  adopted its conventions, its P-A working point, and the repaired twin seeding ([[Lessons that travelled]]).
- The L12 route costs about 2 156 two-qubit gates per Strang step — the reason su2qc-jepa built the much cheaper
  [[Krylov-chain carrier]] and su2qc-skqd built structured codeword circuits.
- The campaign's own claim table says the 8.6× GI-vs-playback cost gap was the question; it was never answered on hardware.

## Workflow

Codex (`AGENTS.md`, prompts v0.3.0/v0.4.0) for layer 1; Hermes orchestrator with Codex builders and NIM reviewers for
layers 2–3; escalation files in `solutions/` (0.5.0.md fixed route 1's missing vertex recoupling factors);
[[Graphify code graph]]; numbered prompt versions `gi_cost_campaign_v.0.6.x.md`.

## Status

Paused since 2026-09-10. Next action recorded in the campaign state: fix the bootstrap to exclude zero-kept repeats,
diagnose the $r=0$ variance shortfall, prove the structured synthesis equivalent (20× cheaper $r=1$), close C0.
