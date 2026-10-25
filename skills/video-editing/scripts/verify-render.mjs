#!/usr/bin/env node
// verify-render.mjs — render acceptance gate for the video-editing skill.
//
// Asserts a rendered MP4 is a valid creator-grade short:
//   - dimensions are 9:16 (default 1080x1920, override with --width/--height)
//   - video codec is h264, pixel format yuv420p
//   - an audio stream is present
//   - (optional) duration is within tolerance of an expected value
//
// Usage:
//   node verify-render.mjs path/to/video.mp4
//   node verify-render.mjs video.mp4 --duration 12 --tolerance 0.5
//   node verify-render.mjs video.mp4 --width 1080 --height 1920
//
// Exit code 0 = PASS, 1 = FAIL, 2 = usage/ffprobe error.
// Requires `ffprobe` (ffmpeg) on PATH.

import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";

function parseArgs(argv) {
  const opts = { width: 1080, height: 1920, duration: null, tolerance: 0.5 };
  const positional = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--duration") opts.duration = Number(argv[++i]);
    else if (a === "--tolerance") opts.tolerance = Number(argv[++i]);
    else if (a === "--width") opts.width = Number(argv[++i]);
    else if (a === "--height") opts.height = Number(argv[++i]);
    else if (a === "-h" || a === "--help") opts.help = true;
    else positional.push(a);
  }
  opts.file = positional[0];
  return opts;
}

function ffprobe(file) {
  let out;
  try {
    out = execFileSync(
      "ffprobe",
      ["-v", "error", "-print_format", "json", "-show_format", "-show_streams", file],
      { encoding: "utf8" }
    );
  } catch (err) {
    console.error("ffprobe failed — is ffmpeg installed and on PATH?");
    console.error(String(err.stderr || err.message).trim());
    process.exit(2);
  }
  return JSON.parse(out);
}

function main() {
  const opts = parseArgs(process.argv.slice(2));

  if (opts.help || !opts.file) {
    console.log(
      "Usage: node verify-render.mjs <file.mp4> [--duration N] [--tolerance N] [--width N] [--height N]"
    );
    process.exit(opts.help ? 0 : 2);
  }
  if (!existsSync(opts.file)) {
    console.error(`File not found: ${opts.file}`);
    process.exit(2);
  }

  const probe = ffprobe(opts.file);
  const video = (probe.streams || []).find((s) => s.codec_type === "video");
  const audio = (probe.streams || []).find((s) => s.codec_type === "audio");
  const duration = Number(probe.format?.duration ?? video?.duration ?? NaN);

  const checks = [];
  const check = (name, pass, detail) => checks.push({ name, pass, detail });

  if (!video) {
    check("video stream", false, "no video stream found");
  } else {
    check(
      `dimensions ${opts.width}x${opts.height}`,
      video.width === opts.width && video.height === opts.height,
      `${video.width}x${video.height}`
    );
    check("codec h264", video.codec_name === "h264", video.codec_name);
    check("pixel format yuv420p", video.pix_fmt === "yuv420p", video.pix_fmt);
  }

  check("audio stream present", Boolean(audio), audio ? audio.codec_name : "none");

  if (opts.duration != null && !Number.isNaN(opts.duration)) {
    const delta = Math.abs(duration - opts.duration);
    check(
      `duration ~${opts.duration}s (±${opts.tolerance})`,
      delta <= opts.tolerance,
      `${duration.toFixed(2)}s (Δ ${delta.toFixed(2)}s)`
    );
  } else {
    check("duration", Number.isFinite(duration), `${duration.toFixed(2)}s`);
  }

  let allPass = true;
  console.log(`\nverify-render — ${opts.file}\n`);
  for (const c of checks) {
    const mark = c.pass ? "PASS" : "FAIL";
    console.log(`  [${mark}] ${c.name}${c.detail ? ` — ${c.detail}` : ""}`);
    if (!c.pass) allPass = false;
  }
  console.log(`\n${allPass ? "GATE PASS ✓" : "GATE FAIL ✗"}\n`);
  process.exit(allPass ? 0 : 1);
}

main();
