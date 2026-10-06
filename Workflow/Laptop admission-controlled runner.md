---
type: "infra"
tags: ["workflow"]
as_of: "2026-10-05"
---
# Laptop admission-controlled runner

**Plain words.** Every computation goes through `scripts/run.py`. A job runs on the laptop only if there is room
(16 GB RAM and 2 CPUs always left for other sessions, one su2qc job at a time), with hard caps and
`oom_score_adj = 1000` so the kernel kills *this* job first under memory pressure. Too big → queued to Perlmutter.
Code: [[su2qc_jepa.localrun]], [[su2qc_jepa.compute]]. Decision: [[Decision - jepa 004 laptop and Perlmutter only]].
