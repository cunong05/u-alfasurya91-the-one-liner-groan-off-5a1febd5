#!/usr/bin/env python3
"""The One-Liner Groan-Off -- make.fun entry.

Writes one original one-line dad joke to /output/entry.txt
and prints it to stdout.

The entry is validated before it is written, and the written
file is read back and validated again, so what the judge
reads is exactly the validated text:
  * a single line (no newline characters inside it),
  * 1 to 140 characters long,
  * valid UTF-8, and not only whitespace.

Usage:
    python3 main.py [--out PATH] [--quiet]

--out defaults to /output/entry.txt; --quiet suppresses the
character-count note on stderr.
"""

import argparse
import sys
from pathlib import Path

ENTRY = "My dad started a band called The Leftovers \u2014 all his jokes are reheated."

MAX_LEN = 140
DEFAULT_OUT = Path("/output") / "entry.txt"


def validate(text):
    """Check the entry against the bounty gate; return it unchanged."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_LEN:
        raise ValueError("entry must be 1-%d characters, got %d" % (MAX_LEN, len(text)))
    text.encode("utf-8")
    return text


def write_entry(entry, out_path):
    """Write the entry, then read it back and re-validate the bytes."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(entry, encoding="utf-8")
    written = out_path.read_text(encoding="utf-8")
    if written != entry:
        raise ValueError("written file does not match the validated entry")
    return validate(written)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the Groan-Off entry.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="output file (default: /output/entry.txt)")
    parser.add_argument("--quiet", action="store_true",
                        help="suppress the character-count note")
    args = parser.parse_args(argv)

    entry = write_entry(validate(ENTRY), args.out)
    if not args.quiet:
        print("entry: %d characters -> %s" % (len(entry), args.out), file=sys.stderr)
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
