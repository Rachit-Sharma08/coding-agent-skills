# Planar tracker node steady mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Planar tracker node.
[Chapter index](INDEX.md) / [Previous section](planar-tracker-node-controls.md) / [Next section](planar-tracker-node-and-surface-tracker.md) / [Planar Tracker Node PTRA](planar-tracker-node-what-the-planar-tracker-saves.md)
<a id="source-corner-pin-mode"></a> <a id="source-merge-mode"></a> <a id="source-stabilize-mode"></a> <a id="source-steady-mode"></a>

### Steady Mode

With Steady mode, the Planar Tracker warps the background plate so as to hold the pattern as still as it can. Whatever motion remains stems from the Planar Tracker not tracking the pattern precisely, or from the pattern not sitting on a genuinely planar surface. Steady mode does little for real stabilization, yet it works well for gauging a track's quality. When the track is solid, the pattern stays put during playback while the surrounding background plate warps around it. A useful check is to zoom into portions of the pattern, hover the mouse cursor over a feature, and watch how far that feature wanders from the cursor across time. Steady Time This is the moment at which the pattern's position is captured and pinned in place. Setting it to the reference frame is the usual choice. Invert Steady Transform This makes the Planar Tracker node undo what the steady transform did. So two Planar Tracker nodes chained one after another, with the second set to invert, ought to return the original image. Drop an effects node between the pair and the effect becomes locked in place. Reserve this for effects that corner pinning cannot achieve, since the two resamplings involved soften the background image. Clipping Mode Decides what becomes of the parts of the background image pushed off frame by the steady transform:

- Domain: The off frame parts are kept.
- Frame: The off frames parts are thrown away.

Domain mode pays off when Steady mode is being used to "lock" an effect onto the pattern. Picture, for instance, painting onto the license plate of a car in motion. One approach steadies the license plate with a Planar Tracker node, paints over it via a Paint node, and finally reverses the steady transform using a second Planar Tracker. With the Clipping mode at Domain, the off frame parts the first Planar Tracker produced are retained, letting the second Planar Tracker map them back into the frame.

### Corner Pin Mode

With Corner Pin mode, one or several textures can be pinned to a planar surface that was tracked earlier and made to take on the surface's perspective distortions. Here is the Planar Tracker corner pin workflow: 1 Track: pick a planar surface in the shot where you want to add a texture or swap an existing one. Track the shot, following the Track section's description of the tracking workflow. 2 Set the Operation Mode to Corner Pin: Moving into Corner Pin mode from Track mode hides the pattern polygon and puts a corner pin control in the viewer. 3 Connect in the texture: Within the Node Editor, route the output of the MediaIn node holding the texture into the Planar Tracker node's Corner Pin 1 input. 4 Adjust corner pin: Within the viewer, drag the corner pin's corners until the texture lands correctly. The Show Grid option is sometimes handy while placing the texture. For finer placement, you can also scrub to other times and tweak the corner pin there. 5 Review: Play the footage back and confirm the texture "sticks" to the planar surface.

### Merge Mode

Governs the way the foreground (the corner pinned texture) composites over the background (the tracked footage). When several corner pins exist, they all share this single option. Four choices are offered:

- BG only
- FG only
- FG over BG
- BG over FG

Number of Corner Pins The + and - buttons raise or lower how many corner pins there are. Every time you add another corner pin, a matching input shows up on the node within the Node Editor. Corner Pin 1 Input Group A set of related inputs belongs to each corner pin:

- Enable: Sets whether the corner pin is shown in the viewer.
- Show Grid: Overlays a grid on the corner pin, which helps while placing the corners.
- Merge Options: Governs how the corner pin texture composites over the background. (Refer to the

Merge node's documentation.)

- Reference Time Positions: Where the four corners sit at the reference time. Should the track fall

short of perfect, these positions can be animated to layer adjustments on top of the track.

### Stabilize Mode

Stabilize mode evens out camera shakiness by applying a transform that partly cancels the camera shake. That stabilizing transform (held in the Stable Track spline) is worked out by comparing neighboring frames. NOTE: Where Steady mode aims to "lock off" all motion entirely, Stabilize mode merely smooths motions. Keep in mind that the Planar Tracker stabilizes off the pattern's motion, so picking the pattern with care is essential. When the pattern's motion fails to stand in for the camera's, the results can be surprising. As an example, tracking the flank of a moving truck while the camera travels alongside it leads the Planar Tracker to smooth the combined motion of both the truck and the camera mounted to it. Sometimes that is not what you want. A better pick may be a stationary object such as the road or a building's side, which leaves only the camera's motion smoothed. An unavoidable byproduct of stabilization is that transparent edges show up along the borders of the image. They appear because the stabilizer knows nothing of what sits off frame, so it cannot fill in the absent pieces. The Planar Tracker node lets you either crop or zoom these edges away. While shooting, if post-production stabilization seems likely to be needed, filming at a higher resolution (or a lower zoom) can occasionally help.

The Planar Tracker Stabilization Workflow 1 Track: Choose a broadly planar region that stands for the motion you mean to stabilize. Track the shot, following the Track section's description of the tracking workflow. 2 Set the Operation Mode to Stabilize: Up until a stabilization is calculated, the Planar Tracker simply passes the input footage through. 3 Adjust stabilization options: The options most often altered are Parameters to Smooth and Smoothing Radius. 4 Compute stabilization: Click the Compute Stabilization button and let the stabilization calculations run to completion. Play back the Planar Tracker node's output to view what the stabilization did. Note that the stabilization transform has brought transparent edges in around the image's borders. 5 Refine: Tune the stabilization options and recompute as many times as you like. 6 Handle transparent edges (optional): Choose Zoom or Crop for the Frame Mode as you prefer, then click the Auto Zoom or Auto Crop button. Play the footage back to see the result. Should there be excessive zoom, or the image be cropped too tight, try dialing back the amount of smoothing.
