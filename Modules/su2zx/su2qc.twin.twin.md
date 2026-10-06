---
type: "module"
package: "SU2ZX"
file: "runs/section8_v0.5.0_20260907T0628Z/src/su2qc/twin/twin.py"
lines: 265
generated: True
as_of: "2026-10-06"
tags: ["module", "su2zx"]
---
# su2qc.twin.twin

Module of [[SU2ZX]] · `runs/section8_v0.5.0_20260907T0628Z/src/su2qc/twin/twin.py` · 265 lines

## What it does (from the module docstring)

> Noise-model twin: FakeTorino (or a real backend's properties) via
> AerSimulator.from_backend, with leakage post-selection and observables.
>
>   twin_backend(seed)              -> AerSimulator noise twin
>   run_counts(isa_circs, shots, seed, backend) -> list of counts dicts (physical
>         bit order already mapped back to LOGICAL q11..q0 strings via the
>         circuit's final layout, so l12.decode applies directly); per-repeat
>         seeds are spawned from `seed` and reported by run_counts_meta()
>   run_counts_meta()               -> {base_seed, shots, n_repeats, seeds, ...}
>         for the last run_counts call (also module-level LAST_SEEDS)
>   postselect(counts)              -> (kept_counts, yield_fraction)
>   observables(kept_counts)        -> dict of P_surv, P_meson, P_BBbar, P_other,
>         E2_l (4), n_v (4), from decoded labels (all Z-basis, diagonal)
>   bootstrap(counts_list, fn, n_boot, seed) -> mean, 2sigma per observable

## Uses

[[su2qc.conventions]] · [[su2qc.encodings.l12]]

## Used by

`su2qc.compile.run_g4`

## Public names

`twin_backend`, `add_measurements`, `spawn_seeds`, `run_counts`, `run_counts_meta`, `postselect`, `observables`, `channel_weights`, `undecodable_weight`, `channel_closure_residual`, `matched_subtraction`, `physical_yield`, `bootstrap`

## Concepts

[[String breaking]] · [[Codewords and the Gauss-law decoder]] · [[Leakage-safe data splits]] · [[Clean-shot fraction]] · [[Noise models and digital twin]] · [[L12 encoding]]
