---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/circuits_ir.py"
lines: 973
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.circuits_ir

Module of [[su2qc-skqd]] · `src/skqd/circuits_ir.py` · 973 lines

## What it does (from the module docstring)

> Backend-independent circuit description ("IR") of the support-generating
> circuits, built from exact local block unitaries of the Hamiltonian terms.
> The IR is a list of gates (name, qubits, params):
>
>     ('x',  [q], None)                     Pauli X (state preparation)
>     ('h',  [q], None)
>     ('rz', [q], angle)                    Rz(angle) = exp(-i angle Z / 2)
>     ('p',  [q], angle)                    phase gate diag(1, e^{i angle})
>     ('cp', [c, t], angle)                 controlled phase diag(1,1,1,e^{i angle})
>     ('cx', [c, t], None)
>     ('unitary', qubits, U)                dense 2^k x 2^k unitary, qubits[0] = least significant bit
>
> Everything in this file is executed and verified in numpy (reference_sim.py);
> the Qiskit and CUDA-Q modules only translate the IR.
>
> Term gates for exp(-i theta H_gamma), gamma in {diag, hop_l, plaq_P}:
>   * diag: exact phases from n_x and j_l read from the codeword bits
>       corner:   n = (q1 xor q2) + 2 q3            (valid codewords)
>       interior: n = f + 2 q4 (1 - f), f = q1 xor q2 xor q3 (parity of the flux ends)
>       electric: (g^2/2) * 3/4 per flux link, applied once, on the 'out' end's flux qubit
>   * hop_l: dense local unitary on the support of reference_sim.term_support
>   * plaq_P: structured gate at 2x2 (corner-only plaquettes) with a Gray-code
>     uniformly controlled Rz; dense local unitary otherwise (only usable for
>     statevector simulation when the support has <= 12 qubits; larger supports
>     raise NotImplementedError until the S2-b decomposition exists).
>     Note: the structured gate equals the dense block unitary on the codeword
>     subspace but is NOT the identity on leaked (non-codeword) strings, whereas
>     the dense local unitary is; with noise the two differ on leaked states.
>
> Coarse single-step circuit (manual Step 4.3 b): X gates preparing the reference
> codeword, then the term gates with theta = k dt in the order diag, hop_0, hop_1,
> ..., plaq_0, ...  (same order as krylov.term_groups).  First-order Trotter: the
> same block repeated k times with theta = dt.
>
> Symbols: theta = angle, dt = Krylov step, k = coarse-step multiplier.

## Uses

[[skqd.codec]] · [[skqd.exact]] · [[skqd.krylov]] · [[skqd.reference_sim]]

## Public names

`gray`, `ucr_angles`, `ucr_gray`, `ucrz_gray`, `structured_term_gates`, `term_structure`, `CircuitFactory`, `run_ir`, `gate_counts`

## Concepts

[[Plaquette and Wilson loop]] · [[Electric basis]] · [[Krylov subspace and Lanczos]] · [[Trotter and Strang splitting]] · [[Codewords and the Gauss-law decoder]] · [[Qiskit]] · [[CUDA-Q]]

## Checked by gates

[[skqd gate K0_2x3_2x4]] · [[skqd gate L2]] · [[skqd gate L3]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate L5]] · [[skqd gate S2]] · [[skqd gate S2D]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
