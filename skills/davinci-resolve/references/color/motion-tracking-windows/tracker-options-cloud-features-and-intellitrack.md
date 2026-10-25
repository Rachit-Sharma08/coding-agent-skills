# Tracker options cloud features and intellitrack

Version: DaVinci Resolve 20.3 Reference Manual. Context: Motion tracking windows.
[Chapter index](INDEX.md) / [Previous section](tracker-type-pop-up-and-object-tracking.md)
<a id="source-additional-commands-in-the-tracker-options-menu"></a> <a id="source-cloud-tracker-workflows"></a> <a id="source-deleting-tracking-points"></a> <a id="source-intellitrack-ai-point-tracker-studio-version-only"></a> <a id="source-tracking-with-the-remaining-tracking-points"></a> <a id="source-using-interactive-mode-to-manually-choose-tracking-features"></a>

### Additional Commands in the Tracker Options Menu

A few extra commands live in the Tracker Options pop-up menu.

- Reset Track Data on Active Window: Removes the tracking data tied to whichever window is currently selected.
- Clear Selected Track Data: Once you drag a bounding box across portions of one or more curves in the Tracker graph, this command strips out that stretch of the graph. Handy for clearing away passages of poor-quality track data. Any curve passages erased this way receive linear interpolation on their own, just as though you'd reached for the Keyframes Interpolation controls.
- Delete Keyframe: Removes tracker graph keyframes sitting at the playhead's current spot.
- Clear All Tracking Points: Wipes the tracking points out of the Power Window on whatever frame you're parked on.
- Show Track: Switch this checkbox on to reveal the motion path the tracking

generated.

- Copy Track Data: Copies track data off whichever window is currently selected. You can pick windows

right in the Viewer while the Tracker palette stays open.

- Paste Track Data: Drops copied track data onto whichever window is currently selected. You can pick windows

right in the Viewer while the Tracker palette stays open.

### IntelliTrack AI Point Tracker (Studio Version Only)

Powered by the DaVinci Neural Engine, the IntelliTrack point tracker now appears in the Color tracker, the Fusion point tracker, and the FX tracker within DaVinci Resolve Studio. You can put the IntelliTrack setting to work on general tracking and stabilization jobs. Like other AI tools, IntelliTrack relies on no fixed rulesets or heuristics; rather, it learns from real world examples. That makes it less prone to fail in cases such as tracking a subject through brief occlusions. In most situations it'll prove more accurate and more dependable than the standard Point Tracker.

Using IntelliTrack: Every bit of the IntelliTrack analysis runs behind the scenes, and nothing more is asked of you beyond picking the IntelliTrack setting, placing the tracking crosshairs over high contrast regions on the same moving subject, and then pressing one of the tracker direction controls.

Setting the IntelliTrack mode for the Color page window tracker

### Cloud Tracker Workflows

The handful of examples coming up demonstrate how to apply the Tracker palette's controls in real-world cases. Quite often, objects crossing in front of a tracked subject—called “occlusions”—create trouble. Even though the DaVinci Resolve tracker resists occlusions very well, the sections below lay out an assortment of techniques to use when an occlusion keeps you from landing a usable track.

### Using Interactive Mode to Manually Choose Tracking Features

Interactive mode lets you hand-remove or hand-add tracking points to sharpen tracking performance wherever the automatic image analysis in DaVinci Resolve returns disappointing results. For instance, you can drop tracking points inside a window that correspond to overlapping features you'd rather not track. Picture a car you're tracking driving past a sign that partly hides it. Left alone, the PowerCurve isolating the car would distort badly as the car nears the sign and then pulls away from it. With Interactive mode, you can delete the tracking points destined to overlap the sign you don't want to track, sharpening the result.

Getting rid of particular, unwanted tracking points within a track: 1 Open the Tracker palette. 2 Switch on the Interactive Mode checkbox. Enabling Interactive Mode 3 Within the Viewer, drag a box over the tracking points inside the window that you'd like removed.

Boxing in the tracking points slated for deletion 4 Click the Delete button.

### Deleting tracking points

The points within the selection area are deleted.

Remaining tracking points ready to be used

5 With Interactive mode still active, click Track Forward or Track Reverse to track the subject from the remaining tracking points. 6 Once your track is done, switch off the Interactive Mode checkbox. DaVinci Resolve reverts to automatically placed tracking points. In a different interactive tracking case, you may occasionally hit situations where you'd like to scrap every automatically placed tracking point and set your own in particular image regions instead. To remove the automatic tracking points and substitute your own: 1 Open the Tracker palette. 2 Turn on the Interactive Mode checkbox.

Selecting Interactive mode 3 Within the Viewer, drag a box over every tracking point in the window, then click the Delete button to clear all tracking points off the image.

Selection box surrounding all tracking points 4 Click the Delete button to clear all tracking points off the image.

Deleting tracking points

5 Drag a box across the precise region where you'd like new tracking points added. Here you only want the top half of the woman's face tracked, since the fence posts cut off the lower half.

1 Positioning the selection box across the window's upper portion 2 Now, click the Insert Track Points button. Interactive mode's Insert button populates the current bounding box with tracking points by itself. The new tracking points settle automatically onto whichever features within your drawn box are well-suited for tracking.

### Tracking with the remaining tracking points

NOTE: When no suitable tracking features turn up, no points get added.
