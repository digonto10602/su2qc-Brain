---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/controls.py"
lines: 97
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.controls

Module of [[su2qc-skqd]] · `src/skqd/controls.py` · 97 lines

## What it does (from the module docstring)

> Classical-support controls at prescribed support size (Step 6 of the SKQD manual).
>
>   (a) CIPSI selected CI: start from the references; iterate {diagonalize on B,
>       score every Hamiltonian neighbour c not in B by |<c|H|psi_R>|^2 / (H_cc - E_R),
>       add the top batch} until |B| reaches the target.
>   (b) BFS neighbour growth, truncated at random when the next layer overshoots.
>   (c) random configurations of the sector (references always included).
>   (d) oracle: the top-|B| configurations by exact ground-state weight (simulator only).
>   (e) ML-alone: the top-|B| configurations by a learned score (ml.py).
>   (f) device-seeded CIPSI: CIPSI growth starting from a device support.
>
> All functions return sorted arrays of full-basis indices of exactly the target size
> (when the sector allows it).
>
> Symbols: B = support, N(B) = Hamiltonian neighbours, psi_R = Ritz vector,
> E_R = Ritz value, H_cc = diagonal element.

## Uses

[[skqd.hamiltonian]] · [[skqd.skqd]]

## Used by

`skqd.skqd`

## Public names

`cipsi`, `bfs`, `random_support`, `oracle`, `top_by_score`, `top_by_count`

## Concepts

[[Link truncation (j_max)]] · [[Baryon-number sectors]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Ritz values and certified bounds]] · [[CIPSI and classical support controls]] · [[Exact diagonalization]] · [[Agent routing (planner, executor, reviewer, runner, scribe)]]

## Checked by gates

[[skqd gate S1]]
