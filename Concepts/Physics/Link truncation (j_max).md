---
type: "concept"
tags: ["concept"]
aliases: ["j_max", "jmax"]
as_of: "2026-10-05"
---
# Link truncation (j_max)

**Plain words.** The electric field on a link can take infinitely many values (spins $j = 0, \tfrac12, 1, \dots$).
A computer must stop somewhere: $j_{\max}$ is the largest spin kept. All SU2QC packages use $j_{\max}=\tfrac12$
(each link is either empty or carries one unit of flux); $j_{\max}=1$ is used as a check of the truncation error
(152 states instead of 82 on the [[Shared 2x2 plaquette]]).
