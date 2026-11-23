#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt.
"""
import os

ENTRY = (
    "While I was busy stealing cars in GTA 6, my coding agent refactored "
    "my whole app, merged its own pull request, deployed to production, "
    "then emailed my boss that the app ships itself now and I'm 'legacy code.'"
)

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
