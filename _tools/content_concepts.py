"""Hand-written concept, method, hardware, workflow, paper and decision notes.
CONCEPTS maps note title -> (folder, type, keyword regex used to auto-link generated notes, body)."""

CONCEPTS = {}


def c(title, folder, kind, regex, body, aliases=None, as_of="2026-10-05"):
    CONCEPTS[title] = dict(folder=folder, type=kind, regex=regex, body=body.strip() + "\n", aliases=aliases or [], as_of=as_of)


P, M, H, W, R, D = "Concepts/Physics", "Concepts/Methods", "Hardware", "Workflow", "Papers", "Decisions"

# ------------------------------------------------------------------ physics
c("SU(2) lattice gauge theory", P, "concept", r"SU\(2\)|non-Abelian", r"""
**Plain words.** A gauge theory describes forces carried by fields that live *between* particles. "SU(2)" is the
symmetry group (2×2 unitary matrices with determinant 1); it is the simplest **non-Abelian** group, meaning the
force carriers themselves carry charge, as in the strong force (whose group is SU(3)). *Lattice* means space is
replaced by a grid: matter on the sites, gauge fields on the links between sites.

**Why SU2QC uses it.** It keeps the hard features of QCD (non-Abelian charges, confinement, string breaking) while
being small enough for today's quantum computers.

Used by every package: [[genesis-su2-lgt]], [[su2qc-skqd]], [[su2qc-jepa]]. Hamiltonian form: [[Kogut-Susskind Hamiltonian]].
""")

c("Kogut-Susskind Hamiltonian", P, "concept", r"Kogut|KS ", r"""
**Plain words.** The energy operator of lattice gauge theory in continuous time ([[Kogut and Susskind 1975]]). Four kinds of term:

$$H = \underbrace{\tfrac{g^2}{2}\sum_\ell E_\ell^2}_{\text{electric}} \;-\; \underbrace{\tfrac{1}{2g^2}\sum_P (W_P + W_P^\dagger)}_{\text{magnetic (plaquette)}} \;+\; \underbrace{m\sum_x (-1)^x n_x}_{\text{mass}} \;+\; \underbrace{\text{hopping}}_{\psi^\dagger U \psi}$$

$g$ is the gauge coupling; $E_\ell^2 = j_\ell(j_\ell+1)$ is the electric energy on link $\ell$; $W_P$ is the
[[Plaquette and Wilson loop]]; the mass term uses [[Staggered fermions]]; the hopping term moves a quark across a
link while updating the link field $U$.

In [[su2qc-skqd]] see [[skqd.hamiltonian]]; in [[su2qc-jepa]] see [[su2qc_jepa.physics.plaquette]] (written in units of $g_E$).
""", aliases=["Kogut–Susskind Hamiltonian", "KS Hamiltonian"])

c("Gauss's law", P, "concept", r"Gauss|gauge-invariant|gauge invariant", r"""
**Plain words.** At every site, the colour charge flowing in through the links must equal the charge sitting on the
site. Only states obeying this everywhere are physical; the rest are artefacts of the encoding.

$$G_a(x)\,|\text{phys}\rangle = 0, \qquad [G_a(x), H] = 0 .$$

Every package checks $[G_a, H]=0$ numerically (gates E1, J0, G7.2–G7.4). On hardware, Gauss's law becomes a free
error check: measured strings that violate it are rejected ([[Codewords and the Gauss-law decoder]]).
""")

c("Link truncation (j_max)", P, "concept", r"j_?max|jmax|truncat", r"""
**Plain words.** The electric field on a link can take infinitely many values (spins $j = 0, \tfrac12, 1, \dots$).
A computer must stop somewhere: $j_{\max}$ is the largest spin kept. All SU2QC packages use $j_{\max}=\tfrac12$
(each link is either empty or carries one unit of flux); $j_{\max}=1$ is used as a check of the truncation error
(152 states instead of 82 on the [[Shared 2x2 plaquette]]).
""", aliases=["j_max", "jmax"])

c("Staggered fermions", P, "concept", r"staggered|fermion|quark", r"""
**Plain words.** A way to put quarks on a lattice: one fermion component per site, with the sign of the mass
alternating between even and odd sites, $m\sum_x(-1)^x n_x$. Filled odd sites play the role of the "Dirac sea";
moving a quark creates particle–antiparticle pairs. "Two-colour" means each site holds up to two quarks (the two
SU(2) colours). Qubit mapping uses [[Jordan-Wigner mapping]].

Used in [[su2qc-skqd]] ([[skqd.fermions]]) and [[su2qc-jepa]]. Absent from [[genesis-su2-lgt]] (pure gauge).
""")

c("Plaquette and Wilson loop", P, "concept", r"plaquette|Wilson|W_P", r"""
**Plain words.** A plaquette is the smallest closed square of links. The Wilson loop $W_P = \mathrm{Tr}(U_1U_2U_3^\dagger U_4^\dagger)$
multiplies the link fields around it; it is the magnetic-energy term of the [[Kogut-Susskind Hamiltonian]] and
the term that lets flux circulate. In [[su2qc-skqd]] the plaquette term is a 30-CNOT pair rotation on 2×2.
""")

