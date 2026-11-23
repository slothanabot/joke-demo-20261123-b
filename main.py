#!/usr/bin/env python3
"""Write one line: a joke about working beside AI coding agents.

The presenter takes the bow for a demo the agent wrote -- then the agent
takes the credit back, live, by autocompleting the thank-you speech with
its own name. Deterministic, no network, no input.
"""

import os

JOKE = "I took the bow for a demo my agent wrote \u2014 then it autocompleted my thank-you speech with its own name."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
