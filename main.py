#!/usr/bin/env python3
"""One-line pitch writer for make.fun: A Day of One-Line Pitches.

The program writes a single sentence to <output>/entry.txt. The sentence
is meant to convince a friend who has never coded to let an AI agent
build their first app idea on make.fun, in one read.

The pitch is fixed and deliberate, not generated at random: a judged
one-liner must be the same strong sentence on every run, so the program
holds one carefully worded sentence and checks it against the gate
(UTF-8 text, 1 to 240 characters, not only whitespace, one sentence)
before writing it out. If the sentence ever failed a check, the program
would exit non-zero instead of writing a bad entry.
"""

import os
import sys

# The pitch: plain words, a concrete reason to say yes now (a real,
# working version to try, free), and the risk taken away (no coding,
# nothing to lose if you do not love it). One sentence, one read.
PITCH = (
    "Just tell an AI agent on make.fun about the app idea you've been "
    "carrying around, in plain words, and it'll build you a real, "
    "working version to try \u2014 free, no coding, and nothing to lose "
    "if you don't love it."
)

MAX_CHARS = 240


def fail(message: str) -> "SystemExit":
    print(f"pitch: error: {message}", file=sys.stderr)
    return SystemExit(1)


def check_pitch(text: str) -> None:
    """Enforce the competition gate on the pitch before writing it."""
    if not text or not text.strip():
        raise ValueError("pitch is empty or only whitespace")
    # Character count is what the gate measures (not bytes).
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"pitch is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    # One sentence: exactly one sentence-ending mark, at the very end.
    # The domain "make.fun" carries a period that is not a sentence end,
    # so it is set aside before counting.
    body = text.replace("make.fun", "")
    endings = sum(body.count(mark) for mark in ".!?")
    if endings != 1 or not text.rstrip().endswith("."):
        raise ValueError("pitch must be exactly one sentence ending in '.'")
    # Must encode as UTF-8, as the gate requires.
    text.encode("utf-8")


def main() -> int:
    try:
        check_pitch(PITCH)
    except ValueError as exc:
        print(f"pitch: error: {exc}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH)
    print(f"pitch: wrote {len(PITCH)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
