# Point editor dialog with offset values and reduce points

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rotoscoping with masks.
[Chapter index](INDEX.md) / [Previous section](moving-polyline-points-and-smoothing-a-polyline-segment.md) / [Next section](shape-point-addition-and-pair-locks.md)
<a id="source-adding-softness-to-a-segment"></a> <a id="source-converting-a-single-polyline-to-a-double-polyline"></a> <a id="source-creating-softness-using-double-polylines"></a> <a id="source-make-double-polyline-button"></a> <a id="source-reduce-points"></a> <a id="source-roto-assist"></a> <a id="source-shape-box"></a> <a id="source-showing-and-hiding-onscreen-polyline-controls"></a> <a id="source-stop-rendering"></a> <a id="source-the-point-editor-dialog-with-offset-values"></a> <a id="source-the-reduce-points-button-in-the-toolbar"></a> <a id="source-the-roto-assist-options-in-the-toolbar"></a> <a id="source-the-shape-box-button-in-the-polyline-toolbar"></a>

### The Point Editor dialog with Offset values

When the precise number escapes you, the dialog box also accepts arithmetic expressions. As an illustration, entering 1.0-5 nudges the point to 0.5 along whichever axis you chose.

### Reduce Points

Sketching a polyline or an editable paint stroke by hand tends to lay down far more control points than the shape actually requires for an efficient curve. Picking Reduce Points from either the polyline’s contextual menu or the toolbar opens a dialog box that lets you trim how many points define the polyline.

### The Reduce Points button in the toolbar

Redundant control points are pruned from the path while the broad form stays intact. At a value of 100, the spline keeps every one of its points. Sliding the control toward the left thins out the points along the path.

### Shape Box

Whenever you have a polyline shape, or a cluster of control points, that you’d like to scale, stretch, squish, skew, or reposition, the shape box makes those moves straightforward. Any of these actions turns it on:

- Click the Shape Box toolbar button.
- Choose Shape Box from the contextual menu.
- Press Shift-B.

### The Shape Box button in the Polyline toolbar

When points are already selected on the polyline as Shape Box mode turns on, the box wraps around exactly those points. If not, you can drag the box across whatever region of control points you’d like to capture. Grabbing a corner handle lets you resize the box freely in both the horizontal and vertical directions. Pulling a handle located on a side instead scales the polyline only along that one axis.

Dragging a side handle resizes along a specific axis Holding Command while you drag a shape box handle pivots the adjustments around the box’s center and keeps the box’s current proportions locked. Holding Shift as you drag a corner handle moves just that one handle, which permits skewed, nonuniform transformations.

Hold Shift while dragging a corner to perform non-uniform transformations

### Showing and Hiding Onscreen Polyline Controls

Telling apart individual points becomes tricky once they sit very near one another. The display can show points together with their direction handles, points by themselves, or handles by themselves. You pick among these display modes via the Show Key Points and Show Handles toolbar buttons, or through the polyline’s context menu.

The Show Key Points and Show Handles buttons in the toolbar

These choices let you declutter the onscreen view while you tweak control points crowded close together, and they help you avoid nudging controls and handles sitting right next to the one you actually mean to move.

### Stop Rendering

Each time points on the polyline shift, the outcome is drawn to the viewer so you get steady interactive feedback. Handy as that is, it can occasionally become a distraction and drag down performance on a heavy effect. You can turn the behavior off so a render only happens once the points come to rest, either by toggling the Stop Rendering button in the toolbar or by picking that item from the polyline contextual menu.

### Roto Assist

Turning on the Roto Assist button in the toolbar before you start tracing your shape causes points to lock onto the nearest high-contrast edge while you draw. A cyan outline marks every point that has locked onto an edge. Roto Assist offers three principal options. Multiple Points: Lets a single click drop several points across a whole edge rather than placing each one separately. Distance: Sets the pixel radius over which the edge search is performed. Reset: Clears the snap attribute from the snapped points. Following a reset, those points can no longer be tracked.

### The Roto Assist options in the toolbar

### Creating Softness Using Double Polylines

Every Mask node carries a standard soft edge control, but it blurs the whole mask uniformly. Yet sometimes—heavy motion blur being a common case—you need one stretch of the curve softened while the rest stays crisp. That selective effect, known as non-uniform softness, is achieved by turning the shape from a single polyline into a double polyline. A double polyline holds two shapes: an inner one and an outer one. The inner shape carries over from the single polyline, while the outer shape governs how far the softness spreads. As the outer shape drifts farther from the inner shape, that portion of the edge grows softer.

Non-uniform softness from a double polyline, built out of an inner shape plus an outer one

### Converting a Single Polyline to a Double Polyline

You turn a mask into a double polyline by clicking the Double Polyline button in the Polyline toolbar, or by right-clicking in the viewer and picking Make Outer Polyline from the mask’s contextual menu. The shape splits into an inner and an outer polyline spline. Each polyline begins with precisely the same form as the single polyline did. That keeps the mask crisp at the outset and preserves any animation you may have already attached to the shape.

### Make Double Polyline button

Control points on the outer shape are parented automatically to the points they correspond to on the inner shape. Consequently, whatever you change on the inner shape carries through to the outer shape as well. That link runs only one direction; you can tweak the outer shape without disturbing the inner shape. A dashed line drawn from point to point shows how the inner and outer shapes’ points relate.

### Adding Softness to a Segment

A green dashed line, rather than a solid one, renders the outer shape so it stands apart from the inner shape. Either of the following selects the outer soft edge shape:

- Step through the onscreen controls with the Tab key until that dashed outline shows up
- In the view, right-click on a spline and pick Controls > Select > Polygon: Outer Polygon. With the outer polyline now active, pull any of its points off the inner polyline to soften that part of the mask.

TIP: Hit Shift-A so every point on the shape is selected, then keep O held down while dragging to push those points outward from the inner shape. From there you have a base from which to refine the falloff. As the outer shape segment moves farther from the inner shape, the falloff in that region grows wider.
