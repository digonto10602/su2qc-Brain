---
type: "infra"
tags: ["workflow"]
as_of: "2026-10-05"
---
# Perlmutter job queue

**Plain words.** A *pull-based* queue: the laptop writes a numbered job file (`jobs/NNN_*.yaml`) and pushes it to GitHub;
a `scrontab` (Slurm's cron) worker on [[NERSC Perlmutter]] pulls it, runs it with Slurm, resubmits after timeouts or
node failures, and pushes results to a `results` branch. Installation merges with, never overwrites, your other two
scrontab entries. Code: [[su2qc_jepa.jobs]]; skqd uses CI tokens and `.sbatch` files ([[skqd.hpc]]).
