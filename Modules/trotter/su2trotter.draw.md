---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/draw.py"
lines: 129
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.draw

Module of [[su2qc-trotter]] · `src/su2trotter/draw.py` · 129 lines

## What it does (from the module docstring)

> Circuit drawings for the report (Qiskit matplotlib drawer, vector PDF).
>
> Circuits are built in drawing mode (`build(..., macro=True)`), which keeps Margolus Toffolis ("M"),
> relative-phase Toffolis ("R"), exact Toffolis, controlled-H and controlled-Rx as single named gates;
> `Circuit.lowered()` of a drawing-mode circuit reproduces the real circuit gate for gate (checked in
> scripts/make_report.py).  Wire names: L<l>_0 = m' (colour at the link's end), L<l>_1 = m (colour at
> its start), L<l>_2 = j (flux on/off) for links l = 0..3; helper registers keep their code names.

## Uses

[[su2trotter.circuit]]

## Public names

`registers`, `to_qiskit`, `stage_view`, `save_drawing`, `chunks`, `blocks_of`, `inverse_blocks`, `block_view`

## Concepts

[[Qiskit]]
