# Sboolean and sbspline and schangestyle

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sboolean, Sbspline, Schangestyle.
[Chapter index](INDEX.md) / [Next section](schangestyle-and-sduplicate-and-sellipse.md)
<a id="source-allow-combining"></a> <a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-controls"></a> <a id="source-external-inputs"></a> <a id="source-inputs"></a> <a id="source-sboolean"></a> <a id="source-sbspline-sbsp"></a> <a id="source-schangestyle-scs"></a> <a id="source-shape-nodes"></a> <a id="source-shape-nodes-part-1"></a> <a id="source-style"></a> <a id="source-style-tab"></a> <a id="source-the-sboolean-controls-tab"></a> <a id="source-the-sboolean-node"></a> <a id="source-the-sboolean-style-tab"></a> <a id="source-the-sbspline-controls"></a> <a id="source-the-sbspline-node"></a> <a id="source-usage"></a>

### Shape Nodes

This chapter walks through the Shape nodes that Fusion offers.

### sBoolean

### The sBoolean node

The sBoolean node merges or removes the overlapping regions of two shapes according to a menu of boolean operations. As with nearly every shape node, the sBoolean node's output is only viewable through a sRender node.

### External Inputs

The node's tile in the Node Editor presents the inputs below. Apart from the subtract boolean operation, which shape goes to which input doesn't matter. Input1: [orange, required] This input takes the output of another shape node. It acts as the base shape once the subtract boolean operation is selected. Input2: [green, optional] This input takes the output of another shape node. It carves the hole out of the base shape once the subtract boolean operation is selected.

### Basic Node Setup

The sBoolean node serves to fuse two shape nodes together. From there, the sBoolean's output can route on to another shape node or a sRender node for viewing.

A star and an ellipse merged within an sBoolean node, then sent to an sRender for viewing and further processing Inspector

### The sBoolean Controls tab

### Controls

The Controls tab mostly exists to pick the boolean operation governing how the two shapes merge. Operation The operation menu carries four boolean operations: Intersection: Now and then called an AND operation, this setting reveals only the regions where the two shapes overlap. What you get is solely where input 1 AND input 2 overlap.

A star and ellipse with the sBoolean node in intersection mode Union: Now and then called an OR operation, this setting reveals only the regions where either of the two shapes lives. What you get is wherever input 1 OR input 2 exists. The Union setting resembles the result of the sMerge node.

A star and ellipse with the sBoolean node in union mode Subtract: Now and then called a NOT operation, this setting outputs input 1's shape but strips away the regions where input 2 overlaps. What you get is input 1 minus input 2.

A star and ellipse with the sBoolean node in subtract mode

Xor: Now and then called an AND NOT operation, this setting outputs input 1's or input 2's shape but strips away the regions where they overlap. What you get is (input 1 minus input 2) + (input 2 minus input 1).

A star and ellipse with the sBoolean node in xor mode Style Mode The Style mode menu carries just one option. The Replace setting swaps the color and alpha level of the incoming shapes for the color set within the Style tab.

### Style Tab

### The sBoolean Style tab

### Style

Whatever color was assigned to the individual shape nodes gives way to the color set through the Style tab controls. Color The color controls fix the color of the output shape coming from the sBoolean node. To pick a shape color, click the color disclosure arrow, work the color swatch, or drag the eyedropper into the viewer to lift a color out of an image. With the RGBA sliders or number fields you can key in each color channel's value or the Alpha channel's strength.

### Allow Combining

With this checkbox on, the Alpha channel value holds steady even while passing through downstream nodes that might overlap the shape with copies of itself. With it off, the Alpha channel value can climb wherever the shape overlaps itself. For example, if an ellipse's Alpha channel reads .5, turning on the Allow Combining checkbox preserves that value even when the shape moves through a duplicate or grid node that overlaps it. Leaving the checkbox off lets the Alpha channel values compound at each spot of overlap. When the sBoolean node is in play, the individual shape node checkboxes are disregarded, and the sBoolean node's own checkbox dictates the Alpha channel's behavior.

Allow Combining Enabled (left), Allow Combining Disabled (right)

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sBSpline [sBSp]

### The sBSpline node

Introduction sBSpline matches a sPolygon in every way but one. Where sPolygon relies on Bézier splines, this node relies on B-Splines. Whereas Bézier splines lean on a central point plus two handles to govern the smoothing of a spline segment, a B-Spline needs only a single point. As a result, a sBSpline shape calls for far fewer control points to land a nicely smoothed shape.

### Usage

### The sBSpline controls

When first dropped into a Node Editor, the sBSpline shape holds only its Center control, shown onscreen. You add points to the sBSpline by clicking in the viewer. Every new point links to the one made before it, but rather than the spline running straight through each control point, sBSpline control points merely sway the spline's shape. Each control point tugs the spline toward itself to form a smooth curve. Much like the sPolygon shape tool, the sBSpline shape auto-animates. Dropping this node into the Node Editor lays a keyframe on the current frame. Stepping to a new frame and altering the shape lays a new keyframe and interpolates between the two defined shapes.

### sChangeStyle [sCS]

The sChangeStyle node sChangeStyle Node Introduction The sChangeStyle node applies a fresh style across the merged shape tree, replacing whatever style—color plus Allow Combining settings—was set up in the upstream shape tools.

### Inputs

The single input on the sChangeStyle tool serves to connect the Shape node whose style you intend to change.
