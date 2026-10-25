# Visual Styles

A **style** is a selectable design-token pack for rendered frames and HyperFrames
compositions. It decides how every video built with this skill *looks* — colors, type,
spacing, components, and motion personality — without touching the editing logic.

The editor reads the active style's `FRAME.md` and themes the whole edit from it.
**Different style → different look, same craft.**

## Picking a style

Reference a style by its folder name:

```text
styles/<name>/FRAME.md
```

The per-style token file is always named `FRAME.md`. If no style is named, the editor
defaults to `vibe-life`.

## Available styles

| Style        | Path                          | Use                                            |
|--------------|-------------------------------|------------------------------------------------|
| `vibe-life`  | `styles/vibe-life/FRAME.md`   | Worked example: warm editorial — cream paper, ink outline, one italic-serif accent word, peach/butter accents. |
| `_template`  | `styles/_template/FRAME.md`   | Starting point for your own style — copy it and fill in your tokens. |

## Add your own style

1. **Copy the template:**
   ```sh
   cp -r styles/_template styles/my-style
   ```
2. **Edit `styles/my-style/FRAME.md`** — fill in the `colors`, `typography`, `rounded`,
   `spacing`, and `components` frontmatter, then write the prose sections describing your
   look (overview, do's/don'ts, motion). The frontmatter is the normative source; the
   prose explains intent.
3. **(Optional) add a showcase** — an `frame-showcase.html` that renders your treatments
   so you can eyeball the system before editing. The `vibe-life` folder has one to copy.
4. **Use it:** tell the editor to theme from `styles/my-style/FRAME.md`.

### What a good `FRAME.md` defines

- **Colors** — full-frame grounds + a small set of rationed accents (don't invent hues
  mid-edit; if a frame needs a tone the palette lacks, the frame is wrong).
- **Typography** — a reading ramp (body, labels) and a display/hero ramp (wordmark,
  claims), plus which face is the "accent" voice. Use local `@font-face` woff2 subsets at
  render time, never a CDN.
- **Rounded / spacing** — the radius scale and safe-area padding, sized in `cqw`/`cqh`.
- **Components** — the atoms (pills, chips, cards, bars) with resolved token values.
- **Motion personality** — calm vs. punchy; this maps to cut grammar and easing in the
  edit (see the skill's "style-theming" and "camera-moves" references).

Keep the same token *roles* across styles (ground, accent-strong, emphasis, ink) so the
editorial-look patterns map cleanly onto any style.
