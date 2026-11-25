"""Write the Weirdest Job Title entry to /output/entry.txt.

Deterministic: no network, no randomness, no timestamps. The single
job title is written exactly, with no trailing newline, so the file
is 53 bytes (within the 1-60 character gate).
"""

import os

LINE = "Professional Apologizer for Billionaires' Group Chats"


def main():
    for base in ("/output", "output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(LINE)
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