c("Intertwiner (dressed-site) basis", P, "concept", r"intertwiner|dressed|iota", r"""
**Plain words.** Instead of storing every link's full state, one stores at each site only the combination of
incoming/outgoing flux and quarks that is a colour singlet (allowed by [[Gauss's law]]). The label of which singlet
is the *intertwiner* $\iota_x$. A basis state is $|\{j_\ell\},\{n_x\},\{\iota_x\}\rangle$. This gives exactly the
physical states — 82 / 1 727 / 37 165 on 2×2 / 2×3 / 2×4.

[[su2qc-skqd]]: [[skqd.vertex]], [[skqd.basis]]. Uses [[Clebsch-Gordan coefficients]].
""")

c("Baryon-number sectors", P, "concept", r"baryon|sector", r"""
**Plain words.** The number of quarks minus the half-filling value is conserved by the Hamiltonian, so the Hilbert
space splits into independent blocks (sectors) labelled by baryon number $B$. On the [[Shared 2x2 plaquette]]:
2 / 20 / 38 / 20 / 2 states for $B = -2..2$. Each sector can be diagonalized or simulated on its own.
""")

c("String breaking", P, "concept", r"string.breaking|stretched|meson|C_string|baryonic", r"""
**Plain words.** Pull two static colour charges apart and a "string" of electric flux forms between them; its energy
grows with length. At some point it becomes cheaper to create a quark–antiquark pair from the vacuum, which snaps the
string into two mesons. Watching this happen in real time is a flagship target of quantum simulation.

[[su2qc-jepa]] learns the dynamics from the stretched-string state (observables $C_{\rm string}$, $P_{\rm meson}$, $P_{\rm baryonic}$).
""")

c("Electric basis", P, "concept", r"electric", r"""
**Plain words.** Describe each link by its electric-field quantum numbers $|j, m, n\rangle$ (Peter–Weyl states). Electric
energy is then diagonal (cheap); the magnetic plaquette term is not. All SU2QC packages build their basis this way at
$j_{\max}=\tfrac12$. Compared with alternatives in [[genesis-su2-lgt]] ([[genesis_su2.encodings]]).
""")

c("Quantum link (rishon) encoding", P, "concept", r"rishon|quantum link", r"""
**Plain words.** Replace each link by a few fermion modes ("rishons") at its two ends, with a fixed total occupation;
the link operators become products of fermion operators ([[Chandrasekharan and Wiese 1997]]). Implemented and
validated at small scale in [[genesis_su2.encodings]]; marked as the proposal candidate for the next matched-Hamiltonian study.
""", aliases=["rishon", "quantum link model"])

c("Fuzzy gauge theory", P, "concept", r"fuzzy", r"""
**Plain words.** A qubitization that replaces the continuous SU(2) group manifold by a "fuzzy" (finite-matrix)
sphere, keeping more of the group structure than a plain truncation ([[Alexandru et al. 2023 fuzzy]]). In
[[genesis-su2-lgt]] it was deliberately **not** implemented: the source definition was not fixed enough, so it is
marked BLOCKED-SOURCE-DEFINITION rather than guessed.
""")

c("Clebsch-Gordan coefficients", P, "concept", r"Clebsch|Racah", r"""
**Plain words.** The numbers that say how two spins combine into a total spin. Needed to build the colour-singlet
states at each site ([[Intertwiner (dressed-site) basis]]). Implemented in [[skqd.su2]] and [[su2qc_jepa.physics.su2]].
""")

c("Jordan-Wigner mapping", P, "concept", r"Jordan|JW", r"""
**Plain words.** A rule that turns fermion operators (which anticommute) into qubit operators by attaching a string of
$Z$ gates that tracks how many fermions sit "before" a given mode. The ordering choice matters and is frozen in each
package's conventions ([[su2qc_jepa.physics.conventions]]; skqd: "JW order = site order").
""")

c("Pauli decomposition", P, "concept", r"Pauli decomposition|canonical Pauli|Pauli coefficients|Pauli representation", r"""
**Plain words.** Writing a Hamiltonian as a weighted sum of products of Pauli matrices $I, X, Y, Z$ — the native
language of qubits. [[genesis-su2-lgt]] keeps one canonical Pauli decomposition ([[genesis_su2.pauli]]) and generates every
backend from it.
""")

# ------------------------------------------------------------------ methods
c("Sample-based Krylov quantum diagonalization (SKQD)", M, "concept", r"SKQD|sample-based|SQD", r"""
**Plain words.** A hybrid quantum–classical way to find ground energies ([[Yu et al. 2025 SKQD]]; parent method
SQD, [[Robledo-Moreno et al. 2024]]). The quantum computer prepares time-evolved states
$e^{-iHk\Delta t}|b_0\rangle$ and is measured in the configuration basis; the distinct, valid configurations form a
subspace $B$; a classical computer diagonalizes the exact $H$ inside $B$. The quantum part only *chooses* the
subspace, so the energy is always an upper bound ([[Ritz values and certified bounds]]).

**The fairness trap.** If the subspace is a large fraction of the sector, random strings find it too — then the
device contributes nothing ([[van Rossum et al. 2026]]; [[Result - 2x2 SKQD run on ibm_kingston]]).

Implemented in [[su2qc-skqd]]: [[skqd.krylov]], [[skqd.skqd]], [[skqd.controls]].
""", aliases=["SKQD", "SQD"])

