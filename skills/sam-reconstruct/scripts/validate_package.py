from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "agents/openai.yaml", "references/sanmu-intake-and-delivery-contract.md",
    "references/reference-adaptation-contract.md",
    "references/original-reconstruction-contract.md", "references/content-framework-selector.md",
    "references/content-form-selector.md", "references/content-framework-case-index.md",
    "references/sanmu-writing-standard-v2-runtime.md", "references/output-contract.md",
    "references/source-map.md", "assets/output-template.md", "assets/state-delta.schema.json",
    "evals/eval_queries.json", "evals/evals.json",
]


def main() -> int:
    errors = [f"missing {p}" for p in REQUIRED if not ROOT.joinpath(p).is_file()]
    skill = ROOT.joinpath("SKILL.md").read_text(encoding="utf-8") if ROOT.joinpath("SKILL.md").is_file() else ""
    for phrase in ["参考内容改写与重构", "faithful_adaptation", "independent_reconstruction", "reference-adaptation-contract.md", "十维原创审计", "content-framework-selector.md", "同义替换", "方向成立门"]:
        if phrase not in skill:
            errors.append(f"SKILL missing {phrase}")
    match = re.search(r"(?m)^name:\s*(.+)$", skill)
    if not match or match.group(1).strip() != ROOT.name:
        errors.append("frontmatter name mismatch")
    try:
        queries = json.loads(ROOT.joinpath("evals/eval_queries.json").read_text(encoding="utf-8"))
        if sum(q.get("should_trigger") is True for q in queries) < 10 or sum(q.get("should_trigger") is False for q in queries) < 10:
            errors.append("trigger evals require 10 positive and 10 negative")
        quality = json.loads(ROOT.joinpath("evals/evals.json").read_text(encoding="utf-8"))["evals"]
        if len(quality) < 14:
            errors.append("quality evals require at least 14")
        schema_text = ROOT.joinpath("assets/state-delta.schema.json").read_text(encoding="utf-8")
        schema = json.loads(schema_text)
        for field in ["task_mode", "source_map", "preserve", "adapt", "rebuild", "direction_gate", "outline_gate", "completion_status"]:
            if field not in schema_text:
                errors.append(f"state schema missing {field}")
        if schema["properties"]["version"]["const"] != "2.5.0-beta":
            errors.append("state schema version is not 2.5.0-beta")
    except Exception as exc:
        errors.append(f"json parse error: {exc}")
    print(json.dumps({"valid": not errors, "skill": ROOT.name, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
