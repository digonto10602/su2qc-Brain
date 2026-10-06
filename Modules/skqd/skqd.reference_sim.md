---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/reference_sim.py"
lines: 189
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.reference_sim

Module of [[su2qc-skqd]] · `src/skqd/reference_sim.py` · 189 lines

## What it does (from the module docstring)

> numpy reference for the circuit layer: codeword embedding of the gauge-invariant
> basis into the 2^n computational space, exact local block unitaries of every
> Hamiltonian term, and a plain statevector simulator that applies those local
> gates.  Everything here runs without Qiskit or CUDA-Q and is what the laptop
> gates compare the Qiskit / CUDA-Q circuits against.
>
> Bit order.  Qubit k is bit k of the computational-basis integer
> (index = sum_k q_k 2^k, little-endian), which is Qiskit's convention for
> Statevector indices; a Qiskit counts key (a string with qubit 0 at the RIGHT
> end) is converted to this package's bit tuple by reversing the string.
>
> Local block unitaries.  For a term gamma with matrix O in the dressed-site basis
> the local support is: the qubits of the touched vertices (x, y for a hopping
> link; the four corners for a plaquette) plus, for a hopping term, the flux
> qubits of the Jordan-Wigner sites strictly between x and y (whose parity
> (-1)^{n_z} is the XOR of their flux bits).  O is local on that support (checked
> by assertion: matrix elements agree for every extension of the local bits).
> The gate is  U_loc = exp(-i theta O_loc) = 1 + V (exp(-i theta h) - 1) V^dag  with
> V the isometry onto the valid local codewords (h = O restricted to them), so it
> acts as the identity on flagged / link-inconsistent local strings and is exactly
> gauge invariant on the physical subspace.
>
> Plaquette at 2x2.  W + W^dag = D X^{(x)8}: every physical state is paired with
> the state with all four link spins flipped (all eight flux bits), and the pair
> amplitude w in {-2, +-1, 1/2} depends only on which corners carry one quark
> (the four corner parities p_c = q1 XOR q2); plaquette_pair_amplitudes checks
> this structure and returns the table.  The structured circuit that uses it
> (CNOT(q1_c -> q2_c) per corner, H on the q1's, CNOT ladder, Gray-code
> uniformly controlled Rz on the last q1 controlled by the parities, inverse)
> lives in circuits_ir.CircuitFactory.plaq_gates and is verified against the
> dense exponential by scripts/report_circuit_structure.py and tests/.
>
> Symbols: theta = angle (k dt for a coarse step), O_loc = local term operator,
> V = codeword isometry, w(p) = plaquette pair amplitude.

## Uses

[[skqd.codec]] · [[skqd.exact]]

## Used by

`skqd.circuits_ir` · `skqd.circuits_qiskit`

## Public names

`bits_to_int`, `int_to_bits`, `qiskit_key_to_bits`, `CodewordEmbedding`, `term_support`, `localize`, `local_unitary`, `apply_local`, `plaquette_pair_amplitudes`

## Concepts

[[Gauss's law]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Intertwiner (dressed-site) basis]] · [[Jordan-Wigner mapping]] · [[Trotter and Strang splitting]] · [[Codewords and the Gauss-law decoder]] · [[Transpilation and CZ count]] · [[Qiskit]] · [[CUDA-Q]]

## Checked by gates

[[skqd gate CF_traj]] · [[skqd gate H0]] · [[skqd gate H0P]] · [[skqd gate H0P_ibm_fez]] · [[skqd gate H0P_rehearsal]] · [[skqd gate H0_canary]] · [[skqd gate H0_diag]] · [[skqd gate H0_dryrun]] · [[skqd gate H0_model]] · [[skqd gate H1]] · [[skqd gate H2]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate L2]] · [[skqd gate Q0P_2x3]] · [[skqd gate S2]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