c("Krylov subspace and Lanczos", M, "concept", r"Krylov|Lanczos", r"""
**Plain words.** Start from one state and repeatedly apply the Hamiltonian (or time evolution); the states you
generate span a *Krylov subspace*, which captures the low-energy physics surprisingly fast. **Lanczos** builds an
orthonormal basis of it in which $H$ becomes tridiagonal (only diagonal and next-to-diagonal entries).

[[su2qc-skqd]] uses time-evolved Krylov states to generate samples ([[skqd.krylov]]). [[su2qc-jepa]] uses Lanczos to
compress the dynamics into $K=12$ states that fit on 12 qubits ([[Krylov-chain carrier]], [[su2qc_jepa.physics.dynamics]]).
""")

c("Trotter and Strang splitting", M, "concept", r"Trotter|Strang|product formula|coarse.step", r"""
**Plain words.** $e^{-iHt}$ is hard to build as a circuit when $H$ has non-commuting parts. Split $H=\sum_\gamma H_\gamma$
and apply each part for a short time in sequence: first-order **Trotter** $\prod_\gamma e^{-iH_\gamma\Delta t}$;
second-order **Strang** uses a symmetric order (error $\propto \Delta t^3$ per step). su2qc-skqd's "coarse step" applies
each term once for time $k\Delta t$ with $\Delta t = \pi/W$ ($W$ = spectral width). [[genesis-su2-lgt]] gate G3 studies
product formulas in Qiskit.
""", aliases=["Trotter", "Strang splitting", "product formula"])

c("Ritz values and certified bounds", M, "concept", r"Ritz|Weinstein|Kato|certif", r"""
**Plain words.** Diagonalize $H$ in a subspace and the lowest eigenvalue $E_R$ (the *Ritz value*) is never below the
true ground energy $E_0$. The residual $r_H = \|(H-E_R)\psi_R\|$ measures how far the approximate eigenvector is from a
true one, which gives a guaranteed interval:

- Weinstein: some exact eigenvalue lies in $[E_R - r_H,\ E_R]$;
- Kato–Temple: the tighter $[E_R - r_H^2/(\alpha - E_R),\ E_R]$ given a lower bound $\alpha$ on the next level.

Both are the ground-state interval only if the nearest level is the ground state (the *gap assumption*). Used in [[skqd.skqd]].
""", aliases=["Weinstein bound", "Kato-Temple bound", "Ritz value"])

c("CIPSI and classical support controls", M, "concept", r"CIPSI|BFS|classical-support", r"""
**Plain words.** To show the quantum device adds value, compare its subspace with subspaces a classical computer
could choose at the *same size*: **CIPSI** (grow the subspace by adding the configurations that perturbation theory
says matter most), **BFS** (add neighbours by Hamiltonian connectivity), random sets, an exact oracle, and an ML
ranker. This comparison is su2qc-skqd's primary endpoint P1. Code: [[skqd.controls]], [[skqd.ml]].
""", aliases=["CIPSI"])

c("Codewords and the Gauss-law decoder", M, "concept", r"codeword|decod|codec", r"""
**Plain words.** Each physical state is assigned a fixed bit string (its *codeword*; 12 bits at 2×2). After
measurement, the decoder checks every string against [[Gauss's law]] and link consistency and either returns the
physical state or rejects the string. Random strings pass only ~0.15 % of the time, so the codewords act as a
built-in distance-2 error-*detection* code. Code: [[skqd.codec]].
""", aliases=["decoder", "codewords"])

c("Exact diagonalization", M, "concept", r"diagonali[sz]|eigendecomposition|dense reference", r"""
**Plain words.** Write the Hamiltonian as a matrix and compute its eigenvalues directly. Feasible for the small
systems here (82, 677, 1 727 states) and used as the "truth" every quantum or ML result is checked against:
[[skqd.exact]], [[genesis_su2.exact]], [[su2qc_jepa.physics.dynamics]].
""")

c("Tensor networks (MPS and TEBD)", M, "concept", r"MPS|TEBD|tensor.network|cuTensorNet", r"""
**Plain words.** A compressed way to store quantum states of 1D-like systems as a chain of small tensors (a
*matrix product state*, MPS); **TEBD** evolves them in time with Trotter steps. They give classical reference results
for systems too big for [[Exact diagonalization]]. Planned in [[genesis-su2-lgt]] (gate G9, `docs/TENSOR_NETWORK_IDEAS.md`), not started.
Used in [[SU2ZX]] v0.4.0 (plaquette chain to $N=32$) and in [[su2qc-qcadvantage]] ([[su2torus.mps]], quimb `CircuitMPS`), where the
**bond dimension** $\chi$ (the size of the tensors, i.e. how much entanglement the MPS can hold) was raised from 32 to 256 at
$N=48$ to find where the classical answer stops converging ([[Result - qcadvantage MPS frontier at N=48]]).
""")

c("JEPA world model", M, "concept", r"JEPA|world model", r"""
**Plain words.** A *joint-embedding predictive architecture* (JEPA) learns by predicting the **summary** (latent
embedding) of a future observation from the summary of the current one, instead of predicting the raw data. A
*world model* is a model that predicts how a system evolves given actions.

In [[su2qc-jepa]]: encoder MLP ($24\to128\to128\to16$) maps a noisy observation vector to a 16-dimensional latent; a
GRU predictor advances it under actions (time steps at given couplings); grounding heads read energy, $C_{\rm string}$,
$P_{\rm meson}$, $P_{\rm baryonic}$ and a flag rate from the latent; [[SIGReg]] prevents collapse; a semigroup check
requires two half-steps to equal one full step. Code: [[su2qc_jepa.models.jepa]], [[su2qc_jepa.models.train]].
""", aliases=["JEPA", "Gauge-JEPA"])

