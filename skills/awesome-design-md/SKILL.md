---
name: awesome-design-md
description: >
  Give an agent a real brand's design system as a single DESIGN.md file, before it writes any
  UI. Use when the user says "make it look like Stripe / Apple / Linear / Vercel / Notion",
  "use this brand's style", "match this design language", "I need a DESIGN.md", "set up a
  design system file", "premium look", "brand-consistent UI", or when a project needs one
  plain-text source of truth for colors, type, spacing, components and shadows that both the
  coding agent and Google Stitch can read. Ships no code — it fetches or writes the DESIGN.md
  and then holds the agent to it.
metadata:
  opencode/autoinvoke: true
---

# awesome-design-md

`DESIGN.md` is the design counterpart of `AGENTS.md`: a plain markdown file at the project root
that says how the product should **look**, while `AGENTS.md` says how it should be **built**.
Every serious UI task should start by reading or creating one — otherwise the agent invents a
new visual language on every page.

Source of ready-made files: **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)**
(MIT, 70+ brands, one folder each under `design-md/<brand>/`).

## Workflow

### 1. Does the project already have one?

```bash
ls DESIGN.md docs/DESIGN.md .stitch/DESIGN.md 2>/dev/null
```

If yes: read it and follow it. Do not "improve" it unless the user asked for a redesign — that
is how a consistent product turns into five different ones.

### 2. Brand named → fetch that DESIGN.md

```bash
# one brand, straight into the project root
curl -fsSL https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/<brand>/DESIGN.md \
  -o DESIGN.md
```

No network, or the brand folder is not in the list? Clone once and browse locally:

```bash
git clone --depth 1 https://github.com/VoltAgent/awesome-design-md.git /tmp/awesome-design-md
ls /tmp/awesome-design-md/design-md
cp /tmp/awesome-design-md/design-md/<brand>/DESIGN.md ./DESIGN.md
```

Each brand folder usually also carries `preview.html` / `preview-dark.html` — open them to check
the palette and type scale before committing to it.

### 3. No brand named, or none of them fit → write one

Use `stitch-design-taste` (generates a DESIGN.md from a brief) or `extract-design-system`
(pulls tokens from a live site). Fill the same nine sections the collection uses:

1. Visual theme and atmosphere
2. Color palette with **semantic** roles (not just hex codes)
3. Typography hierarchy (families, sizes, weights, line heights)
4. Component styling and states (button, card, input, nav — default/hover/active/disabled)
5. Layout: spacing scale, grid, whitespace philosophy
6. Depth: shadows, borders, surface hierarchy
7. Do's and don'ts (the anti-patterns that break the look)
8. Responsive behavior and touch targets
9. Agent prompt guide: the quick color reference + a ready prompt

### 4. Make the agent obey it

In the same task where the UI is built, state the constraint explicitly:

> Follow `DESIGN.md` for every color, font size, spacing value and component state. If a value
> is missing, extend the file — do not invent a new one inline.

Add that line to `AGENTS.md` (or `CLAUDE.md`) once, so every future session inherits it:

```markdown
## Design
All UI follows `DESIGN.md`. Read it before writing components. New tokens go into that file first.
```

### 5. Check the result

- Colors in the code match the palette section, and every color used is in the file.
- Only the type scale in the file is used (no one-off `text-[13px]`).
- Spacing comes from the scale, not random values.
- Hover/active/focus/disabled states exist for every interactive element the file defines.
- Light and dark surfaces are both legible if the file defines both.

## Rules

1. **One DESIGN.md per project.** Two files = two designs.
2. **The file wins over taste.** If the agent disagrees with the file, it proposes an edit to the
   file — it does not silently deviate in one component.
3. **These files are reverse-engineered, not brand-approved.** Treat them as a strong starting
   point, never claim the output is an official Apple/Stripe/Linear page, and never copy a
   brand's logo or proprietary assets because the palette matches.
4. **Tokens first, components second.** A component that hardcodes a color is a bug.
5. **Keep it small.** A DESIGN.md that is 2000 lines never gets read; 150–400 lines that the
   agent actually follows beats an exhaustive one it skips.

## Related skills

`stitch-design-taste` (write a DESIGN.md from scratch) · `extract-design-system` (from a live
URL) · `design-system` (token architecture and component specs) · `design-taste-frontend`
(anti-slop landing pages) · `image-to-code` (screenshot → implementation).
