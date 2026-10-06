---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/quantinuum_native.py"
lines: 333
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.quantinuum_native

Module of [[su2qc-skqd]] · `src/skqd/quantinuum_native.py` · 333 lines

## What it does (from the module docstring)

> The Quantinuum native gate set {Rz, PhasedX, ZZPhase} for the IR circuits (prompts/26, gate Q0P_2x3).
>
> pytket is NOT a dependency of this package: it lives in the isolated venv
> ~/.local/share/su2qc-quantinuum/venv (created with --system-site-packages from the `coding` env, so
> the pinned qiskit / aer / numpy / scipy are the same objects), and every function that needs it
> imports it lazily.  The functions that need no pytket (`qiskit_to_ir`, `hqc_per_shot`, `hqc_job`,
> `ir_counts`, `counts_from_pytket_readouts`, `global_phase_residual`) work in `coding` too.
>
> Conventions (https://docs.quantinuum.com/tket/api-docs/optype.html, read 2026-10-02; pytket angles
> are in HALF-TURNS, 1 half-turn = pi rad):
>
>     Rz(a)        = exp(-i pi a Z / 2)
>     Rx(a)        = exp(-i pi a X / 2),   Ry(a) = exp(-i pi a Y / 2)
>     PhasedX(a,b) = Rz(b) Rx(a) Rz(-b)                (operator product)
>     ZZPhase(a)   = exp(-i pi a (Z x Z) / 2),   ZZMax = ZZPhase(1/2)
>
> The IR (src/skqd/circuits_qiskit.ir_to_qiskit, qiskit convention): rz(l) = exp(-i l Z/2),
> rx(t) = exp(-i t X/2), ry(t) = exp(-i t Y/2), rzz(p) = exp(-i p (Z x Z)/2).  Hence
> rz(l) -> Rz(l/pi), rx(t) -> Rx(t/pi), ry -> Ry(t/pi), rzz(p) -> ZZPhase(p/pi), and PhasedX(a, b)
> reads back as the TIME-ORDERED IR  rz(-pi b), rx(pi a), rz(pi b)  (the operator product read
> right-to-left; fixed by tests/test_quantinuum_native.py against Circuit.get_unitary(), not from
> memory).  The global phase of a pytket circuit (`Circuit.phase`, half-turns) becomes an IR
> `gphase` of pi * phase.
>
> Qubit order: IR qubit k = pytket qubit q[k] = classical bit c[k] (measure q[k] -> c[k]).  pytket's
> `BackendResult.get_counts()` returns bit tuples "in increasing lexicographic order of bits"
> (pytket.backends.backendresult.BasisOrder.ilo, the default), i.e. (c[0], c[1], ...): index k of the
> tuple is bit c[k] = qubit k, which is this package's bit-tuple convention (reference_sim: qubit k =
> bit k).  `counts_from_pytket_readouts` checks that ordering explicitly.
>
> Billing (https://learn.microsoft.com/en-us/azure/quantum/provider-quantinuum, read 2026-10-02):
> HQC = 5 + C (N_1q + 10 N_2q + 5 N_m) / 5000 per job; N_1q = PhasedX count (Rz is virtual and "Rz
> operations excluded", https://docs.quantinuum.com/systems/trainings/helios/getting_started/costing.html),
> N_2q = ZZPhase + ZZMax count, N_m = initialisations + measurements, C = shots.

## Public names

`NativeCompileError`, `qiskit_to_ir`, `ir_counts`, `hqc_per_shot`, `hqc_job`, `global_phase_residual`, `counts_from_pytket_readouts`, `ir_to_pytket`, `compile_config`, `offline_backend`, `check_native`, `compile_native`, `pytket_to_ir`, `native_counts`, `to_qasm`, `from_qasm`, `to_json`, `from_json`, `versions`

## Concepts

[[Readout error and confusion matrix]] · [[Gate-and-evidence discipline]] · [[Qiskit]] · [[Quantinuum H-series]]

## Checked by gates

[[skqd gate CF_traj]] · [[skqd gate Q0P_2x3]]
