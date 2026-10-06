---
type: "module"
package: "su2qc-skqd"
file: "src/skqd/circuits_cudaq.py"
lines: 154
generated: True
as_of: "2026-10-06"
tags: ["module", "skqd"]
---
# skqd.circuits_cudaq

Module of [[su2qc-skqd]] · `src/skqd/circuits_cudaq.py` · 154 lines

## What it does (from the module docstring)

> CUDA-Q translation of the IR circuits (circuits_ir.py) for GPU statevector
> sampling on the laptop (target 'nvidia', GTX 1060 Max-Q) or the desktop (RTX 3070).
>
> NOT executed in the cloud sandbox where this package was assembled.  The laptop
> gate scripts/laptop_L5_cudaq_check.py first establishes the two conventions that
> cannot be known without running CUDA-Q — the order of the result strings and the
> qubit order of cudaq.register_operation for multi-qubit matrices — with a CNOT
> test, and only then compares a sampled 2x2 circuit with the numpy reference.
>
> Design.  CUDA-Q compiles @cudaq.kernel functions from their Python source
> (inspect.getsource), so the IR gate list is turned into straight-line kernel
> SOURCE CODE written to a real .py file in a temporary directory and imported;
> custom unitaries (the hopping block unitaries) are registered first with
> cudaq.register_operation(name, matrix) and called by name inside the kernel, as
> in the CUDA-Q documentation example
>
>     cudaq.register_operation("custom_h", np.array([ [1, 1], [1, -1] ]) / np.sqrt(2))
>     @cudaq.kernel
>     def bell():
>         q = cudaq.qvector(2)
>         custom_h(q[0])
>         x.ctrl(q[0], q[1])
>
> Supported IR gates: x, h, rz, ry, rx, p (r1), cp, cx, gphase, unitary (1- and
> multi-qubit, via cudaq.register_operation) and mcu (a registered one-qubit
> operation applied with .ctrl, with X conjugation for controls active on |0>).
>
> Endianness.  BIG_ENDIAN = True means the first qubit argument of a registered
> operation is the MOST significant bit of its matrix; the matrices of this
> package are little-endian (first qubit = least significant bit, see
> reference_sim.py), so they are bit-reversed before registration when
> BIG_ENDIAN is True.  The convention test in the L5 script sets this flag from
> a measurement; the default below is only a guess.

## Public names

`kernel_source`, `build_kernel`, `sample`

## Concepts

[[Transpilation and CZ count]] · [[CUDA-Q]] · [[Laptop (Dell G7)]]

## Checked by gates

[[skqd gate L5]]
