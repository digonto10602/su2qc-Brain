---
type: "concept"
tags: ["concept"]
aliases: ["twin", "Aer"]
as_of: "2026-10-05"
---
# Noise models and digital twin

**Plain words.** A *digital twin* is a simulator configured with a real device's calibration (gate errors, $T_1$, $T_2$,
readout) so you can rehearse a hardware run. Qiskit **Aer** is the simulator used. Warning learnt in su2qc-skqd: the Aer
model at the echo $T_2$ was 5.1× too optimistic for the clean fraction. Code: [[skqd.noise]], [[su2qc_jepa.twin.noise]], [[su2qc_jepa.twin.run]].
