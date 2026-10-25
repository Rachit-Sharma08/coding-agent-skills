# Setup

Five minutes, no build step. A skill is a folder with a `SKILL.md` inside it — installing one
means putting that folder where your agent looks for skills (or telling the agent where it is).

- [1. Get the repo](#1-get-the-repo)
- [2. Install](#2-install)
- [3. Verify](#3-verify)
- [4. Auto-invoke in OpenCode](#4-auto-invoke-in-opencode)
- [5. Give the skill a second language](#5-give-the-skill-a-second-language)
- [6. Troubleshooting](#6-troubleshooting)

## 1. Get the repo

```bash
git clone https://github.com/Rachit-Sharma08/coding-agent-skills.git
cd coding-agent-skills
```

The repo is ~64 MB because a few skills ship real assets (`ffmpeg-skill`, `davinci-resolve`,
`shopify`). If you only want a handful, use a sparse checkout:

```bash
git clone --filter=blob:none --sparse https://github.com/Rachit-Sharma08/coding-agent-skills.git
cd coding-agent-skills
git sparse-checkout set skills/ffmpeg-skill skills/impeccable skills/seo-audit
```

## 2. Install

### OpenCode

Two folders are read, in this order:

| Scope | Path |
| --- | --- |
| Global | `~/.agents/skills/` |
| Global (alt) | `~/.config/opencode/skills/` |
| Project | `<project>/.agents/skills/` |
| Project (alt) | `<project>/.opencode/skills/` |

```powershell
# Windows — global
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.agents\skills\"

# Windows — one project only
Copy-Item -Recurse -Force .\skills\impeccable,.\skills\ffmpeg-skill "D:\my-app\.agents\skills\"
```

```bash
# macOS / Linux
cp -R skills/* ~/.agents/skills/                       # global
cp -R skills/impeccable skills/seo-audit .agents/skills/ # project
```

Or let the helper do it:

```powershell
.\scripts\install.ps1 -Target opencode
.\scripts\install.ps1 -Target claude
.\scripts\install.ps1 -Path D:\my-app\.agents\skills
```

### Claude Code

| Scope | Path |
| --- | --- |
| Personal | `~/.claude/skills/` |
| Project | `<project>/.claude/skills/` |

```bash
mkdir -p ~/.claude/skills && cp -R skills/* ~/.claude/skills/
```

Claude Code reads the same `SKILL.md` format (`name` + `description` frontmatter). The
`metadata.opencode/autoinvoke` field is ignored there.

### Codex, Cursor, Gemini CLI, anything else

These agents do not all have a skills folder, but they all read a project instruction file
(`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules`). Give them a pointer and they will
open the skill when they need it:

```markdown
## Skills

Skills live in `./skills/`. Each is a folder with a `SKILL.md` whose `description` says when
to use it. Before doing a task, check `SKILLS.md` for a matching skill and read that
`SKILL.md` before starting. Do not load more than 3 skills for one task.
```

If your Codex build supports a skills directory, `~/.codex/skills/` follows the same layout —
copy the folders there and skip the pointer.

## 3. Verify

1. Start a new session (agents read skill folders at startup, not mid-session).
2. Ask: **"list the skills you can see"** — the installed names should come back.
3. Ask for a job one specific skill owns, e.g. *"probe this video file and tell me its codecs"*.
   The agent should load `ffmpeg-skill` on its own and say so.

If step 2 shows nothing, your agent is not reading that folder — move the skill to a path from
the table above, then restart the session.

## 4. Auto-invoke in OpenCode

OpenCode only auto-loads skills that opt in. Every skill in this repo already has it:

```yaml
metadata:
  opencode/autoinvoke: true
```

If you copy in a skill from somewhere else and it never fires on its own, that line is usually
what is missing. Add it to the frontmatter and restart.

## 5. Give the skill a second language

The `description` is the trigger. If you talk to your agent in another language, add your words
to it — otherwise the skill stays silent while you keep describing the task in Hinglish:

```yaml
description: >
  Edit video and audio with local FFmpeg... Use whenever the user mentions a video file,
  captions, a reel, LUFS, transcoding — or says "video banao", "edit kar do", "shorts banao".
```

Same for names people actually type: "word doc", "deck", "spreadsheet", "landing page".

## 6. Troubleshooting

**Skill never loads.** The description does not contain the words you use. Add them. A skill
whose description says "optimize conversion" will not fire on "why is nobody signing up".

**Three skills fire at once.** You installed too many overlapping skills, or the request is
genuinely broad. Keep the rule: max 3, most specific wins, no match means no skill.

**Two skills with the same `name:`.** The agent picks one and you get unpredictable behaviour.
Rename the folder and the `name:` field together.

**Copy fails on Windows with long paths.** Use `robocopy` (it handles long paths):

```powershell
robocopy .\skills "$env:USERPROFILE\.agents\skills" /E
```

**Agent says the skill loaded but the scripts fail.** Skills that ship scripts need their
runtime: `ffmpeg-skill` and `video-use` need FFmpeg on `PATH` and Python 3.10+; `docx`/`pdf`/
`pptx`/`xlsx` need the Python libs their `SKILL.md` lists; `ghidra` needs Ghidra installed.
Read the top of the skill — it says what it expects.

**Everything feels slower.** Each installed skill's name and description sit in the agent's
context. 200+ is fine on a large-context model and wasteful on a small one. Install what your
work actually needs; the rest stay in the repo for later.

**A skill folder's license is not MIT.** Correct — some folders carry their own license (see
[CREDITS.md](CREDITS.md)). Keeping the folder intact keeps the license intact.
