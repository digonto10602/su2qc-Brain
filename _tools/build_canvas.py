"""Hand-laid-out Obsidian Canvas (JSON Canvas 1.0) of the SU2QC packages.
Called by build_vault.py; gate counts are filled in from the registry so the canvas stays current."""
import json
from pathlib import Path

COL = {"genesis": "6", "skqd": "5", "jepa": "4", "shared": "3", "hub": "1", "hw": "2", "trotter": "1", "qca": "5"}
# Obsidian preset colours: 1 red, 2 orange, 3 yellow, 4 green, 5 cyan, 6 purple


def build_canvas(vault: Path, reg: dict):
    nodes, edges = [], []

    def node(nid, x, y, w, h, **kw):
        nodes.append(dict(id=nid, x=x, y=y, width=w, height=h, **kw))
        return nid

    def fnode(nid, path, x, y, w, h, color=None):
        d = dict(type="file", file=path)
        if color:
            d["color"] = color
        return node(nid, x, y, w, h, **d)

    def tnode(nid, text, x, y, w, h, color=None):
        d = dict(type="text", text=text)
        if color:
            d["color"] = color
        return node(nid, x, y, w, h, **d)

    def edge(a, b, label=None, fs="bottom", ts="top", color=None, both=False):
        e = dict(id=f"e{len(edges)}", fromNode=a, fromSide=fs, toNode=b, toSide=ts)
        if label:
            e["label"] = label
        if color:
            e["color"] = color
        if both:
            e["fromEnd"] = "arrow"
        edges.append(e)

    def gate_summary(repo):
        gs = [g for g in reg.get("gates", []) if g["repo"] == repo]
        cnt = {}
        for g in gs:
            cnt[g["word"]] = cnt.get(g["word"], 0) + 1
        return ", ".join(f"{v} {k.upper()}" for k, v in sorted(cnt.items(), key=lambda kv: -kv[1])), gs

    # ---------------------------------------------------------------- top: proposal
    tnode("title", "# SU2QC packages — map\n*Built from every SU2QC repository on github.com/digonto10602 (refreshed 2026-10-06). Click any link to open its note.*",
          -1900, -1500, 1400, 140, COL["hub"])
    fnode("proposal", "Genesis Phase-I proposal.md", -1650, -1300, 900, 300, COL["hub"])

    # ---------------------------------------------------------------- columns
    X = {"genesis": -4050, "su2zx": -2850, "skqd": -1650, "shared": -450, "jepa": 650, "trotter": 1850, "qca": 3050}
    W = 1000
    top = -850

    # groups
    node("g_genesis", X["genesis"] - 40, top - 80, W + 80, 2600, type="group", label="genesis-su2-lgt (Aug 2026, dormant)", color=COL["genesis"])
    node("g_su2zx", X["su2zx"] - 40, top - 80, W + 80, 2600, type="group", label="SU2ZX = genesis-su2-zx-observables (Sept 2026, paused)", color="2")
    node("g_skqd", X["skqd"] - 40, top - 80, W + 80, 2600, type="group", label="su2qc-skqd (Project 2, active)", color=COL["skqd"])
    node("g_shared", X["shared"] - 40, top - 80, 980, 2600, type="group", label="Shared physics, methods and machines", color=COL["shared"])
    node("g_jepa", X["jepa"] - 40, top - 80, W + 80, 2600, type="group", label="su2qc-jepa (Gauge-JEPA-P v2, active)", color=COL["jepa"])

    # genesis column
    fnode("p_genesis", "Packages/genesis-su2-lgt.md", X["genesis"], top, W, 420, COL["genesis"])
    s, _ = gate_summary("genesis-su2-lgt")
    tnode("genesis_code", "### Code layers\n- Physics: [[genesis_su2.pauli]] · [[genesis_su2.exact]] · [[genesis_su2.su2]]\n"
          "- Encodings: [[genesis_su2.encodings]] (electric vs rishon; fuzzy blocked)\n"
          "- Backends: [[genesis_su2.backends.qiskit_backend|Qiskit]] · [[genesis_su2.backends.cudaq_backend|CUDA-Q]] · [[genesis_su2.backends.ibm_runtime|IBM Runtime]] · OpenMP · CUDA\n"
          "- QML: [[genesis_su2.qml.energy_surrogate]]", X["genesis"], top + 460, W, 300)
    tnode("genesis_gates", f"### Gates G0–G7.8\n{s}\n\nOpen: G7.5–G7.6 matched Hamiltonians, G9 tensor networks, G12 hardware dry run.\n\n[[Gates index]]",
          X["genesis"], top + 800, W, 260)
    fnode("r_genesis", "Results/Result - genesis QML surrogate is a negative result.md", X["genesis"], top + 1100, W, 260, COL["genesis"])
    tnode("genesis_ladder", "### Research ladder it proposed\n1 exact → 2 statevector → 3 IBM → 4 QML surrogate → 5 plaquette chain + MPS → "
          "**6 quarks + string breaking** → **7 2+1D dressed-site model** → 8 AI calibration\n\nSteps 6–7 are now done by su2qc-skqd and su2qc-jepa.",
          X["genesis"], top + 1400, W, 260)
    fnode("k_kavaki", "Papers/Kavaki and Lewis 2024.md", X["genesis"], top + 1700, W, 200)

    # skqd column
    fnode("p_skqd", "Packages/su2qc-skqd.md", X["skqd"], top, W, 420, COL["skqd"])
    tnode("skqd_code", "### Code layers\n- Physics: [[skqd.su2]] → [[skqd.vertex]] → [[skqd.basis]] → [[skqd.hamiltonian]] (2nd route [[skqd.fullspace]]) → [[skqd.exact]]\n"
          "- Circuits: [[skqd.circuits_ir]] → Qiskit / CUDA-Q / [[skqd.quantinuum_native|Quantinuum]]; [[skqd.codec]] decoder\n"
          "- Algorithm: [[skqd.krylov]] → [[skqd.skqd]] (Ritz + certificates) · [[skqd.controls]] · [[skqd.ml]]\n"
          "- Device model: [[skqd.noise]] · [[skqd.idle]] · [[skqd.coherence]] · [[skqd.device_req]] · [[skqd.hardware]]",
          X["skqd"], top + 460, W, 300)
    s, _ = gate_summary("su2qc-skqd")
    tnode("skqd_gates", f"### Gates (E, S, L, H, P, M series)\n{s} — counting every validation file, including dry runs and diagnostics\n\nExact physics E1–E3 PASS · hardware [[skqd gate H0_2x2]] PASS · "
          "budget gates S2/S2D FAIL (criterion amended) · [[skqd gate CF_traj]] PASS 7/7 · 6 Oct: [[skqd gate H0_ddrep]] (XY4 not replicated), "
          "[[skqd gate K1_2x3_fpilot]] (2x3 NO-GO) · H1, H2, P1, M1 open · QPU 327 s used, 273 s left",
          X["skqd"], top + 800, W, 260)
    fnode("r_skqd_2x2", "Results/Result - 2x2 SKQD run on ibm_kingston.md", X["skqd"], top + 1100, W, 300, COL["skqd"])
    fnode("r_skqd_dd", "Results/Result - client-side XY4 gain did not replicate.md", X["skqd"], top + 1430, W, 200, COL["skqd"])
    fnode("r_skqd_2x3", "Results/Result - 2x3 needs a different device.md", X["skqd"], top + 1660, W, 240, COL["skqd"])
    fnode("r_skqd_cf", "Results/Result - CF_traj clean-fraction re-ruling.md", X["skqd"], top + 1930, W, 220, COL["skqd"])
    fnode("r_skqd_k1", "Results/Result - 2x3 on ibm_kingston is a measured NO-GO.md", X["skqd"], top + 2180, W, 260, COL["skqd"])

    # shared column
    sx, sw = X["shared"], 900
    fnode("plaq", "Cross-package/Shared 2x2 plaquette.md", sx, top, sw, 420, COL["shared"])
    fnode("c_su2", "Concepts/Physics/SU(2) lattice gauge theory.md", sx, top + 460, sw, 170)
    fnode("c_gauss", "Concepts/Physics/Gauss's law.md", sx, top + 650, sw, 170)
    fnode("c_krylov", "Concepts/Methods/Krylov subspace and Lanczos.md", sx, top + 840, sw, 170)
    fnode("c_cf", "Concepts/Methods/Clean-shot fraction.md", sx, top + 1030, sw, 170)
    fnode("h_kingston", "Hardware/ibm_kingston.md", sx, top + 1220, sw, 150, COL["hw"])
    fnode("h_perl", "Hardware/NERSC Perlmutter.md", sx, top + 1390, sw, 150, COL["hw"])
    fnode("w_graphify", "Workflow/Graphify code graph.md", sx, top + 1560, sw, 150)
    fnode("w_agents", "Workflow/Agent routing (planner, executor, reviewer, runner, scribe).md", sx, top + 1730, sw, 200)
    fnode("opps", "Cross-package/Cross-package opportunities.md", sx, top + 1960, sw, 200, COL["hub"])

    # jepa column
    fnode("p_jepa", "Packages/su2qc-jepa.md", X["jepa"], top, W, 420, COL["jepa"])
    tnode("jepa_code", "### Code layers\n- Physics: [[su2qc_jepa.physics.plaquette]] (routes A/B) · [[su2qc_jepa.physics.dynamics]] · [[su2qc_jepa.physics.chain]] (12-qubit carrier)\n"
          "- Data: [[su2qc_jepa.data.trajectories]] · [[su2qc_jepa.data.records]]\n"
          "- Model: [[su2qc_jepa.models.jepa]] (encoder → 16-d latent → GRU predictor, SIGReg) · [[su2qc_jepa.models.train]]\n"
          "- Twin/hardware: [[su2qc_jepa.twin.run]] · [[su2qc_jepa.hardware.ibm]] · Compute: [[su2qc_jepa.localrun]] · [[su2qc_jepa.jobs]]",
          X["jepa"], top + 460, W, 300)
    s, _ = gate_summary("su2qc-jepa")
    tnode("jepa_gates", f"### Gates J0–J4\n{s}\n\n[[jepa gate J0]] PASS 9/9 · [[jepa gate J1]] FAIL for all 9 finished runs (semigroup row), jobs 013–014 queued · J2 forecasting, J3 hardware error signal not run · J4 optional\n\nPlan: 5 Oct – 29 Nov 2026",
          X["jepa"], top + 800, W, 260)
    fnode("r_j0", "Results/Result - J0 data gate passed.md", X["jepa"], top + 1100, W, 240, COL["jepa"])
    fnode("r_j1", "Results/Result - J1 energy information ceiling.md", X["jepa"], top + 1370, W, 200, COL["jepa"])
    fnode("c_jepa", "Concepts/Methods/JEPA world model.md", X["jepa"], top + 1600, W, 240)
    fnode("c_chain", "Concepts/Methods/Krylov-chain carrier.md", X["jepa"], top + 1870, W, 240)
    fnode("r_j1_ladder", "Results/Result - J1 ladder fails on the semigroup row.md", X["jepa"], top + 2140, W, 300, COL["jepa"])

    # SU2ZX (external) above jepa/shared
    # SU2ZX column
    fnode("p_su2zx", "Packages/SU2ZX.md", X["su2zx"], top, W, 420, "2")
    tnode("su2zx_code", "### Code layers\n- v0.4.0 chain study: [[su2zx.core]] → [[su2zx.compiler_study]] · [[su2zx.robust_study]] · [[su2zx.scaling_study]] (MPS) · [[su2zx.qpu]]\n"
          "- v0.5.0 plaquette + quarks: [[su2qc.ham.route_spinnet]] vs [[su2qc.ham.route_gausskernel]] → [[su2qc.dynamics.engine]]\n"
          "- Circuits: [[su2qc.encodings.l12]] → [[su2qc.circuits.strang_l12]] (≈2 156 2q gates per step) · twin [[su2qc.twin.twin]]",
          X["su2zx"], top + 460, W, 300)
    s, _ = gate_summary("SU2ZX")
    tnode("su2zx_gates", f"### Gates\n{s}\n\nSection 8: [[su2zx gate S8-G1]] PASS (82 states, two routes) · G4 never run\nGI-cost campaign: [[su2zx gate C1]] PASS · [[su2zx gate C0]] PARTIAL · C2–C8 not started",
          X["su2zx"], top + 800, W, 260)
    fnode("r_su2zx_v040", "Results/Result - SU2ZX v0.4.0 compiler and MPS study.md", X["su2zx"], top + 1100, W, 300, "2")
    fnode("r_su2zx_s8", "Results/Result - SU2ZX section 8 verified plaquette.md", X["su2zx"], top + 1430, W, 300, "2")
    fnode("r_su2zx_c0", "Results/Result - GI-cost campaign stalled at C0.md", X["su2zx"], top + 1760, W, 300, "2")
    fnode("lessons", "Cross-package/Lessons that travelled.md", 1850, -1450, 700, 360, COL["hub"])

    # su2qc-trotter column (with the su2qc-paulo-code reference circuit)
    node("g_trotter", X["trotter"] - 40, top - 80, W + 80, 2600, type="group", label="su2qc-trotter + su2qc-paulo-code (Sept 2026, done)", color=COL["trotter"])
    fnode("p_trotter", "Packages/su2qc-trotter.md", X["trotter"], top, W, 420, COL["trotter"])
    tnode("trotter_code", "### Code layers\n- Physics: [[su2trotter.physics]] (plaquette operator, Eqs. 25-28)\n"
          "- Designs: [[su2trotter.baseline]] (Eq. 39, 34 qubits) vs [[su2trotter.lean]] (22 qubits)\n"
          "- Compile + count: [[su2trotter.synth]] → [[su2trotter.cudaq_backend]] · [[su2trotter.pipeline]]\n"
          "- Checks: [[su2trotter.sim]] · [[su2trotter.analysis]] · [[su2trotter.compare]]",
          X["trotter"], top + 460, W, 300)
    s, _ = gate_summary("su2qc-trotter")
    tnode("trotter_gates", f"### Perlmutter CI jobs\n{s}\n\n[[trotter gate R1]] resources · [[trotter gate V1]] GPU verification · [[trotter gate B1]] 60-step benchmark · "
          "[[trotter gate G22]] / [[trotter gate G34]] side-by-side tests (G34 on 32 A100s)",
          X["trotter"], top + 800, W, 260)
    fnode("r_trotter_lean", "Results/Result - lean 22-qubit plaquette Trotter step.md", X["trotter"], top + 1100, W, 300, COL["trotter"])
    fnode("r_trotter_gpu", "Results/Result - lean and reference circuits agree on GPUs.md", X["trotter"], top + 1430, W, 260, COL["trotter"])
    fnode("p_paulo", "Packages/su2qc-paulo-code.md", X["trotter"], top + 1720, W, 300, COL["trotter"])
    fnode("c_cliffordt", "Concepts/Methods/Clifford+T and T-count.md", X["trotter"], top + 2050, W, 150)

    # su2qc-qcadvantage column
    node("g_qca", X["qca"] - 40, top - 80, W + 80, 2600, type="group", label="su2qc-qcadvantage (Oct 2026, cloud phase done)", color=COL["qca"])
    fnode("p_qca", "Packages/su2qc-qcadvantage.md", X["qca"], top, W, 420, COL["qca"])
    tnode("qca_code", "### Code layers\n- Model: [[su2torus.lattice]] (honeycomb torus) → [[su2torus.hamiltonian]]\n"
          "- Exact: [[su2torus.exact]] · [[su2torus.observables]] · [[su2torus.thermal]] (typicality anchors)\n"
          "- Circuits + noise: [[su2torus.trotter]] → [[su2torus.noise]] (echo, ZNE)\n"
          "- Classical frontier: [[su2torus.mps]] (quimb MPS)",
          X["qca"], top + 460, W, 300)
    s, _ = gate_summary("su2qc-qcadvantage")
    tnode("qca_gates", f"### Milestones M1-M6 (locked acceptance tests)\n{s}\n\nFull suite 167 passed; tag v0.1-pre-cluster. "
          "Stopped before GPU-cluster work; 4 decisions wait: [[Decision - qcadvantage open questions before the cluster]]",
          X["qca"], top + 800, W, 260)
    fnode("r_qca_therm", "Results/Result - qcadvantage thermalization and the beta=0 states.md", X["qca"], top + 1100, W, 260, COL["qca"])
    fnode("r_qca_noise", "Results/Result - qcadvantage noise mitigation at N=12.md", X["qca"], top + 1390, W, 260, COL["qca"])
    fnode("r_qca_mps", "Results/Result - qcadvantage MPS frontier at N=48.md", X["qca"], top + 1680, W, 300, COL["qca"])
    fnode("c_1qpp", "Concepts/Physics/One-qubit-per-plaquette SU(2) model.md", X["qca"], top + 2010, W, 190)
    fnode("lineage", "Cross-package/Package lineage.md", -2850, -1300, 1000, 300, COL["hub"])

    # ---------------------------------------------------------------- edges
    edge("proposal", "p_genesis", "starter (Aug)", fs="left")
    edge("proposal", "p_su2zx", "Sept campaign", fs="left")
    edge("proposal", "p_skqd", "Project 2")
    edge("proposal", "p_jepa", "AI world model")
    edge("p_genesis", "p_su2zx", "led to (step 5)", fs="right", ts="left")
    edge("r_su2zx_s8", "plaq", "verified first", fs="right", ts="left", color="3")
    edge("p_su2zx", "p_jepa", "cross-check 7e-14", fs="top", ts="top", color="4")
    edge("r_su2zx_c0", "lessons", "twin-seed lesson", fs="right", ts="left")
    edge("p_su2zx", "p_skqd", "plaquette + quarks", fs="right", ts="left")
    edge("p_skqd", "plaq", "same system", fs="right", ts="left", color="3")
    edge("p_jepa", "plaq", "same system", fs="left", ts="right", color="3")
    edge("r_skqd_2x2", "h_kingston", "run on", fs="right", ts="left", color="2")
    edge("r_skqd_dd", "c_cf", "2.8x on 2 Oct, 0.9x on 6 Oct", fs="right", ts="left")
    edge("r_skqd_cf", "c_cf", "re-ruled statistic", fs="right", ts="left")
    edge("jepa_gates", "h_perl", "J1 jobs", fs="left", ts="right", color="2")
    edge("skqd_gates", "h_perl", "CI tokens", fs="right", ts="left", color="2")
    edge("c_chain", "c_krylov", "Lanczos K=12", fs="left", ts="right")
    edge("skqd_code", "c_krylov", "Krylov states", fs="right", ts="left")
    edge("r_skqd_dd", "jepa_gates", "day-to-day drift: lesson for J3", fs="right", ts="left", color="1")
    edge("genesis_ladder", "p_su2zx", "steps 5-7", fs="right", ts="left", color="6")
    edge("plaq", "c_su2", fs="bottom", ts="top")
    edge("c_su2", "c_gauss", fs="bottom", ts="top")
    edge("k_kavaki", "p_genesis", "Eq. 1", fs="right", ts="right")

    edge("r_skqd_k1", "r_skqd_2x3", "measured", fs="left", ts="left", color="5")
    edge("r_j1", "r_j1_ladder", "energy rows pass", fs="left", ts="left")
    edge("p_paulo", "p_trotter", "Eq. 39 baseline", fs="right", ts="right", color="1")
    edge("proposal", "p_trotter", "fault-tolerant cost", fs="right")
    edge("proposal", "p_qca", "advantage path", fs="right")
    edge("skqd_gates", "trotter_gates", "same CI design", fs="bottom", ts="bottom", color="2")
    edge("trotter_gates", "h_perl", "GPU jobs", fs="left", ts="right", color="2")
    edge("r_qca_mps", "r_su2zx_v040", "MPS: chain vs 2D torus", fs="bottom", ts="bottom")
    edge("c_1qpp", "c_su2", "minimal truncation", fs="left", ts="right")

    canvas = {"nodes": nodes, "edges": edges}
    (vault / "SU2QC Map.canvas").write_text(json.dumps(canvas, indent=2), encoding="utf-8")
    return canvas
