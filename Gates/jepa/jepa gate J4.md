---
type: "gate"
package: "su2qc-jepa"
gate: "J4"
status: "optional"
generated: True
as_of: "2026-10-06"
tags: ["gate", "jepa", "optional"]
---
# jepa gate J4

Gate of [[su2qc-jepa]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | quantum encoder |
| runs on | laptop / Perlmutter |
| status | **OPTIONAL** |
| evidence / script | configs/gates.yaml |

## Preregistered thresholds (`configs/gates.yaml`)

```yaml
J4_quantum_encoder:
  optional: true
  trains_at_qubits: 12
  matched_shot_test: preregistered
```
