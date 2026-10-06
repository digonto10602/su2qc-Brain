---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/data/records.py"
lines: 183
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "data"]
---
# su2qc_jepa.data.records

Module of [[su2qc-jepa]] · `src/su2qc_jepa/data/records.py` · 183 lines

## What it does (from the module docstring)

> Measurement records and the observation estimator shared by all three sources.
>
> A *record* is what a carrier returns for one (state, measurement setting): a
> dictionary of bitstrings -> counts, plus metadata.  The *estimator* turns the
> records of one time point into the observation vector o_t.  Exact states, the
> Aer twin and the hardware all go through the same estimator, which is what
> makes the three sources comparable.
>
> Two carriers are supported:
>
> * ``diagonal``: a Z-basis measurement of a diagonal encoding of the 82-state
>   basis (this is how the exact source and the L12 twin look: every primary
>   observable is a function of the measured configuration).  Records are counts
>   over basis indices.  Flags are leakage flags (zero for the exact source).
> * ``chain``: the Krylov-chain carrier (one-hot encoding of K Krylov vectors).
>   Records are counts over K-bit strings for settings Z and X (optionally Y).
>   Z gives the Krylov populations and the excitation flag; X gives the real
>   parts of the Krylov coherences; together they give every physical observable
>   through O_K = Q_K^T O Q_K (O diagonal in the configuration basis).

## Uses

[[su2qc_jepa.physics.chain]] · [[su2qc_jepa.physics.dynamics]] · [[su2qc_jepa.physics.observables]]

## Used by

`su2qc_jepa.data.trajectories` · `su2qc_jepa.gates.j0_data` · `su2qc_jepa.twin.run`

## Public names

`Record`, `ObservationSpec`, `sample_exact_diagonal`, `estimate_diagonal`, `sample_exact_chain`, `estimate_chain`

## Concepts

[[Krylov subspace and Lanczos]] · [[Leakage-safe data splits]] · [[Krylov-chain carrier]] · [[Noise models and digital twin]] · [[L12 encoding]]
