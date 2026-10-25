"""Render assets/thumbnail.png (1280x640) - the GitHub social preview card.

Usage: python scripts/make_thumbnail.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "thumbnail.png"
W, H = 1280, 640

BG = (11, 11, 18)
INK = (244, 244, 245)
MUTED = (161, 161, 170)
DIM = (113, 113, 122)
ACCENT = (99, 102, 241)
AMBER = (245, 158, 11)

FONTS = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = FONTS / name
    if not path.exists():
        return ImageFont.load_default(size=size)
    return ImageFont.truetype(str(path), size)


bold = font("segoeuib.ttf", 96)
bold_sm = font("segoeuib.ttf", 26)
semi = font("seguisb.ttf", 22)
body = font("segoeui.ttf", 24)
mono = font("consola.ttf", 15)
mono_sm = font("consola.ttf", 13)
tiny = font("segoeui.ttf", 16)


def tracked(draw: ImageDraw.ImageDraw, xy, text: str, fnt, fill, spacing=3):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing


def pill(draw, xy, text, fnt, fg, border, pad_x=16, pad_y=9):
    x, y = xy
    w = draw.textlength(text, font=fnt)
    box = (x, y, x + w + pad_x * 2, y + fnt.size + pad_y * 2)
    draw.rounded_rectangle(box, radius=(box[3] - box[1]) // 2, outline=border, width=1)
    draw.text((x + pad_x, y + pad_y - 1), text, font=fnt, fill=fg)
    return box[2] - box[0]


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# Soft ambient glow behind the headline (blurred layer, so no hard edge).
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((60, 60, 700, 700), fill=(79, 70, 229, 120))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(150))).convert("RGB"), (0, 0))
draw = ImageDraw.Draw(img, "RGBA")

# Dot grid.
for gx in range(0, W, 32):
    for gy in range(0, H, 32):
        draw.point((gx, gy), fill=(255, 255, 255, 10))

# Left accent bar.
draw.rectangle((0, 0, 6, H), fill=ACCENT)

M = 76
pill(draw, (M, 74), "OPEN SOURCE  ·  MIT", mono_sm, (199, 210, 254), (79, 70, 229))

draw.text((M - 4, 140), "Agent", font=bold, fill=INK)
draw.text((M - 4, 236), "Skills", font=bold, fill=INK)
draw.rectangle((M, 348, M + 56, 354), fill=AMBER)

draw.text((M, 386), "206 drop-in skills for the agents", font=body, fill=MUTED)
draw.text((M, 418), "you already use.", font=body, fill=MUTED)

agent_box_x = M
for name in ("Claude Code", "OpenCode", "Codex", "Cursor"):
    w = draw.textlength(name, font=mono_sm)
    draw.rounded_rectangle(
        (agent_box_x, 470, agent_box_x + w + 26, 502), radius=6,
        fill=(24, 24, 33), outline=(45, 45, 58),
    )
    draw.text((agent_box_x + 13, 479), name, font=mono_sm, fill=(212, 212, 216))
    agent_box_x += w + 36

draw.line((M, 552, W - M, 552), fill=(39, 39, 51), width=1)
draw.text((M, 578), "github.com/Rachit-Sharma08/coding-agent-skills", font=tiny, fill=DIM)
draw.text((W - M, 578), "SKILL.md  ·  no plugins", font=mono_sm, fill=DIM, anchor="ra")

# Skill chips, two columns on the right.
chips = [
    "ffmpeg-skill", "impeccable", "seo-audit", "docx",
    "stripe-best-practices", "ghidra", "brainstorming", "pdf",
    "supabase", "transcribe", "systematic-debugging", "artemis",
    "ui-ux-pro-max", "semgrep", "pricing", "canvas-design",
]
col_x = [726, 992]
top = 138
row_h = 44
for i, chip in enumerate(chips):
    col, row = i % 2, i // 2
    x, y = col_x[col], top + row * row_h
    w = draw.textlength(chip, font=mono) + 22
    hot = chip in ("ffmpeg-skill", "impeccable", "seo-audit")
    draw.rounded_rectangle(
        (x, y, x + w, y + 30), radius=6,
        fill=(24, 24, 33, 255) if not hot else (30, 27, 60, 255),
        outline=(70, 70, 90, 255) if hot else (38, 38, 50, 255),
    )
    draw.text((x + 11, y + 7), chip, font=mono, fill=(226, 226, 232) if hot else (140, 140, 152))

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, optimize=True)
print(f"{OUT} {img.size} {OUT.stat().st_size // 1024} KB")
