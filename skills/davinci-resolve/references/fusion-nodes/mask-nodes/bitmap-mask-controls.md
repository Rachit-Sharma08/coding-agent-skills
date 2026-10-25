# Bitmap mask controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Bitmap mask.
[Chapter index](INDEX.md) / [Next section](bitmap-mask-and-b-spline-mask.md)
<a id="source-basic-node-setup"></a> <a id="source-bitmap-mask-bmp"></a> <a id="source-bitmap-mask-node-introduction"></a> <a id="source-inputs"></a> <a id="source-mask-nodes"></a> <a id="source-mask-nodes-part-1"></a> <a id="source-the-bitmap-node"></a>

### Mask Nodes

Here the chapter covers the Mask nodes that Fusion offers.

You can type the abbreviation shown beside each node name into the Select Tool dialog while hunting for tools, and they serve in scripting references too. Throughout this document, treat node trees that show MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where stated otherwise.

### Bitmap Mask [Bmp]

### The Bitmap node

### Bitmap Mask Node Introduction

With the Bitmap mask node, images coming from the node tree can serve as masks for nodes and effects. A Bitmap mask may draw on values from any of the image's color, Alpha, hue, saturation, luminance, and auxiliary coverage channels. Nodes can likewise be masked off the Object ID or Material ID of a 3D-rendered image, so long as those channels were baked in at render time. For effect masks the Bitmap mask node isn't needed. For effects masks, the masked node's Common Settings tab carries controls letting you pick which channel of the mask image builds the mask. That said, on certain nodes a Bitmap mask node may still be needed to feed other mask inputs, such as Garbage Mattes and Pre-Masks. Inserting a Bitmap mask node between the mask source and the target node also unlocks extra options you'd otherwise lack when wiring them up directly — combining masks, blurring the mask, or clipping its threshold, for instance.

### Inputs

Within the Node Editor the Bitmap mask node carries two inputs. Input: The orange input takes in a 2D image that the mask gets built from. Effect Mask: The optional blue input looks for a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask into this input and the masks combine. The Paint mode menu over in the Inspector governs how they combine.

### Basic Node Setup

You don't strictly need the Bitmap mask node to feed an image into the effect mask input, yet it surfaces options you can't otherwise reach. It lets you pick channels beyond RGBA for the mask, plus softness and clipping. In the node tree shown below, a Paint menu sitting in the second Bitmap mask node combines the two Bitmap masks, giving you add, subtract, multiply, and further operations on the merged mask.

Bitmap nodes can be chained together for more advanced matte operations.
