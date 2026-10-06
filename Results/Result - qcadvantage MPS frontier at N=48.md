---
type: "result"
package: "su2qc-qcadvantage"
tags: ["result"]
date: "2026-10-06"
as_of: "2026-10-06"
---
# Result - qcadvantage MPS frontier at N=48

[[qca gate M6]]: $N=48$ ($4\times6$) torus, stripe state, $g=1.25$, $\delta t=0.703$ ($2\delta t/g^2=0.9$), 8 first-order
Trotter steps, [[Tensor networks (MPS and TEBD)|MPS]] bond dimension $\chi=32, 64, 128, 256$ (`results/m6/convergence.json`).

- **Criterion:** successive $\chi$ agree in $\langle H_E\rangle$ to 1 % of the decohered value (0.211) and in every
  $\langle Z_p\rangle$ to 0.01.
- **Converged through step 2** ($t=1.41$); step 3 marginal (largest $\Delta\langle Z_p\rangle = 0.013$, 4 of 48 plaquettes
  over tolerance); unconverged from step 4.
- Cumulative truncation error at step 8 for $\chi=256$: 0.79 (estimated overlap with the exact state ≈ 0.21).
- $\langle H_E\rangle$ alone is misleading: it agrees between $\chi$ values to 0.11 at every step because it averages
  72 bonds; local magnetizations are the sensitive probe.
- Cost: $\chi=256$ took 6935 s single-threaded on a 4-vCPU cloud machine.
- MPS validation ([[qca gate M5]]): $N=24$, $\chi=256$, 4 steps at $\delta t=0.2$: $1-F=1.1\times10^{-9}$.

**Meaning.** At these step sizes, exact-quality MPS at $N=48$ fails after 2–3 steps with $\chi\le256$. Whether GPU MPS
($\chi=1024$–$4096$), PEPS or Pauli propagation reach 4–8 steps decides the advantage claim. Hardware budget from
`results/m5/resources.json`: 456 native-ZZ gates per step at $N=48$; raw fidelity 0.161 after 4 steps at $p_2=10^{-3}$.
Caveat from the M6 audit: at this $\delta t$ the Trotter circuit is far from $e^{-iHt}$
([[Decision - qcadvantage open questions before the cluster]] item 3).
