#!/usr/bin/env python3
"""Verify a Samskill installation using only the standard library."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.S)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify an installed Samskill directory.")
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    target = Path(args.target).expanduser().resolve()
    errors: list[str] = []

    for name in MANIFEST["skills"]:
        directory = target / name
        if not directory.is_dir():
            errors.append(f"missing skill directory: {name}")
            continue
        for relative in MANIFEST["minimum_skill_files"]:
            if not directory.joinpath(relative).is_file():
                errors.append(f"{name}: missing {relative}")
        skill_file = directory / "SKILL.md"
        if skill_file.is_file():
            match = FRONTMATTER.match(skill_file.read_text(encoding="utf-8"))
            if not match or not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", match.group(1)):
                errors.append(f"{name}: invalid frontmatter name")

    print(json.dumps({
        "ok": not errors,
        "target": str(target),
        "version": MANIFEST["version"],
        "skill_count": len(MANIFEST["skills"]),
        "errors": errors
    }, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
