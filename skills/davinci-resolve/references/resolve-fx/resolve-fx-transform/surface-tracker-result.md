# Surface tracker result

Version: DaVinci Resolve 20.3 Reference Manual. Context: Surface tracker studio version only.
[Chapter index](INDEX.md) / [Previous section](match-move-and-surface-tracker.md) / [Next section](surface-tracker-and-transform.md) / [Surface Tracker (Studio Version Only)](match-move-and-surface-tracker.md)
<a id="source-result"></a> <a id="source-using-the-surface-tracker"></a>

### Result

After the tracking data is finished, the Result section is where you decide what video layer to lay over the moving surface and how to composite it.

- Output: Six choices govern what becomes of the tracking data you've produced.

Warp Input 2 Onto 1: Bends the Surface Tracker's second RGB input to match the tracked mesh's shape and position, then composites it onto the clip. Warp Input 2 Onto Blank: Bends the Surface Tracker's second RGB input to the tracked mesh's shape and position and carries the Alpha channel data through, so you can do the real composite in some other node or effect. Warp Input 1's Alpha: Sends the Surface Tracker's results to the first Key input (the second RGB and Key inputs go unused). When that first Key input gets an Alpha channel from another node — a drawn shape, a key, or other Alpha data — it can be warped from the opening frame across the rest. Create Mesh Alpha Mask: Builds an Alpha mask that traces the position and shape of the mesh outline. Every input and alpha is disregarded. Stabilize-Warp Input 1: Runs an inverse warp toward the Reference Frame (which, again, should ideally sit as close to and as square-on to the camera as you can manage). What you get is a still image inside the boundary that carries all the lighting shifts and detail of the surface's movement. You can then work this now-stabilized image with any of DaVinci Resolve's existing tools, sidestepping whatever trouble this region's motion caused in the original video clip. After you've reworked it, you warp the result back onto the original footage with a copy of the original Surface Tracker node, this time set to the Rewarp Stabilized Clip option. Rewarp Stabilized Clip: Composites the result of the Stabilize-Warp Input 1 choice back onto the original video clip once it's been reworked. This option is meant to pair with a copy of a Surface node running Stabilize-Warp Input 1. It blends whatever extra changes were made between the two Surface Trackers seamlessly back into one.

- Overlay/Alpha Source: Lets you pick which frames of the overlay or alpha go into building the result.

First Frame: Handy for locking content from an overlay clip so a single still serves as a fixed texture. Within DaVinci Resolve's External Matte controls you can dial in the offset, and you can equally use that same frame as the texture reference through Reference Frame.

Reference Frame: Begins from whichever reference frame is set right now (described below) rather than from frame 0. That reference frame is the one where the mesh overlay first sits in its “un-warped” state and the positioning controls are live. Each Frame: Handles the overlay or alpha as a clip, warping every frame one after another. You need this for animated overlays or for re-warping stabilized content. Worth noting: over in the Key controls on the Color page, picking an External Matte brings up options that govern how long the external clip lasts.

- Expand/Contract: Lets you push pixels onto or pull them off the overlay or alpha edges. Keep in mind that the expanded region isn't tracked and won't be stabilized along with the content.
- Softness: Softens the edge produced by the Expand/Contract tool so it sits more believably in the scene.
- Motion Blur: This slider adds motion blur to the overlay to keep up the impression that it was

genuinely shot alongside the scene.

- Overlay Placement: These controls let you dial in the starting transform options for the image you intend

to lay over the mesh. Go To Reference: Jumps the playhead to the chosen reference frame. Set to Current: Marks the frame currently under the playhead as the reference frame. Reference Frame: Reports the frame number where the overlay first sits, positioned and unwarped (the spot from which the warp out to every other frame is figured). The positioning controls show on screen whenever the clip rests on the reference frame. The ideal launch point for rendering onto other frames is a frame where the surface looks biggest and least warped. Positioning: Lets you pick how the overlay position is adjusted.

