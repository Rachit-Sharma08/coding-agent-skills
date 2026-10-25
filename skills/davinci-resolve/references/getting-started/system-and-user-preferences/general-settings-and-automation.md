# General settings and automation

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](text-and-color.md) / [Next section](keyboard-customization-and-emulation-presets.md)
<a id="source-automation"></a> <a id="source-control-panels"></a> <a id="source-display-settings"></a> <a id="source-general-settings-1"></a> <a id="source-keyboard-customization"></a> <a id="source-metadata"></a> <a id="source-panel-sensitivity"></a> <a id="source-playback-settings"></a>

### General Settings

Both preferences in the General Settings section let you shape the Loop Jog behavior, which for now lives only on the Fairlight page. Picking Timeline > Loop Jog makes a short sample preview audible as you scrub the playhead along the Timeline. That can ease the job of catching snippets of dialog or music while you quickly scrub through tracks hunting for particular lines or music cues. It likewise lets that short sample preview loop without end when you park the playhead on a frame, so you can pause mid-scrub and hear (by default) the 80 ms just before the playhead cycling around. Two settings let you tailor how this works.

- Loop Jog Alignment: Three choices decide whether your audio loops Pre the playhead position, Centered on the playhead, or Post the playhead position.
- Loop Jog Width: A field lets you set how many milliseconds of audio loop while Loop Jog is on. How many milliseconds map to a single frame hinges on the video’s frame rate. At 25 fps, for instance, you get 1000/25 = 40 ms per frame, so the 80 ms default works out to two frames of looping.
- Enable auto patching: Tick this box and the first of your system audio inputs routes to whichever track has “arm for record” active.
- Mixer follows selected track: Tick this box and the selected track shows up focused and farthest left in the Mixer pane.
- Include mixer events in Undo history: Tick this box and you’ll be able to undo mixer events (changes to panning or to a track’s mute state, say).

### Automation

The Automation section’s two preferences let you set the Glide Time between Automation events and decide whether Automation events ride along when you recall a preset or copy and paste.

- Glide Time: Type a millisecond value to set the Glide Time used for automation.
- Write on Preset or Clipboard Paste: Tick this box and Automation events get

written to the track as you recall a track preset or copy and paste. Bear in mind that with it on, what actually gets written still depends on which master automation is switched on or off. Disable plugin automation, for example, and no plugin automation will be written.

### Playback Settings

These preferences help you lift realtime performance in DaVinci Resolve by switching off particular UI features and tuning the quality of certain operations.

- Hide UI overlays: If a lone GPU is handling both display and CUDA, OpenCL, or Metal processing, or your display GPU is weak, or you’re short on the PCIe bandwidth the current resolution or frame rate demands, switching this option on may bump up real time performance. With it on, onscreen controls — the cursor, Power Window outlines, split-screen views — are switched off and hidden during playback. Pause playback and every onscreen control comes back.
- Minimize interface updates during playback: With this on, real time performance takes precedence during playback as user-interface updates are pared back. It helps when you’re building elaborate grades on low-powered systems or working on high-resolution projects.
- Performance Mode Automatic/Manual: A set of three radio buttons lets you pick Automatic (the default) or Manual (user-selectable) behavior when you switch Performance Mode on in DaVinci Resolve, or turn Performance Mode Off entirely. Under Automatic, Performance mode tunes a range of operations on its own to weigh speed against the image quality you need, keeping onscreen performance brisk while always holding video output at top quality. Under Manual, three separate settings can be switched off for those moments when a given performance tradeoff Resolve makes brings an unwelcome, obvious drop in image quality within Performance Mode:

Optimized Sizing: Concerns how image resizing gets handled. Optimized Decode Quality: Concerns how clip resolution against timeline resolution gets handled. Optimized Image Processing: Concerns how image processing operations get handled.

### Control Panels

This panel’s parameters let you tailor how the DaVinci Control panels behave.

### Panel Sensitivity

Lets you set where red sits on the trackballs, how responsive the trackballs and rings feel, and how responsive the qualifier knobs feel.

- Classic DaVinci trackball alignment: Switch this checkbox on and every color balance control in DaVinci Resolve takes the long-standing orientation it has always used — near, though not quite identical, to the vectorscope alignment of hues. Switch it off and the color balance controls line up exactly with the vectorscope alignment of hues, much as other color grading apps do. Go with whichever mode you know best.
- Grading style: Sets how the trackballs are oriented against the corrections they produce. Two options exist:

DaVinci: Most people will recognize the standard DaVinci controls, since this echoes the vectorscope (how faithfully depends on the Classic DaVinci trackball alignment setting). Rank: The Rank settings differ a fair bit, so this option suits anyone at home with the color controls the Rank control system offered. Here the orientation of red and green is flipped.

- Lift RGB balance: Governs how fast moves on the Lift trackball (over on the left) drive the Lift Color Balance parameters on the Color page. The setting carries over to third-party panels.
- Lift master: Governs how fast moves on the Lift ring (encircling the leftmost trackball) drive the Lift Contrast parameter on the Color page. The setting carries over to third‑party panels.
- Gamma RGB balance: Governs how fast moves on the Gamma trackball (second in from the left) drive the Gamma Color Balance parameters on the Color page. The setting carries over to third-party panels.
- Gamma master: Governs how fast moves on the Gamma ring (encircling that second trackball from the left) drive the Gamma parameter on the Color page. The setting carries over to third‑party panels.
- Gain RGB balance: Governs how fast moves on the Gain trackball (third in from the left) drive the Gain Color Balance parameters on the Color page. The setting carries over to third-party panels.
- Gain master: Governs how fast moves on the Gain ring (encircling the third trackball from the left) drive the Gain Contrast parameter on the Color page. The setting carries over to third-party panels.
- Cursor offset: Governs how fast moves on the fourth trackball act on the cursor, the window position, the log-mode offset, and the other controls that trackball can drive.
- Cursor master: Governs how fast moves on the fourth ring act on the log-mode master offset and the other controls that ring can drive.
- Hue/Saturation/Luminance qualifier: Governs how responsive the HSL panel’s control knobs are.
- Jog: Governs how responsive the jog wheel is.
- Shuttle: Governs how responsive the shuttle dial is.

### Display Settings

Lets you tune the display on your Blackmagic Design control panels.

- LCD brightness: Governs the overall brightness of the DaVinci control panel displays.
- Key backlighting: According to which control panel you’ve chosen, two controls let you

set LCD Brightness and Key backlighting on the DaVinci Resolve Mini panel, while three controls let you tune the color balance of the lit buttons on the DaVinci Resolve Advanced control panel (its default is red).

### Metadata

Through the metadata panel you can assemble your own sets of metadata parameters that then surface in the Metadata Editor. For more on working with this panel, see Chapter 19, “Using Clip Metadata.”

### Keyboard Customization

Picking DaVinci Resolve > Keyboard Customization brings up the standalone Keyboard Customization window. There you can settle on which set of keyboard shortcuts to run, find out which shortcuts exist, or roll your own custom keyboard mappings that hew closer to how you prefer to work across whatever pages you happen to be in.
