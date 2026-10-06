---
type: "concept"
tags: ["concept"]
as_of: "2026-10-05"
---
# Tensor networks (MPS and TEBD)

**Plain words.** A compressed way to store quantum states of 1D-like systems as a chain of small tensors (a
*matrix product state*, MPS); **TEBD** evolves them in time with Trotter steps. They give classical reference results
for systems too big for [[Exact diagonalization]]. Planned in [[genesis-su2-lgt]] (gate G9, `docs/TENSOR_NETWORK_IDEAS.md`), not started.
Used in [[SU2ZX]] v0.4.0 (plaquette chain to $N=32$) and in [[su2qc-qcadvantage]] ([[su2torus.mps]], quimb `CircuitMPS`), where the
**bond dimension** $\chi$ (the size of the tensors, i.e. how much entanglement the MPS can hold) was raised from 32 to 256 at
$N=48$ to find where the classical answer stops converging ([[Result - qcadvantage MPS frontier at N=48]]).
