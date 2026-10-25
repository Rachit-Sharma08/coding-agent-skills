---
colors:
  od-bg: "#f3ecd9"
  od-bg-deep: "#ece2c9"
  od-surface: "#faf6ec"
  od-fg: "#161513"
  od-muted: "#2a2622"
  od-line: "#1b1a18"
  od-accent: "#f0a87a"
  od-accent-strong: "#e88c5a"
  od-agent-text: "#5b7a4a"
  od-agent-voice: "#f0c860"
  od-agent-video: "#b8c8d8"
  od-agent-edit: "#6b4a7a"
  od-light-ribbon: "#161513"
  od-light-highlight: "#f0c860"
  od-light-highlight-peach: "#f0a87a"

typography:
  # --- Reading ramp (carried from design.md, px + cqw equivalents) ---
  workspace-heading:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "32px"            # ≈1.67cqw — chrome only at frame scale
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.01em"
  card-heading:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "1.46cqw"          # ≈28px@1920 — chrome
    fontWeight: 500
    lineHeight: 1.05
  body-lead:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "1.56cqw"          # ≈30px@1920 — at floor
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "1.45cqw"          # ≈28px@1920 — body lifted to floor for frames
    fontWeight: 400
    lineHeight: 1.5
  mono-label:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.78cqw"          # ≈15px — chrome only
    fontWeight: 500
    textTransform: "uppercase"
    letterSpacing: "0.18em"
  mono-label-readable:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "1.4cqw"           # at floor — load-bearing mono
    fontWeight: 500
    textTransform: "uppercase"
    letterSpacing: "0.16em"

  # --- Display / hero ramp (frame-native, far larger than web) ---
  wordmark-mega:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "30cqw"            # identity cover, single-word wordmark
    fontWeight: 500
    lineHeight: 0.84
    letterSpacing: "-1.6cqw"
  display-hero:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "14cqw"            # ≤3-word claims
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: "-0.6cqw"
  display-claim:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "9cqw"             # 4–6 word claims
    fontWeight: 500
    lineHeight: 0.96
    letterSpacing: "-0.32cqw"
  display-claim-long:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "6.2cqw"           # 7+ word claims
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.18cqw"
  serif-accent-hero:
    fontFamily: "Instrument Serif, Times New Roman, serif"
    fontStyle: "italic"
    fontSize: "14cqw"            # paired with display-hero, one word only
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: "-0.2cqw"
  serif-accent-claim:
    fontFamily: "Instrument Serif, Times New Roman, serif"
    fontStyle: "italic"
    fontSize: "9cqw"
    fontWeight: 400
    lineHeight: 0.96
  section-head:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "4.2cqw"           # ledger/catalog headers
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: "-0.08cqw"
  stat-numeral:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "22cqw"            # focal stat numerals
    fontWeight: 500
    lineHeight: 0.88
    letterSpacing: "-0.6cqw"
  stat-ledger:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "3.6cqw"           # ledger-cell numerals (dense exception)
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: "-0.06cqw"
  ribbon-marquee:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: "4.8cqw"           # text inside the ink ribbon
    fontWeight: 500
    textTransform: "uppercase"
    letterSpacing: "0.04em"

rounded:
  pill: "999px"
  small: "14px"
  card: "22px"
  module: "24px"
  stage: "32px"
  band: "48px"

spacing:
  # Carried from design.md
  container-max: "1320px"
  gutter-desktop: "32px"
  gutter-tablet: "20px"
  gutter-mobile: "16px"
  section-pad: "96px"
  section-pad-major: "120px"
  grid-gap: "24px"
  card-pad: "24px"
  card-pad-lg: "28px"
  module-gap: "24px"
  compact-row-gap: "12px"
  # Frame-scale additions
  frame-pad: "5cqw"              # safe area on the long edge
  frame-pad-short: "5.5cqh"      # safe area on the short edge
  rail-gap: "2cqw"
  chip-gap: "1.2cqw"

