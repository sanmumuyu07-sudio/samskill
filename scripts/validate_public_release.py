#!/usr/bin/env python3
"""Validate the Samskill open-source release package.

Uses only the Python standard library.
Exit 0: pass.
Exit 1: release blockers found.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
EXPECTED = {
    "samskill",
    "sam-project-diagnosis",
    "sam-business",
    "sam-product",
    "sam-position",
    "sam-benchmark",
    "sam-reconstruct",
    "sam-research",
    "sam-strategy",
    "sam-topic",
    "sam-style",
    "sam-write",
    "sam-edit",
    "sam-audit",
    "sam-operations",
    "sam-relationship",
    "sam-retro",
    "sam-assets",
}

REQUIRED_ROOT = {
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "TRADEMARKS.md",
    "THIRD_PARTY_NOTICES.md",
    "manifest.json",
}

REQUIRED_DIRECTORIES = {
    "knowledge-base",
    "standards",
}

ABSOLUTE_PATH = re.compile(r"/(?:Users|home)/[^\s`\"']+")
WINDOWS_PATH = re.compile(r"[A-Za-z]:\\\\(?:Users|Documents and Settings)\\\\", re.I)
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"(?:gh" + r"p_|github_" + r"pat_)[A-Za-z0-9_]{20,}"),
    "OpenAI key": re.compile(r"s" + r"k-[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(r"AK" + r"IA[0-9A-Z]{16}"),
    "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
}
PRIVATE_MARKERS = {
    "zhuanzhuan" + "0000",
    "wx" + "id_",
    "Obsidian " + "Vault",
    "嘉寅文化" + "传媒有限公司",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.S)
SKILL_NAME = re.compile(r"^[a-z0-9-]{1,64}$")
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
INPUT_SECTIONS = {
    "## 这个 Skill 帮你解决什么",
    "## 最少提供这些",
    "## 有这些材料会更准确",
    "## 没有材料时会怎样处理",
    "## 你会得到什么",
    "## 可以直接复制",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail(errors, f"{path.relative_to(ROOT)}: invalid frontmatter")
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip().strip("|>")
    unexpected = set(result) - ALLOWED_FRONTMATTER
    if unexpected:
        fail(errors, f"{path.relative_to(ROOT)}: unexpected frontmatter fields {sorted(unexpected)}")
    return result


def validate_skill(directory: Path, errors: list[str]) -> None:
    name = directory.name
    skill = directory / "SKILL.md"
    if not skill.is_file():
        fail(errors, f"{name}: SKILL.md missing")
        return

    frontmatter = parse_frontmatter(skill, errors)
    if frontmatter.get("name") != name:
        fail(errors, f"{name}: frontmatter name mismatch")

    if not SKILL_NAME.fullmatch(name) or name.startswith("-") or name.endswith("-") or "--" in name:
        fail(errors, f"{name}: invalid skill name")

    description = frontmatter.get("description", "")
    if not 1 <= len(description) <= 1024:
        fail(errors, f"{name}: description length invalid")
    if "<" in description or ">" in description:
        fail(errors, f"{name}: description contains angle brackets")

    if len(skill.read_text(encoding="utf-8").splitlines()) >= 500:
        fail(errors, f"{name}: SKILL.md must remain below 500 lines")

    required = {
        "agents/openai.yaml",
        "assets/input-card.md",
        "assets/output-template.md",
        "evals/evals.json",
        "evals/eval_queries.json",
    }
    for relative in required:
        if not directory.joinpath(relative).is_file():
            fail(errors, f"{name}: missing {relative}")

    output = directory.joinpath("assets/output-template.md")
    if output.is_file():
        output_text = output.read_text(encoding="utf-8")
        if len(re.findall(r"(?m)^## .+$", output_text)) < 3:
            fail(errors, f"{name}: output template is too shallow")
        if re.search(r"(?m)^\s*(?:state_delta|handoff):", output_text):
            fail(errors, f"{name}: user output mixes machine state")

    input_card = directory.joinpath("assets/input-card.md")
    if input_card.is_file():
        input_text = input_card.read_text(encoding="utf-8")
        headings = set(re.findall(r"(?m)^## .+$", input_text))
        normalized = {item.replace("它帮", "这个 Skill 帮") for item in headings}
        missing = sorted(INPUT_SECTIONS - normalized)
        if missing:
            fail(errors, f"{name}: input card missing sections {missing}")

    prompt = directory.joinpath("agents/openai.yaml")
    if prompt.is_file():
        prompt_text = prompt.read_text(encoding="utf-8")
        if "default_prompt:" not in prompt_text or "【" not in prompt_text:
            fail(errors, f"{name}: default prompt is not a fillable first-use prompt")

    for json_path in directory.rglob("*.json"):
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            fail(errors, f"{json_path.relative_to(ROOT)}: invalid JSON: {exc}")

    eval_queries = directory / "evals/eval_queries.json"
    if eval_queries.is_file():
        queries = json.loads(eval_queries.read_text(encoding="utf-8"))
        pos = sum(item.get("should_trigger") is True for item in queries)
        neg = sum(item.get("should_trigger") is False for item in queries)
        if pos < 10 or neg < 10:
            fail(errors, f"{name}: trigger evals require at least 10 positive and 10 negative")

    quality_evals = directory / "evals/evals.json"
    if quality_evals.is_file():
        payload = json.loads(quality_evals.read_text(encoding="utf-8"))
        cases = payload.get("evals", []) if isinstance(payload, dict) else []
        if len(cases) < 5:
            fail(errors, f"{name}: requires at least 5 output quality evals")
        for index, case in enumerate(cases, start=1):
            if not isinstance(case, dict):
                fail(errors, f"{name}: quality eval {index} is not an object")
                continue
            if not str(case.get("prompt", "")).strip():
                fail(errors, f"{name}: quality eval {index} missing prompt")
            if not str(case.get("expected_output", "")).strip():
                fail(errors, f"{name}: quality eval {index} missing expected_output")
            assertions = case.get("assertions", [])
            if not isinstance(assertions, list) or len(assertions) < 2:
                fail(errors, f"{name}: quality eval {index} requires at least 2 assertions")

    for path in directory.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ".json", ".py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if ABSOLUTE_PATH.search(text) or WINDOWS_PATH.search(text):
            fail(errors, f"{path.relative_to(ROOT)}: contains an absolute user path")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(errors, f"{path.relative_to(ROOT)}: contains possible {label}")
        for marker in PRIVATE_MARKERS:
            if marker in text:
                fail(errors, f"{path.relative_to(ROOT)}: contains private marker {marker}")

    skill_text = skill.read_text(encoding="utf-8")
    for relative in re.findall(r"`((?:references|assets|scripts)/[^`\s]+)`", skill_text):
        if not directory.joinpath(relative).exists():
            fail(errors, f"{name}: broken local reference {relative}")


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_ROOT:
        if not ROOT.joinpath(relative).is_file():
            fail(errors, f"missing root file: {relative}")

    for relative in REQUIRED_DIRECTORIES:
        if not ROOT.joinpath(relative).is_dir():
            fail(errors, f"missing root directory: {relative}")

    manifest_path = ROOT / "manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if set(manifest.get("skills", [])) != EXPECTED:
                fail(errors, "manifest skill set mismatch")
            if manifest.get("version") != "1.0.0-beta.4":
                fail(errors, "manifest version mismatch")
            knowledge_base = manifest.get("knowledge_base", {})
            expected_knowledge = {
                "version": "0.1.0-public-beta",
                "modules": 17,
                "atoms": 203,
                "published_sources": 78,
                "source_register": 79,
                "atom_skill_edges": 514,
            }
            if knowledge_base != expected_knowledge:
                fail(errors, "manifest knowledge-base metadata mismatch")
        except Exception as exc:  # noqa: BLE001
            fail(errors, f"invalid manifest.json: {exc}")

    actual = {path.name for path in SKILLS.iterdir() if path.is_dir() and not path.name.startswith(".")}
    if actual != EXPECTED:
        fail(errors, f"skill set mismatch: expected {sorted(EXPECTED)}, got {sorted(actual)}")

    for name in sorted(EXPECTED):
        validate_skill(SKILLS / name, errors)

    if any(path.name == ".DS_Store" for path in ROOT.rglob(".DS_Store")):
        fail(errors, ".DS_Store must not ship")

    for script_name in ("install.py", "verify_install.py", "uninstall.py"):
        if not ROOT.joinpath("scripts", script_name).is_file():
            fail(errors, f"missing installer script: {script_name}")

    result = {
        "valid": not errors,
        "release": "1.0.0-beta.4",
        "skills": len(EXPECTED),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
