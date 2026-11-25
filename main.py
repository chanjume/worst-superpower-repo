"""Worst Superpower — writes a single one-line entry to /output/entry.txt."""

import os

ENTRY = (
    # The whole joke in one line: a god-tier power (freeze time) throttled
    # to a single blink — 0.4 seconds, 15,000 times a day, for free.
    "I can freeze time for 0.4 seconds — exactly one blink — "
    "which I already do about 15,000 times a day for free."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
