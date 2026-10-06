---
type: "concept"
tags: ["concept"]
aliases: ["Kogut\u2013Susskind Hamiltonian", "KS Hamiltonian"]
as_of: "2026-10-05"
---
# Kogut-Susskind Hamiltonian

**Plain words.** The energy operator of lattice gauge theory in continuous time ([[Kogut and Susskind 1975]]). Four kinds of term:

$$H = \underbrace{\tfrac{g^2}{2}\sum_\ell E_\ell^2}_{\text{electric}} \;-\; \underbrace{\tfrac{1}{2g^2}\sum_P (W_P + W_P^\dagger)}_{\text{magnetic (plaquette)}} \;+\; \underbrace{m\sum_x (-1)^x n_x}_{\text{mass}} \;+\; \underbrace{\text{hopping}}_{\psi^\dagger U \psi}$$

$g$ is the gauge coupling; $E_\ell^2 = j_\ell(j_\ell+1)$ is the electric energy on link $\ell$; $W_P$ is the
[[Plaquette and Wilson loop]]; the mass term uses [[Staggered fermions]]; the hopping term moves a quark across a
link while updating the link field $U$.

In [[su2qc-skqd]] see [[skqd.hamiltonian]]; in [[su2qc-jepa]] see [[su2qc_jepa.physics.plaquette]] (written in units of $g_E$).
