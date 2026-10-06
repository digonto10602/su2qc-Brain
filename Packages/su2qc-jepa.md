---
type: "package"
package: "su2qc-jepa"
status: "active"
tags: ["package"]
repo: "https://github.com/digonto10602/su2qc-jepa"
last_commit: "2026-10-06 4a23591 (jobs 013\u2013014 queued)"
commits: 57
aliases: ["Gauge-JEPA-P", "Gauge-JEPA-P v2", "su2qc_jepa"]
as_of: "2026-10-06"
---
# su2qc-jepa

**What it is.** The starter package for *Gauge-JEPA-P v2* (plan `plans/001`, 5 Oct – 29 Nov 2026, eight weeks): a
[[JEPA world model]] for the real-time [[String breaking|string-breaking]] dynamics of the hard-core SU(2) plaquette
with two-colour staggered fermions, plus a [[Krylov-chain carrier]] that puts the same dynamics on 12 qubits of an
IBM Heron processor at 22 CZ gates per time step.

**The idea in plain words.** An encoder turns a noisy, finite-shot measurement record into a 16-number summary (the
*latent*). A predictor moves that summary forward in time given the couplings. The model is trained to predict
*summaries*, not raw bit strings. If it learns the dynamics, it can (1) forecast clean observables from one noisy
early measurement and (2) flag when hardware data drift from what the physics allows — a label-free error signal.

**The model.** Same physical system as [[su2qc-skqd]] at 2×2: see [[Shared 2x2 plaquette]] (82 states, sectors
2/20/38/20/2; string breaking from the stretched string lives in the 38-state sector). Couplings in units of
$g_E$: $(c_E, c_M, c_H, c_B)$, frozen working point P-A $= (1, 3/8, 0.25, -0.0625)$ at $g_E=2$.

## Code map

Physics: [[su2qc_jepa.physics.su2]], [[su2qc_jepa.physics.conventions]], [[su2qc_jepa.physics.plaquette]] (routes A
and B), [[su2qc_jepa.physics.dynamics]], [[su2qc_jepa.physics.observables]], [[su2qc_jepa.physics.chain]].
Data: [[su2qc_jepa.data.trajectories]], [[su2qc_jepa.data.records]].
Model: [[su2qc_jepa.models.jepa]], [[su2qc_jepa.models.train]].
Twin and hardware: [[su2qc_jepa.twin.noise]], [[su2qc_jepa.twin.layout]], [[su2qc_jepa.twin.run]], [[su2qc_jepa.hardware.ibm]].
Gates: [[su2qc_jepa.gates.j0_data]], [[su2qc_jepa.gates.j1_training]], [[su2qc_jepa.gates.j2_forecast]],
[[su2qc_jepa.gates.j3_hardware]], [[su2qc_jepa.gates.ledger]].
Infrastructure: [[su2qc_jepa.localrun]], [[su2qc_jepa.jobs]], [[su2qc_jepa.compute]], [[su2qc_jepa.repo.artifacts]], [[su2qc_jepa.repo.graph]].

## Milestones and gates

| milestone | gate | status |
|---|---|---|
| M-env laptop environments | — | DONE |
| M0 bootstrap, CI, code graph | — | PASS |
| M1 physics and data | [[jepa gate J0]] | PASS 9/9 (cross-check with [[SU2ZX]] `su2qc`: max deviation $7.3\times10^{-14}$) |
| M2 model and preregistration | [[jepa gate J1]] | **FAIL for all 9 finished runs** (the plan's 7-rung ladder plus 2 extra semigroup-weight runs): the energy and observable rows pass, the semigroup row fails everywhere; 2 more runs queued (jobs 013, 014). See [[Result - J1 ladder fails on the semigroup row]] |
| forecasting | [[jepa gate J2]] | not run |
| hardware error signal | [[jepa gate J3]] | not run; no hardware job submitted yet |
| quantum encoder | [[jepa gate J4]] | optional |

Decisions: [[Decision - jepa 000 frozen conventions]], [[Decision - jepa 001 numbered artifacts and Graphify]],
[[Decision - jepa 004 laptop and Perlmutter only]], [[Decision - jepa 005 J1 energy threshold]].

## Compute

[[Laptop admission-controlled runner]] for light work (16 GB and 2 CPUs always left free for other sessions; this
project's jobs are the first to be killed under memory pressure) and the [[Perlmutter job queue]] for everything
heavy. The GTX 1060 is not used (PyTorch has no kernels for it).

## Hardware plan

IBM Quantum Open Plan, about 8–13 QPU-minutes total across two 28-day windows ([[IBM Quantum Open Plan]]); IonQ is
optional. All noisy numbers so far are EMULATED.

## Recent engineering (5–6 Oct)

- GPU-only bug: the forecasting baselines built their networks on the CPU while the data were on the GPU, so jobs
  002–007 crashed *after* training (training outputs survived). Fixed in `3fd0a65`, verified on Perlmutter by job 009.
- Laptop and Perlmutter builds of `data/main` agree: noisy inputs bit-identical, exact targets equal to $\sim10^{-13}$
  (different linear-algebra rounding). Node-hours used ≈ 1.9 of 50 (report 012).
- Full report: `reports/012` (plan, physics, every result and the data behind every plot).
