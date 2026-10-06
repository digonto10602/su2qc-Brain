---
type: "concept"
tags: ["concept"]
aliases: ["CZ count"]
as_of: "2026-10-05"
---
# Transpilation and CZ count

**Plain words.** *Transpiling* rewrites a circuit into the gates and qubit connections a specific device supports.
Two-qubit gates (CZ on IBM Heron) are the main error source, so the CZ count after routing is the key cost. skqd's
original budget (≤ 250 CZ per coarse step at 2×2) failed (gates L3, S2) and was amended to a clean-fraction criterion.
