---
name: ai-video-maker
description: Build complete YouTube videos (Shorts se 10-min long-form tak) fully in-code - NO Gemini/external AI video tools needed. Agent writes script and storyboard itself, Edge TTS gives free neural voiceover (Hindi/English), Pexels stock or ffmpeg-generated graphics make top-notch visuals, ffmpeg assembles 1080p video, then agent QC-checks frames visually and audio loudness before delivering. USE whenever the user says "video banao", "youtube video", "channel ke liye video", "voiceover/narration banao", "shorts/reels banao", or shares any video topic/idea.
---

# AI Video Maker (agent-driven, free, no GPU)

Tu hi poora video banata hai: topic → script → voice → visuals → final
MP4 + thumbnail + subtitles. Architecture same hai jaise proven open
pipelines (`its-rath/AI_Video_Generation_Pipeline`, stickman video
pipelines): **TTS + stock + ffmpeg**. Farq: script/storyboard **tu**
likhta hai (koi Gemini nahi), aur **tu hi visually QC** karta hai.

## Pipeline (har video me ye order)

1. **Concept → Script**: title, hook (pehle 5 second me), scene-by-scene
   narration (~150 words/min — 5-min video ≈ 750 words Hindi/English),
   scene table: `# | seconds | visual description | on-screen text`.

2. **Voiceover** (free — `pip install edge-tts`, ek baar):
```powershell
edge-tts --voice hi-IN-SwaraNeural --file script.txt --write-media voice.mp3 --write-subtitles voice.srt --rate=+5%
```
   Voices: `hi-IN-SwaraNeural`, `hi-IN-NeerjaNeural`,
   `en-US-GuyNeural`, `en-US-AriaNeural`.

3. **Assets**:
   - `PEXELS_API_KEY` env var set hai → stock photos/videos:
     `https://api.pexels.com/v1/search?query=<topic>&per_page=15`
     (header: `Authorization: <key>`). Free signup.
   - Key nahi hai → **zero-key mode**: ffmpeg se gradient/solid cards +
     bold drawtext typography (YouTube explainer style isi se banta hai).

4. **Assemble (ffmpeg)** — per scene:
   - Ken Burns on images:
     `scale=3840:-2,zoompan=z='min(zoom+0.0008,1.12)':d=<FPS*sec>:s=1920x1080:fps=30`
   - Titles: `drawtext=fontfile=C\:/Windows/Fonts/segoeuib.ttf:text='...':fontsize=68:...`
   - Har scene ka clip banao → concat demuxer se jodo → voice track +
     optional BGM (`amix`, aur `sidechaincompress` se BGM voice ke
     neeche duck).
   - Encode: `-c:v libx264 -preset veryfast -pix_fmt yuv420p -c:a aac -b:a 192k`
   - Audio final: `loudnorm=I=-14:TP=-1.5:LRA=11` (YouTube standard).

5. **QC — mandatory (user ko "check bhi karo" chahiye)**:
   - `ffprobe`: duration target ±10%, `1920x1080`, `30 fps`, audio
     stream present.
   - 8–12 frames alag timestamps se nikalo aur `read` se **khud dekho**:
     text legible? black frame? crop sahi? watermark? alignment?
   - Audio: `volumedetect` (mean -20..-10 dB sane) + `silencedetect`
     (narration ke beech lambi khamoshi to nahi).
   - Koi fail → sirf wahi scene fix + re-render, poora mat banado.

6. **Deliver**: `video.mp4`, `thumbnail.png` (best frame + title text),
   `voice.srt`, transcript.md, YouTube metadata (title/description/
   tags/hashtags).

## Style rules (top-notch graphics ke liye)

- Typography badi aur clean (1080p par ≥64px), ek font family per
  video, high-contrast text (dark bg + light text).
- Har scene = ek idea; 3–6 sec per visual (boredom nahi).
- Palette: dark background + 1 accent color. Neon/gradient overuse
  marka "AI-generated" lagta hai — bacho.
- BGM hamesha voice se −15 dB+ neeche (ducking), lo-fi/ambient best.
- Hook me text overlay chhota + narration fast; end me 3-sec CTA card.

## Reality notes (honest)

- PC par GPU nahi → render slow-ish: 5-min video ≈ 4–10 min (veryfast
  preset). Bade projects per-scene chunk me banao.
- Stock ke liye `PEXELS_API_KEY` free signup chahiye; warna zero-key
  mode (gradient cards) — usse bhi achhi explainer banti hai.
- Advanced motion graphics ya hand-drawn style chahiye → `pc-control`
  skill se DaVinci Resolve (Python API) par handoff kar sakte ho.

## Related installed skills (hidden; load by exact name)

- **AI video generation / avatars:** `runway-dev`, `runway-dev-models`, `runcomfy-cli`, `ai-video-generation`, `image-to-video`, `lipsync`.
- **Programmatic / motion graphics:** `remotion-best-practices`, `remotion-create`, `remotion-render`, `hyperframes`, `video-use`, `manim-video`.
- **Voice / audio:** `elevenlabs-text-to-speech`, `elevenlabs-music`, `elevenlabs-sound-effects`, `deepgram-speech-to-text`, `deepgram-text-to-speech`.
- **Editing / finishing:** `ffmpeg-skill`, `video-editing`, `davinci-resolve`, `pc-control`.
- **Existing video analysis:** `video-frames`.
- Default free pipeline yahi `ai-video-maker` hai; paid/API skills tab use karo jab user bole ya key de.
