---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/twin/run.py"
lines: 88
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "twin"]
---
# su2qc_jepa.twin.run

Module of [[su2qc-jepa]] · `src/su2qc_jepa/twin/run.py` · 88 lines

## What it does (from the module docstring)

> Twin runner with reproducible, *independent* seeds.
>
> Lesson from the v0.5.0 campaign: Aer seeds shot k of a run with seed_simulator + k, so runs
> seeded with seed + k overlapped in N-1 of N shots and every quoted sigma was void.  Here every
> run gets its own seed from ``numpy.random.SeedSequence(master).spawn(...)``, and the variance
> check (``twin_variance_check``) asserts that repeats are distinct.

## Uses

[[su2qc_jepa.data.records]] · [[su2qc_jepa.physics.chain]]

## Used by

`su2qc_jepa.gates.j0_data`

## Public names

`TwinRunner`, `chain_point_records`, `twin_variance_check`

## Concepts

[[Noise models and digital twin]]
