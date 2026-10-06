---
type: "gate"
package: "su2qc-skqd"
gate: "H0_kpilot_dryrun"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0_kpilot_dryrun

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | ibm_kingston pilot on the selected patch: windowed Ramsey at two lengths (T2*/T2_echo ratio r_eff vs r_crit), T1, the signed k = 1 circuits' direct f_clean; GO/NO-GO on f >= 0.1 (measurement gate) -- DRY RUN |
| runs on | see validation JSON |
| status | **PASS (9 criteria, 0 failing)** |
| evidence / script | validation/H0_kpilot_dryrun.json |

## Concepts

[[Clean-shot fraction]] · [[Decoherence (T1 and T2)]] · [[ibm_kingston]]
