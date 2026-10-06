---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/physics/chain.py"
lines: 265
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "physics"]
---
# su2qc_jepa.physics.chain

Module of [[su2qc-jepa]] · `src/su2qc_jepa/physics/chain.py` · 265 lines

## What it does (from the module docstring)

> The Krylov-chain hardware carrier (one-hot / unary encoding of the Lanczos basis).
>
> Given the tridiagonal Krylov Hamiltonian H_K = sum_k alpha_k |k><k| + sum_k beta_k (|k><k+1| + h.c.),
> encode the K Krylov vectors as the K single-excitation states |k> = |0..010..0> of K qubits on a
> line.  In the single-excitation sector
>     |k><k|            -> n_k = (1 - Z_k)/2
>     |k><k+1| + h.c.   -> (X_k X_{k+1} + Y_k Y_{k+1})/2
> so H_K becomes a nearest-neighbour XY chain with site-dependent fields, and
> exp(-i H_K t) is realised by a second-order (Strang) product formula whose
> entangling cost is 2 CZ per bond per step on IBM hardware.
>
> The circuit conserves the excitation number, so any shot outside the single-
> excitation sector is a detectable error ("excitation flag"), the chain analogue
> of the gauge-leakage flags of the L12 encoding.
>
> `chain_sector_unitary` gives the exact K x K action of the *ideal* Trotter circuit
> inside the single-excitation sector (no 2^K simulation needed), which is the
> noiseless reference against which hardware and twin records are compared.

## Uses

[[su2qc_jepa.physics.dynamics]]

## Used by

`su2qc_jepa.data.records` · `su2qc_jepa.gates.j0_data` · `su2qc_jepa.twin.run`

## Public names

`ChainSpec`, `chain_sector_unitary`, `chain_amplitudes`, `trotter_error`, `cz_count`, `build_chain_circuit`, `sample_z_basis`, `x_basis_probabilities`, `sample_x_basis`, `prep_cascade_params`, `build_chain_prep_circuit`

## Concepts

[[Baryon-number sectors]] · [[Krylov subspace and Lanczos]] · [[Trotter and Strang splitting]] · [[Leakage-safe data splits]] · [[Krylov-chain carrier]] · [[Noise models and digital twin]] · [[Transpilation and CZ count]] · [[L12 encoding]]
