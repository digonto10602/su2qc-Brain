---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/hardware/ibm.py"
lines: 202
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "hardware"]
---
# su2qc_jepa.hardware.ibm

Module of [[su2qc-jepa]] · `src/su2qc_jepa/hardware/ibm.py` · 202 lines

## What it does (from the module docstring)

> IBM Quantum submission path with a dry-run-first, budget-guarded discipline.
>
> Nothing here talks to a QPU unless ``submit(..., confirm=True)`` is called with an approved
> budget file.  The sequence Claude Code must follow (CLAUDE.md, hardware rules):
>
> 1. ``dry_run``  - transpile to the backend's ISA on the chosen qubit line, count CZ and
>                    two-qubit depth, estimate QPU seconds, write a manifest with circuit hashes.
> 2. human reads the manifest and edits configs/hardware_budget.yaml (approved: true).
> 3. ``submit``   - re-checks the manifest hash against the budget file, the running ledger of
>                    QPU seconds, takes a calibration snapshot, submits one Sampler job, records
>                    job id + options + snapshot in evidence/hardware/jobs/<job_id>.json.
> 4. ``collect``  - fetches results, writes raw counts (immutable) and usage.
>
> The quantum-seconds estimate is a *prior*; the pilot job's measured usage replaces it.

## Public names

`BudgetError`, `DryRunSummary`, `estimate_qpu_seconds`, `dry_run`, `check_budget`, `submit`, `collect`, `calibration_snapshot`

## Concepts

[[Transpilation and CZ count]] · [[Gate-and-evidence discipline]]
