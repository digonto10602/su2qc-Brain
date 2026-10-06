---
type: "gate"
package: "su2qc-skqd"
gate: "H0_2x2"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "skqd", "pass"]
---
# skqd gate H0_2x2

Gate of [[su2qc-skqd]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | the full 2x2 SKQD run on ibm_kingston below the signed budget (owner decision 2026-10-02): both sectors, D3' at the measured f, decoding, Ritz energies vs exact E0, certificates, garbage and random baselines (measurement gate) |
| runs on | QPU |
| status | **PASS (8 criteria, 0 failing, 444 s, 2026-10-02 16:04:51 MDT, commit da715fc)** |
| evidence / script | scripts/gate_H0_2x2.py |

## Code it exercises

[[skqd.codec]] · [[skqd.krylov]] · [[skqd.report]] · [[skqd.skqd]]

## Concepts

[[Baryon-number sectors]] · [[Sample-based Krylov quantum diagonalization (SKQD)]] · [[Ritz values and certified bounds]] · [[Codewords and the Gauss-law decoder]] · [[ibm_kingston]]
