---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/coherence.py"
lines: 370
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.coherence

Module of [[su2qc-skqd]] · `src/skqd/coherence.py` · 370 lines

## What it does (from the module docstring)

> Coherence requirement of a compiled circuit: what T2 a device must have to run it.
>
> `skqd.idle` answers "given a calibration record, what does the idle time of this schedule
> cost in log-error units".  This module inverts that question -- given a schedule and a
> target clean-shot fraction, what coherence time does the device need -- and puts the answer
> next to the closed-form estimate the owner uses for a nearly serial circuit,
>
>     T2 / t_2q  >=  n_qubits x n_2q / (2 ln(1/f_target))                       (`serial_bound`)
>
> which assumes (a) a perfectly serial circuit, T = n_2q t_2q, (b) every qubit idle for the
> whole of T, and (c) the linearised T2 term only (no T1 channel, no saturation of
> 1 - e^{-w/T2}).  On the frozen 2x2 canary (a) holds to 3 % and (b) does not: the qubit-time
> utilisation is 0.233 (`data/S2_duration_compare.json` rescheduling_headroom), so the qubits
> are idle 77 % of T rather than 100 %.  `t2_requirement` therefore solves the real budget of
> `skqd.idle` (a per-qubit sum over the ACTUAL idle windows of an ASAP schedule) by bisection,
> and the ratio of the two numbers is a measurement rather than an assumption.
>
> Nothing here is fitted and nothing here is a criterion.  Two conventions are always
> arguments of the call, never choices of this module:
>
> * **which T2**.  The bound is quoted as the dimensionless ratio T2 / t_2q; whether the
>   vendor's number is a Hahn-echo T2 or an in-circuit T2* is the vendor's to declare
>   (amendment 01 item 2, `skqd.idle`'s "Which T2" note).
> * **the T1 channel**.  `t1_mode="inf"` charges dephasing only (the serial formula's premise);
>   `t1_mode="equal"` sets T1 = T2, which is the pessimistic end for a device that quotes one
>   coherence number.
>
> `uniform_record` builds a calibration record in exactly the format
> `scripts/h0_backends.calibration_record` writes, so `skqd.idle` reads a synthetic uniform
> device and a real snapshot through the same code path.

## Uses

[[skqd.idle]]

## Public names

`uniform_record`, `complete_edges`, `record_t_2q`, `serial_bound`, `seriality`, `utilisation`, `packing_bound`, `window_arrays`, `t2_requirement`, `requirement_row`, `coherence_scale_one`, `zero_error_record`

## Concepts

[[Clean-shot fraction]] · [[Decoherence (T1 and T2)]]

## Checked by gates

[[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
