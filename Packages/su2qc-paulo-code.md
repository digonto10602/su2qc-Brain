---
type: "package"
package: "su2qc-paulo-code"
status: "reference"
tags: ["package"]
aliases: ["SU2_plaquette_12qubit_encoding", "Eq. 39 circuit", "promise-aware plaquette circuit"]
as_of: "2026-10-06"
---
# su2qc-paulo-code

A local folder (not a git repository; files dated 10 Sept 2026) holding `SU2_plaquette_12qubit_encoding/`:

- `optimized_plaquette_dontcare_lowT.ipynb` — a Qiskit notebook (47 cells) that builds the *promise-aware* ("don't-care",
  low-T) circuit for one SU(2) plaquette step at $j_{\max}=\tfrac12$: 12 data qubits (3 per link), and it only needs to be
  right on the $5^4=625$ valid encoded states. It verifies the 625×625 block exhaustively in NumPy (41 two-state "bright"
  blocks, 543 "dark" singletons).
- `SU2_plaquette_jmax_half_CT.qasm` / `.qpy` and `_metadata.json` — the compiled Clifford+T circuit: **34 qubits**
  (12 data + 22 work), 3207 gates, depth 2549, **1162 T/T†**, 294 CX, rotations synthesised to $\epsilon=10^{-6}$
  (Qiskit 2.5.2, optimisation level 3, seed 12345).

The folder name credits Paulo; the files themselves do not name an author. This is "Eq. 39" of the
[[su2qc-trotter]] plan, and su2qc-trotter keeps an identical copy in `reference/`. CUDA-Q re-counts it exactly
(34 / 3207 / 2549 / 1162 / 294). Concepts: [[Clifford+T and T-count]], [[Link truncation (j_max)]],
[[Plaquette and Wilson loop]].
