#!/usr/bin/env python3
"""Export every note of the vault to _export/su2qc_brain.jsonl (one JSON object per line) for retrieval or training.

    python export_jsonl.py [--vault ..]

Record fields: id (path), title, type, package, status, tags, aliases, as_of, links, backlinks, text (body without
frontmatter), chars. Also writes _export/graph_edges.csv (source,target) for graph tools such as NetworkX or Gephi.
"""
import argparse, csv, json, re
from pathlib import Path

LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def parse(p: Path):
    t = p.read_text(encoding="utf-8")
    fm, body = {}, t
    if t.startswith("---\n"):
        end = t.find("\n---", 4)
        for line in t[4:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                v = v.strip()
                try:
                    fm[k.strip()] = json.loads(v)
                except Exception:
                    fm[k.strip()] = v
        body = t[end + 4:].lstrip("\n")
    return fm, body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=str(Path(__file__).resolve().parent.parent))
    v = Path(ap.parse_args().vault)
    notes = {}
    for p in sorted(v.rglob("*.md")):
        rel = p.relative_to(v)
        if rel.parts[0] in ("_tools", "_export", ".obsidian"):
            continue
        fm, body = parse(p)
        notes[p.stem] = dict(id=rel.as_posix(), title=p.stem, type=fm.get("type", ""), package=fm.get("package", ""),
                             status=fm.get("status", ""), tags=fm.get("tags", []), aliases=fm.get("aliases", []),
                             as_of=fm.get("as_of", ""), links=sorted({m.strip() for m in LINK.findall(body)}),
                             text=body, chars=len(body))
    alias = {a: k for k, n in notes.items() for a in (n["aliases"] or [])}
    for n in notes.values():
        n["links"] = sorted({alias.get(l, l) for l in n["links"] if alias.get(l, l) in notes})
        n["backlinks"] = []
    for k, n in notes.items():
        for l in n["links"]:
            notes[l]["backlinks"].append(k)
    out = v / "_export"
    out.mkdir(exist_ok=True)
    with open(out / "su2qc_brain.jsonl", "w", encoding="utf-8") as f:
        for n in notes.values():
            n["backlinks"] = sorted(set(n["backlinks"]))
            f.write(json.dumps(n, ensure_ascii=False) + "\n")
    with open(out / "graph_edges.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "target"])
        for k, n in notes.items():
            for l in n["links"]:
                w.writerow([k, l])
    print(f"{len(notes)} notes, {sum(len(n['links']) for n in notes.values())} links -> {out}")


if __name__ == "__main__":
    main()
