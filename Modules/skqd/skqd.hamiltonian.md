---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/hamiltonian.py"
lines: 316
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.hamiltonian

Module of [[su2qc-skqd]] · `src/skqd/hamiltonian.py` · 316 lines

## What it does (from the module docstring)

> Dressed-site Hamiltonian builder — Step 3 / Algorithm 2 of the SKQD manual.
>
> H = -1/2 sum_{l=(x->y)} [ eta_l psi^dag_{x,i} U_ij(l) psi_{y,j} + h.c. ]
>     + m sum_x (-1)^{x1+x2} n_x
>     + g^2/2 sum_l E_l^2
>     - 1/(2 g^2) sum_P (W_P + W_P^dag),
> W_P = sum_{ijkl} U_ij(l_b) U_jk(l_r) (U_lk(l_t))^dag (U_il(l_l))^dag  (counter-clockwise
> from the lower-left corner), links truncated at jmax in the electric basis.
>
> Matrix elements between dressed-site states are obtained by local contraction
> (eq. 4 of the manual): the local singlet tensors of the touched vertices, the
> link operator blocks, the site Fock operators, and the Jordan-Wigner sign
> s_JW = prod_{x<z<y} (-1)^{n_z} for a hopping term psi^dag_x psi_y with the
> intra-site signs absorbed into F_x = psi^loc_dag_{x,i} P_x and F_y = psi^loc_{y,j}
> (x < y, which always holds for the ladder's link orientation).
>
> The builder returns the term matrices separately:
>     terms['mass']      : diag  sum_x (-1)^{x1+x2} n_x
>     terms['electric']  : diag  sum_l j_l (j_l + 1)
>     terms['hop'][l]    : -(eta_l/2) sum_ij psi^dag_x U_ij psi_y + h.c.   (one per link)
>     terms['plaq'][P]   : W_P + W_P^dag                                    (one per plaquette)
> and  H(g^2, m) = m*mass + (g^2/2)*electric + sum_l hop[l] - 1/(2 g^2) sum_P plaq[P].
>
> Symbols: g^2 = gauge coupling, m = staggered quark mass, eta_l = staggered
> hopping phase, E_l^2 = j_l(j_l+1) electric Casimir, n_x = quark occupation.

## Uses

[[skqd.basis]] · [[skqd.fermions]] · [[skqd.su2]] · [[skqd.vertex]]

## Used by

`skqd.controls` · `skqd.exact` · `skqd.fullspace` · `skqd.krylov` · `skqd.ml`

## Public names

`Terms`, `HamiltonianBuilder`, `neighbours`

## Concepts

[[Link truncation (j_max)]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Intertwiner (dressed-site) basis]] · [[Electric basis]] · [[Jordan-Wigner mapping]] · [[Sample-based Krylov quantum diagonalization (SKQD)]]

## Checked by gates

[[skqd gate E1]]
