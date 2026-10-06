---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/fullspace.py"
lines: 187
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.fullspace

Module of [[su2qc-skqd]] · `src/skqd/fullspace.py` · 187 lines

## What it does (from the module docstring)

> Redundant-basis ("projector") construction of the 2 x 2 model — the second,
> independent route of gate E1 (Step 1.3 of the SKQD manual).
>
> The full Hilbert space is the tensor product of the four truncated link spaces
> (5 states each for jmax = 1/2) and the four site Fock spaces (4 states each):
> dimension 5^4 * 4^4 = 160 000.  All operators are built directly from the
> link operators U_ij, L_a, R_a and the fermion operators with explicit
> Jordan-Wigner strings, with no reference to the dressed-site tensors.
>
> Provided checks:
>   * [G_a(x), H] = 0 for every site x and colour a  (gauge invariance of H)
>   * the kernel of sum_{x,a} G_a(x)^2, computed block by block by dense
>     diagonalization (blocks = fixed link spins and site occupations), has
>     dimension 82 with baryon-number split 38/20/20/2/2
>   * P^dag H P on that kernel has the same spectrum as the dressed-site builder
>   * the dressed-site states embedded in the full space are annihilated by
>     every G_a(x), are orthonormal, and reproduce the builder's matrix
>     elements one by one (this tests the contraction formula, JW signs and
>     phases, not only the spectrum).
>
> Symbols: G_a(x) = Gauss-law generator at site x, P = isometry from the
> physical (kernel) space into the redundant space, H = Hamiltonian of
> hamiltonian.py.

## Uses

[[skqd.basis]] · [[skqd.fermions]] · [[skqd.hamiltonian]] · [[skqd.lattice]] · [[skqd.su2]]

## Public names

`FullSpace`

## Concepts

[[Gauss's law]] · [[Link truncation (j_max)]] · [[Staggered fermions]] · [[Intertwiner (dressed-site) basis]] · [[Baryon-number sectors]] · [[Jordan-Wigner mapping]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Exact diagonalization]] · [[Gate-and-evidence discipline]]

## Checked by gates

[[skqd gate E1]]
