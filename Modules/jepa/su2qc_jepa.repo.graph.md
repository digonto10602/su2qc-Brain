---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/repo/graph.py"
lines: 59
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "repo"]
---
# su2qc_jepa.repo.graph

Module of [[su2qc-jepa]] · `src/su2qc_jepa/repo/graph.py` · 59 lines

## What it does (from the module docstring)

> Helpers around the Graphify code graph (graphify-out/graph.json).
>
> Graphify (PyPI package `graphifyy`, command `graphify`) parses the repository locally with
> tree-sitter — no LLM, no API key in code-only mode — into a graph of files, classes, functions,
> imports, calls and Markdown headings, clusters it into communities and writes
> `graphify-out/graph.json` and `graphify-out/GRAPH_REPORT.md`.  This module only *reads* those
> files: it counts nodes/edges/communities, lists the most connected nodes, and decides whether a
> committed graph is structurally identical to a fresh rebuild (ignoring the commit stamp and the
> community assignment, which are not structure).

## Public names

`load_graph`, `graph_stats`, `structure_signature`, `same_structure`

## Concepts

[[Graphify code graph]]
