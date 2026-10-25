# Contributing

Adding a skill is three steps. Keep it that small.

## 1. Create the folder

```
skills/<kebab-case-name>/
  SKILL.md          required
  scripts/          optional
  references/       optional
  LICENSE           required if the skill is not yours
```

## 2. Write `SKILL.md`

```markdown
---
name: <same as folder name>
description: >
  What the skill does, then when to use it. Name the words a user would actually type —
  file types, tool names, job names, other languages if you use them. This field is the
  only thing the agent sees before deciding to load the skill.
metadata:
  opencode/autoinvoke: true
---

# <name>

Short intro: what this is for, what it needs installed.

## Workflow
1. ...
2. ...

## Rules
- What to never do.
- What to do when the input is missing.
```

Rules that keep the catalog usable:

- **`name` matches the folder.** Mismatches cause double-loads and confusion.
- **`description` starts with the job, not the vibe.** "Edit video and audio with FFmpeg…"
  beats "A powerful video solution."
- **Name the trigger words.** Include the file extensions, the tool names and the phrasing you
  use. A skill that never fires is a dead file.
- **No secrets, no absolute paths to your machine.** Use `~` or relative paths.
- **Scripts get an `--help` and fail loudly.** The agent reads errors.

## 3. Regenerate the catalog

```bash
python scripts/build_catalog.py     # rewrites SKILLS.md and scripts/skills.json
```

Commit `SKILLS.md` with your skill — a PR that adds a folder without updating the catalog gets
asked to run the script.

## Pull requests

- One skill per PR (or one fix per PR). Easier to review, easier to revert.
- Say where the skill came from and under what license. No source, no merge.
- Do not relicense somebody else's folder. Keep their `LICENSE` file.
- Test it: install the folder, restart your agent, ask for the job in plain language, confirm
  the skill loads on its own.

## Not accepted

- Skills that only restate what a competent model already does (a "write a function" skill).
- Skills that phone home, collect data, or install things silently.
- Skills that need credentials baked in.
- Offensive-security tooling that ships exploit payload libraries. Point at the tool, do not
  vendor the arsenal.
