---
type: "result"
package: "su2qc-skqd"
tags: ["result"]
date: "2026-10-06"
as_of: "2026-10-06"
---
# Result - 2x3 on ibm_kingston is a measured NO-GO

[[skqd gate K1_2x3_fpilot]] (prompts/32 part B; job `db2avbe8v0ts73c2i8b0`, 188.0 s QPU, preregistered on calibration
`99035ef0`). Two signed 2×3 circuits (5 659 routed CZ, about 411 µs each), 4 pubs × $10^5$ shots on [[ibm_kingston]].

- **0 reference hits in $2\times10^5$ shots**, against 0.191 expected from pure garbage.
- 95 % upper bound on the ideal-sample fraction $\hat f_{\rm ideal}\le2.06\times10^{-5}$, roughly 4 850× below the signed
  bar of 0.1 ([[Clean-shot fraction]]).
- This confirms the model verdict of [[skqd gate K0_2x3_2x4]] (2×3 NO-GO on IBM Heron) with a measurement.

**Consequence.** Only Quantinuum's H2-2 and Helios-1 meet the signed gate-error bar on published numbers (0.1502 and 0.1642
gate-only; [[Quantinuum H-series]]). The 2×3 shot plan of record costs 665 605 HQC at $f=0.10$ ([[skqd gate CV_2x3_plan]]).
See [[Result - 2x3 needs a different device]].
