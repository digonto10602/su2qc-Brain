---
type: "module"
package: "su2qc-qcadvantage"
file: "su2torus/noise.py"
lines: 140
generated: True
as_of: "2026-10-06"
tags: ["module", "qca"]
---
# su2torus.noise

Module of [[su2qc-qcadvantage]] · `su2torus/noise.py` · 140 lines

## What it does (from the module docstring)

> Noisy emulation and error mitigation (PLAN M4; API fixed by tests/acceptance/m4).
>
> Noise model (Aer convention, k qubits, d = 2**k): after each gate
>     E(rho) = (1 - p) rho + p Tr_k(rho) (x) I/d,
> with p = p2 on every cx / rzz and p = p1 on every 1-qubit gate, plus a symmetric readout
> error r on every qubit. Predicted global fidelity: the probability that no gate applies a
> non-identity Pauli, F = prod_gates (1 - eps), eps = p (1 - 1/d^2) (process infidelity):
> eps_2q = 15 p2 / 16, eps_1q = 3 p1 / 4.

## Uses

[[su2torus.trotter]]

## Public names

`noise_model`, `run_noisy`, `predicted_fidelity`, `echo_circuit`, `echo_fidelity`, `mitigate_rescale`, `zne`, `fold_gates`

## Concepts

[[Readout error and confusion matrix]] · [[Noise models and digital twin]]

## Checked by gates

[[qca gate M4]]
