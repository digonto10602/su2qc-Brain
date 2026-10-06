---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/noise.py"
lines: 107
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.noise

Module of [[su2qc-skqd]] · `src/skqd/noise.py` · 107 lines

## What it does (from the module docstring)

> Device-proxy noise model on bit strings (Step 8.2 of the SKQD manual).
>
> Each shot is clean with probability f; otherwise it is, with equal
> probability, a uniformly random bit string or the clean sample with
> Poisson(2) random bit flips.  Independent readout flips with probability
> p_ro per qubit are then applied to every shot.  The decoder of codec.py is
> applied last.
>
> The clean shots are multinomial samples of the ideal state in the
> configuration basis, converted to codewords.
>
> Symbols: f = circuit fidelity proxy (fraction of clean shots), p_ro = readout
> flip probability per qubit, S = number of shots.

## Uses

[[skqd.codec]]

## Public names

`corrupt_shots`, `measure_and_decode`, `measure_and_decode_sequence`

## Concepts

[[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Codewords and the Gauss-law decoder]] · [[Clean-shot fraction]] · [[Readout error and confusion matrix]] · [[Noise models and digital twin]]

## Checked by gates

[[skqd gate S1]]
