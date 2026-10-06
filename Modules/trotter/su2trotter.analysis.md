---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/analysis.py"
lines: 72
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.analysis

Module of [[su2qc-trotter]] · `src/su2trotter/analysis.py` · 72 lines

## What it does (from the module docstring)

> Bright-pair structure of B and tools to check a forward basis transform C.
>
> B restricted to the 625 physical states is a direct sum of 41 two-dimensional bright
> blocks g (|A><B| + |B><A|) (g = 1, 1/2, 1/4) plus 543 dark states (B = 0).  A forward
> transform C is good if, for every block, C|A> and C|B> are single computational states
> that differ only in the side qubit, with a real relative phase.  Then
> C exp(i alpha B) C^dag = exp(i alpha g s X_side) on that pair, s = relative sign.

## Uses

[[su2trotter.physics]] · [[su2trotter.sim]]

## Public names

`bright_blocks`, `pair_images`
