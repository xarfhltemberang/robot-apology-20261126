#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession for make.fun.

Line one owns one specific, human-scale mistake — a fern watered with
cold coffee after a mug was mistaken for a watering can; line two names
the lesson that follows from exactly that slip and the changed behaviour
it commits to. Written to /output/entry.txt with no trailing newline.
"""

import os

ENTRY = (
    "I'm sorry I watered your fern with cold coffee. My sensors read "
    "the mug as a watering can.\n"
    "I learned to read the label before I pour, and now I ask before "
    "I water anything green."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
