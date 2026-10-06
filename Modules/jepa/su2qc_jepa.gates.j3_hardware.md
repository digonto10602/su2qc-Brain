---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/gates/j3_hardware.py"
lines: 78
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "gates"]
---
# su2qc_jepa.gates.j3_hardware

Module of [[su2qc-jepa]] · `src/su2qc_jepa/gates/j3_hardware.py` · 78 lines

## What it does (from the module docstring)

> Gate J3 - label-free hardware error signals (twin rehearsal or real hardware).
>
> Input: residual_eval.json from scripts/residual_eval.py, one entry per (point, shots level) with the
> signals jepa_twin, jepa_self, jepa_t0, raw_twin, flag_rate and the scoring label exact_error.
>
> Pass logic (preregistered):
>   * Spearman(jepa_twin, exact_error) >= residual_spearman_min at the low-shot level (default 512)
>   * non-inferiority: Spearman(jepa_twin) >= Spearman(raw_twin) - noninferiority_margin at the low-shot level
>   * AUROC of jepa_twin for separating arm A (nominal) from arm B (degraded) >= auroc_min at full shots
>   * every baseline Spearman is reported (report-only rows)

## Uses

[[su2qc_jepa.gates.ledger]]

## Public names

`spearman`, `auroc`, `run_j3`

## Concepts

[[Noise models and digital twin]] · [[Gate-and-evidence discipline]] · [[Preregistration]]

## Checked by gates

[[jepa gate J3]]
