# Polygon mask and ranges mask Fusion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Polygon mask, Ranges mask Fusion.
[Chapter index](INDEX.md) / [Previous section](multipoly-and-polygon-mask.md) / [Next section](ranges-mask-fusion-controls.md) / [Continue Ranges Mask RNG FUSION / Controls Tab](ranges-mask-fusion-controls.md) / [Polygon Mask Ply](multipoly-and-polygon-mask.md)
<a id="source-adding-points"></a> <a id="source-b-spline-mask-polygon-toolbar"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-1"></a> <a id="source-inputs-2"></a> <a id="source-ranges-mask-node-introduction"></a> <a id="source-ranges-mask-rng-fusion"></a> <a id="source-the-ranges-node"></a>

### Common Controls

Image and Settings Tabs The Inspector's Image and Settings tabs also recur across the other mask nodes. You will find these common controls fully described at this chapter's end, within the "The Common Controls" section.

### Adding Points

Putting points onto a polygonal effect mask is fairly straightforward. Right after the node lands in the Node Editor there are no points yet, but the tool sits in Click Append mode. Click once in the viewer at each spot where the mask needs a point. Keep clicking to trace the mask's shape. With the shape finished, click the first point again to close the mask. Once the shape is closed, the polyline's mode shifts to Insert and Modify. That lets you adjust and add further points to the mask by clicking on the polyline's segments. To lock the mask's shape and guard against accidental changes, set the Polyline mode to Done from the Polyline toolbar or the contextual menu.

### B-Spline Mask Polygon toolbar

Adding a Polygon (or B-Spline) mask to a node makes a toolbar appear above the viewer, giving quick access to the modes. Rest the pointer on any toolbar button to bring up a tooltip explaining what that button does.

- Click: Click is the default choice while you build a polyline (or B-Spline) mask. It works as a Bézier style drawing tool. A click drops a control point, and clicking again at another spot appends the next control point.
- Draw: Draw is a freehand drawing tool, making a mask the way you might sketch with a pencil on paper. Use the Draw tool to start a new mask, or to extend an open spline already there by clicking the Draw tool and resuming from the last control point.
- Insert: Insert drops a fresh control point onto the spline.
- Modify: Modify lets you safely reposition or smooth any existing point on a spline with no risk of dropping new points by accident.
- Done: Stops any point on the spline from being moved or modified, and bars new points from being added. You can still, however, move and rotate the whole spline.
- Closed: Closes an open spline.
- Smooth: Turns the selected control point from a linear corner into a smooth curve.
- Linear: Turns the selected control point from a smooth curve into linear.
- Select All: Selects every control point on the spline.
- Keys: Reveals or conceals the control points along the spline.
- Handles: Reveals or conceals the Bézier handles along the polyline.
- Shape: Drops a reshape rectangle around the selected spline shape. With that reshape rectangle, deforming groups of control points or entire shapes is far easier than editing each point.
- Delete: Removes the selected control point(s).
- Reduce: Opens a Freehand precision window for cutting down the number of control points on a spline. That can make the paint stroke simpler to edit, particularly when it was made with the Draw tool.
- Publish menu: The publish menu lets you choose between publishing the control points or the path. Publishing is a kind of parameter linking that makes the chosen item available to other controls. It also lets you tie a control point to a tracker.
- Follow Points: Lets a selected point trail the path of a published point, trailing it at an offset position.
- Double Poly: Lets you soften part of the spline curve while leaving other stretches of the curve sharp. The double polyline consists of two shapes, an inner and an outer one. The inner shape is the original shape from the single polyline, while the outer shape governs how far the softness spreads. The farther the outer shape sits from the inner shape, the softer that stretch of the shape grows. Both polylines begin matching the original single polyline exactly, so the mask starts off sharp. Whatever animation was already on the shape carries over. To select the outer shape, tap the Tab key to step through the onscreen controls until the dashed outline shows, or pick the outer polyline from the contextual menu's Controls > Outer Polygon menu.
- Multiframe: Multiframe is a way of editing control points across several keyframes. At the default of none, only a spline's control point on the current keyframe is changed. Setting the menu to All edits the control point on every keyframe. Prev edits the current and previous keyframe, while Next edits the current and next keyframe.
- Onion Skinning: Switching on onion skinning shows a blend of the spline animation in the viewer. It helps when you are lining up spline animation with motion. Picking Onion Skin Settings from the drop down menu lets you set how many overlapping frames appear.
- Roto Assist: Turn on the Roto Assist button as you start painting with the Polyline Stroke tool. As you click to build up the shape's points, the polyline points snap onto the closest edge. A cyan outline flags the points that have snapped onto an edge. The drop down menu offers three chief Roto Assist options: Multiple Points: When on, a single click on a high contrast edge drops several points to map the entire edge at once, sparing you from placing each point on its own. This is a one time only click; the next click reverts to single point edge detection. Distance 8: Opens a dialog for setting the pixel range across which the edge search runs. Reset: Clears the snap attribute on every snapped point. Once reset, those points are no longer available for tracking.

Alter how the toolbar appears by right-clicking it and picking from the choices in the toolbar's contextual menu. The Polylines chapter covers what each of this toolbar's buttons does in depth.

### Ranges Mask [RNG] FUSION

### The Ranges node

### Ranges Mask Node Introduction

Much like the Bitmap mask, the Ranges mask lets images from the node tree serve as masks for nodes and effects. Rather than making a plain luminance-based mask out of a single channel, Ranges supports spline-based selection of low, mid, and high ranges, much as the Color Corrector does.

### Inputs

Within the Node Editor, the Ranges mask node carries two inputs. Input: The orange input takes a 2D image that the mask is built from. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask into this input merges the masks, and how that merging is done is set in the Inspector's Paint mode menu.

### Basic Node Setup

You do not strictly need the Ranges node to feed an image into the effect mask input, but, as with the Bitmap node, it opens up options not otherwise on offer. It permits choosing channels beyond RGBA for the mask, plus softness and clipping. In the node tree below, the Ranges node pulls the composite out of the merge and builds a mask for the color correction.

A Ranges node picks out a particular range within the image so as to build a mask.
