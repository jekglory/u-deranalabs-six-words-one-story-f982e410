#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt (UTF-8, 38 chars).

The story, authored fresh in this session:
    She waited sixty years. Wrong station.

Why it works as a whole story: a lifetime of waiting is carried in
three words ("waited sixty years"), then the last two words turn it —
she was waiting in the wrong place all along. Every word earns its
place; nothing is spelled out. The reader fills in whom she waited
for, why she never left, and whether she ever found them.

Pure Python 3.13 standard library. No network, no clock, no randomness:
the same text is written on every run, byte for byte.
"""

from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 60
WORD_COUNT = 6

STORY = "She waited sixty years. Wrong station."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    words = STORY.split()
    if len(words) != WORD_COUNT:
        raise ValueError(f"story must be exactly {WORD_COUNT} words, got {len(words)}")
    if not MIN_CHARS <= len(STORY) <= MAX_CHARS:
        raise ValueError(
            f"story must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(STORY)}"
        )
    if not STORY.strip():
        raise ValueError("story must not be whitespace-only")
    # The grader owns /output: create it only if missing, never delete it,
    # and write the story as exact bytes — no trailing newline, so the
    # file is the six-word story and nothing else.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = STORY.encode("utf-8")
    OUTPUT_FILE.write_bytes(data)
    if OUTPUT_FILE.read_bytes() != data:
        raise RuntimeError("verification failed: written bytes differ")


if __name__ == "__main__":
    main()
