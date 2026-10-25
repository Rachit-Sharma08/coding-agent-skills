---
name: artemis-android-control
description: >
  Drive a real Android phone or emulator with natural language using Google's ARTEMIS
  (Apache-2.0): tap, type, swipe, open apps, read the screen, pull Logcat, take screenshots,
  and run repeatable mobile test flows. Use when the task is about an Android app or device —
  "test the app on my phone", "reproduce this bug on the emulator", "install the APK and walk
  through onboarding", "check what crashes after login", "pull logcat", "tap through this flow",
  "Android UI automation", "mobile QA", "appium alternative", or any request that needs
  actions on a device rather than on the desktop. Not for iOS, not for desktop apps, and not
  for web pages that a browser tool can already reach.
metadata:
  opencode/autoinvoke: true
---

# ARTEMIS — Android control

ARTEMIS is Google's open-source Android automation agent (`google/artemis`, Apache-2.0). It
observes the live screen, decides the next action, and performs it over ADB. Three ways to use
it: a web console, a CLI, and an MCP server that lets a coding agent drive the device directly.

**This skill assumes ARTEMIS is installed and a device is attached.** If it is not, do the
setup below first — do not pretend to control a phone that is not there.

## Preconditions (check before promising anything)

```bash
adb devices          # must list a device as "device", not "unauthorized" or empty
python --version     # 3.12+
uv --version         # required by ARTEMIS
ffmpeg -version      # required for recording
```

- **No device listed** → stop and tell the user to plug in the phone, enable Developer options →
  USB debugging, and accept the RSA prompt on the phone. An emulator works too (`emulator -avd <name>`).
- **`unauthorized`** → the prompt on the phone was not accepted, or `adb kill-server` then replug.
- **No API key** → ARTEMIS needs a multimodal model key; the setup wizard asks for it once. Never
  invent one or hardcode a key into a file that gets committed.

## Install

Windows (PowerShell):

```powershell
git clone https://github.com/google/artemis.git
cd artemis
.\start.bat
```

macOS / Linux:

```bash
git clone https://github.com/google/artemis.git && cd artemis
./start.sh
```

The one-click script installs ADB, scrcpy, FFmpeg and the `uv` dependencies, then opens
`http://localhost:8000` with a device wizard, live mirroring and a prompt sandbox. It also offers
to mount the MCP server and the testing rules into detected IDEs.

Run it without the web UI:

```bash
uv run artemis run "Open Settings, find Battery, tell me the current level" --profile flash
```

## Profiles — pick deliberately

| Profile | Speed | Use for |
| --- | --- | --- |
| `--profile flash` | ~3–5 s/step, cheap | Known, deterministic UI paths: open a screen, read a value, tap through a fixed flow |
| `--profile pro` | ~15–40 s/step, plans and verifies each action | Exploratory testing, bug reproduction, 20+ step flows, anything where a wrong tap is expensive |

Start with `flash`. Escalate to `pro` when the flow branches, the UI is custom (Canvas, Compose,
Flutter), or the user wants a report rather than a single action.

## MCP wiring (agent drives the phone)

```bash
uv run artemis mcp --install all      # auto-configures detected IDEs + global rules
uv run artemis mcp --install claude   # rules to ~/.claude/rules/artemis.md
uv run artemis mcp --generate-config codex   # print the snippet instead
```

**OpenCode** (`~/.config/opencode/opencode.json`) — ARTEMIS is not in the auto-detect list, add it
by hand; `command` must point at the project's venv Python:

```json
{
  "mcp": {
    "artemis": {
      "type": "local",
      "command": ["D:\\artemis\\.venv\\Scripts\\python.exe", "-m", "mcp_server"],
      "cwd": "D:\\artemis",
      "environment": { "PYTHONUNBUFFERED": "1", "PYTHONPATH": "D:\\artemis" },
      "enabled": true
    }
  }
}
```

Restart the session, then ask: *"use artemis to open the app and check for a crash dialog after
login"*. Tool names are prefixed `artemis_` (`mobile_run_task`, `mobile_get_device_state`,
`mobile_manage_task`, `mobile_inspect_trace`, `mobile_diagnose`).

## Rules for driving a phone

1. **Look before you tap.** Read the current screen state first; never fire a coordinate tap
   against a screen you have not observed in this step.
2. **Destructive actions need confirmation.** Sending a message, deleting data, uninstalling,
   buying, or accepting permissions: describe the action and ask before doing it.
3. **Never type real credentials** into an app. Use a test account the user provides, and never
   put the password in a committed file or a log line.
4. **Evidence over claims.** When reporting, attach the screenshot path and the relevant Logcat
   lines. "It worked" without a screen capture is not a test result.
5. **Bound the loops.** A flow that repeats the same action three times is stuck — stop, capture
   the screen, and report the blocker instead of burning steps.
6. **One device, one task.** If several devices are attached, pass `--serial` (or the MCP
   `device_serial`) explicitly instead of hoping it picks the right one.
7. **Leave the phone as you found it.** Uninstall test builds and clear app data only if the user
   asked; mention it in the report either way.

## Useful commands

```bash
uv run artemis ui                 # web console (mirroring, queue, replays)
uv run artemis status             # server state
uv run artemis restart            # after config changes
uv run artemis stop
uv run artemis doctor             # ADB / scrcpy / FFmpeg / device checks
uv run artemis helper status      # on-device accessibility helper
uv run artemis helper uninstall    # remove it from the phone
```

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `adb devices` empty | Different cable/port, USB mode = File Transfer, enable USB debugging, accept the prompt |
| `unauthorized` | `adb kill-server`, replug, accept the prompt on the phone |
| Browser console at `:8000` not loading | `uv run artemis status`, then `uv run artemis restart`; check the port is not taken |
| Every action fails at the first step | `uv run artemis doctor` — usually scrcpy or FFmpeg missing from `PATH` |
| Model errors / 401 | API key missing or wrong in `.env`; rerun `uv run artemis init` |
| Custom UI (Flutter/Canvas) not found | Use `--profile pro`; visual locating is the fallback when the accessibility tree is empty |
| First task pauses ~3 s | The on-device helper is installing; `uv run artemis helper install` pre-installs it |

## Do not

- Do not install ARTEMIS on a phone you do not own or have permission to automate.
- Do not run it against a production account with real money, messages or personal data.
- Do not claim a mobile test passed without a screenshot and a Logcat check.