components:
  # ---- Atoms carried from design.md, kept at chrome scale ----
  pill-nav:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.6cqw 1.4cqw"
    shadow: "0 2px 0 {colors.od-fg}"
  pill-nav-active:
    backgroundColor: "{colors.od-fg}"
    textColor: "{colors.od-bg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.6cqw 1.4cqw"
    shadow: "0 2px 0 {colors.od-fg}"
  chip-mono:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.5cqw 1.1cqw"
  chip-peach:
    backgroundColor: "{colors.od-accent}"
    textColor: "{colors.od-fg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.5cqw 1.1cqw"
  chip-butter:
    backgroundColor: "{colors.od-agent-voice}"
    textColor: "{colors.od-fg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.5cqw 1.1cqw"
  button-primary:
    backgroundColor: "{colors.od-fg}"
    textColor: "{colors.od-bg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.7cqw 1.6cqw"
    shadow: "0 2px 0 {colors.od-fg}"
  card-paper:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.module}"
    padding: "{spacing.card-pad}"
    shadow: "0 3px 0 {colors.od-fg}"
  card-cream-deep:
    backgroundColor: "{colors.od-bg-deep}"
    textColor: "{colors.od-fg}"
    border: "1.5px solid {colors.od-fg}"
    rounded: "{rounded.module}"
    padding: "{spacing.card-pad}"
    shadow: "0 3px 0 {colors.od-fg}"

  # ---- Frame-scale variants (NEW) ----
  pill-nav-giant:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "0.18cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "1.2cqw 2.4cqw"
    shadow: "0 0.32cqw 0 {colors.od-fg}"
  pill-nav-giant-active:
    backgroundColor: "{colors.od-fg}"
    textColor: "{colors.od-bg}"
    border: "0.18cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "1.2cqw 2.4cqw"
    shadow: "0 0.32cqw 0 {colors.od-fg}"
  chip-mono-giant:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "0.16cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "0.9cqw 1.8cqw"
  chip-peach-giant:
    backgroundColor: "{colors.od-accent}"
    textColor: "{colors.od-fg}"
    border: "0.16cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "0.9cqw 1.8cqw"
  chip-butter-giant:
    backgroundColor: "{colors.od-agent-voice}"
    textColor: "{colors.od-fg}"
    border: "0.16cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "0.9cqw 1.8cqw"
  chip-moss-giant:
    backgroundColor: "{colors.od-agent-text}"
    textColor: "{colors.od-bg}"
    border: "0.16cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "0.9cqw 1.8cqw"
  button-primary-giant:
    backgroundColor: "{colors.od-fg}"
    textColor: "{colors.od-bg}"
    border: "0.2cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label-readable}"
    padding: "1.6cqw 3.2cqw"
    shadow: "0 0.42cqw 0 {colors.od-fg}"
  highlight-peach-pill:
    # The italic-serif word sitting inside a peach pill, inline with a headline.
    backgroundColor: "{colors.od-accent}"
    textColor: "{colors.od-fg}"
    rounded: "{rounded.pill}"
    padding: "0.4cqw 2.2cqw"
  highlight-butter-pill:
    backgroundColor: "{colors.od-agent-voice}"
    textColor: "{colors.od-fg}"
    rounded: "{rounded.pill}"
    padding: "0.4cqw 2.2cqw"
  card-frame:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "0.2cqw solid {colors.od-fg}"
    rounded: "{rounded.stage}"
    padding: "2.6cqw"
    shadow: "0 0.5cqw 0 {colors.od-fg}"
  card-cream-deep-frame:
    backgroundColor: "{colors.od-bg-deep}"
    textColor: "{colors.od-fg}"
    border: "0.2cqw solid {colors.od-fg}"
    rounded: "{rounded.stage}"
    padding: "2.6cqw"
    shadow: "0 0.5cqw 0 {colors.od-fg}"
  agent-card:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "0.18cqw solid {colors.od-fg}"
    rounded: "{rounded.card}"
    padding: "1.6cqw 1.8cqw"
    shadow: "0 0.4cqw 0 {colors.od-fg}"
  ledger-cell:
    backgroundColor: "{colors.od-surface}"
    textColor: "{colors.od-fg}"
    border: "0.14cqw solid {colors.od-fg}"
    rounded: "{rounded.small}"
    padding: "1.1cqw 1.2cqw"
  ribbon-band:
    backgroundColor: "{colors.od-light-ribbon}"
    textColor: "{colors.od-bg}"
    typography: "{typography.ribbon-marquee}"
    padding: "1.6cqw 5cqw"
  state-dot:
    size: "1.0cqw"
    border: "0.14cqw solid {colors.od-fg}"
    rounded: "{rounded.pill}"
  stage-hero:
    backgroundColor: "{colors.od-bg-deep}"
    textColor: "{colors.od-fg}"
    border: "0.22cqw solid {colors.od-fg}"
    rounded: "{rounded.stage}"
    padding: "3cqw"
    shadow: "0 0.6cqw 0 {colors.od-fg}"
  dark-theater:
    backgroundColor: "{colors.od-fg}"
    textColor: "{colors.od-bg}"
    border: "0.18cqw solid {colors.od-line}"
    rounded: "{rounded.stage}"
    padding: "3cqw"
    shadow: "none"
