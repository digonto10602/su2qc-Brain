---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/su2.py"
lines: 180
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.su2

Module of [[su2qc-skqd]] · `src/skqd/su2.py` · 180 lines

## What it does (from the module docstring)

> SU(2) building blocks: spin matrices, Clebsch-Gordan coefficients, and the
> truncated electric-basis link operators.
>
> Conventions (fixed here and verified numerically by tests/test_su2.py and by
> gate E1, which checks [G_a(x), H] = 0 in the redundant basis):
>
> * Link Hilbert space  H_link = (+)_{j <= jmax}  span{ |j, mL, mR> },
>   dimension  sum_j (2j+1)^2  (= 5 for jmax = 1/2, 14 for jmax = 1).
>   The state |j, mL, mR> is the wavefunction  sqrt(2j+1) D^j_{mL mR}(U).
> * U_{ij}  (i, j in {+1/2, -1/2} colour indices) is multiplication by
>   D^{1/2}_{ij}(U), projected to j <= jmax:
>       <j' mL' mR'| U_ij |j mL mR> = sqrt((2j+1)/(2j'+1))
>                                     * C(1/2 i, j mL | j' mL') * C(1/2 j, j mR | j' mR')
>   (Clebsch-Gordan series of D^{1/2} D^j).
> * Left generator  L_a = -J_a^T  acting on the mL index, right generator
>   R_a = +J_a acting on the mR index (as matrices on the ket coefficients).
>   They satisfy exactly, also in the truncated space,
>       [L_a, U_ij] = -(T_a U)_ij ,   [R_a, U_ij] = +(U T_a)_ij ,   T_a = sigma_a/2,
>   and  sum_a L_a^2 = sum_a R_a^2 = j(j+1)  (the electric energy E^2).
> * Matter transforms with Q_a = psi^dag (sigma_a/2) psi, so that
>   psi^dag_x U(x->y) psi_y is gauge invariant with
>   G_a(x) = sum_{out} L_a + sum_{in} R_a + Q_a(x) (+ sigma_a/2 for a static charge).
>
> Every symbol: j = link spin (0 or 1/2 for jmax=1/2), mL/mR = magnetic quantum
> numbers of the left (start-site) and right (end-site) index of the link,
> i,j = colour indices of the 2x2 matrix U, T_a = SU(2) generators in the
> fundamental representation.

## Used by

`skqd.fermions` · `skqd.fullspace` · `skqd.hamiltonian` · `skqd.vertex`

## Public names

`spin_matrices`, `m_values`, `clebsch_gordan`, `LinkSpace`

## Concepts

[[SU(2) lattice gauge theory]] · [[Gauss's law]] · [[Link truncation (j_max)]] · [[Electric basis]] · [[Clebsch-Gordan coefficients]] · [[Gate-and-evidence discipline]]

## Checked by gates

[[skqd gate E1]]
