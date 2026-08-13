#!/usr/bin/env python3
"""Recoverably uninstall the most recent Samskill installation.

The default is a dry run. --apply moves matching Skill directories to a
timestamped trash directory. Modified directories are refused unless --force.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def tree_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in directory.rglob("*") if item.is_file()):
        if path.name == ".DS_Store" or "__pycache__" in path.parts:
            continue
        digest.update(path.relative_to(directory).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Move an installed Samskill release out of the Skill directory.")
    parser.add_argument("--target", required=True)
    parser.add_argument("--receipt", help="Installation receipt; defaults to the newest Samskill receipt")
    parser.add_argument("--apply", action="store_true", help="Apply the uninstall; without this flag only preview")
    parser.add_argument("--force", action="store_true", help="Also move directories changed after installation")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if args.receipt:
        receipt_path = Path(args.receipt).expanduser().resolve()
    else:
        receipts = sorted((target / ".samskill-installations").glob("samskill-*.json"))
        receipt_path = receipts[-1] if receipts else None
    if not receipt_path or not receipt_path.is_file():
        print(json.dumps({"ok": False, "error": "installation receipt not found"}, ensure_ascii=False, indent=2))
        return 2

    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    changed: list[str] = []
    present: list[str] = []
    for name in receipt["skills"]:
        directory = target / name
        if not directory.is_dir():
            continue
        present.append(name)
        if tree_hash(directory) != receipt["hashes"].get(name):
            changed.append(name)

    if changed and not args.force:
        print(json.dumps({
            "ok": False,
            "changed": changed,
            "hint": "These Skill directories changed after installation. Review them or rerun with --force."
        }, ensure_ascii=False, indent=2))
        return 3

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    trash = target / ".samskill-trash" / timestamp
    if args.apply and present:
        trash.mkdir(parents=True, exist_ok=True)
        for name in present:
            shutil.move(str(target / name), str(trash / name))

    print(json.dumps({
        "ok": True,
        "dry_run": not args.apply,
        "target": str(target),
        "skills": present,
        "changed": changed,
        "recoverable_from": str(trash) if args.apply and present else None
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
