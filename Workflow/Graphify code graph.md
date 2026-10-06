---
type: "infra"
tags: ["workflow"]
aliases: ["Graphify", "graphify"]
as_of: "2026-10-05"
---
# Graphify code graph

**Plain words.** Graphify (`pip install graphifyy`) parses a repository locally (no AI calls) into a graph of files,
classes, functions and imports. Coding agents query it (`graphify explain`, `graphify affected`) before editing, so
they never change code they have not mapped. Rebuilt every session and freshness-checked in CI in all three packages.
su2qc-jepa's graph: 842 nodes, 1 615 edges at bootstrap. Code: [[su2qc_jepa.repo.graph]].
