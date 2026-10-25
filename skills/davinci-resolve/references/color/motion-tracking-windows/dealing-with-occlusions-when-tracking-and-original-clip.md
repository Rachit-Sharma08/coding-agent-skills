# Dealing with occlusions when tracking and original clip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Motion tracking windows.
[Chapter index](INDEX.md) / [Next section](window-rotoscoping-after-tracking.md)
<a id="source-clicking-the-delete-tracker-icon"></a> <a id="source-dealing-with-occlusions-when-tracking"></a> <a id="source-motion-tracking-windows-part-2"></a> <a id="source-original-clip"></a> <a id="source-point-tracker-workflows"></a> <a id="source-removing-trackers"></a> <a id="source-tracking-a-window-using-the-point-tracker"></a> <a id="source-using-frame-mode-to-offset-track"></a>

### Dealing With Occlusions When Tracking

Now and then, a stretch of usable tracking data simply isn't there and you have to compensate. A typical cause: something in the shot moves in front of whatever you're following, breaking the continuity of a clip's tracking record. When the thing you're tracking disappears entirely behind some other object in the picture, a straightforward interpolation trick fills in the missing stretch of data. Take the example below, where the woman strolls behind yet another fence post, except this one rises higher than her head. At that moment the window following her face loses its target outright, yet interpolation lets you rescue the take.

### Original clip

Bridging across an occlusion by joining two separate spans of track data: 1 Position the playhead on the earliest trackable frame of the moving feature you're fixing, then draw a Power Window enclosing it.

Adding the Power Window 2 Use Track Forward to advance along the feature as long as you're able, right up until something else in the shot hides it. 3 As soon as the Power Window can no longer hold onto the feature dependably, halt the track.

With the post now blocking the Power Window 4 Open the Tracker palette. 5 Click the Frame button to switch the Tracker into a mode that adjusts one frame at a time. Don't skip this step.

Selecting Frame mode 6 Bring the playhead to whatever frame shows the tracked feature emerging again from behind the obstruction, then reposition the window until it sits over the feature once more.

Moving the playhead and position the window 7 Use Track Forward to keep following the feature through to the clip's final frame. As an alternative, you might have begun at the tail of the clip and applied Track Reverse to follow the feature back as far as it would go, whichever proves simpler. Having now pinpointed where this clip loses dependable tracking, you can move on to configuring the interpolation.

Observe the missing stretch of track data left where the window sat behind the post

8 Drag a bounding box around the segment of the Tracker graph curves lying between the solid tracking at the start and at the finish of the shot.

9 From the option pop-up menu of the Tracker palette, pick Clear Selected Track Data.

Whatever portions of the curves you highlighted get removed, and linear interpolation steps in automatically across that span, leaving no break in either the track data or the window's travel, which glides cleanly from the final reliable frame on one side to the first reliable frame on the other.

### Point Tracker Workflows

For all the sophistication of the Cloud Tracking enabled by default in DaVinci Resolve, certain situations are handled more readily with plain old-school crosshairs. The Point Tracker is built to lock onto very particular details of whatever subject is moving in the way you care about. Where the Cloud Tracker hunts on its own for every trackable point inside a region you outline with a window, the Point Tracker has you drop one or more crosshairs and hand-place them over the high-contrast details you intend to follow. Below are the three principal workflows that cover working with the Point Tracker.

### Tracking a Window Using the Point Tracker

What follows sketches, at a broad level, the way you'd employ the Point Tracker to follow a subject in motion and pass that movement to a Power Window. 1 Set the playhead on whichever frame of the present shot you'd like as your starting point (there's no rule that you begin at a shot's opening frame, given that tracking backward is always an option). 2 Switch on a window of any kind and shape it around the feature you mean to track. As a rule you'd already have set this up, say, surrounding someone's moving face with a Circular window to brighten

their highlights. Confirm that the window meant to receive the tracked motion is the one selected before tracking starts. Here, we'll track a Circular window so it trails the woman’s face.

