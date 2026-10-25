# B spline mask and ellipse mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: B spline mask, Ellipse mask.
[Chapter index](INDEX.md) / [Previous section](bitmap-mask-and-b-spline-mask.md) / [Next section](ellipse-mask-controls.md) / [B-Spline Mask BSp](bitmap-mask-and-b-spline-mask.md)
<a id="source-adding-points"></a> <a id="source-adjusting-tension-on-a-b-spline"></a> <a id="source-b-spline-mask-controls"></a> <a id="source-b-spline-mask-polygon-toolbar"></a> <a id="source-b-spline-toolbar"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-ellipse-mask-elp"></a> <a id="source-ellipse-mask-node-introduction"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-the-ellipse-node"></a>

### Inspector

### B-Spline Mask controls

### Controls Tab

The Controls tab helps you refine how the B-Spline looks once you've drawn it in the viewer. Show View Controls The Show View Controls checkbox switches the mask's onscreen controls in the viewer on or off. Disable it and the onscreen controls — center position, polylines, angles, and so on — won't show even with the node selected. Level Level sets the transparency of the pixels in the mask channel. At 1.0 the mask reads fully opaque (save for a soft edge). Lower values render the mask partly transparent. The outcome equals lowering an effect's blend control. NOTE: Dropping a mask's level drops the values of all pixels the mask covers in the mask channel. As an example, place a Circle mask over a Rectangle mask, and lowering the Circle mask's level lowers the values of all of the mask-channel pixels, even though the Rectangle mask below stays opaque. Filter This control picks the filtering algorithm applied when Soft Edge is added to the mask.

- Box: The fastest method, at the cost of quality. Box suits small amounts of blur best.
- Bartlett: Known too as a Pyramid filter, Bartlett offers a fine trade-off between speed and quality.
- Multi-box: Choosing this filter reveals the Num Passes slider so you can govern quality. At 1 and 2 passes, the results equal Box and Bartlett respectively. From 4 passes upward, results tend to rival Gaussian, in less time and without edge “ringing.”
- Gaussian: Built on a true Gaussian approximation, the Gaussian filter produces excellent results, albeit a bit slower than the others. Now and then it leaves an extremely slight edge “ringing” on floating-point pixels.

Soft Edge Reach for the Soft Edge slider to blur (feather) the mask via the chosen filter. Higher values let the edge fade well past the mask's boundaries. A setting of 0.0 yields a crisp, well-defined edge. Border Width The Border Width control tunes how thick the mask's edge is. With the solid checkbox on, the border grows or shrinks the mask. When the mask isn't solid, the mask shape renders as an outline whose width follows the Border Width setting. Paint Mode Wiring a mask into the effect mask input shows the Paint mode menu. Paint mode sets how the mask coming into the effect mask input merges with the mask the node creates.

- Merge: The default for every mask. The new mask merges into the input mask.
- Add: The new mask's values are summed onto the input mask's values.
- Subtract: Throughout the overlapping regions, the new mask's values are deducted from the input mask's values.
- Minimum: Weighing the input mask's values against the new mask, this returns the

lowest (minimum) value.

- Maximum: Weighing the input mask's values against the new mask, this returns the

highest (maximum) value.

- Average: This yields the mean value (half the sum) taken from the new mask together with the input mask.
- Multiply: This multiplies the input mask's values by the new mask's values.
- Replace: Across any overlap, the new mask wholly takes over the input mask. Regions that

are zero (totally black) in the new mask leave the input mask alone.

- Invert: Portions of the input mask the new mask covers get flipped; white becomes

black and vice versa. Gray regions in the new mask flip partway.

- Copy: This mode discards the input mask completely and draws every value from the new mask.
- Ignore: This mode discards the new mask completely and draws every value from the input mask.

Invert Tick this checkbox to flip the entire mask. Unlike the Invert Paint mode, the checkbox touches every pixel, no matter whether the new mask covers them. Solid With the Solid checkbox on, the mask fills in transparent (white) unless inverted. With it off, the spline renders as an outline alone, its thickness governed by the Border Width slider. Center X and Y These controls set the placement of the B-Spline mask.

Size Reach for the Size control to scale the B-Spline effect mask without disturbing the relative behavior of the points that make up the mask, and without dropping a keyframe into the mask animation. X, Y, and Z Rotation Use this trio of controls to set the mask's rotation angle along any axis. Fill Method The Fill Method menu provides two distinct ways to handle overlapping regions of a polyline. Should overlapping segments in a mask be producing unwanted holes, switch this control over from Alternate across to Non Zero Winding. Right-Click Here for Shape Animation By default, the instant a B-Spline mask is created it begins animating. Its first keyframe lands at the current time, and any shape changes at other times will produce new keys. Right-click this label to open a contextual menu offering options for stripping or re-adding animation on the mask, or publishing and connecting the masks.

### Adding Points

Adding Points to a B-Spline effect mask is fairly simple. Right after you drop the node into the Node Editor, no points exist, but the tool sits in Click Append mode. Click once in the viewer at each spot the mask needs a point. Keep clicking to trace out the mask's shape. Once the shape is finished, click the first point once more to close the mask. With the shape closed, the polyline's mode switches to Insert and Modify. From there you can add and tweak extra points on the mask by clicking the spline segments. To lock the mask's shape down and head off accidental edits, set the Polyline mode to Done via the Polyline toolbar or the contextual menu. Adjusting Tension on a B-Spline A control point's tension dictates how smooth a B-Spline is. To tune a B-Spline's control-point tension, select the point in the viewer, hold the W key, and drag the mouse pointer left and right to raise or lower the tension of the curve passing through that point.

### Adjusting Tension on a B-Spline

### B-Spline Toolbar

Select a B-Spline mask in the Node Editor and a toolbar shows above the viewer, its buttons giving quick access to the modes. Rest the pointer on any toolbar button to bring up a tooltip explaining what that button does.

### B-Spline Mask Polygon toolbar

To alter how the toolbar displays, right-click it and pick from the choices in the toolbar's contextual menu. The Polylines section explains in full what the buttons in this toolbar do.

### Common Controls

Image and Settings Tabs Other mask nodes likewise carry copies of the Inspector's Image and Settings tabs. The closing “The Common Controls” section of this chapter explains these shared controls in full.

### Ellipse Mask [Elp]

### The Ellipse node

### Ellipse Mask Node Introduction

The Ellipse mask shines when you're masking round objects. By default it's a circle, but you get independent control over its width, height, and angle, which opens up a broad range of ellipsoidal shapes.

### Inputs

The Ellipse mask node carries one effect mask input. Effect Mask: The optional blue input looks for a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask into this input and the masks combine. The Paint mode menu over in the Inspector governs how they combine.

### Basic Node Setup

The Ellipse mask node comes in handy for building circular masks. Below, the Ellipse mask builds a circular colored shape by carving a circular shape out of a background node.