- Sliders: Picking this option brings up a bank of transform sliders (X/Y position, zoom, rotate, and so on) for shaping the overlay's starting position.
- Interactive Canvas: Picking this option brings up draggable frame controls inside the Viewer so you can transform the overlay with the mouse. The Viewers display a big grid split into 9 regions; drag inside any one to move, skew, or warp the overlay.
- Interactive Pins: In this mode you reshape the image by hand-placing control points, known as pins, in the Timeline Viewer. A single pin grants you position control only. Scaling and rotation call for at least two points. Dragging one of the pins scales or rotates the image about the other pin. With three pins down, you can build perspective distortions by dragging any one of them. Up to four pins can be added for one-of-a-kind corner pinning distortions.

Reset Position: Returns the on-screen overlay to its default state.

- Interaction Overlays: These buttons govern whether the mesh overlays appear on the Viewer. Show: Keeps the mesh visible the whole time. Hide on Drag: Keeps the mesh visible until you drag a point, at which moment it vanishes so you can study the surface beneath for fine tweaks. Hide: Keeps the mesh out of sight the whole time.
- Compositing: Lets you choose the composite blend mode for the overlay operation.

For a fuller rundown of each blend mode, refer to Chapter 50, “Compositing and Transforms in the Timeline.” Composite Type: A pull-down menu carrying every available composite operation. Opacity: This slider governs how transparent the overlay is.

### Using the Surface Tracker

The Surface Tracker is a rich, flexible tool you can call on to convincingly isolate a moving surface for all sorts of effects. The examples that follow will help you begin exploring what it can do. Using the Surface Tracker to Composite a Logo onto a Fabric Surface A frequent job for the Surface Tracker is laying a still graphic over a moving surface so the graphic acts believably as that surface bends and warps. Here, we'll stick a simple logo onto the back of a jacket. Step one is marking out the boundary for the region we want analyzed. To get the best outcome, lay the boundary on the surface you mean to track rather than around it, and look for a frame where the surface faces the camera squarely and fills as much of the frame as it can. Step two is laying out the Mesh inside the surface we want warped. Here we'll leave the Point Locations setting on Automatic so the effect drops in the mesh points itself. You ideally want more than five mesh points for a solid track. As luck would have it this surface lacks the detail for a good mesh, so we'll briefly drop a Contrast Pop node ahead of the Surface Tracker to artificially boost its detail.

Drawing the first boundary so the jacket region that will carry the logo is isolated

Dropping the Contrast Pop FX ahead of the Surface Tracker input lets us artificially bump up the detail within the boundary, handing it a stronger surface from which to build the mesh.

Next we'll track the Mesh's motion with the Track Forward button, leaving every other control at its default. Notice the track keeps warping and folding right, even as the subject reclines in his chair. The Tracker studies the Mesh movement across the remainder of the video clip. Now that the surface is properly analyzed, the Contrast Pop node is no longer needed, so we can unplug it here. After that we'll drag the logo (a .png file carrying transparency) out of the Media Pool and into the node tree, where it arrives as a matte. We then place a corrector node after the matte so we can tweak the logo's color/saturation/brightness, and the like. Next we route each node's RGB and Key links onward, passing through the matte and corrector nodes, then on into the Surface Tracker's second RGB and Key inputs. The node tree below illustrates it:

The node tree, laying out how the RGB and Key inputs are wired so the logo composites over the jacket Moving on to the Result section now, we dial in this parameter:

- Output: Warp Input 2 onto 1 This grabs the second RGB and Key input (the logo) and bends it across the original image arriving at RGB input 1.

We'll then press the Go To Reference button to send the clip to its reference frame, and within Positioning we'll use the Interactive - Canvas tool to reframe the logo so it sits on the same plane as the jacket.

Reshaping the logo within Interactive Canvas mode so that it reads as though it sits on the jacket's plane As a final move, we shift the Composite Type from Normal across to Overlay so the logo melds more naturally into the jacket's surface. See how the mesh deforms the logo so it hugs the jacket's curves and folds and follows the man as he reclines in his chair.

The completed Surface Tracker composite; the logo clings to every curve and fold of the jacket and rides along with the man as he repositions himself in the chair.
