---
type: "index"
tags: ["index"]
generated: True
as_of: "2026-10-06"
---
# Gates index

Every gate in every package (generated from the repositories).

## [[su2qc-skqd]]

| gate | checks | status |
|---|---|---|
| [[skqd gate E1]] | [G_a(x),H]=0; 82-dim kernel; sector split; two builders agree to 1e-12 | PASS |
| [[skqd gate E2]] | counts of Table 2; codec round trip on all 2x3 states; random-bitstring acceptance ~0.15% | PASS |
| [[skqd gate E3]] | 2x3 and 2x4 references (Table 1); static sectors; dt = pi/W per sector | PASS |
| [[skqd gate S1]] | emulated support recall >= 0.9 at f >= 0.1 with the production budget; controls table | PASS |
| [[skqd gate CS]] | structure of the terms in codeword space (input to S2) | PASS |
| [[skqd gate L2]] | Qiskit circuits reproduce the numpy reference at 2x2 | PASS |
| [[skqd gate L3]] | transpiled CZ counts (S2 measurement) | FAIL |
| [[skqd gate L4]] | Aer noise-model sampling at 2x2 (S3 preparation) | PASS |
| [[skqd gate L5]] | CUDA-Q circuits reproduce the numpy reference at 2x2 | PASS |
| [[skqd gate S2]] | routed CZ per coarse step <= 500 on the target map (<= 250 at 2x2); compiled circuits leak-free | FAIL |
| [[skqd gate S2D]] | device-resolved budget (prompts/12): mean clean-shot fraction f >= 0.1 (worst >= 0.05) per lattice and device; k=1 count | FAIL |
| [[skqd gate L4_fez]] | L4 with NoiseModel.from_backend(FakeFez) and transpilation onto the snapshot (H0 rehearsal) | PASS |
| [[skqd gate S3]] | Aer device-model recall >= 0.9 for the production set; shot budget fixed | PASS |
| [[skqd gate S3_smoke]] | S3 pipeline smoke test at 2x3 B=1 (2 shots per circuit: NOT the production budget) | FAIL |
| [[skqd gate H0P]] | H0 preparation on a calibration snapshot: frozen circuit set leak-free, predicted yield per repetition, readout confusio | PASS |
| [[skqd gate H0_dryrun]] | gate H0 run on the SamplerV2 dry-run counts (data/hardware/H0_dryrun) | PASS |
| [[skqd gate H0P_ibm_fez]] | H0P re-predicted on the live ibm_fez calibration of the session day (prompts/15 D1: the circuits stay frozen, only the p | PASS |
| [[skqd gate H0P_rehearsal]] | H0P on FakeFez with the D3' shot plan through the sampling cache (prompts/16) | PASS |
| [[skqd gate H0_canary]] | the 3-pub canary of prompts/15 D5 on ibm_fez (one frozen r=1 circuit + the two patch-1 readout circuits): the go rule be | FAIL |
| [[skqd gate H0_diag]] | the prompts/19 diagnostic session on ibm_fez: the DD x twirling factorial of the frozen canary circuit and the windowed  | FAIL |
| [[skqd gate H0]] | 2x2 hardware: decoder validity, bit order, parity checks; measured f within 30% of the model | OPEN |
| [[skqd gate H1]] | 2x3 B=0: certified interval of width <= 0.1 containing the exact E0; recall >= 0.8 | OPEN |
| [[skqd gate H2]] | 2x3 B=1: cluster energy certified to +-rH <= 0.15; V(1), V(2) intervals containing exact values | OPEN |
| [[skqd gate P1]] | primary endpoint curves with bootstrap bands | OPEN |
| [[skqd gate M1]] | ML uses credited only under Step 7.5 | OPEN |
| [[skqd gate S2_2x4]] | 2x4 coarse step compiled to exact circuits and verified (measurement gate: counts, duration, idle budget, T2/t_2q requir | PASS |
| [[skqd gate H0_model]] | post-diction of the H0 hardware counts by the scheduled-Aer model at both ends of the T2 bracket; the clean-yield statis | PASS |
| [[skqd gate S2D_levers]] | 2x2 duration levers on ibm_kingston: compile/schedule levers measured, f predicted at both T2 ends, r_crit (measurement  | PASS |
| [[skqd gate H0_kpilot]] | ibm_kingston pilot on the selected patch: windowed Ramsey at two lengths (T2*/T2_echo ratio r_eff vs r_crit), T1, the si | FAIL |
| [[skqd gate H0_ddtest]] | one-job A/B test of client-side DD (context-aware, XY4, XY4-long) against the no-DD baseline on the pilot's two k = 1 ci | PASS |
| [[skqd gate H0_2x2]] | the full 2x2 SKQD run on ibm_kingston below the signed budget (owner decision 2026-10-02): both sectors, D3' at the meas | PASS |
| [[skqd gate Q0P_2x3]] | prompts/26 Stage A: the signed 2x3 circuits compiled to the Quantinuum native gate set (Rz, PhasedX, ZZPhase) for H2-2 / | PASS |
| [[skqd gate CF_traj]] | prompts/28 Part A / prompts/29 Part A': Pauli-trajectory decomposition of the A6 Aer channel on the frozen 2x3 circuits; | PASS |
| [[skqd gate CF_estimator_2x2_info]] | note under H0_2x2 (prompts/28 B4 / prompts/29 3(3)): the recorded 2x2 f values are f_hit; f_hat_ideal = f_hit / r_nc and | PASS |
| [[skqd gate CV_2x2_info]] | note under H0_2x2 (prompts/30 section 5): the convergence/coverage curves on the H0_2x2 counts; not a device test (satur | PASS |
| [[skqd gate Q0P_2x3_plan]] | prompts/28 B3 / prompts/29 B' / prompts/30 P7: rule D3'-R (minimum 2x3 sizing), GO rule v3 on f_hat_ideal, Stage E/P v3, | PASS |
| [[skqd gate CV_2x3_plan]] | prompts/30 (owner decision 2a): energy convergence vs shots and Krylov k and weighted coverage of the D3'-R plan in the  | PASS |
| [[skqd gate H0_ddrep]] | one-job replication of the XY4 gain (T0 vs T3) and of the context-aware collapse (T1) with four mechanism cells (CA+/-,  | PASS |
| [[skqd gate K1_2x3_fpilot]] | prompts/27 stage 0b / prompts/32 B: the 2x3 clean-fraction pilot on ibm_kingston, the two signed k = 1 circuits routed a | PASS |
| [[skqd gate H0P_repro]] | H0 preparation on the FakeFez calibration snapshot: frozen circuit set, predicted yield curve by repetition, readout con | PASS |
| [[skqd gate H0_2x2_dryrun]] | the full 2x2 SKQD run on ibm_kingston below the signed budget (owner decision 2026-10-02): both sectors, D3' at the meas | PASS |
| [[skqd gate H0_ddrep_dryrun]] | one-job replication of the XY4 gain (T0 vs T3) and of the context-aware collapse (T1) with four mechanism cells and four | PASS |
| [[skqd gate H0_ddtest_dryrun]] | one-job A/B test of client-side DD (context-aware, XY4, XY4-long) against the no-DD baseline on the pilot's two k = 1 ci | PASS |
| [[skqd gate H0_diag_dryrun]] | H0 diagnostic session on ibm_fez: the DD x twirling factorial of the frozen canary circuit and the windowed idle tests t | FAIL |
| [[skqd gate H0_kpilot_dryrun]] | ibm_kingston pilot on the selected patch: windowed Ramsey at two lengths (T2*/T2_echo ratio r_eff vs r_crit), T1, the si | PASS |
| [[skqd gate K0_2x3_2x4]] | ibm_kingston readiness of 2x3 and 2x4 on a calibration record: routed CZ, gate-only, idle-aware and XY4-transfer f (prom | PASS |
| [[skqd gate K1_2x3_fpilot_dryrun]] | the 2x3 clean-fraction pilot on ibm_kingston: two signed k = 1 circuits (largest p_ref per sector), routed as gate K0, A | PASS |
| [[skqd gate L4_p2_1e-3]] | Aer noise-model sampling at 2x2 (S3 preparation) | FAIL |
| [[skqd gate L4_p2_3e-3]] | Aer noise-model sampling at 2x2 (S3 preparation) | FAIL |
| [[skqd gate S2D_idle]] | Gate S2D's 2x2 criterion (mean f >= 0.1, worst f >= 0.05) re-evaluated on the idle-aware clean-shot fraction, at both en | FAIL |
| [[skqd gate S2_fixed]] | Fixed-angle generator (same codeword pairs, one angle per flip pattern): cost floor, leakage and recall | FAIL |

## [[su2qc-jepa]]

| gate | checks | status |
|---|---|---|
| [[jepa gate J0]] | data | PASS |
| [[jepa gate J1]] | training | FAIL |
| [[jepa gate J2]] | forecast | NOT-RUN |
| [[jepa gate J3]] | hardware | NOT-RUN |
| [[jepa gate J4]] | quantum encoder | OPTIONAL |

## [[genesis-su2-lgt]]

| gate | checks | status |
|---|---|---|
| [[genesis gate G0]] | core CPU starter | PASS |
| [[genesis gate G1]] | SU(2) fundamental algebra | PASS |
| [[genesis gate G2]] | two-plaquette exact oracle | PASS |
| [[genesis gate G3]] | Qiskit V2 product formula | PASS |
| [[genesis gate G4]] | native cross-language kernels | PARTIAL |
| [[genesis gate G5]] | QML energy surrogate | PASS |
| [[genesis gate G6.1]] | finite-shot kernel | COMPLETED-NEGATIVE |
| [[genesis gate G7.1]] | independent frozen-oracle validation | PASS |
| [[genesis gate G7.2-G7.4]] | encoding/Gauss fixture | PASS |
| [[genesis gate G7.7]] | cutoff/resource study | PARTIAL |
| [[genesis gate G7.5-G7.6]] | matched Hamiltonian/reduced comparison | NOT-STARTED |
| [[genesis gate G7.8]] | encoding decision/closure | PARTIAL |

## [[SU2ZX]]

| gate | checks | status |
|---|---|---|
| [[su2zx gate S8-G0]] | Section 8 v0.5.0 overnight run - criteria: run/T0, run/PROMPT_HASH, run/CONFIG_ENV.md, run/INVENTORY.md, run/MODELS.md,  | PASS |
| [[su2zx gate S8-G1]] | Section 8 v0.5.0 overnight run - criteria: dim_route1_jmax0.5, dim_route2_jmax0.5, dim_route1_jmax1.0, dim_route2_jmax1. | PASS |
| [[su2zx gate S8-G2]] | Section 8 v0.5.0 overnight run - criteria: expm_vs_krylov, energy_conservation, N_conservation, mass_scan_table, resonan | PASS |
| [[su2zx gate S8-G3]] | Section 8 v0.5.0 overnight run - criteria: l12_test_suite, l12_physical_codes, s8_encoding, c7_encoding, block_unitary_d | PASS |
| [[su2zx gate S8-G4]] | Section 8 v0.5.0 overnight run - gate script written, never run | NOT-RUN |
| [[su2zx gate C0]] | GI-cost campaign v0.6.x: V1, V11, Tier 2 pass; V10 distinctness at both r; variance band at r = 0; r = 1 variance record | PARTIAL |
| [[su2zx gate C1]] | GI-cost campaign v0.6.x: three hashes inline; conventions ambiguity resolved under labelled keys; defect classes includi | PASS |
| [[su2zx gate C2]] | GI-cost campaign v0.6.x: V2 both points; V3, V5, V7 counts; V4 table; V6 recorded; V7 route clause resolved or recorded  | NOT-RUN |
| [[su2zx gate C3]] | GI-cost campaign v0.6.x: V8 per accepted circuit; K(t) both points; rejected list; layout table | NOT-RUN |
| [[su2zx gate C4]] | GI-cost campaign v0.6.x: V9; E1 and E5 drafts; sprint closed with its number; decision row | NOT-RUN |
| [[su2zx gate C5]] | GI-cost campaign v0.6.x: V12 on EMULATED at ≥ 2 time points per arm; δ_dev frozen; hash; QPU estimate in cap | NOT-RUN |
| [[su2zx gate C6]] | GI-cost campaign v0.6.x: BLOCKED, precondition named | BLOCKED |
| [[su2zx gate C7]] | GI-cost campaign v0.6.x: BLOCKED, precondition named | BLOCKED |
| [[su2zx gate C8]] | GI-cost campaign v0.6.x: BLOCKED, precondition named | BLOCKED |

## [[su2qc-trotter]]

| gate | checks | status |
|---|---|---|
| [[trotter gate B1]] | scripts/run_benchmark.py: 60-step Trotter evolution of the plaquette on nvidia-fp64 and nvidia, vs exact | PASS |
| [[trotter gate G22]] | scripts/gpu_compare.py: the 8 comparison tests for the 22-qubit lean circuit, fp64 | PASS |
| [[trotter gate G34]] | the 8 comparison tests for the 34-qubit reference, fp64, 32 A100s | PASS |
| [[trotter gate M0]] | multi-node smoke: the 34-qubit reference in fp64 spread over 32 A100s, 2 steps + 1 echo | PASS |
| [[trotter gate R1]] | scripts/run_resources.py: exhaustive exact checks, Clifford+T synthesis, cudaq.estimate_resources tally | PASS |
| [[trotter gate V1]] | scripts/run_cudaq_verify.py --target nvidia-fp64: GPU state-vector verification of the lean circuit (exact and Clifford+ | PASS |
| [[trotter gate smoke]] | CUDA-Q nvidia (12-qubit GHZ) and nvidia-fp64 (22-qubit state), package import | PASS |

## [[su2qc-qcadvantage]]

| gate | checks | status |
|---|---|---|
| [[qca gate M1]] | model correctness (locked tests: G1–G5). Outcome: lattice + H (sparse, Pauli, numba matrix-free). Audit PASS. | PASS |
| [[qca gate M2]] | exact dynamics, Trotter circuits, gate counts (locked tests: G6–G8). Outcome: order-1 step = 9.5n (native ZZ) / 11n (CZ) | PASS |
| [[qca gate M3]] | small-torus physics (locked tests). Outcome: 18 N=12 + 6 N=24 runs + open string; E conserved < 1e-7. Audit: report word | PASS |
| [[qca gate M4]] | noisy emulation and error mitigation (reviewer writes tests). Outcome: N=12 exact density matrix; ZNE cuts <H_E> error 5 | PASS |
| [[qca gate M5]] | classical-campaign code ready for the cluster (reviewer writes tests). Outcome: MPS (quimb) N=24 chi=256 1-F=1.1e-9; res | PASS |
| [[qca gate M6]] | convergence evidence and collaborator package (reviewer writes tests). Outcome: N=48 stripe chi 32–256 (chi=256: 6935 s, | PASS |


Back to [[00 SU2QC Map]].
