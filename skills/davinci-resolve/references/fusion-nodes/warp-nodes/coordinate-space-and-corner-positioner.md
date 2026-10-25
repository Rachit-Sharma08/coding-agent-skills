# Coordinate space and corner positioner

Version: DaVinci Resolve 20.3 Reference Manual. Context: Coordinate space, Corner positioner.
[Chapter index](INDEX.md) / [Next section](dent-and-displace-and-drip.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-coordinate-space-cds"></a> <a id="source-coordinate-space-node-introduction"></a> <a id="source-corner-positioner-cpn"></a> <a id="source-corner-positioner-node-introduction"></a> <a id="source-example"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-the-coordinate-space-controls-tab"></a> <a id="source-the-coordinate-space-node"></a> <a id="source-the-corner-positioner-controls-tab"></a> <a id="source-the-corner-positioner-node"></a> <a id="source-warp-nodes"></a> <a id="source-warp-nodes-part-1"></a>

### Warp Nodes

This chapter walks through the Warp nodes that Fusion offers. The short codes printed beside each node's name come in handy within the Select Tool dialog while you're hunting for tools, and they show up in scripting references too. Throughout this document, node trees depicting MediaIn nodes in DaVinci Resolve can be swapped one-for-one with Loader nodes in Fusion Studio, except where a note says otherwise.

### Coordinate Space [CdS]

### The Coordinate Space node

### Coordinate Space Node Introduction

What the Coordinate Space node does is convert the image's coordinate space, going either from rectangular over to polar or back from polar to rectangular.

### Inputs

On the Coordinate Space node there are two inputs, meant for hooking up a 2D image plus an effect mask, the latter letting you confine where the distortion lands. Input: For the main 2D image being distorted, use the orange input. Effect Mask: The blue input takes a mask shape made from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask into this input keeps the distortion bound to the pixels falling inside the mask. The effects mask gets applied to the tool only after the tool itself has been processed.

### Basic Node Setup

In the example below, the Coordinate Space node builds a circular pattern off a Fast Noise, a Mosaic Blur (DaVinci Resolve Resolve FX only), and a Transform node. That Crop node tacked on at the end is there to dial in whatever resolution you want.

The Coordinate Space node can help create motion graphics backgrounds

### Example

Here's how to pull off a simple tunnel effect with this node: 1. Drop in a Text+ node carrying some text, then animate it so it travels along a path running from the frame's top down to its bottom. 2. Route the Text+ node's output into a Coordinate Space node. 3. From the Shape menu, pick Polar to Rectangular. As the text travels top to bottom down its original path, within the Coordinate Space node it seems to approach from an endless distance. You might have to flip the text with a Transform node so it reads the right way once inside the Coordinate Space node. People also frequently pair the Coordinate Space node up: two of them tuned to differing Shape settings with a Drip or Transform node sitting between them. Set up that way, the effect changes while the underlying image stays put.

### Inspector

### The Coordinate Space Controls tab

### Controls Tab

Over in the Controls tab, the Shape menu toggles between Rectangular to Polar and Polar to Rectangular. Work through the following example to see how the two coordinate spaces play out.

### Common Controls

Settings Tab This node's Settings tab in the Inspector also turns up on other Warp nodes. Those shared controls get a thorough treatment at this chapter's close, under the "The Common Controls" section.

### Corner Positioner [CPn]

### The Corner Positioner node

### Corner Positioner Node Introduction

With the Corner Positioner you can interactively place an image's four corners. The usual job for this is swapping out a sign or some other rectangular piece of a scene. For animation, tie all of the corners to Paths or Trackers.

### Inputs

The Corner Positioner node carries two inputs, used for attaching a 2D image alongside an effect mask, where the mask can hem in the warped region. Input: Feed the main 2D image you're warping into the orange input. Effect Mask: A mask shape drawn from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools belongs in the blue input. Hooking a mask up here restricts the Corner Positioner to just the pixels lying within the mask. That effects mask is applied to the tool once the tool has finished processing.

### Basic Node Setup

Down below, the Corner Positioner places the rectangular corners of MediaIn2 so they sit inside a particular region of the MediaIn1 node. A Planar Tracker follows the background, after which a Planar Transform holds the Corner Positioner in place while the background clip travels. With the planar tracking finished and the Planar Transform generated, the Planar Tracker node has served its purpose and can be deleted.

The Corner Positioner corner-pins a clip into position, leaning on a Planar Transform to match-move that clip onto the background.

### Inspector

### The Corner Positioner Controls tab

### Controls Tab

Within the Controls tab you'll find transform and offset settings covering the image's four corners Mapping Type This picks which method projects the image produced by the Corner Positioner. Under Bi-Linear mode, a plain 2D warp occurs. Under Perspective mode, the image is worked out using the offsets in 2D space and then projected into a 3D perspective. Corners X and Y The Corner Positioner holds four points. Drag them about to interactively set each corner of the image. Hook these control points up to any of the customary modifiers. The input image gets deformed and perspective-corrected so it lines up with where the four corners sit. Offset X and Y Use these to nudge the corner positions a little. That comes in handy when the corners are tied to Trackers whose patterns might not land precisely where you need them.

### Common Controls

Settings Tab Like the other Warp nodes, this one repeats the same Settings tab inside the Inspector. You'll find these shared controls explained fully at the end of this chapter, within the "The Common Controls" section.
