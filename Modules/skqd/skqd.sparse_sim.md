---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/sparse_sim.py"
lines: 377
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.sparse_sim

Module of [[su2qc-skqd]] · `src/skqd/sparse_sim.py` · 377 lines

## What it does (from the module docstring)

> Exact SPARSE statevector simulation of the IR circuits and of transpiled circuits.
>
> Why.  At 2x4 the coarse-step circuit acts on 28 qubits, where a dense statevector is
> 4.3 GB and `run_ir` costs 0.7-3.8 s per gate on the laptop CPU (the planner's P4 in
> `reports/S2_2x4_planner_analysis_20260930.md`): one circuit would be 10-20 hours.  The
> circuits, however, are not dense at all.  A coarse step starts on ONE codeword and every
> term gate maps codewords to codewords (`circuits_ir._multiplexed_two_level` forces the
> identity on any pair of local strings that contains a codeword and carries no rotation), so
> between multiplexed rotations the state lives on at most the 37165 codewords of the 2x4
> basis; inside one multiplexed rotation the Gray-code chain acts on ONE target qubit t, so
> the support only has to be closed under the flip of t -- at most twice as large.
>
> So the whole coarse step can be carried in a sorted index array of order 10^4-10^5 entries.
> This module does exactly that, with **no truncation whatsoever**: an entry is dropped only
> when its amplitude is identically 0.0 (an entry that was created by closing the support
> under a flip and never rotated), which changes nothing about the state.  There is no
> magnitude threshold anywhere in this file.
>
> Representation.  Two equivalent modes, switched on demand:
>
> * SPARSE  -- `idx` (sorted unique int64 basis integers, qubit k = bit k) and `amp`.
>   Permutations (`x`, `cx`) and diagonal gates (`rz`, `p`, `cp`, `cz`, `gphase`) act here.
> * PAIRED on a qubit t -- `base` (sorted unique int64 with bit t cleared) and two amplitude
>   columns `c0`, `c1` for bit t = 0 and 1.  Every two-level gate on t (`ry`, `rx`, `h`, `sx`,
>   one-qubit `unitary`) is then a 2x2 mix of two contiguous arrays, and `cx(c -> t)` with
>   c != t is a swap of the two columns on the rows where bit c of `base` is set.  A
>   uniformly controlled rotation -- 2^c rotations and 2^c CNOTs, all on the same target --
>   therefore runs entirely in this mode at O(support) per gate with no re-sorting at all,
>   which is what makes the 132554-gate `plaq1` term affordable.
>
> The cost of switching modes is one sort; the switch happens once per multiplexed rotation,
> not once per gate.
>
> The result is checked against `circuits_ir.run_ir` at 2x2 and 2x3 and against one dense
> 2^28 `run_ir` of the smallest 2x4 term (`tests/test_sparse_sim.py`, gate S2_2x4 criterion C4).

## Public names

`SparseState`, `apply_ir`, `run_sparse`, `qiskit_to_ir`, `run_sparse_qiskit`, `project`

## Concepts

[[Link truncation (j_max)]] · [[Trotter and Strang splitting]] · [[Codewords and the Gauss-law decoder]] · [[Transpilation and CZ count]] · [[Gate-and-evidence discipline]] · [[Agent routing (planner, executor, reviewer, runner, scribe)]]

## Checked by gates

[[skqd gate S2_2x4]]
