---
type: "module"
package: "su2qc-jepa"
file: "src/su2qc_jepa/models/jepa.py"
lines: 188
generated: True
as_of: "2026-10-06"
tags: ["module", "jepa", "models"]
---
# su2qc_jepa.models.jepa

Module of [[su2qc-jepa]] · `src/su2qc_jepa/models/jepa.py` · 188 lines

## What it does (from the module docstring)

> Gauge-JEPA-P v2: classical encoder + action-conditioned predictor + SIGReg + grounding heads.
>
> Definitions (plain words):
> * encoder  E_theta : observation o_t (noisy, finite shots)  -> latent s_t in R^d
> * predictor P_phi  : (s_t, a_t, ..., a_{t+k-1})             -> predicted latent for time t+k
> * JEPA loss        : || P_phi(s_t, a) - E_theta(o^clean_{t+k}) ||^2 ; the target is the encoder
>                      of the *clean* future observation (exact expectation values), never the
>                      observation itself.  By default there is no moving-average target: collapse is
>                      prevented by SIGReg.  With JEPAConfig.ema_target = tau the target latent comes from an
>                      exponential-moving-average copy of the encoder under stop-gradient (I-JEPA style);
>                      SIGReg then acts on the context latent only.
> * SIGReg           : LeJEPA's sketched isotropic Gaussian regulariser - random 1-D projections of
>                      the latent batch are pushed toward N(0,1) with an Epps-Pulley characteristic-
>                      function statistic.  (arXiv:2511.08544)
> * grounding heads  : linear maps from the latent to known physical quantities (energy, string
>                      Casimir, channel weights, flag rate), used in training only, so the latent is
>                      identifiable and encoder/predictor cannot co-adapt into a trivial code.
> * semigroup loss   : P(s, [a, a]) ~ P(P(s, [a]), [a]) - the predictor must compose like time evolution.

## Used by

`su2qc_jepa.models.train`

## Public names

`JEPAConfig`, `MLP`, `ActionPredictor`, `sigreg_loss`, `effective_rank`, `GaugeJEPA`

## Concepts

[[Gauss's law]] · [[JEPA world model]] · [[SIGReg]]
