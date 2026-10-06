#!/usr/bin/env python3
"""Build (or refresh) the SU2QC Brain Obsidian vault from the package repositories.

    python build_vault.py --repos /path/holding/the/repos --vault ..   (default vault = parent of _tools)

Generated folders (Modules/, Gates/, the *index notes, the canvas) are rewritten on every run.
Hand-written notes come from content_packages.py and content_concepts.py and are written only if missing,
unless --overwrite-hand is given, so edits you make in Obsidian survive a refresh.
"""
import argparse, ast, json, re, shutil, subprocess, sys, warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from content_packages import NOTES  # noqa: E402
from content_concepts import CONCEPTS  # noqa: E402

# One entry per python package.  dir = repository folder, src = package folder inside it,
# short = prefix for module/gate folders and gate note names, note = title of the package note,
# gates = which gate parser to use (one per repository; None for a second package in the same repo).
PACKAGES = [
    dict(dir="su2qc-skqd", src="src/skqd", short="skqd", note="su2qc-skqd", gates="skqd"),
    dict(dir="su2qc-jepa", src="src/su2qc_jepa", short="jepa", note="su2qc-jepa", gates="jepa"),
    dict(dir="genesis-su2-lgt", src="src/genesis_su2", short="genesis", note="genesis-su2-lgt", gates="genesis"),
    dict(dir="genesis-su2-zx-observables", src="src/su2zx", short="su2zx", note="SU2ZX", gates="su2zx"),
    dict(dir="genesis-su2-zx-observables", src="runs/section8_v0.5.0_20260907T0628Z/src/su2qc", short="su2zx", note="SU2ZX", gates=None),
    dict(dir="su2qc-trotter", src="src/su2trotter", short="trotter", note="su2qc-trotter", gates="trotter"),
    dict(dir="su2qc-qcadvantage", src="su2torus", short="qca", note="su2qc-qcadvantage", gates="qca"),
]
# Local checkouts whose folder name differs from the repository name (first existing folder wins).
ALT_DIRS = {
    "su2qc-skqd": ["su2qc-skqd-v0.1.0"],
    "genesis-su2-zx-observables": ["SU2ZX_Foundation_Code_Package/SU2ZX"],
}
NOTES_ORDER = list(dict.fromkeys(p["note"] for p in PACKAGES))
TODAY = date.today().isoformat()


# ----------------------------------------------------------------------------- helpers
def repo_dir(repos: Path, name: str) -> Path:
    for d in [name] + ALT_DIRS.get(name, []):
        if (repos / d).is_dir():
            return repos / d
    return repos / name


def yaml_value(v):
    if isinstance(v, list):
        return "[" + ", ".join(json.dumps(x) for x in v) + "]"
    if isinstance(v, (int, float)):
        return str(v)
    return json.dumps(str(v))


