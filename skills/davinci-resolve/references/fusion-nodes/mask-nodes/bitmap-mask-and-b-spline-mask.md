# Bitmap mask and b spline mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Bitmap mask, B spline mask.
[Chapter index](INDEX.md) / [Previous section](bitmap-mask-controls.md) / [Next section](b-spline-mask-and-ellipse-mask.md) / [Bitmap Mask Bmp](bitmap-mask-controls.md)
<a id="source-b-spline-mask-bsp"></a> <a id="source-basic-node-setup-1"></a> <a id="source-bitmap-mask-controls"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-the-b-spline-node"></a>

### Inspector

### Bitmap Mask controls

### Controls Tab

Use the Controls tab to fine-tune how the image wired into the orange input becomes the Bitmap mask. Show View Controls Toggling the Show View Controls checkbox turns the mask's onscreen controls in the viewer on or off. With it off, onscreen controls — center position, polylines, angles, and the rest — stay hidden even while the node is selected. Level The Level control governs how transparent the pixels in the mask channel are. At a value of 1.0 the mask is fully opaque (barring a soft edge). Drop the value and the mask turns partly transparent. That matches what lowering an effect's Blend control does. NOTE: Dropping a mask's level drops the values of every pixel the mask covers in the mask channel. As an example, set a Circle mask over a Rectangle mask, and lowering the Circle mask's level lowers the values of all the mask-channel pixels, even where the Rectangle mask underneath stays opaque.

Filter This control picks the filtering algorithm applied when Soft Edge is added to the mask.

- Box: The quickest option, though quality suffers. Box fits best when you need only a little blur.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a sound balance between speed and quality.
- Multi-box: Pick this filter and the Num Passes slider shows up so you can dial in the quality. With 1 and 2 passes the output matches Box and Bartlett in turn. At 4 passes or more the output is generally on par with Gaussian, faster, and free of edge “ringing.”
- Gaussian: Relying on a genuine Gaussian approximation, the Gaussian filter delivers superb results, though it runs a touch slower than the rest. Occasionally it yields an exceptionally faint edge “ringing” on floating-point pixels.

Soft Edge Drag the Soft Edge slider to blur (feather) the mask through the chosen filter. Raise the value and the edge fades far past the mask's boundaries. Set it to 0.0 for a crisp, well-defined edge. Paint Mode Wiring a mask into the effect mask input brings up the Paint mode menu. Paint mode decides how the incoming mask for the effect mask input merges with the mask the node itself produces.

- Merge: The default across all masks. The new mask merges into the input mask.
- Add: The new mask's values are added onto the input mask's values.
- Subtract: Where they overlap, the new mask's values come off the input mask's values.
- Minimum: Looking at the input mask's values against the new mask, this shows the lowest

(minimum) value.

- Maximum: Looking at the input mask's values against the new mask, this shows the highest

(maximum) value.

- Average: This produces the mean — that is, half the sum — across the new mask and the input mask.
- Multiply: This takes the input mask's values times the new mask's values.
- Replace: Wherever they overlap, the new mask fully supplants the input mask. Spots that

read zero (pure black) in the new mask leave the input mask untouched.

- Invert: Parts of the input mask sitting under the new mask flip; white turns

black and the reverse. Gray spots in the new mask invert partway.

- Copy: This mode throws out the input mask entirely and takes every value from the new mask.
- Ignore: This mode throws out the new mask entirely and takes every value from the input mask.

Invert Tick this checkbox to flip the whole mask. In contrast to the Invert Paint mode, this checkbox acts on every pixel, whether or not the new mask covers them. Fit Input This menu lets you choose how the image source is handled when it doesn't match the dimensions of the mask being generated. In the example below, a 720 x 576 image source (yellow) generates a 1920 x 1080 mask (gray).

Crop: When the image source is smaller than the generated mask, it lands per the X/Y controls, masking off just a slice of the mask. When the image source is larger, it again lands per the X/Y controls and gets cropped at the mask's borders. Stretch: The image source is stretched across X and Y to span the generated mask's full dimensions. That may visibly distort the image source. Inside: The image source scales uniformly until one of its dimensions (X or Y) reaches the inside dimensions of the mask. Based on the relative dimensions of image source and mask background, either the source's width or height may get cropped to meet the matching dimension of the mask. Width: The image source scales uniformly until its width (X) meets the mask's width. Based on the relative dimensions of image source and mask, the source's Y dimension may fall short of the mask's Y dimension, so the source is either cropped in Y or fails to span the mask's height.

Height: The image source scales uniformly until its height (Y) meets the mask's height. Based on the relative dimensions of image source and mask, the source's X-dimension may fall short of the mask's X-dimension, so the source is either cropped in X or fails to span the mask's width.

Outside: The image source scales uniformly until one of its dimensions (X or Y) reaches the outside dimensions of the mask. Based on the relative dimensions of image source and mask, either the source's width or height may get cropped or fall short of the matching mask dimension.

Center X and Y These controls set the placement of the Bitmap mask. Channel The Channel menu sets which Channel of the input image builds the mask. You may pick from the red, green, blue, plus alpha channels; from the hue, luminance, or saturation values; or from the input image's auxiliary coverage channel (where one exists). Threshold Low/High The Threshold range control lets you clip the bitmap image. Raising the low range control clips pixels under the set value to black (0.0). Lowering the high range control pushes pixels above the set value to white (1.0). Use Object/Use Material This control does nothing unless the input image carries a Material or Object ID channel. Switched on, the Object ID and Material ID build a mask off the chosen object or material. Switched off, the ordinary color channels build the mask.

### Common Controls

Image and Settings Tabs Other Mask nodes carry copies of the Inspector's Image and Settings tabs as well. The chapter's closing “The Common Controls” section walks through these shared controls thoroughly.

### B-Spline Mask [BSp]

### The B-Spline node

A B-Spline mask matches a Polygon mask in every way but one. Polygon masks rely on Bézier splines, while this mask node relies on B-Splines. A Bézier spline uses one central point plus two handles to control how its spline segment smooths, whereas a B-Spline needs just a lone point. As a result, a B-Spline shape calls for far fewer control points to build a nicely smoothed form. Right after you add it to a node, the B-Spline mask holds only the Center control, shown onscreen. You add points to the B-Spline by clicking in the viewer. Every fresh point links to the previous one, but rather than the spline passing straight through each control point, B-Spline control points merely influence the spline shape. The control point tugs the spline toward itself to form a smooth curve. As with the Polygon mask tool, the B-Spline mask auto-animates. Dropping this node into the Node Editor sets a keyframe at the current frame. Jump to another frame, alter the shape, and a new keyframe is created, interpolating between the two defined shapes.

### Inputs

The B-Spline mask node carries one effect mask input. Effect Mask: The optional blue input looks for a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask into this input and the masks combine. The Paint mode menu over in the Inspector governs how they combine.

### Basic Node Setup

The B-Spline node can build a single smooth spline shape on its own, or join with other masks to form more involved shapes. Down in the node tree below, the B-Spline mask builds a smooth, curved shape serving as a garbage matte on the Delta Keyer.

A B-Spline node producing a smooth, curved form that serves as a garbage matte
