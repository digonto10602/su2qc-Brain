---
type: "gate"
package: "genesis-su2-lgt"
gate: "G5"
status: "pass"
generated: True
as_of: "2026-10-06"
tags: ["gate", "genesis", "pass"]
---
# genesis gate G5

Gate of [[genesis-su2-lgt]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).

| | |
|---|---|
| checks | QML energy surrogate |
| runs on | exact ED plus mean/linear/RBF-SVR baselines |
| status | **PASS locally; no advantage claim** |
| tolerance | frozen split; MAE/RMSE/R² recorded |
| evidence / script | `tests/test_qml_data.py`, `benchmarks/results/qml_energy_surrogate.json` |
