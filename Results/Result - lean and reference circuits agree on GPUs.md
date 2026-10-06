---
type: "result"
package: "su2qc-trotter"
tags: ["result"]
date: "2026-09-27"
as_of: "2026-10-06"
---
# Result - lean and reference circuits agree on GPUs

[[su2qc-trotter]] on [[NERSC Perlmutter]] A100s, [[CUDA-Q]] 0.16.0, fp64 state vectors.

- [[trotter gate V1]]: 48 GPU runs of the lean circuit; worst $1-F = 7.0\times10^{-14}$ (exact rotations),
  $1.4\times10^{-12}$ (Clifford+T).
- [[trotter gate B1]]: 60 steps from the strong-coupling vacuum, $dt=0.1$: circuit equals the exact Trotter product to
  $1-F=4.0\times10^{-12}$ (fp64), 25 ms per step; the vacuum empties and revives with period ≈ 3.
- [[trotter gate G22]] / [[trotter gate G34]]: 8 side-by-side tests, the 34-qubit reference on 32 A100s (8 nodes, 256 GB
  state) and the lean circuit on 1 A100. With ideal rotations the two agree to $10^{-12}$ in every test; a
  [[Loschmidt echo]] with one technique forward and the other backward returns to $8.6\times10^{-14}$ (1 step) and
  $8.9\times10^{-13}$ (10 steps). Clifford+T differences are $\sim10^{-5}$ (from synthesis). Cost ≈ 20 node-hours.
