# Promotion

A repo nobody sees gets no stars. This file is the launch kit: exact metadata, where to post,
what to say, and what not to do. Copy-paste, then adjust the parts that sound like you.

Honest expectation first: **stars cannot be guaranteed.** What is in your control is (a) the repo
being genuinely useful in the first 60 seconds, (b) being findable by search, and (c) showing up
in the places where agent users already hang out. That is what this file covers.

## 0. Repo metadata (do this first)

```bash
gh repo edit Rachit-Sharma08/coding-agent-skills \
  --description "207 drop-in skills for Claude Code, OpenCode, Codex and Cursor — video, design, SEO, docs, backend, security, reverse engineering." \
  --add-topic agent-skills \
  --add-topic claude-code \
  --add-topic opencode \
  --add-topic codex \
  --add-topic cursor \
  --add-topic ai-agents \
  --add-topic llm \
  --add-topic skills \
  --add-topic prompt-engineering \
  --add-topic developer-tools \
  --add-topic anthropic \
  --add-topic mcp
```

Then, in the GitHub UI:

1. **Social preview** → Settings → Social preview → upload `assets/thumbnail.png` (1280×640).
   This is the card that shows on X, LinkedIn, Discord and Slack. Without it, shares look broken.
2. **Pin the repo** on your profile.
3. **Website field** → leave empty or point at a gist/site; do not put a placeholder.
4. **Release** `v1.0.0` with the skill count and the three best skills as highlights. Releases
   put the repo in GitHub's "Releases" feeds and give people a stable thing to link to.

## 1. Who this is for (pick your angle)

| Audience | Their pain | Your hook |
| --- | --- | --- |
| Claude Code / OpenCode users | "My agent is generic; it doesn't know my tools" | 207 skills, one clone, no plugin config |
| Agent-curious devs | "What is a skill, actually?" | `SKILL.md` explained in 10 lines + a real catalog |
| Video/design people | "AI can't edit my footage" | `ffmpeg-skill` does cuts, captions, loudness, reframes |
| Marketers | "AI writes slop copy" | the Corey Haines pack, credited, wired to fire on real phrasing |
| Security/RE folks | "Agents are useless for binaries" | Ghidra / Binary Ninja / semgrep / CodeQL skills |

Pick **one** angle per post. The repo can serve all five; a single post cannot.

## 2. Launch checklist (7 days)

| Day | Action |
| --- | --- |
| 0 | Metadata + social preview + release + pin. Ask 5 people who use coding agents to try one skill and tell you what broke. |
| 1 | **Show HN** (link post, your own words in the first comment). Best window: Tue–Thu, 08:00–10:00 ET. |
| 2 | **X thread** (below) + LinkedIn post. Tag nothing, hashtag nothing. |
| 3 | **Reddit** — one sub only: r/ClaudeAI *or* r/opencode. Answer every comment for 2 hours. |
| 4 | **dev.to / Hashnode** post: "What an agent skill actually is" with your repo as the example. |
| 5 | **Awesome-list PRs** (see §5). These are slow but they are the durable traffic. |
| 6 | Second Reddit sub with a *different* post (a teardown of one skill, not the repo again). |
| 7 | Write down what worked (referrers in Insights), then go back to shipping skills. |

Do not post to five subreddits on the same day with the same text. That is how accounts get
banned and repos get flagged as spam.

## 3. Show HN

**Title:** `Show HN: 207 agent skills for coding agents (Claude Code, OpenCode, Codex)`

**First comment:**

> I use coding agents all day and kept rewriting the same instructions: how to cut a video with
> ffmpeg, how to audit a page, how to not wreck a Stripe integration. So I collected them into
> skill folders — a `SKILL.md` with a description the agent matches on, plus the instructions it
> loads when it matches. 207 of them now, all installed and used, not scraped.
>
> Two things I learned building this that might be useful even if you don't want the repo:
>
> 1. The `description` is the whole product. It is the only thing the agent sees before deciding
>    to load the skill. Vague descriptions = skills that never fire.
> 2. More skills is not better. Past ~200 the agent starts picking the wrong one, so the repo
>    ships a rule: max 3 skills, most specific wins, no match means no skill.
>
> Happy to answer anything about the format, or where it breaks.

## 4. X / Twitter thread

