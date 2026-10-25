# Surface tracker mesh

Version: DaVinci Resolve 20.3 Reference Manual. Context: Surface tracker.
[Chapter index](INDEX.md) / [Previous section](planar-tracker-node-and-surface-tracker.md) / [Surface Tracker SFt](planar-tracker-node-and-surface-tracker.md) / [Next section](surface-tracker-result.md)
<a id="source-mesh"></a> <a id="source-the-mesh-tab-in-the-surface-tracker-controls"></a> <a id="source-the-track-tab-in-the-surface-tracker-controls"></a> <a id="source-track"></a> <a id="source-tracking-nodes-part-4"></a>

### Mesh

Now that the boundaries are defined, you can build the mesh across the surface to be tracked. Because the first mesh acts as the launch point for tracking, the best results come from placing the mesh when your surface is as square-on and as close to the camera as it gets.

### The Mesh tab in the Surface Tracker controls

You can adjust the mesh by hand, dragging existing points (hold command and drag a region around several points to move them together) or clicking an area to drop new ones. Option-clicking a point takes it out of the mesh. Adding mesh points manually helps when the surface has flexible spots you know will fold the texture but that the mesh placement did not pick up at first. For example, an outstretched arm may carry no active mesh point at the elbow, but a mouse click (plus a little human anatomy) lets you add one there. Another case is seeding points into a low-detail area that you know will gain detail as it turns into view. Dropping mesh points into blank, low-detail regions will not help the results and can even hurt them, so keeping points sparse on smooth areas is preferable. A handy rule of thumb: once more than five points sit inside the boundaries, the mesh is probably good enough for tracking. After tracking, points can neither be added nor removed. A strong mesh signals strong tracking, since the two go together. When few mesh points are detected and the results fail to track tightly, you can prop them up artificially. For instance, confirm the content is plainly visible. Tracking and point detection can break down when the surface is too bright (HDR), too dark, or low in contrast from working in log. As a fix, you can temporarily insert a brightness/contrast node ahead of the Surface Tracker to set contrast by hand, then run the Surface Tracker. Just switch the brightness/contrast node back off once the tracking wraps up. Regenerate Mesh: This button rebuilds the mesh at the current frame and settings, throwing out any manual changes you made.

- Point Locations: These controls set which mode generates the mesh points.
- Automatic: The Surface Tracker finds the strongest details for tracking on its own and drops

mesh points onto those details. For most situations, Automatic delivers the best results.

- Point Number Limit: Sets the ceiling on how many mesh points get placed. Since the count of mesh points governs how the overlay flexes and folds, set it to match how flexible the surface is expected to be. They have no direct bearing on tracking speed.
- Minimum Point Spacing: Sets the smallest allowed gap between mesh points. This keeps mesh points from clustering too closely in highly detailed regions and getting in each other's way.
- Uniform: Lays a regular grid of points within the boundary and leans on internal shape models to warp that grid as tracking proceeds. On a highly detailed surface, this may beat Automatic mode.

Horizontal Spacing: Sets the horizontal gap between neighboring points in the uniform mesh. Vertical Spacing: Sets the vertical gap between neighboring points in the uniform mesh.

The automatic mesh laid over the boundary. The bee now sits composited on the shirt, though it does not look terribly realistic just yet.

### Track

In this part of the effect, the motion of the mesh points is tracked over time. Run the tracking through the clip with the Tracking Direction controls. Once tracking finishes, the effect performs no further analysis, and any extra contrast help from upstream nodes can be dropped after this step. Straightforward cases may track with no user input at all, while trickier ones call on several added controls to refine the track.

### The Track tab in the Surface Tracker controls

Repairing a broken track takes some hands-on tweaking of both the mesh and the tracking data. Whenever tracking is underway, mesh points can be moved either one at a time or with the lasso selection tool (Command - Drag) drawn around the whole mesh or just sections of it. That lasso selection tool can additionally stretch, scale, and rotate the mesh points, which makes it simpler to warp and position the mesh exactly where you want should the automatic tracking falter. Mesh points cannot, however, be added or removed at this stage until you first reset the tracking. Editing mesh points by hand at a frame touches only that frame directly; the neighboring tracking data is left alone. It does, though, shift the neighboring interpolated positions, which makes it useful for tracking from that point forward. For example:

- Tracking holds up until frame 150, where a few points break away from the rest after a lighting change. At frame 150 you can nudge them back into place, and resuming tracking carries them on with their corrected positions.
- Tracking runs until frame 150, then has no data for a handful of frames before picking back up at 160. Editing the points at either frame 150 or 160 makes the in-between frames interpolate with those changes applied.
- Tracking covers up to frame 150 and from frame 160 onward, leaving frames 151-159 interpolated. Adjusting a few points at frame 155 lays down tracking data there, so frames 151-154 now interpolate from the last tracked frame to this one, and frames 156-159 from this one to the next tracked frame.

Go to Start: Pressing this jumps the playhead to whichever frame was tracked first, or to the frame on which the boundary was made. Go To End: Pressing this jumps the playhead to whichever frame was tracked last. Tracking Direction Controls: This cluster runs the tracking analysis in whichever direction you choose. Reading left to right, the buttons go: Track Backwards, then Track Backwards One Frame, followed by Pause Tracking, next Track Forwards Then Reverse, after that Track Forwards One Frame, and finally Track Forwards. With them you can lay down a track over the entire clip or confine the tracking to only one stretch of it. Trimming: This group lets you reshape the track data once it has already been generated.

- Remove Tracking Data Before This Frame: Wipes every bit of tracking data that precedes the current frame.
- Track From Last Known Match: This button ties the tracking data at the current frame back to the most recent frame that still holds tracking data. Should too much motion separate those two moments, you can nudge the points roughly where they belong and attempt the match once more. Say, for instance, the track runs cleanly up to frame 150, but an object crossing the scene throws the track off for six frames (151-157). You can either pause the tracking data before it reaches those frames or delete that span’s data afterward. Then, at frame 158, this button lets you pick the track back up from the last solid result at frame 150.
- Remove Tracking Data At This Frame: Wipes the tracking data sitting on the current frame.
- Remove Tracking Data After This Frame: Wipes every bit of tracking data that follows the current frame.

Tracking Behavior: These settings let you tune how the tracking behaves.

- Motion Range: Governs how widely the search for matches extends. Push this slider up when the surface moves so fast the tracking can’t keep up with it.
- Mesh Rigidity: Governs the mesh’s flexibility. Lower this slider to loosen up the mesh points. You’ll get the cleanest results when the clip is free of noise and warps gently. Raise this slider for a “stiffer” tracked surface that warps less internally.
- Quality: Because the tracker can demand heavy computation, the advice is to run the Faster setting while you tweak the mesh, then switch to Better for the final track after every parameter is dialed in.

Interaction Overlays: These buttons govern whether the mesh overlays appear in the Viewer.

- Show: Keeps the mesh visible the whole time.
- Hide on Drag: Leaves the mesh visible until you drag a point, at which moment it vanishes so you can study the surface beneath while making fine adjustments.
- Hide: Keeps the mesh hidden the whole time.

NOTE: The Surface Tracker generates data on every frame of the source clip. When the source clip’s frame rate differs from the timeline’s, the tracking can look like it stutters or skips frames. You can “bake” the retiming into a clip by right-clicking it on the Edit page and selecting “Render In Place,” which yields a result carrying precisely one frame per timeline frame.
