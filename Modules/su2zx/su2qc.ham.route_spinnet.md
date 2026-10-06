---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/route_spinnet.py"
lines: 776
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "ham"]
---
# su2qc.ham.route_spinnet

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/ham/route_spinnet.py` · 776 lines

## What it does (from the module docstring)

> Route 1: analytic spin-network / dressed-site Hamiltonian for SU(2) single plaquette
> with dynamical two-color staggered fermions.
>
> Basis: ((j1,j2,j3,j4), (n1,n2,n3,n4), tag) where:
>   j_l in {0, 1/2} (jmax=0.5) or {0, 1/2, 1} (jmax=1) as floats
>   n_v in {0,1,2} with gauge-invariant constraints per vertex
>   tag = 0 (always for 2-valent vertices)
>
> Gauge invariance at each 2-valent vertex with incident link spins (j_a, j_b) and matter n_v:
>   - if j_a == j_b:     n_v in {0, 2}  (vacuum or baryon)
>   - if |j_a - j_b| == 1/2: n_v = 1  (doublet)
>   - if |j_a - j_b| == 1:     NOT allowed (projected out, only jmax=1)
>
> Hamiltonian: H = H_elec + H_mass + H_hop + H_mag
>
> eta = (+1, -1, +1, +1) per link l1..l4.
> Staggered vacuum: n_vac = (0,2,0,2).  Vertices v1..v4 at (0,0),(1,0),(1,1),(0,1).
> Links: l1:v1->v2, l2:v2->v3, l3:v4->v3, l4:v1->v4.
> Plaquette: U_box = U_l1 U_l2 U_l3^dag U_l4^dag (counter-clockwise v1->v2->v3->v4->v1).

## Uses

[[su2qc.conventions]]

## Used by

`su2qc.dynamics.engine` · `su2qc.dynamics.scan` · `su2qc.encodings.l12` · `su2qc.ham.compare` · `su2qc.ham.limits`

## Public names

`enumerate_basis`, `build_hamiltonian`, `build_hamiltonian_no_magnetic`, `number_op`, `total_number`, `casimir_link`, `P_stretched`, `P_short`, `P_surv`, `P_meson`, `P_BBbar`, `charge`, `validate_dimensions`, `validate_hermiticity`, `validate_commutator`, `pure_electric_check`

## Concepts

[[SU(2) lattice gauge theory]] · [[Gauss's law]] · [[Link truncation (j_max)]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Intertwiner (dressed-site) basis]] · [[Baryon-number sectors]]

## Checked by gates

[[su2zx gate S8-G1]]
