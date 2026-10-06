---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/twin/noise.py"
lines: 65
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "twin"]
---
# su2qc_jepa.twin.noise

Module of [[su2qc-jepa]] · `src/su2qc_jepa/twin/noise.py` · 65 lines

## What it does (from the module docstring)

> Noise models for the Aer twin.
>
> Two sources: a synthetic Heron-like model (for development and for the J0/J3 simulator-only
> checks) and a calibration snapshot of a real IBM backend (``NoiseModel.from_backend`` when a
> backend object is available, or a saved properties JSON).  The twin is *calibrated*, not
> *trusted*: the hardware residual (gate J3) is precisely a measurement of how far the twin is
> from the device.

## Used by

`su2qc_jepa.gates.j0_data`

## Public names

`HeronLike`, `heron_like_noise_model`, `noise_model_from_backend`, `save_noise_summary`

## Concepts

[[Noise models and digital twin]] · [[Gate-and-evidence discipline]]
