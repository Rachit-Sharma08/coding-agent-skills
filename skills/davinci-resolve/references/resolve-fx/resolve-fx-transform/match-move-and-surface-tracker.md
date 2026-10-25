# Match move and surface tracker

Version: DaVinci Resolve 20.3 Reference Manual. Context: Match move studio version only, Surface tracker studio version only.
[Chapter index](INDEX.md) / [Previous section](match-move-a-tracker-control-in-the-match-move-filter.md) / [Match Move (Studio Version Only)](match-move-a-tracker-control-in-the-match-move-filter.md) / [Next section](surface-tracker-result.md)
<a id="source-bounds"></a> <a id="source-compositing"></a> <a id="source-mesh"></a> <a id="source-resolve-fx-transform-part-2"></a> <a id="source-stabilizing"></a> <a id="source-surface-tracker-studio-version-only"></a> <a id="source-the-display-options-group-1"></a> <a id="source-track"></a>

### The Display Options group

Within this group you switch the display of assorted onscreen controls on or off. The available checkboxes are Show Trackers; Show Center, being the red center point of the track; and Show Paths, being the motion paths that were tracked. Show Comp Result displays the composited foreground layer over the background layer.

### Compositing

The Compositing controls oversee the third phase of match moving, used as you fit the foreground image against the background image to build a seamless composite. Note that if the foreground image needs color correction to match the background, you'll have to insert a corrector node between the Ext. Matte feeding the foreground image into the Color page and the FX node performing the compositing.

Controls revealed once Main Controls is switched to Compositing Rendering Options: Through the Composite Type pop-up menu you decide whether the output composite is the Ext. Matte overlaid on the background or the background Plate by itself. Plate Cropping: Four sliders trim the Left, Right, Top, and Bottom of the image as required. Global Blend: The Blend slider, found in every Resolve FX plugin within DaVinci Resolve, sets the effect's opacity, which in practice governs how opaque the foreground layer is.

### Stabilizing

Despite the name, the Stabilizing controls have nothing to do with match moving; rather, they let you repurpose the motion tracking produced via the Tracking Controls to steady the image. An Edge Behavior pop-up menu determines how to deal with the blanking that appears around the edges when the background image is transformed to hold the frame's subject in position.

Controls revealed once Main Controls is switched to Stabilizing

### Surface Tracker (Studio Version Only)

The Surface Tracker serves to lay textures and effects onto pliable or deformable moving surfaces such as cloth and skin. It makes certain that the way the texture or effect folds and deforms convincingly tracks the folding and deforming of the surface it's pinned to within the image. As a sophisticated effect, the Surface tracker carries a wide array of options and controls aimed at producing the most lifelike composites achievable. In every case, though, you simply proceed left to right across the buttons sitting in the effect's settings. 1 Press the Bounds button, then click on the screen to mark out the surface region where the fresh texture should go. The bounds ought to cover a single surface at a time and steer clear of crossing or sitting on object edges. 2 Press the Mesh button to set the control points that follow the surface's natural folds and curves inside the bounds. 3 Press the Track button so the surface's motion gets analyzed over time, drawing on the Mesh you just laid out. 4 Press the Result button to lay the texture over the top of the moving Mesh. The advice is to run the Surface Tracker as its own FX Node, dragged straight from the effects library into the node tree, instead of attaching it to an ordinary corrector node. Doing so gives you an extra Alpha input for laying down textures that carry some built-in transparency. On each of the Surface Tracker's tabs, the Tracked Range reports the first and last frame numbers of your clip that hold tracking data. Altering the bounds or the mesh layout clears any tracking data already present, and you'll have to track it again.

(Left) The Surface Tracker at work, laying the logo on, and (Right) bending and matching it convincingly to the shirt's folds.

### Bounds

Here is where you're asked to outline a region on the image onto which the texture should go. The best choice is a clip frame in which the surface you intend to track sits as near to the camera and as flat-on as it can. That frame then serves as the effect's default reference frame. To use the tool, confirm the Open FX Overlay controls are switched on in the Viewer. Just click around the image to drop several points enclosing the region you're defining (three points at minimum), and the effect joins them into a polygon for you automatically. Place boundary points on the surface being tracked, not surrounding it. Dropping points on object edges or the background by mistake will introduce tracking errors.

