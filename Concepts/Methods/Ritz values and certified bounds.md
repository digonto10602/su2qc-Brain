---
type: "concept"
tags: ["concept"]
aliases: ["Weinstein bound", "Kato-Temple bound", "Ritz value"]
as_of: "2026-10-05"
---
# Ritz values and certified bounds

**Plain words.** Diagonalize $H$ in a subspace and the lowest eigenvalue $E_R$ (the *Ritz value*) is never below the
true ground energy $E_0$. The residual $r_H = \|(H-E_R)\psi_R\|$ measures how far the approximate eigenvector is from a
true one, which gives a guaranteed interval:

- Weinstein: some exact eigenvalue lies in $[E_R - r_H,\ E_R]$;
- Kato–Temple: the tighter $[E_R - r_H^2/(\alpha - E_R),\ E_R]$ given a lower bound $\alpha$ on the next level.

Both are the ground-state interval only if the nearest level is the ground state (the *gap assumption*). Used in [[skqd.skqd]].
