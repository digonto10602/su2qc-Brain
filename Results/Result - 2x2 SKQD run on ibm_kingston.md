---
type: "result"
package: "su2qc-skqd"
tags: ["result"]
date: "2026-10-02"
as_of: "2026-10-05"
---
# Result - 2x2 SKQD run on ibm_kingston

**Date:** 2026-10-02. **Gate:** [[skqd gate H0_2x2]] PASS 8/8. **Device:** [[ibm_kingston]]. **Package:** [[su2qc-skqd]].

- 7 reference configurations × $k=1..4$ = 28 circuits on 12 qubits; one coarse step ≈ 588 CZ, ≈ 44 µs.
- Decoder: 0 mismatches on 58 hardware strings ([[Codewords and the Gauss-law decoder]]).
- Measured [[Clean-shot fraction]]: $f = 0.1271\ [0.1084, 0.1479]$ with client DD, $0.0413$ without.
- Signal support: 35 of 38 states ($B=0$), 19 of 20 ($B=1$) above the 3σ noise line.
- Energies ([[Ritz values and certified bounds]]): $B=0$: $E_R=-3.6402189$, $r_H = 0.0603$, $|E_R-E_0| = 5.48\times10^{-4}$;
  $B=1$: $E_R = -1.8615823$, $r_H = 5.95\times10^{-3}$, $|E_R-E_0| = 5.75\times10^{-6}$. All intervals contain the exact $E_0$.

**The catch.** At 2×2 the sector is so small that uniformly random strings through the same decoder give $E_R=E_0$
exactly (garbage-only baseline, 100 seeds). So the energies are a pipeline validation, not evidence that "the device
finds the ground state" ([[van Rossum et al. 2026]]). A physics claim needs 2×3 ([[Result - 2x3 needs a different device]]).
