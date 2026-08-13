#!/usr/bin/env python3
"""Validate a sam-project-diagnosis state_delta JSON document.

This validator uses only the Python standard library so the Skill remains portable.

Exit codes:
0 valid
2 file or JSON error
3 contract validation failure
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


STAGES = {f"S{i}" for i in range(7)}
MODES = {"new", "checkup", "symptom"}
ROLES = {"owner", "subject", "operator", "advisor"}
CONFIDENCE = {"high", "medium", "low"}
LABELS = {"F", "O", "I", "H", "D", "U"}
DELIVERY_AUDIENCES = {"self", "team", "client", "project"}
DELIVERY_MODES = {"conversation", "tentative", "internal", "client", "ledger"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a Samskill project diagnosis state_delta JSON file."
    )
    parser.add_argument("--state", required=True, help="Path to the state_delta JSON file.")
    return parser.parse_args()


def fail(path: str, message: str, errors: list[dict[str, str]]) -> None:
    errors.append({"path": path, "message": message})


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_keys(obj: Any, keys: set[str], path: str, errors: list[dict[str, str]]) -> bool:
    if not isinstance(obj, dict):
        fail(path, "must be an object", errors)
        return False
    for key in sorted(keys - set(obj)):
        fail(f"{path}.{key}", "is required", errors)
    return True


def require_string_list(obj: Any, path: str, errors: list[dict[str, str]], min_items: int = 0) -> None:
    if not isinstance(obj, list):
        fail(path, "must be an array", errors)
        return
    if len(obj) < min_items:
        fail(path, f"must contain at least {min_items} item(s)", errors)
    for index, item in enumerate(obj):
        if not isinstance(item, str):
            fail(f"{path}[{index}]", "must be a string", errors)


def validate(state: Any) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    top = {
        "intake", "project_id", "generated_at", "diagnosis_mode", "user_role", "target",
        "stage", "capabilities", "evidence_added", "bottleneck", "decisions",
        "seven_day_plan", "permission", "versions"
    }
    if not require_keys(state, top, "$", errors):
        return errors

    if not nonempty(state.get("project_id")):
        fail("$.project_id", "must be a non-empty string", errors)

    intake = state.get("intake")
    intake_keys = {
        "delivery_audience", "delivery_mode", "confirmed", "tentative",
        "ambiguous", "conflicting", "unknown", "blocking_confirmations",
        "nonblocking_unknowns", "affected_sections",
    }
    if require_keys(intake, intake_keys, "$.intake", errors):
        if intake.get("delivery_audience") not in DELIVERY_AUDIENCES:
            fail("$.intake.delivery_audience", f"must be one of {sorted(DELIVERY_AUDIENCES)}", errors)
        if intake.get("delivery_mode") not in DELIVERY_MODES:
            fail("$.intake.delivery_mode", f"must be one of {sorted(DELIVERY_MODES)}", errors)
        for key in intake_keys - {"delivery_audience", "delivery_mode"}:
            require_string_list(intake.get(key), f"$.intake.{key}", errors)

    generated_at = state.get("generated_at")
    try:
        datetime.fromisoformat(str(generated_at).replace("Z", "+00:00"))
        if "T" not in str(generated_at):
            raise ValueError
    except ValueError:
        fail("$.generated_at", "must be an ISO 8601 date-time", errors)

    if state.get("diagnosis_mode") not in MODES:
        fail("$.diagnosis_mode", f"must be one of {sorted(MODES)}", errors)
    if state.get("user_role") not in ROLES:
        fail("$.user_role", f"must be one of {sorted(ROLES)}", errors)

    target = state.get("target")
    if require_keys(target, {"statement", "window"}, "$.target", errors):
        for key in ("statement", "window"):
            if not nonempty(target.get(key)):
                fail(f"$.target.{key}", "must be a non-empty string", errors)

    stage = state.get("stage")
    if require_keys(stage, {"code", "scope", "confidence"}, "$.stage", errors):
        if stage.get("code") not in STAGES:
            fail("$.stage.code", f"must be one of {sorted(STAGES)}", errors)
        if not nonempty(stage.get("scope")):
            fail("$.stage.scope", "must be a non-empty string", errors)
        if stage.get("confidence") not in CONFIDENCE:
            fail("$.stage.confidence", f"must be one of {sorted(CONFIDENCE)}", errors)

    capabilities = state.get("capabilities")
    if require_keys(capabilities, {"formed", "signals", "unvalidated"}, "$.capabilities", errors):
        for key in ("formed", "signals", "unvalidated"):
            require_string_list(capabilities.get(key), f"$.capabilities.{key}", errors)

    evidence = state.get("evidence_added")
    if not isinstance(evidence, list):
        fail("$.evidence_added", "must be an array", errors)
    else:
        for index, item in enumerate(evidence):
            path = f"$.evidence_added[{index}]"
            if require_keys(item, {"id", "label", "statement", "source"}, path, errors):
                if item.get("label") not in LABELS:
                    fail(f"{path}.label", f"must be one of {sorted(LABELS)}", errors)
                for key in ("id", "statement", "source"):
                    if not nonempty(item.get(key)):
                        fail(f"{path}.{key}", "must be a non-empty string", errors)

    bottleneck = state.get("bottleneck")
    if require_keys(bottleneck, {"module", "statement", "rationale"}, "$.bottleneck", errors):
        if not re.fullmatch(r"0[1-9]|1[0-7]", str(bottleneck.get("module", ""))):
            fail("$.bottleneck.module", "must be a two-digit module code from 01 to 17", errors)
        for key in ("statement", "rationale"):
            if not nonempty(bottleneck.get(key)):
                fail(f"$.bottleneck.{key}", "must be a non-empty string", errors)

    decisions = state.get("decisions")
    if require_keys(decisions, {"keep", "change", "defer"}, "$.decisions", errors):
        require_string_list(decisions.get("keep"), "$.decisions.keep", errors)
        require_string_list(decisions.get("change"), "$.decisions.change", errors, min_items=1)
        require_string_list(decisions.get("defer"), "$.decisions.defer", errors)

    plan = state.get("seven_day_plan")
    if not isinstance(plan, list) or not plan:
        fail("$.seven_day_plan", "must contain at least one action", errors)
    else:
        required = {"owner", "action", "output", "done_signal", "stop_condition"}
        for index, item in enumerate(plan):
            path = f"$.seven_day_plan[{index}]"
            if require_keys(item, required, path, errors):
                for key in required:
                    if not nonempty(item.get(key)):
                        fail(f"{path}.{key}", "must be a non-empty string", errors)

    permission = state.get("permission")
    if require_keys(permission, {"preview_only", "approved_write_path"}, "$.permission", errors):
        if permission.get("preview_only") is not True:
            fail("$.permission.preview_only", "must be true before explicit write authorization", errors)
        if permission.get("approved_write_path") is not None:
            fail("$.permission.approved_write_path", "must be null in preview state", errors)

    versions = state.get("versions")
    if require_keys(versions, {"skill", "atom_library"}, "$.versions", errors):
        if versions.get("skill") != "2.2.0-beta":
            fail("$.versions.skill", "must equal 2.2.0-beta", errors)
        if versions.get("atom_library") != "2.0":
            fail("$.versions.atom_library", "must equal 2.0", errors)

    return errors


def main() -> int:
    args = parse_args()
    path = Path(args.state).expanduser().resolve()
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"State file not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON at line {exc.lineno}: {exc.msg}", file=sys.stderr)
        return 2

    errors = validate(state)
    payload = {
        "valid": not errors,
        "state": str(path),
        "error_count": len(errors),
        "errors": errors,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not errors else 3


if __name__ == "__main__":
    raise SystemExit(main())
