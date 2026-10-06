---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/physics.py"
lines: 93
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.physics

Module of [[su2qc-trotter]] · `src/su2trotter/physics.py` · 93 lines

## What it does (from the module docstring)

> Exact reference physics for one SU(2) plaquette at jmax = 1/2.
>
> Conventions follow plan/hamiltonian-gauge-theories-circuits.pdf (Eqs. 23-39):
>
> * one link = 3 qubits (q_m', q_m, q_j) at indices (3l, 3l+1, 3l+2); computational
>   index of a link = 4 j + 2 m + m' with the colour value + <-> 1, - <-> 0;
> * link states |0>, |-->, |-+>, |+->, |++>  ->  codes 000, 100, 101, 110, 111 (j m m');
> * plaquette operator  W = sum_{abcd} U_ab(0) U_bc(1) U^dag_cd(2) U^dag_da(3),
>   B = Re Tr W = (W + W^dag) / 2;
> * H_B = -(2 / (g_s g_t a)) sum_p B_p, so one Trotter step of the plaquette is
>   V = exp(+i alpha B) with alpha = 2 dt / (g_s g_t a).

## Used by

`su2trotter.analysis` · `su2trotter.baseline` · `su2trotter.compare` · `su2trotter.cudaq_backend` · `su2trotter.lean` · `su2trotter.sim` · `su2trotter.trotter`

## Public names

`qmp`, `qm`, `qj`, `truncated_link_U`, `kron_links`, `plaquette_W`, `plaquette_B`, `alpha_of`, `target_unitary`, `physical_to_code`

## Concepts

[[SU(2) lattice gauge theory]] · [[Link truncation (j_max)]] · [[Plaquette and Wilson loop]] · [[Trotter and Strang splitting]]

## Checked by gates

[[trotter gate B1]] · [[trotter gate G22]] · [[trotter gate R1]] · [[trotter gate V1]]
