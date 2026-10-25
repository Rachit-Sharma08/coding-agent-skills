# Create bump map and custom filter node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Create bump map, Custom filter node.
[Chapter index](INDEX.md) / [Next section](custom-filter-node-and-erode-dilate-node-and-filter-node.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-create-bump-map-cbu"></a> <a id="source-create-bump-map-controls"></a> <a id="source-create-bump-map-node-introduction"></a> <a id="source-custom-filter-controls"></a> <a id="source-custom-filter-node-cflt"></a> <a id="source-custom-filter-node-introduction"></a> <a id="source-examples"></a> <a id="source-filter-nodes"></a> <a id="source-filter-nodes-1"></a> <a id="source-input"></a> <a id="source-input-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-original-image"></a> <a id="source-the-create-bump-map-node"></a> <a id="source-the-custom-filter-node"></a>

### Filter Nodes

This chapter walks through the Filter nodes that Fusion offers. The shorthand shown beside each node name is what you type into the Select Tool dialog while hunting for tools, and it also shows up in scripting references. Throughout this document, node trees that display MediaIn nodes in DaVinci Resolve stand in equally for Loader nodes in Fusion Studio, except where a note says otherwise.

### Create Bump Map [CBu]

### The Create Bump Map node

### Create Bump Map Node Introduction

The Create Bump Map node takes a grayscale (height map) image and turns it into a bump map. Whereas the Bump Map node converts an image into a 3D material, the Create Bump Map node instead generates bump vector data and hands back the result as an RGB image, leaving it open to further image-processing operations.

### Input

Two inputs sit on the Create Bump Map node: one carries the main image, while the other takes an effect mask that confines where the bump map gets built. Input: The orange input pulls the RGBA channels out of an image so the bump map can be calculated. Effect Mask: The optional blue effect mask input takes a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input restricts bump-map creation to just the pixels falling inside the mask. The effects mask gets applied to the tool only after the tool has finished processing.

### Basic Node Setup

A 2D grayscale image such as a fast noise feeds the Create Bump Map node, after which it can run through assorted 2D image-processing filters that build the bump map texture.

A Create Bump Map node outputs its bump map in RGB form, ready for downstream image processing

### Inspector

### Create Bump Map controls

### Controls Tab

Every parameter for building the bump map lives in the Controls tab. Filter Size This menu fixes the filter size used when generating the bump map. The filter size can be put at 3 x 3 pixels or 5 x 5 pixels, which sets how wide a radius of pixels gets sampled. A bigger size means a longer render. Height Source The Height Source menu picks the channel from which the grayscale information is drawn. Clamp Normal.Z This slider trims the lower readings of the blue channel inside the resulting bump texture. Wrap Mode This menu governs how the image wraps along its borders, letting the filter give a proper result with seamless tiling textures. Height Scale The height scale menu changes the contrast of the values produced in the bump map. Pushing this value up makes the bump map more pronounced. Bump Map Texture Depth Through this menu the finished bump texture is matched to, or recast into, whichever bit depth you prefer. NOTE: The definitions below are offered to make some of the terms used in the Create Bump Map node and other comparable node types clearer. Height Map: A grayscale image that holds one height value per pixel. Bump Map: An image whose RGB channels store normals used to alter the existing normals (typically expressed in tangent space). Normal Map: An image whose RGB channels store normals used to replace the existing normals (typically expressed in tangent or object space).

### Common Controls

Settings Tab Because the Settings tab controls are shared by every Filter node, you'll find their write-ups in the "The Common Controls" section closing out this chapter.

### Custom Filter Node [CFlt]

### The Custom Filter node

### Custom Filter Node Introduction

You use the Custom Filter node to run custom convolution filters over images. A custom convolution filter can deliver an enormous range of image effects. Emboss, relief, sharpen, blurring, and edge detection, for instance, are all convolution filters. A number of ready-made custom filters ship in the Filters directory and can be brought in by right-clicking the control header and choosing Settings > Load from the contextual menu. The Custom filter leans on an array (or grid) carrying values in a 3 x 3, 5 x 5, or 7 x 7 layout. (Note: Inside the Inspector the array is forever drawn as a 7 x 7 grid, yet dialing the Matrix Size down to 3 x 3 engages just the middle 9 cells.) The middle of the array stands for the current pixel, while the surrounding entries stand for neighboring pixels. A value of 1 feeds the pixel's full value into the filter. A value of 0 disregards the pixel's value. A value above 1 amplifies that pixel's contribution to the outcome. You can also key in negative values, where the pixel's value gets subtracted from the average. Only whole numbers are allowed; 0.x won't work.

### Input

Two inputs sit on the Custom Filter node: one carries the main image, while the other takes an effect mask that confines where the custom filter is applied. Input: The orange input pulls the RGBA channels out of an image so the custom filter can be calculated. Effect Mask: The optional blue effect mask input takes a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input restricts the custom filter to just the pixels falling inside the mask. The effects mask gets applied to the tool only after the tool has finished processing.

### Basic Node Setup

You can drop the Custom Filter node in after an image, a mask, or any node that calls for a custom convolution filter.

A Custom Filter node placed after a MediaIn node in DaVinci Resolve

### Inspector

### Custom Filter controls

### Controls Tab

The Controls tab is where you fix the filter size and then enter convolution filter values into the filter matrix. Color Channels (RGBA) By default the custom filter works across the R, G, B, and A channels. You can edit channels selectively by ticking or clearing the checkboxes next to each one. These are not the same as the RGBA checkboxes sitting under the Common Controls. The node weighs these controls before it does any processing. Clearing a channel makes the node bypass that channel during processing, which speeds up rendering the effect. By contrast, the matching controls on the Common Controls tab take effect after the node has processed. Matrix Size This menu offers a filter size of 3 x 3 pixels; alternatively 5 x 5 pixels, or else 7 x 7 pixels, thereby fixing how wide a radius of pixels gets sampled. A bigger size means a longer render. Update Lock With this control on, Fusion holds off rendering the filter. That's handy while you dial in each value of the filter, after which you switch Update Lock off and render. Filter Matrix Laid out as a 7 x 7 grid of text boxes, the Filter Matrix control takes a number in each cell that represents how strongly the matching pixel sways the overall convolution filter. The text box dead center stands for the pixel the filter processes. The text box just to the left of center stands for the pixel immediately to its left, and so on. The Matrix size defaults to 3 x 3. Only the pixels directly bordering the current pixel get analyzed. Choosing a larger Matrix size switches on more of the grid's text boxes for entry.

Normalize This dictates how much filter normalization reaches the outcome. Zero gives back a normalized image. With positive values the filter result gets brighter, its level pushed upward. With negative values it goes darker, its level pulled down. Floor Level This tacks on or strips away a minimum, the so-called Floor Level, against the result of the filtered image. Zero adds nothing to the image. Positive values add to the filtered image, while negative values subtract from it.

### Examples

Original Image Example Take, for example, a filter holding the values... 000 010 000 ...which draws nothing from its neighboring pixels, leaving the resulting image untouched.

### Original image

Softening Example A faint softening effect would look like... 111 111 111 ...where the surrounding pixels get averaged together with the center.

Before and after averaging neighboring pixels to soften the image
