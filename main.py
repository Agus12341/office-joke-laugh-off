#!/usr/bin/env python3
"""Write the one-line office joke to entry.txt in the output folder."""

import os

# One line about work life: picked from five drafts judged pairwise on
# the kit's criteria (office joke first, then real laugh, clear on one
# read, fresh, tight). The joke is the euphemism itself, exposed by
# its own legal department. The gate checks entry.txt as UTF-8 text
# of 1 to 200 characters: this line is 78 code points, 79 with its
# trailing newline (verified by a local run).
TEXT = "Our boss calls it 'synergy' because 'unpaid overtime' tested badly with legal."


def write_entry(out_dir: str) -> None:
    """Write the joke, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
