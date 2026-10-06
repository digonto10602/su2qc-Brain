---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/hardware.py"
lines: 211
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.hardware

Module of [[su2qc-skqd]] · `src/skqd/hardware.py` · 211 lines

## What it does (from the module docstring)

> Hardware-session helpers (manual Step 9.1, prompts/07 and prompts/13).
>
> Two independent jobs:
>
> 1. **Readout calibration.**  `confusion_matrix` turns the counts of the
>    preparation circuits (all-0, all-1 and the single-qubit flips) into a
>    *tensored* (independent-qubit) readout model C with
>    ``C[q, m, p] = P(measure m on qubit q | prepared p)``, and `apply_inverse`
>    unfolds a counts dictionary with the exact tensor inverse
>    ``(C_0^{-1} x ... x C_{n-1}^{-1})``.  The tensored model ignores measurement
>    crosstalk between qubits; it is the model the SKQD manual's Step 9.1 asks for
>    ("per-qubit readout confusion") and it is the only one that can be calibrated
>    with O(n) circuits.  Unfolded counts are quasi-counts: they may be negative.
>
> 2. **Layout bookkeeping of a transpiled circuit.**  A transpiled circuit lives on
>    physical qubits and its routing permutes them, so its statevector is *not* in
>    this package's logical bit order.  `transpiled_layout` reads the final layout
>    and the measurement map off the circuit, and `logical_statevector` returns the
>    noiseless statevector of the transpiled circuit permuted back to logical order
>    (qubit k = bit k, `reference_sim`), which is what `CodewordEmbedding.leakage`
>    expects.  A wrong layout permutation is exactly the mistake that makes a real
>    hardware run decode to garbage, so it is checked before anything is submitted.
>
> `codeword_bit_order` and `link_consistency_checks` export the decoder's own
> bookkeeping (which qubit carries which vertex/link datum, and which qubit pairs
> must agree) into the per-circuit manifests that travel with the job.
>
> Nothing here changes a convention; `codec.py` and `reference_sim.py` are read only.

## Uses

[[skqd.codec]]

## Public names

`confusion_matrix`, `apply_inverse`, `transpiled_layout`, `logical_statevector`, `codeword_bit_order`, `link_consistency_checks`

## Concepts

[[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Codewords and the Gauss-law decoder]] · [[Leakage-safe data splits]] · [[Readout error and confusion matrix]] · [[Transpilation and CZ count]]

## Checked by gates

[[skqd gate H0P]] · [[skqd gate H0_diag]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate K1_2x3_fpilot]] · [[skqd gate S2D_levers]]
