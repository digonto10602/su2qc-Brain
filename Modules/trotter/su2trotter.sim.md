---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/sim.py"
lines: 104
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.sim

Module of [[su2qc-trotter]] · `src/su2trotter/sim.py` · 104 lines

## What it does (from the module docstring)

> Exact sparse state-vector simulator for :class:`Circuit` gate lists.
>
> The plaquette circuits are almost classical (permutations, a few Hadamards and the
> rotations), so a dictionary {basis index: amplitude} stays small.  This is an
> independent cross-check of the CUDA-Q simulation, and it is fast enough to run all
> 625 encoded basis inputs exhaustively.

## Uses

[[su2trotter.physics]]

## Used by

`su2trotter.analysis` · `su2trotter.compare` · `su2trotter.pipeline`

## Public names

`apply`, `run`, `encoded_block`, `compare_to_target`, `verify`

## Concepts

[[Plaquette and Wilson loop]] · [[CUDA-Q]]

## Checked by gates

[[trotter gate G22]] · [[trotter gate R1]]
