#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory (make.fun).

Writes the entry -- one original one-line text -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = "Grandmother's kitchen smelled of rice steam and rain on hot concrete, and I believed then that summer evenings would last forever because nobody had told me they end."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