The same image can carry several boundaries and several holes; every boundary merges into a single shape first, and then the holes are subtracted from it. Multiple boundaries and holes exist so you can mask off intricate surfaces, leaving out regions you don't want tracked. You might, for instance, draw a boundary around a person's face while using several holes to leave out the eyes and mouth, since those shift appearance rapidly as the subject blinks and speaks and are therefore extremely hard to track. Multiple boundaries are meant for one shared surface; applying them across different surfaces in the image produces poor results. To track distinct surfaces, it's better to use several instances of the Surface Tracker. The boundary isn't meant for rotoscoping objects, only for studying a surface's motion. For rotoscoping foreground objects, see the discussion in the Tracking Using a Mask section further down. Click to Add Points: These controls are what you use to form boundary regions on the image.

- Boundary: The boundary region presently selected on the image. The drop-down menu switches which boundary or hole is current. Where a boundary has problems (such as crossed edges, too few points, and so on), an error message shows up beside its name.
- - Bound: Drops a boundary polygon onto the image. Several boundaries can be set for one surface, and they get merged into a single shape.
- - Hole: Introduces a region that's left out of tracking on the surface. It's used to strip overly intricate, shifting portions of a surface out of the effect's calculations.
- Delete: Removes whichever boundary or hole is selected in the Boundary field. At present this action can't be undone, so treat the button with care.
- Clear All: Wipes out every boundary and hole in the effect.

### Mesh

Once the boundaries exist, you go on to lay the mesh across the surface that's to be tracked. Because the starting mesh is what tracking builds from, you'll get the best outcome by placing it while your surface is as flat-on and as close to the camera as it gets. You tweak the mesh by hand, dragging existing points (hold command and drag a box around several points to move them together) or clicking somewhere to drop new ones. Option-clicking a point deletes it from the mesh. Hand-placing mesh points helps when the surface has flexible spots known to fold the texture but not picked up when the mesh first goes down. An outstretched arm, say, might lack an active mesh point at the elbow, yet a mouse click (paired with a little grasp of human anatomy) lets you add one there. Another scenario is seeding points in a low-detail region that you anticipate will gain detail as it turns into view. Dropping mesh points into flat, detail-poor areas won't help results and can in fact worsen them, so keeping points sparse on smooth areas is preferable. As a rough guideline, once more than five points sit inside the boundaries, the mesh is probably solid enough to track. Points can't be added or removed once tracking is done. Since they go hand in hand, a good mesh signals good tracking. When your mesh registers few points and the results fail to track tightly, you can boost your results deliberately. For instance, make sure the content is plainly visible. Tracking and point detection can break down if the surface is overly bright (HDR), overly dark, or low in contrast from working in log. To get better results, place a corrector node ahead of the Surface Tracker to set contrast and levels by hand, then run the Surface Tracker. You could

likewise put a corrector node carrying the Contrast Pop effect ahead of the Surface Tracker to assist with tracking surfaces that are too smooth. Either way, just switch the corrector node off again once tracking has wrapped up.

- Regenerate Mesh: Clicking this rebuilds the mesh using the current frame and settings, throwing away whatever manual edits were made.
- Point Locations: These controls set which mode produces the mesh points.

Automatic: On its own, the Surface Tracker finds the best details for tracking and drops mesh points onto them. Automatic yields the best results in most situations.

- Point Number Limit: Sets the ceiling on how many mesh points get placed. How the overlay flexes and folds depends on the mesh point count, which you should match to how flexible you expect the surface to be. They have no direct bearing on tracking speed.
- Minimum Point Spacing: Sets the smallest allowed gap between mesh points. It keeps mesh points from clustering too densely in highly detailed regions and getting in each other's way.
- Uniform Grid: Lays down an even grid of points within the boundary and leans on internal shape models to warp that grid as tracking proceeds. On a highly detailed surface this can outperform Automatic mode.

Horizontal Spacing: Tunes the horizontal gap separating neighboring points in the uniform mesh. Vertical Spacing: Tunes the vertical gap separating neighboring points in the uniform mesh.

### Track

In this part of the effect, the motion of the mesh points is tracked across time. The Tracking Direction controls let you run the tracking procedure through the clip. Once tracking finishes, the effect performs no further analysis, and you can throw away any extra contrast help from upstream nodes after this step. Straightforward cases may track all the way through with no user involvement, while trickier ones call on several extra controls to refine the track. Repairing a broken track means making some manual tweaks to both the mesh and the tracking data. Whenever tracking is underway, you can adjust mesh points individually or with the lasso selection tool (Command - Drag) drawn around the whole mesh or only portions of it. That lasso selection tool can also stretch, scale, and rotate the mesh points, so it's simpler to deform the mesh by hand and set it precisely where you want should the automatic tracking fall short for some reason. That said, you can't add or delete extra mesh points at this point without first resetting the tracking.

