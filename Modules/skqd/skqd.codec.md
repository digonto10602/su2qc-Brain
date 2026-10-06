---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/codec.py"
lines: 202
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.codec

Module of [[su2qc-skqd]] · `src/skqd/codec.py` · 202 lines

## What it does (from the module docstring)

> Hardware codewords and the per-shot decoder (Steps 2.4 and 2.5 of the SKQD manual).
>
> Qubit layout: vertices own contiguous blocks of qubits in site order; a bit
> string is a tuple of ints q_0 ... q_{N-1} (q_k = value of qubit k).  Within a
> vertex the first bits are the flux bits of its link ends in canonical (link
> index) order, j = 1/2 <=> 1.
>
> Corner (2 ends), 3 qubits (q1,q2,q3):
>     q1 = q2 -> n in {0,2}, q3 = n/2;    q1 != q2 -> n = 1, q3 = 0 (q3 = 1 is a leakage flag)
> Interior (3 ends), 4 qubits:
>     #flux ends even -> q4 = n/2;  one -> n = 1, q4 = 0 (q4 = 1 flag);  three -> n = 1, q4 = iota
> Charged corner (static spin-1/2), 3 qubits:
>     (0,0) -> n = 1, q3 = 0 (1 flag);  (1,1) -> n = 1, q3 = iota;  unequal -> n in {0,2}, q3 = n/2
> Charged interior, 5 qubits (17 states; the manual fixes the count, the bit
> assignment below is this package's choice):
>     #flux 0 -> n = 1, (q4,q5) = (0,0);   #flux 1 -> n in {0,2}, (q4,q5) = (n/2, 0);
>     #flux 2 -> n = 1, (q4,q5) = (iota, 0);  #flux 3 -> n in {0,2}, (q4,q5) = (n/2, iota);
>     every other (q4,q5) is a flag.
>
> Decoder: (i) split into vertex codewords, (ii) reject any flagged vertex,
> (iii) reject any link whose flux bit differs between its two end vertices,
> (iv) read ({j_l},{n_x},{iota_x}), (v) reject if sum_x n_x is not the target
> sector, (vi) look the label up in the basis index.
>
> Symbols: n = quark occupation, iota = intertwiner label, j = link spin.

## Uses

[[skqd.basis]]

## Used by

`skqd.circuits_ir` · `skqd.hardware` · `skqd.noise` · `skqd.reference_sim`

## Public names

`Reject`, `Codec`

## Concepts

[[Staggered fermions]] · [[Intertwiner (dressed-site) basis]] · [[Baryon-number sectors]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Codewords and the Gauss-law decoder]] · [[Leakage-safe data splits]] · [[Noise models and digital twin]]

## Checked by gates

[[skqd gate E2]] · [[skqd gate H0]] · [[skqd gate H0P]] · [[skqd gate H0P_ibm_fez]] · [[skqd gate H0P_rehearsal]] · [[skqd gate H0_2x2]] · [[skqd gate H0_canary]] · [[skqd gate H0_ddrep]] · [[skqd gate H0_ddtest]] · [[skqd gate H0_diag]] · [[skqd gate H0_dryrun]] · [[skqd gate H0_kpilot]] · [[skqd gate H0_model]] · [[skqd gate H1]] · [[skqd gate H2]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate K1_2x3_fpilot]] · [[skqd gate L2]] · [[skqd gate L3]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate L5]] · [[skqd gate S1]] · [[skqd gate S2D]] · [[skqd gate S2D_levers]]
