# Offset angle distance position and path

Version: DaVinci Resolve 20.3 Reference Manual. Context: Offset angle distance position, Path.
[Chapter index](INDEX.md) / [Previous section](midi-spline-and-position-modifiers.md) / [Next section](perturb.md) / [Offset (Angle, Distance, Position)](midi-spline-and-position-modifiers.md)
<a id="source-controls-tab-3"></a> <a id="source-example-1"></a> <a id="source-inspector-4"></a> <a id="source-path"></a> <a id="source-the-path-modifier-controls-tab"></a>

### Example

Here's a basic comp showing one way offsets might come in handy.

- Make a fresh Comp running 100 frames.
- Build a node tree where a black background and a foreground Text node both feed

to a Merge.

- Over in the Text Layout tab, drive the text across the frame with the Center X control, taking it from one edge

over to the other.

- Jump to frame 0.
- Inside the Text tab in the Inspector, right-click the Size control and pick Modify With > Offset

Distance off the contextual menu. That drops in two onscreen controls: a crosshair standing for the position and an X control standing for the offset. Those onscreen controls mirror the Position and Offset controls shown in the Modifiers tab. From here the text's size rides on the gap, or offset, separating the two onscreen controls.

- Drag the X onscreen control around in the viewer and watch how its distance from the crosshair drives the size of the merge, and through that the text. The crosshair and the X onscreen controls are both animatable and can link to other controls.
- Position the X centered at the bottom of the viewer.
- In the Inspector, select the Modifiers tab.
- Within the Offset on Text size section, right-click on Position and pick Connect To >

PathConnect the Offset's position value onto the path that's already present by right-clicking the Position control and selecting Connect To > Path1 Position.

- Play the comp to view the animation.

Now the text contracts toward the middle of the path (where the gap between the offset and the path bottoms out) and swells at the path's ends (where that gap between the offset and the path peaks).

### Path

Two splines drive the Path modifier's animation of points: an onscreen motion path (spacial) and a Time spline you see in the Spline Editor (temporal). To put an object's position control under a Path's control, right-click that Position control (in the Inspector, or else in the viewer) and choose Path from the contextual menu. That lays a keyframe at the present position. Begin a path by moving the playhead and dragging the center position control around the viewer. The Spline Editor shows a displacement spline for editing the path's temporal value, its "acceleration."

### Inspector

### The Path modifier Controls tab

### Controls Tab

The path's Controls tab lets you scale, move, and rotate the path. It also carries the Displacement parameter, which lets you govern the acceleration of an object riding the path. Center Where the path actually centers. This too can be changed and animated to slide the whole path around. Size How big the path is. Once again, this leaves the animation open to later changes.

X Y Z Rotation The path can turn across all three dimensions for sophisticated control. Displacement Every motion path comes paired with a Displacement spline in the Spline Editor. The Displacement spline marks where the animated element sits along its path, given as a value from 0.0 to 1.0. You use Displacement splines to govern how fast — or how accelerated — an object's travel along the path is. To slow, hasten, halt, or even back up the control's motion along the path, change the values of the points for the path's displacement, whether in the Spline Editor or in the Inspector.

- When the Displacement reads 0.0 in the Spline Editor, the control sits right at a path's start.
- When it reads 1.0, the control has reached the path's far end.
- Every locked point along the motion path in the viewer is paired with a point on the

Displacement spline.

- Unlocked points show a control point in the viewer yet carry no matching point on the

Displacement spline. Heading Offset Wiring to the Heading tunes how the object auto-orients along the path. So, for example, when a mask's angle is wired to the path's heading, the mask's angle swings to match the path's angle. Right-Click Here for Shape Animation You can animate the shape of the path too, or wire it to other path controls such as Polyline Masks or Paint Strokes. TIP: Switching Default Paths You're free to change which default path type gets used when you animate a position or center control to a path (should you favor that kind of animation). Open the Preferences window and pick the Global Settings. Under the Default category, open the Point With menu and choose Path. From then on, choosing Animate from a Position or Center control's contextual menu brings up a path.