---

# FRAME.md — Vibe Life, at frame scale

> **Atoms are sacred · composition is free · numbers come from the script.**

## Overview

Vibe Life is a warm editorial studio with a friendly little operating system inside it. At frame scale, the brand reads as **cream paper, ink outline, one italic serif word, one accent pill** — never dark dev-tool chrome, never pastel AI slop, never a SaaS feature grid. Frames are hand-placed: large editorial type sits on a paper ground, a 1.5px ink line draws the boundary, a flat 2–3px hard shadow gives gravity, and a single peach or butter pill carries the human voltage. Italic Instrument Serif is the brand's voice — used on **one** word per frame, never a full line, never a system label. Mono uppercase is reserved for state and metadata: AGENT · READY · DRAFT-04. The frame is the unit; the slideshow is the enemy.

**Frame Craft Bar**

- **Squint test** — one element dominates at 3–6× its nearest neighbor. The wordmark, the claim, the focal artifact, or the stat — pick one and let everything else be quiet.
- **Silence test** — sparse archetypes (identity, oversized-claim, focal-artifact, closer) read 55–75% empty. **Named density exception:** the *Agent Ledger* plate, which is intentionally tight because density is its content.
- **Restraint test** — the brand's scarce element is the **italic serif word in an accent pill**. It fires **once per frame**. If two accent pills appear at full strength, demote one to a mono chip.
- **Reference bar** — aim at a Comme des Garçons zine cover, an *Apartamento* spread, an *Are.na* annual; failure looks like a Notion landing page or a beige feature grid.

## Colors

Tokens are unchanged from `design.md`. At frame scale they behave as **full-frame grounds + a rationed accent**.

- **Grounds** (full-bleed, never as small swatches): `{colors.od-bg}` cream is the default frame ground; `{colors.od-bg-deep}` is the embedded stage / quiet alt; `{colors.od-surface}` paper is reserved for cards, pills, and lifted surfaces *on top of* a cream frame; `{colors.od-fg}` ink is the inverse-frame ground used for ribbon breaks, dark theaters, and closers.
- **Ink** `{colors.od-fg}` carries every outline (1.5px on chrome scale → 0.18–0.22cqw at frame scale) and every shadow. There is no gray panel and no soft blur on a Vibe Life frame.
- **Accents fire once.** `{colors.od-accent}` peach is the friendly editorial voltage. `{colors.od-agent-voice}` butter is selection / voice / active. `{colors.od-agent-text}` moss is calm-ready / text agent. `{colors.od-agent-video}` sky is video/avatar counterweight. `{colors.od-agent-edit}` plum is HyperFrames edit. **Only one accent at full strength per frame.** A second accent appears only as a tiny dot inside a mono chip.
- **No invented hues.** If a frame needs a tone the palette doesn't carry, the frame is wrong — restructure it.

