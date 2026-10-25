# Camera tracker solve tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera tracker.
[Chapter index](INDEX.md) / [Previous section](camera-tracker-track-tab.md) / [Next section](camera-tracker-3d-scene-transform.md) / [Camera Tracker CTra](camera-tracker-track-tab.md)
<a id="source-delete-trim-previous"></a> <a id="source-export"></a> <a id="source-export-1"></a> <a id="source-operations-on-selected-tracks"></a> <a id="source-solve-tab"></a> <a id="source-solve-weight"></a> <a id="source-the-camera-tracker-export-tab"></a> <a id="source-the-camera-tracker-solve-tab"></a> <a id="source-track-filtering"></a> <a id="source-trim-next-rename-set-color-export-flag"></a>

### Solve Tab

### The Camera Tracker Solve tab

The Solve tab is the place where tracking data gets turned into a rebuilt camera motion path together with the point cloud. It's also where you scrub out bad or false tracks and carry out other track operations, like deciding which marks ship out in the Point Cloud 3D. You can additionally weight the markers to steer the solve calculations. As an example, you might already have a solid camera solve, yet the point cloud lacks enough locators in a spot where an object has to sit, so dropping in extra tracks and setting their Solve Weight to zero leaves the solved camera untouched while adding more points to the cloud. Solve Hitting Solve fires up the solver, which combines the tracking information and the camera specifications to build a virtual camera path and point cloud that approximate how the physical camera moved across the live-action footage. The console pops open by itself, showing the solver's progress. Delete Delete strips away any solved information, the camera and the point cloud included, yet retains all of the tracking data. Average Solve Error After the camera is solved, a recap of the solve calculation appears at the top of the Inspector. Foremost among those figures is the Average Solve Error. That number serves as a solid gauge of whether the camera solve worked. Picture it as the gap (in pixels) between tracks in the 2D image and the rebuilt 3D locators projected back onto the picture through the rebuilt camera. In the end, when you're after a low solve error, anything under 1.0 pixels usually produces a good track. Landing between 0.6 and 0.8 pixels counts as excellent.

Clean Tracks by Filter Pressing this button picks out tracks according to the Track Filtering options. Should the Auto Delete Tracks By Filter checkbox be switched on, the picked tracks get deleted too. Clean Foreground Tracks Pressing this button selects the tracks riding on fast-moving objects that would otherwise drive up the solve error. The Foreground Threshold slider decides that selection. Foreground Threshold This slider fixes the detection threshold for spotting tracks on fast-moving objects. A higher value is more forgiving. Auto Delete Tracks by Filter With this checkbox on, the tracks chosen by the Clean Tracks By Filter button get deleted. Switch on the checkbox, then hit Clean Tracks By Filter. Every track matching the filtering options is then chosen and removed. Auto Delete Foreground Tracks With this checkbox on, the tracks chosen by the Clean Foreground Tracks button get deleted. Switch on the checkbox, then hit Clean Foreground Tracks. Every track satisfying the foreground threshold criteria is removed. Accept Solve Error This slider sets a tolerable ceiling for the solve error. Should the solve error exceed this figure, the Camera Tracker sweeps across the focal length setting trying to drag the solve error below the Accept Solve Error value. If the solver still can't land a solution, the Camera Tracker prints a console message saying the solver failed. When no solution turns up, your best move is to feed in the correct focal length or else manually clean out some noisy tracks and re-solve. Auto Select Seed Frames With this switched on, the Camera Tracker picks two frames to act as a reference for kicking off the solve. Those two frames get solved first and a camera is rebuilt, after which more frames are folded in gradually and the solution is "grown" outward from the seed frames. Which seed frames you use heavily shapes the whole solve and can readily make the solve fail. The seed frames may be located automatically or set by hand. Switching this off lets the user choose their own pair of frames. Picking seed frames by hand suits advanced users. While selecting seed frames, you have to balance two opposing aims: the seed frames ought to share a lot of tracks yet sit far apart in perspective (that is, the baseline distance separating the two corresponding cameras is long). Refine Focal Length Switching this on lets the solver nudge the lens focal length so it matches the tracking points. You can keep the focal length from being nudged by locking the Focal Length parameter in the Camera tab.

