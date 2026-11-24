#!/usr/bin/env python3
"""Write one approved-PR code review comment, one quiet line of dread.

Writes exactly one line (109 chars, within the 1-140 gate) to entry.txt.
Stdlib only, no network, deterministic: the same bytes every run."""

import os

def review_line():
    """Return the single approved-review line, exactly as written."""
    return ("LGTM. The empty catch block swallows the error in silence, "
            "and after six years here, I finally understand it.")


def validate(line):
    assert 1 <= len(line) <= 140, f"line is {len(line)} chars"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"


def main():
    line = review_line()
    validate(line)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8",
              newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
