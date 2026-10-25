# How to judge track accuracy and deleting tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D camera tracking.
[Chapter index](INDEX.md) / [Previous section](automatic-tracking-point-count-and-preview.md) / [Next section](camera-tracker-filtering-and-scene-export.md)
<a id="source-3d-camera-tracking-part-2"></a> <a id="source-deleting-tracks"></a> <a id="source-how-to-judge-track-accuracy"></a>

### How to Judge Track Accuracy

Because tracking markers get color-coded on their own, weeding out false or weak tracks becomes simpler. After the solver finishes, every tracker receives a solve error color flagging which 3D locators line up closely with their 2D tracking points and which line up badly.

- Green: Good. Tracked very well.
- Yellow: Moderate confidence. Usually an acceptable track.
- Orange: Low Confidence. May be acceptable in some situations.
- Red: No Confidence. The tracks have not solved well.

Park the pointer over any tracking point and a sizeable metadata tooltip pops up carrying that point's solve error. For a clearer picture of the accuracy, switch on the 3D locator display in the viewer using the Reprojection Locators button on the viewer toolbar.

After a solve, the Camera Tracker toolbar can display Reprojection locators As the solver turns the tracking points into a point cloud, it generates a 3D reprojection locator for every tracking point. Each of these Reprojection locators shows up as a tiny X mark beside its matching tracking point. The tighter those two sit on each other, the smaller the solve error.

Reprojection locators displayed with tracking points, and tooltip Filtering the trackers comes down to clearing out every red tracker mark while holding onto all the green ones. Deciding whether to keep both yellow and orange, or yellow alone, mostly depends on how many marks the clip gives you. Keeping yellow marks only yields a better solve, yet if there aren't enough marks left to compute the 3D scene, you'll have to retain a few of the stronger orange ones too. Tips for What to Keep and What to Delete Learning to recognize false tracks, then trimming the track data by hand down to a tight set of clean tracks, leads to a more accurate solve. As you tidy any track—especially the yellow and orange color-coded ones—bear these points in mind:

- Hold onto any track whose movement is driven entirely by the movement of the

live‑action camera.

- Remove tracks sitting on people or objects in motion, along with any that suffer parallax issues.
- Remove tracks showing up as reflections in glass or water.
- Remove tracks on highlights that slide across a surface.
- Remove tracks that fail to track a feature cleanly.
- Remove tracks landing on false corners produced where

foreground and background layers overlap.

- Think about removing tracks tied to locators the solver placed

at the wrong Z-depth.

### Deleting Tracks

Removing tracks can be done by hand in the viewer or through filters that grab batches of tracks at once. For hand-deletion in the viewer, it helps to tweak the viewer a little so the tracks read more clearly. On the Camera Tracker toolbar over the viewer, hitting the Track Trails button conceals the trails behind the tracking points. With the viewer thus tidied to points alone, selecting becomes easier. Over at the toolbar's far right, the Darken Image button dims the image a touch, once more helping the points pop in the viewer.

Concealing trails and dimming the viewer makes spotting and picking out weak tracks simpler

When you set out to remove low-quality tracks, drag a selection box across the cluster of tracks you'd like gone. To get rid of them, use the Delete Tracks button found on the Camera Tracker toolbar, or simply hit Command-Delete. Keeping the Command key held down lets you pick out scattered tracking marks that sit apart from one another. Should you mistakenly grab tracks you meant to keep, hold the Command key still and drag back over them to release the selection. As you delete tracks, watch the current Average Solve Error shown at the top of the Inspector, then run the solver again. Removing tracks in small batches and re-solving each time beats wiping out one or two big chunks at once. As noted earlier, cutting away too many tracks can backfire and drive the Average Solve Error up.
