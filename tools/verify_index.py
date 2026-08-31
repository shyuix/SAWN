#!/usr/bin/env python3
"""Integrity check: everything published here runs off one index.

  python3 tools/verify_index.py

1. Extracts the fitted index embedded in app/rag-simulator.html and
   asserts it is identical to rag/index.json, so nothing the demo shows can
   diverge from what `cli.py` computes.
2. Asserts kb/sources.json is the corpus that index was fitted over: same 23
   instruments, same code, authority, url and text, in the same order.
3. Asserts every id an evaluation question expects exists in the corpus, so
   eval/questions.yaml cannot reference an instrument that was renamed away.
4. Runs the evaluation and asserts the documented metrics reproduce.

Exits 0 only if all four hold. No dependencies.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_simulator(shipped):
    sim = ROOT / "app" / "rag-simulator.html"
    if not sim.exists():
        sim = ROOT / "rag-simulator.html"   # flat submission package layout
    html = sim.read_text(encoding="utf8")
    m = re.search(r'<script id="idx" type="application/json">(.*?)</script>', html, re.S)
    if not m:
        print("FAIL: no embedded index found in the simulator")
        return False
    if json.loads(m.group(1)) != shipped:
        print("FAIL: rag/index.json differs from the index inside the simulator")
        return False
    print("OK: rag/index.json is identical to the index inside the simulator")
    return True


def check_corpus(shipped):
    kb = ROOT / "kb" / "sources.json"
    if not kb.exists():
        print("FAIL: kb/sources.json is missing")
        return False
    sources = json.loads(kb.read_text(encoding="utf8"))["sources"]
    chunks = shipped["chunks"]
    if len(sources) != len(chunks):
        print(f"FAIL: kb/sources.json has {len(sources)} instruments, "
              f"the index has {len(chunks)}")
        return False
    for s, c in zip(sources, chunks):
        pairs = [("id", "src"), ("code", "code"), ("title", "title"),
                 ("authority", "auth"), ("url", "url"), ("text", "text")]
        for a, b in pairs:
            if s[a] != c[b]:
                print(f"FAIL: {s['id']} differs from the index on '{a}'")
                return False
    print(f"OK: kb/sources.json matches the {len(chunks)} instruments in the index")
    return True


def check_eval_ids(shipped):
    ids = {c["src"] for c in shipped["chunks"]}
    y = (ROOT / "eval" / "questions.yaml").read_text(encoding="utf8")
    used = {t.strip() for m in re.finditer(r"expect:\s*\[([^\]]*)\]", y)
            for t in m.group(1).split(",") if t.strip()}
    missing = sorted(used - ids)
    if missing:
        print(f"FAIL: eval/questions.yaml expects instruments not in the corpus: "
              f"{', '.join(missing)}")
        return False
    print(f"OK: all {len(used)} instrument ids used by the evaluation exist in the corpus")
    return True


def main():
    shipped = json.loads((ROOT / "rag" / "index.json").read_text(encoding="utf8"))
    for check in (check_simulator, check_corpus, check_eval_ids):
        if not check(shipped):
            return 1
    print()
    return subprocess.run([sys.executable, str(ROOT / "cli.py"), "eval"]).returncode


if __name__ == "__main__":
    sys.exit(main())
