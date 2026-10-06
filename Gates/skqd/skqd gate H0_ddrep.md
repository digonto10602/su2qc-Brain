---
type: "gate"
package: "su2qc-skqd"
gate: "H0_ddrep"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0_ddrep

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | one-job replication of the XY4 gain (T0 vs T3) and of the context-aware collapse (T1) with four mechanism cells (CA+/-, XX, X(-X), CA minus two qubits) and four pulse-train pubs on the two k = 1 circuits; preregistered classes and reading rule (measurement gate) |
| runs on | QPU |
| status | **PASS (8 criteria, 0 failing, 422 s, 2026-10-06 01:11:17 MDT, commit 36c48a2)** |
| evidence / script | scripts/gate_H0_ddrep.py |

## Code it exercises

[[skqd.codec]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[SIGReg]] · [[Dynamical decoupling]] · [[Decoherence (T1 and T2)]] · [[Preregistration]]
