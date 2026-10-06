---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/lean.py"
lines: 140
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.lean

Module of [[su2qc-trotter]] · `src/su2trotter/lean.py` · 140 lines

## What it does (from the module docstring)

> Lean promise-aware plaquette circuit (this work).
>
> Same physics and 12-qubit encoding as the baseline (plan Sec. IV.A), re-engineered for
> T-count and width.  Changes relative to the baseline:
>
> 1. vertex flags q_i = jx AND jy are computed once (Margolus, exact from a clean ancilla)
>    and kept; they control the bright-state Hadamards directly (2 T each);
> 2. domain-wall colours are made pair-invariant with two CNOTs, y ^= jx XOR q = jx AND NOT jy,
>    instead of four relative-phase Toffolis;
> 3. q_i is turned *in place* into a dark-vertex flag by a controlled swap into the unused
>    slot (q=0, x=1) plus one Toffoli that restores pair invariance, so the active flag is a
>    4-input NOR (3 ANDs) instead of 4 error bits + an 8-input NOR (11 ANDs);
> 4. the colour Toffolis are Margolus gates whose single -1 sits on an input that never
>    occurs on the code space (4 T instead of 7 T);
> 5. the three class-controlled Rx rotations are merged into one phase function
>    Theta = th_h*active + (th_1 - th_h)*(active AND u) + (th_q - th_1)*g_q, implemented
>    with exactly four arbitrary-angle Rz (one on the side qubit, three ZZ phases).

## Uses

[[su2trotter.baseline]] · [[su2trotter.circuit]] · [[su2trotter.physics]]

## Used by

`su2trotter.trotter`

## Public names

`Lean`, `build`

## Concepts

[[Plaquette and Wilson loop]] · [[Transpilation and CZ count]] · [[Clifford+T and T-count]]

## Checked by gates

[[trotter gate G22]] · [[trotter gate R1]] · [[trotter gate V1]]
