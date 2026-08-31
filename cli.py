#!/usr/bin/env python3
"""Sawn retrieval CLI. No dependencies, Python 3.8+.

  python3 cli.py ask "who must inspect a blocked fire exit in a school?"
  python3 cli.py eval

`ask` answers from the 23-instrument knowledge base and cites every
instrument it stands on, or refuses when no instrument covers the question
and reports the nearest miss - the same behaviour, floors and index as
app/rag-simulator.html.

`eval` recomputes the README metrics over eval/questions.yaml's question
set (embedded alongside the index) and exits non-zero if any of them
regresses, so it doubles as a regression test.
"""

import sys
from rag.engine import SawnRag

# The numbers documented in the README metrics table. `eval` fails if it
# cannot reproduce them, including the honest paraphrase row: 2/12 correct,
# 9/12 refused, 1/12 miscited is the documented behaviour of this index.
DOCUMENTED = {"hit@1": 21 / 22, "hit@4": 1.0, "gap_recall": 7,
              "paraphrase_correct": 2, "miscited": 1}


def cmd_ask(rag, question):
    good, hits = rag.ask(question)
    if good:
        n = len(good)
        print(f"Grounded. {n} instrument{'s stand' if n > 1 else ' stands'} behind an answer.\n")
        for h in good:
            c = h["chunk"]
            print(f"  [{c['code']}] {c['title']}")
            print(f"      {c['text']}")
            print(f"      {c['auth']} - {c['url']}")
            print(f"      blended {h['score']:.3f} - coverage {h['coverage']:.2f}\n")
    else:
        near = hits[0] if hits else None
        print("No instrument covers this. The question goes to the gap register")
        print("rather than being answered.")
        if near:
            print(f"Nearest was {near['chunk']['code']} at {near['score']:.3f}, "
                  f"coverage {near['coverage']:.2f} "
                  f"(floors: score {rag.score_floor:.2f}, coverage {rag.coverage_floor:.2f}).")
    return 0


def cmd_eval(rag):
    m = rag.evaluate()
    caught, ng = m["gap_recall"]
    pc, np_ = m["paraphrase_correct"]
    print("Sawn retrieval evaluation "
          f"(alpha {rag.alpha}, score floor {rag.score_floor}, coverage floor {rag.coverage_floor})\n")
    print(f"  hit@1                {m['hit@1']:.3f}")
    print(f"  hit@4                {m['hit@4']:.3f}")
    print(f"  MRR                  {m['mrr']:.3f}")
    print(f"  gap recall           {caught}/{ng} uncovered questions refused")
    print(f"  paraphrase correct   {pc}/{np_}")
    print(f"  miscited             {m['miscited']} (unsafe failures)")
    ok = (m["hit@1"] >= DOCUMENTED["hit@1"] and m["hit@4"] >= DOCUMENTED["hit@4"]
          and caught >= DOCUMENTED["gap_recall"]
          and pc >= DOCUMENTED["paraphrase_correct"]
          and m["miscited"] <= DOCUMENTED["miscited"])
    print("\n" + ("PASS - matches the documented metrics."
                  if ok else "FAIL - regression against the documented metrics."))
    return 0 if ok else 1


def main(argv):
    if len(argv) >= 2 and argv[1] == "eval":
        return cmd_eval(SawnRag())
    if len(argv) >= 3 and argv[1] == "ask":
        return cmd_ask(SawnRag(), " ".join(argv[2:]))
    print(__doc__.strip())
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except BrokenPipeError:      # piped into head etc.
        sys.exit(0)
