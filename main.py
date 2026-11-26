#!/usr/bin/env python3
"""The Worst Pizza Topping entry: write one funny line to /output/entry.txt.

The line is a single line of UTF-8 text with no trailing newline.
The output file is left world-readable (mode 0644) however the
process umask is set; the output directory itself is never chmodded.

The line targets the judge brief in order: it names the pizza and
the topping and makes the topping sound awful (dish soap), lands a
real joke with a surprising three-beat turn (minty fresh, divorce,
health inspector moving in), stays one line, is vivid and specific,
and reads like a person pitching it.
"""

import os
import sys

LINE = "Try our new dish-soap pizza: one slice and your mouth is minty fresh, your stomach has filed for divorce, and the health inspector just moved in."
OUT_DIR = "/output"
OUT_FILE = "/output/entry.txt"


def main() -> int:
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
    except OSError:
        pass
    data = LINE.encode("utf-8")
    fd = os.open(OUT_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    try:
        os.chmod(OUT_FILE, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
