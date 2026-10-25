# Multitext and plasma and text

Version: DaVinci Resolve 20.3 Reference Manual. Context: Multitext, Plasma, Text.
[Chapter index](INDEX.md) / [Previous section](multitext-layout-tab-type.md) / [Next section](text-tab-spacing.md) / [Continue Text+ TXT+ / Shading Tab](text-layout-tab.md) / [MultiText MTxT](mandelbrot-and-multitext.md)
<a id="source-basic-node-setup"></a> <a id="source-circles-tab"></a> <a id="source-color-tab"></a> <a id="source-common-controls"></a> <a id="source-image-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-multitext-shading-tab-controls"></a> <a id="source-page-tab"></a> <a id="source-plasma-node-circles-tab"></a> <a id="source-plasma-node-color-tab"></a> <a id="source-plasma-node-introduction"></a> <a id="source-plasma-plas"></a> <a id="source-settings-tab"></a> <a id="source-shading-tab"></a> <a id="source-text-node-introduction"></a> <a id="source-text-txt"></a> <a id="source-the-plasma-node"></a> <a id="source-the-text-node"></a>

### Multitext Shading tab controls

### Shading Tab

Within the Shading tab sit the controls for tuning the text's color, outline, and shadow. Fill These controls govern the color and opacity of the text layer. Enable: Tick this box to switch the text layer on or off. Color Controls:0These assorted controls let you pick the color and opacity for the text layer.

- Softness X and Y: These sliders set how soft the text outline becomes when forming the shading element. The X- and Y-axis can each be controlled on their own. Glow: This slider lays a glow over the softened part of the shading element. Blend: This slider sets how far the softness control's result gets blended back toward the original. You can lean on it to soften the outcome of the soften operation.

Outline These controls fix the color and style of the font outline. Enable: Tick this box to switch the font outline on or off. Color Controls: These controls govern the color and opacity of the outline. Thickness: Thickness sets how thick the outline becomes. Larger values yield thicker outlines. Adapt to Perspective: Ticking this checkbox makes your outline taper thinner where the text recedes from the camera and thicker where it draws nearer. This yields a more believable outline on text transformed in 3D, though it adds considerably to render time. Outside Only: Ticking this checkbox confines the outline to the text's outer edge alone. Out of the box, the outline straddles the edge and overlaps the text in part. Join Style: These buttons present choices for how the outline's corners are rendered. The choices include Sharp, Rounded, and Beveled. Line Style: This menu supplies further choices for the line's style. Apart from the standard solid line, an assortment of dash and dot patterns is on offer. Shadow These controls fix the color and style of the font drop shadow. Enable: Tick this box to switch the font drop shadow on or off. Color Controls: These controls govern the color and opacity of the drop shadow. Position X/Y: These set where the drop shadow lands relative to the main text.

### Page Tab

These parameters let you place a custom-colored backdrop behind the text layers. Layout These govern the text layer's size and placement. Background These controls govern the color of the background shape. Pure black renders as transparent.

### Image Tab

These parameters give you control over the image as a whole, such as aspect ratio plus color and gamma spaces.

### Settings Tab

These parameters are the usual Settings controls shared by Fusion Generator Nodes.

### Plasma [PLAS]

### The Plasma node

### Plasma Node Introduction

The Plasma node generates backgrounds, drawing on four circular patterns to build images resembling plasma. It serves well as a deforming pattern feeding the Shadow and Deform nodes, and for producing an array of other handy shapes and patterns. It bears a resemblance to the Fast Noise node.

### Inputs

Plasma's single input takes an effect mask that restricts where the plasma pattern shows up. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the plasma to just the pixels inside the mask.

### Basic Node Setup

Much like the Mandelbrot node, the Plasma node turns out images suited to motion graphics and sci-fi effects. In the figure below it produces motion graphics serving as a title's backdrop.

### Inspector

A Plasma node applied as a background to a Merge node

### Plasma node Circles tab

### Circles Tab

Through the Circles tab you govern the shape and pattern the Plasma node turns out. Scale The Scale control sets how large the generated pattern is. Operation This menu's choices set the mathematical relationship the four circles take on wherever they cross. Circle Type Pick which kind of circle gets used. Circle Center Read out and shift where the circle's center sits. Circle Scale Sets how large the circle used for the pattern is.

### Plasma node Color tab

### Color Tab

By way of the Color tab you tune the colors and where, within the pattern, those colors land for the plasma being generated. Phase Phase shifts the whole image's color phase. Animating it produces psychedelic color cycles. R/G/B/A Phases Shifts the phase of each individual color channel along with the Alpha. Animating these produces color cycling effects.

### Common Controls

Image and Settings Tabs The Inspector's Image and Settings tabs recur across numerous Generator nodes. These shared controls get a full treatment toward this chapter's close, in the "The Common Controls" section.

### Text+ [TXT+]

### The Text+ node

### Text+ Node Introduction

The Text+ node in Fusion is a sophisticated character generator that handles multiple styles, 3D transformations, and several shading layers. You can lay the text out against a user-defined frame, around a circle, or along a path. Text can be built from any TrueType, OpenType, or PostScript 1 font present on the machine. Thanks to multibyte and Unicode character support, text can be generated in any language, right-to-left and vertically oriented scripts included. This node turns out a 2D image. For extruded 3D text with optional beveling, turn to the Text 3D node.
