---
# ============================================================================
# FRAME.md — STYLE TEMPLATE
# Copy this folder to styles/<your-style>/ and replace every value below.
# The frontmatter is the normative source of truth; the prose explains intent.
# Sizes are authored in cqw/cqh against the frame (1cqw = 10.8px at 1080 wide).
# ============================================================================

colors:
  # Grounds — full-bleed backgrounds (never small swatches).
  bg: "#ffffff"            # default frame ground
  bg-deep: "#f2f2f2"       # quiet alternate / embedded stage
  surface: "#ffffff"       # cards, pills, lifted surfaces ON a ground
  fg: "#111111"            # ink: every outline + every text default
  muted: "#555555"         # secondary text

  # Accents — fire ONE at full strength per frame; others demote to a dot/chip.
  accent: "#ff7a59"        # primary editorial voltage
  accent-strong: "#e85d3a" # underline / accent-bar variant
  emphasis: "#ffcf5c"      # keyword pop inside bars/pills

typography:
  # --- Reading ramp (load-bearing text; legibility floor ~1.4cqw) ---
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1.45cqw"
    fontWeight: 400
    lineHeight: 1.5
  card-heading:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1.46cqw"
    fontWeight: 600
    lineHeight: 1.05
  mono-label:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "1.4cqw"
    fontWeight: 500
    textTransform: "uppercase"
    letterSpacing: "0.16em"

  # --- Display / hero ramp (frame-native, far larger than web) ---
  wordmark-mega:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "30cqw"        # identity cover, single word
    fontWeight: 700
    lineHeight: 0.84
    letterSpacing: "-1.2cqw"
  display-hero:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "14cqw"        # <=3-word claims
    fontWeight: 600
    lineHeight: 0.92
    letterSpacing: "-0.5cqw"
  display-claim:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "9cqw"         # 4-6 word claims
    fontWeight: 600
    lineHeight: 0.96
  serif-accent-hero:
    fontFamily: "Times New Roman, serif"
    fontStyle: "italic"
    fontSize: "14cqw"        # the ONE accent word, paired with display-hero
    fontWeight: 400
    lineHeight: 0.92
  stat-numeral:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "22cqw"        # focal stat numerals
    fontWeight: 700
    lineHeight: 0.88

rounded:
  pill: "999px"
  small: "14px"
  card: "22px"
  stage: "32px"

spacing:
  frame-pad: "5cqw"          # safe area on the long edge
  frame-pad-short: "5.5cqh"  # safe area on the short edge
  card-pad: "2.4cqw"
  chip-gap: "1.2cqw"

components:
  chip-mono:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.fg}"
    border: "0.16cqw solid {colors.fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "0.9cqw 1.8cqw"
  highlight-pill:
    # The accent word sitting inside a pill, inline with a headline.
    backgroundColor: "{colors.accent}"
    textColor: "{colors.fg}"
    rounded: "{rounded.pill}"
    padding: "0.4cqw 2.2cqw"
  card-frame:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.fg}"
    border: "0.2cqw solid {colors.fg}"
    rounded: "{rounded.stage}"
    padding: "{spacing.card-pad}"
    shadow: "0 0.5cqw 0 {colors.fg}"   # flat hard shadow, not blur
  button-primary:
    backgroundColor: "{colors.fg}"
    textColor: "{colors.bg}"
    border: "0.2cqw solid {colors.fg}"
    rounded: "{rounded.pill}"
    typography: "{typography.mono-label}"
    padding: "1.6cqw 3.2cqw"
    shadow: "0 0.42cqw 0 {colors.fg}"
---

# FRAME.md — <Your Style Name>, at frame scale

> One-line motto for the style. e.g. **Atoms are sacred · composition is free.**

## Overview

Describe the look in 3–5 sentences. What does it read as at a glance? What are the
non-negotiable signatures (the ground, the one accent, the type pairing, the shadow
style)? What is it explicitly *not* (no dark dev-tool chrome, no pastel AI slop, no SaaS
feature grid — whatever your anti-patterns are)?

**Craft bar**

- **Squint test** — one element dominates at 3–6× its nearest neighbor.
- **Silence test** — sparse frames read 55–75% empty (note any dense exception).
- **Restraint test** — name your scarce element (the one that fires once per frame).
- **Reference bar** — what good looks like; what failure looks like.

## Colors

Explain the role of each token group: which are full-bleed **grounds**, which is the
**ink** that carries outlines and shadows, and which **accents** are rationed. State the
rule: only one accent at full strength per frame; no invented hues.

## Typography

Two ramps, and which face is the **accent voice** used on exactly one word per frame.
State the legibility floor (≈1.4cqw / 27px@1920). Load-bearing text uses the reading
ramp; the display ramp is frame-native.

## Layout — The Frame

Default ratio and variants (this skill targets **9:16 / 1080×1920** first; styles may
also define 16:9 and 1:1). Safe area = `{spacing.frame-pad}` / `{spacing.frame-pad-short}`.
Everything is sized in `cqw`/`cqh` against the frame, never `vw`/`vh`.

## Elevation & Depth

Name your depth ceiling — e.g. one flat ink shadow (`0 0.4–0.6cqw 0 {colors.fg}`), no
layered blur on chrome.

## Components

Walk through each component in the frontmatter: intent + when to use. Resolved values live
only in the frontmatter `components:` block.

## Motion & Timing

Calm vs. punchy. Cut grammar (hard paper-cut vs. crossfade), section-transition device,
what may animate inside a frame, and dwell times per archetype. This maps directly to the
edit's easing and cut frequency.

## Do's and Don'ts

**Do** — list the signatures to keep.
**Don't** — list the anti-patterns (the things that make it look generic).

## Aspect-Ratio Behavior

Optional table: how each treatment re-scales across 16:9 / 9:16 / 1:1. In every ratio, no
load-bearing line drops below the 1.4cqw floor.
