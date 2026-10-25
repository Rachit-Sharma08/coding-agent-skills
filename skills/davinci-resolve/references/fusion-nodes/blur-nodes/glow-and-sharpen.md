# Glow and sharpen

Version: DaVinci Resolve 20.3 Reference Manual. Context: Glow, Sharpen.
[Chapter index](INDEX.md) / [Previous section](defocus-and-directional-blur-and-glow.md) / [Next section](sharpen-and-soft-glow.md) / [Glow Glo](defocus-and-directional-blur-and-glow.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-3"></a> <a id="source-glow-controls"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-sharpen-node-introduction"></a> <a id="source-sharpen-shrp"></a> <a id="source-the-sharpen-node"></a>

### Inputs

Three inputs sit on the Glow node: an orange one feeding the main 2D image, then a blue one taking an effect mask, plus a third — colored white — for a Glow mask. Input: The orange input takes the main 2D image that the glow is applied to. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask here holds the glow's source to the pixels inside that mask. An effect mask gets applied once the tool has processed. Glow Mask: The Glow node allows pre-masking by way of the white glow mask input. A Glow pre-mask filters the image ahead of the glow being applied. The glow is then merged back over the original image. That differs from an ordinary effect mask, which clips the rendered output. The Glow mask permits the glow to spill past the mask's edges while still holding the glow's source to the pixels inside the mask.

Apart from that, Glow masks behave just like Effect masks in every way.

### Basic Node Setup

A Glow node accepts a 2D image such as the MediaIn1 pictured below. Its output carries the node tree onward by feeding another 2D image-processing node or a Merge node.

### Inspector

A Glow node applied to a MediaIn1 node in DaVinci Resolve

### Glow controls

### Controls Tab

Inside the Controls tab live all the main controls for shaping the glow. A Color Scale section down at the bottom of the Inspector lets you tint the glow. Filter Reach for this menu to pick the Blur method the filter uses. The choices are spelled out below.

- Box: A plain yet very fast Box filter.
- Bartlett: Bartlett brings a softer, more delicate glow with a gentler falloff but can take longer to

render than Box.

- Multi-box: Multi-box runs a Box filter across several layered passes to mimic a Gaussian shape.

Use a fair number of passes (four, say) and you get a high-quality blur, frequently quicker than the Gaussian filter, and free of any ringing.

- Gaussian: Gaussian brings a soft glow, blurred via the Gaussian algorithm.
- Fast Gaussian: Fast Gaussian brings a soft glow, blurred via the Gaussian algorithm. This is the default method.
- Blend: Blend brings a nonlinear glow that reads evenly in the whites and blacks.
- Hilight: Hilight brings a glow yet raises no halo around the surrounding pixels.
- Solarize: Solarize brings a glow and solarizes the image.

Color Channels (RGBA) Out of the box this filter works on the R, G, B, and A channels. You can filter channels selectively by clicking each channel to turn it on or off. NOTE: This isn't the same thing as the RGBA checkboxes sitting under the common controls. These picks are honored before the node processes the image, so turning off a channel makes the node bypass it during processing, which speeds the effect's render. The channel controls on the Common Controls tab, by contrast, take effect only once the node finishes its work. Lock X/Y Checking Lock X/Y keeps the horizontal and vertical glow amounts bound to one another. Otherwise you can apply different glow amounts to each axis. Glow Size Glow Size sets how big the glow effect grows. Bigger values widen the glowing highlights across the image. Num Passes Available only in Multi-box mode. Bigger values smooth out the effect's spread but also push render times up. It pays to find the sweet spot between the quality you want and render times you can live with. Glow The Glow slider sets how intense the glow effect is. Bigger values tend to blow the image right out to white. Clipping Mode This setting governs how edges get treated during domain-of-definition rendering. It carries real weight for nodes such as Blur, which may need to sample parts of the image lying beyond the current domain.

- Frame: Frame is the default, and it automatically forces the node's domain of definition to span the image's whole frame, in effect disregarding the present domain of definition. Where the upstream DoD falls short of the frame, the leftover frame area is taken as black/transparent.
- Domain: Choosing Domain honors the upstream domain of definition as the node's effect is applied. This can lead to unwanted clipping wherever the node reaches for a large filter.
- None: Choosing None skips source image clipping altogether. So whatever data the node's effect needs that would normally fall outside the upstream DoD is taken as black/transparent.

Blend The Blend slider sets what share of the affected image is blended with original image. The nearer the value gets to 0, the more of the original image it folds back in. This control is a cloned copy of the Blend slider over on the Common Controls tab; adjusting one adjusts the other in lockstep. Apply Mode Three Apply Modes are on hand for how the glow gets applied to the image.

- Normal: Default. This mode simply lays the glow straight over top of the original image.
- Merge Under: Merge Under tucks the glow beneath the image, going by the Alpha channel.

Threshold mode allows clipping of the threshold values.

- Threshold: This control clips how far the glow's effect reaches. A fresh range slider shows up. Pixels in the

glowed regions whose values fall under the low value are driven to black. Pixels whose values top high are driven to white. High-Low Range Control: On hand only in Threshold mode. Pixels in the glowed regions whose values fall under the low value are driven to black. Pixels whose values top high are driven to white. Color Scale (RGBA) These Scale sliders let you set how much glow lands on each color channel one at a time, tinting the glow. Click and hold the Pick button, then drag the pointer across the viewer, to lift a specific color out of the image.

### Common Controls

Settings Tab The Settings tab in the Inspector also recurs across the other Blur nodes. These shared controls get a full treatment at this chapter's close, under the “The Common Controls” section.

### Sharpen [Shrp]

### The Sharpen node

### Sharpen Node Introduction

The Sharpen node runs a convolution filter to bring out detail across an image as a whole or within a single channel.

### Inputs

A Sharpen node carries two inputs, one for a 2D image and one for an effect mask that can hold down the region the sharpen touches.

Input: The orange input takes the main 2D image for sharpening. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask here confines the sharpen to the pixels inside that mask. An effect mask gets applied once the tool has processed.

### Basic Node Setup

A Sharpen node accepts a 2D image such as the MediaIn1 pictured below. Its output carries the node tree onward by feeding another 2D image-processing node or a Merge node.

### Inspector

A Sharpen node applied to a MediaIn1 node in DaVinci Resolve
