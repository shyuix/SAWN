"""Sawn retrieval engine.

The same pipeline that runs inside app/rag-simulator.html, as plain
Python over the same fitted index (rag/index.json):

  1. tokenise: lowercase, ASCII word runs, 1-2 grams
  2. encode:   sublinear tf x idf, l2 norm, SVD projection, l2 norm again
  3. score:    blended = alpha * min-max(dense cosine) + (1-alpha) * max-norm(BM25)
  4. ground:   cite only when blended score >= score_floor AND
               query-term coverage >= coverage_floor; otherwise refuse and
               send the question to the gap register

No third-party dependencies. The index is fitted offline; this file only
loads and applies it, so `python3 cli.py ask "..."` runs anywhere.
"""

import json
import math
import re
from pathlib import Path

_WORD = re.compile(r"\b[A-Za-z0-9_][A-Za-z0-9_/-]+\b")


class SawnRag:
    def __init__(self, index_path=None):
        p = Path(index_path) if index_path else Path(__file__).with_name("index.json")
        d = json.loads(p.read_text(encoding="utf8"))
        self.d = d
        self.stop = set(d["stop"])
        self.ndim = len(d["components"])
        self.alpha = d["defaults"]["alpha"]
        self.score_floor = d["defaults"]["score_floor"]
        self.coverage_floor = d["defaults"]["coverage_floor"]
        # BM25 statistics over the same tokenised chunks
        toks = d["tokens"]
        self.n_docs = len(toks)
        self.avgdl = sum(len(t) for t in toks) / self.n_docs
        df = {}
        for t in toks:
            for w in set(t):
                df[w] = df.get(w, 0) + 1
        self.idf_b = {w: math.log(1 + (self.n_docs - n + 0.5) / (n + 0.5))
                      for w, n in df.items()}
        self.doc_sets = [set(t) for t in toks]
        self.doc_tfs = []
        for t in toks:
            tf = {}
            for w in t:
                tf[w] = tf.get(w, 0) + 1
            self.doc_tfs.append(tf)

    # ---- tokenisation ----
    def grams(self, text):
        toks = _WORD.findall(text.lower())
        out = list(toks)
        out.extend(toks[i] + " " + toks[i + 1] for i in range(len(toks) - 1))
        return toks, out

    # ---- dense encoding: tf-idf then SVD projection, l2 at both stages ----
    def encode(self, text):
        _, gs = self.grams(text)
        vocab, idf, comps = self.d["vocab"], self.d["idf"], self.d["components"]
        tf = {}
        for g in gs:
            if g in vocab:
                tf[g] = tf.get(g, 0) + 1
        if not tf:
            return [0.0] * self.ndim
        vec = {vocab[g]: (1 + math.log(c)) * idf[vocab[g]] for g, c in tf.items()}
        n = math.sqrt(sum(x * x for x in vec.values()))
        if n:
            vec = {j: x / n for j, x in vec.items()}
        out = [sum(comps[k][j] * x for j, x in vec.items()) for k in range(self.ndim)]
        m = math.sqrt(sum(x * x for x in out))
        return [x / m for x in out] if m else out

    # ---- lexical scoring ----
    def bm25(self, qterms):
        k1, b = 1.4, 0.72
        scores = []
        for tf, t in zip(self.doc_tfs, self.d["tokens"]):
            dl = len(t)
            if not dl:
                scores.append(0.0)
                continue
            s = 0.0
            for q in qterms:
                f = tf.get(q, 0)
                if not f:
                    continue
                s += self.idf_b.get(q, 0.0) * f * (k1 + 1) / (
                    f + k1 * (1 - b + b * dl / self.avgdl))
            scores.append(s)
        return scores

    # ---- retrieval ----
    def search(self, question, k=4):
        toks, _ = self.grams(question)
        qterms = [t for t in toks if t not in self.stop]
        qv = self.encode(question)
        dense = [sum(r * q for r, q in zip(row, qv)) for row in self.d["matrix"]]
        lex = self.bm25(qterms)
        lmax = max(max(lex), 0)
        dmin, dmax = min(dense), max(dense)
        drange = (dmax - dmin) or 1.0
        uniq = set(qterms)
        rows = []
        for i, dv in enumerate(dense):
            dn = (dv - dmin) / drange
            ln = lex[i] / lmax if lmax else 0.0
            covered = sum(1 for t in uniq if t in self.doc_sets[i])
            rows.append({
                "i": i, "chunk": self.d["chunks"][i], "dense": dv, "lex": lex[i],
                "score": self.alpha * dn + (1 - self.alpha) * ln,
                "coverage": covered / len(uniq) if uniq else 0.0,
            })
        rows.sort(key=lambda r: r["score"], reverse=True)
        seen, out = set(), []
        for r in rows:
            src = r["chunk"]["src"]
            if src in seen:
                continue
            seen.add(src)
            out.append(r)
        return out[:k], qterms

    def grounded(self, hits):
        return [h for h in hits
                if h["score"] >= self.score_floor
                and h["coverage"] >= self.coverage_floor]

    def ask(self, question, k=4):
        """Grounded hits and full hits for one question."""
        hits, _ = self.search(question, k)
        return self.grounded(hits), hits

    # ---- the evaluation the README numbers come from ----
    def evaluate(self):
        ev = self.d["eval"]
        h1 = hk = 0
        rr = 0.0
        for q in ev["answerable"]:
            cites = [h["chunk"]["src"] for h in self.grounded(self.search(q["q"])[0])]
            if cites and cites[0] in q["expect"]:
                h1 += 1
            if any(c in q["expect"] for c in cites):
                hk += 1
            for rank, c in enumerate(cites, 1):
                if c in q["expect"]:
                    rr += 1.0 / rank
                    break
        caught = sum(1 for q in ev["gaps"]
                     if not self.grounded(self.search(q["q"])[0]))
        pc = pw = 0
        for q in ev["paraphrase"]:
            cites = [h["chunk"]["src"] for h in self.grounded(self.search(q["q"])[0])]
            if any(c in q["expect"] for c in cites):
                pc += 1
            elif cites:
                pw += 1
        na, ng, np_ = len(ev["answerable"]), len(ev["gaps"]), len(ev["paraphrase"])
        return {
            "hit@1": h1 / na, "hit@4": hk / na, "mrr": rr / na,
            "gap_recall": (caught, ng), "paraphrase_correct": (pc, np_),
            "miscited": pw,
        }