def write_note(path: Path, fm: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---"] + [f"{k}: {yaml_value(v)}" for k, v in fm.items() if v not in (None, "", [])] + ["---", ""]
    path.write_text("\n".join(lines) + body, encoding="utf-8")


def mod_name(pkg_dir: Path, f: Path) -> str:
    rel = f.relative_to(pkg_dir.parent).with_suffix("")
    return ".".join(rel.parts)


def clean_doc(d: str) -> str:
    d = (d or "").strip()
    d = d.replace("[[", "[ [").replace("]]", "] ]")
    return d


def concept_links(text: str):
    out = []
    for title, spec in CONCEPTS.items():
        if spec["type"] in ("paper", "decision", "hardware") and spec["folder"] != "Hardware":
            continue
        try:
            if re.search(spec["regex"], text):
                out.append(title)
        except re.error:
            pass
    return out


def git_info(repo: Path):
    try:
        h = subprocess.run(["git", "-C", str(repo), "log", "-1", "--format=%h %cs"], capture_output=True, text=True).stdout.strip()
        n = subprocess.run(["git", "-C", str(repo), "rev-list", "--count", "HEAD"], capture_output=True, text=True).stdout.strip()
        b = subprocess.run(["git", "-C", str(repo), "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
        return h, n, b
    except Exception:
        return "", "", ""


def imports_of(src: str, top: str):
    """Return dotted module names under `top` imported by this source."""
    out = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            m = node.module
            if node.level and node.level > 0:
                continue
            if m == top or m.startswith(top + "."):
                if m == top:
                    for a in node.names:
                        out.add(f"{top}.{a.name}")
                else:
                    out.add(m)
                    for a in node.names:
                        out.add(f"{m}.{a.name}")
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name == top or a.name.startswith(top + "."):
                    out.add(a.name)
    return out


def relative_imports(src: str, modname: str):
    out = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    base = modname.split(".")
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.level:
            parent = base[:-node.level] if node.level <= len(base) else []
            target = parent + (node.module.split(".") if node.module else [])
            for a in node.names:
                out.add(".".join(target + [a.name]))
            out.add(".".join(target))
    return out


# ----------------------------------------------------------------------------- modules
def build_modules(repos: Path, vault: Path, registry: dict):
    allmods = {}
    for P in PACKAGES:
        repo_name, pkg_rel, short = P["note"], P["src"], P["short"]
        repo = repo_dir(repos, P["dir"])
        pkg_dir = repo / pkg_rel
        if not pkg_dir.is_dir():
            print(f"  [skip] {repo_name}: {pkg_dir} not found")
            continue
        top = pkg_dir.name
        files = sorted(p for p in pkg_dir.rglob("*.py") if p.name != "__init__.py")
        names = {mod_name(pkg_dir, f): f for f in files}
        for name, f in names.items():
            src = f.read_text(encoding="utf-8", errors="replace")
            try:
                doc = ast.get_docstring(ast.parse(src)) or ""
            except SyntaxError:
                doc = ""
            imps = imports_of(src, top) | relative_imports(src, name)
            deps = sorted({n for n in names if n != name and any(i == n or i.startswith(n + ".") for i in imps)})
            try:
                tree = ast.parse(src)
                defs = [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and not n.name.startswith("_")]
            except SyntaxError:
                defs = []
            allmods[name] = dict(repo=repo_name, short=short, file=f.relative_to(repo).as_posix(), doc=doc,
                                 deps=deps, lines=src.count("\n") + 1, defs=defs, top=top)
    users = {n: [] for n in allmods}
    for n, m in allmods.items():
        for d in m["deps"]:
            users[d].append(n)
    for n, m in allmods.items():
        concepts = concept_links(m["doc"])
        sub = n.split(".")[1] if n.count(".") >= 2 else ""
        body = [f"# {n}", "", f"Module of [[{m['repo']}]] · `{m['file']}` · {m['lines']} lines", ""]
        body += ["## What it does (from the module docstring)", ""]
        doc = clean_doc(m["doc"]) or "*(no docstring)*"
        body += ["> " + line if line.strip() else ">" for line in doc.splitlines()] + [""]
        if m["deps"]:
            body += ["## Uses", "", " · ".join(f"[[{d}]]" for d in m["deps"]), ""]
        if users[n]:
            body += ["## Used by", "", " · ".join(f"`{u}`" for u in sorted(users[n])), ""]
        if m["defs"]:
            shown = m["defs"][:25]
            body += ["## Public names", "", ", ".join(f"`{d}`" for d in shown) + (" …" if len(m["defs"]) > 25 else ""), ""]
        if concepts:
            body += ["## Concepts", "", " · ".join(f"[[{c}]]" for c in concepts), ""]
        gates = registry.get("module_gates", {}).get(n, [])
        if gates:
            body += ["## Checked by gates", "", " · ".join(f"[[{g}]]" for g in sorted(gates)), ""]
        fm = dict(type="module", package=m["repo"], file=m["file"], lines=m["lines"], generated=True,
                  as_of=TODAY, tags=["module", m["short"]] + ([sub] if sub and sub != n.split(".")[-1] else []))
        write_note(vault / "Modules" / m["short"] / f"{n}.md", fm, "\n".join(body))
    registry["modules"] = allmods
    return allmods


# ----------------------------------------------------------------------------- gates
def status_word(s: str):
    s2 = s.upper()
    for w in ("PARTIAL", "COMPLETED-NEGATIVE", "NOT STARTED", "PASS", "FAIL", "NOT RUN", "OPEN", "OPTIONAL"):
        if w in s2:
            return w.lower().replace(" ", "-")
    return "unknown"


def parse_md_table(text: str):
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


def script_modules(path: Path, top: str, known: dict):
    if not path.exists():
        return []
    imps = imports_of(path.read_text(encoding="utf-8", errors="replace"), top)
    return sorted({n for n in known if any(i == n or i.startswith(n + ".") for i in imps)})


def gates_skqd(repo: Path, known):
    out = []
    gm = repo / "validation" / "gates.md"
    if not gm.exists():
        return out
    for cells in parse_md_table(gm.read_text())[1:]:
        if len(cells) < 4:
            continue
        gid, check, runs, status = cells[:4]
        status = status.replace("**", "")
        cands = [repo / "scripts" / f"gate_{gid}.py"] + sorted((repo / "scripts").glob(f"laptop_{gid}_*.py"))
        if gid in ("L4_fez",):
            cands += [repo / "scripts" / "laptop_L4_aer_noise.py"]
        if gid.startswith("H0") or gid in ("H1", "H2"):
            cands += [repo / "scripts" / "gate_H0.py"]
        if gid == "S3":
            cands += [repo / "scripts" / "s3_device_model.py"]
        script = next((p for p in cands if p.exists()), None)
        mods = script_modules(script, "skqd", known) if script else []
        out.append(dict(id=gid, check=check, runs_on=runs, status=status, word=status_word(status),
                        script=script.relative_to(repo).as_posix() if script else None, modules=mods))
    # gates that have a validation JSON but are not (yet) in the generated table
    seen = {g["id"] for g in out}
    for j in sorted((repo / "validation").glob("*.json")):
        gid = j.stem
        if gid in seen or gid.startswith("ci_"):
            continue
        try:
            d = json.loads(j.read_text())
        except Exception:
            continue
        if not isinstance(d, dict) or "status" not in d:
            continue
        crit = d.get("criteria") or []
        nfail = sum(1 for c in crit if isinstance(c, dict) and c.get("passed") is False)
        status = f"{d['status']} ({len(crit)} criteria, {nfail} failing)" if crit else str(d["status"])
        script = next((p for p in [repo / "scripts" / f"gate_{gid}.py"] if p.exists()), None)
        mods = script_modules(script, "skqd", known) if script else []
        out.append(dict(id=gid, check=str(d.get("title", "")), runs_on="see validation JSON", status=status,
                        word=status_word(str(d["status"])), script=f"validation/{j.name}", modules=mods))
    return out


def gates_jepa(repo: Path, known):
    out = []
    state = {}
    try:
        state = json.loads((repo / "STATE.json").read_text())
    except Exception:
        pass
    ledger = (repo / "evidence" / "GATE_LEDGER.md").read_text() if (repo / "evidence" / "GATE_LEDGER.md").exists() else ""
    ytext = (repo / "configs" / "gates.yaml").read_text() if (repo / "configs" / "gates.yaml").exists() else ""
    blocks = re.split(r"\n(?=J\d_\w+:)", ytext)
    gate_mod = {"J0": "su2qc_jepa.gates.j0_data", "J1": "su2qc_jepa.gates.j1_training",
                "J2": "su2qc_jepa.gates.j2_forecast", "J3": "su2qc_jepa.gates.j3_hardware"}
    for b in blocks:
        m = re.match(r"(J\d)_(\w+):", b.strip())
        if not m:
            continue
        gid, name = m.group(1), m.group(2)
        hits = re.findall(rf"##\s*{gid}_\w+\s*[—-]\s*([A-Z ]+?)\s*[—-]", ledger)
        word = hits[-1].strip() if hits else ("OPTIONAL" if "optional: true" in b else "NOT RUN")
        if not hits:  # the ledger is written by every gate run; STATE.json can lag behind it
            for ms in state.get("milestones", {}).values():
                if isinstance(ms, dict) and ms.get("gate") == gid and ms.get("gate_status"):
                    word = ms["gate_status"]
        elif len(hits) > 1:
            word = f"{word} (latest of {len(hits)} ledger entries: " + ", ".join(f"{hits.count(h)} {h.strip()}" for h in dict.fromkeys(hits)) + ")"
        mods = [gate_mod[gid]] if gid in gate_mod and gate_mod[gid] in known else []
        out.append(dict(id=gid, check=name.replace("_", " "), runs_on="laptop / Perlmutter", status=word,
                        word=status_word(word), script="configs/gates.yaml", modules=mods,
                        thresholds=b.strip()))
    return out


def gates_genesis(repo: Path, known):
    out = []
    vm = repo / "docs" / "VALIDATION_MATRIX.md"
    if not vm.exists():
        return out
    for cells in parse_md_table(vm.read_text())[1:]:
        if len(cells) < 5 or not cells[0].startswith("G"):
            continue
        claim, oracle, art, tol, status = cells[:5]
        gid = claim.split()[0]
        mods = set()
        for t in re.findall(r"`(tests/[\w/]+\.py)`", art):
            mods |= set(script_modules(repo / t, "genesis_su2", known))
        out.append(dict(id=gid, check=claim[len(gid):].strip(), runs_on=oracle, status=status,
                        word=status_word(status), script=art, modules=sorted(mods), tolerance=tol))
    return out


def gates_su2zx(repo: Path, known):
    """Section 8 overnight run gates G0-G4 (GATE_G*.json) and GI-cost campaign gates C0-C8."""
    out = []
    run = repo / "runs" / "section8_v0.5.0_20260907T0628Z"
    for gpy in sorted((run / "gates").glob("gate_G*.py")):
        gid = gpy.stem.split("_")[1]
        js = run / "gates" / f"GATE_{gid}.json"
        if js.exists():
            d = json.loads(js.read_text())
            crit = d.get("criteria") or []
            nfail = sum(1 for c in crit if isinstance(c, dict) and c.get("pass") is False)
            status = f"{d.get('status')} ({len(crit)} criteria, {nfail} not met; attempt {d.get('attempt')})"
            names = ", ".join(str(c.get("name")) for c in crit[:12])
            check = f"Section 8 v0.5.0 overnight run - criteria: {names}"
        else:
            status, check = "NOT RUN", "Section 8 v0.5.0 overnight run - gate script written, never run"
        mods = sorted({n for n in known if n.startswith("su2qc.")} & set(script_modules(gpy, "su2qc", known)))
        out.append(dict(id=f"S8-{gid}", check=check, runs_on="laptop (twin mode, FakeTorino)", status=status,
                        word=status_word(status), script=gpy.relative_to(repo).as_posix(), modules=mods))
    camp = repo / "runs" / "campaign_v060"
    state = {}
    try:
        state = json.loads((camp / "CAMPAIGN_STATE.json").read_text())
    except Exception:
        pass
    defs = {}
    prompts = sorted((repo / "prompts").glob("gi_cost_campaign_v.*.md"))
    if prompts:
        for cells in parse_md_table(prompts[-1].read_text()):
            if cells and re.match(r"^C\d", cells[0]):
                defs[cells[0]] = cells[1] if len(cells) > 1 else ""
    for gid in [f"C{i}" for i in range(9)]:
        st = state.get("gates", {}).get(gid, {})
        key = gid if gid in defs else ("C6–C8" if gid in ("C6", "C7", "C8") else gid)
        word = st.get("status") or ("BLOCKED" if gid in ("C6", "C7", "C8") else "NOT RUN")
        detail = "; ".join(st.get("failed", [])) if st.get("failed") else ""
        status = f"{word.upper()}" + (f" - open: {detail}" if detail else "")
        out.append(dict(id=gid, check=f"GI-cost campaign v0.6.x: {defs.get(key, '')}", runs_on="laptop / cluster (Hermes)",
                        status=status, word=status_word(status) if word.upper() != "BLOCKED" else "blocked",
                        script="runs/campaign_v060/CAMPAIGN_STATE.json", modules=[]))
    return out


def gates_trotter(repo: Path, known):
    """Perlmutter CI jobs (validation/ci_<token>.json); job descriptions from the table in TROTTER-CI-SETUP.md."""
    out = []
    setup = repo / "TROTTER-CI-SETUP.md"
    what = {}
    if setup.exists():
        for cells in parse_md_table(setup.read_text()):
            if len(cells) >= 3 and re.match(r"^`\w+`$", cells[0]):
                what[cells[0].strip("`")] = (cells[1], cells[2])
    for j in sorted((repo / "validation").glob("ci_*.json")):
        d = json.loads(j.read_text())
        gid = d.get("gate") or j.stem[3:]
        if "pass" in d:
            ok = d["pass"]
            status = f"{'PASS' if ok else 'FAIL'} (job {d.get('jobid')}, {d.get('seconds')} s" + (f", {d['nodes']} nodes" if d.get("nodes") else "") + ")"
        else:
            checks = d.get("checks") or {}
            ok = bool(checks) and all(isinstance(c, dict) and c.get("pass") for c in checks.values())
            status = f"{'PASS' if ok else 'FAIL'} ({len(checks)} checks, job {d.get('jobid')})"
        wall, job = what.get(gid, ("", ""))
        mods = []
        for sc in re.findall(r"`(scripts/[\w/]+\.py)", job):
            mods += script_modules(repo / sc, "su2trotter", known)
        out.append(dict(id=gid, check=re.sub(r"`", "", job) or "Perlmutter CI job", runs_on=f"Perlmutter GPU via trotter-ci ({wall})" if wall else "Perlmutter GPU via trotter-ci",
                        status=status, word=status_word(status), script=f"validation/{j.name}", modules=sorted(set(mods))))
    return out


def gates_qca(repo: Path, known):
    """Milestones M1-M6 with LOCKED acceptance tests (tests/acceptance/mN); status from notes/STATUS.md, title from plan/PLAN.md."""
    out = []
    try:
        locked = json.loads((repo / "tests" / "acceptance" / "LOCK.json").read_text()).get("milestones", [])
    except Exception:
        locked = []
    plan = (repo / "plan" / "PLAN.md").read_text() if (repo / "plan" / "PLAN.md").exists() else ""
    titles = dict(re.findall(r"^## (M\d+) [—-] (.+)$", plan, re.M))
    status_md = (repo / "notes" / "STATUS.md").read_text() if (repo / "notes" / "STATUS.md").exists() else ""
    results = dict(re.findall(r"^- (M\d+): (.+)$", status_md, re.M))
    audits = {p.stem for p in (repo / "reports" / "audits").glob("*.md")} if (repo / "reports" / "audits").is_dir() else set()
    for ms in sorted({m.upper() for m in locked} | set(titles)):
        tdir = repo / "tests" / "acceptance" / ms.lower()
        mods = set()
        for t in sorted(tdir.glob("*.py")):
            mods |= set(script_modules(t, "su2torus", known))
        res = results.get(ms, "")
        if res:
            status = "PASS (locked acceptance tests green" + ("; audit PASS" if "Audit PASS" in res or "audit PASS" in res.lower() else "") + ")"
        else:
            status = "NOT RUN" if ms.lower() in locked else "NOT STARTED"
        aud = [a for a in sorted(audits) if ms.lower() in a or (a.startswith("m2_m5") and ms in ("M2", "M3", "M4", "M5"))]
        out.append(dict(id=ms, check=titles.get(ms, "milestone") + (f". Outcome: {res}" if res else ""),
                        runs_on="cloud session (4 vCPU, 16 GB); no GPU cluster yet", status=status, word=status_word(status),
                        script=f"tests/acceptance/{ms.lower()}" + (f"; audits: {', '.join('reports/audits/' + a + '.md' for a in aud)}" if aud else ""),
                        modules=sorted(mods)))
    return out


def build_gates(repos: Path, vault: Path, registry: dict):
    known = registry["modules"]
    allg = []
    fns = {"skqd": gates_skqd, "jepa": gates_jepa, "genesis": gates_genesis, "su2zx": gates_su2zx,
           "trotter": gates_trotter, "qca": gates_qca}
    for P in PACKAGES:
        repo_name, short = P["note"], P["short"]
        repo = repo_dir(repos, P["dir"])
        if not repo.is_dir() or not P["gates"]:
            continue
        for g in fns[P["gates"]](repo, known):
            g["repo"], g["short"] = repo_name, short
            g["title"] = f"{short} gate {g['id']}"
            allg.append(g)
    mg = {}
    for g in allg:
        for m in g["modules"]:
            mg.setdefault(m, []).append(g["title"])
        body = [f"# {g['title']}", "", f"Gate of [[{g['repo']}]] — a scripted pass/fail checkpoint ([[Gate-and-evidence discipline]]).", "",
                "| | |", "|---|---|", f"| checks | {g['check']} |", f"| runs on | {g['runs_on']} |",
                f"| status | **{g['status']}** |"]
        if g.get("tolerance"):
            body.append(f"| tolerance | {g['tolerance']} |")
        if g.get("script"):
            body.append(f"| evidence / script | {g['script']} |")
        body.append("")
        if g.get("thresholds"):
            body += ["## Preregistered thresholds (`configs/gates.yaml`)", "", "```yaml", g["thresholds"], "```", ""]
        if g["modules"]:
            body += ["## Code it exercises", "", " · ".join(f"[[{m}]]" for m in g["modules"]), ""]
        concepts = concept_links(g["check"] + " " + g["status"])
        if concepts:
            body += ["## Concepts", "", " · ".join(f"[[{c}]]" for c in concepts), ""]
        fm = dict(type="gate", package=g["repo"], gate=g["id"], status=g["word"], generated=True, as_of=TODAY,
                  tags=["gate", g["short"], g["word"]])
        write_note(vault / "Gates" / g["short"] / f"{g['title']}.md", fm, "\n".join(body))
    registry["gates"] = allg
    registry["module_gates"] = mg
    return allg


# ----------------------------------------------------------------------------- hand notes + indexes
def build_hand(vault: Path, overwrite: bool):
    written = 0
    for rel, (fm, body) in NOTES.items():
        p = vault / rel
        if p.exists() and not overwrite:
            continue
        write_note(p, fm, body)
        written += 1
    for title, s in CONCEPTS.items():
        p = vault / s["folder"] / f"{title}.md"
        if p.exists() and not overwrite:
            continue
        tag = {"concept": "concept", "infra": "workflow", "tool": "tool", "hardware": "hardware",
               "paper": "paper", "decision": "decision"}[s["type"]]
        fm = dict(type=s["type"], tags=[tag], aliases=s["aliases"], as_of=s.get("as_of", "2026-10-05"))
        write_note(p, fm, f"# {title}\n\n" + s["body"])
        written += 1
    return written


def build_indexes(vault: Path, registry: dict):
    def idx(name, title, intro, items):
        write_note(vault / "Indexes" / f"{name}.md", dict(type="index", tags=["index"], generated=True, as_of=TODAY),
                   f"# {title}\n\n{intro}\n\n" + "\n".join(items) + "\n\nBack to [[00 SU2QC Map]].\n")

    by_folder = {}
    for t, s in CONCEPTS.items():
        by_folder.setdefault(s["folder"], []).append(t)
    idx("Physics concepts index", "Physics concepts index", "Physics ideas the packages rely on, each defined in plain words.",
        [f"- [[{t}]]" for t in sorted(by_folder.get("Concepts/Physics", []))] + ["- [[Shared 2x2 plaquette]]"])
    idx("Methods index", "Methods index", "Algorithms, machine learning and noise ideas.",
        [f"- [[{t}]]" for t in sorted(by_folder.get("Concepts/Methods", []))])
    idx("Hardware index", "Hardware index", "Quantum processors and classical machines.",
        [f"- [[{t}]]" for t in sorted(by_folder.get("Hardware", []))])
    idx("Workflow index", "Workflow index", "How the work is run: agents, gates, job queues, tools.",
        [f"- [[{t}]]" for t in sorted(by_folder.get("Workflow", []))] + [f"- [[{t}]]" for t in sorted(by_folder.get("Decisions", []))])
    idx("Papers index", "Papers index", "Papers cited inside the repositories.",
        [f"- [[{t}]]" for t in sorted(by_folder.get("Papers", []))])
    res = sorted(Path(r).stem for r in NOTES if r.startswith("Results/"))
    idx("Results index", "Results index", "Headline numbers, each tied to the gate that produced it.", [f"- [[{t}]]" for t in res])

    lines = []
    for repo_name in NOTES_ORDER:
        gs = [g for g in registry["gates"] if g["repo"] == repo_name]
        if not gs:
            continue
        lines += [f"## [[{repo_name}]]", "", "| gate | checks | status |", "|---|---|---|"]
        for g in gs:
            chk = g["check"].replace("|", "/")[:120]
            lines.append(f"| [[{g['title']}]] | {chk} | {g['word'].upper()} |")
        lines.append("")
    idx("Gates index", "Gates index", "Every gate in every package (generated from the repositories).", lines)

    lines = []
    for repo_name in NOTES_ORDER:
        ms = sorted(n for n, m in registry["modules"].items() if m["repo"] == repo_name)
        if not ms:
            continue
        lines += [f"## [[{repo_name}]]", ""] + [f"- [[{n}]] — {(registry['modules'][n]['doc'].split('.')[0] or '').strip()[:140]}" for n in ms] + [""]
    idx("Modules index", "Modules index", "Every Python module (generated from docstrings and imports).", lines)


# ----------------------------------------------------------------------------- graph colours
def write_obsidian_config(vault: Path):
    cfg = vault / ".obsidian"
    cfg.mkdir(exist_ok=True)

    def rgb(h):
        return int(h.lstrip("#"), 16)
    groups = [("tag:#package", "#e8590c"), ("tag:#result", "#c2255c"), ("tag:#gate", "#868e96"),
              ("path:Modules/skqd", "#1c7ed6"), ("path:Modules/jepa", "#2f9e44"), ("path:Modules/genesis", "#f08c00"), ("path:Modules/su2zx", "#fcc419"),
              ("path:Modules/trotter", "#e64980"), ("path:Modules/qca", "#5c7cfa"),
              ("tag:#hardware", "#7048e8"), ("tag:#paper", "#495057"), ("path:Concepts/Physics", "#0ca678"),
              ("path:Concepts/Methods", "#1098ad"), ("tag:#workflow OR tag:#tool OR tag:#decision", "#ae3ec9"),
              ("tag:#hub OR tag:#cross-package", "#f03e3e")]
    graph = {"collapse-filter": False, "search": "", "showTags": False, "showAttachments": False, "hideUnresolved": True,
             "showOrphans": False, "collapse-color-groups": False,
             "colorGroups": [{"query": q, "color": {"a": 1, "rgb": rgb(c)}} for q, c in groups],
             "collapse-display": False, "showArrow": True, "textFadeMultiplier": -0.6, "nodeSizeMultiplier": 1.1,
             "lineSizeMultiplier": 0.8, "collapse-forces": False, "centerStrength": 0.45, "repelStrength": 12,
             "linkStrength": 0.9, "linkDistance": 180, "scale": 0.5, "close": False}
    # keep the user's own Graph view settings (zoom, toggles, forces); only the colour groups are owned by the builder
    try:
        old = json.loads((cfg / "graph.json").read_text())
        graph = {**graph, **{k: v for k, v in old.items() if k != "colorGroups"}}
    except Exception:
        pass
    (cfg / "graph.json").write_text(json.dumps(graph, indent=2))
    try:
        app = json.loads((cfg / "app.json").read_text())
    except Exception:
        app = {}
    app.update({"userIgnoreFilters": sorted(set(app.get("userIgnoreFilters", [])) | {"_tools/", "_export/"}), "alwaysUpdateLinks": True})
    (cfg / "app.json").write_text(json.dumps(app, indent=2))


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos", required=True, help="folder that contains the package repositories")
    ap.add_argument("--vault", default=str(HERE.parent))
    ap.add_argument("--overwrite-hand", action="store_true", help="also rewrite hand-written notes")
    a = ap.parse_args()
    repos, vault = Path(a.repos).expanduser(), Path(a.vault).expanduser()
    for d in ("Modules", "Gates", "Indexes"):
        shutil.rmtree(vault / d, ignore_errors=True)
    reg = {}
    build_modules(repos, vault, reg)
    build_gates(repos, vault, reg)
    build_modules(repos, vault, reg)  # second pass adds gate backlinks to modules
    n = build_hand(vault, a.overwrite_hand)
    build_indexes(vault, reg)
    write_obsidian_config(vault)
    from build_canvas import build_canvas
    build_canvas(vault, reg)
    meta = {"built": TODAY, "packages": {d: dict(zip(("head", "commits", "branch"), git_info(repo_dir(repos, d)))) | {"folder": repo_dir(repos, d).relative_to(repos).as_posix()}
                                         for d in dict.fromkeys(P["dir"] for P in PACKAGES) if repo_dir(repos, d).is_dir()},
            "modules": len(reg["modules"]), "gates": len(reg["gates"])}
    (vault / "_tools" / "last_build.json").write_text(json.dumps(meta, indent=2))
    print(f"modules {len(reg['modules'])}, gates {len(reg['gates'])}, hand notes written {n}")


if __name__ == "__main__":
    main()
