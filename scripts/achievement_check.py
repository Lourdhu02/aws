#!/usr/bin/env python3
"""
achievement_check.py — scan progress.md and achievements.md, report score.

Usage:
    python scripts/achievement_check.py

Reads:
    progress.md        — topic status table
    achievements.md    — achievement table

Prints a summary of what's done, what's not, and a point score.
"""

import re
import sys
from pathlib import Path


def parse_progress(path: Path):
    """Extract topic -> status from the progress.md table."""
    text = path.read_text(encoding="utf-8", errors="replace")
    # Match table rows: | Topic | Status | Notes |
    pattern = re.compile(r"^\|\s*(.+?)\s*\|\s*(Not Started|Reading|Hands-On|Revised|Complete)\s*\|", re.MULTILINE)
    topics = {}
    for m in pattern.finditer(text):
        topic = m.group(1).strip()
        status = m.group(2).strip()
        topics[topic] = status
    return topics


def parse_achievements(path: Path):
    """Extract achievement rows from achievements.md tables."""
    text = path.read_text(encoding="utf-8", errors="replace")
    # Match: | # | Achievement | 要求 | ... | Status | Date | Evidence |
    pattern = re.compile(
        r"^\|\s*([A-Za-z0-9.]+)\s*\|\s*(.+?)\s*\|\s*.*?\|\s*.*?\|\s*(☐|✅|✓|x|X)\s*\|",
        re.MULTILINE,
    )
    achievements = {}
    for m in pattern.finditer(text):
        aid = m.group(1).strip()
        name = m.group(2).strip()
        status = m.group(3).strip()
        achievements[aid] = {"name": name, "status": status}
    return achievements


def phase_points(phase_num: str, topics: dict) -> int:
    """1 point if all topics in a phase are Complete."""
    phase_topics = [t for t in topics if t.startswith(f"{phase_num}.") or t.startswith(f"Phase {phase_num}") or t.startswith(f"{phase_num} ") or t.startswith(f"Phase-{phase_num}")]
    if not phase_topics:
        # fallback: topics that contain the phase number
        phase_topics = [t for t in topics if phase_num in t.split() or f"Phase {phase_num}" in t]
    if not phase_topics:
        return 0
    if all(topics.get(t) == "Complete" for t in phase_topics):
        return 1
    return 0


def main():
    root = Path.cwd()
    progress_path = root / "progress.md"
    ach_path = root / "achievements.md"

    if not progress_path.exists():
        print("ERROR: progress.md not found")
        return 1
    if not ach_path.exists():
        print("ERROR: achievements.md not found")
        return 1

    topics = parse_progress(progress_path)
    achs = parse_achievements(ach_path)

    print("=== Topic Status Summary ===")
    total = len(topics)
    done = sum(1 for s in topics.values() if s == "Complete")
    in_progress = sum(1 for s in topics.values() if s in ("Reading", "Hands-On", "Revised"))
    not_started = sum(1 for s in topics.values() if s == "Not Started")
    print(f"Total topics: {total}")
    print(f"  Complete:      {done}")
    print(f"  In progress:   {in_progress}")
    print(f"  Not started:   {not_started}")

    print("\n=== Achievements Status ===")
    total_ach = len(achs)
    done_ach = sum(1 for a in achs.values() if a["status"] in ("✅", "✓", "x", "X"))
    print(f"Total achievements: {total_ach}")
    print(f"  Done:  {done_ach}")
    print(f"  Left:  {total_ach - done_ach}")

    print("\n=== Pending Achievements ===")
    for aid, info in achs.items():
        if info["status"] in ("☐",):
            print(f"  {aid}: {info['name']}")

    print("\n=== Phase Score (1 pt per fully complete phase) ===")
    score = 0
    for phase in range(0, 10):
        pts = phase_points(str(phase), topics)
        score += pts
        label = f"Phase {phase}"
        print(f"  {label}: {'✅ 1 pt' if pts else '☐ 0 pt'}")
    print(f"  Phase total: {score}")

    print("\nNote: full scoring (projects, cross-phase, cert) requires manual entry.")
    print("See achievements.md for the complete scoring rubric.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
