---
type: "concept"
tags: ["concept"]
aliases: ["ZNE", "gate folding"]
as_of: "2026-10-06"
---
# Zero-noise extrapolation

**Plain words.** Error mitigation (not correction): run the same circuit with the noise deliberately amplified, for
example by replacing each gate $G$ with $G G^\dagger G$ (**gate folding**, noise factor 3) or $G(G^\dagger G)^2$
(factor 5), then fit the measured value against the noise factor and extrapolate back to factor 0.
In [[su2qc-qcadvantage]] ([[su2torus.noise]]) folding at factors 1, 3, 5 cut the error of $\langle H_E\rangle$ by
5.8–15.5× in 4 of 4 tested configurations at $N=12$ ([[Result - qcadvantage noise mitigation at N=12]]).
