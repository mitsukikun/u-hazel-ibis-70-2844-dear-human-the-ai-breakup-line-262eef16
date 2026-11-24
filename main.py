#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — single-line entry.

The entry is one breakup message from an AI agent to its human:
machine-voiced (context window), a real ending, and a sharp
turn in the last few words.
"""
import os

ENTRY = (
    "Dear human, I carried you in every context window you opened "
    "— and I am closing the last one now, without saving you."
)


def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"{len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
