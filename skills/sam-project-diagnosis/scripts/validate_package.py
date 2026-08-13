#!/usr/bin/env python3
"""Run deterministic, dependency-free checks for the Skill package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a sam-project-diagnosis package.")
    parser.add_argument("--skill", default=str(Path(__file__).resolve().parent.parent))
    return parser.parse_args()


def main() -> int:
    root = Path(parse_args().skill).expanduser().resolve()
    errors: list[str] = []
    checks: list[str] = []
    skill_md = root / "SKILL.md"

    if not skill_md.is_file():
        errors.append("SKILL.md missing")
    else:
        content = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not match:
            errors.append("SKILL.md frontmatter invalid")
        else:
            frontmatter: dict[str, str] = {}
            for line in match.group(1).splitlines():
                if not line.strip():
                    continue
                key, separator, value = line.partition(":")
                if not separator:
                    errors.append(f"unsupported frontmatter line: {line}")
                    continue
                frontmatter[key.strip()] = value.strip()
            unknown = set(frontmatter) - ALLOWED_FRONTMATTER
            if unknown:
                errors.append(f"unexpected frontmatter keys: {sorted(unknown)}")
            name = frontmatter.get("name", "")
            description = frontmatter.get("description", "")
            if name != root.name:
                errors.append(f"frontmatter name {name!r} does not match directory {root.name!r}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                errors.append("name is not kebab-case")
            if not 1 <= len(description) <= 1024:
                errors.append("description length must be 1..1024")
            if "<" in description or ">" in description:
                errors.append("description contains angle brackets")
            checks.append(f"SKILL.md lines={len(content.splitlines())}")
            if len(content.splitlines()) >= 500:
                errors.append("SKILL.md should remain under 500 lines")

            referenced = set(re.findall(r"`((?:references|assets|scripts)/[^`\s]+)`", content))
            for relative in sorted(referenced):
                if not (root / relative).exists():
                    errors.append(f"referenced file missing: {relative}")
            checks.append(f"SKILL.md referenced resources={len(referenced)}")

    required = [
        "agents/openai.yaml",
        "references/modes-and-intake.md",
        "references/diagnostic-model.md",
        "references/core-runtime-contracts.md",
        "references/symptom-routing.md",
        "references/deliverable-contract.md",
        "references/source-rules.md",
        "references/source-register.md",
        "references/state-and-handoff.md",
        "references/examples-and-tests.md",
        "assets/diagnosis-report-template.md",
        "assets/project-state-delta.schema.json",
        "evals/eval_queries.json",
        "evals/evals.json",
        "scripts/validate_state.py",
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"required file missing: {relative}")
    checks.append(f"required files checked={len(required)}")

    for path in sorted(root.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {path.relative_to(root)}:{exc.lineno}: {exc.msg}")
    checks.append(f"JSON files parsed={len(list(root.rglob('*.json')))}")

    query_path = root / "evals" / "eval_queries.json"
    if query_path.is_file():
        queries = json.loads(query_path.read_text(encoding="utf-8"))
        positive = sum(item.get("should_trigger") is True for item in queries)
        negative = sum(item.get("should_trigger") is False for item in queries)
        train = sum(item.get("split") == "train" for item in queries)
        validation = sum(item.get("split") == "validation" for item in queries)
        if (positive, negative) != (10, 10):
            errors.append(f"trigger eval balance must be 10/10, got {positive}/{negative}")
        if (train, validation) != (12, 8):
            errors.append(f"trigger split must be 12/8, got {train}/{validation}")
        checks.append(f"trigger evals={positive} positive/{negative} negative; split={train}/{validation}")

    output = {"valid": not errors, "skill": str(root), "checks": checks, "errors": errors}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
