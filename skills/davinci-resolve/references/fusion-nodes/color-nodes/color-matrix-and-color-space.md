# Color matrix and color space

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color matrix, Color space.
[Chapter index](INDEX.md) / [Previous section](color-gain-and-color-matrix.md) / [Next section](copy-aux-and-gamut.md) / [Color Matrix CMx](color-gain-and-color-matrix.md)
<a id="source-adding-1-to-each-channel"></a> <a id="source-basic-node-setup-1"></a> <a id="source-brightness-per-channel-example"></a> <a id="source-color-space-controls"></a> <a id="source-color-space-cs"></a> <a id="source-color-space-node-introduction"></a> <a id="source-controls-tab-1"></a> <a id="source-copying-values-example"></a> <a id="source-example-1-invert"></a> <a id="source-example-2-brightness-per-channel"></a> <a id="source-example-3-copying-values"></a> <a id="source-inputs-1"></a> <a id="source-inspector-1"></a> <a id="source-settings-tab-1"></a> <a id="source-settings-tab-2"></a> <a id="source-the-color-space-node"></a>

### Example 1: Invert

Say you want a plain invert or negative of the color values while keeping the Alpha channel as is; the matrix would come out like this: Color Matrix example Notice that we're obliged to add 1 to every channel so the inverted values climb back into the positive numbers. We'll walk this example through one step at a time, watching the waveform of a 32-bit grayscale gradient. 1 The original grayscale.

Original Grayscale

2 RGB set to -1. That inverts the values, but they drop under 0.

RGB set to -1 3 Adding 1 to each channel holds the inversion in place while shifting the values back up into a positive range.

### Adding 1 to each channel

### Example 2: Brightness per Channel

Here the brightness of each channel is steered on its own. It takes 0.2 away from the red channel, puts 0.314 onto the green channel, and puts 0.75 onto the blue channel, all while Alpha stays put.

### Brightness per channel example

### Example 3: Copying Values

Color values can also be shuttled back and forth from one channel to another. Here the red channel holds the image's luminance values figured by thirds, the green channel holds luminance values figured by the proper black-and-white conversion method, and the blue channel takes a third approach that pulls more information from red and less from blue. On top of that, the blue channel's brightness drops by 0.1, and the Alpha channel is swapped out for the original blue channel.

### Copying Values example

### Settings Tab

This same Settings tab from the Inspector turns up in the other Color nodes too. The chapter spells out these shared controls thoroughly at its end, within “The Common Controls” section.

### Color Space [CS]

### The Color Space node

### Color Space Node Introduction

The Color Space node lets you operate on an image through an assortment of alternate color space formats. Out of the box Fusion runs on the RGB color space, and the bulk of nodes and displays read an image's primary channels as Red, Green, and Blue. Shift the color space away from RGB and most images take on an odd look, because Fusion's viewers keep reading the primary channels as Red, Green, and Blue. Convert an image to YUV and view it in one of the viewers, for instance, and the Y channel reads as Red, while Green stands in for the U channel and Blue for the V channel. A number of familiar Fusion interface elements point at the RGB channels straight away. Among them are the four buttons usually sitting on the Inspector's Settings tab that confine the node's effect to one color channel. Apply a conversion to an image and those buttons stay labeled R, G, and B, yet the values behind them now come from the present color space. (For an RGB to HLS conversion, as an example, Red stands for Hue, Green for Luminance, and Blue for Saturation. The color space conversion never alters the Alpha value.)

### Inputs

The Color Space node carries a pair of inputs, one taking the main image and the other an effect mask. Input: This orange input is the sole connection that's mandatory. It pipes in a 2D image for the color space operation to convert. Effect Mask: The optional blue effect mask input welcomes a mask shape made from polylines, plain primitive shapes, paint strokes, or bitmaps produced by other tools. Hooking a mask up here keeps the color space adjustment to nothing but the pixels falling inside that mask. The tool gets an effect mask applied to it once its processing has finished.

### Basic Node Setup

In the manner of many 2D image-processing nodes, the Color Space node accepts a 2D image such as a Loader or the MediaIn1 shown below, works on the image, and then stretches the node tree onward by joining to a further 2D image-processing node or a Merge node.

### Inspector

A Color Space node carrying out a conversion on a MediaIn1 node

### Color Space controls

### Controls Tab

Two menus make up the Color Space node's Controls tab. The upper Conversion menu sets whether you're taking an image to RGB or away from RGB. The lower menu chooses the alternative color space you're converting either to or from. Conversion Three options sit in this menu. None leaves the image alone. Pick To Color and the input image is taken into whichever color space the Color Type control below it names. Pick To RGB and the input image is brought back to the RGB color space out of the type named in the Color Type menu (YUV to RGB, say). Color Type This menu is where you pick the color space conversion that runs when the To Color conversion is active. With the To RGB option chosen in the Conversion menu, the Color Type option ought to match the input image's existing color space. Eight color space options are on offer.

- HSV (Hue, Saturation, and Value): Every pixel in the HSV color space gets spelled out by its Hue, Saturation, and Value components. Value is the trait that lets us tell a light color apart from a dark one, in other words brightness. Lowering saturation is loosely like working white into a paint chip on a palette. Raising Value is loosely like working in black.
- YUV (Luma, Blue Chroma, and Red Chroma): PAL video's analog broadcast relies on the YUV color space. In the past this format was a frequent choice for color correcting images, owing to how well-known it was among a big share of video engineers. Every pixel gets spelled out by its Luminance, Blue Chroma, and Red Chroma components.
- YIQ (Luma, In Phase, and Quadrature): NTSC video's analog broadcast relies on the YIQ color space. This one shows up far less than YUV and is hardly ever encountered in production. Every pixel gets spelled out by its Luminance, Chroma (the in-phase or red-cyan channel), and Quadrature (magenta-green) components.
- CMY (Cyan, Magenta, and Yellow): Though it's more at home in print, the CMY format crops up often in computer graphics from other software packages. Every pixel gets spelled out by its Cyan, Magenta, and Yellow components. CMY is nonlinear.
- HLS (Hue, Luminance, and Saturation): Every pixel in the HLS color space gets spelled out by its Hue, Luminance, and Saturation components. Only slight differences separate the HLS and HSV color spaces.
- XYZ (CIE Format): You use this mode to carry a CIE XYZ image to and from RGB color spaces. Unlike the other color spaces here, CIE XYZ is a weighted space rather than a nonlinear one. Nonlinear, in this sense, means that identical changes in value at different spots in the color space might not deliver the same visual magnitude of change to the eye.

Put plainly, the CIE color space is a perceptual color system whose weighted values came out of experiments in which subjects were tasked with matching an existing light source by means of three primary light sources. Because it spans the full gamut of colors a person can perceive, this color space is most commonly put to work for gamut conversion and for matching color spaces between image display formats.

- Negative: The color channels get inverted. The color space stays RGBA.
- BW: The image is turned into black and white. How much each channel adds to the luminance

of the image can be tuned through slider controls that show up once this option is chosen. Those sliders default to values reflecting each channel's typical perceptual share of an image's luminance. The image keeps its RGBA color space.

### Settings Tab

Other Color nodes carry a copy of this Inspector Settings tab as well. These shared controls get a detailed write-up where the chapter wraps up, under the “The Common Controls” section.
