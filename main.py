#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from 1800, using only things a person of that year could
picture: a post office, a library, a letter, a book, a table.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

SENTENCE = (
    "The internet is one post office and library for the whole world, "
    "where a letter reaches any door before you blink and any book "
    "lies open on the same table."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, "entry must be 1-200 characters"
    assert SENTENCE.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
