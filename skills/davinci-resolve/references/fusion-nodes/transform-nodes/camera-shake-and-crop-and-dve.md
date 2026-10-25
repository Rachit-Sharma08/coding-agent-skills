# Camera shake and crop and dve

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera shake, Crop, Dve.
[Chapter index](INDEX.md) / [Previous section](camera-shake-controls.md) / [Next section](dve-and-letterbox.md) / [Camera Shake CSh](camera-shake-controls.md)
<a id="source-auto-crop-tab"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-crop-crp"></a> <a id="source-crop-node-introduction"></a> <a id="source-dve-dve"></a> <a id="source-dve-node-introduction"></a> <a id="source-example"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-the-auto-crop-tab"></a> <a id="source-the-crop-controls-tab"></a> <a id="source-the-crop-node"></a> <a id="source-the-dve-node"></a>

### Example

Resize filters. Reading across, the samples run Nearest Neighbor, then Box, Linear, Quadratic, and Cubic, followed by Catmull-Rom and Gaussian, then Mitchell, Lanczos, Sinc, plus Bessel.

Edges This menu decides how the image's Edges are dealt with.

- Canvas: Makes the edges uncovered by the shake take on the canvas color—typically transparent or black.
- Wrap: Wraps the edges around, so the top carries over to the bottom, the left over to the right, and so forth.
- Duplicate: Repeats the Edges, which leaves a faint smearing at the borders.
- Mirror: Pixels from the image are mirrored outward to reach the frame edge.

Invert Transform Turn this control on to Invert whatever position, rotation, or scaling transformation is present. It comes in handy when you need to precisely undo motion that an upstream Camera Shake introduced. Flatten Transform Switching on the Flatten Transform option stops this node from merging its transformation with the nodes beside it. Transforms arriving from its input may still be concatenated, but its own transformation will not combine with whatever node sits at its output.

### Common Controls

Settings Tab Other Transform nodes carry a copy of the same Settings tab found here in the Inspector. You will find a full account of these shared controls under the “The Common Controls” section at this chapter's close.

### Crop [Crp]

### The Crop node

### Crop Node Introduction

With the Crop node you can carve out a section of an image, or shift the image inside a bigger image area. Note, though, that—unlike a mask—this node genuinely alters the image's resolution. TIP: To crop directly in the viewer, switch on Allow Box Selection at the viewer's upper-left corner while the Crop node is both selected and being viewed. Then drag out a crop rectangle over the region you care about to carry out the crop. NOTE: Since this node alters the image's physical resolution, animating the parameters is discouraged.

### Inputs

A 2D image to be cropped wires into the Crop node's lone input. Input: The primary 2D image you intend to crop attaches to the orange input.

### Basic Node Setup

In the layout below, the Crop node sits between the MediaIn1 node and the Merge's background input. In contrast to a mask tool, cropping the MediaIn1 alters the clip's resolution. Because the cropped MediaIn1 node feeds the orange background input, it also dictates the resolution of the Merge output.

Use the Crop node to carve out a section of an image.

### Inspector

### The Crop Controls tab

### Controls Tab

For cropping the image, the Controls tab offers both XY Offset and XY Size methods. Offset X and Y These controls slide the image off-screen by nudging it left/right or up/down. Whatever is cropped vanishes past the borders of the output image. These control values are expressed in pixels. Size X and Y Reach for these controls to define the vertical and horizontal resolution of the image the Crop node outputs. These control values are expressed in pixels.

Keep Aspect Switched on, the Crop node holds onto the aspect of the input image. Keep Centered Switched on, the Crop node automatically nudges the X and Y Offset controls so the image stays centered. With the XY Offset sliders driven automatically, you steer the cropping through the Size sliders or via the Allow Box Selection button in the viewer. Reset Size This returns the image dimensions to match the input image's size. Reset Offset This returns the X and Y Offsets to their defaults. Change Pixel Aspect Tick this checkbox to expose a Pixel Aspect control, which lets you alter the image’s pixel aspect. Clipping Mode This option picks the method used to deal with the image edges during domain of definition (DoD) rendering. It matters a great deal for nodes such as Blur, which can need samples drawn from areas of the image beyond the current domain.

- Frame: Frame is the default; it forces the node’s domain of definition to span the image's full frame, in effect disregarding the present domain of definition. Should the upstream DoD fall short of the frame, whatever frame area is left over gets handled as black/transparent.
- Domain: Choosing Domain makes the node honor the upstream DoD as it applies its effect. Where the node relies on a large filter, this can produce unwanted clipping.
- None: Picking None skips source-image clipping entirely. As a result, any data the node’s effect needs that would ordinarily fall beyond the upstream DoD gets handled as black/transparent.

### Auto Crop Tab

The Auto Crop tab inspects the chosen channel and crops the image according to that channel’s edges. Whatever auto crop arrives at then shows up over in the Crop tab parameters.

### The Auto Crop tab

RGBA Color Channels Pick which channels get inspected during an Auto Crop. This helps when auto cropping images whose backgrounds are not solid in a given color channel, such as a blue color gradient. Switching a channel off tells Auto Crop to skip it while assessing the image. Auto Crop This examines the image and tries to work out the background color, then trims each edge of the image inward to the first pixel that differs from that color.

### Common Controls

Settings Tab Other Transform nodes carry a copy of the same Settings tab found here in the Inspector. You will find a full account of these shared controls under the “The Common Controls” section at this chapter's close.

### DVE [DVE]

### The DVE node

### DVE Node Introduction

A 3D-image transformation, the DVE (Digital Video Effects) node mirrors the kind of nodes that lived in the old tape-based online editing suites. Image rotations, perspective shifts, and Z moves all fall within its scope. Every transformation lets you specify its axis.

### Inputs

A 2D image, a DVE mask, and an effect mask all attach to the DVE node's three inputs, with the effect mask available to confine where the DVE acts. Input: The primary 2D image the DVE transforms feeds the orange input. DVE Mask: The white DVE mask input masks the image ahead of the DVE transform being carried out, which alters both the image and the mask together. Effect Mask: A mask shape—made from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools—feeds the blue input. Wiring a mask here makes the DVE alter only the portion of the image inside the mask. The tool finishes processing first, and only then is an effects mask applied to it.
