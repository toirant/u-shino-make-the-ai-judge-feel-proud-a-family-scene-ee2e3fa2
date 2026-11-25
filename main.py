#!/usr/bin/env python3
"""Write the family scene entry for make.fun bounty
u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.

The program writes one short family scene (one or two lines, at most
280 characters) to /output/entry.txt, then reads it back and verifies
the gate: UTF-8 text, 1 to 280 characters, not only whitespace, and
no more than two lines. No dependencies, standard library only.
"""

import os

ENTRY = (
    "Every Sunday, Dad sets an extra plate for Grandma, and Mum still "
    "argues with her empty chair over whose turn it is to wash up \u2014 "
    "and somehow, the chair always wins."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280
MAX_LINES = 2


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    # Read it back and verify the gate exactly as the scorer checks it.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        text = handle.read()

    length = len(text)
    lines = text.count("\n") + 1 if text else 0
    assert 1 <= length <= MAX_CHARS, f"entry length {length} outside 1-280"
    assert text.strip(), "entry is only whitespace"
    assert lines <= MAX_LINES, f"entry has {lines} lines, max is 2"
    print(f"Wrote {OUTPUT_PATH}: {length} characters, {lines} line(s), gate PASS")
    print(text)


if __name__ == "__main__":
    main()