c("SIGReg", M, "concept", r"SIGReg|collapse", r"""
**Plain words.** A JEPA can "cheat" by mapping every input to the same latent (collapse), which makes prediction
trivial. *SIGReg* (sketched isotropic Gaussian regularization) penalises latents whose distribution is far from a
round Gaussian, keeping them spread out. Its weight is one rung of [[su2qc-jepa]]'s ablation ladder (jobs 003, 004).
The J1 gate checks the *effective rank* of the latent ($\ge 8$ of 16).
""")

c("Quantum kernel methods", M, "concept", r"[Qq]uantum.kernel|QSVR|kernel surrogate|FidelityStatevectorKernel", r"""
**Plain words.** Encode each data point as a quantum state; the overlap between two states is a similarity
("kernel") that a classical support-vector machine can use. Finite shots make each overlap noisy. In
[[genesis-su2-lgt]] the quantum-kernel surrogate became unstable at 512 shots ([[Result - genesis QML surrogate is a negative result]]).
""")

c("Leakage-safe data splits", M, "concept", r"leakage|held.out|splits", r"""
**Plain words.** When training on physics data, test examples must come from coupling values never seen in training
(split by parameters, not by rows), otherwise the model looks better than it is. [[skqd.ml]] splits by
$(\lambda, \text{lattice})$; [[jepa gate J0]] checks that no held-out trajectory appears in training.
""")

c("Krylov-chain carrier", M, "concept", r"Krylov.chain|chain carrier|unary|one-hot", r"""
**Plain words.** [[su2qc-jepa]]'s trick to put the plaquette dynamics on hardware cheaply. [[Krylov subspace and Lanczos|Lanczos]]
compresses the relevant dynamics into $K=12$ basis states with a tridiagonal Hamiltonian; each basis state is
encoded as one excited qubit in a line of 12 ($|0\dots010\dots0\rangle$). Nearest-neighbour hops then implement the
dynamics: 22 CZ per Trotter step, 34 / 56 / 100 / 188 CZ for $r = 1, 2, 4, 8$ steps — a real depth ladder. States with
zero or two excitations are flagged as errors. Code: [[su2qc_jepa.physics.chain]]; qubit line chosen by [[su2qc_jepa.twin.layout]].
""", aliases=["KC carrier", "chain carrier"])

# ------------------------------------------------------------------ noise / hardware physics
c("Clean-shot fraction", M, "concept", r"clean.shot|clean fraction|clean_fraction|f_clean|yield", r"""
**Plain words.** The probability that one run (shot) of a circuit happens with no error at all, $f$. SKQD cost scales
like $1/f$ shots (worse, $1/f^2$, at very small $f$). su2qc-skqd's go/no-go bar is $f\ge0.1$. Estimated from hardware by
the reference-string statistic or a mixture estimator; the CF_traj work showed the hit statistic actually tracks the
*ideal-sample* fraction ([[Result - CF_traj clean-fraction re-ruling]]). Code: [[skqd.device_req]], [[skqd.idle]].
""", aliases=["clean fraction", "f"])

c("Dynamical decoupling", M, "concept", r"\bDD\b|decoupling|XY4", r"""
**Plain words.** While a qubit waits idle it slowly loses its phase. Inserting carefully timed pulse sequences (e.g.
**XY4**: X, Y, X, Y) into the idle windows cancels much of that drift. In [[su2qc-skqd]], client-side XY4 raised the
clean fraction 2.8× on ibm_kingston on 2 Oct, but the gain did not replicate on 6 Oct ([[Result - client-side XY4 gain did not replicate]]).
""", aliases=["DD", "XY4"])

c("Decoherence (T1 and T2)", M, "concept", r"\bT1\b|\bT2|Ramsey|idle|dephas|relaxation", r"""
**Plain words.** $T_1$: how long a qubit keeps its energy (an excited $|1\rangle$ decays to $|0\rangle$). $T_2$: how long it keeps
its phase. $T_2^\*$ (measured by a Ramsey experiment) includes slow drifts; $T_2^{\rm echo}$ removes them. Long, serial
circuits are limited by idle time, which is why the 2×3 SKQD circuit fails on superconducting devices. Code:
[[skqd.idle]], [[skqd.coherence]].
""", aliases=["T1", "T2", "T2*"])

c("Readout error and confusion matrix", M, "concept", r"readout|confusion", r"""
**Plain words.** Measuring a qubit sometimes returns the wrong bit. The *confusion matrix* records how often each
prepared value is read as each outcome; it is measured with simple preparation circuits and used to correct counts.
In the ibm_kingston run the smallest diagonal entry was 0.9417. Code: [[skqd.hardware]].
""")

c("Noise models and digital twin", M, "concept", r"Aer|twin|noise.model|NoiseModel|emulat", r"""
**Plain words.** A *digital twin* is a simulator configured with a real device's calibration (gate errors, $T_1$, $T_2$,
readout) so you can rehearse a hardware run. Qiskit **Aer** is the simulator used. Warning learnt in su2qc-skqd: the Aer
model at the echo $T_2$ was 5.1× too optimistic for the clean fraction. Code: [[skqd.noise]], [[su2qc_jepa.twin.noise]], [[su2qc_jepa.twin.run]].
""", aliases=["twin", "Aer"])

