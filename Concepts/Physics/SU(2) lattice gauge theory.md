---
type: "concept"
tags: ["concept"]
as_of: "2026-10-05"
---
# SU(2) lattice gauge theory

**Plain words.** A gauge theory describes forces carried by fields that live *between* particles. "SU(2)" is the
symmetry group (2×2 unitary matrices with determinant 1); it is the simplest **non-Abelian** group, meaning the
force carriers themselves carry charge, as in the strong force (whose group is SU(3)). *Lattice* means space is
replaced by a grid: matter on the sites, gauge fields on the links between sites.

**Why SU2QC uses it.** It keeps the hard features of QCD (non-Abelian charges, confinement, string breaking) while
being small enough for today's quantum computers.

Used by every package: [[genesis-su2-lgt]], [[su2qc-skqd]], [[su2qc-jepa]]. Hamiltonian form: [[Kogut-Susskind Hamiltonian]].
