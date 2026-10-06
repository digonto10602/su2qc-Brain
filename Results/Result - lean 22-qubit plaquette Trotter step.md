---
type: "result"
package: "su2qc-trotter"
tags: ["result"]
date: "2026-09-24"
as_of: "2026-10-06"
---
# Result - lean 22-qubit plaquette Trotter step

[[su2qc-trotter]], one plaquette, one Trotter step, $g_s=g_t=a=\Delta t=1$ ($\alpha=2$), rotations synthesised to
$\epsilon=10^{-6}$ each, basis {H, S, S†, T, T†, CX}; counts from `cudaq.estimate_resources` ([[trotter gate R1]] reproduced
them on Perlmutter under a different CUDA-Q version).

| circuit | qubits (data + ancilla) | gates | depth | T/T† | CX |
|---|---|---|---|---|---|
| Eq. 39, [[su2qc-paulo-code]] export | 34 (12 + 22) | 3207 | 2549 | 1162 | 294 |
| same design, su2qc-trotter's CUDA-Q compile | 34 (12 + 22) | 1678 | 1171 | 660 | 294 |
| **lean design** | **22 (12 + 10)** | **1681** | **966** | **424** | **210** |
| lean + electric term (full Trotter step) | 22 | 2309 | 1118 | 680 | 210 |

- Lean T = 172 fixed (logic) + 252 in 4 synthesised rotations; 4 arbitrary rotations is the minimum for its flag structure
  (checked over all parity bases).
- T versus $\epsilon$: lean 264 ($10^{-2}$) … 586 ($10^{-10}$); baseline 426 … 914.
- Exhaustive check on all 625 encoded inputs: logical circuits $\|U-e^{i\phi}V\|_2\le3.4\times10^{-14}$, leakage 0;
  Clifford+T circuits $1.1\times10^{-6}$ (lean), below the summed synthesis error.
- See [[Clifford+T and T-count]], [[Trotter and Strang splitting]].