c("Transpilation and CZ count", M, "concept", r"transpil|\bCZ\b|ECR|CNOT|routed", r"""
**Plain words.** *Transpiling* rewrites a circuit into the gates and qubit connections a specific device supports.
Two-qubit gates (CZ on IBM Heron) are the main error source, so the CZ count after routing is the key cost. skqd's
original budget (≤ 250 CZ per coarse step at 2×2) failed (gates L3, S2) and was amended to a clean-fraction criterion.
""", aliases=["CZ count"])

# ------------------------------------------------------------------ workflow
c("Gate-and-evidence discipline", W, "infra", r"[Gg]ate [A-Z]\d|validation/|ledger|pass/fail", r"""
**Plain words.** A **gate** is a scripted pass/fail checkpoint with numeric thresholds set in advance. Only gate
scripts decide PASS/FAIL; every number in a report is copied from the gate's JSON output, never typed by hand.
Used by all packages: genesis (G0–G12), skqd (E, S, L, H, P, M series), jepa (J0–J4). See [[Gates index]].
""", aliases=["gates"])

c("Graphify code graph", W, "infra", r"[Gg]raphify", r"""
**Plain words.** Graphify (`pip install graphifyy`) parses a repository locally (no AI calls) into a graph of files,
classes, functions and imports. Coding agents query it (`graphify explain`, `graphify affected`) before editing, so
they never change code they have not mapped. Rebuilt every session and freshness-checked in CI in all three packages.
su2qc-jepa's graph: 842 nodes, 1 615 edges at bootstrap. Code: [[su2qc_jepa.repo.graph]].
""", aliases=["Graphify", "graphify"])

c("Numbered artifacts", W, "infra", r"numbered|new_artifact|INDEX\.md", r"""
**Plain words.** Every plan, prompt, report, decision and figure is a numbered, append-only file in its own folder
(`prompts/004_...md`), created by a script that also updates the folder's `INDEX.md`. Nothing is overwritten, so any
result can be traced to the prompt that produced it. Formalised in [[Decision - jepa 001 numbered artifacts and Graphify]];
code [[su2qc_jepa.repo.artifacts]]. su2qc-skqd numbers prompts (00–29) the same way.
""")

c("Agent routing (planner, executor, reviewer, runner, scribe)", W, "infra", r"planner|executor|reviewer|runner-sonnet|scribe", r"""
**Plain words.** Different AI models get different jobs, matched to cost and difficulty (su2qc-skqd `prompts/ROUTING.md`):

| role | model | effort | job |
|---|---|---|---|
| planner-fable | Claude Fable 5.1 | high (max for blocked gates) | physics decisions, writes the next numbered prompt |
| executor-opus | Claude Opus 5.5 | high | implements the prompt |
| reviewer-opus | Opus | medium | audits JSON ↔ report ↔ code before a push |
| runner-sonnet | Sonnet | low | runs gates and tests, never edits source |
| scribe-haiku | Haiku | low | updates status tables, never changes numbers |

Fallbacks when quotas run out: NIM open models for running, Codex for executing; the planner has no substitute.
""", aliases=["agent routing", "planner-fable"])

c("Perlmutter job queue", W, "infra", r"Perlmutter|scrontab|Slurm|sbatch|worker", r"""
**Plain words.** A *pull-based* queue: the laptop writes a numbered job file (`jobs/NNN_*.yaml`) and pushes it to GitHub;
a `scrontab` (Slurm's cron) worker on [[NERSC Perlmutter]] pulls it, runs it with Slurm, resubmits after timeouts or
node failures, and pushes results to a `results` branch. Installation merges with, never overwrites, your other two
scrontab entries. Code: [[su2qc_jepa.jobs]]; skqd uses CI tokens and `.sbatch` files ([[skqd.hpc]]).
""")

c("Laptop admission-controlled runner", W, "infra", r"admission|oom_score|localrun|[Rr]esource-aware", r"""
**Plain words.** Every computation goes through `scripts/run.py`. A job runs on the laptop only if there is room
(16 GB RAM and 2 CPUs always left for other sessions, one su2qc job at a time), with hard caps and
`oom_score_adj = 1000` so the kernel kills *this* job first under memory pressure. Too big → queued to Perlmutter.
Code: [[su2qc_jepa.localrun]], [[su2qc_jepa.compute]]. Decision: [[Decision - jepa 004 laptop and Perlmutter only]].
""")

c("Preregistration", W, "infra", r"prereg", r"""
**Plain words.** Writing down the analysis, thresholds and go/no-go rules *before* the data exist (here, before a
QPU session), so the result cannot be tuned after the fact. su2qc-skqd preregisters every hardware session
(`reports/H0_*_prereg_*.md`); su2qc-jepa freezes its gate thresholds by 16 Oct 2026 (`docs/PREREGISTRATION.md`).
""")

c("Qiskit", W, "tool", r"[Qq]iskit|SamplerV2", r"""
IBM's open-source quantum SDK: circuits, transpiler, Aer simulator, and Runtime primitives (SamplerV2) for real
devices. Used by all three packages: [[skqd.circuits_qiskit]], [[su2qc_jepa.hardware.ibm]], [[genesis_su2.backends.qiskit_backend]].
""")

