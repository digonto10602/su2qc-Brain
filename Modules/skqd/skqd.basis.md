---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/basis.py"
lines: 86
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.basis

Module of [[su2qc-skqd]] · `src/skqd/basis.py` · 86 lines

## What it does (from the module docstring)

> Gauge-invariant configuration basis  |b> = |{j_l}, {n_x}, {iota_x}>  of the
> dressed-site construction (Step 2 of the SKQD manual), with baryon-number
> sectors.
>
> A label b is stored as (j2, n, iota): tuples of ints with j2 = 2 j_l per link,
> n = occupation per site, iota = intertwiner index per site.  The basis is the
> list of all labels for which every vertex has a non-empty singlet space, one
> state per choice of the intertwiner indices.
>
> Baryon number  B = 1/2 sum_x (n_x - n^vac_x),  n^vac_x = 0 on even sites and
> 2 on odd sites.  We store 2B as an int.

## Uses

[[skqd.lattice]] · [[skqd.vertex]]

## Used by

`skqd.codec` · `skqd.exact` · `skqd.fullspace` · `skqd.hamiltonian` · `skqd.krylov` · `skqd.ml`

## Public names

`Basis`, `enumerate_basis`, `count_labels_without_intertwiner`

## Concepts

[[Intertwiner (dressed-site) basis]] · [[Baryon-number sectors]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Noise models and digital twin]]

## Checked by gates

[[skqd gate E1]] · [[skqd gate E2]]
