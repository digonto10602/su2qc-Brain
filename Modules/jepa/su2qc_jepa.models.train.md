---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/models/train.py"
lines: 265
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "models"]
---
# su2qc_jepa.models.train

Module of [[su2qc-jepa]] · `src/su2qc_jepa/models/train.py` · 265 lines

## What it does (from the module docstring)

> Training loop, probes, forecasting evaluation and baselines for Gauge-JEPA-P v2.
>
> The forecasting task (gate J2): from the noisy observation at context step c (and the known
> action sequence), predict the clean observables at later steps.  JEPA predicts latents and a
> linear probe (ridge, fit on the training split) reads observables out of them.  Baselines
> see exactly the same inputs: ridge regression, an autoregressive one-step model in
> observation space rolled out, and a direct supervised MLP.

## Uses

[[su2qc_jepa.models.jepa]]

## Used by

`su2qc_jepa.gates.j1_training`

## Public names

`TrainConfig`, `prepare_tensors`, `train_jepa`, `diagnostics`, `r2_score`, `fit_probe`, `forecast_jepa`, `baseline_ridge`, `baseline_autoregressive`, `baseline_supervised_mlp`

## Concepts

[[JEPA world model]] · [[Gate-and-evidence discipline]]
