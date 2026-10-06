---
type: "package"
package: "su2qc-qcadvantage"
status: "paused"
tags: ["package"]
repo: "https://github.com/digonto10602/su2qc-qcadvantage"
branch: "claude/modest-mayer-kh4s6b"
last_commit: "2026-10-06"
commits: 29
aliases: ["SU(2) torus frontier run", "su2torus", "qcadvantage"]
as_of: "2026-10-06"
---
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
