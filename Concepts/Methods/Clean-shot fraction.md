---
type: "concept"
tags: ["concept"]
aliases: ["clean fraction", "f"]
as_of: "2026-10-05"
---
# Clean-shot fraction

**Plain words.** The probability that one run (shot) of a circuit happens with no error at all, $f$. SKQD cost scales
like $1/f$ shots (worse, $1/f^2$, at very small $f$). su2qc-skqd's go/no-go bar is $f\ge0.1$. Estimated from hardware by
the reference-string statistic or a mixture estimator; the CF_traj work showed the hit statistic actually tracks the
*ideal-sample* fraction ([[Result - CF_traj clean-fraction re-ruling]]). Code: [[skqd.device_req]], [[skqd.idle]].
