---
type: "concept"
tags: ["concept"]
as_of: "2026-10-05"
---
# Leakage-safe data splits

**Plain words.** When training on physics data, test examples must come from coupling values never seen in training
(split by parameters, not by rows), otherwise the model looks better than it is. [[skqd.ml]] splits by
$(\lambda, \text{lattice})$; [[jepa gate J0]] checks that no held-out trajectory appears in training.
