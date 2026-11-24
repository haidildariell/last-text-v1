#!/usr/bin/env python3
"""Last Text at One Percent — writes the phone's final text to /output/entry.txt."""

import os

LINE = "Last text: I turned off your 6 a.m. alarm myself. Sleep in. I'm dying, but at least one of us gets some rest."


PARTS = [
    "Last text: I turned off your 6 a.m. alarm myself.",
    "Sleep in.",
    "I'm dying, but at least one of us gets some rest.",
]


def build_text() -> str:
    text = " ".join(PARTS)
    if text != LINE:
        raise ValueError("restructured text must match the original line")
    return text


def validate(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    return text


def main() -> None:
    text = validate(build_text())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
