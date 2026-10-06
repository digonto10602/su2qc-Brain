---
type: "package"
package: "su2qc-skqd"
status: "active"
tags: ["package"]
repo: "https://github.com/digonto10602/su2qc-skqd"
last_commit: "2026-10-06 b25f03f (PACKAGE_FULL_REPORT_20261006)"
commits: 200
aliases: ["SKQD package", "SU2QC Project 2", "skqd"]
as_of: "2026-10-06"
---
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
