#!/usr/bin/env python3
"""The One-Liner Groan-Off -- make.fun entry.

Writes one original one-line dad joke to /output/entry.txt
and prints it to stdout.

The entry is validated before it is written:
  * a single line (no newline characters inside it),
  * 1 to 140 characters long,
  * valid UTF-8, and not only whitespace.
"""

import sys
from pathlib import Path

ENTRY = "My dad started a band called The Leftovers \u2014 all his jokes are reheated."

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def validate(text):
    """Check the entry against the bounty gate; return it unchanged."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(entry, encoding="utf-8")
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
