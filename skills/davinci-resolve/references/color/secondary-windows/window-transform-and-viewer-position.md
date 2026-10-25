# Window transform controls and manipulating the window position on the viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary windows.
[Chapter index](INDEX.md) / [Previous section](power-windows-and-adding-nodes-with-windows.md) / [Next section](curve-windows-and-bezier-conversion.md)
<a id="source-drawing-curves"></a> <a id="source-manipulating-the-window-position-on-the-viewer"></a> <a id="source-window-softness"></a> <a id="source-window-transform-controls"></a> <a id="source-window-transform-controls-1"></a>

### Window Transform Controls

Windows carry transform parameters resembling those in the Sizing palette. With these you can modify the window, moving all of its control points in unison.

### Window transform controls

- Size: Grows or shrinks the whole window. The default size is 50.00.
- Aspect: Changes the window's aspect ratio. The default here is 50.00; raise it to make the

window wider, and smaller values make the window taller.

- Pan: Slides the window along the X axis. The default position is 50.00; raise it to push

it rightward, while smaller values shift it leftward.

- Tilt: Slides the window along the Y axis. The default position is 50.00; raise it to lift the

window up, smaller values move the window down.

- Rotate: 0 is the default value. Raising this parameter turns the shape clockwise, while lowering

this parameter rotates the shape counterclockwise.

- Opacity: Lets you tune how transparent a single window's input to the node's key is.
- Convergence: With “Apply stereoscopic convergence to windows and effects” turned on under the

General Options of the Project Settings, this extra Transform parameter shows up, letting you build correctly aligned convergence for a window dropped onto a stereoscopic 3D clip. For additional details on handling Stereoscopic 3D projects, refer to Chapter 15, “Stereoscopic Workflows.” These transform parameters likewise map to onscreen controls in the Viewer, which the pointer can drive directly.

### Manipulating the window position on the Viewer

Although a lot of the onscreen controls map to parameters within the Window palette, certain ones — like the control points that reshape linear, polygonal, and Curve windows — can only be moved with the pointer. Onscreen controls for window transforms:

- To pick any window: Click on one window from a group of many to select it, which makes that window's controls live.
- To move any window: Drag anywhere inside the window's onscreen control. A window's position maps to the Window palette's Pan and Tilt parameters. With a gradient window, drag the center control point.
- To resize a circular window while keeping its aspect ratio fixed: Drag one of the four blue corner points outward to grow it, or inward to shrink it. This maps to the Window palette's Size parameter.
- To squeeze or stretch a circular window, changing its aspect ratio: Drag any of the blue control points at top, bottom, left, or right. Those tweaks map to the Window palette's Aspect parameter.
- To rotate a window: Drag the inner white rotate handle at the top, in the window's middle. For a gradient, drag the bottom arrow handle.
- To change window softness: Drag any of the magenta softness handles. Window shapes carry different handle sets, which map to the Softness parameters.
- To reshape a linear window: Drag whichever white corner handle to corner-pin the window, or grab a white top, bottom, or side handle to shift an entire side segment of the window.
- To reshape a polygonal window: Switching on a polygonal window shows a plain white rectangle bearing four corner control points. Click anywhere across the rectangle's face to drop in more control points for reshaping the polygon, and drag any control point to alter the form. A polygon window tops out at 128 control points.
- To resize a curve and adjust its aspect: Shift-drag a bounding box over whichever control points you'd like to transform, then drag the box's corners to scale the points while keeping the shape's aspect ratio fixed, or drag the top, bottom, left, or right points to squeeze or stretch the shape.
- To remove control points from polygonal or Curve windows: Middle-click whichever control point you want gone.

NOTE: If you delete a control point from a polygonal window that has already been animated through the Keyframe Editor, that point will snap on and off abruptly at the keyframes that drive the animation.

### Window Softness

Every window type carries its own Softness parameters, which depend on how much that window can be adjusted.

- Circular: One parameter, Soft 1, controls the even softness around the oval's border.
- Linear: A set of four, Soft 1–4, controls the softness of each of the linear window's four

sides on its own. Magenta softness control points at top, bottom, left, and right let you set the softness of every side of the linear shape separately.

- Polygon: A pair of parameters, Inside Softness and Outside Softness, set the overall softness for a polygonal window. No onscreen softness control points are present.
- Curve: A pair, Inside Softness and Outside Softness, govern a curve's overall softness. With the onscreen controls, the magenta inside and outside softness control points can be moved independently to form whatever softness profile you require.
- Gradient: One parameter, Soft 1, controls the even softness along the gradient window's border.

### Drawing Curves

Among all the windows, the Curve window alone shows no onscreen controls the moment it's first switched on. You instead click inside the Viewer to drop in control points, sketching your own bespoke shape around whatever region you'd like to isolate.
