---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/optimize.py"
lines: 187
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.optimize

Module of [[su2qc-trotter]] · `src/su2trotter/optimize.py` · 187 lines

## What it does (from the module docstring)

> Light, provably-safe peephole optimisation for Clifford+T(+rz) gate lists.
>
> Passes (all exact up to a global phase):
>
> 1. ``push_paulis``: X and Z gates are commuted to the end of the circuit (Pauli frame),
>    rewriting the gates they pass (T <-> Tdg, S <-> Sdg, rz(t) -> rz(-t) under X; X <-> Z
>    under H; the usual CX/CZ propagation rules).  The residual frame is emitted at the end.
> 2. ``cancel_merge``: commutation-aware cancellation of H.H, CX.CX, CZ.CZ and merging of
>    diagonal single-qubit phases (z, s, sdg, t, tdg, rz) on the same wire.
> 3. ``to_basis``: rewrite into the target basis {h, s, sdg, t, tdg, cx} (the basis used in
>    the plan, Eq. 39): cz -> h cx h, x -> h s s h, z -> s s.

## Uses

[[su2trotter.circuit]]

## Used by

`su2trotter.pipeline`

## Public names

`push_paulis`, `cancel_merge`, `to_basis`, `optimize`, `finalize`

## Concepts

[[Transpilation and CZ count]] · [[Clifford+T and T-count]]
