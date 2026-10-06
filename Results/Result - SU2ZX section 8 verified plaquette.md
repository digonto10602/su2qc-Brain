---
type: "result"
package: "SU2ZX"
tags: ["result"]
date: "2026-09-07"
as_of: "2026-10-05"
---
# Result - SU2ZX section 8 verified plaquette

The overnight Hermes run of 7 Sept 2026 built the [[Shared 2x2 plaquette]] by two independent routes:
spectra agree to $2.7\times10^{-15}$, stretched-string time series to $1.6\times10^{-15}$; route 2 gives $[G^a_v, H_{\rm term}] = 0.0$
exactly for every term on the 160 000-dimensional redundant space ([[Gauss's law]]). Dimensions 82 / 152, sectors
2/20/38/20/2, electric-limit degeneracies 16/16/18/16/16. One real defect (route 1 missing vertex recoupling factors)
was caught by the disagreement and fixed via `solutions/0.5.0.md`. The L12 circuits are exact (block unitary deviation
$2.7\times10^{-14}$, zero leakage) with Trotter slopes ≈ −2.1. Run halted at T+4 h: G4–G9 never ran, 0 QPU seconds.
Gates: [[su2zx gate S8-G1]], [[su2zx gate S8-G2]], [[su2zx gate S8-G3]].