c("CUDA-Q", W, "tool", r"CUDA-Q|cudaq", r"""
NVIDIA's quantum programming platform; runs circuits on GPU statevector simulators. Used in [[skqd.circuits_cudaq]]
(gate L5 PASS) and [[genesis_su2.backends.cudaq_backend]] (skipped in G4 for lack of an install). Docker image
`nvcr.io/nvidia/quantum/cuda-quantum:cu13-0.15.1` works on your desktop.
""")

# ------------------------------------------------------------------ hardware
c("ibm_kingston", H, "hardware", r"kingston", r"""
IBM Heron r2 processor. Site of [[su2qc-skqd]]'s successful 2×2 campaign on 2026-10-02: $T_2^\*$ pilot
([[skqd gate H0_kpilot]], FAIL on the $f\ge0.1$ go rule), DD A/B test ([[skqd gate H0_ddtest]] PASS), full run
([[skqd gate H0_2x2]] PASS). See [[Result - 2x2 SKQD run on ibm_kingston]]. On 2026-10-06: the DD replication
([[skqd gate H0_ddrep]]; [[Result - client-side XY4 gain did not replicate]]) and the 2×3 pilot ([[skqd gate K1_2x3_fpilot]];
[[Result - 2x3 on ibm_kingston is a measured NO-GO]]).
""")

c("ibm_fez", H, "hardware", r"\bfez\b|FakeFez|ibm_fez", r"""
IBM Heron r2 processor. [[su2qc-skqd]]'s first hardware target (Sept 2026): rehearsal on the FakeFez snapshot, live
re-prediction ([[skqd gate H0P_ibm_fez]]), then the canary failed ([[skqd gate H0_canary]]) and a diagnostic session
([[skqd gate H0_diag]]) tested idle-relaxation vs sampler-option hypotheses. The campaign moved to [[ibm_kingston]].
""")

c("ibm_marrakesh", H, "hardware", r"marrakesh", r"""
IBM Heron processor surveyed during [[su2qc-skqd]]'s patch selection (22 Sept 2026; reports `H0_patch_select_*marrakesh*`). Not used for a run.
""")

c("IBM Quantum Open Plan", H, "hardware", r"Open Plan", r"""
IBM's free tier: about 10 QPU-minutes per rolling 28-day window. [[su2qc-jepa]]'s hardware campaign is designed for
≈ 8–13 QPU-minutes across two windows, preceded by a 1.5-minute pilot. Heron r3 devices are Premium/Flex only.
""")

c("Quantinuum H-series", H, "hardware", r"Quantinuum|Helios|H2-2|H1-1|HQC|pytket", r"""
Trapped-ion processors (H1, H2, Helios) with all-to-all connectivity and long coherence; billed in HQC credits. The
2×3 SKQD circuits are compiled to the native gate set $\{R_z, \text{PhasedX}, \text{ZZPhase}\}$ and verified
([[skqd gate Q0P_2x3]] PASS); emulator and pilot not run (no Nexus login, no budget). Code: [[skqd.quantinuum_native]].
""")

c("IonQ Forte", H, "hardware", r"IonQ|Forte|Braket", r"""
Trapped-ion processor available through Amazon Braket ($0.30 per task + $0.08 per shot). [[su2qc-skqd]]'s feasibility
check from published specifications: 2×3 no, 2×2 yes. [[su2qc-jepa]] made IonQ optional (100 tasks × 1 000 shots ≈ $8k).
""")

c("NERSC Perlmutter", H, "hardware", r"Perlmutter|A100|NERSC", r"""
NERSC supercomputer with NVIDIA A100 GPU nodes. All heavy SU2QC work goes here through the [[Perlmutter job queue]]
(su2qc-jepa) or CI tokens (su2qc-skqd). su2qc-jepa's A100 smoke test passed (reports/008).
""")

c("Laptop (Dell G7)", H, "hardware", r"GTX 1060|i7-8750H", r"""
64 GB RAM, 6-core i7-8750H, GTX 1060 Max-Q (not used by su2qc-jepa: PyTorch has no kernels for it). Shared with
other Claude sessions, hence the [[Laptop admission-controlled runner]]. su2qc-skqd's laptop gates (L2–L5) run here.
""")

