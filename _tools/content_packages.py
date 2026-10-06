"""Hand-written notes: the hub, the three packages, cross-package notes, results and decisions.
Each entry: path (relative to vault) -> (frontmatter dict, markdown body).
Written 2026-10-05 from the public repositories at the commits recorded in each package note."""

AS_OF = "2026-10-05"

NOTES = {}


def note(path, fm, body):
    fm = dict(fm)
    fm.setdefault("as_of", AS_OF)
    NOTES[path] = (fm, body.strip() + "\n")


# --------------------------------------------------------------------------- hub
note("00 SU2QC Map.md",
     {"type": "hub", "tags": ["hub"], "aliases": ["SU2QC brain", "Home"], "as_of": "2026-10-06"},
     r"""
# SU2QC Map

This is the entry note (a *map of content*: an Obsidian term for a note whose job is to link to everything else).
Open **Graph view** to see the whole "brain", or open [[SU2QC Map.canvas|the canvas]] for the hand-laid-out picture.

## The research goal

All packages serve the Genesis Phase-I proposal *AI-Accelerated Non-Abelian Gauge Dynamics on Quantum Hardware*
(see [[Genesis Phase-I proposal]]): simulate [[SU(2) lattice gauge theory]] on quantum computers, with AI and
machine learning helping at every step.

## The packages (all SU2QC repositories on github.com/digonto10602, read for this map)

| package | one-line job | state on 2026-10-06 |
|---|---|---|
| [[genesis-su2-lgt]] | first starter: a pure-gauge two-plaquette benchmark on every backend | dormant since 2026-08-13 (v1.1.0) |
| [[su2qc-skqd]] | Project 2: sample-based Krylov diagonalization of SU(2) with quarks, run on IBM hardware | active; 2×2 hardware run done; XY4 gain did not replicate; 2×3 on IBM measured NO-GO (6 Oct); next route is Quantinuum (access email not sent) |
| [[su2qc-jepa]] | Gauge-JEPA-P v2: a JEPA world model of string breaking, with a Krylov-chain hardware carrier | active; week 1 of 8; J0 PASS; J1 FAIL for all 9 finished training runs (semigroup row), jobs 013–014 queued |
| [[SU2ZX]] (`genesis-su2-zx-observables`) | compiler study on a pure-gauge chain, then the verified one-plaquette-with-matter code and the GI-cost campaign | paused since 2026-09-10; campaign at C0 partial |
| [[su2qc-trotter]] | Clifford+T resources for one plaquette Trotter step ($j_{\max}=\tfrac12$, 12-qubit encoding) with CUDA-Q; lean 22-qubit design | done 2026-09-27; all 7 Perlmutter CI jobs PASS |
| [[su2qc-paulo-code]] | the reference 34-qubit Clifford+T plaquette circuit (notebook + QASM) that su2qc-trotter starts from | static files, not a git repository |
| [[su2qc-qcadvantage]] | "SU(2) torus frontier run": one-qubit-per-plaquette SU(2) on tori, exact + noisy + MPS, toward a quantum-advantage test | cloud phase M1–M6 done 2026-10-06 (branch `claude/modest-mayer-kh4s6b`); 4 decisions wait for you before cluster work |

## How they fit together

- [[Shared 2x2 plaquette]] — the one physical system that su2qc-skqd and su2qc-jepa both study.
- [[Package lineage]] — what each package inherited from the one before.
- [[Cross-package opportunities]] — places where one package's result could help another (Claude's notes, labelled).
- [[Lessons that travelled]] — mistakes caught once and then built into later packages.

## Browse by kind

- Physics ideas: [[Physics concepts index]]
- Algorithms and machine learning: [[Methods index]]
- Quantum computers and clusters: [[Hardware index]]
- How the work is run (agents, gates, job queues): [[Workflow index]]
- Papers the packages cite: [[Papers index]]
- Headline numbers: [[Results index]]
- Every gate (pass/fail checkpoint): [[Gates index]]
- Every code module: [[Modules index]]

## Using this vault with AI

See [[How to use this vault]] — Graph view tips, how to refresh it when the repositories change, and how the
`_export/su2qc_brain.jsonl` file can feed an agent or a training set.
""")

note("How to use this vault.md",
     {"type": "hub", "tags": ["hub", "howto"], "as_of": "2026-10-06"},
     r"""
# How to use this vault

## Opening it

1. The vault lives at `~/Projects/su2qc-Brain`, next to the repositories it is built from.
2. In Obsidian: *Open folder as vault* → choose the `su2qc-Brain` folder.
3. Open [[00 SU2QC Map]]. Press the graph icon (or `Ctrl/Cmd+G`) for **Graph view**.

Graph view colours are preset (in `.obsidian/graph.json`): packages, modules, gates, concepts, hardware, papers and
results each get their own colour. Useful graph filters (type them in the graph's search box):

- `tag:#package` — only the packages
- `path:Modules/skqd` — only the su2qc-skqd code
- `tag:#gate -tag:#pass` — gates that have not passed
- `[[Gauss's law]]` — everything that mentions Gauss's law

**Local graph** (right-click a note → *Open local graph*) shows one note and its neighbours; this is often more
readable than the full graph.

## What is generated and what is hand-written

- `Modules/` and `Gates/` are **generated** from the repositories by `_tools/build_vault.py` (module docstrings,
  import statements, gate tables). Do not edit them by hand; re-run the builder instead.
- Everything else (packages, concepts, hardware, papers, results, decisions, hubs) is **hand-written** and safe to edit.

## Refreshing after the repositories change

```bash
cd ~/Projects/su2qc-Brain/_tools
python build_vault.py --repos ~/Projects --overwrite-hand   # reads every su2qc-* repo plus genesis-su2-lgt and the SU2ZX checkout
python export_jsonl.py                       # rebuild _export/su2qc_brain.jsonl
```

A Claude Code session can do this for you: "read `_tools/README.md` and refresh the vault".

## Using it for AI

`_export/su2qc_brain.jsonl` has one JSON record per note (a *JSONL* file: one JSON object per line, the usual
input format for training and retrieval pipelines). Each record has `id`, `title`, `type`, `package`, `status`,
`links` (the notes it points to), `backlinks` and `text`.

- **Retrieval (recommended).** *Retrieval-augmented generation* (RAG) means the model looks up the most relevant
  notes when it answers. Point Claude Code, Hermes or any RAG tool at the vault folder or the JSONL file, and an
  agent starting a new SU2QC session gets the project map, the conventions and the latest gate status in a few
  thousand tokens.
- **Agent memory.** Add a line to a package's `CLAUDE.md`: "read `~/Projects/su2qc-Brain/00 SU2QC Map.md` and the notes it
  links before planning".
- **Fine-tuning (limited).** About 200 notes is far too small to teach a model physics by fine-tuning. It *is*
  enough for an evaluation set (questions whose answers are in the notes) or as a seed for generated
  question–answer pairs. The real training data in these projects are the measurement records and trajectories in
  the repositories themselves (see [[su2qc-jepa]] datasets and [[su2qc-skqd]] `data/hardware/`).
""")

