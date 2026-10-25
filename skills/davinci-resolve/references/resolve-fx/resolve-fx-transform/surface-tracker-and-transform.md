# Surface tracker and transform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Surface tracker studio version only, Transform.
[Chapter index](INDEX.md) / [Previous section](surface-tracker-result.md) / [Next section](transform-advanced-options.md) / [Surface Tracker (Studio Version Only)](match-move-and-surface-tracker.md)
<a id="source-animation"></a> <a id="source-general"></a> <a id="source-image-adjustment"></a> <a id="source-position-controls"></a> <a id="source-tracking-using-a-mask-in-the-surface-tracker"></a> <a id="source-transform"></a> <a id="source-using-the-surface-trackers-stabilize-warp"></a>

### Tracking Using a Mask in the Surface Tracker

When something blocks the surface you mean to track, an input key can serve as a tracking mask to keep the obstructing object out of the track. Regions of full alpha (pure white) in the Alpha channel get analyzed for tracking, and the rest is left out. Whatever suits — an effect, a window, or a qualifier — can act as the Alpha channel generator. Take the shot below: the path has the surface mesh on it, yet the woman crossing the path disrupts the mesh tracking. Wire up a node's key output that carries a Magic Mask isolating the walking woman's shape, then invert that mask (making the woman black against white surroundings), and the mesh disregards her legs and feet as they cross it, tracking only points in the white regions (everything that isn't the woman).

Trouble tracking the path's surface; while the woman crosses the mesh, its points latch onto her feet rather than the path, which breaks the tracking along the path's right side.

Wiring up an inverted key from a Magic Mask node of the woman alone makes the tracking pass over the woman crossing the mesh (any black region) and track only points within the white portion of the Alpha channel.

The mesh that results now sits properly on the path's right side and tracks correctly while she walks across it.

At the Surface Tracker's last step, the alpha-bearing overlay is composited over the alpha-bearing original clip, so when you've used a tracking mask, the advice is to unplug it from the Surface Tracker's key input once the tracking has finished.

### Using the Surface Tracker's Stabilize Warp

The Surface Tracker's Stabilize Warp operation lets you lean on the mesh to lock a stretch of video in place, making it simpler to pair with certain other operations. It's a help when the surface you're reworking resists isolation by other tools because of how it moves. Setting up the Surface Tracker to stabilize regions plays out a little differently.

- To begin, set up the Surface Tracker's mesh tracking on whatever surface you intend to work on, just as covered earlier in this chapter.
- When that's done, head into the Result section and pick the Output mode named Stabilize-Warp Input 1, then route that RGB output into a fresh corrector or FX node.
- Doing so singles out just the mesh surface and pins it in place so you can make whatever tweaks you need. This approach contrasts with, say, a window qualifier, which clings to the video and travels with it. With Stabilize Warp, the “window” (really the mesh-defined boundary) is the thing held still, while the video shifts and warps inside it.
- Once your tweaks are done, route the corrector node's RGB output back into a precise copy of the first Surface Tracker node. That copied Surface Tracker node's Output then has to be switched to Rewarp Stabilized Clip. This lays the adjusted mesh back down onto the original video clip. Copying an FX node such as the Surface Tracker outright isn't supported right now. To duplicate the Surface Tracker, pull a still into your Gallery, then right-click it and append the still's node graph back into the same clip, removing the surplus duplicate nodes apart from the Surface Tracker.

Take the clip below, where we'll lean on the Surface Tracker to take a small mole off the woman's chin. Ordinarily we could reach for a Patch Replacer FX to drop a clean patch of nearby skin over the mole. This shot is hard to handle well in the Patch Replacer because the subject tilts her head as she speaks while the camera trucks around her. With movement on every axis, the skin beneath the source patch keeps shifting angle and lighting, which wrecks the effect. The patch replacer does offer tracking, but the mole sits on her chin and her talking flexes the skin around her cheek too, leaving it ill-suited to a plain track. Here, we can put the Surface Tracker's Stabilize Warp function to work to “hold” those facial pixels still beneath the source and target patches, patch them, and then build a Rewarp Stabilized Clip version of the Surface Tracker to drop those fixed pixels back onto the original image.

We'd like this mole gone from the woman's chin. Between camera movement and her chin and cheek flexing as she speaks, the Patch Replacer can't manage it on its own. We'll start by building a mesh over her face and tracking it as laid out above. Cutting holes for the eyes and mouth keeps their quick movement from upsetting the mesh on her face.

We lay the mesh over her face and track it, leaving gaps in the mesh at her eyes and mouth. With the tracking finished, in Result we'll pick the Output mode Stabilize-Warp Input 1. That pins the mesh in place and hands us the resulting output, which we'll route into a Patch Replacer node. Now we can just use the Patch replacer statically to cover the mole with another patch of skin. There's no tracking to do. Since the mesh holds still while the video warps inside it, this region now lines up flawlessly with the angles, lighting shifts, and skin stretching of the area as she talks.

The locked mesh holds steady (over the face) while the video bends within it. That lets us run a static Patch Replacer to swap the mole region for a clean patch on her cheek. No further tracking is called for.

From here, we'll make a precise copy of the Surface Tracker node and set it down after the Patch Replacer. To duplicate the Surface Tracker node, pull a still of the current clip, then right-click that still in the Gallery and pick Append Node Graph to bring it back into our node tree. We want to drop whatever surplus nodes got added and keep only the Surface Tracker copy. Then, inside the copied Surface Tracker, we'll pick “Rewarp Stabilized Clip” from the Result tab's Output mode. After that, hook the original clip up to RGB input 1 and feed the Patch Replacer's output into RGB input 2, as the node graph below shows:

The node tree laying out the proper wiring for Warp Stabilizing the mesh. On the first Surface Tracker node, the Result Output reads “Stabilize-Warp Input 1.” On the second Surface Tracker copy, that Result Output instead reads “Rewarp Stabilized Clip.” The actual mole removal takes place inside the Patch Replacer FX node. Our finished effect now shows the mole gone, and no matter how her jaw moves or where the camera sits, the source patch always lines up flawlessly with the lighting and position changes as time passes. The upshot is a far more seamless, convincing effect.

The shot that results conceals the mole flawlessly (above), regardless of how her face is positioned or how the camera moves.

### Transform

The Transform Resolve FX gives you a good deal more command than you get from the basic transforms found in the Inspector's Sizing or in the Color page Sizing palette. It carries all the usual Position, Tilt, Zoom, and Rotate controls but throws in corner pinning, two flavors of on-screen control, motion blur, plus Edge behavior controls.

### General

- Control Mode: This drop-down offers three ways to drive the transforms. One leans on sliders in the Inspector, while the other two work by manipulating the Viewer's image.

Sliders: Drives the transforms with sliders and checkboxes in the Inspector. This route gives you no Viewer overlays for setting position, scale, or rotation, but it does deliver exact control through numeric values. Interactive-Canvas: Picking this mode shifts the controls out of the Inspector and into the Timeline Viewer. The Viewer's controls appear as a bold white outline with four vertices, one per corner. Drag any part of that white outline to stretch, squeeze, and corner-pin. Dragging the image's center repositions the frame. The red subdivision overlays make shearing effects simple — drag line segments to shift two corners at once. Interactive-Pins: In this mode you reshape the image by hand-placing control points, known as pins, in the Timeline Viewer. A single pin grants you position control only. Scaling and rotation call for at least two points. Dragging one of the pins scales or rotates the image about the other pin. With three pins down, you can build perspective distortions by dragging any one of them. Up to four pins can be added for one-of-a-kind corner pinning distortions. TIP: You can Option-Click a pin to delete it, or hit the Reset Canvas button to clear every pin.

Resolve FX Transform Interactive-Canvas mode (Left) alongside Interactive-Pins mode (Right) Just one Control mode can be live at any given moment. You can't, for example, make tweaks with the sliders and then jump to one of the interactive methods. The sliders reset the instant you choose a different method. You can, though, apply two Transform effects to one clip, adjusting one through Sliders and the other through an interactive method.

### Position Controls

- Canvas Keyframe: Shown only while the Control mode sits on Interactive-Canvas or Interactive-Pins. The Canvas Keyframe carries no control beyond a keyframe button that lets you keyframe the changes you make in the Viewer.
- Reset Canvas: Clears any interactive changes made in the Viewer along with any keyframes born from those changes.

The parameters below appear only while the Control Mode is set to Sliders.

- Position X and Y: Slides the image around within the frame for pan and scan tweaks. X carries the image left or right, while Y carries it up or down.
- Zoom: Lets you enlarge the image or shrink it.
- Rotate: Spins the image about its center.
- Width: Stretches or squeezes the image along one direction only.
- Height: Stretches or squeezes the image along one direction only.
- Pitch: Tips the image toward or away from the camera around an axis that runs through the

center of the image left to right. Positive values shove the image's top away and draw its bottom forward. Negative values draw the top forward and shove the bottom away. The bigger the value, the more extreme the stretch.

- Yaw: Tips the image toward or away from the camera around an axis running through the image's center top to bottom. Positive values draw the image's left forward and shove its right away. Negative values shove the left away and draw the right forward. The bigger the value, the more extreme the stretch.
- Flip Horizontal/Vertical: A pair of checkboxes flip the image across different dimensions. Flip Horizontal: Mirrors the image along the X-axis, left to right. Flip Vertical: Mirrors the clip along the Y-axis, flipping it upside down.

### Image Adjustment

- Crop: Ticking this checkbox reveals the crop tools so you can selectively trim parts of the frame off each side.
- Edge Softness: This control sets how much the Alpha channel is feathered for compositing.
- Edge Rounding: This control rounds off the corners of the Alpha channel for compositing.

### Animation

- Motion Blur: Keyframe the transform so the frame travels fast and you'll get a blurring effect. The Motion Blur slider governs how strong the blur is.
