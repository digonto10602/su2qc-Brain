---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/report.py"
lines: 121
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.report

Module of [[su2qc-skqd]] · `src/skqd/report.py` · 121 lines

## What it does (from the module docstring)

> Gate-result bookkeeping: every gate script records its criteria and the numbers
> it actually computed in validation/<GATE>.json and writes reports/<GATE>_*.md
> from those same numbers.  Nothing in a report is typed by hand.

## Public names

`environment`, `Criterion`, `GateResult`, `write_report`, `md_table`, `env_block`

## Concepts

[[Gate-and-evidence discipline]]

## Checked by gates

[[skqd gate CF_traj]] · [[skqd gate E1]] · [[skqd gate E2]] · [[skqd gate E3]] · [[skqd gate H0]] · [[skqd gate H0P]] · [[skqd gate H0P_ibm_fez]] · [[skqd gate H0P_rehearsal]] · [[skqd gate H0_2x2]] · [[skqd gate H0_canary]] · [[skqd gate H0_ddrep]] · [[skqd gate H0_ddtest]] · [[skqd gate H0_diag]] · [[skqd gate H0_dryrun]] · [[skqd gate H0_kpilot]] · [[skqd gate H0_model]] · [[skqd gate H1]] · [[skqd gate H2]] · [[skqd gate K0_2x3_2x4]] · [[skqd gate K1_2x3_fpilot]] · [[skqd gate L2]] · [[skqd gate L3]] · [[skqd gate L4]] · [[skqd gate L4_fez]] · [[skqd gate L5]] · [[skqd gate Q0P_2x3]] · [[skqd gate S1]] · [[skqd gate S2]] · [[skqd gate S2D]] · [[skqd gate S2D_idle]] · [[skqd gate S2D_levers]] · [[skqd gate S2_2x4]]
