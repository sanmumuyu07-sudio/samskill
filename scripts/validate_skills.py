#!/usr/bin/env python3
"""Run official-compatible structural validation for every bundled Skill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py"


def fallback_validate(directory: Path) -> tuple[bool, str]:
    skill = directory / "SKILL.md"
    if not skill.is_file():
        return False, "SKILL.md missing"
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False, "frontmatter missing"
    if f"\nname: {directory.name}\n" not in text:
        return False, "frontmatter name mismatch"
    if "\ndescription:" not in text:
        return False, "description missing"
    return True, "fallback validation passed"


def main() -> int:
    results = []
    for directory in sorted((ROOT / "skills").iterdir()):
        if not directory.is_dir():
            continue
        if VALIDATOR.is_file():
            proc = subprocess.run(
                [sys.executable, str(VALIDATOR), str(directory)],
                text=True,
                capture_output=True,
                check=False,
            )
            detail = (proc.stdout + proc.stderr).strip()
            if proc.returncode == 0:
                ok = True
                mode = "official"
            elif "ModuleNotFoundError" in detail and "yaml" in detail:
                ok, fallback_detail = fallback_validate(directory)
                detail = f"official validator unavailable (PyYAML missing); {fallback_detail}"
                mode = "fallback-no-pyyaml"
            else:
                ok = False
                mode = "official"
        else:
            ok, detail = fallback_validate(directory)
            mode = "fallback"
        results.append({"skill": directory.name, "ok": ok, "mode": mode, "detail": detail})

    payload = {
        "ok": all(item["ok"] for item in results),
        "count": len(results),
        "results": results,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
