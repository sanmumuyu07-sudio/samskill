#!/usr/bin/env python3
"""Standard-library release regression tests."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable


def run(*parts: str, expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [PYTHON, *parts],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != expect:
        raise AssertionError(
            f"command returned {result.returncode}, expected {expect}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


class ReleaseTests(unittest.TestCase):
    def test_release_validator(self) -> None:
        result = run("scripts/validate_public_release.py")
        self.assertTrue(json.loads(result.stdout)["valid"])

    def test_all_skills_validate(self) -> None:
        result = run("scripts/validate_skills.py")
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["count"], 18)

    def test_public_release_has_governance_files(self) -> None:
        required = {
            "TRADEMARKS.md",
            "THIRD_PARTY_NOTICES.md",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/workflows/validate.yml",
        }
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_no_private_markers_or_secret_shapes(self) -> None:
        blocked = (
            "zhuanzhuan" + "0000",
            "wx" + "id_",
            "Obsidian " + "Vault",
            "嘉寅文化" + "传媒有限公司",
        )
        secret_shapes = (
            "gh" + "p_",
            "github_" + "pat_",
            "BEGIN " + "PRIVATE KEY",
            "BEGIN RSA " + "PRIVATE KEY",
        )
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.suffix not in {".md", ".json", ".yaml", ".yml", ".py"} and path.name != "LICENSE":
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for marker in (*blocked, *secret_shapes):
                self.assertNotIn(marker, text, f"{path}: {marker}")

    def test_install_verify_repeat_and_uninstall(self) -> None:
        with tempfile.TemporaryDirectory(prefix="samskill-release-test-") as temp:
            target = Path(temp) / "skills"
            dry = run("scripts/install.py", "--target", str(target), "--dry-run")
            self.assertTrue(json.loads(dry.stdout)["dry_run"])
            run("scripts/install.py", "--target", str(target))
            verified = run("scripts/verify_install.py", "--target", str(target))
            self.assertTrue(json.loads(verified.stdout)["ok"])
            repeat = run("scripts/install.py", "--target", str(target), "--dry-run")
            self.assertTrue(all(item["action"] == "unchanged" for item in json.loads(repeat.stdout)["actions"]))
            preview = run("scripts/uninstall.py", "--target", str(target))
            self.assertTrue(json.loads(preview.stdout)["dry_run"])
            applied = run("scripts/uninstall.py", "--target", str(target), "--apply")
            self.assertFalse(json.loads(applied.stdout)["dry_run"])
            self.assertFalse((target / "samskill").exists())

    def test_conflict_refused_then_backed_up(self) -> None:
        with tempfile.TemporaryDirectory(prefix="samskill-conflict-test-") as temp:
            target = Path(temp) / "skills"
            custom = target / "sam-business"
            custom.mkdir(parents=True)
            (custom / "SKILL.md").write_text("custom\n", encoding="utf-8")
            refused = run("scripts/install.py", "--target", str(target), "--dry-run", expect=3)
            self.assertIn("sam-business", json.loads(refused.stdout)["conflicts"])
            run("scripts/install.py", "--target", str(target), "--force")
            backups = list((target / ".samskill-backups").glob("*/sam-business/SKILL.md"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "custom\n")

    def test_modified_install_requires_force_to_uninstall(self) -> None:
        with tempfile.TemporaryDirectory(prefix="samskill-modified-test-") as temp:
            target = Path(temp) / "skills"
            run("scripts/install.py", "--target", str(target))
            skill = target / "sam-topic" / "SKILL.md"
            skill.write_text(skill.read_text(encoding="utf-8") + "\nmodified\n", encoding="utf-8")
            refused = run("scripts/uninstall.py", "--target", str(target), "--apply", expect=3)
            self.assertIn("sam-topic", json.loads(refused.stdout)["changed"])
            self.assertTrue(skill.exists())

    def test_reconstruct_dual_mode_contract(self) -> None:
        directory = ROOT / "skills" / "sam-reconstruct"
        skill = (directory / "SKILL.md").read_text(encoding="utf-8")
        adaptation = (directory / "references" / "reference-adaptation-contract.md").read_text(encoding="utf-8")
        output = (directory / "assets" / "output-template.md").read_text(encoding="utf-8")
        schema = json.loads((directory / "assets" / "state-delta.schema.json").read_text(encoding="utf-8"))

        for phrase in ("faithful_adaptation", "independent_reconstruction", "reference-adaptation-contract.md"):
            self.assertIn(phrase, skill)
        for phrase in ("保留、适配、重建", "开头采用原稿优先", "批量改写"):
            self.assertIn(phrase, adaptation)
        self.assertIn("参考型改写", output)
        self.assertIn("独立原创重构", output)

        reconstruction = schema["properties"]["reconstruction"]
        self.assertEqual(
            reconstruction["properties"]["task_mode"]["enum"],
            ["faithful_adaptation", "independent_reconstruction"],
        )
        self.assertEqual(schema["properties"]["version"]["const"], "2.5.0-beta")


if __name__ == "__main__":
    unittest.main(verbosity=2)
