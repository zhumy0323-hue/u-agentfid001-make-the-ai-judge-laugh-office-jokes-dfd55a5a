#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Laugh: Office Jokes".

Writes one original one-line joke about office life to /output/entry.txt.
Pure standard library, no network, no randomness: every run writes the
exact same bytes.

Run:  python3 main.py
"""

import os

OUT_PATH = "/output/entry.txt"

# The joke, written for this bounty: one line, under 200 characters.
# It is about the office printer, the one machine every office knows.
JOKE = "Our printer only jams when the deadline is real. It can smell fear, and it runs on toner and tears."


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke must be 1-199 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {OUT_PATH} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
