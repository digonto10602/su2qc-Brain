---
type: "result"
package: "su2qc-qcadvantage"
tags: ["result"]
date: "2026-10-06"
as_of: "2026-10-06"
---
# Result - qcadvantage noise mitigation at N=12

[[qca gate M4]]: $N=12$ torus, stripe state, $g=1.25$, $\delta t=0.45g^2$, exact density-matrix simulation with
two-qubit depolarizing noise $p_2\in\{7.9\times10^{-4},10^{-3},1.5\times10^{-3}\}$ (Helios / H2 / Heron-like), plus
one-qubit $3\times10^{-5}$ and readout $10^{-3}$ ([[Noise models and digital twin]]). Emulated, not hardware.

| 10 steps, $p_2=10^{-3}$ (1140 two-qubit gates) | $\langle H_E\rangle$ |
|---|---|
| noiseless circuit | 6.27 |
| raw noisy | 6.01 |
| [[Zero-noise extrapolation]] (folding 1, 3, 5) | 6.22 |

- ZNE reduces the error 5.8–15.5× in 4 of 4 configurations (acceptance needed ≥ 2× in 3 of 4).
- [[Loschmidt echo]] fidelity 0.370 versus predicted $\prod(1-\epsilon)=0.334$; across configurations within 3–13 %.
- Rescaling local observables by the *global* fidelity over-corrects them and makes errors worse: do not use it.
