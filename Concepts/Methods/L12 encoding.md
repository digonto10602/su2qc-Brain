---
type: "concept"
tags: ["concept"]
aliases: ["L12"]
as_of: "2026-10-05"
---
# L12 encoding

**Plain words.** [[SU2ZX]]'s 12-qubit encoding of the [[Shared 2x2 plaquette]] (3 qubits per vertex), with
exact gauge-invariant Strang circuits built from block unitaries. Exact and leak-free, but about 2 156 two-qubit gates
per Strang step after compilation — far too deep for current hardware, which is why the later packages built cheaper
carriers ([[Krylov-chain carrier]], skqd codewords). Code: [[su2qc.encodings.l12]], [[su2qc.circuits.strang_l12]].
