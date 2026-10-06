---
type: "result"
package: "su2qc-skqd"
tags: ["result"]
date: "2026-10-06"
as_of: "2026-10-06"
aliases: ["Result - client-side XY4 raises clean fraction"]
---
# Result - client-side XY4 gain did not replicate

**2 Oct 2026** ([[skqd gate H0_ddtest]] PASS): a one-job A/B test on [[ibm_kingston]] of client-side
[[Dynamical decoupling]] variants against no DD. Client-side XY4 in the long idle windows raised the
[[Clean-shot fraction]] by a ratio $R_{T3}=2.819\ [2.495, 3.185]$ (no DD 0.0400, XY4 0.1129); the context-aware variant collapsed;
IBM's runtime DD gave no gain.

**6 Oct 2026** ([[skqd gate H0_ddrep]], job `db29p6nr11fs7396e4ig`, 37.0 s QPU): the same frozen circuits again.

| | 2 Oct | 6 Oct |
|---|---|---|
| no-DD clean fraction | 0.0400 [0.0358, 0.0446] | 0.0818 [0.0758, 0.0881] |
| client XY4 (cell T3) | 0.1129 [0.1058, 0.1203] | 0.0732 [0.0675, 0.0792] |
| ratio $R_{T3}$ | 2.819 [2.495, 3.185] | 0.895 [0.804, 0.996] |

The gain did not replicate; the context-aware collapse did not replicate either; a coherent $x$-pulse over-rotation
of 0.015–0.020 rad was measured on all 12 qubits. **Lesson:** the day-to-day change of the device (factor ≈ 2 in the
no-DD baseline) is larger than the decoupling effect being tested, so a one-day A/B test is not a result. Intervals
are 95 %; numbers from `validation/H0_ddtest.json`, `validation/H0_ddrep.json` via skqd's 2026-10-06 full report.
