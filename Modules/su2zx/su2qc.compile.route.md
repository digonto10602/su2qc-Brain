---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/compile/route.py"
lines: 127
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx", "compile"]
---
# su2qc.compile.route

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/compile/route.py` · 127 lines

## What it does (from the module docstring)

> Phase 4: route logical L12 circuits to a Heron-class target and verify.
>
> route(circ, backend, opt=3, seed=7) -> (isa_circ, layout_info)
> routed_equivalence(logical, isa) -> 1 - |<psi_routed|psi_logical>| including
>       the final layout permutation (statevector on the 12 logical qubits).
> routed_resources(isa) -> dict(n_2q, depth_2q, depth)
> pyzx_tp(circ) -> circuit after the monograph's topology-preserving PyZX pass
>       (reused from the repo's src/su2zx/compiler_study.py if importable).

## Uses

[[su2qc.circuits.strang_l12]]

## Used by

`su2qc.compile.run_g4`

## Public names

`fake_heron`, `route`, `routed_resources`, `routed_equivalence`, `pyzx_pass`, `state_equivalence`

## Concepts

[[Transpilation and CZ count]] · [[ZX-calculus circuit optimization]] · [[L12 encoding]]
