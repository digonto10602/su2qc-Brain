---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/trotter.py"
lines: 59
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.trotter

Module of [[su2qc-trotter]] · `src/su2trotter/trotter.py` · 59 lines

## What it does (from the module docstring)

> Full single-plaquette Trotter step: electric phases + magnetic plaquette circuit.
>
> H = (g_t^2 / 4a) sum_l (T_L^2 + T_R^2)  -  (2 / (g_s g_t a)) Re Tr U_plaquette      (plan Eq. 16)
>
> On the jmax = 1/2 link, T_L^2 + T_R^2 = 3/2 on j = 1/2 and 0 on j = 0 (Eq. 33), so the
> electric factor is one phase gate per link on its j qubit (Eq. 35).  First-order step:
> U(dt) = exp(-i H_E dt) exp(-i H_B dt).

## Uses

[[su2trotter.circuit]] · [[su2trotter.lean]] · [[su2trotter.physics]]

## Public names

`electric_angle`, `electric_diag`, `hamiltonian`, `exact_trotter_step`, `exact_evolution`, `build_step`

## Concepts

[[Link truncation (j_max)]] · [[Plaquette and Wilson loop]] · [[Electric basis]] · [[Trotter and Strang splitting]]

## Checked by gates

[[trotter gate B1]] · [[trotter gate G22]] · [[trotter gate R1]]
