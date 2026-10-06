---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/conventions.py"
lines: 101
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx"]
---
# su2qc.conventions

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/conventions.py` · 101 lines

## What it does (from the module docstring)

> FROZEN conventions for the SU(2) single-plaquette patch with dynamical matter.
>
> Frozen at G0 of run section8_v0.5.0_20260907T0628Z. DO NOT EDIT.
> Both Hamiltonian routes, all encodings, circuits, and analysis import from here
> and ONLY from here. Any objection goes to physics/conventions_objection_*.md.
>
> Model (Section 5.1 of the v0.5.0 prompt):
>   Lattice units a = 1. One square plaquette, open boundaries.
>   H = (g^2/2) sum_l E_l^2
>     + m sum_v (-1)^{x_v+y_v} psi\dagger_v psi_v
>     + (1/2) sum_l ( eta_l psi\dagger_{s(l)} U_l psi_{t(l)} + h.c. )
>     - (1/(2 g^2)) Tr( U_box + U_box\dagger )
>   U_box = U_l1 U_l2 U_l3\dagger U_l4\dagger   (counter-clockwise v1->v2->v3->v4->v1)
>   E^2 = j(j+1) per link. Truncation j in {0, 1/2} (hardcore gluon); j_max = 1
>   is built too for the truncation-error statement.

## Used by

`su2qc.dynamics.engine` · `su2qc.dynamics.scan` · `su2qc.ham.compare` · `su2qc.ham.limits` · `su2qc.ham.route_gausskernel` · `su2qc.ham.route_spinnet` · `su2qc.twin.twin`

## Public names

`parity`, `eta`, `charge`, `casimir`, `coupling_electric`, `coupling_magnetic`, `tree_level_resonance`

## Concepts

[[SU(2) lattice gauge theory]] · [[Link truncation (j_max)]] · [[Plaquette and Wilson loop]]

## Checked by gates

[[su2zx gate S8-G1]]
