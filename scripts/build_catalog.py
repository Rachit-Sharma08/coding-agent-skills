"""Regenerate SKILLS.md from the frontmatter of every skills/<name>/SKILL.md.

Usage: python scripts/build_catalog.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def field(fm: str, key: str) -> str:
    """Read a top-level or one-level-indented YAML scalar, quoted or folded."""
    m = re.search(rf"(?m)^\s*{key}:\s*(.*)$", fm)
    if not m:
        return ""
    value = m.group(1).strip()
    if value in ("|", ">", "|-", ">-", "", "''", '""'):
        # Block scalar or empty: grab the indented lines that follow.
        start = m.end() + 1
        lines = fm[start:].split("\n")
        block = []
        for line in lines:
            if line.strip() and not line.startswith((" ", "\t")):
                break
            block.append(line.strip())
        value = " ".join(block).strip()
    if len(value) > 1 and value[0] == value[-1] and value[0] in "'\"":
        quote = value[0]
        value = value[1:-1].replace(quote * 2, quote)
    return " ".join(value.split())


PREFIXES = (
    "When the user wants to ",
    "When the user wants ",
    "Use when the user wants to ",
    "Use when someone wants to ",
    "When someone wants to ",
    "Use when ",
)


def first_sentence(text: str, limit: int = 160) -> str:
    text = text.replace("|", "/")
    for prefix in PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):]
            text = text[:1].upper() + text[1:]
            break
    cut = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9'\"`(])", text, maxsplit=1)[0]
    if len(cut) > limit:
        cut = cut[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:.-") + "…"
    return cut.strip()


def main() -> None:
    rows = []
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        fm = frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        name = field(fm, "name") or path.parent.name
        desc = field(fm, "description")
        license_file = path.parent / "LICENSE" if (path.parent / "LICENSE").exists() else None
        rows.append(
            {
                "name": name,
                "dir": path.parent.name,
                "summary": first_sentence(desc) if desc else "(no description)",
                "license": "yes" if license_file else "",
            }
        )
    rows.sort(key=lambda r: r["name"].lower())

    lines = [
        "# Skill Catalog",
        "",
        f"All **{len(rows)}** skills in this repo, A–Z. Click a skill name to open its folder;",
        "every folder has a `SKILL.md` with the full instructions the agent loads.",
        "",
        "> Regenerate this file with `python scripts/build_catalog.py` after adding or editing a skill.",
        "",
        "| Skill | What it does |",
        "| --- | --- |",
    ]
    for r in rows:
        summary = r["summary"] + (" _(see skill LICENSE)_" if r["license"] else "")
        lines.append(f"| [`{r['name']}`](skills/{r['dir']}/) | {summary} |")
    lines += [
        "",
        "## Notes",
        "",
        "- `license` marker means the skill folder ships its own LICENSE file; check it before",
        "  redistributing that folder on its own.",
        "- Skill names are stable IDs. Rename a folder and update `name:` in its `SKILL.md`",
        "  together, or agents will load the wrong one.",
        "",
    ]
    (ROOT / "SKILLS.md").write_text("\n".join(lines), encoding="utf-8")

    stats = {
        "skills": len(rows),
        "with_own_license": sum(1 for r in rows if r["license"]),
        "names": [r["name"] for r in rows],
    }
    (ROOT / "scripts" / "skills.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(f"SKILLS.md written: {len(rows)} skills, {stats['with_own_license']} with own LICENSE")


if __name__ == "__main__":
    main()