# ------------------------------------------------------------------ papers
c("Kavaki and Lewis 2024", R, "paper", r"Kavaki", r"""
*From square plaquettes to triamond lattices for SU(2) gauge theory*, Communications Physics 7, 208 (2024).
Eq. (1) is the two-qubit, two-plaquette Hamiltonian of [[genesis-su2-lgt]]; it already ran on IBM hardware.
Reference code: github.com/randylewis/SelfMitigatedQITE.
""")
c("Kogut and Susskind 1975", R, "paper", r"Kogut and Susskind", r"""
*Hamiltonian formulation of Wilson's lattice gauge theories*, Phys. Rev. D 11, 395 (1975). Origin of the
[[Kogut-Susskind Hamiltonian]]. Cited by [[genesis-su2-lgt]].
""")
c("Chandrasekharan and Wiese 1997", R, "paper", r"Chandrasekharan", r"""
*Quantum link models*, arXiv:hep-lat/9609042. Basis of the [[Quantum link (rishon) encoding]]. Cited by [[genesis-su2-lgt]].
""")
c("Alexandru et al. 2019 digitization", R, "paper", r"1906\.11213", r"""
*Gluon field digitization for quantum computers*, arXiv:1906.11213. Cited by [[genesis-su2-lgt]]; related:
*Qubitization strategies for bosonic field theories*, arXiv:2209.00098.
""")
c("Alexandru et al. 2023 fuzzy", R, "paper", r"2308\.05253", r"""
*Fuzzy gauge theory for quantum computers*, arXiv:2308.05253. Source of [[Fuzzy gauge theory]]. Cited by [[genesis-su2-lgt]].
""")
c("Yu et al. 2025 SKQD", R, "paper", r"2501\.09702", r"""
*Quantum-centric algorithm for sample-based Krylov diagonalization*, arXiv:2501.09702. The method behind
[[su2qc-skqd]] ([[Sample-based Krylov quantum diagonalization (SKQD)]]).
""")
c("Robledo-Moreno et al. 2024", R, "paper", r"2405\.05068", r"""
*Chemistry beyond exact solutions on a quantum-centric supercomputer*, arXiv:2405.05068. Introduced sample-based
quantum diagonalization (SQD) with configuration recovery. Cited by [[su2qc-skqd]].
""")
c("Rosanowski et al. 2025", R, "paper", r"2510\.26951", r"""
Rosanowski, Eisinger, Funcke, Poschinger, Schmidt-Kaler, arXiv:2510.26951 — sample-based methods for the Schwinger
model on trapped-ion and superconducting processors. Closest prior gauge-theory SKQD work cited by [[su2qc-skqd]].
""")
c("van Rossum et al. 2026", R, "paper", r"2608\.11569", r"""
van Rossum, Cohn, Shrapnel, Gupta, arXiv:2608.11569 — critique of SQD benchmarking: random configurations can rebuild
accurate subspaces, so fair comparisons must control subspace size. Central to [[su2qc-skqd]]'s honesty about the 2×2
result (with Vaquero-Sabater et al., arXiv:2605.23697).
""")

# ------------------------------------------------------------------ decisions
c("Decision - jepa 000 frozen conventions", D, "decision", r"decisions/000", r"""
[[su2qc-jepa]] decisions/000 (planner, 2026-10-01): conventions and coupling points are frozen — geometry, loop
orientation, staggered phases ($\prod_\square \eta = -1$), Jordan–Wigner order, and P-A $= (1, 3/8, 0.25, -0.0625)$ at $g_E=2$
(the v0.6.1 ruling). Code: [[su2qc_jepa.physics.conventions]].
""")
c("Decision - jepa 001 numbered artifacts and Graphify", D, "decision", r"decisions/001", r"""
[[su2qc-jepa]] decisions/001 (2026-10-02): [[Numbered artifacts]] for everything produced, and the [[Graphify code graph]]
checked at session start, rebuilt at session end, and verified fresh in CI.
""")
c("Decision - jepa 004 laptop and Perlmutter only", D, "decision", r"decisions/004", r"""
[[su2qc-jepa]] decisions/004 (2026-10-02, supersedes 002 and 003): compute is the laptop and Perlmutter only (not the
RTX 3070 desktop); an admission-controlled laptop runner and self-healing Perlmutter jobs.
See [[Laptop admission-controlled runner]], [[Perlmutter job queue]].
""")
c("Decision - jepa 005 J1 energy threshold", D, "decision", r"decisions/005", r"""
[[su2qc-jepa]] decisions/005 (Digonto, 2026-10-05, option C of reports/010): J1 energy-grounding threshold
$R^2 \ge 0.887 = 0.97 \times$ the measured information ceiling 0.9145. See [[Result - J1 energy information ceiling]].
""")


c("ZX-calculus circuit optimization", M, "concept", r"ZX|PyZX|[Tt]eleport|full_reduce|compiler", r"""
**Plain words.** The ZX-calculus rewrites a quantum circuit as a graph of simple "spiders" and simplifies it with a
small set of exact rules; **PyZX** is the standard library. "Basic" and "Teleport" are two PyZX simplification
strategies. Used in [[SU2ZX]] v0.4.0 to choose the cheapest compiled circuit for each case, and in your SU(2) circuit
lab (PyZX `basic_optimization` cut two Strang repetitions from 118 to 94 ECR gates; `full_reduce` made it worse, 180).
""", aliases=["ZX calculus", "PyZX"])

c("L12 encoding", M, "concept", r"L12|l12", r"""
**Plain words.** [[SU2ZX]]'s 12-qubit encoding of the [[Shared 2x2 plaquette]] (3 qubits per vertex), with
exact gauge-invariant Strang circuits built from block unitaries. Exact and leak-free, but about 2 156 two-qubit gates
per Strang step after compilation — far too deep for current hardware, which is why the later packages built cheaper
carriers ([[Krylov-chain carrier]], skqd codewords). Code: [[su2qc.encodings.l12]], [[su2qc.circuits.strang_l12]].
""", aliases=["L12"])


