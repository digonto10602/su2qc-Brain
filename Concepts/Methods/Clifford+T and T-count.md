---
type: "concept"
tags: ["concept"]
aliases: ["T-count", "Clifford+T", "magic state"]
as_of: "2026-10-06"
---
# Clifford+T and T-count

**Plain words.** Fault-tolerant quantum computers will run only a fixed, finite gate set: the **Clifford** gates
(H, S, CNOT — cheap on error-corrected hardware) plus the **T gate** (a $\pi/4$ phase — expensive, because it needs
*magic-state distillation*). Arbitrary rotations must be approximated by long H/S/T sequences (**synthesis**, e.g.
gridsynth) to a chosen error $\epsilon$. The **T-count** (number of T and T$^\dagger$ gates) is the standard cost metric.
[[su2qc-trotter]] counts it for one plaquette Trotter step: 1162 T (Paulo's 34-qubit circuit) versus 424 T (the lean
22-qubit design) at $\epsilon=10^{-6}$ per rotation ([[Result - lean 22-qubit plaquette Trotter step]]).
