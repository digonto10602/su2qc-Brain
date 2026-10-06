---
type: "decision"
package: "su2qc-qcadvantage"
status: "waiting"
tags: ["decision"]
as_of: "2026-10-06"
---
# Decision - qcadvantage open questions before the cluster

Four decisions that `notes/STATUS.md` of [[su2qc-qcadvantage]] (6 Oct 2026) leaves to you. **Not yet decided.**

1. **Initial state at $N=48$–$64$.** The plan prescribes the stripe state, but on tori with even $L_1$ it sits at
   $\beta=0$ (thermal = decohered), so it cannot separate physics from noise. Recommended: the SU(2) vacuum
   ($\beta\approx1.4$) or an odd-row state. Evidence: `reports/m3_physics.md` §3; [[Result - qcadvantage thermalization and the beta=0 states]].
2. **Open-lattice electric term.** The code uses the bond form; METHODS' $3n_p$ form differs on open lattices
   (string $E_E(0)=4.41$ vs $5.88$). Evidence: `reports/audits/m1_audit.md`.
3. **Trotter step size.** $2\delta t/g^2=0.9$ (plan M6) departs strongly from $e^{-iHt}$: at $N=12/16$, step 8, Trotter
   $\langle H_E\rangle$ is 0.54 versus exact 0.31 (fractions of $E_\infty$). Decide $\delta t$ before cluster thermal-anchor
   work. Evidence: `reports/audits/m6_audit.md`.
4. **Tags.** Push `m1-done` … `v0.1-pre-cluster` from a machine with tag-push rights (`git push origin --tags`).
