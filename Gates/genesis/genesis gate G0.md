---
type: "gate"
package: "genesis-su2-lgt"
gate: "G0"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G0

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | core CPU starter |
| runs on | NumPy/SciPy and OpenMP smoke path |
| status | **PASS** |
| tolerance | mandatory checks pass |
| evidence / script | `./scripts/verify.sh`; isolated venv install record in `docs/RESEARCH_LOG.md` |
