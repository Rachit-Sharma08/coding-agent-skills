# A power window tracking a womans face and simple tracking using the tracker menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Motion tracking windows.
[Chapter index](INDEX.md) / [Next section](tracker-type-pop-up-and-object-tracking.md)
<a id="source-a-power-window-tracking-a-womans-face"></a> <a id="source-controls-in-the-window-tracker-palette"></a> <a id="source-copying-and-pasting-tracking"></a> <a id="source-motion-tracking-windows"></a> <a id="source-motion-tracking-windows-part-1"></a> <a id="source-simple-tracking-using-the-tracker-menu"></a> <a id="source-simple-ways-of-working-with-existing-tracking-data"></a> <a id="source-the-tracker-palette"></a> <a id="source-tips-for-better-tracking"></a> <a id="source-tracker-palette-controls-in-more-detail"></a> <a id="source-tracker-palette-modes"></a> <a id="source-tracking-one-frame-at-a-time"></a> <a id="source-tracking-windows-across-transitions"></a> <a id="source-tracking-windows-when-youll-be-exporting-media-with-handles"></a> <a id="source-types-of-tracking"></a>

### Motion Tracking Windows

You can certainly keyframe a Power Window by hand to chase a moving subject you'd like to isolate, but this chapter explains how the cloud- and point-based motion tracking tools in DaVinci Resolve let Power Windows ride along with the movement of both subjects and the camera as quickly and easily as possible. A range of methods then follow for handling tricky tracking situations and the recurring difficulties that show up with subjects that resist tracking.

The Tracker palette has three modes, available from the Palette menu.

- Window mode gives you tracking controls that lock a window onto the motion of a moving feature in the shot.
- Stabilizer mode applies that same engine to calm or steady movement across the whole frame.
- FX mode provides a Point Tracker for driving the positioning controls of ResolveFX or OFX plugins.

To learn more about the FX and Stabilizer modes, refer to Chapter 152, “Sizing and Image Stabilization.” DaVinci Resolve ships with a remarkably straightforward yet potent 3D cloud tracker, letting you lock any Power Window (Circular, Linear, Polygonal, Curve, or Gradient) quickly and precisely onto any moving feature. That spares you from hand-animating a window's location with dynamic keyframes. Specifically, the tracker can match a window's position, size, rotation, plus its pitch and yaw in 3D space, to either foreground or background objects that travel through the frame.

### A Power Window tracking a woman’s face

### Simple Tracking Using the Tracker Menu

The quickest route to tracking a feature with a Power Window is through the commands in the Color > Tracker menu. Those commands are: Track Forward (Command-T): Tracks a window onto a feature starting at the playhead's current location and running ahead to the clip's final frame. Track Reverse (Option-T): Tracks a window onto a feature from where the playhead sits and moving backward, finishing at the clip's first frame. Track Stop (Command-Option-T): Halts any track. Handy for aborting a lengthy track that has gone bad (the Stop button on a control panel halts tracking too). One Frame Forward (Option-Right Arrow): Advances a window's track onto a feature by a single frame past the current spot. One Frame Reverse (Option-Left Arrow): Moves a window's track onto a feature one frame back from where you are. The majority of window tracks can be handled with these three commands. To make any Power Window follow a moving feature inside the frame: 1 Position the playhead on the frame of the current shot where you'd like to start (you needn't begin tracking on a shot's first frame). 2 Switch on any window and shape it to enclose the feature you intend to track. You've usually done this already anyway—for instance, ringing someone's moving face with a Circular window to brighten their highlights. 3 To initiate tracking, do one of the following:

- Choose Color > Tracker > Track Forward (press Command-T).
- Choose Color > Tracker > Track Reverse (Option-T).

DaVinci Resolve then opens the Viewer page on its own, drops a cluster of tracking points inside the window you drew, and runs the track from the current frame—ahead to the last frame or back to the first. DaVinci Resolve studies a cloud of tracking points that ride the vectors of each trackable cluster of pixels inside your window, producing quick and accurate results. Once the track completes, the window you positioned automatically shifts, scales, spins, and shears to keep pace with the feature being tracked. As soon as a clip carries tracking data on one of its windows, a tiny tracking icon shows up inside that clip's icon on the Thumbnail timeline.

A tracking badge in the upper-left of the Thumbnail timeline marks a clip as tracked

Object tracking underway. The software drops tracking points automatically across the image's trackable features Should the track you ran prove unsatisfactory, you can move the window over a different region of the subject you want to track and start the track over. Fresh tracking data replaces whatever previous tracking data was on that window. After you're pleased with the track, you can keep resizing, repositioning, or reshaping the tracked window. Because tracking data lives separately from the window transform parameters (which support keyframing), any edits you make to a window shift it away from the path that was originally tracked.