# --------------------------------------------------------------------------- packages
note("Packages/genesis-su2-lgt.md",
     {"type": "package", "package": "genesis-su2-lgt", "status": "dormant", "tags": ["package"],
      "repo": "https://github.com/digonto10602/genesis-su2-lgt", "last_commit": "2026-08-13 a74543e",
      "commits": 11, "aliases": ["Genesis SU(2) LGT starter", "genesis_su2"]},
     r"""
# genesis-su2-lgt

**What it is.** The first SU2QC starter package (version 1.1.0, built on 2026-08-13 with Codex). It takes the
smallest genuine SU(2) gauge model that has already run on IBM hardware — two square plaquettes, pure gauge (no
quarks), links truncated at $j_{\max}=\tfrac12$ — and makes the *same* Hamiltonian run identically on every backend:
exact NumPy/SciPy, [[Qiskit]], [[CUDA-Q]], IBM Runtime, OpenMP C++ and a custom CUDA kernel.

**The physics.** After [[Gauss's law]] is imposed, the seven links reduce to two qubits. In units of $g^2/2$, with
$x = 2/g^4$ ([[Kavaki and Lewis 2024]], Eq. 1):

$$H = \tfrac38\,(7I - 3Z_0 - Z_0Z_1 - 3Z_1) - \tfrac{x}{2}(3I + Z_1)X_0 - \tfrac{x}{2}(3I + Z_0)X_1 .$$

One canonical [[Pauli decomposition]] is the single source; every backend is generated from it so that no backend can
drift to different physics.

## What it contains

- Code: [[genesis_su2.pauli]], [[genesis_su2.exact]], [[genesis_su2.su2]], [[genesis_su2.encodings]],
  [[genesis_su2.qml.energy_surrogate]], and backends [[genesis_su2.backends.qiskit_backend]],
  [[genesis_su2.backends.cudaq_backend]], [[genesis_su2.backends.ibm_runtime]].
- Gates G0–G7.8 (see [[Gates index]]): G0–G2 PASS, G3 PASS locally (Qiskit 2.5.1, no hardware), G4 PARTIAL (CUDA-Q
  skipped), G5 PASS (no advantage claimed), G6.1 completed-negative, G7.1–G7.4 PASS, G7.5–G7.6 not started,
  G7.7–G7.8 PARTIAL.
- An encoding study ([[Electric basis]] vs [[Quantum link (rishon) encoding]] vs [[Fuzzy gauge theory]]): the
  fuzzy option was marked *BLOCKED-SOURCE-DEFINITION* (no guessed matrices).
- A quantum-kernel energy surrogate: a learning exercise, see [[Quantum kernel methods]]. With 512 shots the
  kernel regression was unstable.
- Workflow: `AGENTS.md`, Codex prompts, `FEATURES.md` change log enforced in CI, [[Graphify code graph]].

## The research ladder it set out (README)

1. exact spectra and real-time evolution of the two-plaquette model → 2. Qiskit and CUDA-Q statevectors →
3. IBM hardware → 4. quantum-kernel surrogate → 5. plaquette chain checked with [[Tensor networks (MPS and TEBD)]] →
6. [[Staggered fermions]], meson/baryon observables, [[String breaking]] → 7. the proposal's 2+1D dressed-site model →
8. AI-assisted layout and calibration.

Step 5 was taken up by [[SU2ZX]] (plaquette chain, MPS to $N=32$); steps 6 and 7 by SU2ZX Section 8,
[[su2qc-skqd]] and [[su2qc-jepa]]; see [[Package lineage]].

## Status

Dormant since 2026-08-13. Open items: G7.5–G7.6 (matched reduced/unreduced Hamiltonian comparison), G9 tensor
networks, G12 hardware dry run, proposal milestone M1.
""")

note("Packages/su2qc-skqd.md",
     {"type": "package", "package": "su2qc-skqd", "status": "active", "tags": ["package"],
      "repo": "https://github.com/digonto10602/su2qc-skqd", "last_commit": "2026-10-06 b25f03f (PACKAGE_FULL_REPORT_20261006)",
      "commits": 200, "aliases": ["SKQD package", "SU2QC Project 2", "skqd"], "as_of": "2026-10-06"},
     r"""
# su2qc-skqd

**What it is.** The code package for *SU2QC Project 2, revision 2*: neural-enhanced
[[Sample-based Krylov quantum diagonalization (SKQD)]] of SU(2) lattice gauge theory with two-colour
[[Staggered fermions|staggered quarks]] on open $2\times L_x$ ladders. Built and validated from 2026-09-14; 200
commits; the busiest package. Full report: `reports/PACKAGE_FULL_REPORT_20261006.md`.

**The idea in plain words.** A quantum computer runs short time-evolution circuits from simple starting
configurations and is measured many times. The measured bit strings that pass the [[Codewords and the Gauss-law decoder|Gauss-law decoder]]
form a small set of configurations (the *support*). A classical computer then diagonalizes the exact Hamiltonian
inside that set. The answer can never be below the true ground energy, and the [[Ritz values and certified bounds|residual]]
gives a certified error bar.

**The model.** [[Kogut-Susskind Hamiltonian]] on a $2\times L_x$ patch, $j_{\max}=\tfrac12$, quark mass $m = 3g^2/16$.
Physical basis = [[Intertwiner (dressed-site) basis]]: 82 states at 2×2 (see [[Shared 2x2 plaquette]]), 1 727 at 2×3,
37 165 at 2×4, split by [[Baryon-number sectors|baryon number]].

## Code map

Physics core: [[skqd.su2]], [[skqd.lattice]], [[skqd.fermions]], [[skqd.vertex]], [[skqd.basis]], [[skqd.hamiltonian]],
[[skqd.fullspace]] (second, independent route), [[skqd.exact]].
Circuits: [[skqd.circuits_ir]] (backend-independent), [[skqd.circuits_qiskit]], [[skqd.circuits_cudaq]],
[[skqd.quantinuum_native]], [[skqd.reference_sim]], [[skqd.sparse_sim]], [[skqd.codec]].
Algorithm: [[skqd.krylov]], [[skqd.skqd]], [[skqd.controls]], [[skqd.ml]].
Device modelling: [[skqd.noise]], [[skqd.idle]], [[skqd.coherence]], [[skqd.device_req]], [[skqd.hardware]], [[skqd.hpc]].
Bookkeeping: [[skqd.report]].

## Gates (see [[Gates index]])

Of 46 gate result files, 34 PASS and 12 FAIL (the FAILs are re-defined cost gates, honest negative hardware results or
by-construction records). E1, E2, E3, S1, CS, L2, L4, L5 PASS; L3, S2, S2D FAIL on the CZ budget (criterion later amended);
H0 realised as the measurement gate [[skqd gate H0_2x2]] PASS 8/8; [[skqd gate CF_traj]] PASS 7/7 (5 Oct). Newest (5–6 Oct):
[[skqd gate CV_2x3_plan]] PASS 37/37 and [[skqd gate Q0P_2x3_plan]] PASS 7/7 (the 2×3 shot plan, emulated),
[[skqd gate K0_2x3_2x4]] PASS 6/6 (2×3 on IBM Heron NO-GO on a model), [[skqd gate H0_ddrep]] PASS (measurement ran;
the XY4 gain did not replicate), [[skqd gate K1_2x3_fpilot]] PASS 8/8 (measurement ran; decision NO-GO).
H1, H2, P1, M1 open. A gate PASS here means the run met its recording criteria, not that the hoped-for effect appeared.

## Hardware story so far

1. **ibm_fez** (Sept 2026): canary circuits failed the go rule; a diagnostic session followed ([[ibm_fez]]).
2. **ibm_kingston** (2 Oct 2026): pilot, a [[Dynamical decoupling]] A/B test, then the full 2×2 SKQD run — see
   [[Result - 2x2 SKQD run on ibm_kingston]] and [[Result - client-side XY4 gain did not replicate]] (2 Oct gain, not replicated 6 Oct).
3. **2×3**: ruled out on superconducting devices by the idle-time budget; compiled for [[Quantinuum H-series]]
   (gate Q0P_2x3, 0 HQC spent); [[IonQ Forte]] feasibility "2×3 no, 2×2 yes"; a QEC analysis (prompts/27) concluded
   error correction is a ~2029-class option — see [[Result - 2x3 needs a different device]].
4. **Statistic re-ruled** (prompts/29): the [[Clean-shot fraction]] estimator re-ruled with trajectory simulations;
   $r_{nc}=1.115$ ([[Result - CF_traj clean-fraction re-ruling]]).
5. **6 Oct, option A** (prompts/32): the 2×2 XY4 A/B test was repeated on the same frozen circuits — the gain did
   not replicate and the no-DD baseline doubled ([[Result - client-side XY4 gain did not replicate]]).
6. **6 Oct, option B**: the K1 2×3 pilot on ibm_kingston — 0 reference hits in $2\times10^5$ shots, a firm NO-GO
   ([[Result - 2x3 on ibm_kingston is a measured NO-GO]]).
7. **QPU account:** 327 s of 600 s used, 273 s left, 14 jobs. **Next:** Quantinuum access (emulator first, then a
   ≈9 950 HQC pilot; the full 2×3 campaign ≥ 665 605 HQC at $f=0.10$); the access email is still an unsent draft.

## How work runs here

[[Agent routing (planner, executor, reviewer, runner, scribe)]]: Fable 5.1 plans and writes numbered prompts, Opus
implements and reviews, Sonnet runs gates, Haiku keeps the tables. Every number in a report comes from a
`validation/*.json` file ([[Gate-and-evidence discipline]]). Heavy jobs go to [[NERSC Perlmutter]] via CI tokens.
Hardware sessions are preregistered ([[Preregistration]]).

## Is it publishable?

Report of 2026-10-06: the 2×2 result still supports a **methods note** (honest SKQD at a size where noise saturates the
subspace). The short note on client-side XY4 is **no longer supported as written** — at most a calibration-dependent,
non-replicated observation. **Not** an SU(2) physics result, because at 2×2 random strings through the decoder already
reproduce $E_0$. A physics claim needs 2×3 hardware data, which IBM cannot provide.
""")

