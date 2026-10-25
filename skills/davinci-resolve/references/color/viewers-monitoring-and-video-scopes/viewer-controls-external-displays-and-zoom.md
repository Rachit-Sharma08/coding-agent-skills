# Onscreen controls and external displays and zooming into the viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](add-edit-guide-dialog-and-proxy-handling.md) / [Next section](spacebar-jkl-playback-and-viewer-skimming.md)
<a id="source-navigating-using-the-arrow-keys"></a> <a id="source-onscreen-controls-and-external-displays"></a> <a id="source-using-the-jog-bar-and-transport-controls"></a> <a id="source-viewers-monitoring-and-video-scopes-part-2"></a> <a id="source-zooming-into-the-viewer"></a>

### Onscreen Controls and External Displays

DaVinci Resolve was made to run with calibrated external displays wired to video output interfaces, and for most colorists handling broadcast or theatrical programs, this is the advised way to work when color-critical evaluation matters. For that reason, many onscreen controls tied to jobs like color sampling, window adjustment, and key manipulation get mirrored to your video output, so you can hide the Viewer on your computer's monitor and work off an external display alone. To set whether onscreen controls mirror to video out or stay off: Pick an option from the Window Outline submenu within the Viewer's option menu. The three options are:

- Off: Drops the window outline from both the external display and the Viewer.
- On: The default; keeps the window outline on both the external display and the Viewer.
- Only UI: Drops the window outline from your external display while keeping it in the Viewer.

To show clip flags on video output: Tick the "Show clip flags on video output" checkbox option within the Color page Viewer's option menu. Doing so paints one or more small colored flag overlays into the bottom-left corner of the video output. That keeps the flagged clips visible at all times on your grading hero display while you work, should that aid you in tracking whatever the flags are helping you stay on top of. By default it stays off. Limitations When Grading With the Viewer on a Computer Display Few computer displays can meet the color-critical tolerances or specs that quality control insists on for streaming, broadcast, or theatrical delivery. A further wrinkle is that, depending on the mix of workstation and computer display, the Viewer may not render each clip's image data the same way the calibration your operating system applies to your computer display renders it, varying with which OS you run DaVinci Resolve on. That can leave your computer display unfit, in its default state, for monitoring projects bound for the web's sRGB standard. For instance, grade a project on your computer display using the Color page Viewer and the resulting clip might not look identical in the QuickTime player or in other post-production applications.

You can address this in one of two ways:

- When running DaVinci Resolve on macOS, you can switch on "Use Mac Display Color Profile for viewers" within the Hardware Configuration panel of the System Settings. That lets DaVinci Resolve adopt whatever color profile you set under the macOS System Preferences, via the Displays panel's Color tab, leaning on ColorSync on macOS so DaVinci Resolve renders color the same way your computer monitor does. It now covers every color profile bundled with macOS, plus color profiles produced by calibration software like that from X-rite, Datacolor, or other applications. Where the computer supports it, an "Use 10-bit precision in viewers" option may also be available for you to switch on. Turn that on and the rendered output shown in QuickTime Player lines up with what the DaVinci Resolve Viewer shows.
- Failing that, you can put a dedicated Color Viewer LUT to work for calibration through the 1D/3D Color Viewer Lookup Table drop-down menu sitting in the Color Management panel of the Project Settings. This has you profiling your computer display for calibration just as you would an external display, with a probe plus color management software, then loading the resulting calibration LUT into DaVinci Resolve. Bear in mind that calibrating a monitor can only bring a high-quality display into standards compliance; it can't compensate for a display gamut that runs too small.

For more, head to the "Lookup Tables" section, see Chapter 4, "System and User Preferences." Put bluntly, if professional work is the goal, your grading belongs on some kind of calibrated external broadcast display, class A and 10- or 12-bit, hooked up through a Blackmagic Design video interface. Provided everything runs as it should, an image sent to video out of DaVinci Resolve ought to match one sent to video out of whatever other post-production application you use, and that should serve as your baseline when weighing the output of two different applications.

### Zooming into the Viewer

While using the Viewer to sample tricky colors or trace a detailed PowerCurve, zooming into the image can pay off. To zoom in or out of the Viewer, do one of the following:

- Bring the pointer inside the Viewer, then spin the scroll wheel to zoom the image in or out.
- Press Command-Equal to zoom in, or Command-Minus to zoom out.

To pan around the Viewer:

- Bring the pointer inside the Viewer, then middle-click and drag to pan the image around.

To reset the size of the Viewer image:

- Pick 100% (Actual Size) (Option-Shift-Z) off the sizing drop-down menu at the Viewer's upper left.
- Choose View > Zoom > Zoom to Fit (Shift-Z).

To enable or disable image zoom being sent to video out:

- Pick "Gang viewer zoom with video output" from the Viewer's option menu so the image on video out zooms to exactly match the Viewer's zoom level, letting you judge a zoomed-in slice of the image on your suite's hero display.

### Using the Jog Bar and Transport Controls

Controlling playback ranks among the Viewer's chief jobs. The jog bar, sitting right below the image in the Viewer, carries a playhead you can drag left and right to scrub through the currently selected clip as quickly as you can move the pointer. That jog bar playhead is tied to the playheads in the Timeline and Keyframe Editor. Move one playhead and all three move. How much of the Timeline the jog bar covers depends on whether the Node Editor sits in Clip or Timeline mode. Under Clip mode, the jog bar's width equals however long the currently selected clip runs. Under Timeline mode, its width equals the whole Timeline's combined duration. Below the jog bar, a row of transport controls hands you finer control over timeline playback.

- Previous clip: Jumps the playhead onto the first frame of the clip before this one.
- Reverse: Initiates 100% playback in reverse.
- Stop: Stops playback.
- Play: Initiates 100% playback.
- Next clip: Jumps the playhead onto the first frame of the clip after this one.
- Loop: Confines playback to the current clip, wrapping back to the first frame when you're playing

forward to a clip's end, or wrapping to the last frame when you're playing in reverse toward a clip's start. Two further buttons hand you control over audio playback and clip display within the Viewer:

- Unmix: Switching Unmix on disables every transition, composited superimposition, and effect that blends two or more clips at once. With Unmix, you can size up a clip's look free of distraction any time an adjustment hinges on how the clip reads on its own, or any time changes depend on frames that a transition like a dissolve or a fade from black would otherwise bury. Once you want to view your grades alongside transitions and composites again, switch Unmix off.
- Mute: Click the speaker icon to switch audio playback on or off, or right-click the speaker icon and drag the slider to set the level.

### Navigating Using the Arrow Keys

The keyboard's Arrow Keys let you move through clips and the Timeline in a few different ways.

- Up/Down Arrow: Jumps the playhead onto the first frame of the clip before or after it.
- Left/Right Arrow: Steps the playhead one frame backward or forward each press.
- Shift-Left/Right Arrow: Steps the playhead one second backward or forward each press.
