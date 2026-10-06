---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/gates/j2_forecast.py"
lines: 46
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "gates"]
---
# su2qc_jepa.gates.j2_forecast

Module of [[su2qc-jepa]] · `src/su2qc_jepa/gates/j2_forecast.py` · 46 lines

## What it does (from the module docstring)

> Gate J2 - forecasting on held-out couplings versus baselines (from runs/<name>/forecast_eval.json).
>
> eval layout: {"mae": {family: {model: {"+4": {target: mae}, "+8": {...}}}}, "targets": [...], ...}
> Families: "onfam" (held-out g_E) and "strong" (held-out masses near the resonance).  Each family
> is gated separately; the gate passes when every family passes its rows.

## Uses

[[su2qc_jepa.gates.ledger]]

## Public names

`run_j2`

## Concepts

[[Leakage-safe data splits]] · [[Gate-and-evidence discipline]]

## Checked by gates

[[jepa gate J2]]
