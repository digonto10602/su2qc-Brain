---
type: "package"
package: "su2qc-trotter"
status: "done"
tags: ["package"]
repo: "https://github.com/digonto10602/su2qc-trotter"
last_commit: "2026-09-27"
commits: 79
aliases: ["su2trotter", "trotter-ci", "lean plaquette circuit"]
as_of: "2026-10-06"
---
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
