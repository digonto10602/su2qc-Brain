---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/twin/layout.py"
lines: 77
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "twin"]
---
# su2qc_jepa.twin.layout

Module of [[su2qc-jepa]] · `src/su2qc_jepa/twin/layout.py` · 77 lines

## What it does (from the module docstring)

> Choose the physical line of K qubits for the chain carrier from calibration data.
>
> Score of a path = sum of CZ errors along its edges + sum of readout assignment errors of its
> qubits (both are what the chain carrier is sensitive to).  Simple-path enumeration by DFS
> with a cap, which is fine for K <= 16 on heavy-hex graphs of 127-156 qubits.

## Public names

`edge_errors_from_backend`, `best_line`, `heavy_hex_edges`

## Concepts

[[Krylov-chain carrier]] · [[Readout error and confusion matrix]] · [[Transpilation and CZ count]]
