#!/usr/bin/env python3
"""news-image-20261118 entry: deliver the front page to /output/entry.png.

The front page ('THE WORLD — Wednesday 18 November 2026', 35 stories from
six continents) is rendered at build time by work/render.py and ships beside
this program as entry.png. This program only copies it, using the standard
library, so the graded run needs nothing installed and always writes
identical bytes.
"""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SIZE_CAP = 1024 * 1024


def main():
    source = os.path.join(BASE, "entry.png")
    if not os.path.isfile(source):
        raise SystemExit("entry.png is missing from the repository")
    size = os.path.getsize(source)
    if size == 0:
        raise SystemExit("entry.png is empty")
    if size > SIZE_CAP:
        raise SystemExit("entry.png exceeds the 1 MiB cap")
    # Pre-copy validation: the file must be a JPEG (SOI marker + EOI marker)
    # so a truncated or non-image file fails loudly instead of being graded.
    with open(source, "rb") as fh:
        head = fh.read(2)
        fh.seek(-2, os.SEEK_END)
        tail = fh.read(2)
    if head != b"\xff\xd8" or tail != b"\xff\xd9":
        raise SystemExit("entry.png is not a complete JPEG file")
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(target) != size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
