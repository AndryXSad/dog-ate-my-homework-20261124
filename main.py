"""The Dog Ate My Homework: Funniest Excuse — entry program (program/v1).

Writes one line — the excuse a dog gives after being caught eating the
homework — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that
variable is set). The line was chosen by a local pairwise tournament over 14
original candidates, scored on the published judge criteria in order: the
dog's own voice, the biggest laugh with a twist of dog logic, sounding like
a real dog, standing alone, and feeling fresh.

The winning line: the homework started a staring contest with the dog, and
the dog answers with pack logic — there can only be one alpha in the house,
and it is not long division. A dog that believes it has done nothing wrong.
"""

import os
import sys

LINE = (
    "The homework started it. It looked at me. I looked back. "
    "There can only be one alpha in this house, and it isn't long division."
)


def validate_line(line: str) -> bool:
    """Apply the sealed gate: 1 to 200 characters, not whitespace-only."""
    return bool(line.strip()) and 1 <= len(line) <= 200


def resolve_output_dir() -> str:
    """Read the grader's output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(path: str, line: str) -> None:
    """Write the line to entry.txt exactly, with no trailing newline."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> int:
    if not validate_line(LINE):
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
