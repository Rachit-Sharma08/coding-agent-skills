# Filter node and rank filter node and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Filter node, Rank filter node, Common controls.
[Chapter index](INDEX.md) / [Previous section](custom-filter-node-and-erode-dilate-node-and-filter-node.md) / [Next section](common-controls-controls.md) / [Filter Node Fltr](custom-filter-node-and-erode-dilate-node-and-filter-node.md)
<a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-common-filter-settings-inspector"></a> <a id="source-controls-tab-3"></a> <a id="source-example"></a> <a id="source-filter-controls"></a> <a id="source-inputs-2"></a> <a id="source-inspector-3"></a> <a id="source-rank-filter-node-introduction"></a> <a id="source-rank-filter-node-rflt"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-rank-filter-node"></a>

### Filter controls

### Controls Tab

The Controls tab is where you choose the filter type, the channels it acts on, and how much it blends back with the original image.

Filter Type The Filter Type menu offers a lineup of filter types covered below.

- Relief: This makes the image look pressed into metal, like the design on a coin. The image seems bumped and laid over gray.
- Emboss Over: Embosses the image atop itself, with highlight and shadow height and direction you can adjust.
- Noise: Adds noise evenly across images. It's frequently handy for 3D computer-generated images that have to be composited with live action, since it cuts down the squeaky-clean look baked into rendered images. The frame number serves as the random generator seed. As a result, the effect changes on every frame yet stays repeatable.
- Defocus: This filter type blurs the image.
- Sobel: Sobel is an advanced edge detection filter. Paired with a Glow filter, it produces

impressive neon light effects from live-action or 3D-rendered images.

- Laplacian: Laplacian is a highly sensitive edge detection filter, giving a finer edge than the

Sobel filter.

- Grain: Layers noise onto images resembling film grain (chiefly in the midrange). It's handy for

3D computer-generated images that have to be composited with live action, since it cuts down the squeaky-clean look baked into rendered images. The frame number serves as the random generator seed. As a result, the effect changes on every frame yet stays repeatable. Color Channels (RGBA) By default the Filter node works across the R, G, B, and A channels. You can edit channels selectively by ticking or clearing the checkboxes next to each one. Power Values span 1 to 10. Power scales up, in proportion, how strongly the chosen filter hits the image. This has no bearing on the Sobel or Laplacian filter type. Angle This control runs from 0 to 315 degrees and shifts the effect in steps of 45 degrees. It applies only to the Relief and Emboss filters. Median Depending on the Filter Type chosen, the Median control may surface. It modulates the Median filter's strength. A value of 0.5 gives the true median result, since it locates the middle values. A value of 0.0 locates the minimums, and 1.0 locates the maximums. This applies to the Median setting only. Seed This control shows up only with the Grain or Noise filter types. The Seed slider lets you keep the effect's random elements seeded with a steady value. Given the same seed value, the randomizer always returns the same result. Animated This control shows up only with the Grain or Noise filter types. Tick the checkbox to make the noise or grain shift from one frame to the next. For static noise, clear this checkbox.

### Common Controls

Settings Tab Because the Settings tab controls are shared by every Filter node, you'll find their write-ups in the "The Common Controls" section closing out this chapter.

### Rank Filter Node [RFlt]

### The Rank Filter node

### Rank Filter Node Introduction

The Rank Filter inspects surrounding pixels, orders those pixels by value, and then swaps the color of the inspected pixels for the color of whichever pixel holds the chosen rank.

### Inputs

Two inputs sit on the Rank Filter node: one carries the main image, while the other takes an effect mask that confines where the filter is applied. Input: The orange input handles the main 2D image that the Rank filter acts on. Effect Mask: The optional blue effect mask input takes a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input restricts the rank filter to just the pixels falling inside the mask. The effects mask gets applied to the tool only after the tool has finished processing.

### Basic Node Setup

You can park the Rank Filter node anywhere in a node tree to apply an effect to an image.

