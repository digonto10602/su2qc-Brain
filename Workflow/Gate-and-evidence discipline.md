---
type: "infra"
tags: ["workflow"]
aliases: ["gates"]
as_of: "2026-10-05"
---
# Gate-and-evidence discipline

**Plain words.** A **gate** is a scripted pass/fail checkpoint with numeric thresholds set in advance. Only gate
scripts decide PASS/FAIL; every number in a report is copied from the gate's JSON output, never typed by hand.
Used by all packages: genesis (G0–G12), skqd (E, S, L, H, P, M series), jepa (J0–J4). See [[Gates index]].
