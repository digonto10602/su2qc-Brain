---
type: "concept"
tags: ["concept"]
aliases: ["ZX calculus", "PyZX"]
as_of: "2026-10-05"
---
# ZX-calculus circuit optimization

**Plain words.** The ZX-calculus rewrites a quantum circuit as a graph of simple "spiders" and simplifies it with a
small set of exact rules; **PyZX** is the standard library. "Basic" and "Teleport" are two PyZX simplification
strategies. Used in [[SU2ZX]] v0.4.0 to choose the cheapest compiled circuit for each case, and in your SU(2) circuit
lab (PyZX `basic_optimization` cut two Strang repetitions from 118 to 94 ECR gates; `full_reduce` made it worse, 180).
