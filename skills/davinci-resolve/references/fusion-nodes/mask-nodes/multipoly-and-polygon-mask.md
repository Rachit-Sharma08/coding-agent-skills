# Multipoly and polygon mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Multipoly, Polygon mask.
[Chapter index](INDEX.md) / [Previous section](mask-paint-and-multipoly.md) / [Next section](polygon-mask-and-ranges-mask-fusion.md) / [MultiPoly MPly](mask-paint-and-multipoly.md)
<a id="source-basic-node-setup-1"></a> <a id="source-controls-tab"></a> <a id="source-inputs-1"></a> <a id="source-inspector-1"></a> <a id="source-multipoly-controls"></a> <a id="source-polygon-mask-controls"></a> <a id="source-polygon-mask-node-introduction"></a> <a id="source-polygon-mask-ply"></a> <a id="source-the-polygon-node"></a> <a id="source-usage"></a>

### Usage

Once the MultiPoly is added, the tool stands ready for you to begin drawing your first mask. To build a mask, use the tools across the top of the viewer to lay down polygons, splines, and points (those points become the polyline's segments). Click the first point again to close the mask.

The MutliPoly tool showing three creation of masks on the viewer Inspector

### Multipoly controls

Within the Inspector, clicking the Polygon or BSpline button creates a new mask type. Every new mask joins the List view housed in the Inspector. Inside the List view you can rename or reorder any masks you have just added. To modify particular shapes, select them in the layer list and change their properties in the Inspector's lower section.

To animate any of the masks you have drawn, click the animation diamond beside the text "Right-click here for shape animation" at the Inspector's foot, or right-click that text and pick Animate. Right-clicking a mask in the layer list brings up a few options. Duplicate: Copies the selected mask and inserts a new entry into the layer list. Split here: Splits off the selected mask along with any mask beneath it, copying them into a brand-new MultiPoly node. Rename: Lets you rename the selected mask. Reset to default: Leaves the mask entry in the layer list but strips its shape away and returns all its controls to default. Delete: Removes the mask.

### Polygon Mask [Ply]

### The Polygon node

### Polygon Mask Node Introduction

The Polygon mask shines when you need to mask objects whose shape is irregular. Freshly added to a node, the Polygon mask shows only Center and Angle controls onscreen. Clicking in the viewer adds points to the polyline, each new point linking to the one made just before it. As with the B-Spline mask tool, the Polygon mask animates itself automatically. Adding this node to the Node Editor lays a keyframe on the current frame. Jumping to another frame and altering the shape lays a new keyframe and interpolates between the two defined shapes.

### Inputs

A single effect mask input is what the Polygon mask node carries. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask into this input merges the masks. How that merging works is set in the Inspector's Paint mode menu.

### Basic Node Setup

You can use the Polygon node to produce a detailed spline shape, or pair it with other masks for shapes more complex still. In the node tree below, the Polygon mask produces a detailed shape serving as a solid matte on the Delta Keyer.

A Polygon node generates a detailed shape as a Solid matte.

### Inspector

### Polygon Mask controls

### Controls Tab

The Controls tab serves to refine how the polyline looks once you have drawn it in the viewer. Show View Controls The Show View Controls checkbox turns the display of the mask's onscreen controls in the viewer on or off. With the checkbox off, those onscreen controls, center position, polylines, angles, and the rest, remain hidden even while the node is selected. Level The Level control fixes the transparency level of the pixels in the mask channel. At a value of 1.0 the mask is fully opaque (unless it carries a soft edge). Lower values render the mask partly transparent. The effect is the same as turning down an effect's blend control. NOTE: Lowering a mask's level lowers the values of every pixel the mask covers within the mask channel. For instance, when a Circle mask sits over a Rectangle mask, dropping the Circle mask's level lowers the values of all the pixels in the mask channel, even though the Rectangle mask below stays opaque.

Filter This control chooses the filtering algorithm used as Soft Edge is applied to the mask.

- Box: The fastest of the options, but with lower quality. Box suits small amounts of blur best.
- Bartlett: Known as well by the name Pyramid filter, Bartlett trades off speed against quality nicely.
- Multi-box: Picking this filter reveals the Num Passes slider for tuning the quality. With 1 and 2 passes, the output equals Box and Bartlett in turn. At 4 passes or more, it usually rivals Gaussian, taking less time and leaving no edge "ringing."
- Gaussian: Using a genuine Gaussian approximation, the Gaussian filter produces excellent results, though it runs a bit slower than the others. Now and then it may put a very faint edge "ringing" onto floating-point pixels.

Soft Edge Use the Soft Edge slider to feather (blur) the mask through the chosen filter. Higher values let the edge fade well past the mask's boundaries. A value of 0.0 makes a crisp, well‑defined edge. Border Width The Border Width control sets how thick the mask's edge is. With the solid checkbox on, the border fattens or thins the mask. When the mask is not solid, its shape draws as an outline whose width follows the Border Width setting. Paint Mode Wiring a mask into the effect mask input brings up the Paint mode menu. The Paint mode sets how the mask arriving at the effect mask input and the mask made in the node are merged.

- Merge: Merge is the default for every mask. The new mask is blended into the input mask.
- Add: The new mask's values are summed with the input mask's values.
- Subtract: Across the overlapping areas, the new mask values are deducted from the input mask's values.
- Minimum: Setting the input mask's values beside the new mask, this shows the lowest

(minimum) value.

- Maximum: Setting the input mask's values beside the new mask, this shows the highest

(maximum) value.

- Average: This averages together the new mask and the input mask, giving half their combined sum.
- Multiply: This multiplies the input mask's values by those of the new mask.
- Replace: Anywhere they overlap, the new mask wholly supplants the input mask. Spots that

are zero (entirely black) in the new mask leave the input mask alone.

- Invert: Where the new mask covers the input mask, those areas flip; white turns

black and the other way around. Gray spots in the new mask are inverted only in part.

- Copy: This mode discards the input mask completely and pulls every value from the new mask.
- Ignore: This mode discards the new mask completely and pulls every value from the input mask.

Invert Checking this box inverts the whole mask. Unlike the Invert Paint mode, the box acts on all pixels, regardless of whether the new mask covers them.

Solid With the Solid checkbox on, the mask is filled to read transparent (white) unless inverted. With it off, the spline draws as a mere outline whose thickness comes from the Border Width slider. Center X and Y These controls set the position of the polygon spline mask. Size The Size control resizes the polygon spline effect mask without disturbing the relative behavior of the points making up the mask and without laying a keyframe in the mask animation. X, Y, and Z Rotation These three controls set the mask's rotation angle on any axis. Fill Method The Fill Method menu gives two distinct techniques for handling overlapping regions of a polyline. When overlapping segments in a mask spawn unwanted holes, switch this control over to Non Zero Winding from its Alternate setting. Right-Click Here for Shape Animation Each polygon spline mask, by default, is animated the moment it is created. The first keyframe lands at the current time, and shape changes at other times add new keys. A right-click on this label opens a contextual menu with options for stripping or re-adding animation to the mask, or for publishing and linking the masks together.
