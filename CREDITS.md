# Credits

## Owner

**[Rachit Sharma](https://github.com/Rachit-Sharma08)** — collected, curated, edited and wired
this collection together: picked which skills were worth keeping, tightened descriptions so they
fire on the right request, added extra triggers (including Hinglish phrasing, because that is how
he actually talks to his agent), removed duplicates and dead skills, wrote `artemis-android-control`,
and built the catalog and install tooling. Without that work this would be an unreadable dump of
folders.

## Upstream work

Most skills started life as somebody else's public work. Credit where it is due:

| Source | What it covers here |
| --- | --- |
| [Anthropic's public skills](https://github.com/anthropics/skills) | `docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`, `canvas-design`, `brand-guidelines`, `web-artifacts-builder`, `slack-gif-creator`, `internal-comms`, `doc-coauthoring` and related document/design skills |
| [obra/superpowers](https://github.com/obra/superpowers) | The workflow skills: `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`, `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `requesting-code-review`, `receiving-code-review`, `finishing-a-development-branch`, `writing-skills`, `using-superpowers`, `diagnosing-superpowers` |
| [Corey Haines — `coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) — MIT, © 2025 | The marketing/SEO pack: `ai-seo`, `seo-audit`, `cro`, `copywriting`, `content-strategy`, `analytics`, `social`, `schema`, `programmatic-seo`, `competitor-alternatives`, and the `geo-*` family |
| [kajisho5](https://github.com/kajisho5) — MIT, © 2026 | `ffmpeg-skill` |
| [Browser Use](https://github.com/browser-use) — MIT, © 2026 | `video-use` |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Reference material inside `security-review` |
| [Blackmagic Design](https://www.blackmagicdesign.com/) documentation | `davinci-resolve` references (folder ships AGPL-3.0) |
| [Dietrich Gebert](https://github.com/dietrichgebert) — `@dietrichgebert/ponytail` | The Ponytail discipline skills (`ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, …) |
| [Google — ARTEMIS](https://github.com/google/artemis) — Apache-2.0 | Basis for `artemis-android-control` |

Skills without a named source above were written or heavily rewritten for this collection, or
come from authors whose license file travels with the folder. **Every folder that has its own
`LICENSE` keeps it** — that file, not this one, governs that folder.

## License map

- Repo scaffolding — `README.md`, `SETUP.md`, `SKILLS.md`, `CREDITS.md`, `PROMOTION.md`,
  `CONTRIBUTING.md`, `scripts/*` — MIT (see [LICENSE](LICENSE)).
- Each `skills/<name>/` folder — its own license if present, otherwise MIT as part of this repo.
- 20 skill folders ship a `LICENSE` or `LICENSE.txt` (marketing pack, `ffmpeg-skill`,
  `video-use`, `davinci-resolve`, `security-review`, …). Read it before republishing that folder
  on its own.

## Attribution requests and takedowns

If you wrote one of these skills and the credit is wrong, or you want it removed:

1. Open an issue titled `attribution: <skill-name>` (or email via the GitHub profile).
2. A wrong credit gets fixed. A removal request gets the folder deleted from the repo and from
   history within 72 hours, no argument.

## Contributing a skill

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills must say where they came from and under what
license, or they are not merged.
