---
type: "package"
package: "genesis-su2-lgt"
status: "dormant"
tags: ["package"]
repo: "https://github.com/digonto10602/genesis-su2-lgt"
last_commit: "2026-08-13 a74543e"
commits: 11
aliases: ["Genesis SU(2) LGT starter", "genesis_su2"]
as_of: "2026-10-05"
---
# genesis-su2-lgt

**What it is.** The first SU2QC starter package (version 1.1.0, built on 2026-08-13 with Codex). It takes the
smallest genuine SU(2) gauge model that has already run on IBM hardware — two square plaquettes, pure gauge (no
quarks), links truncated at $j_{\max}=\tfrac12$ — and makes the *same* Hamiltonian run identically on every backend:
exact NumPy/SciPy, [[Qiskit]], [[CUDA-Q]], IBM Runtime, OpenMP C++ and a custom CUDA kernel.

**The physics.** After [[Gauss's law]] is imposed, the seven links reduce to two qubits. In units of $g^2/2$, with
$x = 2/g^4$ ([[Kavaki and Lewis 2024]], Eq. 1):

$$H = \tfrac38\,(7I - 3Z_0 - Z_0Z_1 - 3Z_1) - \tfrac{x}{2}(3I + Z_1)X_0 - \tfrac{x}{2}(3I + Z_0)X_1 .$$

One canonical [[Pauli decomposition]] is the single source; every backend is generated from it so that no backend can
drift to different physics.

## What it contains

- Code: [[genesis_su2.pauli]], [[genesis_su2.exact]], [[genesis_su2.su2]], [[genesis_su2.encodings]],
  [[genesis_su2.qml.energy_surrogate]], and backends [[genesis_su2.backends.qiskit_backend]],
  [[genesis_su2.backends.cudaq_backend]], [[genesis_su2.backends.ibm_runtime]].
- Gates G0–G7.8 (see [[Gates index]]): G0–G2 PASS, G3 PASS locally (Qiskit 2.5.1, no hardware), G4 PARTIAL (CUDA-Q
  skipped), G5 PASS (no advantage claimed), G6.1 completed-negative, G7.1–G7.4 PASS, G7.5–G7.6 not started,
  G7.7–G7.8 PARTIAL.
- An encoding study ([[Electric basis]] vs [[Quantum link (rishon) encoding]] vs [[Fuzzy gauge theory]]): the
  fuzzy option was marked *BLOCKED-SOURCE-DEFINITION* (no guessed matrices).
- A quantum-kernel energy surrogate: a learning exercise, see [[Quantum kernel methods]]. With 512 shots the
  kernel regression was unstable.
- Workflow: `AGENTS.md`, Codex prompts, `FEATURES.md` change log enforced in CI, [[Graphify code graph]].

## The research ladder it set out (README)

1. exact spectra and real-time evolution of the two-plaquette model → 2. Qiskit and CUDA-Q statevectors →
3. IBM hardware → 4. quantum-kernel surrogate → 5. plaquette chain checked with [[Tensor networks (MPS and TEBD)]] →
6. [[Staggered fermions]], meson/baryon observables, [[String breaking]] → 7. the proposal's 2+1D dressed-site model →
8. AI-assisted layout and calibration.

Step 5 was taken up by [[SU2ZX]] (plaquette chain, MPS to $N=32$); steps 6 and 7 by SU2ZX Section 8,
[[su2qc-skqd]] and [[su2qc-jepa]]; see [[Package lineage]].

## Status

Dormant since 2026-08-13. Open items: G7.5–G7.6 (matched reduced/unreduced Hamiltonian comparison), G9 tensor
networks, G12 hardware dry run, proposal milestone M1.
