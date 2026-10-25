# Displaying marker with the timeline and autosnap

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](navigating-around-the-spline-editor-and-markers.md) / [Next section](selecting-moving-and-deleting-keyframes-and-moving-keyframes.md)
<a id="source-adding-keyframes"></a> <a id="source-animating-with-different-spline-types"></a> <a id="source-autosnap"></a> <a id="source-autosnapping-and-markers"></a> <a id="source-b-spline"></a> <a id="source-bézier-spline"></a> <a id="source-creating-animation-splines"></a> <a id="source-cubic-spline"></a> <a id="source-deleting-animation-splines"></a> <a id="source-displaying-marker-with-the-timeline"></a> <a id="source-locked-and-unlocked-controls-points"></a> <a id="source-locked-points"></a> <a id="source-natural-cubic-spline"></a> <a id="source-three-spline-types-in-the-modify-with-menu"></a> <a id="source-unlocked-points"></a> <a id="source-working-with-keyframes-and-splines"></a>

### Displaying Marker with the Timeline

Beside each marker, the Marker List window carries checkboxes that set whether that marker shows in the Spline Editor, the Keyframes Editor, both, or neither. Fresh markers start out active across both panels. To keep a marker out of one panel, clear the matching checkbox.

### Autosnap

To help you place keyframe control points exactly along the horizontal (time) axis, the Spline Editor’s Autosnap function can be switched on. Right-click a spline and pick Options > Autosnap Points to open a submenu of four choices.

- None: Lets keyframes sit anywhere, even between frames.
- Frame: Keyframes snap onto the closest frame.
- Fields: Keyframes snap onto the closest field.
- Markers: Keyframes snap onto the closest marker.

### Autosnapping and Markers

Out of the box, a freshly made marker snaps onto the closest frame. Dragging markers with the mouse snaps them onto the current frame as well. To alter this behavior, pick Options > Autosnap Markers > None, or pick Options > Autosnap Markers > Field, from the contextual menu.

### Creating Animation Splines

An animation spline comes into being on its own the moment you keyframe a parameter in the Inspector or the Keyframes Editor. Yet you can bring an animation spline to life without laying down a keyframe first. To create a spline: Right-click the parameter you mean to animate in the Inspector, and pick Animate from the contextual menu.

Picking Animation from the menu puts a spline up in the Spline Editor Choosing Animate from the contextual menu ties the parameter to the default spline type. That’s typically a Bézier Spline, unless you swap the default spline out in the Defaults panel of the Fusion Preferences.

### Deleting Animation Splines

To strip an animation spline off a parameter, right-click that control in the Inspector and pick Remove [tool parameter’s name] from the contextual menu. Pulling a spline off a parameter actually deletes it only when no other tool in the composition is hooked to that same spline at the time.

Removing a spline from a parameter removes the animation

### Animating with Different Spline Types

Unless the Preferences say otherwise, a Bézier spline is the default. Should you want some spline type other than Bézier for the animation curve, you can pick that spline type from the Modify With contextual submenu before you set down any keyframes.

### Three spline types in the Modify With menu

- Bézier Spline: The Bézier spline is the default curve type. At every keyframe on the spline, three points set how smooth the curve runs. The first of them is the keyframe proper, standing for the value at a given moment. The remaining two act as handles that govern how smoothly the curve gets drawn for the segments leading into and out of the keyframe. Bézier ranks as the most-used spline type, since a Bézier spline lets you mix curves and straight lines together.

### Bézier spline

- Modify with > B-Spline: A B-spline leans on one lone point to set the curve’s smoothness. Rather than handles, a single control point fixes both the value and how smooth the curve is. Hold the W key while dragging the control point left or right to tune the curve’s tension.

### B-spline

- Modify with > Cubic Spline: A Cubic spline resembles a Bézier in that the spline runs through the control point. Cubic splines, however, show no handles and always form the smoothest curve they can. On that count they’re akin to B-splines. This spline type sees use almost never.

### Cubic spline

- Modify with > Natural Cubic Spline: A Natural Cubic spline behaves much like a Cubic one, save that its changes stay more confined. Adjusting a single control point leaves other tangents untouched beyond the neighboring control points on either side.

### Natural Cubic spline

### Working with Keyframes and Splines

After you’ve animated a parameter and brought up the Spline Editor, the spline’s keyframes, and with them the animation, can be worked in all manner of ways. Selecting Keyframe control points lets you move, copy, and reshape the interpolation of your animation.

### Adding Keyframes

Once a first keyframe exists, more keyframes get tacked onto a spline on their own each time you move the playhead and alter the value of that spline’s parameter. Change the strength of an animated glow at frame 15, for instance, and a keyframe carrying the new value lands on frame 15. Within the Spline Editor, you can also drop control points straight onto a spline by clicking it wherever the new keyframe should go.

Adding Keyframes at the Playhead To set a fresh keyframe at the playhead’s present spot, press Command-K on the keyboard, or right-click in the graph and pick Set Key, and a keyframe appears beneath the playhead. Adding Equal Keyframes To hold a value across several frames, right-click in the graph area and pick Set Key Equal To, which opens a submenu for adding a new keyframe set equal in value to either the previous or the following keyframe. To keep a value steady across a pair of keyframes, choose from that Set Key Equal To submenu

### Locked and Unlocked Controls Points

Animate the Center X/Y or Pivot X/Y parameters on any tool and you bring a displacement spline into the Spline Editor. That displacement spline stands for the animated object’s relative offset position as it travels its path. Because the displacement spline works in relative terms, each of its keyframes lands on a value from 0.0 up to 1.0. Where the Spline Editor reads a displacement of 0.0, the object sits right at a path’s start. Read 1.0 and the object rests at the path’s end.

The displacement spline represents the relative position along a motion path

A displacement path is built from locked and unlocked points. How you added a point to the polyline decides whether it’s locked. A locked point on the spline carries a matching point in the viewer’s motion path, whereas an unlocked point has no counterpart in the viewer’s motion path. Each behaves in its own way, laid out below. TIP: You can turn displacement splines into X and Y coordinates by right-clicking the motion path in the viewer and picking Path#: Polyline > Convert to X/Y Path.

### Locked Points

A locked point is the motion path’s counterpart to a keyframe. You make one by shifting the playhead’s position and altering the parameter value. Such points dictate that the animated object has to occupy a set position on a set frame. Since these keyframes bear only on position along the path, they can travel solely in the horizontal direction across the spline’s time axis. In the Spline Editor, locked points show up as larger lock icons. Every locked key carries a matching point on the viewer’s motion path. Delete a locked point and the overall timing of the motion shifts.

### Unlocked Points

An unlocked point comes from clicking right on the spline in the Spline Editor. Points like these grant extra say over the acceleration along the motion path while leaving the path itself alone. Going the other direction, you can drop unlocked points in the viewer to shape the motion path without touching the timing. To turn an unlocked point into a locked one, or the reverse, select the point(s), right‑click, and pick Lock Point from the contextual menu. For more on motion paths and locked keyframes, the DaVinci Resolve manual covers them across Chapters 71 and 73 while the Fusion Studio manual does so across Chapters 8 and 10.