Enable Lens Parameter With this on, lens distortion parameters become available to assist in fixing lens distortion during the solve.

- Refine Center Point: Usually off, since camera lenses tend to sit centered within the film gate, though that can vary on certain cameras. As an example, a cine camera might be configured for Academy 1.85, which carries a sound stripe along the left, and when shooting super35 the lens shifts to the right.
- Refine Lens Parameters: This refines the lens distortion or the lens's curvature. Wide angle cameras tend to show more distortion.

NOTE: While solving for the camera’s motion path, a simulated lens is built internally to mimic the lens distortion present in the source footage. That simulated lens model is far simpler than actual real-world lenses, yet it grabs the lens distortion traits that matter for landing an accurate camera solve. The Camera Tracker models two distortion types: Radial Distortion: How strong this distortion gets depends on how far you are from the lens center. Pincushion, barrel, and mustache distortion all serve as examples. Bigger values map to bigger lens curvatures. Capturing radial distortion matters most for wide angle lenses and fisheye lenses (which carry heavy distortion because they take in 180 degrees of a scene and then optically cram it onto a flat rectangular sensor). Tangential Distortion: This distortion arises when the camera’s imaging sensor and the physical lens aren't parallel to one another. It tends to throw skew distortions into the footage akin to what you'd get by tugging the corners of a corner pin inside Fusion. You'll see this distortion in really cheap consumer cameras, while it's all but absent in film cameras, DSLRs, and essentially any camera used across film or broadcast. Leaving it off is the recommendation. Enable Lens Parameters With this off, the Camera Tracker runs no lens curvature simulations at all. That's the default, and it should stay off whenever the lens has very low distortion or the lens distortion has already been stripped out of the source clip. Switching on the Enable Lens Parameters checkbox decides which lens parameters get modeled and solved for. Any parameter left off keeps its default values. These are the available options:

- Radial Quadratic: Models nothing but Quadratic radial lens curvature, namely barrel or pincushion distortion. It's the type of distortion seen most often. Picking it has the low and high order distortion values solved for.
- Radial Quartic: Models nothing but Quartic radial lens curvature, which blends barrel together with pincushion distortion. With it, the low and high order distortion values get solved for.
- Radial & Tangential: Models and solves both the radial and the tangential distortion. Tangential ties back to lens elements that sit misaligned.
- Division Quadratic: Delivers a sharper simulation of Quadratic radial lens curvature. Here too, the low and high order distortion values are solved for.
- Division Quartic: Delivers a sharper simulation of Quartic radial lens curvature. Once more, the low and high order distortion values end up solved for.

Lower Order Radial Distortion: Every simulation offers this slider. It governs the quadratic lens curvature. Higher Order Radial Distortion: Only Quartic simulations offer this slider. It governs the quartic lens curvature. Tangential Distortion X/Y: Only Tangential simulations offer these sliders. They govern skew distortion.

### Track Filtering

The Camera Tracker is capable of churning out a great many auto-generated tracks. Instead of pouring time into inspecting the quality of each track one by one, it helps to have quicker ways of weeding out big batches of potentially bad tracks. The input sliders below come in handy for grabbing large groups of tracks by certain quality metrics, after which you can run a range of different operations on them. As an example, the weaker tracks can be picked out and deleted, leaving a stronger set of tracks to solve from. Every filter can be switched on or off on its own. Minimum Track Length (Number of Markers) Grabs tracks whose duration falls below the slider’s value. Short tracks rarely get the chance to travel far, so they hand the solver less perspective information than a longer track does, yet short and long tracks alike carry equal weight in the solve process, which makes long tracks worth more to the solver. Locators tied to shorter tracks also land less precisely in 3D space than those tied to longer tracks. When a shot holds plenty of long tracks, clearing out the short ones can pay off. On typical shots, a value somewhere from 5 to 10 is suggested. Where long tracks are scarce (say, the camera spins quickly so tracks begin and slide off frame fast), a value nearer 3 is advisable. Maximum Track Error Grabs tracks whose average track error tops the slider’s value. During tracking, tracks shut down on their own once their track error passes some threshold. That auto shutdown governs the maximum track error, whereas this slider governs the average track error. As an example, tracks chasing the leaves in a tree are often inaccurate and may sometimes be flagged by their high average error. Maximum Solve Error Grabs tracks whose solve error tops the slider’s value. Among the simplest ways to sharpen a camera solve is to grab the 20% of tracks carrying the highest solve error and just delete them (though now and then this backfires). Select Tracks Satisfying Filters Grabs the tracks in the scene that meet the Track Filtering values above. Note that pressing this button shows the tracks meeting the filter values in the Selected Tracks area of the Solve tab and tints them in the viewer. This button helps when Auto Select Tracks While Dragging Sliders is switched off, or when the selection got lost by accident, say, from a stray click in the viewer. Auto Select Tracks While Dragging Sliders With this ticked on, dragging the sliders above (Minimum Track Length, Maximum Track Error, Maximum Solve Error) selects the matching tracks interactively in the viewer.

