# Anaglyph and combiner

Version: DaVinci Resolve 20.3 Reference Manual. Context: Anaglyph, Combiner.
[Chapter index](INDEX.md) / [Next section](combiner-and-disparity-and-disparity-to-z.md)
<a id="source-anaglyph-ana"></a> <a id="source-anaglyph-node-introduction"></a> <a id="source-basic-node-setup"></a> <a id="source-color"></a> <a id="source-combiner-com"></a> <a id="source-combiner-node-introduction"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-dubois"></a> <a id="source-half-color"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-monochrome"></a> <a id="source-optimized"></a> <a id="source-stereo-nodes"></a> <a id="source-stereo-nodes-part-1"></a> <a id="source-the-anaglyph-color-type-menu"></a> <a id="source-the-anaglyph-controls-tab"></a> <a id="source-the-anaglyph-method-menu"></a> <a id="source-the-anaglyph-node"></a> <a id="source-the-combiner-node"></a>

### Stereo Nodes

This chapter walks through the Stereo nodes that Fusion offers. Stereoscopic nodes appear only within Fusion Studio and DaVinci Resolve Studio.

You can type the abbreviation beside each node's name into the Select Tool dialog while hunting for tools, and the same shorthand applies in scripting references. Throughout this document, any node tree that depicts MediaIn nodes in DaVinci Resolve can be read as equivalent to Loader nodes in Fusion Studio, except where stated otherwise.

### Anaglyph [ANA]

### The Anaglyph node

NOTE: You'll find the Anaglyph node solely within Fusion Studio and DaVinci Resolve Studio.

### Anaglyph Node Introduction

You reach for the Anaglyph node to build stereoscopic pictures out of distinct left eye and right eye images. Typically it sits at the close of a stereoscopic pipeline, where it shows or hands off the finished result.

### Inputs

Three connections sit on the Anaglyph node, namely a left eye input, a right eye input, plus an effect mask. Left Eye Input: Feed the orange input the 2D picture that stands for the left eye of your stereo comp. Right Eye Input: Feed the green input the 2D picture that stands for the right eye of your stereo comp. Effect Mask: The blue input expects a mask shape built from polylines, simple primitive forms, paint strokes, or bitmaps coming from other tools. Wiring a mask here confines the stereoscopic creation to just the pixels lying inside that mask.

### Basic Node Setup

You normally drop the Anaglyph node at the tail of a stereoscopic node tree so it can present the finished result. With distinct left- and right-eye pictures, the left eye image goes into the orange input while the right eye image goes into the node's green input. With horizontally or vertically stacked pictures that already hold both left- and right-eye data, only the orange input gets a connection.

An Anaglyph node using separate left and right eye inputs

### Inspector

### The Anaglyph Controls tab

### Controls Tab

With the parameters found in the Controls tab, the individual images get merged into a stereoscopic output. Color Type Menu The Color Type menu lets you select among various color encodings to suit whichever display device you favor. So your stereo glasses match, pick from these encodings: Red/Cyan, Red/Green, Red/ Blue, Amber/Blue, and Green/Magenta. Of these, Red/Cyan sees the most use.

### The Anaglyph Color Type menu

Method Beyond the color chosen to encode the image, the Method menu offers a further five approaches to pick from: Monochrome, Half-color, Color, Optimized, and Dubois. Each is explained in the entries that follow.

### The Anaglyph Method menu

- Monochrome: Take a Red/Cyan Color Type as the example: the left eye holds the left image's luminance, which lands in the red channel of the output. The right eye holds the right image's luminance, which lands in the output's green and blue channels.
- Half-Color: Again assuming a Red/Cyan Color Type, the left eye holds the left image's luminance, deposited into the red channel of the output. The right eye instead holds the color channels of the right image that correspond to that eye's glasses color.

### Monochrome

### Half-Color

- Color: The left eye holds the color channels of the left image matching that eye's glasses color, and the right eye holds the color channels of the right image matching that eye's glasses color.
- Optimized: Take red/cyan glasses, for instance: the brightness reaching the viewer through the left eye comes out far dimmer than the brightness through the right eye. Going by the usual ITU-R 601 luminance ratios, the red eye delivers 0.299 brightness whereas the cyan eye delivers 0.587+0.114=0.701 brightness—more than double. That brightness gap across the eyes can trigger what's known as retinal rivalry or binocular rivalry, capable of wrecking the stereo effect. With the Optimized method, the right eye is built exactly as the Color method builds it. The left eye likewise draws on the green and blue channels, but paired with a brightness boost that cuts down retinal rivalry. Because it pulls the identical pair of channels from each source image, it leaves the third channel unreproduced. As an example, the red output channel receives 1.05× the green plus 0.45× the blue channels of the left image, while the output's green and blue channels receive the green and blue channels of the right image. The red component of both the left and right images goes unused.

### Color

### Optimized

- Dubois: When colors are reasonably saturated, the Half-color, Color, and Optimized methods can bring on retinal rivalry, since the color reaches only a single eye. Picture red/ cyan glasses: a saturated green object reads as black through the red eye yet green through the cyan eye. By drawing on the spectral behavior of red/cyan glasses specifically together with CRT (Trinitron) phosphors, the Dubois method yields a superior anaglyph that, on the whole, lessens the retinal rivalry stemming from such per-eye color discrepancies. It likewise tends to curb the ghosting that appears as one eye 'leaks' into the other. Fusion's specially computed matrix targets red/ cyan glasses and is not offered for other glasses types. And because it derives from CRT color primaries, it may fall short on a typical LCD (even so, it will most likely still yield less retinal rivalry and ghosting than the alternative methods).

### Dubois

Swap Eyes Lets you trade the left and right eye inputs with little effort. Horiz Stack Accepts an image whose left- and right-eye data sit side by side horizontally. Such images often go by the names “crosseyed” or “straight stereo.” Just wire that single image into the node's orange input. The node then builds an image half as wide as the original, drawing the left half of the source for the left eye and the right half of the source for the right eye. Color encoding follows whatever color type and method you specified. Vert Stack Accepts an image whose left- and right-eye data sit stacked vertically. Just wire that single image into the node's orange input. The node then builds an image half as tall as the original, drawing the bottom half of the source for the left eye and the top half of the source for the right eye. Color encoding follows whatever color type and method you specified.

### Common Controls

Settings Tab You'll find the Inspector's Settings tab repeated across the other Stereo nodes as well. Full coverage of these shared controls sits at this chapter's close, under the “The Common Controls” section.

### Combiner [Com]

### The Combiner node

NOTE: You'll find the Combiner node solely within Fusion Studio and DaVinci Resolve Studio.

### Combiner Node Introduction

Fed two stereoscopic inputs, the Combiner node produces what are called “stacked images” holding the left and right eye, arranged either beside one another or one above the other. Stereoscopic nodes ship only with Fusion Studio and DaVinci Resolve Studio.
