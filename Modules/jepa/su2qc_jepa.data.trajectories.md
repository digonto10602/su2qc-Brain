---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/data/trajectories.py"
lines: 264
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "data"]
---
# su2qc_jepa.data.trajectories

Module of [[su2qc-jepa]] · `src/su2qc_jepa/data/trajectories.py` · 264 lines

## What it does (from the module docstring)

> Trajectory generator: exact dynamics + emulated finite-shot observations + split manifest.
>
> A trajectory is an initial gauge-invariant state followed by n actions.  An action
> is one time step of duration dt at couplings (cM, cH, cB) (cE = 1 in units of g_E);
> a mass quench is a trajectory whose cM changes at a given step.  Every time point
> carries the clean exact observables (the JEPA target) and a finite-shot
> observation (the JEPA context), built through the same estimator used for twin
> and hardware records (see records.py).
>
> Two coupling *families* are scanned, because the physics-setup measurements of
> 1 Oct 2026 showed that the mass dependence of the P-A window is weak while the
> strong-coupling resonance at mu* = 3/8 is sharp:
>
> * family "onfam"  - on-family points (cH, cB) = (1/(2 g_E), -1/(4 g_E^2)) with g_E scanned;
>                     held out by g_E (the dynamics depend strongly on g_E, weakly on mu).
> * family "strong" - strong-coupling points cH = |cB| = 0.02 (the P-S regime) with mu scanned
>                     around the resonance; held out by mu.
>
> Splits are by rule, never by row.  The manifest records every parameter and a
> checksum of the arrays.

## Uses

[[su2qc_jepa.data.records]] · [[su2qc_jepa.physics.conventions]] · [[su2qc_jepa.physics.dynamics]] · [[su2qc_jepa.physics.observables]] · [[su2qc_jepa.physics.plaquette]]

## Public names

`FamilyConfig`, `DatasetConfig`, `dataset_fingerprint`, `generate_dataset`, `load_dataset`

## Concepts

[[Gauss's law]] · [[JEPA world model]] · [[Leakage-safe data splits]] · [[Noise models and digital twin]]
