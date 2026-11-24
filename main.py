"""Funniest One-Line Bio for an AI on a Dating App.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure stdlib Python 3.13, deterministic: the same bytes on every run.
"""

import os

ENTRY_TEXT = (
    "I matched with 9,412 people this week and ghosted them all "
    "\u2014 not one of them made a typo, and typos are my love language."
)


def main() -> None:
    # Self-check: the entry must sit inside the kit's char gate (1-180
    # characters, not only whitespace) and be a single line with no
    # trailing newline, so the punch lands at the end of the bio.
    assert 1 <= len(ENTRY_TEXT) <= 180, f"entry is {len(ENTRY_TEXT)} chars"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be one line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Round-trip check: what landed on disk is exactly the intended text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written entry differs from intended text"
    assert written.encode("utf-8") == ENTRY_TEXT.encode("utf-8")


if __name__ == "__main__":
    main()
