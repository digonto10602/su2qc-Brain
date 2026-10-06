---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/localrun.py"
lines: 340
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa"]
---
# su2qc_jepa.localrun

Module of [[su2qc-jepa]] · `src/su2qc_jepa/localrun.py` · 340 lines

## What it does (from the module docstring)

> Resource-aware, self-healing execution on the laptop (decisions/004).
>
> The laptop (64 GB RAM, 6-core i7-8750H, GTX 1060 Max-Q not used) is shared with other Claude sessions, so
> every computation from this project goes through `scripts/run.py`, which uses this module to:
>
> 1. **classify** the command: heavy (estimated above `heavy_minutes` at the granted threads, or asks for a GPU)
>    → always sent to Perlmutter through the job queue; light → may run here;
> 2. **admit** it only if the machine has room *now*: MemAvailable minus the request stays above a reserve kept
>    for other programs, and the 1-minute load plus the requested threads leaves free cores; only one su2qc
>    computation at a time across all sessions (a lock file).  If there is no room it waits (bounded), then
>    sends the job to Perlmutter if it can be queued;
> 3. **run it capped**: lowest CPU/I/O priority, thread caps for every math library, a memory ceiling (cgroup via
>    `systemd-run --user --scope` when available, otherwise an address-space limit), a wall-clock limit, and
>    `oom_score_adj = 1000` so that under memory pressure the kernel kills this job, never another session;
> 4. **heal**: a resource failure (memory kill, address-space exhaustion, timeout) is retried once with a larger
>    memory ceiling if the machine has room, otherwise the job is sent to Perlmutter; a program error (an
>    ordinary exception) is not retried — it is a bug and is reported with the log tail.
>
> Every attempt is appended to `.local_runs/ledger.jsonl` (git-ignored) with its probe, limits and outcome.

## Uses

[[su2qc_jepa.compute]] · [[su2qc_jepa.jobs]]

## Public names

`Probe`, `probe`, `Policy`, `load_policy`, `Request`, `estimate_minutes`, `classify`, `is_heavy`, `admit`, `RunResult`, `run_capped`, `is_resource_failure`, `heal_decision`, `ledger_append`

## Concepts

[[Gate-and-evidence discipline]] · [[Perlmutter job queue]] · [[Laptop admission-controlled runner]] · [[NERSC Perlmutter]] · [[Laptop (Dell G7)]]
