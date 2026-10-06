---
type: "result"
package: "SU2ZX"
tags: ["result"]
date: "2026-09-06"
as_of: "2026-10-05"
---
# Result - SU2ZX v0.4.0 compiler and MPS study

Pure-gauge plaquette chain, ideal simulation only ([[SU2ZX]] layer 1).

- **MPS scaling** to $N=32$ plaquettes without a full statevector; validation at $N=5, 8$ max error $2.27\times10^{-9}$
  (bond cap 64). Short-time, shallow circuits only. See [[Tensor networks (MPS and TEBD)]].
- **Compiler winners** ([[ZX-calculus circuit optimization]]): 33 families robustly Basic, 29 robustly Teleport, 21 tied,
  0 seed-sensitive; 830 of 860 compiler outputs pass the numerical gates.
- **ML compiler selector: NULL.** Prospective regret 0.0250 vs 0.0090 for the best simple baseline.
- **Symmetry-aware ordering: MIXED.** Preserves mirror symmetry and cuts depth, but the output distribution (TVD)
  improved in only 16 of 56 comparisons.
- No QPU jobs; no claim about string tension, string breaking or advantage.
