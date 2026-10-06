---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/synth.py"
lines: 95
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.synth

Module of [[su2qc-trotter]] · `src/su2trotter/synth.py` · 95 lines

## What it does (from the module docstring)

> Clifford+T synthesis of arbitrary-angle rz gates (Ross-Selinger gridsynth via pygridsynth).
>
> CUDA-Q has no rotation synthesiser, so this is the only non-CUDA-Q step of the
> compilation.  Each rz(theta) is replaced by an exact Clifford+T word U with
> ||U - e^{i phi} rz(theta)||_2 <= eps.  Global phases (gridsynth's W = e^{i pi/4}) are
> dropped: in our circuits every rz is an uncontrolled single-qubit gate.

## Uses

[[su2trotter.circuit]]

## Used by

`su2trotter.pipeline`

## Public names

`gridsynth_word`, `word_matrix`, `rz_matrix`, `phase_distance`, `clifford_t_rz`, `word_to_gates`, `synthesize`

## Concepts

[[CUDA-Q]] · [[Clifford+T and T-count]]
