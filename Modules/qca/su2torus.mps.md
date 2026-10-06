---
type: "module"
package: "su2qc-qcadvantage"
file: "su2torus/mps.py"
lines: 166
generated: True
as_of: "2026-10-06"
tags: ["module", "qca"]
---
# su2torus.mps

Module of [[su2qc-qcadvantage]] · `su2torus/mps.py` · 166 lines

## What it does (from the module docstring)

> MPS simulation of the Trotter circuits with quimb CircuitMPS (PLAN M5; API fixed by
> tests/acceptance/m5). The circuit is exactly su2torus.trotter.trotter_circuit; gates are applied
> one by one as explicit matrices (taken from Qiskit, so the conventions cannot drift), on an MPS
> whose site k holds plaquette snake_order(lat)[k].

## Uses

[[su2torus.trotter]]

## Public names

`snake_order`, `simulate_mps`, `mps_statevector`

## Concepts

[[Plaquette and Wilson loop]] · [[Trotter and Strang splitting]] · [[Tensor networks (MPS and TEBD)]] · [[Qiskit]]

## Checked by gates

[[qca gate M5]]
