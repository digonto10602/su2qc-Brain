---
type: "concept"
tags: ["concept"]
aliases: ["thermal anchor", "decohered value", "typicality"]
as_of: "2026-10-06"
---
# Thermalization and canonical typicality

**Plain words.** A closed quantum system started far from equilibrium usually ends up looking *thermal*: local
observables settle to the values of a thermal state $e^{-\beta H}/Z$ whose inverse temperature $\beta$ is fixed by the
starting energy. The **thermal anchor** is that predicted late-time value; the **decohered value** is the
infinite-temperature ($\beta=0$) value, i.e. what a fully scrambled or fully noise-destroyed state would give.
**Canonical typicality** computes thermal values without diagonalizing $H$: apply $e^{-\beta H/2}$ to a few random
vectors and average (statistical error shrinks with the number of vectors).

In [[su2qc-qcadvantage]] ([[su2torus.thermal]]) this is how an observable is judged useful: if the anchor sits close to
the decohered value, hardware noise and real physics cannot be told apart. See
[[Result - qcadvantage thermalization and the beta=0 states]].
