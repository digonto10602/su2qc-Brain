---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/hpc.py"
lines: 115
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.hpc

Module of [[su2qc-skqd]] · `src/skqd/hpc.py` · 115 lines

## What it does (from the module docstring)

> CI / Slurm / GPU-telemetry helpers shared by the gate scripts that may run on Perlmutter.
>
> These four functions were written for gate L4 (`scripts/laptop_L4_aer_noise.py`) and are moved
> here unchanged so that gate S3 (`scripts/s3_device_model.py`) uses the SAME detection, the same
> Slurm fallbacks and the same telemetry parser rather than a copy that can drift.  L4 imports them
> back under their original names, so its behaviour is exactly what it was.
>
> Nothing here imports qiskit (the CI runs qiskit 1.4.3, the laptop 2.5.2), and nothing here reads
> or writes a validation file: the caller decides what to record.
>
> Reference: the owner's engine and HPC policy in RUNBOOK.md, "Engine and HPC policy for Perlmutter
> runs" -- every GPU job records wall time, per-phase timings, GPUs and tasks used, seconds per shot,
> peak GPU memory and mean GPU utilization.

## Public names

`ci_context`, `qiskit_versions`, `slurm_layout`, `gpu_telemetry`, `gpu_count`

## Concepts

[[Gate-and-evidence discipline]] · [[Perlmutter job queue]] · [[Qiskit]] · [[NERSC Perlmutter]]

## Checked by gates

[[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate S2_2x4]]
