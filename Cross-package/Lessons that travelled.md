---
type: "hub"
tags: ["cross-package"]
as_of: "2026-10-05"
---
# Lessons that travelled

| lesson | where it was learnt | where it is now built in |
|---|---|---|
| Aer seeds shot $k$ with `seed + k`, so runs seeded `seed`, `seed+1` overlap in $N-1$ of $N$ shots and every quoted spread was void | [[SU2ZX]] GI-cost campaign, session c060_p0_20260909_5 (seeds 500/501: 1 023 shift matches of 1 024) | [[su2qc_jepa.twin.run]] spawns independent seeds; a row of [[jepa gate J0]] tests it |
| generated code documentation covered a different package than the one under test, letting the twin-seed defect through review | SU2ZX v0.6.3 | [[Graphify code graph]] rebuilt every session and freshness-checked in CI ([[Decision - jepa 001 numbered artifacts and Graphify]]) |
| a raw residual against the twin correlates ~perfectly with the exact error, so a "Spearman ≥ 0.7" bar is meaningless without label-free baselines | su2qc-jepa plan audit | [[jepa gate J3]] must report raw_twin, flag_rate, jepa_self, jepa_t0 |
| at 2×2, random strings through the decoder already reproduce $E_0$ (sector saturation) | [[su2qc-skqd]] H0_2x2 | garbage-only and random-equal-size baselines are now mandatory in skqd reports |
| the device model can be 5× off; measure first | su2qc-skqd kingston pilot | skqd: pilot before every main run; jepa plan: 1.5-minute pilot measures the real rate |
| an "all outputs verified at 1e-10" flag was too strong: default-tolerance `Operator.equiv` never checked routed outputs, and PyZX's QASM rounding added ~1e-10 errors | [[SU2ZX]] v0.4.0 audit | explicit atol/rtol and independent routed-output checks; skqd verifies circuits against its own IR to < 1e-10 |
| a builder can silently miss physics (route 1 omitted dressed-vertex recoupling factors) — only a second independent route catches it | [[SU2ZX]] Section 8, solutions/0.5.0.md | every package now builds the Hamiltonian two ways |
| one Hamiltonian, many backends: never re-type physics per backend | [[genesis-su2-lgt]] | skqd's backend-independent IR ([[skqd.circuits_ir]]); jepa's two-route builder |
| a one-day hardware A/B test is not a result: the device's no-DD clean fraction doubled in 4 days, more than the XY4 effect | [[su2qc-skqd]] H0_ddrep (6 Oct) | skqd's 2026-10-06 report withdraws the XY4 note as written; [[Cross-package opportunities]] item 1 |
| code that only runs on a GPU on the cluster can fail where the laptop never shows it (CPU network, GPU data) | [[su2qc-jepa]] jobs 002–007 | a device test in the CPU and CUDA cases; a 2-epoch GPU smoke job before long runs |