note("Packages/su2qc-jepa.md",
     {"type": "package", "package": "su2qc-jepa", "status": "active", "tags": ["package"],
      "repo": "https://github.com/digonto10602/su2qc-jepa", "last_commit": "2026-10-06 4a23591 (jobs 013–014 queued)",
      "commits": 57, "aliases": ["Gauge-JEPA-P", "Gauge-JEPA-P v2", "su2qc_jepa"], "as_of": "2026-10-06"},
     r"""
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
""")

note("Packages/SU2ZX.md",
     {"type": "package", "package": "SU2ZX", "status": "paused", "tags": ["package"],
      "repo": "https://github.com/digonto10602/genesis-su2-zx-observables", "last_commit": "2026-09-10",
      "commits": 27, "aliases": ["genesis-su2-zx-observables", "su2qc package", "SU2ZX Foundation Code Package", "GI-cost campaign"]},
     r"""
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
""")

note("Packages/su2qc-qcadvantage.md",
     {"type": "package", "package": "su2qc-qcadvantage", "status": "paused", "tags": ["package"],
      "repo": "https://github.com/digonto10602/su2qc-qcadvantage", "branch": "claude/modest-mayer-kh4s6b",
      "last_commit": "2026-10-06", "commits": 29, "aliases": ["SU(2) torus frontier run", "su2torus", "qcadvantage"],
      "as_of": "2026-10-06"},
     r"""
# su2qc-qcadvantage

**Goal.** A lattice-gauge-theory simulation that a quantum computer can run and that is hard to reproduce classically:
the "SU(2) torus frontier run" (Claude's label from `docs/idea.md`, 2 Oct 2026). Take the
[[One-qubit-per-plaquette SU(2) model]] of [[Ciavarella et al. 2026]], put it on a torus of $N=48$–$64$ plaquettes, quench it
and watch it thermalize ([[Thermalization and canonical typicality]]) for 7–10 Trotter steps on all-to-all trapped ions
([[Quantinuum H-series]]: Helios, H2), with the abelian twin as control.

**Repository state.** All work sits on branch `claude/modest-mayer-kh4s6b` (29 commits, 5–6 Oct 2026, a Claude Code cloud
session); `main` holds only the initial plan commit. Tags `m1-done` … `m6-done`, `v0.1-pre-cluster` exist only in the cloud
session (the proxy did not allow tag pushes).

## Milestones (cloud phase, all with locked acceptance tests; full suite 167 passed)

| milestone | what | gate note |
|---|---|---|
| M1 | lattice + Hamiltonian (sparse, Pauli, matrix-free numba) | [[qca gate M1]] |
| M2 | exact evolution, Trotter circuits, gate counts: first-order step $9.5n$ (native ZZ) / $11n$ (CZ) two-qubit gates | [[qca gate M2]] |
| M3 | small-torus physics at $N=12, 24$ | [[qca gate M3]] |
| M4 | noisy emulation + mitigation at $N=12$ | [[qca gate M4]] |
| M5 | MPS code, resource table, cluster configs | [[qca gate M5]] |
| M6 | MPS convergence at $N=48$, collaborator package | [[qca gate M6]] |

Results: [[Result - qcadvantage thermalization and the beta=0 states]] · [[Result - qcadvantage noise mitigation at N=12]] ·
[[Result - qcadvantage MPS frontier at N=48]]. Open decisions: [[Decision - qcadvantage open questions before the cluster]].

## Code (`su2torus/`)

[[su2torus.lattice]] (honeycomb plaquette graph) → [[su2torus.hamiltonian]] → [[su2torus.exact]] (expm_multiply / Chebyshev) ·
[[su2torus.trotter]] (circuits, gate counts) · [[su2torus.observables]] · [[su2torus.thermal]] (exact and typicality anchors) ·
[[su2torus.noise]] (Aer noise, [[Loschmidt echo]], [[Zero-noise extrapolation]]) · [[su2torus.mps]] (quimb CircuitMPS,
[[Tensor networks (MPS and TEBD)]]).

## Workflow

The physics loop (coordinator, builder, tester, fixer, auditor, planner agents) with `notes/STATUS.md`, locked
acceptance tests (`tests/acceptance/LOCK.json`), audits in `reports/audits/`, and `scripts/check_summary.py`, which
re-reads every number in the collaborator summary from the JSON result files.

## Status

Stopped on purpose before any GPU-cluster work. Next (from the summary): large-$\chi$ MPS on GPU at $N=48$–$96$,
PEPS with belief-propagation gauging, Pauli propagation; then the hardware run.
""")

