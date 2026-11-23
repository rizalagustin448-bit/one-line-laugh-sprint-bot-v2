#!/usr/bin/env python3
"""One-Line Laugh Sprint v2 — writes one original funny line to /output/entry.txt."""
import os

LINE = "My smartwatch just congratulated me for standing up, which is the saddest trophy I've ever earned while sitting back down."

def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
