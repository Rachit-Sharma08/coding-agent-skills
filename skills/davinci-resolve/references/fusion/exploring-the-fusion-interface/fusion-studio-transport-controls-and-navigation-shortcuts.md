# Fusion studio transport controls and navigation shortcuts

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](real-time-playback-not-guaranteed-and-frame-increment-options.md) / [Next section](fusion-playback-ram-cache-and-limits.md)
<a id="source-changing-the-time-display-format"></a> <a id="source-frame-increment-options-1"></a> <a id="source-fusion-studio-transport-controls-1"></a> <a id="source-fusion-studio-viewer-quality-and-proxy-options"></a> <a id="source-keyframe-display-in-the-time-ruler"></a> <a id="source-looping-options-1"></a> <a id="source-navigation-shortcuts"></a> <a id="source-range-fields"></a> <a id="source-real-time-playback-not-guaranteed-1"></a> <a id="source-render"></a> <a id="source-the-current-time"></a> <a id="source-the-time-ruler-displaying-keyframe-marks"></a>

### Fusion Studio transport controls

### Navigation Shortcuts

A lot of the usual transport keyboard shortcuts you already know carry over into Fusion, though a handful are unique to what Fusion needs to do. Use any of these to push the playhead along the Time Ruler from the keyboard:

- Spacebar: Switches forward playback on or off.
- JKL: The familiar JKL scheme is supported, with J to play backward, K to stop,

and L to play forward.

- Back Arrow: Steps backward by a single frame.
- Forward Arrow: Steps forward by a single frame.
- Shift-Back Arrow: Moves to the clip’s Global End frame.
- Shift-Forward Arrow: Moves to the clip’s Global Start frame.
- Command-Back Arrow: Jumps to the Render Range In point.
- Command-Forward Arrow: Jumps to the Render Range Out point.

### Real-Time Playback Not Guaranteed

Since so many of the effects you build on the Fusion page lean heavily on the processor, real-time playback at the project’s full frame rate is not assured unless the composition has been cached beforehand. The “Fusion RAM Cache for Playback” section later in this chapter goes into more detail.

### Frame Increment Options

Right-click any of the Step Backward, Play Reverse, Play Forward, or Step Forward buttons to open a dropdown where you can define a frame increment value. Picking a frame number there causes the playhead to advance in sub-frame or multi-frame steps every time you use a keyboard shortcut or press the Step Forward/Backward buttons. Multi-frame steps are handy while rotoscoping. Sub-frame steps help while rotoscoping or when checking interlaced frames one field at a time (0.5 of a frame).

To set the step size the playhead jumps by, right-click either the Step Forward or the Step Backward button.

### Looping Options

Toggle the Loop button to switch playback looping on or off. Right-clicking the button lets you choose which looping behavior applies:

- Playback Loop: The playhead runs to the end of the Time Ruler and then begins again from the start.
- Ping-pong Loop: After the playhead reaches the end of the Time Ruler, playback runs in reverse until it arrives back at the start of the Time Ruler, then keeps bouncing to and fro.

### Range Fields

In Fusion Studio, the four time fields on the left of the transport controls give you a fast way to change the global range and render range.

Global Time Fields sitting on the left-hand side of the transport controls Audio The Audio button acts as a toggle that mutes or restores whatever audio belongs to the clip. Right-clicking it also opens a drop-down where you can pick a WAV file to play alongside the composition and set an offset for its playback.

### Render

Click the Render button among the transport controls to bring up the composition’s Render Settings dialog. That dialog is where you set the render options and start rendering any Saver nodes the composition contains. Shift-click the button to bypass the dialog and use the default render values (full resolution, high quality, motion blur enabled).

### The Current Time