## Typography

Two ramps, three voices, one italic word.

The **reading ramp** (`{typography.body}`, `{typography.body-lead}`, `{typography.card-heading}`, `{typography.workspace-heading}`, `{typography.mono-label-readable}`) carries any line of running text or load-bearing mono. **Legibility floor: 1.4cqw (≈27px@1920).** Anything below that is colophon-only: timestamps, the leading bauble label, the corner index. A load-bearing mono line uses `{typography.mono-label-readable}`, not `{typography.mono-label}`.

The **display / hero ramp** is frame-native: `{typography.wordmark-mega}` (30cqw, identity cover only), `{typography.display-hero}` (14cqw, ≤3 words), `{typography.display-claim}` (9cqw, 4–6 words), `{typography.display-claim-long}` (6.2cqw, 7+ words). **Fit-to-measure:** the headline text block is capped at **≤78cqw wide** and stepped by word count — short lines go big, long lines step down. A fixed hero size on a long line blows out the edge and reads as a deck.

**The italic word.** Instrument Serif italic appears on exactly one word per frame, in `{typography.serif-accent-hero}` or `{typography.serif-accent-claim}`, often nested inside a `{components.highlight-peach-pill}` or `{components.highlight-butter-pill}`. It is the human in the headline. Never use italic on the display sans; never use the serif for body, labels, or more than one word.

## Layout — The Frame

The frame is **1920×1080** primary (16:9, landscape), plus **1080×1920** (9:16, vertical) and **1080×1080** (1:1, square) variants. Safe area is `{spacing.frame-pad}` (5cqw) on the long edge and `{spacing.frame-pad-short}` (5.5cqh) on the short edge — no load-bearing element crosses it. No element touches the edge except a deliberate full-bleed ground or a ribbon.

The **vw law restated for frames:** every display size, gap, padding, and structural offset is authored in `cqw` against the 1920-wide frame. Conversion: `px ÷ 1920 × 100 = cqw`. Only chrome atoms (border thickness expressed as px in source, button radius, micro shadow) stay in px. **In the showcase, frames render with `container-type: size` and internal sizing in `cqw`** — never raw `vw`, which would resolve against the viewport and force every frame full-bleed. Treat `cqw` and `vw` as equivalent expressions: same numeric value, different container.

## Elevation & Depth

The depth ceiling is **one flat 2–3px ink shadow** (`0 0.4–0.6cqw 0 {colors.od-fg}`) on a lifted surface. That is the brand's signature gravity — *sticker shadow*, not card blur. Soft blur is reserved for dimensional content previews (an avatar scene mock, a gradient preview stage) and never for chrome. The ledger plate uses a single shadow on its outer card; inner cells are flat. The dark theater has no shadow — its inverse ground is its depth.

## Shapes

Radius at frame scale follows `{rounded}` unchanged: **pills 999px** (chips, buttons, nav, the highlight pill), **small 14px** (ledger cells), **card 22px / module 24px** (agent cards, paper cards), **stage 32px** (the hero stage and the dark theater), **band 48px** (large CTA bands). The corner radius is read at frame scale; do not scale it up arbitrarily. Pills are the brand's signature — every CTA, every chip, every active nav state lives inside one.

## Components

The frontmatter `components:` block is the normative source. Each entry below is intent + reference + non-token construction. **Resolved values live only in the frontmatter.**

