#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes the tournament-champion museum placard to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The entry was chosen by an internal pairwise tournament over 16 candidate
placards, judged against the published judge brief (inventiveness of the
conceit, then dryness of wit, economy, and label craft). See CANDIDATES.md
for the full bracket.
"""

import os
import sys

ENTRY = (
    "Fire extinguisher, c. 1994. Red steel, untouched. "
    "A guardian god, inspected yearly, invoked never. "
    "Donated by Health & Safety."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Gate: 1-180 chars, not only whitespace.
    text = ENTRY.strip()
    if not (1 <= len(text) <= 180) or not text.strip():
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
