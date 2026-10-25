# Moving polyline points and smoothing a polyline segment

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rotoscoping with masks.
[Chapter index](INDEX.md) / [Previous section](polyline-creation-modes-and-click-append.md) / [Next section](point-editor-dialog-with-offset-values-and-reduce-points.md)
<a id="source-deleting-selected-points"></a> <a id="source-editing-bézier-handles"></a> <a id="source-hold-command-to-adjust-one-handle-independently"></a> <a id="source-linearizing-a-polyline-segment"></a> <a id="source-moving-polyline-points"></a> <a id="source-point-editor"></a> <a id="source-rotoscoping-with-masks-part-2"></a> <a id="source-smoothing-a-polyline-segment"></a> <a id="source-transforming-individual-or-multiple-points"></a>

### Moving Polyline Points

You can shift the selected polyline points with either the keyboard or the mouse. To move selected control points with the pointer, do one of the following:

- Drag on the selected points anywhere in the viewer.
- Hold Shift while dragging to restrict movement to a single axis.
- With Option held, drag at any spot in the viewer to shift the selected control point.

To move selected control points with the keyboard, do one of the following:

- Tap the keyboard's Up or Down Arrow keys to inch a point upward or downward within the viewer.
- Hold Command-Up or Down Arrow keys to move in smaller increments.
- Hold Shift-Up or Down Arrow keys to move in larger increments.

### Smoothing a Polyline Segment

When you want to mold the polyline and steer its slope, you can opt to smooth a spline segment by working the Bézier direction handles. Smoothing the points selected on an active polyline happens any of these ways:

- Press Shift-S.
- Click the Smooth button on the Polyline toolbar.
- Choose Smooth from the polyline's contextual menu.

The Smooth button in the toolbar (Shift-S)

### Linearizing a Polyline Segment

To guarantee a polyline segment is perfectly straight, that segment has to be linearized. A linear segment lines the Bézier direction handles up with the segment, so it carries no curvature. The segment always renders as a straight line running between two points on the polyline. Linearizing the points selected on an active polyline happens any of these ways:

- Press Shift-L.
- Click the Linear button on the polyline's toolbar.
- Choose Linear from the polyline's contextual menu.

The Linear button in the toolbar (Shift-L)

### Transforming Individual or Multiple Points

Pick the points you want to transform, and then do one of the following:

- Hold T and drag to twist.
- Hold S and drag to scale.
- Hold X and drag to scale horizontally only.
- Hold Y and drag to scale vertically only.
- Hold O and drag to offset the points perpendicular to the tangent.

Wherever the pointer sits as the transformation kicks off becomes the center the transformation pivots around.

### Deleting Selected Points

You can remove a selected point or batch of points by pressing Delete or Backspace, picking Delete off the contextual menu, or clicking the Delete Point button in the toolbar. The polyline's shape shifts to reflect those points being gone. TIP: Removing every point in a polyline doesn't remove the polyline itself. To delete a polyline, you have to delete the node or modifier that spawned it.

### Editing Bézier Handles

On Bézier polylines, each control point carries two direction handles that tune the slope of a curve passing through it. These direction handles surface only while the point is selected. Dragging a direction handle tweaks the curve of the segment leaving that control point. The direction handle on the opposite side of the control point shifts in step too, holding the bond between the two handles. To sever the bond between direction handles and move one on its own, hold Command as you drag a handle. Later changes will restore the bond, unless you keep Command held through each adjustment.

### Hold Command to adjust one handle independently

When you want to change a handle's length without altering its angle, hold Shift as you move a direction handle.

### Point Editor

Through the Point Editor dialog you can relocate control points using exact X and Y coordinates. Tapping the E key on the keyboard summons the Point Editor dialog and lets you relocate one or more selected control points.

Positioning control points through the Point Editor dialog Inside the dialog box sit that point's X- and Y-axis values. Punch fresh values into those boxes and the control point relocates. Select several control points and they all snap to one position. That comes in handy for aligning control points along the X- or Y-axis. Whenever you've selected more than a single point, two radio buttons up at the dialog box's top determine whether your adjustments reach every selected point or only one. Choose the Individual option and the affected point shows up in the viewer inside a larger box. Should the selected point be the wrong one, the Next and Previous buttons at the bottom of the dialog let you shift the selection.

Beyond entering absolute coordinates for the X- and Y-axis, points can be nudged with relative offsets measured from wherever they sit now. A single click on an axis label flips that field into an offset entry. At that moment the label switches from X to X-offset, or from Y to Y-offset.