A Rank Filter node placed after a MediaIn node in DaVinci Resolve

Inspector

l Rank Filter controls Controls Tab The Controls tab is where you set the filter's size and rank value. Size This control fixes the pixel size of the area the filter samples. A value of 1 samples 1 pixel in every direction next to the center pixel. That comes to 9 pixels total, the center sampled pixel included. Bigger values draw from a wider area. Low Size settings work wonders for clearing salt and pepper style noise, whereas higher Size settings yield something akin to watercolor paintings. Rank The Rank slider decides which of the sampled pixel values wins out. Here 0 points to the lowest value (the darkest pixel), while 1 points to the highest value (the brightest pixel).

### Example

What follows is a before and after pairing for a Rank filter, its Size put at 7 and its Rank at 0.7, building a watercolor effect.

Before and after of a Rank Filter producing a watercolor-style effect

### The Common Controls

A handful of identical controls in the Inspector are shared across the Filter nodes. This section runs through the controls that the Filter nodes have in common.

### Inspector

### Common Filter settings Inspector

### Settings Tab

You'll find the Settings tab of the Inspector on every tool in the Filter category. These Settings controls even turn up on third-party filter-type plugin tools. The controls stay consistent and behave the same way on each tool, though a few tools tack on one or two extra options, which are covered here as well. Blend The Blend control fades between the image the tool received at its input and the finished, altered image it sends to its output. With the blend value at 0.0, the outgoing image is the same as the incoming one. Typically this makes the tool skip processing altogether, copying the input straight through to the output. Process When Blend Is 0.0 The tool still processes even when the input value is zero. That can help when this node's processing is scripted to kick off another task while the node's value sits at 0.0.

Red/Green/Blue/Alpha Channel Selector These four buttons confine the tool's effect to chosen color channels. This filter often kicks in after the tool has been processed. For instance, if you clear the red button on a Blur tool, the blur runs across the image first, and then the red channel from the original input gets copied back over the red channel of the result. A few exceptions exist, such as tools where clearing these channels makes the tool skip processing that channel entirely. Tools that behave this way usually carry a matching set of RGBA buttons on the Controls tab in the tool. In that case, the buttons on the Settings and the Controls tabs are one and the same. Apply Mask Inverted Turning on the Apply Mask Inverted option flips the whole mask channel for the tool. The mask channel is the merged outcome of every mask wired into or produced within a node. Multiply by Mask Choosing this option multiplies the RGB values of the masked image by the mask channel's values. That turns every pixel of the image left out of the mask (that is, set to 0) black/transparent. Use Object/Use Material (Checkboxes) Certain 3D software can render to file formats carrying extra channels. The EXR file format notably supports Object ID and Material ID channels, which can serve as a mask for the effect. These checkboxes decide whether those channels get used, when present. Which specific Material ID or Object ID is affected gets chosen with the next set of controls. Correct Edges This checkbox surfaces only while the Use Object or Use Material checkboxes are on. It flips the method used for handling overlapping object edges in a multi-object image. When on, the Coverage and Background Color channels are tapped to separate and sharpen the effect around the object's edge. With this option off (or where no Coverage or Background Color channels exist), aliasing can crop up on the mask's edge. To dig deeper into the Coverage and Background Color channels, turn to Chapter 78, "Understanding Image Channels," within the DaVinci Resolve Reference Manual, or to Chapter 18 over in the Fusion Reference Manual. Object ID/Material ID (Sliders) With these sliders you choose which ID gets turned into a mask, drawn from an image's object or material channels. The Sample button works much like the Color Picker does, letting you grab IDs straight off the image shown in the view. The image or sequence has to have been rendered out of a 3D software package with those channels baked in. Use GPU The Use GPU menu carries three settings. Putting the menu on Disable shuts off hardware-accelerated rendering through your computer's graphics card. Enabled taps the hardware. Auto leans on a capable GPU when one exists and drops back to software rendering when no capable GPU is around
