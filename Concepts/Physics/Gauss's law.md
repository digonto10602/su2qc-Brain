---
type: "concept"
tags: ["concept"]
as_of: "2026-10-05"
---
# Gauss's law

**Plain words.** At every site, the colour charge flowing in through the links must equal the charge sitting on the
site. Only states obeying this everywhere are physical; the rest are artefacts of the encoding.

$$G_a(x)\,|\text{phys}\rangle = 0, \qquad [G_a(x), H] = 0 .$$

Every package checks $[G_a, H]=0$ numerically (gates E1, J0, G7.2–G7.4). On hardware, Gauss's law becomes a free
error check: measured strings that violate it are rejected ([[Codewords and the Gauss-law decoder]]).