- **Pill chrome** — `{components.pill-nav-giant}`, `{components.pill-nav-giant-active}`, and the family `{components.chip-mono-giant}` / `{components.chip-peach-giant}` / `{components.chip-butter-giant}` / `{components.chip-moss-giant}` carry the nav and the metadata. Active state is **inked fill, cream text** — `pill-nav-giant-active`. A long mono label may wrap inside the capsule; it does not overflow.
- **Highlight pill** — `{components.highlight-peach-pill}` and `{components.highlight-butter-pill}` are the **container for the italic serif word** inside a display headline. The pill sits **inline** with the surrounding display sans, baseline-aligned, padding tuned so the cap-height fills the pill. Use one per frame.
- **Primary CTA** — `{components.button-primary-giant}` is inked pill with cream mono label. A leading bauble (a small cream circle inside the pill) appears when useful; it is the only decoration the button carries.
- **Cards** — `{components.card-frame}` (paper) and `{components.card-cream-deep-frame}` (embedded well) are the two everyday lifted surfaces. Both carry the ink outline + flat shadow. **Construction note (non-token):** rotation. A card may be rotated −1° to +2° to read as hand-placed; rotation is per-instance and lives in the treatment.
- **Agent card** — `{components.agent-card}` is the role-state-artifact-action card. The role accent (moss / butter / sky / plum) appears as a thin left-edge ink-bordered strip OR a single chip in the header — never as the card fill. State is a `{components.chip-mono-giant}` with a `{components.state-dot}` filled in the accent.
- **Ledger cell** — `{components.ledger-cell}` is the dense-exception unit. Cells tile in a grid with `{spacing.compact-row-gap}` between rows. A cell carries one numeral (`{typography.stat-ledger}`) and one mono label (`{typography.mono-label-readable}`).
- **Ribbon band** — `{components.ribbon-band}` is the full-bleed ink rhythm break. Text inside is `{typography.ribbon-marquee}` in cream, uppercase, slightly tracked.
- **Stage hero** — `{components.stage-hero}` is the large rounded cream-deep stage for a focal artifact (avatar scene mock, gradient preview, draft package). Internal composition (waveform bars, scene frame, timeline) is non-token — treatment-specific.
- **Dark theater** — `{components.dark-theater}` is the inverse-frame counterweight: live generation console, output preview, closer. Display type on the theater is cream, italic serif is butter or peach.
- **State dot** — `{components.state-dot}` is a 1.0cqw inked circle filled in the agent accent; it sits inside a mono chip and never alone.

## Motion & Timing

Motion derives from the brand: **calm but alive, never anxious.** Cut grammar = **paper cuts** — a clean 80–120ms swap between frames, never a fade. Section transitions may use a **ribbon wipe** (the ink ribbon translates across the frame at 600–900ms, `cubic-bezier(0.23, 1, 0.32, 1)`) — punctuation, not chrome default. Within a frame, the only things that may move are **the live-state dot pulse** (1.6s gentle ambient) and **a mono marquee on the ribbon band** (slow, 30–40s, never on a non-ribbon frame). Display type does not animate — no kerning-in, no character reveal, no parallax. Dwell: identity covers 1.5–2.0s, claims 2.5–4.0s, focal-artifact 3.5–5.0s, ledger 4.0–6.0s (it has more to read), closer 1.5–2.5s. Export at the frame's native ratio; never letterbox.

## Frame Treatments

### 1 · Identity Cover  (identity · move: oversized centered wordmark with one italic-serif word in a peach pill)
**Ground** `{colors.od-bg}` cream, padding: `{spacing.frame-pad}`.
**Container** flex column, centered both axes, gap: `2cqw`.
**Composes** `{components.highlight-peach-pill}`, `{components.chip-mono-giant}`
**Focal** wordmark in `{typography.wordmark-mega}` — single word "Vibe", centered, with the italic-serif word "life" in `{typography.serif-accent-hero}` sitting inside a `{components.highlight-peach-pill}` baseline-aligned to the right of the wordmark. Pair fits within ≤78cqw.
**Chrome** a single `{components.chip-mono-giant}` at top-center, label = brand tagline (e.g. — TAGLINE —).
**Accent** the one peach pill on the italic word.
**Silence** ~62% empty; cream paper breathes around the wordmark.
**Fixed** the peach pill carries the italic word; the wordmark is centered; one chip only.  **Free** the wordmark text; the chip text.
**Density** sparse.

