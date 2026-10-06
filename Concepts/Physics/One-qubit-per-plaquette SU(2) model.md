---
type: "concept"
tags: ["concept"]
aliases: ["minimal SU(2) truncation", "abelian twin", "honeycomb plaquette torus"]
as_of: "2026-10-06"
---
# One-qubit-per-plaquette SU(2) model

**Plain words.** The cheapest known exactly gauge-invariant form of pure SU(2) gauge theory in 2+1 dimensions
([[Ciavarella et al. 2026]]): keep only $j=0$ and $j=\tfrac12$ on every link of a triangular lattice and use
[[Gauss's law]] to eliminate the links, so that each **plaquette** becomes one qubit. The plaquettes form a honeycomb
graph; on a torus (periodic boundaries) there are $N$ plaquette qubits:

$$H=\frac{3g^2}{16}\sum_{\langle pq\rangle}(1-Z_pZ_q)\;-\;\frac1{g^2}\sum_p\Big[\prod_{q\in nb(p)}c(n_q)\Big]X_p,\qquad c(0)=1,\ c(1)=\tfrac12 .$$

The first sum is the electric energy (a cost on every bond between plaquettes in different states); the second flips a
plaquette with an amplitude that depends on its neighbours (this neighbour dependence is what makes it non-Abelian).
Setting $c\equiv1$ gives the **abelian twin**, the transverse-field Ising model, used as a control.
Code: [[su2torus.lattice]], [[su2torus.hamiltonian]] in [[su2qc-qcadvantage]].