Command-Drag lets you lasso a group of mesh points and then scale, rotate, and stretch them however you need.

Hand-editing the mesh points at one frame changes only that frame directly and leaves the adjacent tracking data alone. It does, though, alter adjacent interpolated positions, which makes it useful for tracking from that frame forward. For example:

- The track holds up through frame 150, where a handful of points break away from the others because of a lighting shift. Those points can be dragged back into place at frame 150, and if you then resume tracking, they carry on from their corrected positions.
- Tracking runs to frame 150, then has no data for a few frames until it picks back up at 160. Editing the points at either frame 150 or frame 160 makes the frames in between interpolate with those edits factored in.
- Tracking covers up to frame 150 and again from frame 160 on, leaving frames 151-159 interpolated. Some points get adjusted at frame 155. That generates tracking data at that frame, so now frames 151‑154 interpolate from the last tracked frame to this one, and frames 156-159 interpolate from this one to the next tracked frame.

Suppose something in the frame covers the tracked surface — say you're tracking a mesh on a shirt and the person's arm sweeps down through the mesh, breaking the track. An Alpha channel may let you resolve this, as the Tracking Using a Mask section below explains. Tracking data also appears as keyframes within the Keyframe Editor under the FX node's Surface Tracker keyframing data, and it's reachable too as the bottommost control in the Track section, where data at a frame can be made or removed directly.

- Go to Start: Pressing this jumps the playhead to the earliest tracked frame, or to the frame on which the boundary was made.
- Go To End: Pressing this jumps the playhead to the latest tracked frame.
- Tracking Direction Controls: These controls run the tracking analysis in whichever direction

is shown. Reading left to right, they run: Track Backwards, then Track Backward One Frame, next Pause Tracking, after that Track Forwards Then Reverse, followed by Track Forwards One Frame, and lastly Track Forwards. With them you can lay the track over the entire clip or restrict tracking to only a portion of it.

- Tracking Data Controls: These controls let you work with the track data once it has been generated.

Remove Tracking Data Before This Frame: Wipes every bit of tracking data that sits earlier than the current frame. Track From Last Known Match: Pressing this lines up the tracking data with the current frame and links it back to the most recent frame that still holds tracking data. Where too much movement separates those two moments, you can nudge the points roughly where they belong and attempt the match once more. Say tracking runs cleanly through to frame 150, but an object crossing the scene throws the track off for six frames (151-157). You can halt the tracking data before those frames arrive, or strip out their tracking data afterward. Then, at frame 158, pressing this button picks the track back up from the last solid track at frame 150. Remove Tracking Data At This Frame: Wipes the tracking data sitting on the current frame. Remove Tracking Data After This Frame: Wipes every bit of tracking data that comes later than the current frame.

- Interaction Overlays: These buttons govern whether the mesh overlays appear on the Viewer.

Show: Keeps the mesh visible the whole time. Hide on Drag: Keeps the mesh visible until you drag a point, at which moment it vanishes so you can study the surface beneath while making fine tweaks. Hide: Keeps the mesh out of sight the whole time.

- Tracking Behavior: These options give you a say in how the tracking behaves.

Motion Range: Decides how broad a region is searched for matches. Push this slider up when the surface travels too fast and the tracking can't lock onto it.

Mesh Rigidity: Decides how supple the mesh stays. Pull this slider down to loosen the mesh points. You'll see the best results when the clip is free of noise and warps smoothly. Push this slider up for a “stiffer” tracked surface that warps less internally. Quality: The tracker can really tax your processor; the advice is to stay on the Faster setting while you tweak the mesh, then switch to Better for the finished track after every parameter is dialed in right. Tracking Keyframes: Drives the Surface Tracker from within the standard Keyframe Editor. This option lets you add, remove, and move between the various keyframes. NOTE: The Surface Tracker lays down data on every frame of the source clip. Should the source clip's frame rate differ from the timeline's, tracking can look like it stutters or drops frames. You can “bake” the retiming into a clip by right-clicking it on the Edit page and picking “Render In Place,” which yields a result holding precisely one frame per timeline frame.
