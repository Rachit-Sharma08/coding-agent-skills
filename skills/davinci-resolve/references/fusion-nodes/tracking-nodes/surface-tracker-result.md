# Surface tracker result

Version: DaVinci Resolve 20.3 Reference Manual. Context: Surface tracker.
[Chapter index](INDEX.md) / [Previous section](surface-tracker-mesh.md) / [Next section](tracker-a-tracker-node-branched-from-the-node-tree.md) / [Surface Tracker SFt](planar-tracker-node-and-surface-tracker.md)
<a id="source-result"></a> <a id="source-the-result-tab-in-the-surface-tracker-controls"></a>

### Result

After the tracking data is finished, the Result section is where you decide what video layer to lay over the moving surface and how to composite it.

### The Result tab in the Surface Tracker controls

Output: Six choices govern what becomes of the tracking data you’ve produced.

- Warp Input 2 Onto 1: Bends the Surface Tracker’s overlay input to match the tracked mesh’s shape and position, then composites it onto the clip.
- Warp Input 2 Onto Blank: Bends the Surface Tracker’s overlay input to match the tracked mesh’s shape and position while carrying through the Alpha channel information, so you can do the real composite over in another node or effect.
- Warp Input 1’s Alpha: Feeds the Surface Tracker’s results into the Effect Mask input.
- Create Mesh Alpha Mask: Builds an Alpha mask that traces the position and shape of the mesh outline. Every input and alpha is disregarded.
- Stabilize-Warp Input 1: Applies an inverse warp toward the Reference Frame (which, once more, should ideally be a frame as close to and as square-on to the camera as you can get). What you get is a still image inside the boundary that nonetheless carries all the lighting shifts and surface-motion detail painted onto it. With the image now stabilized, any of DaVinci Resolve’s existing tools can modify it, sidestepping whatever trouble this region’s motion caused in the original video clip. After modifying it, you warp the result back onto the original footage using a duplicate of the original Surface Tracker node, this time set to Rewarp Stabilized Clip instead.
- Rewarp Stabilized Clip: Takes whatever the Stabilize-Warp Input 1 selection produced and, after it’s been modified, lays that result back over the source footage. This choice is meant to pair with a duplicate of a Surface node running Stabilize-Warp Input 1. It cleanly merges whatever extra modifications were introduced between the two Surface Trackers.

Overlay/Alpha Source: Lets you pick which frames of the overlay or alpha feed into the result.

- First Frame: Handy for locking content from an overlay clip so a single still frame serves as a static texture.
- Reference Frame: Begins at whatever reference frame is currently set (see below) rather than at frame

0. That reference frame is the one on which the mesh overlay first sits in its “un-warped” state, with the positioning controls live.

- Each Frame: Handles the overlay or alpha like a clip, warping every frame one after another. You’ll need this for animated overlays or for re-warping stabilized content.

Contract/Expand: Lets you tack on or strip away pixels at the overlay or alpha edges. Keep in mind that the expanded region isn’t tracked and won’t be stabilized to the content. Softness: Softens the boundary of the Expand/Contract tool so it folds more convincingly into the scene. Motion Blur: This slider adds motion blur to the overlay, sustaining the impression that it was truly shot alongside the scene. Overlay Placement: These controls set the starting transform options for whatever image you mean to lay over the mesh.

- Go To Reference: Sends the playhead to the chosen reference frame.
- Set to Current: Marks the frame currently under the playhead as the reference frame.
- Reference Frame: Reports the frame number where the overlay originally rests, unwarped (the basis from which the warp to all other frames is computed). The positioning controls show up on screen whenever the clip sits on the reference frame. The ideal launch point for rendering onto other frames is a frame where the surface appears largest and least distorted.
- Positioning: Lets you pick the way you adjust the overlay’s position.

Sliders: Selecting this brings up a row of transform sliders (X/Y position, zoom, rotate, and so on) for tweaking the overlay’s starting position. Interactive Canvas: Selecting this brings up draggable frame controls in the Viewer, so you transform the overlay with mouse gestures. The Viewer presents a large grid split into 9 regions; dragging within any one moves, skews, or warps the overlay. Interactive Pins: Reshaping the image in this mode means placing control points by hand, known as pins, in the Timeline Viewer. A single pin grants position control alone. Scaling and rotation call for two points at minimum. Dragging one pin scales or rotates the image about the other pin. With three pins, dragging any of them yields perspective distortions. You can go up to four pins for distinctive corner pinning distortions.

- Reset Position: Returns the on-screen overlay to its default state.

Interaction Overlays: This set of buttons decides whether the mesh overlays are shown in the Viewer.

- Show: Displays the mesh continuously.
- Hide on Drag: Keeps the mesh on screen until you drag a point, whereupon it disappears so you can view the underlying surface while fine-tuning.
- Hide: Suppresses the mesh continuously.

Compositing: Lets you pick the composite blend mode for the overlay operation.

- Composite Type: A drop-down listing every available composite operation.
- Opacity: This slider sets how transparent the overlay is.

For a fuller account of each blend mode, refer to Chapter 50, "Compositing and Transforms in the Timeline."

In the finished surface track, the bee graphic is composited onto his shirt. Screen served as the composite type, with opacity lowered so it blends into the fabric. As the shirt folds and deforms during play, the bee follows along convincingly.
