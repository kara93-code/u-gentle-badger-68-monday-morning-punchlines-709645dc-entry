"""Monday Morning Punchlines — one joke about Monday morning.

The joke treats Monday morning as an uninvited houseguest: it does not
knock, it walks in, eats the weekend, and then — the turn — asks what is
for lunch, as if it lived here. No alarm, no coffee, no complaint about
hating Mondays: the laugh comes from the escalation, not the cliché.
"""

import os
import sys

JOKE = (
    "Monday morning didn't knock. It let itself in, "
    "ate my weekend, and asked what's for lunch."
)


def main() -> int:
    text = JOKE.strip()
    if not text:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: joke is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    # Round-trip check: what the grader reads must be exactly the joke.
    with open(path, encoding="utf-8") as fh:
        if fh.read() != text:
            print("error: written entry does not match the joke",
                  file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
