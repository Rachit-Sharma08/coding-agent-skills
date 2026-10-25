# Drecolor and dresize and dtransform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Drecolor, Dresize, Dtransform.
[Chapter index](INDEX.md) / [Previous section](deep-to-points-and-dholdout-and-dmerge.md) / [Next section](image-to-deep-and-common-controls.md)
<a id="source-basic-node-setup-5"></a> <a id="source-basic-node-setup-6"></a> <a id="source-basic-node-setup-7"></a> <a id="source-common-controls-5"></a> <a id="source-common-controls-6"></a> <a id="source-common-controls-7"></a> <a id="source-drecolor-drc"></a> <a id="source-dresize-drz"></a> <a id="source-dtransform-dxf"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a>

### dRecolor [dRc]

The dRecolor node dRecolor Node Introduction Deep Image data gets combined with an RGB (multi-layer) image by this tool. The node carries two inputs — one for Deep/depth, the other for Color. Turn to this node to recolor Deep Image samples using 2D RGB values Inputs Two inputs are what the dRecolor tool relies on, one for deep color images and one for RGB images. Depth: From a node holding the deep image data you mean to recolor, this orange input is connected. Color: That green input is for the RGB image you’d like to use in combining with the Depth input.

### Basic Node Setup

Into the dRecolor node comes media holding deep image data. From there it lets you combine that with an ordinary 2D image by way of the RGB input.

Taking in deep image data, dRecolor lets you blend it together with a 2D RGB image. Inspector

dRecolor controls Controls Tab Inside the Controls tab sit parameters for blending the 2D RGB image into the background deep image.

- Center X/Y: Reposition the 2D RGB image over the deep image.
- Target Input Alpha: Tick this checkbox to switch on the Alpha channel from the Color input,

shaping how transparent the deep samples are. Switch this option off and only RGB goes toward recoloring the deep image.

- Drop Input Zero Alpha: Switch this on and pixels in the RGBA source carrying zero alpha get skipped and leave the deep image untouched.

### Common Controls

Settings Tab Other Deep Image nodes carry the Inspector’s Settings tab in duplicate too. Detailed coverage of these common controls arrives at the end of this chapter, under the “The Common Controls” section.

### dResize [dRz]

The dResize node dResize Node Introduction A Deep Image’s width and height get resized by this tool.

### Inputs

One input alone is what the dResize tool relies on. Image: From a node holding the deep image data you mean to resize, this orange input is connected.

### Basic Node Setup

Into the dResize node comes media holding deep image data. From there it lets you resize that before handing it on to the rest of the node tree.

dResize accepts deep image data and lets you resize it. Inspector

dResize controls Controls Tab Inside the Controls tab sit parameters for resizing the deep image.

- Width: Scales the image’s width.
- Height: Scales the image’s height.

### Common Controls

Settings Tab A duplicate of the Inspector’s Settings tab appears on other Deep Image nodes as well. These common controls are laid out in full at the chapter’s end, within the “The Common Controls” section.

### dTransform [dXF]

The dTransform node dTransform Node Introduction Adjusting the spatial positioning of deep image data while keeping its depth samples is what this tool lets you do. Deep Images can be scaled and translated, the sample Z values included.

### Inputs

One input plus an effect mask is what the dTransform tool relies on. Image: From a node holding the deep image data you mean to transform, this orange input is connected. Effect Mask: That optional blue effect mask input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools.

### Basic Node Setup

Into the dTransform node comes media holding deep image data. From there it lets you transform that before handing it on to the rest of the node tree.

dTransform accepts deep image data and lets you transform it.

Inspector

dTransform controls Controls Tab Inside the Controls tab sit parameters for transforming the deep image.

- Scale Z: With the slider you can stretch or squeeze the source’s overall depth samples. Raise the scale and the overall depth distance grows. Lower it and the depth range gets compressed.
- Translate Z: Translate Z lets you slide an object forward or back along its depth channel. That gives you the control to move an object nearer to or farther from camera. Sample: Click and drag out of the sample button into the viewer to pick a value.
- Center X/Y: Move the center position of the deep image.
- Pivot X/Y: Move the pivot point of the deep image.
- Size X/Y: Resize the deep image on the selected axis.
- Use Size and Aspect: Tick this box to switch on the parameters below. Size: Scales the image evenly along both the X and Y axes Aspect: Lets you set the image’s aspect ratio.

### Common Controls

Settings Tab The Inspector’s Settings tab is duplicated across other Deep Image nodes too. Full detail on these common controls is given at this chapter’s end, in the “The Common Controls” section.
