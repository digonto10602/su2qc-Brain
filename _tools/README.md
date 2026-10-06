# _tools — keeping the SU2QC Brain current

| file | job |
|---|---|
| `build_vault.py` | reads the repositories and regenerates `Modules/`, `Gates/`, `Indexes/`, `SU2QC Map.canvas`, `.obsidian/graph.json`; writes hand-written notes only if they are missing (`--overwrite-hand` to force) |
| `content_packages.py` | hand-written hub, package, cross-package and result notes (source of truth for first build) |
| `content_concepts.py` | hand-written concept, method, hardware, workflow, paper and decision notes, plus the keyword patterns that auto-link modules and gates to concepts |
| `build_canvas.py` | the canvas layout (coordinates are hand-set; gate counts are filled in automatically) |
| `export_jsonl.py` | writes `_export/su2qc_brain.jsonl` (one record per note) and `_export/graph_edges.csv` |
| `last_build.json` | when the vault was built and from which commits |

## Refresh (for you or a Claude Code session)

```bash
# 1. pull the repositories (they must sit side by side in ~/Projects; local folder names that differ from the
#    repository name are mapped in ALT_DIRS in build_vault.py: su2qc-skqd-v0.1.0, SU2ZX_Foundation_Code_Package/SU2ZX)
cd ~/Projects && for r in su2qc-skqd-v0.1.0 su2qc-jepa su2qc-trotter su2qc-qcadvantage genesis-su2-lgt SU2ZX_Foundation_Code_Package/SU2ZX; do git -C $r pull --ff-only; done
# 2. rebuild the generated part of the vault and the export
cd ~/Projects/su2qc-Brain/_tools
python build_vault.py --repos ~/Projects --overwrite-hand   # --overwrite-hand: content_*.py is the source of truth
python export_jsonl.py
```

Only the standard library is needed (Python 3.9+).

## Adding a package

Add it to `PACKAGES` in `build_vault.py` (repo folder → python package folder and a short prefix), write a package
note in `content_packages.py` (or directly in `Packages/` inside Obsidian), add a gate parser if its gate table has a
new format, and add a column to `build_canvas.py`.

## Rule for agents editing this vault

Do not hand-edit `Modules/`, `Gates/` or `Indexes/` — they are overwritten on every build. Hand-written notes are
rewritten from `content_packages.py` / `content_concepts.py` when the build runs with `--overwrite-hand`, so put
lasting edits in those files. Put new knowledge in a
hand-written note (Packages, Concepts, Results, Decisions, Cross-package) and link it with `[[wikilinks]]`. Every
note keeps its YAML header (`type`, `tags`, `as_of`).
