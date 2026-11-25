#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- entry generator.

Writes the 27-character story to /output/entry.txt (no trailing newline).
Stdlib only; no network, no local imports, no fonts.
"""

import os

ENTRY = "MomSaidNoWiFiTillDishesDone"


def validate_story(text):
    """Gate: a whole story must fit in 1-32 characters, single line.

    The bounty limit is 32 characters max; anything shorter than 1 char
    is not a story at all. A newline would add a 28th byte and break the
    exact 27-character entry, so it is rejected here too.
    """
    assert 1 <= len(text) <= 32, "entry must be 1-32 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


def main():
    validate_story(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