### 2 · Oversized Claim  (editorial / oversized-claim · move: centered display headline, one italic word in butter pill, no other elements)
**Ground** `{colors.od-bg}` cream, padding: `{spacing.frame-pad}`.
**Container** flex column, centered, single text block.
**Composes** `{components.highlight-butter-pill}`
**Focal** a 3–6 word claim in `{typography.display-hero}` (or `{typography.display-claim}` if 4–6 words), centered, with one word in `{typography.serif-accent-hero}` inside a `{components.highlight-butter-pill}` inline. Text block ≤78cqw.
**Chrome** none. No kicker. No chip.
**Accent** the single butter pill.
**Silence** ~70% empty.
**Fixed** centered anchor; one italic word; one pill.  **Free** the claim text; which word is italicized; pill color may swap to peach if the prior frame was butter.
**Density** sparse.

### 3 · Focal Artifact — Draft Package on Stage  (focal-artifact · move: a single lifted artifact on a cream-deep stage, ink outline, flat shadow)
**Ground** `{colors.od-bg}` cream, padding: `{spacing.frame-pad}`.
**Container** flex column, centered. Stage at 70cqw wide, 64cqh tall, centered with `2.4cqw` headroom for a kicker chip above.
**Composes** `{components.stage-hero}`, `{components.card-frame}`, `{components.chip-mono-giant}`, `{components.chip-peach-giant}`
**Focal** a `{components.card-frame}` sitting on a `{components.stage-hero}`, rotated −1°, holding the artifact: title in `{typography.card-heading}`, three lines of `{typography.body}`, a `{components.chip-peach-giant}` footer with the next action.
**Chrome** one `{components.chip-mono-giant}` above the stage (e.g. — STATE LABEL —).
**Accent** the peach action chip on the artifact card.
**Silence** ~58% empty (stage carries weight; frame still breathes).
**Fixed** stage on cream; one artifact; one rotation; one accent chip.  **Free** artifact title and body; the action label.
**Density** standard.

### 4 · Agent Ledger  (data/ledger · move: dense grid of agent cells, the named density exception)
**Ground** `{colors.od-bg-deep}` cream-deep, padding: `{spacing.frame-pad}`.
**Container** grid 4 columns × 3 rows of `{components.ledger-cell}`, gap `{spacing.compact-row-gap}` (≈0.6cqw). Section head row above, height ≈8cqh, `margin-bottom: 2cqw` so a wrapping head can never collide with the first row.
**Composes** `{components.ledger-cell}`, `{components.chip-mono-giant}`, `{components.state-dot}`
**Focal** the **grid itself** — the only frame where mass-of-cells is the dominant element.
**Chrome** section head in `{typography.section-head}` top-left ("— LEDGER LABEL —"), one `{components.chip-mono-giant}` top-right with the timestamp.
**Accent** state dots inside cells, each filled in its agent accent (moss / butter / sky / plum). The dots are the rationed voltage; no other accent fires.
**Silence** tight by design — the density exception.
**Fixed** 12 cells, 4×3 grid; one dot per cell; flat ink outline.  **Free** cell numerals, cell labels, which dots are which color.
**Density** dense-exception.

### 5 · Ribbon Break  (chrome/catalog · move: full-bleed ink ribbon as editorial rhythm break)
**Ground** split: top 24cqh `{colors.od-bg}` cream, ribbon 38cqh `{components.ribbon-band}` full-bleed center, bottom 38cqh `{colors.od-bg-deep}` cream-deep. Padding `{spacing.frame-pad}` on cream zones only; ribbon is edge-to-edge.
**Container** absolute three-stripe layout.
**Composes** `{components.ribbon-band}`, `{components.chip-mono-giant}`
**Focal** the ribbon itself, with `{typography.ribbon-marquee}` cream uppercase text centered — a single phrase, no marquee in static; e.g. — RIBBON PHRASE —.
**Chrome** a single `{components.chip-mono-giant}` in the top cream stripe (left), and a `{typography.mono-label-readable}` line in the bottom stripe (right). No other elements.
**Accent** none — the ink ground is the voltage.
**Silence** ~55% empty across the cream zones.
**Fixed** three stripes, ribbon at full bleed; cream copy is centered to the ribbon.  **Free** ribbon phrase; chip text; bottom label.
**Density** sparse.