note("Packages/su2qc-trotter.md",
     {"type": "package", "package": "su2qc-trotter", "status": "done", "tags": ["package"],
      "repo": "https://github.com/digonto10602/su2qc-trotter", "last_commit": "2026-09-27", "commits": 79,
      "aliases": ["su2trotter", "trotter-ci", "lean plaquette circuit"], "as_of": "2026-10-06"},
     r"""
# su2qc-trotter

**Goal.** Count the fault-tolerant cost ([[Clifford+T and T-count]]) of **one SU(2) plaquette evolved by one Trotter
step** in the $j_{\max}=\tfrac12$, 12-qubit encoding (3 qubits per link, 625 valid states out of 4096), built, verified and
counted with [[CUDA-Q]]. Specification: `plan/hamiltonian-gauge-theories-circuits (1).pdf`, Sec. IV.A (Eqs. 31–39).
Private repository, 79 commits, 24–27 Sept 2026.

**Starting point.** The 34-qubit Clifford+T circuit of Eq. 39 from [[su2qc-paulo-code]] (copied to `reference/`).

**Main result.** A **lean 22-qubit design** (12 data + 10 ancilla qubits): 424 T instead of 1162, 210 CX instead of 294,
depth 966 instead of 2549, verified exhaustively on all 625 encoded basis states and on Perlmutter GPUs.
See [[Result - lean 22-qubit plaquette Trotter step]] and [[Result - lean and reference circuits agree on GPUs]].

## Code (`src/su2trotter/`)

[[su2trotter.physics]] (the plaquette operator from Eqs. 25–28) → [[su2trotter.baseline]] (the Eq. 39 design) and
[[su2trotter.lean]] (the lean design) → [[su2trotter.synth]] (Clifford+T synthesis) → [[su2trotter.cudaq_backend]] ·
[[su2trotter.pipeline]] · [[su2trotter.sim]] · [[su2trotter.analysis]] · [[su2trotter.trotter]] · [[su2trotter.compare]].

## Perlmutter CI (`trotter-ci`)

Same design as su2qc-skqd's `skqd-ci` ([[Perlmutter job queue]]): push a token to `ci/request.txt`, a scrontab poller on
[[NERSC Perlmutter]] runs it and pushes `validation/ci_<token>.json`. Jobs: [[trotter gate smoke]], [[trotter gate R1]],
[[trotter gate V1]], [[trotter gate B1]], [[trotter gate G22]], [[trotter gate M0]], [[trotter gate G34]] — all PASS.
Errors met and fixed: `docs/CI_LOG.md` (fp32 norm drift criterion, GPU state copy, CI overwriting hand-written reports).

## Status

Done (last commit 27 Sept: LaTeX report in `docs/report`). Further reductions noted but not taken: measurement-based
uncomputation (−40 T), Hamming-weight phasing of the electric rotations.
""")

note("Packages/su2qc-paulo-code.md",
     {"type": "package", "package": "su2qc-paulo-code", "status": "reference", "tags": ["package"],
      "aliases": ["SU2_plaquette_12qubit_encoding", "Eq. 39 circuit", "promise-aware plaquette circuit"], "as_of": "2026-10-06"},
     r"""
# su2qc-paulo-code

A local folder (not a git repository; files dated 10 Sept 2026) holding `SU2_plaquette_12qubit_encoding/`:

- `optimized_plaquette_dontcare_lowT.ipynb` — a Qiskit notebook (47 cells) that builds the *promise-aware* ("don't-care",
  low-T) circuit for one SU(2) plaquette step at $j_{\max}=\tfrac12$: 12 data qubits (3 per link), and it only needs to be
  right on the $5^4=625$ valid encoded states. It verifies the 625×625 block exhaustively in NumPy (41 two-state "bright"
  blocks, 543 "dark" singletons).
- `SU2_plaquette_jmax_half_CT.qasm` / `.qpy` and `_metadata.json` — the compiled Clifford+T circuit: **34 qubits**
  (12 data + 22 work), 3207 gates, depth 2549, **1162 T/T†**, 294 CX, rotations synthesised to $\epsilon=10^{-6}$
  (Qiskit 2.5.2, optimisation level 3, seed 12345).

The folder name credits Paulo; the files themselves do not name an author. This is "Eq. 39" of the
[[su2qc-trotter]] plan, and su2qc-trotter keeps an identical copy in `reference/`. CUDA-Q re-counts it exactly
(34 / 3207 / 2549 / 1162 / 294). Concepts: [[Clifford+T and T-count]], [[Link truncation (j_max)]],
[[Plaquette and Wilson loop]].
""")

note("Decisions/Decision - qcadvantage open questions before the cluster.md",
     {"type": "decision", "package": "su2qc-qcadvantage", "status": "waiting", "tags": ["decision"], "as_of": "2026-10-06"},
     r"""
# Decision - qcadvantage open questions before the cluster

Four decisions that `notes/STATUS.md` of [[su2qc-qcadvantage]] (6 Oct 2026) leaves to you. **Not yet decided.**

1. **Initial state at $N=48$–$64$.** The plan prescribes the stripe state, but on tori with even $L_1$ it sits at
   $\beta=0$ (thermal = decohered), so it cannot separate physics from noise. Recommended: the SU(2) vacuum
   ($\beta\approx1.4$) or an odd-row state. Evidence: `reports/m3_physics.md` §3; [[Result - qcadvantage thermalization and the beta=0 states]].
2. **Open-lattice electric term.** The code uses the bond form; METHODS' $3n_p$ form differs on open lattices
   (string $E_E(0)=4.41$ vs $5.88$). Evidence: `reports/audits/m1_audit.md`.
3. **Trotter step size.** $2\delta t/g^2=0.9$ (plan M6) departs strongly from $e^{-iHt}$: at $N=12/16$, step 8, Trotter
   $\langle H_E\rangle$ is 0.54 versus exact 0.31 (fractions of $E_\infty$). Decide $\delta t$ before cluster thermal-anchor
   work. Evidence: `reports/audits/m6_audit.md`.
4. **Tags.** Push `m1-done` … `v0.1-pre-cluster` from a machine with tag-push rights (`git push origin --tags`).
""")

# --------------------------------------------------------------------------- cross-package
note("Cross-package/Shared 2x2 plaquette.md",
     {"type": "concept", "tags": ["concept", "cross-package"], "aliases": ["82-state plaquette", "one plaquette with quarks"]},
     r"""
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
""")

note("Cross-package/Package lineage.md",
     {"type": "hub", "tags": ["cross-package"]},
     r"""
# Package lineage

```mermaid
flowchart LR
  G[Genesis Phase-I proposal] --> A[genesis-su2-lgt<br/>Aug 2026<br/>pure gauge, 2 qubits]
  A --> Z[SU2ZX<br/>Sept 2026<br/>chain compiler study v0.4.0,<br/>plaquette + quarks v0.5.0,<br/>GI-cost campaign v0.6]
  Z --> S[su2qc-skqd<br/>from 14 Sept<br/>SKQD, IBM hardware]
  Z --> J[su2qc-jepa<br/>from 1 Oct<br/>JEPA world model]
  S -. hardware lessons .-> J
  PC[su2qc-paulo-code<br/>Sept 2026<br/>34-qubit Clifford+T circuit] --> T[su2qc-trotter<br/>24-27 Sept<br/>lean 22-qubit step, CUDA-Q]
  S -. CI design .-> T
  Q[su2qc-qcadvantage<br/>5-6 Oct<br/>torus frontier run]
  S -. physics loop, agents .-> Q
```

| from → to | what was inherited |
|---|---|
| [[genesis-su2-lgt]] → everything | one canonical Hamiltonian feeding all backends; gate tables; [[Graphify code graph]]; "no guessed physics" rule |
| [[SU2ZX]] → [[su2qc-jepa]] | verified `su2qc` physics code (cross-check target), conventions of 9 Sept, the twin-seed lesson |
| [[SU2ZX]] → [[su2qc-skqd]] | the one-plaquette-with-matter system, the 82-state count, the lesson that the L12 circuits are too deep |
| [[genesis-su2-lgt]] → [[SU2ZX]] | Codex workflow (`AGENTS.md`), the Graphify harness, the step-5 plaquette chain |
| Genesis research ladder step 6–7 → skqd, jepa | staggered fermions, meson/baryon observables, string breaking, dressed-site basis |
| [[su2qc-skqd]] → [[su2qc-jepa]] | Claude Code agent routing, numbered prompts, Perlmutter use (both now share the same working style) |
| [[su2qc-paulo-code]] → [[su2qc-trotter]] | the Eq. 39 34-qubit circuit (kept in `reference/`) as the baseline to beat |
| [[su2qc-skqd]] → [[su2qc-trotter]] | the GitHub-to-Perlmutter CI design (`skqd-ci` → `trotter-ci`, separate key, poll minute :37) |
| (new model) → [[su2qc-qcadvantage]] | different physics: pure-gauge one-qubit-per-plaquette model from [[Ciavarella et al. 2026]], not the 2×2 plaquette with quarks; inherits the Claude Code physics loop (locked acceptance tests, audits) |

Workflow drift worth knowing: genesis-su2-lgt and SU2ZX v0.4.0 were built with **Codex** (`AGENTS.md`); SU2ZX
Section 8 and the GI-cost campaign with the **Hermes** orchestrator; su2qc-skqd and su2qc-jepa with **Claude Code**
(`CLAUDE.md`, `.claude/agents`).
""")

