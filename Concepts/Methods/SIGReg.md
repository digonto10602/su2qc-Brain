---
type: "concept"
tags: ["concept"]
as_of: "2026-10-05"
---
# SIGReg

**Plain words.** A JEPA can "cheat" by mapping every input to the same latent (collapse), which makes prediction
trivial. *SIGReg* (sketched isotropic Gaussian regularization) penalises latents whose distribution is far from a
round Gaussian, keeping them spread out. Its weight is one rung of [[su2qc-jepa]]'s ablation ladder (jobs 003, 004).
The J1 gate checks the *effective rank* of the latent ($\ge 8$ of 16).
