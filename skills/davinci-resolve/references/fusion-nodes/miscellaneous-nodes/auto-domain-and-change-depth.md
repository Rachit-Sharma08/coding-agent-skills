# Auto domain and change depth

Version: DaVinci Resolve 20.3 Reference Manual. Context: Auto domain, Change depth.
[Chapter index](INDEX.md) / [Next section](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md)
<a id="source-auto-domain-adod"></a> <a id="source-auto-domain-node-introduction"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-change-depth-cd"></a> <a id="source-change-depth-node-introduction"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-miscellaneous-nodes"></a> <a id="source-miscellaneous-nodes-part-1"></a> <a id="source-the-auto-domain-controls-tab"></a> <a id="source-the-auto-domain-node"></a> <a id="source-the-change-depth-controls-tab"></a> <a id="source-the-change-depth-node"></a>

### Miscellaneous Nodes

Fusion's assorted nodes are the subject of this chapter.

The shorthand sitting beside each node name works inside the Select Tool dialog while you hunt for tools, and it carries over to scripting references too. Within these pages, node trees that depict MediaIn nodes in DaVinci Resolve may be swapped freely for Loader nodes in Fusion Studio, except where a note states otherwise.

### Auto Domain [ADoD]

### The Auto Domain node

### Auto Domain Node Introduction

Drawing on the bounds of the input image’s background Canvas color, the Auto Domain node fixes the image’s domain of definition (DoD) by itself. The image’s real physical dimensions remain unaltered. A handful of EXR images ship with their DoDs already tuned, while the rest of the formats do not. When you work with formats besides EXR, this node can hasten compositions by tuning the DoD to the actual content rather than to the frame’s dimensions. Take a CG character, which hardly ever fills an image’s whole frame. Faced with that sort of image, the Auto Domain node pins the DoD to a rectangular zone by checking image pixels against the Canvas color. What the Canvas color tells you is the color carried by the pixels that lie beyond the DoD. Where no Canvas color has been established through the Set Canvas Color node, the color falls back to black. Such a default suits an image that carries a premultiplied alpha channel. You wind up with a DoD that surrounds just the slice of the clip holding the character alone. To keep pace with motion, the DoD refreshes every frame, as when a character strolls nearer the camera. Yet should a clip lack an alpha channel, the Set Canvas Color node serves to set the Canvas color as solid alpha tinted to match the solid background. Further detail on the Set Canvas Color node lives in Chapter 94, "Color Nodes," of the DaVinci Resolve Reference Manual, or in Chapter 34 of the Fusion Reference Manual.

NOTE: The Domain of Definition names a bounding box drawn around the pixels holding a nonzero value. Its purpose is to confine image-processing math and to hasten rendering.

### Inputs

By way of its one input, the Auto Domain node takes a 2D image plus an effect mask, the latter handy for bounding the blurred area. Input: For the primary 2D image undergoing the blur, the orange input is the one to use. Effect Mask: Feeding the blue input is a mask shape drawn with polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools. Wiring a mask here pins the blur down to only the pixels inside the mask.

### Basic Node Setup

The case shown below takes it that the image holds no alpha channel but instead shows a CG character rendered over a black background. You see this often across render passes such as specular or shadows. That image then runs into a Set Canvas Color node, which makes the Canvas color black with a solid alpha. From there the Set Canvas Color feeds the Auto Domain node, which picks out the pixels and pins the DoD. Were the source image already carrying a premultiplied alpha channel, you could skip the Set Canvas Color and wire the image straight into the Auto Domain node.

An Auto Domain node trims the region of image processing on its own.

### Inspector

### The Auto Domain Controls tab

### Controls Tab

Most of the time the Auto Domain node works out the DoD bounding box automatically; still, you can reshape that rectangle through the Controls tab in the Inspector. Left Marks the left edge of the ADoD’s search area. Pushing this slider up shifts the left edge rightward, dropping more data off the left margin. Here a value of 1 lands at the image’s right border, whereas 0 sits at its left border. The slider defaults to 0 (left border). Bottom Marks the bottom edge of the ADoD’s search area. Pushing this slider up shifts the bottom edge upward, dropping more data off the bottom margin. Here a value of 1 lands at the image’s top border, whereas 0 sits at its bottom border. The slider defaults to 0 (bottom border). Right Marks the right edge of the ADoD’s search area. Pushing this slider up shifts the right edge leftward, dropping more data off the right margin. Here a value of 1 lands at the image’s right border, whereas 0 sits at its left border. The slider defaults to 1 (right border).

Top Marks the top edge of the ADoD’s search area. Pushing this slider up shifts the top edge downward, dropping more data off the top margin. Here a value of 1 lands at the image’s top border, whereas 0 sits at its bottom border. The slider defaults to 1 (top border).

### Common Controls

Settings Tab The Inspector’s Settings tab repeats across the other miscellaneous nodes as well. You will find these shared controls spelled out fully where this chapter closes, under the “The Common Controls” section.

### Change Depth [CD]

### The Change Depth node

### Change Depth Node Introduction

A single plain purpose drives the Change Depth node, which is to alter the bits per color channel a node draws on for processing. You will often see it applied right after color correcting 32-bit floating-point image files, dropping them from float processing down to 16-bit per channel so as to spare both memory and performance. It earns its keep too when, beyond some spot in your node tree, you decide your images want working at a deeper bit depth than they began with, or when you trim the bit depth to conserve memory.

### Inputs

Through its lone input, the Change Depth node accepts a 2D image together with an effect mask, the latter useful for bounding the blurred area. Input: For the primary 2D image headed for conversion, the orange input is the one to use. Effect Mask: The blue input receives a mask shape made with polylines, basic primitive shapes, paint strokes or bitmaps out of other tools. Tying a mask to this input pins the blur down to only the pixels lying inside the mask.

### Basic Node Setup

In the example beneath this, a Loader node in Fusion Studio gets color corrected and is then stepped down from a floatingpoint image to a 16-bit image, sparing image-processing time and memory.

A Change Depth node set downstream of the color correction performed on a floating-point image.

### Inspector

### The Change Depth Controls tab

### Controls Tab

The pair of controls belonging to this node are the Depth menu and the Dither menu. That duo of menus serves to convert and fine-tune the image’s color depth. Depth The Keep setting leaves the image untouched and merely holds onto the input depth. Every other option swaps the image’s bit depth to whatever value it names. Dither While stepping down out of a higher bit depth, throwing in Error Diffusion or Additive Noise can prove handy for masking artifacts thrown off by troublesome (high-contrast) areas.

### Common Controls

Settings Tab This same Settings tab from the Inspector turns up again throughout the other miscellaneous nodes. A thorough rundown of these shared controls sits at the chapter’s close within the “The Common Controls” section.