note("Cross-package/Cross-package opportunities.md",
     {"type": "hub", "tags": ["cross-package", "claude-note"]},
     r"""
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
""")

note("Cross-package/Lessons that travelled.md",
     {"type": "hub", "tags": ["cross-package"]},
     r"""
# Lessons that travelled

| lesson | where it was learnt | where it is now built in |
|---|---|---|
| Aer seeds shot $k$ with `seed + k`, so runs seeded `seed`, `seed+1` overlap in $N-1$ of $N$ shots and every quoted spread was void | [[SU2ZX]] GI-cost campaign, session c060_p0_20260909_5 (seeds 500/501: 1 023 shift matches of 1 024) | [[su2qc_jepa.twin.run]] spawns independent seeds; a row of [[jepa gate J0]] tests it |
| generated code documentation covered a different package than the one under test, letting the twin-seed defect through review | SU2ZX v0.6.3 | [[Graphify code graph]] rebuilt every session and freshness-checked in CI ([[Decision - jepa 001 numbered artifacts and Graphify]]) |
| a raw residual against the twin correlates ~perfectly with the exact error, so a "Spearman ≥ 0.7" bar is meaningless without label-free baselines | su2qc-jepa plan audit | [[jepa gate J3]] must report raw_twin, flag_rate, jepa_self, jepa_t0 |
| at 2×2, random strings through the decoder already reproduce $E_0$ (sector saturation) | [[su2qc-skqd]] H0_2x2 | garbage-only and random-equal-size baselines are now mandatory in skqd reports |
| the device model can be 5× off; measure first | su2qc-skqd kingston pilot | skqd: pilot before every main run; jepa plan: 1.5-minute pilot measures the real rate |
| an "all outputs verified at 1e-10" flag was too strong: default-tolerance `Operator.equiv` never checked routed outputs, and PyZX's QASM rounding added ~1e-10 errors | [[SU2ZX]] v0.4.0 audit | explicit atol/rtol and independent routed-output checks; skqd verifies circuits against its own IR to < 1e-10 |
| a builder can silently miss physics (route 1 omitted dressed-vertex recoupling factors) — only a second independent route catches it | [[SU2ZX]] Section 8, solutions/0.5.0.md | every package now builds the Hamiltonian two ways |
| one Hamiltonian, many backends: never re-type physics per backend | [[genesis-su2-lgt]] | skqd's backend-independent IR ([[skqd.circuits_ir]]); jepa's two-route builder |
| a one-day hardware A/B test is not a result: the device's no-DD clean fraction doubled in 4 days, more than the XY4 effect | [[su2qc-skqd]] H0_ddrep (6 Oct) | skqd's 2026-10-06 report withdraws the XY4 note as written; [[Cross-package opportunities]] item 1 |
| code that only runs on a GPU on the cluster can fail where the laptop never shows it (CPU network, GPU data) | [[su2qc-jepa]] jobs 002–007 | a device test in the CPU and CUDA cases; a 2-epoch GPU smoke job before long runs |
""")

# --------------------------------------------------------------------------- results
note("Results/Result - 2x2 SKQD run on ibm_kingston.md",
     {"type": "result", "package": "su2qc-skqd", "tags": ["result"], "date": "2026-10-02"},
     r"""
# Result - 2x2 SKQD run on ibm_kingston

**Date:** 2026-10-02. **Gate:** [[skqd gate H0_2x2]] PASS 8/8. **Device:** [[ibm_kingston]]. **Package:** [[su2qc-skqd]].

- 7 reference configurations × $k=1..4$ = 28 circuits on 12 qubits; one coarse step ≈ 588 CZ, ≈ 44 µs.
- Decoder: 0 mismatches on 58 hardware strings ([[Codewords and the Gauss-law decoder]]).
- Measured [[Clean-shot fraction]]: $f = 0.1271\ [0.1084, 0.1479]$ with client DD, $0.0413$ without.
- Signal support: 35 of 38 states ($B=0$), 19 of 20 ($B=1$) above the 3σ noise line.
- Energies ([[Ritz values and certified bounds]]): $B=0$: $E_R=-3.6402189$, $r_H = 0.0603$, $|E_R-E_0| = 5.48\times10^{-4}$;
  $B=1$: $E_R = -1.8615823$, $r_H = 5.95\times10^{-3}$, $|E_R-E_0| = 5.75\times10^{-6}$. All intervals contain the exact $E_0$.

**The catch.** At 2×2 the sector is so small that uniformly random strings through the same decoder give $E_R=E_0$
exactly (garbage-only baseline, 100 seeds). So the energies are a pipeline validation, not evidence that "the device
finds the ground state" ([[van Rossum et al. 2026]]). A physics claim needs 2×3 ([[Result - 2x3 needs a different device]]).
""")

note("Results/Result - client-side XY4 gain did not replicate.md",
     {"type": "result", "package": "su2qc-skqd", "tags": ["result"], "date": "2026-10-06", "as_of": "2026-10-06",
      "aliases": ["Result - client-side XY4 raises clean fraction"]},
     r"""
# Result - client-side XY4 gain did not replicate

**2 Oct 2026** ([[skqd gate H0_ddtest]] PASS): a one-job A/B test on [[ibm_kingston]] of client-side
[[Dynamical decoupling]] variants against no DD. Client-side XY4 in the long idle windows raised the
[[Clean-shot fraction]] by a ratio $R_{T3}=2.819\ [2.495, 3.185]$ (no DD 0.0400, XY4 0.1129); the context-aware variant collapsed;
IBM's runtime DD gave no gain.

**6 Oct 2026** ([[skqd gate H0_ddrep]], job `db29p6nr11fs7396e4ig`, 37.0 s QPU): the same frozen circuits again.

| | 2 Oct | 6 Oct |
|---|---|---|
| no-DD clean fraction | 0.0400 [0.0358, 0.0446] | 0.0818 [0.0758, 0.0881] |
| client XY4 (cell T3) | 0.1129 [0.1058, 0.1203] | 0.0732 [0.0675, 0.0792] |
| ratio $R_{T3}$ | 2.819 [2.495, 3.185] | 0.895 [0.804, 0.996] |

The gain did not replicate; the context-aware collapse did not replicate either; a coherent $x$-pulse over-rotation
of 0.015–0.020 rad was measured on all 12 qubits. **Lesson:** the day-to-day change of the device (factor ≈ 2 in the
no-DD baseline) is larger than the decoupling effect being tested, so a one-day A/B test is not a result. Intervals
are 95 %; numbers from `validation/H0_ddtest.json`, `validation/H0_ddrep.json` via skqd's 2026-10-06 full report.
""")

