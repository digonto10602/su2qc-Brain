---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/circuits/strang_l12.py"
lines: 251
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "circuits"]
---
# su2qc.circuits.strang_l12

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/circuits/strang_l12.py` · 251 lines

## What it does (from the module docstring)

> Exact gauge-invariant block unitaries and Strang circuits for L12 (G3).
>
> Method (structure, not generic 12-qubit synthesis):
>   * Each Hamiltonian group T in {D, h0..h3, B} is an 82x82 matrix from the
>     verified route-1 Hamiltonian (term split checked exact by the dynamics
>     lane).  Lifted to the 4096-dim code space it is E T E^dag: zero on every
>     unphysical code, so exp(-i theta E T E^dag) is the identity on the
>     complement -> gauge invariance by construction, zero leakage.
>   * D is diagonal: a 12-qubit Diagonal gate (phases on the 82 codes, 1 else).
>   * Each h_l and B act non-trivially on a SUPPORT of s < 12 qubits (found
>     numerically as the qubits whose bits ever change or on which the matrix
>     element depends); the lifted operator factorizes as U_s (x) I on the rest
>     when all elements depend only on the support bits.  For links whose
>     Jordan-Wigner string crosses other vertices, the sign depends on the
>     parity (a XOR b) of those vertices; the support then includes those
>     (a,b) pairs.  U_s = expm(-i theta M_s) on 2^s dims (s <= 10), built as a
>     UnitaryGate.  Exactness is verified by tests to 1e-12.
>   * Strang step: D/2 . [h0,h2]/2 . [h1,h3]/2 . B . [h1,h3]/2 . [h0,h2]/2 . D/2
>     (l0=(v0,v1), l2=(v3,v2) disjoint; l1=(v1,v2), l3=(v0,v3) disjoint).
>
> Verification helpers avoid dense 4096x4096 operators: the circuit is applied
> to statevectors on the 82 codes with Aer/Statevector, and compared with the
> exact 82-dim propagator.

## Uses

[[su2qc.dynamics.scan]] · [[su2qc.encodings.l12]]

## Used by

`su2qc.circuits.export_l12` · `su2qc.circuits.synth_l12` · `su2qc.compile.route` · `su2qc.compile.run_g4`

## Public names

`params`, `terms`, `code_index`, `basis_to_code`, `local_matrix`, `supports`, `unitary`, `strang_step`, `prep_stretched`, `full_circuit`, `exact_strang_matrix`, `circuit_state`, `to_basis`, `leakage_prob`, `resources`

## Concepts

[[Gauss's law]] · [[Jordan-Wigner mapping]] · [[Trotter and Strang splitting]] · [[Leakage-safe data splits]] · [[Noise models and digital twin]] · [[L12 encoding]]

## Checked by gates

[[su2zx gate S8-G3]]
