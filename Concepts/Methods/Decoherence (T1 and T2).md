---
type: "concept"
tags: ["concept"]
aliases: ["T1", "T2", "T2*"]
as_of: "2026-10-05"
---
# Decoherence (T1 and T2)

**Plain words.** $T_1$: how long a qubit keeps its energy (an excited $|1\rangle$ decays to $|0\rangle$). $T_2$: how long it keeps
its phase. $T_2^\*$ (measured by a Ramsey experiment) includes slow drifts; $T_2^{\rm echo}$ removes them. Long, serial
circuits are limited by idle time, which is why the 2×3 SKQD circuit fails on superconducting devices. Code:
[[skqd.idle]], [[skqd.coherence]].