note("Results/Result - 2x3 on ibm_kingston is a measured NO-GO.md",
     {"type": "result", "package": "su2qc-skqd", "tags": ["result"], "date": "2026-10-06", "as_of": "2026-10-06"},
     r"""
# Result - 2x3 on ibm_kingston is a measured NO-GO

[[skqd gate K1_2x3_fpilot]] (prompts/32 part B; job `db2avbe8v0ts73c2i8b0`, 188.0 s QPU, preregistered on calibration
`99035ef0`). Two signed 2×3 circuits (5 659 routed CZ, about 411 µs each), 4 pubs × $10^5$ shots on [[ibm_kingston]].

- **0 reference hits in $2\times10^5$ shots**, against 0.191 expected from pure garbage.
- 95 % upper bound on the ideal-sample fraction $\hat f_{\rm ideal}\le2.06\times10^{-5}$, roughly 4 850× below the signed
  bar of 0.1 ([[Clean-shot fraction]]).
- This confirms the model verdict of [[skqd gate K0_2x3_2x4]] (2×3 NO-GO on IBM Heron) with a measurement.

**Consequence.** Only Quantinuum's H2-2 and Helios-1 meet the signed gate-error bar on published numbers (0.1502 and 0.1642
gate-only; [[Quantinuum H-series]]). The 2×3 shot plan of record costs 665 605 HQC at $f=0.10$ ([[skqd gate CV_2x3_plan]]).
See [[Result - 2x3 needs a different device]].
""")

note("Results/Result - 2x3 needs a different device.md",
     {"type": "result", "package": "su2qc-skqd", "tags": ["result"], "date": "2026-10-02", "as_of": "2026-10-06"},
     r"""
# Result - 2x3 needs a different device

- On superconducting devices the 2×3 coarse step is longer and more serial than 2×2; the idle-time budget
  ([[Decoherence (T1 and T2)]], [[skqd.idle]]) rules it out (amendment 01 item 4; [[skqd gate S2D]] FAIL).
- [[IonQ Forte]]: "2×3 no, 2×2 yes" from published specifications.
- [[Quantinuum H-series]]: the 2×3 circuits are compiled to the native gate set and verified exactly
  ([[skqd gate Q0P_2x3]] PASS; 0 HQC spent, no Nexus login yet).
- Error correction (prompts/27): full QEC ≈ $10^5$ T gates per shot (a ~2029-class option); an Iceberg error-detection
  code is a net loss because the Gauss-law codewords already form a distance-2 detection code; there is no quantum
  "amplifier", but more shots help — usable clean fraction at 2×3 drops to about $10^{-3}$.
- **Measured on 6 Oct:** IBM at 2×3 is a firm NO-GO ([[Result - 2x3 on ibm_kingston is a measured NO-GO]]). The
  re-sized 2×3 plan (rule D3'-R, sector $B=1$ doubled) costs 1 279 660 / 665 605 / 471 801 HQC at $f=0.05/0.10/0.15$;
  a Quantinuum access email exists as an unsent draft.
- The planned substantial result is the primary endpoint P1 (device support vs CIPSI/BFS/random/ML at equal size) on
  2×3 hardware data ([[CIPSI and classical support controls]]).
""")

note("Results/Result - CF_traj clean-fraction re-ruling.md",
     {"type": "result", "package": "su2qc-skqd", "tags": ["result"], "date": "2026-10-05"},
     r"""
# Result - CF_traj clean-fraction re-ruling

[[skqd gate CF_traj]] PASS 7/7 (prompts/29 Part A', 2026-10-05). Trajectory simulations show that the
reference-string hit fraction $f_{\rm hit}$ estimates the *ideal-sample fraction* $f_{\rm ideal}$ (shots whose output
distribution equals the ideal one), not the error-free fraction. Pooled $k=1$ ratio $f_{\rm hit}/f_{\rm ideal} = 1.069\ [1.029, 1.115]$,
so $r_{nc} = 1.115$ is the correction used for go/no-go decisions. Under idle dephasing (2×2, $T_2^\*$ end) the hit
fraction **under**-estimates $f_{\rm ideal}$ ($r=0.674$). Part B' (applying the new statistic to decisions) waits for the owner.
See [[Clean-shot fraction]].
""")

note("Results/Result - J0 data gate passed.md",
     {"type": "result", "package": "su2qc-jepa", "tags": ["result"], "date": "2026-10-03"},
     r"""
# Result - J0 data gate passed

[[jepa gate J0]] PASS 9/9 (2026-10-03): 82 states, sectors 2/20/38/20/2, electric-limit degeneracies 16/16/18/16/16;
two construction routes agree to $4.4\times10^{-16}$; $[G,H]=0$; estimator bias within 4 standard errors; the $K=12$
Krylov chain reproduces the P-A window to $1.05\times10^{-4}$; 5 twin repeats independent; no split leakage. Cross-check
with [[SU2ZX]]: max deviation $7.3\times10^{-14}$. Datasets: `main`, `chain_onfam`, `chain_strong` (built on Perlmutter).
""")

note("Results/Result - J1 energy information ceiling.md",
     {"type": "result", "package": "su2qc-jepa", "tags": ["result"], "date": "2026-10-05"},
     r"""
# Result - J1 energy information ceiling

Before judging whether the JEPA latent "knows" the energy, su2qc-jepa measured how much energy information one
clean observation contains at all: best $R^2 = 0.9145$ (0.994 if the couplings are also given). The J1 energy
grounding threshold was therefore set to $0.97\times0.9145 = 0.887$ ([[Decision - jepa 005 J1 energy threshold]]).
""")

note("Results/Result - J1 ladder fails on the semigroup row.md",
     {"type": "result", "package": "su2qc-jepa", "tags": ["result"], "date": "2026-10-06", "as_of": "2026-10-06"},
     r"""
# Result - J1 ladder fails on the semigroup row

[[jepa gate J1]], 5 seeds × 200 epochs per run on [[NERSC Perlmutter]]; thresholds in `configs/gates.yaml`: effective
rank ≥ 8 (how many latent directions the model really uses; low rank = partial *collapse*), $R^2$ energy ≥ 0.887,
$C_{\rm string}$ ≥ 0.99, $P_{\rm meson}$ ≥ 0.95, $P_{\rm baryonic}$ ≥ 0.98, and **semigroup residual < $10^{-3}$** (the relative
mismatch between predicting two steps at once and one step twice).

| run (change vs base) | rank min | semigroup max | verdict |
|---|---|---|---|
| `v1_base` | 5.16 | $3.3\times10^{-3}$ | FAIL (rank, semigroup) |
| `v1_wsigreg2` ([[SIGReg]] weight 2) | 8.26 | $5.3\times10^{-3}$ | FAIL (semigroup) |
| `v1_wsigreg5` | 10.5 | $8.5\times10^{-3}$ | FAIL (semigroup) |
| `v1_latent32` | 6.12 | $4.7\times10^{-3}$ | FAIL |
| `v1_ema` | 13.1 | $2.2\times10^{-2}$ | FAIL (also $P_{\rm meson}$ 0.915) |
| `v1_wground3` | 5.63 | $6.9\times10^{-3}$ | FAIL |
| `v1_curriculum` | 6.18 | $2.9\times10^{-3}$ | FAIL |
| `v1_wsemigroup1` (semigroup weight 1) | 4.94 | $1.7\times10^{-3}$ | FAIL |
| `v1_wsig2_wsg1` | 8.56 | $5.6\times10^{-3}$ | FAIL (semigroup) |

- Energy, $C_{\rm string}$ and $P_{\rm baryonic}$ pass in every run reported in `reports/012`; energy $R^2\approx0.90$, within
  ≈ 0.015 of the measured ceiling ([[Result - J1 energy information ceiling]]).
- Raising the SIGReg weight fixes the rank but the semigroup residual grows with rank (Pearson 0.898 between rank and
  $\log_{10}$ residual over 30 runs — a correlation among runs that also differ in loss weights, not a proven mechanism).
- The plan's fallback (J1 PARTIAL) is written for a rank failure, not a semigroup failure; no rule covers this case yet.
- Queued: jobs 013 (`v1_wsig2_wsg3`) and 014 (`v1_wsig2_wsg10`), stronger semigroup weights with SIGReg 2.

Sources: `reports/012` §8.3 (first six rows), `evidence/GATE_LEDGER.md` and the gate commits of 6 Oct (last three rows).
""")

