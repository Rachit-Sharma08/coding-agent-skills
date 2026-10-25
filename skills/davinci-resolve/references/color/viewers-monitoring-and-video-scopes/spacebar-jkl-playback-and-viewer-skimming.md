# Controlling playback using the spacebar and jkl keys and skimming in the viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](viewer-controls-external-displays-and-zoom.md) / [Next section](safe-area-overlays-in-the-viewer-and-use-gray-background.md)
<a id="source-cinema-viewing-mode"></a> <a id="source-color-page-in-cinema-mode"></a> <a id="source-color-page-in-enhanced-viewer-mode"></a> <a id="source-color-page-in-full-viewer-mode"></a> <a id="source-controlling-playback-using-the-spacebar-and-jkl-keys"></a> <a id="source-enhanced-full-and-cinema-viewing"></a> <a id="source-enhanced-viewing-mode"></a> <a id="source-fast-review-on-the-color-page"></a> <a id="source-full-viewing-mode"></a> <a id="source-navigating-using-timecode"></a> <a id="source-skimming-in-the-viewer"></a> <a id="source-viewer-and-transport-timecode-displays"></a>

### Controlling Playback Using the Spacebar and JKL Keys

Playback can be started and stopped with the spacebar, or you can adopt the JKL keyboard shortcut scheme for driving playback: J runs it backward, K halts it, and L runs it forward. These shortcuts have plenty of further applications. For details, refer to Chapter 35, “Preparing Clips for Editing and Viewer Playback.” under “Using JKL to Control Playback”

### Skimming in the Viewer

Footage can be skimmed in any viewer across the Media, Cut, Edit, Color, and Deliver pages: hold down the C key and drag the pointer back and forth within the viewer.

### Fast Review on the Color Page

The Fast Review playback command (Playback > Fast Review) has now arrived on the Color page. Built to help you scan long runs of clips at speed, choosing it kicks off accelerated playback through the Timeline, with the playback rate scaled to the length of each clip you pass through. Longer clips race by, while shorter ones play nearer to real time.

### Navigating Using Timecode

You can also enter timecode in absolute or relative terms to reposition the playhead in the Color page Viewer. As you type timecode, key in each pair — hour, minute, second, and frame — one after another, using a period to stand in for a pair of zeros and speed entry along. Whatever pair (or period) you type last is always taken as the frame number, and any pairs you skip are assumed to be zero. There's no need to key in colons or semicolons. For details, refer to Chapter 35, “Preparing Clips for Editing and Viewer Playback.” under “Moving the Playhead Using Timecode.”

### Viewer and Transport Timecode Displays

Two timecode displays sit on the Viewer, and each one defaults to a different timecode setting. The upper display, the Header timecode display, defaults to showing the Source timecode. The lower display, the Transport timecode display, defaults to the Record timecode. That bottom display can be switched among four options, much like those in the Data Burn-In palette. To switch a timecode display to another setting: The upper timecode display is a drop-down menu you can set to whatever timecode, frame number, or KeyKode you'd like shown. The lower timecode display can likewise be switched by right‑clicking it and picking the value type to show from the contextual menu that opens. The options are these:

- Timeline Timecode: The timecode that matches the playhead's spot within the overall Timeline.
- Source Timecode: The timecode that matches the playhead's spot relative to the

currently selected clip.

- Timeline Frame: The frame count that matches the playhead's spot within the overall Timeline.
- Source Frame: The frame count that matches the playhead's spot relative to the currently

selected clip.

- KeyKode: The KeyKode number that matches the media's KeyKode track, where one exists.
- Show Timecode at 30 FPS: Presents 24 fps timecode, via 3:2 pulldown, as 29.97 fps timecode.

Has no effect on video playback.

- Copy and Paste Timecode: A pair of commands makes copying and pasting timecode values easy.

Likewise, the upper timecode display can instead be switched to show KeyKode, when it is present, inside the header of a DPX media file.

### Enhanced, Full, and Cinema Viewing

To grow the Viewer, switch on Enhanced Viewing mode via Workspace > Viewer Mode > Enhanced Viewer Mode (Option-F).

### Enhanced Viewing Mode

While in Enhanced Viewing mode, the Viewer behaves just as it does at normal size, but it grows to occupy the full area of screen above the palettes and Keyframe Editor. Press (Option-F) once more to leave Enhanced Viewing mode. This comes in handy when you need a tighter view of the image — to make detailed corrections, study noise patterns up close, perform a delicate color selection, or trace an elaborate PowerCurve.

### Color page in Enhanced Viewer mode

### Full Viewing Mode

While in Full Viewing mode (reached by choosing Workspace > Viewer Mode > Full Page Viewer, by pressing Shift-F, or by Option-clicking the Enhanced Viewing mode button), the Viewer claims still more space by hiding the palette controls, yet leaves the bottom strip of the DaVinci Resolve UI intact — there you still find the transport controls, the Onscreen Control dropdown menu, the timecode readout, and the page buttons. This mode helps when you want a closer look at the image but still need a small set of onscreen controls within reach.

### Color page in Full Viewer mode

### Cinema Viewing Mode

There's also Cinema mode, which gives you full-screen viewing. Reach Cinema mode by choosing Workspace > Viewer Mode > Cinema Mode Viewer (P). Within Cinema mode the menu bar disappears, and the image fills the screen with none of the usual onscreen controls present. Sliding the pointer across the screen exposes a hidden set of onscreen controls — a play button, jog bar, mute button, and exit button (which turns off Cinema mode). You can additionally lay scopes over the image, which proves useful in on-set settings.

### Color page in Cinema mode

Cinema mode serves well for thorough media review during on-set and digital dailies work when you're remote and have no secondary video display.

TIP: Should you want to overlay timecode on the image in Cinema mode for reference, the controls inside the Data Burn-In window (Workspace > Data Burn-In) let you configure whatever information you'd like shown throughout playback.
