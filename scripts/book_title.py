#!/usr/bin/env python3
"""Decide what Tiv calls his book this session, and record it.

  python scripts/book_title.py roll            # prints CHANGE | KEEP <title> | REVERT <title>
  python scripts/book_title.py set <session> "<title>"   # record the title used

Odds per journal entry: 90% change, 2% keep the current title, 8% revert to a
previous (non-current) title. With no earlier title to revert to, REVERT becomes CHANGE.
The newest row of journal/book_titles.md is the current title.
"""
import random
import re
import sys
from pathlib import Path

FILE = Path(__file__).resolve().parent.parent / "journal" / "book_titles.md"
ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*$")


def titles():
    return [(int(m.group(1)), m.group(2)) for line in FILE.read_text().splitlines()
            if (m := ROW.match(line))]


def roll(rng=random):
    rows = titles()
    if not rows:
        return "CHANGE"
    current = rows[-1][1]
    r = rng.random()
    if r < 0.02:
        return f"KEEP {current}"
    if r < 0.10:
        earlier = sorted({t for _, t in rows if t != current})
        return f"REVERT {rng.choice(earlier)}" if earlier else "CHANGE"
    return "CHANGE"


def record(session, title):
    rows = titles()
    if rows and rows[-1] == (session, title):
        return
    with FILE.open("a") as f:
        f.write(f"| {session} | {title} |\n")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "roll":
        print(roll())
    elif len(sys.argv) == 4 and sys.argv[1] == "set":
        record(int(sys.argv[2]), sys.argv[3])
    else:
        sys.exit(__doc__)