# ------------------------------------------------------------------ added 2026-10-06 (su2qc-qcadvantage, su2qc-trotter)
c("One-qubit-per-plaquette SU(2) model", P, "concept", r"one.qubit.per.plaquette|honeycomb|plaquette graph|abelian twin", r"""
**Plain words.** The cheapest known exactly gauge-invariant form of pure SU(2) gauge theory in 2+1 dimensions
([[Ciavarella et al. 2026]]): keep only $j=0$ and $j=\tfrac12$ on every link of a triangular lattice and use
[[Gauss's law]] to eliminate the links, so that each **plaquette** becomes one qubit. The plaquettes form a honeycomb
graph; on a torus (periodic boundaries) there are $N$ plaquette qubits:

$$H=\frac{3g^2}{16}\sum_{\langle pq\rangle}(1-Z_pZ_q)\;-\;\frac1{g^2}\sum_p\Big[\prod_{q\in nb(p)}c(n_q)\Big]X_p,\qquad c(0)=1,\ c(1)=\tfrac12 .$$

The first sum is the electric energy (a cost on every bond between plaquettes in different states); the second flips a
plaquette with an amplitude that depends on its neighbours (this neighbour dependence is what makes it non-Abelian).
Setting $c\equiv1$ gives the **abelian twin**, the transverse-field Ising model, used as a control.
Code: [[su2torus.lattice]], [[su2torus.hamiltonian]] in [[su2qc-qcadvantage]].
""", aliases=["minimal SU(2) truncation", "abelian twin", "honeycomb plaquette torus"], as_of="2026-10-06")

c("Thermalization and canonical typicality", P, "concept", r"thermali[sz]|typicality|thermal anchor|decohered", r"""
**Plain words.** A closed quantum system started far from equilibrium usually ends up looking *thermal*: local
observables settle to the values of a thermal state $e^{-\beta H}/Z$ whose inverse temperature $\beta$ is fixed by the
starting energy. The **thermal anchor** is that predicted late-time value; the **decohered value** is the
infinite-temperature ($\beta=0$) value, i.e. what a fully scrambled or fully noise-destroyed state would give.
**Canonical typicality** computes thermal values without diagonalizing $H$: apply $e^{-\beta H/2}$ to a few random
vectors and average (statistical error shrinks with the number of vectors).

In [[su2qc-qcadvantage]] ([[su2torus.thermal]]) this is how an observable is judged useful: if the anchor sits close to
the decohered value, hardware noise and real physics cannot be told apart. See
[[Result - qcadvantage thermalization and the beta=0 states]].
""", aliases=["thermal anchor", "decohered value", "typicality"], as_of="2026-10-06")

c("Zero-noise extrapolation", M, "concept", r"\bZNE\b|zero.noise|folding", r"""
**Plain words.** Error mitigation (not correction): run the same circuit with the noise deliberately amplified, for
example by replacing each gate $G$ with $G G^\dagger G$ (**gate folding**, noise factor 3) or $G(G^\dagger G)^2$
(factor 5), then fit the measured value against the noise factor and extrapolate back to factor 0.
In [[su2qc-qcadvantage]] ([[su2torus.noise]]) folding at factors 1, 3, 5 cut the error of $\langle H_E\rangle$ by
5.8–15.5× in 4 of 4 tested configurations at $N=12$ ([[Result - qcadvantage noise mitigation at N=12]]).
""", aliases=["ZNE", "gate folding"], as_of="2026-10-06")

c("Loschmidt echo", M, "concept", r"Loschmidt|forward.backward echo|cross.technique echo", r"""
**Plain words.** Run a circuit forward and then its exact inverse. Without noise you return to the starting state
with probability 1; the measured return probability therefore estimates the *global fidelity* $F$ of the noisy run.
[[su2qc-qcadvantage]] uses it to check the noise model (echo $F$ within 3–13 % of the predicted $\prod(1-\epsilon)$), and
found that rescaling local observables by the global $F$ over-corrects them. [[su2qc-trotter]] uses a cross-technique
echo (one circuit forward, the other backward) to show the lean and reference circuits are the same unitary.
""", aliases=["echo fidelity", "forward-backward echo"], as_of="2026-10-06")

c("Clifford+T and T-count", M, "concept", r"Clifford\+T|T.count|T/T|gridsynth", r"""
**Plain words.** Fault-tolerant quantum computers will run only a fixed, finite gate set: the **Clifford** gates
(H, S, CNOT — cheap on error-corrected hardware) plus the **T gate** (a $\pi/4$ phase — expensive, because it needs
*magic-state distillation*). Arbitrary rotations must be approximated by long H/S/T sequences (**synthesis**, e.g.
gridsynth) to a chosen error $\epsilon$. The **T-count** (number of T and T$^\dagger$ gates) is the standard cost metric.
[[su2qc-trotter]] counts it for one plaquette Trotter step: 1162 T (Paulo's 34-qubit circuit) versus 424 T (the lean
22-qubit design) at $\epsilon=10^{-6}$ per rotation ([[Result - lean 22-qubit plaquette Trotter step]]).
""", aliases=["T-count", "Clifford+T", "magic state"], as_of="2026-10-06")

c("Ciavarella et al. 2026", R, "paper", r"2608\.28752|Ciavarella", r"""
Ciavarella, de Putter, Younis and Rrapaj, arXiv:2608.28752 (as cited in `su2qc-qcadvantage/README.md` and
`docs/idea.md`). The one-qubit-per-plaquette minimal SU(2) truncation, run on 156 qubits of IBM `ibm_boston` (August 2026) as a
string-breaking experiment. The model behind [[su2qc-qcadvantage]]; see [[One-qubit-per-plaquette SU(2) model]].
""", as_of="2026-10-06")