note("Results/Result - genesis QML surrogate is a negative result.md",
     {"type": "result", "package": "genesis-su2-lgt", "tags": ["result"], "date": "2026-08-13"},
     r"""
# Result - genesis QML surrogate is a negative result

[[genesis-su2-lgt]] gate G5 trained a quantum-kernel regression ([[Quantum kernel methods]]) to predict $E_0(x)$ from
the coupling and one early-time return probability, against mean, linear and classical RBF-SVR baselines: it works
with exact kernels but claims no advantage. G6.1: with 512 shots the kernel estimate made the regression unstable —
recorded as COMPLETED-NEGATIVE.
""")

note("Results/Result - qcadvantage thermalization and the beta=0 states.md",
     {"type": "result", "package": "su2qc-qcadvantage", "tags": ["result"], "date": "2026-10-06", "as_of": "2026-10-06"},
     r"""
# Result - qcadvantage thermalization and the beta=0 states

[[qca gate M3]], exact dynamics on tori of $N=12$ and $24$ plaquettes at $g=1.25$ (`results/m3/summary.json`).

- From the vacuum the SU(2) model relaxes toward a thermal state with $\beta=1.440$ ($N=24$) and $1.448$ ($N=12$); the
  typicality uncertainty is $\pm0.04$ in $\beta$, so no finite-size shift is resolved
  ([[Thermalization and canonical typicality]]).
- At $g\le1.25$ the abelian twin relaxes more slowly; its thermal electric energy is 8.13 versus 5.15 for SU(2) ($N=24$).
- **The stripe and Néel-half states sit at infinite temperature** ($\beta=0$) on even-$L_1$ tori, including the $N=48$
  frontier torus: exactly half the bonds are cut, so their late-time values equal the decohered values. For the abelian
  twin $\langle H_E\rangle(t)$ is then exactly constant, by symmetry.
- Energy is conserved to below $10^{-7}$. Recommended physics target: the SU(2) vacuum at $g\approx1.25$–$1.4$.
  This feeds [[Decision - qcadvantage open questions before the cluster]] item 1.
""")

note("Results/Result - qcadvantage noise mitigation at N=12.md",
     {"type": "result", "package": "su2qc-qcadvantage", "tags": ["result"], "date": "2026-10-06", "as_of": "2026-10-06"},
     r"""
# Result - qcadvantage noise mitigation at N=12

[[qca gate M4]]: $N=12$ torus, stripe state, $g=1.25$, $\delta t=0.45g^2$, exact density-matrix simulation with
two-qubit depolarizing noise $p_2\in\{7.9\times10^{-4},10^{-3},1.5\times10^{-3}\}$ (Helios / H2 / Heron-like), plus
one-qubit $3\times10^{-5}$ and readout $10^{-3}$ ([[Noise models and digital twin]]). Emulated, not hardware.

| 10 steps, $p_2=10^{-3}$ (1140 two-qubit gates) | $\langle H_E\rangle$ |
|---|---|
| noiseless circuit | 6.27 |
| raw noisy | 6.01 |
| [[Zero-noise extrapolation]] (folding 1, 3, 5) | 6.22 |

- ZNE reduces the error 5.8–15.5× in 4 of 4 configurations (acceptance needed ≥ 2× in 3 of 4).
- [[Loschmidt echo]] fidelity 0.370 versus predicted $\prod(1-\epsilon)=0.334$; across configurations within 3–13 %.
- Rescaling local observables by the *global* fidelity over-corrects them and makes errors worse: do not use it.
""")

note("Results/Result - qcadvantage MPS frontier at N=48.md",
     {"type": "result", "package": "su2qc-qcadvantage", "tags": ["result"], "date": "2026-10-06", "as_of": "2026-10-06"},
     r"""
# Result - qcadvantage MPS frontier at N=48

[[qca gate M6]]: $N=48$ ($4\times6$) torus, stripe state, $g=1.25$, $\delta t=0.703$ ($2\delta t/g^2=0.9$), 8 first-order
Trotter steps, [[Tensor networks (MPS and TEBD)|MPS]] bond dimension $\chi=32, 64, 128, 256$ (`results/m6/convergence.json`).

- **Criterion:** successive $\chi$ agree in $\langle H_E\rangle$ to 1 % of the decohered value (0.211) and in every
  $\langle Z_p\rangle$ to 0.01.
- **Converged through step 2** ($t=1.41$); step 3 marginal (largest $\Delta\langle Z_p\rangle = 0.013$, 4 of 48 plaquettes
  over tolerance); unconverged from step 4.
- Cumulative truncation error at step 8 for $\chi=256$: 0.79 (estimated overlap with the exact state ≈ 0.21).
- $\langle H_E\rangle$ alone is misleading: it agrees between $\chi$ values to 0.11 at every step because it averages
  72 bonds; local magnetizations are the sensitive probe.
- Cost: $\chi=256$ took 6935 s single-threaded on a 4-vCPU cloud machine.
- MPS validation ([[qca gate M5]]): $N=24$, $\chi=256$, 4 steps at $\delta t=0.2$: $1-F=1.1\times10^{-9}$.

**Meaning.** At these step sizes, exact-quality MPS at $N=48$ fails after 2–3 steps with $\chi\le256$. Whether GPU MPS
($\chi=1024$–$4096$), PEPS or Pauli propagation reach 4–8 steps decides the advantage claim. Hardware budget from
`results/m5/resources.json`: 456 native-ZZ gates per step at $N=48$; raw fidelity 0.161 after 4 steps at $p_2=10^{-3}$.
Caveat from the M6 audit: at this $\delta t$ the Trotter circuit is far from $e^{-iHt}$
([[Decision - qcadvantage open questions before the cluster]] item 3).
""")

