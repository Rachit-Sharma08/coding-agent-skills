# Custom filter node and erode dilate node and filter node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom filter node, Erode dilate node, Filter node.
[Chapter index](INDEX.md) / [Previous section](create-bump-map-and-custom-filter-node.md) / [Next section](filter-node-and-rank-filter-node-and-common-controls.md) / [Custom Filter Node CFlt](create-bump-map-and-custom-filter-node.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-2"></a> <a id="source-emboss-example"></a> <a id="source-erode-dilate-controls"></a> <a id="source-erode-dilate-node-erdl"></a> <a id="source-erode-dilate-node-introduction"></a> <a id="source-filter-node-fltr"></a> <a id="source-filter-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector-2"></a> <a id="source-the-erode-dilate-node"></a> <a id="source-the-filter-node"></a>

### Emboss Example

In the example that follows, five times the value is subtracted from the top left and five times the value is added at the lower right. -5 0 0 010 005 Wherever stretches of the processed image are very smooth in color, the neighboring values stay very close. Wherever the pixels differ across the image (an edge, say), the outputs differ too and tend to accentuate or emboss edges in the image.

A Custom Filter that adds and subtracts surrounding pixels, yielding an embossed look Exposure Example Taking the values... 111 111 111 ...and pushing Normalize toward a positive value brightens the image or makes it glow, mimicking film overexposure.

The Custom Filter Normalize slider used to change exposure Relief Example Taking the values... -1 0 0 000 001

... and pushing Floor Level toward a positive value yields a Relief filter.

Custom Filter Floor Level slider driving a relief result Common Controls Settings Tab Because the Settings tab controls are shared by every Filter node, you'll find their write-ups in the "The Common Controls" section closing out this chapter.

### Erode Dilate Node [ErDl]

### The Erode Dilate node

### Erode Dilate Node Introduction

The Erode Dilate node shrinks or grows the image, the direction depending on whether the Amount slider holds a negative or a positive value.

### Inputs

Two inputs sit on the Erode Dilate node: one carries the main image, while the other takes an effect mask that confines where the erode or dilate is applied. Input: The orange input pulls the RGBA channels out of an image so the custom filter can be calculated. Effect Mask: The optional blue effect mask input takes a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input restricts the erode or dilate to just the pixels falling inside the mask. The effects mask gets applied to the tool only after the tool has finished processing.

### Basic Node Setup

People routinely reach for the Erode Dilate node to shrink or grow mattes. In the example below, a Luma Keyer feeds the Erode Dilate, which then hands the altered key off to a Matte Control that embeds it into the image.

### Inspector

An Erode Dilate node sitting downstream of a Luma Keyer, acting on a Matte Control

### Erode Dilate controls

### Controls Tab

The Controls tab holds the main Amount slider, which decides whether you're running an erode (by keying in a negative value) or a dilate (by keying in a positive value). Color Channels (RGBA) By default the Erode Dilate node works across the R, G, B, and A channels. You can edit channels selectively by ticking or clearing the checkboxes next to each one. These are not the same as the RGBA checkboxes sitting under the Common Controls. The node weighs these controls before it does any processing. Clearing a channel makes the node bypass that channel during processing, which speeds up rendering the effect. By contrast, the channel controls on the Common Controls tab take effect after the node has processed.

Lock X/Y The Lock X/Y checkbox splits the Amount slider into amount X and amount Y, letting each axis carry its own value for the effect. Amount A negative Amount value drives the image to erode. Eroding imitates an underexposed frame, contracting the image as the darker regions spread and gnaw into the brighter ones. A positive Amount value drives the image to dilate, much like overexposing a camera. Areas of high luminance and brightness expand, gnawing into the darker regions of the image. Either approach wipes out fine detail in the image and tends to posterize subtle gradients. How the Amount slider scales is tied to the width of the input image, since an amount value of 1 = image width. To erode or dilate an HD image by precisely 1 pixel, then, you'd key in 1/1920, or 0.00052083.

### Common Controls

Settings Tab Because the Settings tab controls are shared by every Filter node, you'll find their write-ups in the "The Common Controls" section closing out this chapter.

### Filter Node [Fltr]

### The Filter node

### Filter Node Introduction

The Filter node packs several standard convolution filters that you pick straight from a list. With this node you can do anything from radically reshaping an image's look to layering in subtle randomly-generated film grain. The Sobel and Laplacian settings see frequent use for edge detection.

### Inputs

Two inputs sit on the Filter node: one carries the main image, while the other takes an effect mask that confines where the filter is applied. Input: The orange input handles the main 2D image that the filter acts on. Effect Mask: The optional blue effect mask input takes a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input restricts the filter to just the pixels falling inside the mask. The effects mask gets applied to the tool only after the tool has finished processing.

### Basic Node Setup

You can drop the Filter node in after an image, a mask, or any node needing a filter applied. In the example below, it builds an edge matte, which then masks the soft glow ringing the keyed foreground.

A Filter node set to Sobel, pulling an edge matte out of the image Inspector