```
Coding agents are only as good as the instructions you give them.

I collected 207 of those instructions into reusable skills — video editing, SEO, Stripe,
Ghidra, Word docs, design systems.

Free, MIT, one clone. 🧵
```

```
1/ A "skill" is a folder with a SKILL.md:

name: ffmpeg-skill
description: Edit video and audio with local FFmpeg... use when the user mentions a clip,
captions, a reel, LUFS

The description is the trigger. The rest of the file is what the agent reads after it fires.
```

```
2/ What's inside:

• ffmpeg-skill — 42 scripts, cuts to captions to loudness
• impeccable — UI that doesn't look like a template
• seo-audit / ai-seo — the Corey Haines pack, credited
• docx / pdf / pptx / xlsx — real files, not chat output
• ghidra / semgrep / codeql — security work
```

```
3/ The part nobody talks about: 200+ skills installed is a liability.

Past a point the agent picks the wrong one. The repo ships the rule I actually use:

- clear description match only
- max 3 skills per task
- if two match, take the more specific one
- no match → no skill
```

```
4/ Install (OpenCode):

cp -R skills/* ~/.agents/skills/

Claude Code:

cp -R skills/* ~/.claude/skills/

Then restart the session — skills load at startup, not mid-session.

Repo + full catalog: https://github.com/Rachit-Sharma08/coding-agent-skills

If one saves you an afternoon, a star helps other people find it.
```

## 5. Reddit / forum post (r/ClaudeAI or r/opencode)

**Title:** `I put 207 agent skills in one repo — here's what actually made them fire`

> Most "skill collections" fail for the same reason: the description is written like marketing
> copy instead of a trigger. I went through mine and rewrote them to use the words people
> actually type — including Hinglish, because that is how I talk to my agent.
>
> What is in the repo: video/audio (ffmpeg, 42 scripts), design (impeccable, ui-ux-pro-max),
> marketing/SEO (the Corey Haines pack, credited), docs (docx/pdf/pptx/xlsx), backend (Stripe,
> Supabase, Prisma, Better Auth), security/RE (Ghidra, Binary Ninja, semgrep, CodeQL), and the
> workflow skills I use to stop the agent from free-styling (brainstorming → plan → execute →
> verify).
>
> Two things that changed the results more than adding skills:
>
> 1. Max 3 skills per task. Past that, the agent starts blending instructions.
> 2. If no skill clearly matches, it works without one. A forced skill is worse than none.
>
> Repo (MIT, catalog in SKILLS.md): https://github.com/Rachit-Sharma08/coding-agent-skills
>
> If you install it and something doesn't fire, tell me the phrasing you used — that is the bug
> I care about.

## 6. Awesome-list PRs (durable traffic)

Open a PR adding one line to the relevant section — follow each list's format exactly, and only
where agent skills/tools are actually accepted:

- `hesreallyhim/awesome-claude-code` → Skills section
- `awesome-opencode` / OpenCode community lists → Plugins & Skills
- `punkpeye/awesome-mcp-servers` → only if you add an MCP-backed skill (not yet)
- `e2b-dev/awesome-ai-agents` → Tools
- Any "awesome-ai-coding" list with a Skills or Prompts section

PR description: one line on what it is, one line on why it belongs in that section. No pitch.

## 7. Keep the feed alive (this is what actually compounds)

Stars come in waves that follow *new* content, not the initial post.

- **Ship weekly.** One new skill, or one rewritten description, per week. Cut a release each
  time (`gh release create v1.0.x --generate-notes`). Releases show in followers' feeds.
- **Write the post, not the ad.** "How I made my agent stop guessing which skill to use" gets
  read; "check out my repo" does not.
- **Answer the trigger questions.** Every "why isn't my skill loading" thread on Reddit/Discord
  is a chance to link the troubleshooting section, not the repo root.
- **Add a `docs/` example per month** — one real before/after (a video edited, an audit run).
  Screenshots beat description text every time.
- **Track one number:** referrers → github.com in Insights. If Reddit sends nothing after two
  posts, your title is the problem, not the sub.

## 8. What not to do

- No bought stars, no star-exchange groups. They get accounts flagged and the repo delisted from
  search.
- No mass DMs with the link.
- No "1000 skills!" claims. Precision is the selling point.
- No reposting someone else's skill folder without its LICENSE and credit — that is the one
  thing that turns a launch into a takedown.
