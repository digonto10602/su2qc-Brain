---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/idle.py"
lines: 270
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.idle

Module of [[su2qc-skqd]] · `src/skqd/idle.py` · 270 lines

## What it does (from the module docstring)

> Idle-time relaxation in the clean-shot fraction f.
>
> `gate_S2D.analyse_on_backend` (and `device_req.clean_shot_fraction`, its inverse algebra)
> computes f as a product over the *instructions* of a compiled circuit,
>
>     f_gates = prod_{2q gates} (1 - eps_gate) x prod_{measured qubits} (1 - eps_ro) ,
>
> and therefore contains no term for the time a qubit spends WAITING for other qubits'
> gates.  On a heavy-hex device the routed 2x2 coarse step is nearly serial (663 CZ in
> depth 1328, 43.71 us before readout) and each of its 12 qubits idles 19-42 us of that;
> the omission is not small.  Gate H0_diag (2026-09-22, `validation/H0_diag.json`) measured
> the canary circuit under {DD on/off} x {twirling on/off} and found f = 0.0255 where
> `analyse_on_backend` predicted 0.2195, with the idle term accounting for the whole
> discrepancy (3.323 error units available against 2.153 missing).
>
> This module adds that term, with no fitted parameter.  It schedules a compiled circuit
> ASAP on a calibration RECORD (`scripts/h0_backends.calibration_record`: the record's own
> durations, T1, T2 and errors), collects the idle windows of every active qubit, and
> converts them into a log-error budget in the Pauli-twirling approximation of thermal
> relaxation -- the channel Aer's `RelaxationNoisePass` would attach to an explicit `delay`:
>
>     per idle window w on qubit q:   p = (1 - e^{-w/T1_q})/4 + (1 - e^{-w/T2_q})/2
>     S_T1 = sum_q sum_w (1 - e^{-w/T1_q})/4     S_T2 = sum_q sum_w (1 - e^{-w/T2_q})/2
>     f    = f_gates x exp(-S_T1 - S_T2)                                   (DD off)
>
> The runtime's `PadDynamicalDecoupling` pads a window only when it is longer than
> `sequence_min_length_ratios` (default 2.0) times the sequence length, so with XY4 =
> 4 x sx_duration a window is DD-eligible when w / (4 sx_duration) > 2.0, and one sequence
> per eligible window costs S_DD = sum_eligible 4 x sx_error.  The refocusing efficiency
> rho (the fraction of the eligible-window T2 budget that survives DD) is not computable
> from a calibration, so DD-on predictions are a bracket over rho:
>
>     f(rho) = f_gates x exp(-S_T1 - rho S_T2_eligible - S_T2_ineligible - S_DD) .
>
> **Which T2.**  The calibration record's `T2_s` is the vendor's Hahn-echo T2; the windowed
> Ramsey test of gate H0_diag measured the free-induction T2* on the same patch on the same
> day and found it 2-7x shorter (median ratio 0.174 over the 9 qubits with a usable time).
> Neither is the effective dephasing time inside a circuit, and H0_diag does not determine
> where between them it lies: on the echo T2 the idle-aware model predicted 31 accepted
> shots against the measured 35 (a factor 1.13), on the measured T2* it is 89x too
> pessimistic.  This module therefore never chooses: `idle_budget` takes an explicit
> per-qubit `t2_s` override and `effective_t2` builds one from a recorded ratio, so the
> convention is always an argument of the call and a recorded field of the output.
>
> Nothing here is a criterion and nothing here is fitted.  The bars of amendment 01
> section 1(c) (mean f >= 0.1, worst f >= 0.05) are unchanged; what changes is the f they
> are read on.

## Used by

`skqd.coherence`

## Public names

`instruction_duration_s`, `schedule_asap`, `effective_t2`, `effective_t1`, `idle_budget`, `idle_log_budget`, `relaxation_factor`, `f_idle_aware`

## Concepts

[[Trotter and Strang splitting]] · [[Clean-shot fraction]] · [[Dynamical decoupling]] · [[Decoherence (T1 and T2)]] · [[Readout error and confusion matrix]] · [[Noise models and digital twin]] · [[Transpilation and CZ count]] · [[Gate-and-evidence discipline]]

## Checked by gates

[[skqd gate H0P]] · [[skqd gate H0_ddtest]] · [[skqd gate H0_kpilot]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate S2D_idle]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
