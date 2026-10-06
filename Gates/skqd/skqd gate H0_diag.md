---
type: "gate"
package: "su2qc-skqd"
gate: "H0_diag"
status: "fail"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "fail"]
---
# skqd gate H0_diag

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | the prompts/19 diagnostic session on ibm_fez: the DD x twirling factorial of the frozen canary circuit and the windowed T1/Ramsey tests that decide between the idle-relaxation and the sampler-options hypotheses |
| runs on | QPU |
| status | **FAIL (8 criteria, 2 failing, 1 s, 2026-09-22 14:46:44 MDT, commit 4d1e8f6)** |
| evidence / script | scripts/gate_H0_diag.py |

## Code it exercises

[[skqd.codec]] · [[skqd.exact]] · [[skqd.hardware]] · [[skqd.reference_sim]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Dynamical decoupling]] · [[Decoherence (T1 and T2)]] · [[ibm_fez]]
