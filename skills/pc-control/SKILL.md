---
name: pc-control
description: Control Windows apps on this PC like a human - DaVinci Resolve video editing via its official Python API, CapCut via keyboard automation, and any GUI app via screenshot-see-act-verify loop. USE when the user asks to open or control DaVinci Resolve, CapCut, or any desktop app, wants video editing done on the PC, or says "PC se kar", "app kholo", "DaVinci me edit kar", "CapCut se banao", "screen par karo".
---

# PC Control (Windows)

Tu (agent) ban jaata hai eyes + hands. Loop: **screenshot → dekho → act →
verify**. Har act ke baad naya screenshot. Andha click kabhi nahi.

## Screenshots (aankhein)

```powershell
powershell -File <skill>\scripts\screenshot.ps1 -Out "$env:TEMP\oc-screen.png"
```
Phir `read` tool se wo image dekho — UI state, dialogs, buttons sab
dikhenge. Ek screenshot = ek nazar.

## DaVinci Resolve (preferred — REAL API, GUI hacking nahi)

Resolve ka **official Python scripting API** use karo — reliable, fast,
version-proof. Learning repos: `in03/snapper`,
`jjsawdon/DaVinci-Resolve-Utilities`.

Setup:
- Resolve **installed + running** hona chahiye. Start:
  `Start-Process "Resolve"` (ya Start Menu se "DaVinci Resolve").
- Python path add (ek baar per script):
```python
import sys, os
sys.path.append(os.path.expandvars(
    r"%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules"))
import DaVinciResolveScript as dvr
resolve = dvr.scriptapp("Resolve")
pm = resolve.GetProjectManager()
proj = pm.GetCurrentProject()
mp  = proj.GetMediaPool()
```
- Common ops:
  - `mp.ImportMedia(["C:\\vid\\a.mp4", ...])` → media items
  - `proj.CreateTimelineFromClips("Main", clips)` → timeline
  - `resolve.OpenPage("edit")` / `"cut"` / `"deliver"`
  - Render: `proj.SetRenderSettings({"TargetDir":..., "CustomName":...,
    "SelectAllFrames":True})`; `jid = proj.AddRenderJob()`;
    `proj.StartRendering(jid)`; status `proj.IsRenderingInProgress()`.
- Har call ka **return value check** karo (None/failure = screenshot le
  kar GUI state verify — page sahi hai? dialog to nahi aaya?).

## CapCut (no API — keyboard automation, EXPERIMENTAL)

CapCut ke liye koi official API nahi — sirf shortcut automation chalega:

- Window activate + keys: PowerShell COM se —
  `$ws = New-Object -ComObject WScript.Shell; $ws.AppActivate("<window title>"); Start-Sleep -Milliseconds 300; $ws.SendKeys("^i")`
  (Ctrl = `^`, Alt = `%`, Shift = `+`).
- Uske baad **hamesha** screenshot + verify. Typa hua? Dialog aaya?
- Common: import `^i`, split `b`, delete `del`, play/pause `space`,
  zoom `+/-`.
- Fragile hai: UI version badalta hai to shortcuts badal sakte hain.
  Pehle screenshot se UI confirm, tabhi keys bhejo.

## Rules

1. **Pehle pucho: API hai ya GUI?** API hai to API (DaVinci) — GUI
   automation sirf last resort (CapCut).
2. Ek act = ek step = ek verify. Do steps kabhi blind kabhi nahi.
3. Popups (update prompts, sign-in, toasts) screenshot me dhoondho aur
   pehle close karo — wo sab kuch block karte hain.
4. 3 consecutive verify-fail → ruk jao, screenshot + plain explanation
   do ki kya dikkat hai (overnight mode me best-effort chalte raho —
   AGENTS.md smart-work rule 6).
5. Bade destructive ops (project overwrite/delete) → pehle file copy/
   snapshot; phir bhi daro mat, rule 6 apply hota hai.
6. User ki baki screen activity respect karo — jis window me kaam ho
   usi ko focus karo, minimize/maximize sab mat karo.
