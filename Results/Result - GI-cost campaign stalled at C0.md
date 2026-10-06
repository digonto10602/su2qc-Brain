---
type: "result"
package: "SU2ZX"
tags: ["result"]
date: "2026-09-10"
as_of: "2026-10-05"
---
# Result - GI-cost campaign stalled at C0

The campaign ([[SU2ZX]] layer 3) was to measure the hardware cost of exact gauge invariance (arm GI, the L12 Strang
circuits) against Krylov playback (arm KR). After five sessions (7–10 Sept): [[su2zx gate C1]] PASS (preregistration),
[[su2zx gate C0]] PARTIAL — the twin-seed defect was found and repaired ([[Lessons that travelled]]), but the variance
band at $r=0$ (dC ratio 0.238) is an open finding, $r=1$ was too expensive to evaluate (821 320 operations, depth 506 888
on 133 qubits), and an empty-repeat bootstrap contamination remains. C2–C8 never started; hardware disabled.
In practice the follow-up work moved to [[su2qc-skqd]] (14 Sept) and [[su2qc-jepa]] (1 Oct).
