# Spolygon and srectangle

Version: DaVinci Resolve 20.3 Reference Manual. Context: Spolygon, Srectangle.
[Chapter index](INDEX.md) / [Previous section](sngon-and-soutline-and-spolygon.md) / [Next section](srectangle-and-srender-and-sstar.md) / [sPolygon sPly](sngon-and-soutline-and-spolygon.md)
<a id="source-adding-points"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-1"></a> <a id="source-controls-2"></a> <a id="source-external-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-srectangle"></a> <a id="source-style-1"></a> <a id="source-style-tab-1"></a> <a id="source-the-spolygon-controls-tab"></a> <a id="source-the-spolygon-style-tab"></a> <a id="source-the-spolygon-toolbar"></a> <a id="source-the-srectangle-node"></a>

### Basic Node Setup

Being a shape generator, the sPolygon node produces a shape and so carries no inputs. The sPolygon's output can feed a sRender for viewing and further compositing, or—more commonly—hook into another Shape node such as sGrid or sDuplicate.

An sPolygon node wired into an sDuplicate node, the output shown through an sRender node

### Inspector

### The sPolygon Controls tab

### Controls

You use the Controls tab to set the polygon's traits—fill, border, size, and placement. Solid With the Solid checkbox on, the rectangle shape fills with whatever color you defined in the Style tab. With it off, only an outline drawn by the Border Width control shows, and the middle turns transparent. Border Width This parameter grows or shrinks the border running around the shape. Though usable while the Solid checkbox is on, its main job is governing outline thickness once the checkbox is off. Border Style The Border Style parameter dictates the way the rectangle's sides meet at the corners. Three corner styles stand available. Bevel flattens each corner to a square. Round gives corners a curved finish. Miter keeps corners sharp and pointed. Cap style Those cap styles let lines end flat, rounded, or squared off. Flat caps finish with flat, squared ends, whereas rounded caps finish with semi-circular ends. Squared caps carry projecting ends reaching half the line width past the line's end. None of the caps show up unless the length sits below 1.0. Position Only when the Solid checkbox is off does the Position parameter appear. It lets you set the shape's starting point. Paired with the Length parameter, it places the gap in the outline.

Length Only when the Solid checkbox is off does the Length parameter appear. A length of 1.0 yields a closed shape. Dropping the length under 1.0 opens a gap in the outline. Keyframing the Length parameters lets you build write-on style animations. X and Y Offset You use these parameters to shift the shape left, right, up, and down across the frame. The shape begins at the frame's center, and the parameters offset that placement. The offset coordinates are normalized to the frame's width. So an X offset of 0.0 sits centered, and a value of 0.5 drops the shape's center right onto the frame's right edge. Z Offset [3D] When working with the 3D toolset, you can shift the polygon back and forth along the Z-axis by tuning these controls. Size Reach for the Size control to scale the polygon shape up or down, without disturbing the relative behavior of the points making up the shape or laying down a keyframe in the shape animation. X,Y,Z Rotation These three controls let you tune the shape's rotation angle along any axis. Fill Method [3D] The Fill Method menu provides two distinct ways of treating overlapping regions within a polyline. If overlapping segments in a shape are producing unwanted holes, try flipping this control's setting from Alternate to Non Zero Winding.

### Style Tab

### The sPolygon Style tab

### Style

The Style tab handles assigning color to the shape and managing its transparency.

Color The Color parameter controls fix the color of both fill and border coming from the sPolygon node. To pick a shape color, click the color disclosure arrow and work the color swatch, or drag the eye dropper into the viewer to lift a color out of an image. With the RGBA sliders or number fields you can key in the value of each color channel or the Alpha channel's strength. Allow Combining With this checkbox on, the Alpha channel value holds steady, even while passing through downstream nodes that might overlap the shape with copies of itself. With it off, the Alpha channel value can climb wherever the shape overlaps itself. For example, if a rectangle Alpha channel reads .5, turning on the Allow Combining checkbox preserves that value even when the shape moves through a duplicate or grid node that overlaps the shape and Alpha channel. Leaving the checkbox off lets the Alpha channel values compound at each spot of overlap.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the "The Common Controls” section.

### Adding Points

Adding Points to a polygonal shape stays fairly straightforward. Right after you drop the node into the Node Editor, no points exist yet, but the tool sits in Click Append mode. Click once in the viewer at every spot the shape needs a point. Keep clicking to trace out the shape. With the shape finished, click the first point again to close it. Once closed, the polyline's mode flips to Insert and Modify. From there you can tweak and tack on more points by clicking the polyline's segments. To freeze the shape and shield it from accidental edits, switch the Polyline mode over to Done using the Polyline toolbar or contextual menu.

### The sPolygon toolbar

Any time you add a Polygon (or B-Spline) shape onto a node, a toolbar appears over the viewer, keeping the modes close at hand. Rest the pointer on any toolbar button and a tooltip pops up to explain that button's role.

- Click: Click is the default choice while building a polyline (or B-Spline) shape. It works as a Bézier style drawing tool. A click drops a control point, and clicking once more somewhere else appends the next one.
- Draw: Draw acts as a freehand drawing tool, producing a shape much like sketching with a pencil on paper. Use the Draw tool to start a fresh shape, or to lengthen an open spline that already exists by selecting the Draw tool and resuming from its last control point.
- Insert and Modify: Insert drops a fresh control point onto the spline and lets you adjust it.
- Modify Only: Modify lets you safely reposition or smooth any existing spline point without

the worry of tacking on new points by accident.

- Done: Blocks every spline point from being repositioned or adjusted, and no new points can

go on either. The whole spline, though, can still be moved and rotated.

- Close: Seals up an open spline.
- Smooth: Switches the chosen control point from linear into a smooth curve.
- Linear: Switches the chosen control point from a smooth curve into linear.
- Select All: Grabs every control point on the spline at once.
- Show Key Points: Toggles the spline's control points between shown and hidden.
- Show All Handles: Toggles the polyline's Bézier handles between shown and hidden.
- Shape Box: Drops a reshape rectangle around the chosen spline shape. With that reshape

rectangle, deforming clusters of control points or whole shapes goes far easier than editing one point at a time.

- Delete Points: Removes whichever control point(s) you've selected.
- Reduce Points: Brings up a Freehand precision window for trimming the count of control points on a spline. That can ease editing of the paint stroke, particularly one made with the Draw tool.

Adjust how the toolbar appears by right-clicking on it and picking from the choices shown in the toolbar's contextual menu.

### sRectangle

### The sRectangle node

The sRectangle node serves to build rectangular shapes. As with nearly every shape node, the sRectangle node's output is only viewable through a sRender node.

### External Inputs

This node generates shapes and does not have any inputs.
