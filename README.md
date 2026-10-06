# SU2QC Brain

An [Obsidian](https://obsidian.md) vault that maps the SU2QC research packages (SU(2) lattice gauge theory on quantum
computers): what each package does, its code modules, its pass/fail gates, the physics concepts, hardware, papers and
headline results, and how the packages connect.

Packages mapped: `genesis-su2-lgt`, `genesis-su2-zx-observables` (SU2ZX), `su2qc-skqd`, `su2qc-jepa`, `su2qc-trotter`,
`su2qc-paulo-code` (reference circuit), `su2qc-qcadvantage`.

## View it

Clone, then in Obsidian choose *Open folder as vault*. Start at `00 SU2QC Map.md`, open `SU2QC Map.canvas`, or press
`Ctrl/Cmd+G` for the graph view. Details: `How to use this vault.md`.

## Rebuild it

`Modules/`, `Gates/` and `Indexes/` are generated from the repositories by `_tools/build_vault.py`; the hand-written
notes come from `_tools/content_packages.py` and `_tools/content_concepts.py`. See `_tools/README.md`.
`_export/su2qc_brain.jsonl` has one JSON record per note, for retrieval or AI pipelines.
