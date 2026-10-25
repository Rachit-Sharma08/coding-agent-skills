# Background color tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Background.
[Chapter index](INDEX.md) / [Next section](day-sky-and-fast-noise.md)
<a id="source-background-bg"></a> <a id="source-background-node-introduction"></a> <a id="source-basic-node-setup"></a> <a id="source-color-tab"></a> <a id="source-common-controls"></a> <a id="source-generator-nodes"></a> <a id="source-generator-nodes-part-1"></a> <a id="source-gradient"></a> <a id="source-gradient-controls"></a> <a id="source-horizontal-gradient-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-the-background-node"></a>

### Generator Nodes

This section covers the Generator nodes that Fusion offers.

Each node name is paired with an abbreviation; you can type these into the Select Tool dialog while hunting for tools and reference them when scripting. Throughout this document, treat node graphs that display MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a difference is called out.

### Background [Bg]

### The Background node

### Background Node Introduction

Whether you need a plain single-color backdrop or an intricate looping gradient, the Background node can build it.

### Inputs

The Background node carries a single input, meant for an effect mask. Effect Mask: Into this optional blue effect mask input you can feed a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask here confines the background color strictly to the pixels falling inside that mask.

### Basic Node Setup

After the Background node produces a color, it hands that color along to a downstream node such as the Paint node shown below.

### Inspector

A Background node generating a background for the Paint tool

### Color Tab

You govern both the style and the color(s) of the produced background from the Color tab. Type Reach for this control to pick which style of background the node turns out. There are four options:

- Solid Color: As the default, this yields a single-color image.
- Horizontal: This yields a two-color horizontal gradation.
- Vertical: This yields a two-color vertical gradation.
- Four Corner: This yields a four-color corner gradation.

Horizontal/Vertical/Four Point With the Type menu on Horizontal, Vertical, or Four Corner, the node presents two- or four-color swatches that let you assign the left/right, top/bottom, or four-corner gradient colors

### Horizontal gradient controls

### Gradient controls

### Gradient

Switching the Type menu to Gradient brings up extra controls for tailoring the direction of the gradient colors.

Gradient Type Which shape the gradient is drawn in is chosen from this menu. Six options exist:

- Linear: Lays the gradient down along a straight path running from the first color stop to the last.
- Reflect: Builds the gradient by mirroring the linear gradient out from each side of the starting point.
- Square: Builds the gradient with a square pattern while the starting point sits at the

center of the image.

- Cross: Builds the gradient with a cross pattern while the starting point sits at the center

of the image.

- Radial: Builds the gradient with a circular pattern while the starting point sits at the center

of the image.

- Angle: Builds the gradient with a counterclockwise sweep while the starting point sits at the

center of the image. Viewer Start and End Position Two red control points joined by a green line mark the Start and End positions inside the viewer, fixing where the gradient opens and closes. Gradient Colors You pick the gradient's colors from this gradient color bar. By default, two color stops establish the start and end colors. To recolor the gradient, select a color stop and then assign a fresh color with the Eyedropper or color swatch. The gradient bar lets you add, move, copy, and remove colors. Reworking a single color comes down to clicking the triangle that sits beneath it on the bar. Adding a fresh color stop to the gradient bar goes like this: 1 Click anywhere along the bar's lower edge. 2 Set the new stop's color through the Eyedropper or color swatch. Moving a color stop along the gradient bar: just drag it horizontally, left or right, across the bar. Copying a color stop: keep Command (macOS) or Ctrl (Windows) held while dragging a stop. Deleting a color stop: pull it upward, beyond the top of the gradient bar. Interpolation Space Which color space gets used when computing the colors that fall between stops is governed by this menu. Offset The Offset control shifts the gradient's position against the start and end markers. It proves most valuable alongside the repeat and ping-pong modes covered below.

Repeat Three options on this menu dictate how the gradient acts once the Offset control scrolls it beyond its start and end positions. Picking Once holds the color steady through the offset. Picking Repeat wraps back around to the start color whenever the offset runs past the end color. Picking Ping-pong plays the color pattern back in reverse. Sub-Pixel The Sub-Pixel menu sets the sub-pixel precision applied when the gradient's edges show up in repeat mode or when the gradient is animated. Cranking it higher slows rendering considerably but yields more accuracy. Gradient Contextual Menu Each gradient carries its own contextual menu, opened by right-clicking the gradient bar. That Gradient contextual menu holds choices for animating, publishing, and linking one gradient to another. It also offers a gradient-specific modifier that assembles a custom gradient by sampling colors off a node's output.

### Common Controls

Image and Settings Tabs Many Generator nodes repeat the same Image and Settings tabs found in the Inspector. You'll find these shared controls explained thoroughly later on, within this chapter's “The Common Controls” section.
