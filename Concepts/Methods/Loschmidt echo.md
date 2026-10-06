---
type: "concept"
tags: ["concept"]
aliases: ["echo fidelity", "forward-backward echo"]
as_of: "2026-10-06"
---
# Loschmidt echo

**Plain words.** Run a circuit forward and then its exact inverse. Without noise you return to the starting state
with probability 1; the measured return probability therefore estimates the *global fidelity* $F$ of the noisy run.
[[su2qc-qcadvantage]] uses it to check the noise model (echo $F$ within 3–13 % of the predicted $\prod(1-\epsilon)$), and
found that rescaling local observables by the global $F$ over-corrects them. [[su2qc-trotter]] uses a cross-technique
echo (one circuit forward, the other backward) to show the lean and reference circuits are the same unitary.
