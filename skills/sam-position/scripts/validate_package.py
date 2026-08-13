#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

def main() -> int:
    parser=argparse.ArgumentParser(description="Validate a Samskill package")
    parser.add_argument("--skill", default=str(Path(__file__).resolve().parent.parent))
    args=parser.parse_args(); root=Path(args.skill).resolve(); errors=[]
    skill=root/"SKILL.md"
    if not skill.is_file(): errors.append("SKILL.md missing")
    else:
        text=skill.read_text(encoding="utf-8")
        m=re.match(r"^---\n(.*?)\n---", text, re.S)
        if not m: errors.append("frontmatter invalid")
        else:
            fields={line.partition(":")[0].strip():line.partition(":")[2].strip() for line in m.group(1).splitlines() if ":" in line}
            if fields.get("name") != root.name: errors.append("name mismatch")
            if not 1 <= len(fields.get("description", "")) <= 1024: errors.append("description length invalid")
        if len(text.splitlines()) >= 500: errors.append("SKILL.md exceeds 500 lines")
        for rel in re.findall(r"`((?:references|assets|scripts)/[^`\s]+)`", text):
            if not (root/rel).exists(): errors.append(f"missing reference: {rel}")
        if "TODO" in text: errors.append("TODO remains")
    for path in root.rglob("*.json"):
        try: json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc: errors.append(f"invalid JSON {path.name}: {exc}")
    eq=root/"evals"/"eval_queries.json"
    if eq.is_file():
        q=json.loads(eq.read_text(encoding="utf-8")); pos=sum(x.get("should_trigger") is True for x in q); neg=sum(x.get("should_trigger") is False for x in q)
        if pos < 10 or neg < 10: errors.append(f"trigger minimum {pos}/{neg}")
    result={"valid":not errors,"skill":str(root),"errors":errors}
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if not errors else 1
if __name__ == "__main__": raise SystemExit(main())
