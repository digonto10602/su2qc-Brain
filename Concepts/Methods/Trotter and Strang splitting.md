---
type: "concept"
tags: ["concept"]
aliases: ["Trotter", "Strang splitting", "product formula"]
as_of: "2026-10-05"
---
# Trotter and Strang splitting

**Plain words.** $e^{-iHt}$ is hard to build as a circuit when $H$ has non-commuting parts. Split $H=\sum_\gamma H_\gamma$
and apply each part for a short time in sequence: first-order **Trotter** $\prod_\gamma e^{-iH_\gamma\Delta t}$;
second-order **Strang** uses a symmetric order (error $\propto \Delta t^3$ per step). su2qc-skqd's "coarse step" applies
each term once for time $k\Delta t$ with $\Delta t = \pi/W$ ($W$ = spectral width). [[genesis-su2-lgt]] gate G3 studies
product formulas in Qiskit.
