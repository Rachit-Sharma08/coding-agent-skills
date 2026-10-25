# Polyline creation modes and click append

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rotoscoping with masks.
[Chapter index](INDEX.md) / [Previous section](rotoscoping-mask-attachment-and-mattecontrol.md) / [Next section](moving-polyline-points-and-smoothing-a-polyline-segment.md)
<a id="source-click-append"></a> <a id="source-closing-polylines"></a> <a id="source-done"></a> <a id="source-draw-append"></a> <a id="source-insert-and-modify"></a> <a id="source-modify-only"></a> <a id="source-polyline-creation-modes"></a> <a id="source-polyline-points-selection"></a> <a id="source-protection-modes"></a> <a id="source-selecting-and-adjusting-polylines"></a>

### Polyline Creation Modes

The toolbar offers a few different modes for building and reshaping polylines. Which mode kicks in when a polyline is first added hinges on whether it serves as a path or a mask. Each mode gets a fuller description below.

### Click Append

For mask creation, this mode is the default. You use it to lay down the mask's rough form fast, after which you move to Insert and Modify mode to sharpen the mask further.

The Click Append toolbar button (Shift-C) To make a mask via the Click Append mode, follow these steps: 1 Pick Click Append off the toolbar, or hit Shift-C. 2 Click the pointer at the spot where the shape should begin. 3 Reposition the pointer and click to tack a fresh point onto the previous one. 4 Closing the shape means hovering the mouse pointer over that first point you made and clicking once the pointer's appearance changes. Once a shape closes, the polyline flips automatically into Insert and Modify mode. The Click Append mode seldom gets used for paths, but it can come in handy when you know a motion path's overall form yet haven't pinned down the timing. TIP: Holding Shift as you draw a mask locks each new point to 45-degree angles off the prior point. That can really help when you're drawing regular geometry.

### Insert and Modify

A mask built in Click Append mode flips into Insert and Modify mode by itself the moment its shape closes. You can also switch into this mode by hand by clicking the Insert and Modify button in the toolbar or pressing the Shift-I keyboard shortcut. Working in this mode makes it simpler to drop in extra points and refine the mask's shape. Dragging the control points or direction handles reshapes points already on the polyline.

The Insert Modify toolbar button (Shift-I) Insert and Modify mode doubles as the default mode for building motion paths. A fresh control point is tacked onto the polyline's end, extending or refining the path, whenever a parameter animated along a motion path gets moved.

### Draw Append

The Draw Append mode lays down a freehand polyline shape straight on the viewer, much like sketching with a pencil or paintbrush. This mode pairs especially well with a tablet and suits building garbage mattes and effect masks around intricate shapes.

The Draw Append toolbar button (Shift-D)

### Protection Modes

Beyond the modes for building a polyline, two further modes exist to guard the points against any more changes once they've been made.

### Modify Only

Modify Only mode lets you reshape points already on the polyline, but it won't let new points be added to the shape.

The Modify Only toolbar button (Shift-M) TIP: Even with Modify Only active, you can still delete points off a polyline.

### Done

The Done mode blocks the creation of any new points along with any further reshaping of points already on the polyline.

The Done toolbar button (Shift-N)

### Closing Polylines

A polyline can be closed in several ways, each joining the final point back to the first. To close a polyline, do one of the following:

- Bring the pointer over that first point you made, then click that point.
- Press Shift-O on the keyboard.
- Click the Close button on the polyline toolbar.
- Keep drawing a polyline until the shape is ready to close, then right-click and pick Polygon:Polyline > Closed.

The Close toolbar button (Shift-O) Each of these options is a toggle that can likewise reopen a closed polygon.

### Selecting and Adjusting Polylines

To form the shape a mask or motion path calls for, you have to know how to work the splines. Fusion supplies several easy methods for selecting, moving, and smoothing a spline, plus more involved adjustment methods for scaling, skewing, and twisting one.

### Polyline Points Selection

Selecting a polyline's control points, whether one or several, can be done any of these ways:

- Click directly on the control points.
- Lasso around the points.

To add points to or drop them from the current selection, do one of the following:

- Hold the Shift key to select a continuous range of points.
- With Command held, click whichever control points you mean to add or drop.
- Press Command-A to select all the points on the active polyline.

TIP: With a control point selected, pressing Page Down or Page Up on the keyboard picks the next control point going clockwise or counterclockwise. That can really help when control points sit very close together.
