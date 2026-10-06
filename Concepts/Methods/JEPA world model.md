---
type: "concept"
tags: ["concept"]
aliases: ["JEPA", "Gauge-JEPA"]
as_of: "2026-10-05"
---
# JEPA world model

**Plain words.** A *joint-embedding predictive architecture* (JEPA) learns by predicting the **summary** (latent
embedding) of a future observation from the summary of the current one, instead of predicting the raw data. A
*world model* is a model that predicts how a system evolves given actions.

In [[su2qc-jepa]]: encoder MLP ($24\to128\to128\to16$) maps a noisy observation vector to a 16-dimensional latent; a
GRU predictor advances it under actions (time steps at given couplings); grounding heads read energy, $C_{\rm string}$,
$P_{\rm meson}$, $P_{\rm baryonic}$ and a flag rate from the latent; [[SIGReg]] prevents collapse; a semigroup check
requires two half-steps to equal one full step. Code: [[su2qc_jepa.models.jepa]], [[su2qc_jepa.models.train]].