### Operations on Selected Tracks

Tracks picked straight in the viewer with the mouse, or picked through track filtering, can have these operations run on them:

### Delete Trim Previous

### Trim Next Rename Set Color Export Flag

### Solve Weight

None Toggle All Show Names Show Frame Range Show Solve Error

Pulls the tracks out of the set. Faced with bad tracks, the plainest, easiest move is to just delete them. Snips the tracked frames running from the current frame back to the track's start. Trimming a track can sometimes serve you better than deleting it. As an example, high-quality long tracks turn inaccurate once the feature they follow begins to be occluded, or once the tracked feature drifts too near the picture's edge. Snips the tracked frames running from the current frame to the track's end. Swaps the current auto-generated name for a fresh one. Permits a user-assigned color for the tracking points. This decides whether the locators tied to the chosen tracks ship out in the point cloud. By default, every locator is flagged exportable. By default, all tracks are used and weighted equally while solving for the camera’s motion path. The most frequent use of this option is to drop a track’s weight to zero so it stays out of the camera’s motion path yet still keeps a rebuilt 3D locator. Setting a track’s weight to anything besides 1.0 or 0.0 should be left to advanced users. These functions govern the onscreen display of track names and values: Clears/hides the selected tracks. Swaps the selected and unselected track sets. Selects every track. Shows the track name. By default these are numbers. Shows a track's start and end frame. Shows how much solve error each selected track carries.

Selected Tracks This area shows the properties of a track point or a group of points. Its options let you:

- Clear: Deselects all tracks and clears this area.
- Invert: Deselects the current selected tracks and selects the other tracks.
- Visible: Selects all the trackers at the current frame.
- All: Selects all trackers on all frames.
- Search: Selects tracks whose names contain a substring.

TIP: You can also pick tracks straight in the 2D viewer with the mouse, or in the 3D viewer by picking their matching locators within the point cloud.

### Export

Through the Export tab you convert the tracked and solved data this node has produced into a form usable for compositing.

### The Camera Tracker Export tab

### Export

Clicking the Export button builds a basic setup ready for 3D match moving:

- A Camera 3D whose animated translation and rotation track the live-action camera's movement, plus an attached image plane.
- A Point Cloud 3D that holds the rebuilt 3D positions of the tracks.
- A Shape 3D configured to produce a ground plane.
- A Merge 3D that combines the camera, point cloud, and ground plane. Look at the Merge 3D through the camera within a 3D viewer and the 3D locators ought to ride along with the tracked footage.
- A Renderer 3D configured to match the input footage.

Whether individual nodes get exported can be toggled on or off in the Export Options tab. Update Previous Export Clicking this button refreshes the previously exported nodes with whatever new data has been produced. Those previously exported nodes are tracked in the Previous Export section down at the bottom of this section. Here’s a case showing why this helps: 1 Export after solving the camera. 2 Build out an elaborate Node Editor around those exported nodes to handle a set extension.

3 Maybe the camera isn't as precise as you'd like, or perhaps you re-run the solver to fold in extra tracks for a denser point cloud. Rather than exporting the Camera 3D and Point Cloud 3D nodes a second time and threading them back in, just press the Update Previous Export button to “overwrite” those existing nodes right where they are. Automatically Update Previous Export After Solves With this, every node already exported (Camera 3D, Point Cloud 3D, Lens Distort, Renderer 3D, plus the ground plane) updates itself each time you solve.
