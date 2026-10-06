---
type: "hub"
tags: ["hub"]
aliases: ["SU2QC brain", "Home"]
as_of: "2026-10-06"
---
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
