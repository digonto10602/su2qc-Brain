---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/ml.py"
lines: 102
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.ml

Module of [[su2qc-skqd]] · `src/skqd/ml.py` · 102 lines

## What it does (from the module docstring)

> Minimal gauge-invariant importance model (Step 7.4 of the SKQD manual): a ridge
> regression on hand-built gauge-invariant configuration features, conditioned on
> lambda = (g^2, m, B, Lx), trained leakage-safely (splits by (lambda, lattice),
> never by row; the test coupling is excluded from training on every lattice).
>
> Target: f(b; lambda) ~ log max(|<b|Omega_lambda>|, 1e-6).
> Score usage: ranking configurations of a sector (ML-alone proposal, Step 7.3 iii).
>
> The sixteen features of one configuration b = ({j_l},{n_x},{iota_x}):
>   1 flux x-links, 2 flux y-links, 3 quarks on even sites, 4 holes on odd sites,
>   5 'meson' links (flux link, quark on its even end, hole on its odd end),
>   6 flux loops (plaquettes with four flux links), 7 vertices with two flux ends,
>   8 vertices with three flux ends, 9 sum of intertwiner labels,
>   10 diagonal energy H_bb - H_sea,sea, 11 total flux links, 12 sites with n = 1,
>   13 even sites with n = 2, 14 odd sites with n = 0, 15 flux links with n = 1 at both ends,
>   16 (H_bb - H_sea,sea)^2.
> The design matrix is [F, F / g^2, g^2, 1/g^2, m, 2B, Lx, 1].
>
> Symbols: F = feature matrix, w = ridge weights, alpha = ridge penalty.

## Uses

[[skqd.basis]] · [[skqd.hamiltonian]] · [[skqd.krylov]] · [[skqd.lattice]]

## Public names

`features`, `design`, `RidgeRanker`, `spearman`

## Concepts

[[Gauss's law]] · [[Staggered fermions]] · [[Plaquette and Wilson loop]] · [[Intertwiner (dressed-site) basis]] · [[Baryon-number sectors]] · [[String breaking]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Leakage-safe data splits]] · [[Noise models and digital twin]]

## Checked by gates

[[skqd gate S1]]