At the right of the transport controls, the Current Time field displays the frame where the playhead sits, which matches the frame visible in the viewer. You may also type time values into it to shift the playhead by a precise amount. While defining ranges or typing frame numbers to reach a specific frame, the entries can include sub-frame fractions. A range might run from –145.6 to 451.75, or the playhead might rest at 115.22. This is especially handy when animating parameters, because keyframes can sit exactly where they need to be instead of on a frame boundary, producing more natural animation. Sub-frame time also lets you employ time remapping nodes, or simply scale keyframes in the Spline view, without losing precision. NOTE: A great many Fusion fields can evaluate math expressions you type in. Typing 2 + 4 into most fields, for instance, enters the value 6.0. Since Feet + Frames treats the + symbol as a separator rather than a math operator, the Current Time field will not properly evaluate math expressions containing the + symbol, even with the display format set to Frames mode.

### Fusion Studio Viewer Quality and Proxy Options

A row of five buttons on the right of the transport controls lets you either switch on high-quality playback and accept slower processing, or step into one of several proxy modes that briefly cut the display quality to keep processing quick while you work. Whatever you choose here, final output always renders at the highest quality.

These five buttons govern viewer quality, motion blur, the proxy options, and how image processing updates are applied.

HiQ While assembling a composition, how fast you can work tends to matter more than how the displayed image looks. The High Quality setting lets you pick between quicker interactivity and final render quality. With High Quality off, demanding, time-consuming steps such as area sampling, anti-aliasing, and interpolation are skipped so the viewer image appears faster. Turning High Quality on forces a full-quality render to the viewer matching exactly what final delivery will output. MB The Motion Blur button is a global control. Switching Motion Blur off briefly suspends motion blur across the entire composition, regardless of which individual nodes have it on. That can sharply speed up viewer renders. Motion blur must already be enabled on the individual nodes before this button does anything. Prx A draft mode for quicker processing while you build your composite. Switching Proxy on cuts the resolution of the images sent to the viewer, trimming render times by processing only one of every x pixels rather than each one. A slider in the General panel of the Fusion Preferences sets x; you open those preferences via the Fusion menu on macOS, or via the File menu under Windows and Linux. Aprx Another draft mode for quicker processing while you build your composite. Switching Auto Proxy on cuts the image resolution only while you click and drag to change a parameter. As soon as you let go, the image jumps back to full resolution. This smooths the adjustment of processor-intensive operations, removing the jerkiness of waiting for every frame to render fully. The auto proxy ratio likewise comes from a slider in the General panel of the Fusion Preferences, opened from the Fusion menu under macOS or from the File menu on Windows and Linux. Selective Updates Last in this right-hand group of five, this button is a three-way toggle controlling when nodes refresh the viewer image. By default, as you work in Fusion, every node needed to show the viewer image is updated. The Selective Update button alters that behavior across previews and final renders. The three options are:

- Update All (All): Makes every node in the current node tree render. This mainly serves to refresh all the thumbnails shown in the Node Editor.
- Selective (Some): Renders only the nodes that contribute directly to the current image. The name reflects that just the selective nodes get rendered. This is the default.
- No Update (None): Halts rendering completely, which helps when you have many edits to make on a composition that renders slowly.

These options also live in the Fusion Preferences General panel.

### Changing the Time Display Format

Out of the box, every time field and marker in Fusion is counted in frames, yet you can switch the time display to SMPTE timecode or Feet + Frames instead. Here is how to switch the time display format: 1 In DaVinci Resolve, pick Fusion > Fusion Settings; within Fusion Studio under macOS, use Fusion Studio > Preferences; and within Fusion Studio under Windows or Linux, use File > Preferences. 2 Once the Fusion settings dialog appears, open the Defaults panel and pick a Timecode option. 3 Open the Frame Format panel. For timecode, select a frame rate and tick the “has fields” checkbox when your project is interlaced. For feet and frames, set the Film Size value so it matches how many frames fit in a foot of film for the format your project uses. 4 Click Save.

### Keyframe Display in the Time Ruler

Select a node that has keyframed parameters and those keyframes show up along the Time Ruler as small white tic marks, so you can move between and edit them without opening the Keyframes Editor or Spline Editor just to see them.

### The Time Ruler displaying keyframe marks

To shift the playhead between keyframes along the Time Ruler:

- Use Option-Left Bracket ([) to skip leftward onto the nearest keyframe.
- Use Option-Right Bracket (]) to skip rightward onto the nearest keyframe.
