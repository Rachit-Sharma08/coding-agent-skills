# Color gain and color matrix

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color gain, Color matrix.
[Chapter index](INDEX.md) / [Previous section](color-gain-gain-tab.md) / [Next section](color-matrix-and-color-space.md) / [Color Gain Clr](color-curves-and-color-gain.md)
<a id="source-balance-tab"></a> <a id="source-basic-node-setup"></a> <a id="source-color-gain-balance-tab"></a> <a id="source-color-gain-hue-tab"></a> <a id="source-color-gain-ranges-tab"></a> <a id="source-color-gain-saturation-setting-tab"></a> <a id="source-color-matrix-cmx"></a> <a id="source-color-matrix-controls"></a> <a id="source-color-matrix-node-introduction"></a> <a id="source-controls-tab"></a> <a id="source-hue-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-ranges-tab"></a> <a id="source-saturation-tab"></a> <a id="source-settings-tab"></a> <a id="source-the-color-matrix-node"></a>

### Saturation Tab

Within this Setting tab live the controls for how intense the colors are in each separate RGB channel.

### Color Gain Saturation setting tab

RGB Saturation As you adjust a single channel, setting it to 0.0 drains every bit of that channel's color away. Going above one heightens the scene's color, driving it toward the primary color.

### Balance Tab

Inside the Color Gain node, this tab supplies controls for tuning a color channel's overall balance. You get separate color and brightness controls covering the image's High, Mid, and Dark ranges. The colors come paired as opposites drawn from the two leading color spaces. Red values may be nudged toward Cyan, Green values toward Magenta, and Blue toward Yellow. Each channel's brightness can be lifted or dropped.

### Color Gain Balance tab

CMY Brightness Highs/Mids/Darks Out of the box, the Balance sliders move from -1 to +1, though you can type in values past that span by hand to strengthen the result. Leaving any slider at 0.0 means the image channel goes unchanged. A positive or negative reading tells you the image channel's balance has been shifted toward one or the other color of the pair.

### Hue Tab

Turn to the Color Gain node's Hue tab when you want to rotate the image's overall hue while leaving brightness and saturation alone. Three sliders give you separate command over the High, Mid, and Dark ranges. Here's how the hues sit in order across the RGB color space: Red, Yellow, Green, Cyan, Blue, Magenta and Red.

### Color Gain Hue tab

High/Mid/Dark Hue Anything over 0 rotates the image's hue rightward (red shifts to yellow). Anything under 0 rotates it leftward (red shifts to magenta). Reach -1.0 or 1.0 and the hue rounds the full cycle back to where it began. The hue sliders default to a -1.0 to +1.0 span. You can key in values beyond that span by hand.

### Ranges Tab

Housed in the Ranges tab are the controls for declaring which of an image's pixels count as shadows and which count as highlights. The midrange is always worked out as whatever pixels fall outside both the shadows and the highlights.

### Color Gain Ranges tab

Spline Display You dial in the ranges by working the spline handles. Four spline points exist, each carrying a single Bézier handle. The upper pair of handles marks where the shadow and highlight ranges begin, while the lower pair marks where the range ends. Those Bézier handles govern the falloff. There are no dedicated controls for the midtones range, since it's taken to be whatever sits between the shadow and highlight ranges. The X and Y text controls under the Spline display let you type exact positions for whichever Bézier point or handle is selected. Preset Simple/Smooth Ranges Pressing one of these two buttons resets the spline ranges to either Smooth (the default) or Simple (linear).

### Settings Tab

You'll find the Inspector's Settings tab repeated across the other Color nodes as well. A full account of these shared controls waits at this chapter's close, in the “The Common Controls” section.

### Color Matrix [CMx]

### The Color Matrix node

### Color Matrix Node Introduction

With the ColorMatrix you get an enormous range of operations for tweaking values one color channel at a time.

### Inputs

Two inputs come with the Color Matrix node: one carries the main image and the other an effect mask. Input: This orange input is the sole connection you must make. It feeds in a 2D image for the color matrix to adjust. Effect Mask: The optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask here confines the color matrix adjustment to just the pixels inside that mask. An effect mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

As with plenty of 2D image-processing nodes, the Color Matrix node takes in a 2D image such as a Loader node or the MediaIn1 pictured below. Its output carries the node tree forward by wiring into a further 2D image-processing node or a Merge node.

### Inspector

A Color Matrix node working on a MediaIn1 node

### Color Matrix controls

### Controls Tab

Color Matrix scales the RGBA channels according to the figures you enter in a 4 x 4 grid. That grid's fifth column/row serves as an Add column. Update Lock With this control on, Fusion holds off rendering the node. It's handy for dialing in each of the node's values first, then clearing Update Lock to render it. Matrix This is what sets which kind of operation actually runs. Reading across, the horizontal rows lay out the node's output values, left to right being R, G, B, A, and Add. The vertical columns lay out the input values, top to bottom being R, G, B, A, and Add. Through the Add column you can simply add values onto the separate color channels. By default the output values match the input values exactly.

- 1.0 sends a full 100% of the Red channel input through to the Red channel output.
- 1.0 likewise carries 100% of the Green channel input over to the Green channel output.
- 1.0 passes 100% of the Blue channel input straight to the Blue channel output.
- 1.0 routes 100% of the Alpha channel input onward to the Alpha channel output.

Laid out as math, the matrix's default settings come out like this: [R out] = 1 _ [R in] + 0 _ [G in] + 0 _ [B in] + 0 _ [A in] + 0 [G out] = 0 _ [R in] + 1 _ [G in] + 0 _ [B in] + 0 _ [A in] + 0 [B out] = 0 _ [R in] + 0 _ [G in] + 1 _ [B in] + 0 _ [A in] + 0 [A out] = 0 _ [R in] + 0 _ [G in] + 0 _ [B in] + 1 _ [A in] + 0 Invert Turning this option on flips the Matrix. Picture shuffling channels around, running other operations through different nodes, then copying and pasting the original ColorMatrix, set to Invert, to bring your channels back to where they started.
