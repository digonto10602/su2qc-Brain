---
type: "result"
package: "su2qc-skqd"
tags: ["result"]
date: "2026-10-02"
as_of: "2026-10-06"
---
# Result - 2x3 needs a different device

- On superconducting devices the 2×3 coarse step is longer and more serial than 2×2; the idle-time budget
  ([[Decoherence (T1 and T2)]], [[skqd.idle]]) rules it out (amendment 01 item 4; [[skqd gate S2D]] FAIL).
- [[IonQ Forte]]: "2×3 no, 2×2 yes" from published specifications.
- [[Quantinuum H-series]]: the 2×3 circuits are compiled to the native gate set and verified exactly
  ([[skqd gate Q0P_2x3]] PASS; 0 HQC spent, no Nexus login yet).
- Error correction (prompts/27): full QEC ≈ $10^5$ T gates per shot (a ~2029-class option); an Iceberg error-detection
  code is a net loss because the Gauss-law codewords already form a distance-2 detection code; there is no quantum
  "amplifier", but more shots help — usable clean fraction at 2×3 drops to about $10^{-3}$.
- **Measured on 6 Oct:** IBM at 2×3 is a firm NO-GO ([[Result - 2x3 on ibm_kingston is a measured NO-GO]]). The
  re-sized 2×3 plan (rule D3'-R, sector $B=1$ doubled) costs 1 279 660 / 665 605 / 471 801 HQC at $f=0.05/0.10/0.15$;
  a Quantinuum access email exists as an unsent draft.
- The planned substantial result is the primary endpoint P1 (device support vs CIPSI/BFS/random/ML at equal size) on
  2×3 hardware data ([[CIPSI and classical support controls]]).
