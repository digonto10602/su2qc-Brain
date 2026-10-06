---
type: "index"
tags: ["index"]
generated: True
as_of: "2026-10-06"
---
# Modules index

Every Python module (generated from docstrings and imports).

## [[su2qc-skqd]]

- [[skqd.basis]] — Gauge-invariant configuration basis  |b> = |{j_l}, {n_x}, {iota_x}>  of the
dressed-site construction (Step 2 of the SKQD manual), with bary
- [[skqd.circuits_cudaq]] — CUDA-Q translation of the IR circuits (circuits_ir
- [[skqd.circuits_ir]] — Backend-independent circuit description ("IR") of the support-generating
circuits, built from exact local block unitaries of the Hamiltonian
- [[skqd.circuits_qiskit]] — Qiskit translation of the IR circuits (circuits_ir
- [[skqd.codec]] — Hardware codewords and the per-shot decoder (Steps 2
- [[skqd.coherence]] — Coherence requirement of a compiled circuit: what T2 a device must have to run it
- [[skqd.controls]] — Classical-support controls at prescribed support size (Step 6 of the SKQD manual)
- [[skqd.device_req]] — Device-requirement algebra for the amended budget criterion
- [[skqd.exact]] — Exact sector references (Step 1
- [[skqd.fermions]] — Two-colour staggered-fermion site
- [[skqd.fullspace]] — Redundant-basis ("projector") construction of the 2 x 2 model — the second,
independent route of gate E1 (Step 1
- [[skqd.hamiltonian]] — Dressed-site Hamiltonian builder — Step 3 / Algorithm 2 of the SKQD manual
- [[skqd.hardware]] — Hardware-session helpers (manual Step 9
- [[skqd.hpc]] — CI / Slurm / GPU-telemetry helpers shared by the gate scripts that may run on Perlmutter
- [[skqd.idle]] — Idle-time relaxation in the clean-shot fraction f
- [[skqd.krylov]] — Support-generating states (Step 4 of the SKQD manual), emulated exactly in
the gauge-invariant basis
- [[skqd.lattice]] — Open 2 x Lx ladder (Ly = 2 rows), the geometry of the SKQD manual (Step 1
- [[skqd.ml]] — Minimal gauge-invariant importance model (Step 7
- [[skqd.noise]] — Device-proxy noise model on bit strings (Step 8
- [[skqd.quantinuum_native]] — The Quantinuum native gate set {Rz, PhasedX, ZZPhase} for the IR circuits (prompts/26, gate Q0P_2x3)
- [[skqd.reference_sim]] — numpy reference for the circuit layer: codeword embedding of the gauge-invariant
basis into the 2^n computational space, exact local block u
- [[skqd.report]] — Gate-result bookkeeping: every gate script records its criteria and the numbers
it actually computed in validation/<GATE>
- [[skqd.skqd]] — HPC post-processing of a support: projected diagonalization, certification
and support-quality metrics (Step 5 of the SKQD manual)
- [[skqd.sparse_sim]] — Exact SPARSE statevector simulation of the IR circuits and of transpiled circuits
- [[skqd.su2]] — SU(2) building blocks: spin matrices, Clebsch-Gordan coefficients, and the
truncated electric-basis link operators
- [[skqd.vertex]] — Local singlet (intertwiner) tensors of one dressed vertex — Algorithm 1 of the
SKQD manual (VERTEXTENSORS)

## [[su2qc-jepa]]

- [[su2qc_jepa.compute]] — Device selection and the measured unit costs used by the laptop runner (su2qc_jepa
- [[su2qc_jepa.data.records]] — Measurement records and the observation estimator shared by all three sources
- [[su2qc_jepa.data.trajectories]] — Trajectory generator: exact dynamics + emulated finite-shot observations + split manifest
- [[su2qc_jepa.gates.j0_data]] — Gate J0 - data integrity: physics fingerprints, two routes, estimator bias, twin seeds, Krylov window, splits
- [[su2qc_jepa.gates.j1_training]] — Gate J1 - training health from history
- [[su2qc_jepa.gates.j2_forecast]] — Gate J2 - forecasting on held-out couplings versus baselines (from runs/<name>/forecast_eval
- [[su2qc_jepa.gates.j3_hardware]] — Gate J3 - label-free hardware error signals (twin rehearsal or real hardware)
- [[su2qc_jepa.gates.ledger]] — Gate results and the ledger
- [[su2qc_jepa.hardware.ibm]] — IBM Quantum submission path with a dry-run-first, budget-guarded discipline
- [[su2qc_jepa.jobs]] — Job requests for the Perlmutter worker — decisions/004 (queue introduced in decisions/003)
- [[su2qc_jepa.localrun]] — Resource-aware, self-healing execution on the laptop (decisions/004)
- [[su2qc_jepa.models.jepa]] — Gauge-JEPA-P v2: classical encoder + action-conditioned predictor + SIGReg + grounding heads
- [[su2qc_jepa.models.train]] — Training loop, probes, forecasting evaluation and baselines for Gauge-JEPA-P v2
- [[su2qc_jepa.physics.chain]] — The Krylov-chain hardware carrier (one-hot / unary encoding of the Lanczos basis)
- [[su2qc_jepa.physics.conventions]] — Frozen conventions for the hard-core SU(2) Kogut-Susskind plaquette with
two-colour staggered fermions
- [[su2qc_jepa.physics.dynamics]] — Exact real-time evolution and Lanczos/Krylov compression
- [[su2qc_jepa.physics.observables]] — Observables of the plaquette in the gauge-invariant configuration basis
- [[su2qc_jepa.physics.plaquette]] — Hard-core SU(2) Kogut-Susskind plaquette with two-colour staggered fermions
- [[su2qc_jepa.physics.su2]] — SU(2) building blocks: spin matrices and Clebsch-Gordan coefficients
- [[su2qc_jepa.repo.artifacts]] — Numbered artifacts: plans, prompts, reports, decisions and figures
- [[su2qc_jepa.repo.graph]] — Helpers around the Graphify code graph (graphify-out/graph
- [[su2qc_jepa.twin.layout]] — Choose the physical line of K qubits for the chain carrier from calibration data
- [[su2qc_jepa.twin.noise]] — Noise models for the Aer twin
- [[su2qc_jepa.twin.run]] — Twin runner with reproducible, *independent* seeds

## [[genesis-su2-lgt]]

- [[genesis_su2.backends.cudaq_backend]] — CUDA-Q objects generated from the same canonical Pauli coefficients
- [[genesis_su2.backends.ibm_runtime]] — Explicitly guarded IBM Quantum Runtime V2 submission path
- [[genesis_su2.backends.qiskit_backend]] — Qiskit simulator and IBM Runtime preparation from canonical Pauli terms
- [[genesis_su2.cli]] — Small command-line interface for reproducible reference calculations
- [[genesis_su2.config]] — Small deterministic configuration schema for starter experiments
- [[genesis_su2.encodings]] — Small, dense SU(2) link-encoding references for G7 validation
- [[genesis_su2.exact]] — Dense reference calculations used to validate all accelerated backends
- [[genesis_su2.pauli]] — Canonical Pauli representation of the two-plaquette SU(2) benchmark
- [[genesis_su2.qml.energy_surrogate]] — Quantum-kernel surrogate for the ground-state energy curve
- [[genesis_su2.su2]] — Fundamental SU(2) generators and link matrices for convention tests

## [[SU2ZX]]

- [[su2qc.circuits.export_l12]] — Write circuits/resources_logical
- [[su2qc.circuits.strang_l12]] — Exact gauge-invariant block unitaries and Strang circuits for L12 (G3)
- [[su2qc.circuits.synth_l12]] — Structured synthesis of the L12 block unitaries
- [[su2qc.compile.route]] — Phase 4: route logical L12 circuits to a Heron-class target and verify
- [[su2qc.compile.run_g4]] — Phase 4 production: compile, route, PyZX comparison, twin run, decision inputs
- [[su2qc.conventions]] — FROZEN conventions for the SU(2) single-plaquette patch with dynamical matter
- [[su2qc.dynamics.engine]] — Exact-dynamics engine for the 82-state (jmax=0
- [[su2qc.dynamics.run_g2]] — Run the full G2 production sequence and print a summary (OPS lane)
- [[su2qc.dynamics.scan]] — Mass scan / resonance finder, truncation comparison, Trotter-window selector
- [[su2qc.encodings.l12]] — The 12-qubit, three-bits-per-vertex L12 encoding
- [[su2qc.ham.compare]] — Verifier-owned comparison of the two independent Hamiltonian routes (G1)
- [[su2qc.ham.limits]] — Verifier-owned limit tests for gate G1
- [[su2qc.ham.route_gausskernel]] — Route 2: redundant Kogut-Susskind space followed by Gauss-law projection
- [[su2qc.ham.route_spinnet]] — Route 1: analytic spin-network / dressed-site Hamiltonian for SU(2) single plaquette
with dynamical two-color staggered fermions
- [[su2qc.replicate]] — Minimal replication manifest helper for the campaign
- [[su2qc.twin.twin]] — Noise-model twin: FakeTorino (or a real backend's properties) via
AerSimulator
- [[su2zx.compiler_study]] — Diverse, exact, target-aware compiler study for SU2ZX v0
- [[su2zx.core]] — Physics, circuits, and observables for the j_max=1/2 SU(2) plaquette chain
- [[su2zx.paths]] — Small path guard shared by command-line modules
- [[su2zx.qpu]] — Dry-run-first IBM experiment
- [[su2zx.qpu_analysis]] — Analyze raw and M3-mitigated IBM data against the ideal Trotter circuit
- [[su2zx.report]] — Generate the v0
- [[su2zx.robust_study]] — Fixed-target routing robustness and prospective pairwise compiler selection
- [[su2zx.scaling_study]] — Symmetry physics and direct MPS observables without dense-state scaling
- [[su2zx.study]] — Generate exact/Trotter observables, distributions, and physics plots
- [[su2zx.tn_study]] — CPU matrix-product-state validation for SU2ZX v0

## [[su2qc-trotter]]

- [[su2trotter.analysis]] — Bright-pair structure of B and tools to check a forward basis transform C
- [[su2trotter.baseline]] — Baseline: the 34-qubit promise-aware circuit of optimized_plaquette_dontcare_lowT
- [[su2trotter.circuit]] — Minimal circuit IR used to build the plaquette circuits
- [[su2trotter.compare]] — Gate-level comparison data for the two techniques (reference 34-qubit, lean 22-qubit)
- [[su2trotter.cudaq_backend]] — CUDA-Q backend: build kernels from the gate IR, count resources, simulate
- [[su2trotter.draw]] — Circuit drawings for the report (Qiskit matplotlib drawer, vector PDF)
- [[su2trotter.lean]] — Lean promise-aware plaquette circuit (this work)
- [[su2trotter.optimize]] — Light, provably-safe peephole optimisation for Clifford+T(+rz) gate lists
- [[su2trotter.physics]] — Exact reference physics for one SU(2) plaquette at jmax = 1/2
- [[su2trotter.pipeline]] — Build -> verify -> optimise -> synthesise -> CUDA-Q resource count -> re-verify
- [[su2trotter.plotstyle]] — Shared finishing step for all comparison plots
- [[su2trotter.sim]] — Exact sparse state-vector simulator for :class:`Circuit` gate lists
- [[su2trotter.synth]] — Clifford+T synthesis of arbitrary-angle rz gates (Ross-Selinger gridsynth via pygridsynth)
- [[su2trotter.trotter]] — Full single-plaquette Trotter step: electric phases + magnetic plaquette circuit

## [[su2qc-qcadvantage]]

- [[su2torus.exact]] — Exact (state-vector) tools
- [[su2torus.hamiltonian]] — Minimal (one qubit per plaquette) SU(2) Hamiltonian, arXiv:2608
- [[su2torus.lattice]] — Plaquette graph of the triangular lattice (= honeycomb graph)
- [[su2torus.mps]] — MPS simulation of the Trotter circuits with quimb CircuitMPS (PLAN M5; API fixed by
tests/acceptance/m5)
- [[su2torus.noise]] — Noisy emulation and error mitigation (PLAN M4; API fixed by tests/acceptance/m4)
- [[su2torus.observables]] — Observables on state vectors (docs/METHODS
- [[su2torus.thermal]] — Thermal (late-time) anchors (docs/METHODS
- [[su2torus.trotter]] — Trotter circuits (docs/METHODS


Back to [[00 SU2QC Map]].
