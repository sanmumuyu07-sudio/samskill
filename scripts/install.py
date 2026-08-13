#!/usr/bin/env python3
"""Install Samskill without silently overwriting existing skills.

Stdout is JSON. Existing different directories are rejected unless --force.
With --force, the previous directory is moved to a timestamped backup first.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills"
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
ALL_SKILLS = MANIFEST["skills"]


def tree_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in directory.rglob("*") if item.is_file()):
        if path.name in {".DS_Store"} or "__pycache__" in path.parts:
            continue
        digest.update(path.relative_to(directory).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def select_skills(value: str) -> list[str]:
    if value.strip().lower() == "all":
        return list(ALL_SKILLS)
    selected = [item.strip() for item in value.split(",") if item.strip()]
    unknown = sorted(set(selected) - set(ALL_SKILLS))
    if unknown:
        raise ValueError(f"unknown skills: {', '.join(unknown)}")
    if not selected:
        raise ValueError("no skills selected")
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Samskill into a Skill discovery directory.")
    parser.add_argument("--target", required=True, help="Target directory, for example ~/.codex/skills")
    parser.add_argument("--skills", default="all", help="all or comma-separated skill names")
    parser.add_argument("--dry-run", action="store_true", help="Report actions without writing")
    parser.add_argument("--force", action="store_true", help="Back up and replace conflicting skill directories")
    args = parser.parse_args()

    try:
        selected = select_skills(args.skills)
    except ValueError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2

    target = Path(args.target).expanduser().resolve()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = target / ".samskill-backups" / timestamp
    receipt_dir = target / ".samskill-installations"
    actions: list[dict[str, str]] = []
    conflicts: list[str] = []

    for name in selected:
        source = SOURCE / name
        destination = target / name
        if not source.is_dir():
            conflicts.append(f"source missing: {name}")
            continue
        if not destination.exists():
            actions.append({"skill": name, "action": "install"})
        elif destination.is_dir() and tree_hash(source) == tree_hash(destination):
            actions.append({"skill": name, "action": "unchanged"})
        elif args.force:
            actions.append({"skill": name, "action": "backup-and-replace"})
        else:
            conflicts.append(name)

    if conflicts:
        print(json.dumps({
            "ok": False,
            "target": str(target),
            "conflicts": conflicts,
            "hint": "Rerun with --force only after reviewing the target. Conflicts are backed up before replacement."
        }, ensure_ascii=False, indent=2))
        return 3

    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)
        for item in actions:
            name = item["skill"]
            action = item["action"]
            source = SOURCE / name
            destination = target / name
            if action == "unchanged":
                continue
            if action == "backup-and-replace":
                backup_root.mkdir(parents=True, exist_ok=True)
                shutil.move(str(destination), str(backup_root / name))
            shutil.copytree(source, destination)

        hashes = {name: tree_hash(target / name) for name in selected}
        receipt = {
            "package": MANIFEST["name"],
            "version": MANIFEST["version"],
            "installed_at_utc": timestamp,
            "target": str(target),
            "skills": selected,
            "hashes": hashes,
            "backup": str(backup_root) if backup_root.exists() else None
        }
        receipt_dir.mkdir(parents=True, exist_ok=True)
        receipt_path = receipt_dir / f"samskill-{MANIFEST['version']}-{timestamp}.json"
        receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        receipt_path = None

    print(json.dumps({
        "ok": True,
        "dry_run": args.dry_run,
        "target": str(target),
        "version": MANIFEST["version"],
        "actions": actions,
        "receipt": str(receipt_path) if receipt_path else None
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
