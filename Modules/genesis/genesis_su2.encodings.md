---
type: "module"
package: "genesis-su2-lgt"
file: "src/genesis_su2/encodings.py"
lines: 307
generated: True
as_of: "2026-10-06"
tags: ["module", "genesis"]
---
# genesis_su2.encodings

Module of [[genesis-su2-lgt]] · `src/genesis_su2/encodings.py` · 307 lines

## What it does (from the module docstring)

> Small, dense SU(2) link-encoding references for G7 validation.
>
> These are validation-scale constructions, not production lattice backends.
> The electric basis uses truncated Peter-Weyl states ``|j,m,n>``. The quantum
> link model uses four fermionic rishon modes at fixed total occupation two,
> following the non-commuting-link construction of Chandrasekharan and Wiese.
> Both expose the same link/Gauss/projector surface and keep boundary defects
> visible.

## Public names

`EncodingMetadata`, `LinkEncoding`, `ElectricRepresentationEncoding`, `QuantumLinkEncoding`

## Concepts

[[SU(2) lattice gauge theory]] · [[Gauss's law]] · [[Link truncation (j_max)]] · [[Staggered fermions]] · [[Electric basis]] · [[Quantum link (rishon) encoding]]

## Checked by gates

[[genesis gate G7.2-G7.4]]
