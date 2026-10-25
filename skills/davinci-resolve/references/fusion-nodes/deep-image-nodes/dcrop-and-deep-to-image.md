# Dcrop and deep to image

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dcrop, Deep to image.
[Chapter index](INDEX.md) / [Next section](deep-to-image-and-deep-to-points.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-caching-deep-composites-to-disk"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-dcrop-dcr"></a> <a id="source-deep-image-compositing-toolset-studio-version-only"></a> <a id="source-deep-image-nodes"></a> <a id="source-deep-image-nodes-1"></a> <a id="source-deep-to-image-controls"></a> <a id="source-deep-to-image-dti"></a> <a id="source-deep-to-image-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-the-deep-to-image-node"></a>

### Deep Image Nodes

Fusion’s Deep Image Nodes, used to composite objects in 3D space, are the subject of this chapter. Each node name carries an abbreviation beside it that you can type into the Select Tool dialog while hunting for tools, and that also turns up in scripting references. Throughout this document, treat node trees that show MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a note says otherwise.

### Deep Image Compositing Toolset (Studio Version Only)

A subset of tools in Fusion can load, work with, and save deep image data. Such deep image data — most notably in formats like OpenEXR — keeps several samples for each pixel so as to capture data about objects sitting at varying depths within one pixel. By drawing on this valuable information, the Fusion Deep Image toolset can stack intricate 3D renders — especially in spots where several objects overlap — and merge them into rendered 3D scenes. You’ll find the tools inside the Deep Image subcategory, each carrying a d-prefix. There’s also this:

- Renderer3D nodes can output deep image data.
- Loader and the MediaIn node can import deep image data EXRs.
- Saver can export deep image EXRs.
- Every deep compositing tool — apart from Image to Deep and Deep to Image — is able, on its own, to

turn 2D image inputs into a deep image. NOTE: A linear colorspace is what deep compositing calls for. After the merge is done, you’re free to convert the results into whatever colorspace you want.

### Caching Deep Composites to Disk

Caching deep compositions to disk eases the load that intricate deep compositions place on your computer. The way to do it: right-click whichever node you’d like to cache, pick Cache to Disk, choose where the cache should be saved, and hit OK.

### dCrop [dCr]

The dCrop node dCrop Node Introduction Using min and max depth values you specify, this tool crops Deep Image samples. Pixels can also be cropped by it through an input mask.

### Inputs

A single input is what the dCrop tool relies on. Input: The lone required connection is this orange input. A node carrying deep image data feeds it. Effect Mask: That optional blue effect mask input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools.

### Basic Node Setup

Into the dCrop node comes the media in that holds the deep image data. From there it lets you refine which depth boundaries get handed along to the next tool.

dCrop accepts deep image data Inspector

dCrop controls Controls Tab Inside the Controls tab sit parameters that govern how much depth information moves on to — or is held back from — the node tree beyond. Depth Crop Cropping the Z parameters belonging to the deep image data is what this lets you do.

- Use Minimum Z: Tick this box to apply a Minimum Z depth to the crop. Use Minimum Z: Set the Minimum Z amount with this slider. Sample: Click and drag out of the sample button into the Viewer to pick a value.
- Use Maximum Z: Tick this box to apply a Maximum Z depth to the crop.
- Keep Outside Depth Range: Reach for this control to flip the cropped selection. Once you’ve set a

minimum and/or maximum value with the sliders above, this control reverses the selection so that the cropped area now shows.

### Common Controls

Settings Tab Other Deep Image nodes carry a copy of the Inspector’s Settings tab as well. Full coverage of these common controls waits at this chapter’s close, under “The Common Controls.”

### Deep to Image [DTI]

### The Deep to Image node

### Deep to Image Node Introduction

By flattening its depth samples, this tool turns deep data into a 2D image. What comes out is the deep composite, set for ordinary 2D compositing.

### Inputs

A single input is what the Deep to Image tool relies on. Input: The lone required connection is this orange input. A node carrying deep image data feeds it.

### Basic Node Setup

Into the Deep to Image node comes the media in that holds the deep image data. From there it flattens the image for further work in normal 2D compositing.

Taking in deep image data, Deep to Image flattens it and then routes the resulting 2D image onward through the node tree.

### Inspector

### Deep to Image controls

### Controls Tab

Inside the Controls tab sit parameters that govern the depth information.

- Flip Depth: Inverts the depth information.
- Volumetric Composition: Rather than treating overlapping deep samples as flat surfaces, the Volumetric Composition option blends them as semi-transparent volumes, modeling true interaction through elements like fog or VDBs. The upshot is a more believable composite of semi‑transparent elements.