Preparing to follow a window placed across a woman's face 3 Bring up the Tracker palette, then pick Point Tracker via the lower-right pop-up.

Choosing the Point Tracker 4 Ahead of tracking, decide which kinds of motion you'd like analyzed and passed to the window in front of you. The available choices are Pan, Tilt, Zoom, Rotate or Perspective 3D. How many of these transformations you can actually apply hinges on the number of points you set up to track. Picking which sort of motion gets analyzed 5 Click the Add Tracker Point icon. A fresh tracker crosshairs shows up in the Viewer, centered on the frame.

Clicking the Add Tracker Point icon

6 Bring the pointer right onto the tracker crosshairs, and once it becomes the move cursor, drag it so the crosshairs sit squarely over the feature you intend to track. You'll get the cleanest result by choosing a high-contrast detail, such as a corner, a line's endpoint, a tiny shape like a pebble, or some ragged detail. In contrast to other point trackers, here there's no separate inside or outside zone to tune, just the single crosshairs you have to position. In this case, that first crosshairs lands at the inner edge of her stage left eyebrow (parking it at the corner of her eye would add too much jitter, since the tracker would catch her blinks).

Aligning the tracker crosshairs onto the detail you intend to follow 7 To sharpen the precision of the track, you can add further tracker crosshairs and drop them over additional details on the subject you're following. The cleanest results come from putting every crosshairs on details sharing one plane of motion. Put differently, avoid placing some crosshairs on a foreground face and others on a distant background tree, because those two features travel along wildly different motion vectors. Here, the trackers go on her inner eyebrows and at the corner of her lips.

Placing four trackers onto the corners of her eyebrows and mouth

The completed track, done with four point trackers and the track path displayed 8 Once your crosshairs are all set, click either Track Forward or Track Backward to begin tracking. The clip gets analyzed, the Tracker graph fills in with the tracking data, and the window you'd selected shifts on its own to match how the tracked feature moves.

### Removing Trackers

Should a given tracker turn out to cause trouble, you can get rid of it by selecting it inside the Viewer and clicking the Delete Tracker icon, then retracking the subject afterward.

### Clicking the Delete Tracker icon

### Using Frame Mode to Offset Track

One recurring headache with point tracking is handling occlusions, along with moments when the tracked feature drifts out of the frame. The remedy in DaVinci Resolve is the Frame mode of the Tracker palette, which lets you shift the tracker crosshairs over to a different feature while keeping the resulting motion offset so it stays on the original motion path. 1 Here, a point tracker crosshairs sits at the corner of a building's window that's being adjusted on its own with a Power Window. The window serves the purpose because, once the woman turns to depart, she blocks most of the building's other trackable outer edges, which would otherwise wreck the track.

Setting up to track a building moving off screen

2 With the camera panning, the tracked feature is on the verge of leaving the frame, which threatens to wreck the track. The moment this occurs, click the Stop Track button.

Halting the track at its final solid frame, just before the tracker leaves the screen 3 Return the playhead to the last solid frame of tracking, then click the Frame button in the Tracker palette to enter Frame mode.

Turning on Frame mode, to prepare to offset the track 4 While in Frame mode, you can drag the tracker over to a different part of the building, this time the roof's outer edge, which makes a better target as the building exits frame to the left, given that the Power Window leaves frame ahead of the building roof's far right corner.

Moving the tracker onto a different, more suitable feature 5 Now press the Track Forward button once more, and the crosshairs start following the new feature, except the motion is offset, so the Power Window keeps traveling along the original motion path.

By tracking an offset feature, you let the window travel entirely past the screen edge

Across the relocation of the tracker crosshairs in Frame mode, the tracker path stays smooth and unbroken 6 If you switch on the track path (via the Tracker Option menu) and park the playhead on the frame where the tracker was relocated, you'll notice the motion preceding the move and the motion after it flow on along one continuous path, free of abrupt jumps. Once you're done, click the Clip button to leave Frame mode.
