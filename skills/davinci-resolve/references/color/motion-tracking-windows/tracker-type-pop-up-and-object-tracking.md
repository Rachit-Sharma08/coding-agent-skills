# Tracker type pop up and object tracking

Version: DaVinci Resolve 20.3 Reference Manual. Context: Motion tracking windows.
[Chapter index](INDEX.md) / [Previous section](power-window-tracking-and-tracker-menu.md) / [Next section](tracker-options-cloud-features-and-intellitrack.md)
<a id="source-clipframe-controls"></a> <a id="source-interactive-mode-controls"></a> <a id="source-interactive-mode-controls-1"></a> <a id="source-object-tracking"></a> <a id="source-point-tracker-controls"></a> <a id="source-point-tracker-controls-1"></a> <a id="source-selecting-clip-or-frame-to-apply-adjustments"></a> <a id="source-the-tracker-graph"></a> <a id="source-the-tracker-type-pop-up"></a>

### The tracker type pop-up

There are three options:

- The Cloud Tracker: Scans every region of the image for trackable points on its own and uses them to work out the motion in the shot you want for driving a Power Window or steadying a shot. This tracker type excels at quickly locking a window onto the movement of nearly any feature with very little effort.
- The Point Tracker: Lets you place one or more tracker crosshairs by hand to follow particular features in the shot. The greater the number of crosshairs you add and place, the more precise the track becomes. The Point Tracker shines whenever you need to follow the motion of one very specific feature in the frame. It also helps when you want to steady a shot crowded with subjects moving in different directions, where a good result is hard to reach with the Cloud Tracker.
- IntelliTrack: Is an AI tool that leans on no fixed rulesets or heuristics. Rather, real world examples are what train it. As a result it's less prone to break down in cases such as following a subject through short occlusions. In the majority of situations it proves more accurate and more dependable than the ordinary Point Tracker.

### Object Tracking

The object tracking controls supply the most fundamental tracking functions, a number of which are echoed inside the Color > Tracker menu.

Choose which type of transform you want to track before tracking A row of five checkboxes lets you toggle which transforms motion tracking will apply to the window automatically. You have to select these checkboxes before running a track so the transforms in play are restricted.

- Pan and Tilt: Turns on tracking of horizontal and vertical placement, for when a window should transform to chase a tracked subject's location.
- Zoom: Turns on tracking of size, for when a window should transform and rescale to keep up with a tracked subject.
- Rotate: Turns on tracking of orientation, for when a window should transform and spin alongside a tracked subject.
- Perspective 3D: Turns on tracking of pitch and yaw within 3D space, for when a window should skew to match a tracked subject's orientation inside the scene. Ideal for making a window “stick” to a surface.

NOTE: After tracking or stabilization has run, switching these checkboxes off won't change the result at all. To alter things, you have to enable or disable the checkboxes you need first, and then reanalyze the clip.

Having set the transforms you intend to track, the analyze controls then let you go ahead with analyzing the subject being tracked.

- Track One Frame Reverse button: Motion tracks one frame backward. Handy for the slow tracking of tricky subjects that need frequent correction.
- Track Reverse button: Starts tracking backward from the present frame, finishing at the clip's first frame. Useful for reverse tracking when your ideal launch point falls somewhere in the shot's middle.
- Pause button: Halts tracking (assuming you click this button quickly enough before the track wraps up).
- Track Forward button: Starts tracking ahead from the present frame, finishing at the last frame of

the clip.

- Track Forward and Back button: Starts tracking ahead from the present frame, then on

completion runs backward from the frame you originally selected. That gives you a single-button method for tracking out of the middle of a shot.

- Track One Frame Forward button: Motion tracks one frame ahead. Handy for the slow tracking of tricky subjects that need frequent correction.

### Clip/Frame Controls

A pair of buttons governs how hand-made tweaks to the placement of tracked windows influence the track as a whole.

### Selecting clip or frame to apply adjustments

- Clip: This is the default mode, where edits you make to a window's position apply across the whole track at once. As an example, track a feature and then drag the window, and the window travels along a motion path held at a steady offset from the original track for the whole clip. Reach for this mode when the track satisfies you but you'd like to tune the window's overall shape and placement relative to the path of motion it rides.
- Frame: Here, the edits you make to a window's position or shape lay down a keyframe at the frame where the playhead sits. Several keyframes interpolate into animation, letting you hand-transform a window to tackle assorted problems. The mode helps with rotoscoping window shape and placement to match a subject that defies automatic tracking. Frame mode also serves for repairing individual frames that tracked poorly, for animating windows that follow a subject completely out of frame, or for making manual, frame-by-frame window position tweaks to cover untrackable≈sections.

### The Tracker Graph

The Tracker graph gives you a visual readout of the tracking data under analysis. Every transform control that can be tracked owns its own curve, letting you assess each tracked parameter independently, and each curve carries a color that matches the corresponding label of the tracking transforms listed above. A vertical slider on the right of the Tracker graph scales the height of the curve data inside so it all fits more readably within the graph. A horizontal slider along the bottom of the graph zooms the tracker curves in and out, revealing finer detail in the tracking paths. Above the Tracker graph sits a Timeline ruler holding a playhead locked to the playheads in the Viewer and Keyframe Editor.

The Tracker graph showing a curve for each transform control Within the Tracker graph you can draw a bounding box to select part of one or more curves and remove sections of poor-quality tracking data using the Clear Selected Keyframes command in the Tracker Options menu. To clear the current bounding box from the Tracker graph, click once anywhere inside the graph.

### Interactive Mode Controls

Sitting at the bottom-left of the Tracker palette, the Interactive controls let you hand-edit the tracking point cloud that DaVinci Resolve builds automatically when you track with the Cloud Tracker, giving you room to experiment with various approaches toward better tracking in difficult shots.

### Interactive mode controls

- Interactive Mode checkbox: Switches the Interactive tracking mode on or off. Entering Interactive mode lets you hand-edit the point cloud that DaVinci Resolve relies on to track the feature inside the current window. You then run your track while Interactive mode is active.
- Insert: Adds tracking points onto whichever trackable features sit inside a bounding box you've drawn in the Viewer. The inserted tracking points land automatically according to the image's trackable pixels.
- Set Point: Lets you reach for the cursor (with the DaVinci Resolve Advanced control panel) to drop individual tracking points by hand, one at a time, to track a feature. Should no trackable pixel group sit at the cursor's coordinates, the tracking point snaps to the closest trackable pixel group. Tracking rotation requires at least two tracking points on separate pixel groups, and tracking zoom requires at least three.
- Delete: Wipes out every tracking point inside a bounding box you've drawn in the Viewer.

### Point Tracker Controls

When the Point Tracker is active, the Interactive Mode controls go away, swapped out for the Point Tracker's two controls.

### Point Tracker controls

- Add Tracker: Click to spawn a fresh tracker that lands automatically at the frame's center. After it exists, drag it with the pointer to align with whatever feature you intend to track. Create however many trackers you wish; they all track together at once.
- Delete Tracker: Pick any tracker (red marks a selected tracker, blue a deselected one), and click this button to get rid of it.
