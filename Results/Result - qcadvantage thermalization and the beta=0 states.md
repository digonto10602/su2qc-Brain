---
type: "result"
package: "su2qc-qcadvantage"
tags: ["result"]
date: "2026-10-06"
as_of: "2026-10-06"
---
# Result - qcadvantage thermalization and the beta=0 states

[[qca gate M3]], exact dynamics on tori of $N=12$ and $24$ plaquettes at $g=1.25$ (`results/m3/summary.json`).

- From the vacuum the SU(2) model relaxes toward a thermal state with $\beta=1.440$ ($N=24$) and $1.448$ ($N=12$); the
  typicality uncertainty is $\pm0.04$ in $\beta$, so no finite-size shift is resolved
  ([[Thermalization and canonical typicality]]).
- At $g\le1.25$ the abelian twin relaxes more slowly; its thermal electric energy is 8.13 versus 5.15 for SU(2) ($N=24$).
- **The stripe and Néel-half states sit at infinite temperature** ($\beta=0$) on even-$L_1$ tori, including the $N=48$
  frontier torus: exactly half the bonds are cut, so their late-time values equal the decohered values. For the abelian
  twin $\langle H_E\rangle(t)$ is then exactly constant, by symmetry.
- Energy is conserved to below $10^{-7}$. Recommended physics target: the SU(2) vacuum at $g\approx1.25$–$1.4$.
  This feeds [[Decision - qcadvantage open questions before the cluster]] item 1.
