"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine (at most 120
characters) to /output/entry.txt. Deterministic, standard library
only: the same label is written on every run.
"""

import os
import sys

LINE = "WARNING: Do not wave at your past self. He waves back, follows you home, and eats your food."

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def resolve_output_dir():
    """Return the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if override.strip():
        return override
    return DEFAULT_OUTPUT_DIR


def entry_path():
    """Return the full path of the entry file to write."""
    return os.path.join(resolve_output_dir(), OUTPUT_FILENAME)


def validate_line(line):
    """Check the label is a single clean line within the 120-char limit."""
    if not line or not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        sys.exit(1)
    if line != line.strip():
        print("error: entry line has leading or trailing whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 120:
        print("error: entry is %d characters, over the 120 limit" % len(line), file=sys.stderr)
        sys.exit(1)


def main():
    validate_line(LINE)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
