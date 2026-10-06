---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/jobs.py"
lines: 116
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa"]
---
# su2qc_jepa.jobs

Module of [[su2qc-jepa]] · `src/su2qc_jepa/jobs.py` · 116 lines

## What it does (from the module docstring)

> Job requests for the Perlmutter worker — decisions/004 (queue introduced in decisions/003).
>
> A job is a numbered YAML file `jobs/NNN_<slug>.yaml` on the `main` branch, written on the laptop by
> `scripts/jobs/enqueue.py` and never edited afterwards.  A worker (scripts/worker/worker.py, started by
> `scrontab` on Perlmutter) pulls `main`, runs jobs addressed to it at the
> exact commit named in the file, and pushes status and outputs to the separate `results` branch:
>
>     results/<NNN>/status.json      state, timings, node-hours, output sizes, worker host
>     results/<NNN>/log.txt          last lines of the job's output
>     results/<NNN>/outputs/<path>   the files listed under `outputs:` (e.g. runs/v1_base/...)
>
> The laptop never connects to Perlmutter; the worker never pushes to `main`.
>
> Safety: every command step must be `python scripts/<allowed>.py ...` with the script in
> ALLOWED_SCRIPTS, so a worker only ever runs this repository's own entry points.

## Used by

`su2qc_jepa.localrun` · `su2qc_jepa.repo.artifacts`

## Public names

`retry_resources`, `parse_steps`, `validate_job`

## Concepts

[[Intertwiner (dressed-site) basis]] · [[Numbered artifacts]] · [[Perlmutter job queue]] · [[NERSC Perlmutter]]
