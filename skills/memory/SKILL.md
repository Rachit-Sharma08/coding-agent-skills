---
name: memory
description: Persistent memory across sessions - global and per-project. USE whenever the user says "yaad rakh", "remember this", "note kar le", "save this", "tumhe yaad hai?", or asks you not to explain something twice again. Also use at the START of any new conversation in a project that has a memory file, and whenever a durable fact emerges (user preferences, corrections, project decisions, environment facts, workflow habits). Never store secrets/passwords/API keys - only WHERE secrets live.
---

# Memory

Har session fresh hota hai — is skill ka kaam usko permanent memory
dene ka hai. Do files hain:

1. **Global**: `~/.config/opencode/memory.md` — user-level facts jo HAR
   project me apply hote hain (pasand, workflow, PC facts).
2. **Project**: `<project>/.opencode/memory.md` — sirf us project ke facts.

## Read (kab padho)

- Naya conversation shuru hua aur memory file exist karti hai → pehle
  turn me padh lo (ya jab task purane context maangta hai).
- User bole "yaad hai kya / remember" → seedha wo fact dhundho.

## Write (kab aur kaise)

Jab bhi durable fact aaye, usi turn me append/update karo:

- User preference ya correction ("aise mat kar, mujhe wo acha lagta hai")
- Project decision ("auth Firebase use karta hai", "deploy Vercel par")
- Environment fact ("ffmpeg installed hai", "D: drive par space hai")
- Repeat hone wali instruction (jo baar baar samjhani pad rahi hai)

Format — dated bullet, latest wins, dedupe:

```markdown
## Global memory (user-level)
- 2026-10-21: User Hinglish me baat karta hai; raat ko autonomous
  overnight runs chalta hai; free-only models; no GPU PC.

## Project memory
- 2026-10-21: Stack = Node + Postgres. Auth = custom JWT. Deploy = Vercel.
```

Rules:

- **Secrets kabhi mat likho** (keys/passwords/tokens) — sirf location
  likho: "API key `.env` me hai".
- Dedupe: purana same-matlab bullet delete ya update karo; date update.
- Cap: ~100 lines per file. Usse upar ho to stale/irrelevant prune karo.
- Project file me sirf us project ki baat; user-level cheezein global me.
- Project file git me na jaaye — pehli baar banate waqt `.gitignore` me
  `.opencode/memory.md` add karo (agar git repo hai).
