#!/usr/bin/env python3
"""Validate the public atom library without private dependencies."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "knowledge-base"
STANDARDS = ROOT / "standards"
ABSOLUTE_PATH = re.compile(r"/(?:Users|home)/[^\s`\"']+")
WINDOWS_PATH = re.compile(r"[A-Za-z]:\\(?:Users|Documents and Settings)\\", re.I)
PRIVATE_MARKERS = (
    "zhuanzhuan" + "0000",
    "Obsidian " + "Vault",
    "wx" + "id_",
    "嘉寅文化" + "传媒有限公司",
    "db" + "skill",
    "李" + "守洲",
    "dont" + "besilent",
)


def main() -> int:
    errors: list[str] = []
    required = {
        KB / "README.md",
        KB / "manifest.json",
        KB / "atom-skill-map.csv",
        KB / "source-register.csv",
        STANDARDS / "README.md",
    }
    for path in required:
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")

    atoms = list((KB / "modules").glob("*/SAM-*.md")) if KB.exists() else []
    modules = [p for p in (KB / "modules").iterdir() if p.is_dir()] if (KB / "modules").exists() else []
    sources = list((KB / "sources").glob("SRC-*.md")) if KB.exists() else []
    if len(modules) != 17:
        errors.append(f"expected 17 modules, got {len(modules)}")
    if len(atoms) != 203:
        errors.append(f"expected 203 atoms, got {len(atoms)}")
    if len(sources) < 70:
        errors.append(f"expected at least 70 public source cards, got {len(sources)}")

    atom_ids: set[str] = set()
    referenced_sources: set[str] = set()
    for path in atoms:
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"(?m)^id:\s*([^\s]+)", text)
        if not match:
            errors.append(f"{path.relative_to(ROOT)} missing atom id")
            continue
        atom_id = match.group(1)
        if atom_id in atom_ids:
            errors.append(f"duplicate atom id {atom_id}")
        atom_ids.add(atom_id)
        referenced_sources.update(re.findall(r"SRC-[A-Z0-9-]+", text))
        for field in ("knowledge_maturity", "evidence_maturity", "validation_maturity", "required_inputs", "outputs", "stop_conditions"):
            if not re.search(rf"(?m)^{field}:", text):
                errors.append(f"{path.relative_to(ROOT)} missing {field}")

    register_rows: list[dict[str, str]] = []
    if (KB / "source-register.csv").is_file():
        with (KB / "source-register.csv").open(encoding="utf-8", newline="") as handle:
            register_rows = list(csv.DictReader(handle))
    registered = {row.get("source_id", "") for row in register_rows}
    for source_id in sorted(referenced_sources - registered):
        errors.append(f"unregistered source {source_id}")

    mapping_rows: list[dict[str, str]] = []
    if (KB / "atom-skill-map.csv").is_file():
        with (KB / "atom-skill-map.csv").open(encoding="utf-8", newline="") as handle:
            mapping_rows = list(csv.DictReader(handle))
    mapped_atoms = {row.get("atom_id", "") for row in mapping_rows}
    for atom_id in sorted(atom_ids - mapped_atoms):
        errors.append(f"atom has no Skill mapping: {atom_id}")
    allowed_mapping_basis = {"explicit_runtime_reference", "module_scope_candidate"}
    for row in mapping_rows:
        if row.get("mapping_basis") not in allowed_mapping_basis:
            errors.append(f"invalid mapping basis for {row.get('atom_id', '')}")

    for directory in (KB, STANDARDS):
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".json", ".csv"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if ABSOLUTE_PATH.search(text) or WINDOWS_PATH.search(text):
                errors.append(f"{path.relative_to(ROOT)} contains absolute path")
            for marker in PRIVATE_MARKERS:
                if marker in text:
                    errors.append(f"{path.relative_to(ROOT)} contains private marker")

    manifest = {}
    if (KB / "manifest.json").is_file():
        manifest = json.loads((KB / "manifest.json").read_text(encoding="utf-8"))
        if manifest.get("atoms") != 203 or manifest.get("modules") != 17:
            errors.append("knowledge-base manifest count mismatch")

    result = {
        "valid": not errors,
        "modules": len(modules),
        "atoms": len(atoms),
        "sources": len(sources),
        "source_register": len(register_rows),
        "atom_skill_edges": len(mapping_rows),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
