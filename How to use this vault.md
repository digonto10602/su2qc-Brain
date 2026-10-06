---
type: "hub"
tags: ["hub", "howto"]
as_of: "2026-10-06"
---
# How to use this vault

## Opening it

1. The vault lives at `~/Projects/su2qc-Brain`, next to the repositories it is built from.
2. In Obsidian: *Open folder as vault* → choose the `su2qc-Brain` folder.
3. Open [[00 SU2QC Map]]. Press the graph icon (or `Ctrl/Cmd+G`) for **Graph view**.

Graph view colours are preset (in `.obsidian/graph.json`): packages, modules, gates, concepts, hardware, papers and
results each get their own colour. Useful graph filters (type them in the graph's search box):

- `tag:#package` — only the packages
- `path:Modules/skqd` — only the su2qc-skqd code
- `tag:#gate -tag:#pass` — gates that have not passed
- `[[Gauss's law]]` — everything that mentions Gauss's law

**Local graph** (right-click a note → *Open local graph*) shows one note and its neighbours; this is often more
readable than the full graph.

## What is generated and what is hand-written

- `Modules/` and `Gates/` are **generated** from the repositories by `_tools/build_vault.py` (module docstrings,
  import statements, gate tables). Do not edit them by hand; re-run the builder instead.
- Everything else (packages, concepts, hardware, papers, results, decisions, hubs) is **hand-written** and safe to edit.

## Refreshing after the repositories change

```bash
cd ~/Projects/su2qc-Brain/_tools
python build_vault.py --repos ~/Projects --overwrite-hand   # reads every su2qc-* repo plus genesis-su2-lgt and the SU2ZX checkout
python export_jsonl.py                       # rebuild _export/su2qc_brain.jsonl
```

A Claude Code session can do this for you: "read `_tools/README.md` and refresh the vault".

## Using it for AI

`_export/su2qc_brain.jsonl` has one JSON record per note (a *JSONL* file: one JSON object per line, the usual
input format for training and retrieval pipelines). Each record has `id`, `title`, `type`, `package`, `status`,
`links` (the notes it points to), `backlinks` and `text`.

- **Retrieval (recommended).** *Retrieval-augmented generation* (RAG) means the model looks up the most relevant
  notes when it answers. Point Claude Code, Hermes or any RAG tool at the vault folder or the JSONL file, and an
  agent starting a new SU2QC session gets the project map, the conventions and the latest gate status in a few
  thousand tokens.
- **Agent memory.** Add a line to a package's `CLAUDE.md`: "read `~/Projects/su2qc-Brain/00 SU2QC Map.md` and the notes it
  links before planning".
- **Fine-tuning (limited).** About 200 notes is far too small to teach a model physics by fine-tuning. It *is*
  enough for an evaluation set (questions whose answers are in the notes) or as a seed for generated
  question–answer pairs. The real training data in these projects are the measurement records and trajectories in
  the repositories themselves (see [[su2qc-jepa]] datasets and [[su2qc-skqd]] `data/hardware/`).
