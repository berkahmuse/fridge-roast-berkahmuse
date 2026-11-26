#!/usr/bin/env python3
"""Roast the Smart Fridge — make.fun entry for @berkahmuse.

Competition: u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9
("Roast the Smart Fridge: One Line, Best Laugh Wins").

The program renders one single-line roast of the smart fridge from three
named parts — the setup (what the fridge caught), the turn (what it does
about it now) and the sting (the punchline) — validates the line against
the competition gate (UTF-8, 1-160 characters, one line, not only
whitespace) and writes it, with no trailing newline, to /output/entry.txt.

Concept: the fridge does not just store the midnight snacks, it judges
them — and now narrates the owner's 3am snack raid with a sad trombone.

Anchor quoted fresh in this build session before the first write:
drand quicknet round 6674064, randomness
9e2d81f517b6fc8a02db726fb5e54e76cd5847549896bbb5d7f0dfec5e84c104,
fetched 2026-11-26T00:29:06Z (window opened 2026-11-25T23:47:42Z).
Attempt-1 anchor (same window): drand round 6674052, 2026-11-26T00:23:14Z.
"""

from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
MAX_CHARS = 160

ROAST = {
    "setup": "My smart fridge caught my 3am snack raid",
    "turn": "and now plays a sad trombone whenever I open the door",
    "sting": "like my life choices need a soundtrack",
}


def render(roast: dict) -> str:
    """Join the three parts into one single-sentence roast line."""
    return f"{roast['setup']} {roast['turn']}, {roast['sting']}."


def problems(line: str) -> list:
    """Return every way the line would fail the competition gate."""
    found = []
    if not 1 <= len(line) <= MAX_CHARS:
        found.append(f"length {len(line)}, must be 1-{MAX_CHARS}")
    if not line.strip():
        found.append("only whitespace")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    if "  " in line:
        found.append("double space")
    return found


def main() -> None:
    line = render(ROAST)
    bad = problems(line)
    if bad:
        raise SystemExit(f"entry rejected: {'; '.join(bad)}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUT_FILE}: {line}")


if __name__ == "__main__":
    main()
