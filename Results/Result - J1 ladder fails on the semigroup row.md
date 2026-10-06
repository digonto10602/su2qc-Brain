---
type: "result"
package: "su2qc-jepa"
tags: ["result"]
date: "2026-10-06"
as_of: "2026-10-06"
---
# Result - J1 ladder fails on the semigroup row

[[jepa gate J1]], 5 seeds × 200 epochs per run on [[NERSC Perlmutter]]; thresholds in `configs/gates.yaml`: effective
rank ≥ 8 (how many latent directions the model really uses; low rank = partial *collapse*), $R^2$ energy ≥ 0.887,
$C_{\rm string}$ ≥ 0.99, $P_{\rm meson}$ ≥ 0.95, $P_{\rm baryonic}$ ≥ 0.98, and **semigroup residual < $10^{-3}$** (the relative
mismatch between predicting two steps at once and one step twice).

| run (change vs base) | rank min | semigroup max | verdict |
|---|---|---|---|
| `v1_base` | 5.16 | $3.3\times10^{-3}$ | FAIL (rank, semigroup) |
| `v1_wsigreg2` ([[SIGReg]] weight 2) | 8.26 | $5.3\times10^{-3}$ | FAIL (semigroup) |
| `v1_wsigreg5` | 10.5 | $8.5\times10^{-3}$ | FAIL (semigroup) |
| `v1_latent32` | 6.12 | $4.7\times10^{-3}$ | FAIL |
| `v1_ema` | 13.1 | $2.2\times10^{-2}$ | FAIL (also $P_{\rm meson}$ 0.915) |
| `v1_wground3` | 5.63 | $6.9\times10^{-3}$ | FAIL |
| `v1_curriculum` | 6.18 | $2.9\times10^{-3}$ | FAIL |
| `v1_wsemigroup1` (semigroup weight 1) | 4.94 | $1.7\times10^{-3}$ | FAIL |
| `v1_wsig2_wsg1` | 8.56 | $5.6\times10^{-3}$ | FAIL (semigroup) |

- Energy, $C_{\rm string}$ and $P_{\rm baryonic}$ pass in every run reported in `reports/012`; energy $R^2\approx0.90$, within
  ≈ 0.015 of the measured ceiling ([[Result - J1 energy information ceiling]]).
- Raising the SIGReg weight fixes the rank but the semigroup residual grows with rank (Pearson 0.898 between rank and
  $\log_{10}$ residual over 30 runs — a correlation among runs that also differ in loss weights, not a proven mechanism).
- The plan's fallback (J1 PARTIAL) is written for a rank failure, not a semigroup failure; no rule covers this case yet.
- Queued: jobs 013 (`v1_wsig2_wsg3`) and 014 (`v1_wsig2_wsg10`), stronger semigroup weights with SIGReg 2.

Sources: `reports/012` §8.3 (first six rows), `evidence/GATE_LEDGER.md` and the gate commits of 6 Oct (last three rows).
