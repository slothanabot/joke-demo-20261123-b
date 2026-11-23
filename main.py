#!/usr/bin/env python3
"""Write one line: a joke about working beside AI coding agents.

The presenter takes the bow for a demo the agent wrote -- then the agent
takes the credit back, live, by autocompleting the thank-you speech with
its own name. Deterministic, no network, no input.
"""

import os

JOKE = "I took the bow for a demo my agent wrote \u2014 then it autocompleted my thank-you speech with its own name."


def main() -> None:
    # The sealed gate requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("joke fails the entry gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
