---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/vertex.py"
lines: 112
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.vertex

Module of [[su2qc-skqd]] · `src/skqd/vertex.py` · 112 lines

## What it does (from the module docstring)

> Local singlet (intertwiner) tensors of one dressed vertex — Algorithm 1 of the
> SKQD manual (VERTEXTENSORS).
>
> A vertex owns one index per link end (mL of outgoing links, mR of incoming
> links, canonical order = link index order), its matter Fock state, and
> optionally a static spin-1/2.  Its physical states are the singlets of the
> Gauss-law generators
>     G_a = sum_{out} L_a + sum_{in} R_a + Q_a|_n (+ sigma_a/2 for a static charge),
> i.e. the kernel of sum_a G_a^2 restricted to the occupation-n block.
>
> When the kernel has dimension > 1 the states are labelled by the fusion-tree
> (intertwiner) label iota: the simultaneous eigenbasis of the cumulative
> Casimirs C_k = (G^{(1)} + ... + G^{(k)})^2 over the constituents in canonical
> order (link ends, then matter, then static charge), combined into the single
> operator sum_k 7^{k-2} C_k (k = 2 .. K'-1) as in the manual.  For an uncharged
> interior vertex with three flux ends and n = 1, iota in {0, 1} is the
> intermediate spin J_12 in {0, 1} of the first two link ends.
>
> Symbols: j_e = spin of end e, role_e in {out, in}, n = quark occupation,
> d_e = 2 j_e + 1, K = number of ends, K' = number of constituents.

## Uses

[[skqd.fermions]] · [[skqd.su2]]

## Used by

`skqd.basis` · `skqd.hamiltonian`

## Public names

`vertex_tensors`, `kernel_dim`

## Concepts

[[Gauss's law]] · [[Staggered fermions]] · [[Intertwiner (dressed-site) basis]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Noise models and digital twin]]

## Checked by gates

[[skqd gate E2]]
