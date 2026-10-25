# New eye and splitter

Version: DaVinci Resolve 20.3 Reference Manual. Context: New eye, Splitter.
[Chapter index](INDEX.md) / [Previous section](disparity-to-z-and-global-align-and-new-eye.md) / [Next section](splitter-and-stereo-align.md) / [New Eye NE](disparity-to-z-and-global-align-and-new-eye.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-outputs-1"></a> <a id="source-outputs-2"></a> <a id="source-splitter-node-introduction"></a> <a id="source-splitter-spl"></a> <a id="source-the-new-eye-controls-tab"></a> <a id="source-the-splitter-node"></a>

### Inputs

You wire the left and right images into the two inputs on the New Eye node. Left Input: Either the left eye image or the stack image hooks into the orange input. Right Input: The right eye image hooks into the green input. That input appears only while the Stack Mode menu is set to Separate.

### Outputs

Differing from most Fusion nodes, New Eye carries two outputs, one per eye. Left Output: This puts out the left eye image bearing a new disparity channel, or a Stacked Mode image bearing a new disparity channel. Right Output: This puts out the right eye image bearing a new disparity channel. You'll see that output only if Stack Mode sits on Separate.

### Basic Node Setup

In the example that follows, the New Eye node builds a fresh image by interpolating across the two stereo images using their embedded disparity channels.

A New Eye node builds a fresh stereo image out of embedded disparity Inspector

### The New Eye Controls tab

### Controls Tab

Identical sets of parameters for the left eye and the right eye divide up the Controls tab. With these parameters you pick which eye to rebuild and the methods the interpolation uses. Enable The Enable checkbox lets you turn the left or right eye on by itself. Whichever eye is enabled gets swapped by New Eye for an interpolated one. Say the left eye is your "master" and you're rebuilding the right eye: you'd switch the left eye off and the right eye on.

Lock XY Holds the X and Y interpolation parameters together. Unlock them and you may feed separate interpolation factors that draw on the X and Y disparity. For instance, working on the right eye with the X Interpolation slider at 1.0 and the Y Interpolation slider at -1.0 effectively maps the left eye onto the right eye while keeping it vertically aligned to the left eye. XY Interpolation Factor Interpolation sets where the interpolated frame lands relative to the two source frames: a slider sitting at -1.0 yields the frame Left, while one at 1.0 yields the frame Right. At 0.0 the slider yields a result midway between Left and Right. Depth Ordering Depth Ordering decides which portions of the image render on top. Warping images frequently produces overlap. Where the image overlaps itself, two choices govern which values draw on top.

- Largest Disparity On Top: Within the overlapping sections, the bigger disparity values are what render in front.
- Smallest Disparity On Top: Within the overlapping sections, the lesser disparity values are what render in front.

Clamp Edges In some situations this option clears away the transparent gaps that can show up along the edges of interpolated frames. Clamp Edges brings a stretching artifact to the frame's edges, most noticeable as objects pass through it or as the camera moves. Given those artifacts, it's wise to reach for Clamp Edges only to patch small gaps around an interpolated frame's borders. Softness Cuts down the stretchy artifacts that Clamp Edges might bring in. With more than one of the Source Frame and Warp Direction checkboxes switched on, the stretching effect near the edges can double up. There, hold softness fairly low, somewhere near 0.01. With just one checkbox on, a bigger softness of about 0.03 works. Source Frame and Warp Direction This node's output comes from blending as many as four separate warps. You may draw on the color values from the left or right frame paired with the Forward (left > right) Disparity or the Backward (right > left) Disparity. At times you'll want to replace an eye that already exists. To regenerate the right eye, for example, you'd rely solely on left eye warps. Trying out the various options to find which looks best is worthwhile. Drawing on both the left and right eyes can plug gaps along the left/right side of images. Drawing on both the Forward/Backward Disparity can produce a doubling-up effect wherever the disparities clash.

- Left Forward: Grabs the Left frame, then interpolates the new frame via the Forward Disparity.
- Right Forward: Grabs the Right frame, then interpolates the new frame via the Forward

Disparity.

- Left Backward: Grabs the Left frame, then interpolates the new frame via the Back Disparity.
- Right Backward: Grabs the Right frame, then interpolates the new frame via the Back Disparity.

### Common Controls

Settings Tab On the other Stereo nodes too, this Inspector Settings tab is reproduced. Detailed coverage of these common controls waits at the end of this chapter within the "The Common Controls" section.

### Splitter [Spl]

### The Splitter node

NOTE: The Splitter node ships only with Fusion Studio plus DaVinci Resolve Studio.

### Splitter Node Introduction

A stacked input image—say one the Combiner produced—goes into the Splitter, which then hands back two output images: one left eye and one right eye.

### Inputs

You wire the left and right images into the two inputs on the Splitter node. Left Input: A stacked stereo image hooks into the orange input.

### Outputs

Differing from most Fusion nodes, the Splitter node carries two outputs, one per eye. Left Output: Out of this comes the left eye image. Right Output: Out of this comes the right eye image.

### Basic Node Setup

In the diagram below, a stacked stereo image feeds the input of a Splitter, from which a left and a right eye emerge.

A Splitter node pulls a left and a right image out of one stacked stereo image

Inspector

l The Splitter Controls tab Controls Tab You use the Controls tab to declare the kind of stacked image wired into the node's input. Split Three options for setting the stacked input image's orientation live in the Split menu.

- None: Nothing happens. Both outputs carry an image identical to the one that came in.
- Horiz: The node looks for a horizontally stacked image. The upshot is two output images, each

spanning half the width of the source image.

- Vert: The node looks for a vertically stacked image. The upshot is two output images, each

spanning half the height of the source image. Swap Eyes Lets you flip the left and right eye outputs with ease.
