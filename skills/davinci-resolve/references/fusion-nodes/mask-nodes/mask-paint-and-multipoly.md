# Mask paint and multipoly

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mask paint, Multipoly.
[Chapter index](INDEX.md) / [Previous section](mask-paint-mask-paint-node-introduction.md) / [Next section](multipoly-and-polygon-mask.md) / [Mask Paint PNM](mask-paint-mask-paint-node-introduction.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-introduction"></a> <a id="source-mask-paint-controls"></a> <a id="source-mask-tab"></a> <a id="source-multipoly-mply"></a> <a id="source-the-mask-paint-tab"></a> <a id="source-the-multipoly-node"></a>

### Inputs

A single effect mask input is what the Paint mask node carries.

Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask into this input merges the masks. The way that merging happens is governed by the Paint mode menu within the Inspector.

### Basic Node Setup

The Mask Paint node comes in handy for painting masks in a looser, more freehand, pressure sensitive manner. In the node tree below, the Mask Paint node serves to patch holes in a Bitmap mask.

A Mask Paint node can be put to work repairing the troublesome regions of a matte.

### Inspector

### Mask Paint controls

Because the Mask Paint node's Controls tab is essentially the same as the Paint node's, you can find fuller detail in Chapter 113, "Paint Node," within the DaVinci Resolve Reference Manual, or Chapter 53 of the Fusion Reference Manual. What sets the two nodes apart is that, since Mask Paint works on single-channel mask images, it has no Channel Selector control and every color control holds just one Alpha value. The Mask tab, though, carries several parameters that differ from the Paint tool, and those are covered below.

### The Mask Paint tab

### Mask Tab

The Mask tab serves to fine-tune the basic mask parameters that sit outside the realm of "panting." Among these are how several masks merge, the overall softness control, and the level control. Show View Controls The Show View Controls checkbox switches the display of the mask's onscreen controls in the viewer on or off. With this checkbox off, the onscreen controls, center position, polylines, angles, and the rest, stay hidden even while the node is selected. Level The Level control fixes the transparency level of the pixels in the mask channel. At a value of 1.0, the mask is fully opaque (barring a soft edge). Lower values leave the mask partly transparent. The outcome matches lowering an effect's blend control. NOTE: Dropping a mask's level drops the values of every pixel the mask covers in the mask channel. As an example, with a Circle mask laid over a Rectangle mask, lowering the Circle mask's level drops the values of all the pixels in the mask channel, even while the Rectangle mask underneath stays opaque. Filter This control picks the filtering algorithm applied when Soft Edge is added to the mask.

- Box: The quickest method, though quality suffers. Box works best with only small amounts of blur.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a solid balance between speed and quality.
- Multi-box: Choosing this filter brings up the Num Passes slider, which lets you dial in the quality. At 1 and 2 passes, the output matches Box and Bartlett in turn. From 4 passes up, the output is generally on par with Gaussian, achieved faster and free of edge "ringing."
- Gaussian: Built on a true Gaussian approximation, the Gaussian filter delivers excellent results, albeit a touch slower than the rest. On occasion it can yield a barely perceptible edge "ringing" on floating-point pixels.

Soft Edge Reach for the Soft Edge slider to blur (feather) the mask through the chosen filter. The larger the value, the farther the edge fades past the mask's boundaries. A value of 0.0 yields a crisp, well-defined edge.

Paint Mode Wiring a mask into the effect mask input brings up the Paint mode menu. The Paint mode decides how the mask coming into the effect mask input and the mask built in the node are merged.

- Merge: Merge is the default across all masks. The new mask is blended into the input mask.
- Add: The new mask's values are added onto the input mask's values.
- Subtract: Within the overlapping areas, the new mask values are taken away from the input mask's values.
- Minimum: Weighing the input mask's values against the new mask, this shows the lowest

(minimum) value.

- Maximum: Weighing the input mask's values against the new mask, this shows the highest

(maximum) value.

- Average: This takes the new mask and input mask and averages them (half their sum).
- Multiply: This multiplies the input mask's values by the new mask's values.
- Replace: Wherever they overlap, the new mask fully takes the place of the input mask. Spots that

read zero (fully black) in the new mask leave the input mask unchanged.

- Invert: Wherever the new mask covers the input mask, those areas flip; white turns

black and the reverse. Gray spots in the new mask invert only partly.

- Copy: This mode throws away the input mask entirely and draws all values from the new mask.
- Ignore: This mode throws away the new mask entirely and draws all values from the input mask.

Invert Ticking this checkbox flips the whole mask. Unlike the Invert Paint mode, the checkbox acts on every pixel, whether or not the new mask covers it.

### Common Controls

Image and Settings Tabs The Inspector's Image and Settings tabs appear in the other mask nodes too. Full descriptions of these common controls sit at this chapter's close, in the "The Common Controls" section.

### MultiPoly [MPly]

### The MultiPoly node

### Introduction

By letting you build several masks inside one node, the MultiPoly tool streamlines rotoscoping. The inspector's list of polygon shapes makes it easy to modify, organize, and animate shapes from a single straightforward interface. Because the masks sit in a scrolling list, much like the convenience MultiMerge provides, organizing, editing, and animating individual shapes is effortless. This intuitive interface simplifies drawing intricate masks and lets you assemble polished compositions with ease. On top of that, every one of these benefits lives inside this List view, which speeds up selecting and modifying particular shapes, toggling whether they are visible, and adjusting their parameters precisely.
