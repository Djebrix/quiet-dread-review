#!/usr/bin/env python3
"""Write one code review comment (approving a PR, quiet existential dread)
to entry.txt. Stdlib only, no network, deterministic."""

import os

LINE = "LGTM. The empty catch block swallows the error in silence, and after six years here, I finally understand it."


def main():
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