### Tracking Windows Across Transitions

If you track a window that spans a transition boundary—say a dissolve between two clips—DaVinci Resolve carries the track onward across the entire stretch of video beneath the transition automatically.

### Tracking Windows When You’ll Be Exporting Media With Handles

Because windows tracked to follow moving features in a clip are only transformed on the frames that hold tracking data, Round Trip workflows—where you append handles to graded rendered clips so editorial keeps trimming room in the footage you hand off—require you to track every window across the full span of those handles. That way, if an editor actually trims any of the clips you delivered to make use of the handles, all the windows behave correctly. A simple approach is to choose View > Show Current Clips With Handles, which displays each clip you pick within the Timeline alongside handles whose size comes from the “Default handles length” control located in the Editing panel under the User Preferences. Verify that this “Default handles length” lines up with the handles you output via the “Add X Frame handles” choice found in the Render Settings list over on the Deliver page. Once each clip's handles show up this way, it becomes simple to track windows across every frame you'll render.

### Simple Ways of Working With Existing Tracking Data

When a stretch of a shot is left untracked—maybe you began tracking later, or stopped before the shot ended—the window you tracked simply stays put at the first or last frame that did get tracked. To close those gaps, move the playhead to the first or last tracked frame and run Track Backward or Track Forward to cover the rest of that shot's frames.

### Tips for Better Tracking

When a feature shifts shape in a way that throws off the tracker, try tracking a smaller portion of it with a smaller window. After you land a clean track, you're free to resize the window however you need, and it won't disturb the track you already created. Likewise, if you're tracking a feature that slips behind something onscreen and vanishes for the rest of the shot, there's an easy way to keep an awkward window from hanging in the middle of the scene. You can apply dynamic keyframes to animate the Key Output Gain parameter (found in the Key tab of the Color page), ramping it from a full-strength correction of 1.0 toward 0—the level where the correction disappears and carries the window off with it.

### Tracking One Frame at a Time

Within the Tracker palette, clicking either the “track one frame forward” button or its “track one frame backward” counterpart lets you advance a track over a moving feature a single frame at a time, which makes it simpler to tweak a tough track once you've set tracking to Frame mode (by clicking the Frame button). While in Frame mode, you can keyframe window transformations to hug awkward motion more faithfully as you step through the track one frame at a time; manual edits to a window's position become keyframes that build frame-specific transformations, instead of offsetting the entire tracked motion path the way Clip mode does. As you stack multiple keyframes in the Tracker graph, the animation interpolates from one keyframe to the next on its own.

### Copying and Pasting Tracking

Frequently you'll set several windows on a single moving subject—a car, perhaps—where one motion track can drive them all. Through commands in the Option menu, track data copies and pastes from one window onto another inside the same node, which saves time whenever you want a group of windows tracking in unison. Transferring track data between two windows goes like this: 1 Open the Window palette, then highlight a window already carrying tracking (marked by a tracking badge at its shape icon's corner); from the Option pop-up, choose Copy Track Data. 2 Highlight a different window; from the Option pop-up, choose Paste Track Data. Once one window's track data is on the clipboard, paste it onto as many further windows as suits you. By the same token, tracking can be pulled out of the Tracker palette's FX mode and dropped onto a window, for cases where one set of tracking data ought to power both an effect and a window. Moving track data off an FX track onto a window works this way: 1 Open the Tracker palette, highlight the FX mode that holds the tracking data you'd like to grab; from the Option pop-up, choose Copy Track Data. 2 Open the Window palette, highlight a window; from the Option pop‑up, choose Paste Track Data. Once one window's track data is on the clipboard, paste it onto as many further windows as suits you.

### Tracker Palette Controls in More Detail

Mixing object tracking with keyframing to animate windows is easy. As a rule, you'll lean on object tracking to make a window track the position and orientation of a moving feature, but you can layer dynamic marks onto the window track of the correction in the Color page to adjust its size and shape so it hugs a feature's shifting form.

### Controls in the Window Tracker Palette

Now and then you'll hit a shot that just won't track cleanly with the Tracker menu's simple commands. For those, the Viewer page exposes the full suite of object tracking controls you can use to tweak tracking operations across different scenarios.

### The Tracker palette

The object tracking controls are divided into seven groups.

### Tracker Palette Modes

The Option drop-down menu of the Tracker palette lets you pick among Window mode (to lock a window onto the motion of a feature in the frame), Stabilizer mode (to tame unwanted camera movement For details about Stabilizer mode, consult Chapter 152, “Sizing and Image Stabilization.”), and FX mode (to track position for use with Resolve FX or Open FX plugins).

### Types of Tracking

A pop-up menu sitting below the Tracker graph lets you decide between the Cloud Tracker and the Point Tracker.
