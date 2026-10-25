# Spline editor control summary and choosing which parameters to show

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](keyframes-editor-control-summary-and-adjusting-clip-timings.md) / [Next section](essential-spline-editing-tools-and-modes.md)
<a id="source-choosing-which-parameters-to-show"></a> <a id="source-essential-spline-editing"></a> <a id="source-spline-editor-control-summary"></a>

### Spline Editor Control Summary

Up top, a row of Zoom and Framing controls lets you adjust the work area holding the curves.

- Scaling the editor's size is done with the vertical and horizontal zoom controls.
- A Zoom to Fit button brings the full width of every curve in line with how wide the Spline Editor currently is.
- A Zoom to Rect tool has you draw out a rectangle that marks a region of the Spline Editor to zoom in on.

For a time reference—plus a place to scrub the playhead along—there's a Timeline ruler. The Parameter list off to the left is where you settle which splines are on view in the Graph view. By default, the Parameter list presents every parameter of every node in a hierarchical list. Beside each name sit checkboxes that reveal or conceal the curves belonging to different keyframed parameters. Color controls let you tailor each spline's tint so splines stand out more easily in a crowded situation. The Graph view, which fills most of this panel, lays out the animation spline along two axes. Time runs along the horizontal axis, while the spline's value runs along the vertical axis. Selected control points report their values in the edit fields down at the bottom of the graph. Finally, the toolbar along the bottom of the Spline Editor offers controls for setting control point interpolation, spline looping, or picking Spline editing tools for various jobs.

### Choosing Which Parameters to Show

Before you set about editing splines to tailor or build animation, you'll need to pick which parameter's splines you mean to work on. To show every parameter in every node:

- Click the Splines Editor Option menu and pick Expose All Controls. Flip this control off again to return to whatever you'd been viewing beforehand.

To show splines for the currently selected node:

- Click the Splines Editor Option menu and pick Show Only Selected Tool.

### Essential Spline Editing

The Spline Editor is a deep, capable space for editing and retiming keyframes and splines, but the overview below will get you going with this tool for building and refining animation. To select one or more control points:

- Clicking any control point selects it.
- Command-click several control points to select all of them.
- Draw a bounding box round several control points and they get selected together as one group.

To edit control points and splines:

- Click at any spot along a spline to drop in a control point.
- Drag one or more selected control points to reshape the spline.
- Shift-drag a control point to pin its motion to the vertical or horizontal.

To edit Bézier curves:

- Pick any control point and its Bézier handles appear, ready to be dragged.
- Command-drag a Bézier handle and the angle joining the left and right handles snaps apart.

To delete control points:

- Pick one or more control points, then hit the Delete or Backspace key.