### 6 · Live Console  (brand-signature / focal-artifact · move: inverse dark theater with one butter selection row, the brand's signature move)
**Ground** `{colors.od-bg}` cream, padding: `{spacing.frame-pad}`.
**Container** centered `{components.dark-theater}` 80cqw × 72cqh, inset on the cream frame so 5cqw of cream shows on every side.
**Composes** `{components.dark-theater}`, `{components.chip-butter-giant}`, `{components.state-dot}`, `{components.chip-mono-giant}`
**Focal** a single butter-filled selection row inside the theater — full theater-width, `8cqh` tall, `{rounded.pill}`, with `{typography.mono-label-readable}` ink text inside and a `{components.state-dot}` filled butter on the left. Section title above the row in `{typography.section-head}` cream.
**Chrome** three small mono labels in cream below the row, `{spacing.chip-gap}` apart, as a quiet list. A `{components.chip-mono-giant}` top-right corner of the theater for state.
**Accent** the one butter selection row — the brand's "selected row" signature.
**Silence** ~60% empty inside the theater; cream margin frames it.
**Fixed** dark theater centered; one butter selection row; no decorative glow.  **Free** the row label; the title; the cream sub-labels.
**Density** standard.

### 7 · Stat Closer  (closer · move: one huge numeral, one mono label, one italic serif word, dark ground)
**Ground** `{colors.od-fg}` ink, padding: `{spacing.frame-pad}`.
**Container** flex column, centered.
**Composes** `{components.chip-butter-giant}`
**Focal** a stat numeral in `{typography.stat-numeral}`, cream color, centered. Below it, a single italic word in `{typography.serif-accent-claim}` butter, centered.
**Chrome** one mono label above the numeral, cream, in `{typography.mono-label-readable}` — the unit or context.
**Accent** the butter italic word — the only color on the frame.
**Silence** ~72% empty.
**Fixed** centered stack: label, numeral, italic word; dark ground.  **Free** the numeral (from the script), the unit, the italic word.
**Density** sparse.
**Construction note** on the dark ground, the mono label and stat numeral are rendered cream-on-ink (it's a label, not a chip). For a true chip on this frame, use `{components.chip-butter-giant}` (butter chip reads on dark) sparingly — never a paper chip.

## Do's and Don'ts

**Do**

- Center the wordmark, the claim, the focal artifact, the closer. Center is the Vibe Life anchor.
- Use **one** italic serif word per frame, inside one accent pill.
- Keep the ink line and the flat hard shadow on every lifted surface.
- Let the cream paper breathe. Sparse frames read 55–75% empty by design.
- Vary the composition axis — don't run the same anchor more than twice in a row. Use the ledger or the ribbon to break a run.
- Express gravity through ink outline + flat shadow, not blur.

**Don't**

- Don't italicize the display sans. The italic must come from Instrument Serif.
- Don't fire two accent pills at full strength on the same frame. Demote one to a chip or a dot.
- Don't park a kicker chip in the top-left of every frame — that is the deck reflex. The chip is rationed.
- Don't render a treatment as a website nav + hero + features layout. The frame is a plate, not a page.
- Don't use soft blur on chrome. Blur is reserved for dimensional artifact previews only.
- Don't introduce a hue, weight, or radius the source does not define.
- Don't fabricate metrics, follower counts, or completion percentages — the numeral on the Stat Closer comes from the script or is held as `— figure —`.

## Aspect-Ratio Behavior

| Treatment | 16:9 (primary) | 9:16 | 1:1 |
|---|---|---|---|
| 1 · Identity Cover | wordmark ≈30cqw, italic pill inline right | wordmark steps to 36cqw, italic pill wraps to a second line below, both centered | wordmark 26cqw, italic pill inline right; chip moves above the pair |
| 2 · Oversized Claim | claim in `display-hero` 14cqw, ≤78cqw text block | claim steps to `display-claim` (9cqw) and wraps to 4 lines max; italic pill on its own line | claim in `display-claim`, 3 lines max, centered |
| 3 · Focal Artifact | stage 70cqw × 64cqh, chip above | stage rotates to 80cqw × 50cqh (shorter), chip above; card rotation flattens to 0° to avoid edge clip | stage 78cqw × 60cqh, chip above |
| 4 · Agent Ledger | 4 cols × 3 rows | 2 cols × 6 rows; head row stacks; `compact-row-gap` preserved | 3 cols × 4 rows |
| 5 · Ribbon Break | three-stripe horizontal | ribbon rotates to a vertical mid-band; cream stripes left and right | ribbon centered across midline, cream above + below |
| 6 · Live Console | theater 80cqw × 72cqh inset | theater fills 90cqw × 82cqh; selection row full-width; sub-labels stack | theater 86cqw × 86cqh |
| 7 · Stat Closer | label / numeral / italic stack, centered | numeral steps to `display-hero` (14cqw) so it doesn't blow out vertically | numeral at `stat-numeral`, label above, italic below — unchanged |

In every ratio, no load-bearing line drops below the 1.4cqw floor (re-measured against the long edge of that ratio's container).

## Approved Real Entities & Numerals

Real entities that may appear on a frame, drawn only from `design.md`:

- Product noun: **Vibe Life**.
- Surfaces named in source: Studio, Brand Memory, Agents, Library, Publish.
- Vocabulary: Brand Memory, Raw Idea, Draft Package, Voice Take, Avatar Scene, HyperFrames Cut, Publish Queue, Agent Handoff, Review Pass.
- Agent roles: Text Agent (moss), Voice Agent (butter), Avatar Agent (sky), HyperFrames Editor (plum).
- State labels (source list): Listening, Drafting, Rendering, Reviewing, Ready, Blocked.

**Numerals are never invented.** A numeral on a Stat Closer or in a Ledger cell either comes from the script or is held as `— figure —`. The showcase uses placeholders.

## Pre-Render Self-Audit

Run before any frame is finalized:

- **Squint** — one element dominates at 3–6× its nearest neighbor.
- **Silence** — sparse archetypes read 55–75% empty; Ledger is the only dense exception.
- **Restraint** — exactly one accent pill at full strength; one italic serif word.
- **Weight** — every lifted surface has the 0.18–0.22cqw ink outline + flat shadow; no soft blur on chrome.
- **Depth ceiling** — only one shadow per surface; no layered drop-shadows.
- **Geometry** — pill 999px, radius from the `{rounded}` scale; no improvised corners.
- **Anchor** — center is the default for hero/cover/focal/closer; the run does not repeat the same anchor more than twice; ledger uses a different anchor than the surrounding frames.
- **Element count** — ≤ 2–3 distinct elements per frame (focal + at most a chip + one accent). Ledger is the exception by construction.
- **Floor** — every load-bearing line ≥1.4cqw; mono labels below the floor are chrome only.
- **Fidelity** — every size used references a frontmatter token; no ad-hoc cqw appears in a treatment.
- **No invention** — no hue, weight, radius, font, or numeral outside the source.

## Known Gaps

- `cqw` and `cqh` are documented extensions of the DESIGN.md spec. Consumers store them as strings; renderers interpret them as container-query units against a frame container with `container-type: size`.
- The italic-pill construction (inline-baseline alignment of a `{components.highlight-peach-pill}` against `{typography.wordmark-mega}` or `{typography.display-hero}`) is a non-token construction documented in `## Components` prose — it cannot be fully expressed as a single property token.
- Card rotation (−1° to +2°) is a non-token construction documented per treatment.
- The Aspect-Ratio Behavior re-scales are guidance; treatments may tune a step further in 9:16 if a load-bearing line approaches the floor.
- Motion specs derive from the brand character in `design.md` §8 but are extended for cut-grammar (paper cut, ribbon wipe); these are not in the source.