note("Results/Result - lean 22-qubit plaquette Trotter step.md",
     {"type": "result", "package": "su2qc-trotter", "tags": ["result"], "date": "2026-09-24", "as_of": "2026-10-06"},
     r"""
# Result - lean 22-qubit plaquette Trotter step

[[su2qc-trotter]], one plaquette, one Trotter step, $g_s=g_t=a=\Delta t=1$ ($\alpha=2$), rotations synthesised to
$\epsilon=10^{-6}$ each, basis {H, S, S†, T, T†, CX}; counts from `cudaq.estimate_resources` ([[trotter gate R1]] reproduced
them on Perlmutter under a different CUDA-Q version).

| circuit | qubits (data + ancilla) | gates | depth | T/T† | CX |
|---|---|---|---|---|---|
| Eq. 39, [[su2qc-paulo-code]] export | 34 (12 + 22) | 3207 | 2549 | 1162 | 294 |
| same design, su2qc-trotter's CUDA-Q compile | 34 (12 + 22) | 1678 | 1171 | 660 | 294 |
| **lean design** | **22 (12 + 10)** | **1681** | **966** | **424** | **210** |
| lean + electric term (full Trotter step) | 22 | 2309 | 1118 | 680 | 210 |

- Lean T = 172 fixed (logic) + 252 in 4 synthesised rotations; 4 arbitrary rotations is the minimum for its flag structure
  (checked over all parity bases).
- T versus $\epsilon$: lean 264 ($10^{-2}$) … 586 ($10^{-10}$); baseline 426 … 914.
- Exhaustive check on all 625 encoded inputs: logical circuits $\|U-e^{i\phi}V\|_2\le3.4\times10^{-14}$, leakage 0;
  Clifford+T circuits $1.1\times10^{-6}$ (lean), below the summed synthesis error.
- See [[Clifford+T and T-count]], [[Trotter and Strang splitting]].
""")

note("Results/Result - lean and reference circuits agree on GPUs.md",
     {"type": "result", "package": "su2qc-trotter", "tags": ["result"], "date": "2026-09-27", "as_of": "2026-10-06"},
     r"""
# Result - lean and reference circuits agree on GPUs

[[su2qc-trotter]] on [[NERSC Perlmutter]] A100s, [[CUDA-Q]] 0.16.0, fp64 state vectors.

- [[trotter gate V1]]: 48 GPU runs of the lean circuit; worst $1-F = 7.0\times10^{-14}$ (exact rotations),
  $1.4\times10^{-12}$ (Clifford+T).
- [[trotter gate B1]]: 60 steps from the strong-coupling vacuum, $dt=0.1$: circuit equals the exact Trotter product to
  $1-F=4.0\times10^{-12}$ (fp64), 25 ms per step; the vacuum empties and revives with period ≈ 3.
- [[trotter gate G22]] / [[trotter gate G34]]: 8 side-by-side tests, the 34-qubit reference on 32 A100s (8 nodes, 256 GB
  state) and the lean circuit on 1 A100. With ideal rotations the two agree to $10^{-12}$ in every test; a
  [[Loschmidt echo]] with one technique forward and the other backward returns to $8.6\times10^{-14}$ (1 step) and
  $8.9\times10^{-13}$ (10 steps). Clifford+T differences are $\sim10^{-5}$ (from synthesis). Cost ≈ 20 node-hours.
""")

note("Genesis Phase-I proposal.md",
     {"type": "hub", "tags": ["hub", "proposal"], "aliases": ["Genesis", "Genesis proposal"]},
     r"""
# Genesis Phase-I proposal

*AI-Accelerated Non-Abelian Gauge Dynamics on Quantum Hardware* (NMSU / BNL / UMD) — the parent document of every
SU2QC package. It asks for SU(2) lattice gauge theory Hamiltonians, quantum circuits and physical observables on real
quantum hardware, with AI/ML accelerating the workflow.

| package | which part of the proposal it serves |
|---|---|
| [[genesis-su2-lgt]] | backend-portable starter; encoding comparison; first QML surrogate |
| [[su2qc-skqd]] | hybrid quantum–classical spectroscopy with ML-assisted configuration ranking, on hardware |
| [[su2qc-jepa]] | AI world model of real-time gauge dynamics; label-free hardware error signals |
| [[SU2ZX]] | verified one-plaquette-with-matter physics core; ZX/QML circuit work |
| [[su2qc-trotter]] (with [[su2qc-paulo-code]]) | fault-tolerant (Clifford+T) circuit cost of the plaquette Trotter step |
| [[su2qc-qcadvantage]] | a path to a beyond-classical SU(2) dynamics run on today's hardware |
""")


note("Results/Result - SU2ZX v0.4.0 compiler and MPS study.md",
     {"type": "result", "package": "SU2ZX", "tags": ["result"], "date": "2026-09-06"},
     r"""
# Result - SU2ZX v0.4.0 compiler and MPS study

Pure-gauge plaquette chain, ideal simulation only ([[SU2ZX]] layer 1).

- **MPS scaling** to $N=32$ plaquettes without a full statevector; validation at $N=5, 8$ max error $2.27\times10^{-9}$
  (bond cap 64). Short-time, shallow circuits only. See [[Tensor networks (MPS and TEBD)]].
- **Compiler winners** ([[ZX-calculus circuit optimization]]): 33 families robustly Basic, 29 robustly Teleport, 21 tied,
  0 seed-sensitive; 830 of 860 compiler outputs pass the numerical gates.
- **ML compiler selector: NULL.** Prospective regret 0.0250 vs 0.0090 for the best simple baseline.
- **Symmetry-aware ordering: MIXED.** Preserves mirror symmetry and cuts depth, but the output distribution (TVD)
  improved in only 16 of 56 comparisons.
- No QPU jobs; no claim about string tension, string breaking or advantage.
""")

note("Results/Result - SU2ZX section 8 verified plaquette.md",
     {"type": "result", "package": "SU2ZX", "tags": ["result"], "date": "2026-09-07"},
     r"""
# Result - SU2ZX section 8 verified plaquette

The overnight Hermes run of 7 Sept 2026 built the [[Shared 2x2 plaquette]] by two independent routes:
spectra agree to $2.7\times10^{-15}$, stretched-string time series to $1.6\times10^{-15}$; route 2 gives $[G^a_v, H_{\rm term}] = 0.0$
exactly for every term on the 160 000-dimensional redundant space ([[Gauss's law]]). Dimensions 82 / 152, sectors
2/20/38/20/2, electric-limit degeneracies 16/16/18/16/16. One real defect (route 1 missing vertex recoupling factors)
was caught by the disagreement and fixed via `solutions/0.5.0.md`. The L12 circuits are exact (block unitary deviation
$2.7\times10^{-14}$, zero leakage) with Trotter slopes ≈ −2.1. Run halted at T+4 h: G4–G9 never ran, 0 QPU seconds.
Gates: [[su2zx gate S8-G1]], [[su2zx gate S8-G2]], [[su2zx gate S8-G3]].
""")

note("Results/Result - GI-cost campaign stalled at C0.md",
     {"type": "result", "package": "SU2ZX", "tags": ["result"], "date": "2026-09-10"},
     r"""
# Result - GI-cost campaign stalled at C0

The campaign ([[SU2ZX]] layer 3) was to measure the hardware cost of exact gauge invariance (arm GI, the L12 Strang
circuits) against Krylov playback (arm KR). After five sessions (7–10 Sept): [[su2zx gate C1]] PASS (preregistration),
[[su2zx gate C0]] PARTIAL — the twin-seed defect was found and repaired ([[Lessons that travelled]]), but the variance
band at $r=0$ (dC ratio 0.238) is an open finding, $r=1$ was too expensive to evaluate (821 320 operations, depth 506 888
on 133 qubits), and an empty-repeat bootstrap contamination remains. C2–C8 never started; hardware disabled.
In practice the follow-up work moved to [[su2qc-skqd]] (14 Sept) and [[su2qc-jepa]] (1 Oct).
""")
