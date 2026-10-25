# A curvy path defined by a spline shape and a displacement curve in the spline editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating with motion paths.
[Chapter index](INDEX.md) / [Previous section](animating-using-motion-paths-and-types-of-motion-paths.md) / [Next section](compound-motion-path-centers.md)
<a id="source-a-curvy-path-defined-by-a-spline-shape"></a> <a id="source-a-displacement-curve-in-the-spline-editor"></a> <a id="source-locked-points"></a> <a id="source-locked-points-on-a-path-in-the-viewer"></a> <a id="source-locking-and-unlocking-points"></a> <a id="source-switching-default-paths"></a> <a id="source-the-paths-displacement-spline-with-locked-keyframes"></a> <a id="source-tips-for-manipulating-motion-paths"></a> <a id="source-types-of-control-points"></a> <a id="source-unlocked-points"></a> <a id="source-using-a-path-modifier-to-adjust-orientation"></a> <a id="source-xy-path"></a>

### A curvy path defined by a spline shape

How fast the bee travels isn’t set by the curved shape of the path. At any given spot along the path, the bee’s speed comes down to the Displacement parameter. You can govern that Displacement parameter from the Modifiers tab or from the Spline Editor. To wield the Displacement parameter for an object’s speed on a path, proceed like so. 1 Park the playhead at the animation’s opening. 2 In the Modifiers tab, drag the Displacement parameter to 0.0. That plants the object at the path’s start. 3 Click the Keyframe button just right of the Displacement parameter. 4 Move the playhead deeper into the comp and drag the Displacement parameter until the object rests where you want it for the current frame. 5 Keep updating the playhead and the Displacement parameters at the comp’s key moments until you arrive at the path’s end. With the first pass of animation laid down, the Displacement curve in the Spline Editor lets you refine the timing. To refine an object’s timing along a path: 1 Open the Spline Editor and switch on the Displacement spline in the header. 2 Slide control points horizontally toward each other to quicken the pace between them while keeping the object’s spot on the path. A longer, flatter curve linking two points signals a gentler rate of change. 3 Drag a control point up or down to move its location on the path while holding the timing between two points steady.

### A Displacement curve in the Spline Editor

TIP: Keep Option pressed as you click the spline path in the viewer and a fresh point joins the spline path without any Displacement keyframe landing in the Spline Editor. That way you reshape the path while leaving the speed along it untouched.

### Using a Path Modifier to Adjust Orientation

Orienting the object along the path is the Heading parameter’s job. Say you want our animated bee to auto-orient according to which way the path runs — you’d tie the bee’s angle to the Heading parameter. To link the Heading with an object’s angle: 1 Within a Transform node, right-click that object’s angle parameter. 2 Pick Connect To > Path > Heading. Within our sample comp, the bee now auto-orients as the path dips and climbs.

The Transform’s angle parameter wired to the path modifier’s Heading parameter

### XY Path

In contrast to a Polyline path, the XY path modifier leans on separate Spline Editor splines, one figuring the X-axis position and the other the Y-axis. To animate a coordinate control through an XY path modifier:

- Right-click either the viewer’s center coordinate control or, in the Inspector, the Center X/ Y parameter, then pick Modify With > XY Path off the contextual menu.

Adding the XY Path modifier to a Center parameter in the Inspector On the surface, XY paths behave much like Polyline paths. With the modifier in place, build the path by parking the playhead and dragging the onscreen control to where you want it. Park the playhead once more and shift the onscreen control to its next spot. What sets them apart is that the control points exist purely for spatial placement. No Displacement parameter is on hand to manage temporal placement.

XY path modifier controls in the Modifiers tab of the Inspector

Rather than dragging in the viewer, you can build a motion path from the controls in the Modifiers tab, with the object’s own Inspector controls acting as an offset against that motion path. Use the XYZ parameters to place the object, the Center X/Y parameters to place the whole path, the Size and Angle to scale and turn the path, and the Heading Offset control to tune orientation.

Animating a snippet of text by means of an XY path modifier Working with XY Paths inside the Spline Editor For the XY path, the Spline Editor shows the X and Y channel splines. Any change you make to the path in the viewer or the Inspector turns up as keyframes on those splines in the Spline Editor. In contrast to a Polyline path, XY paths carry no Displacement curve. The object’s speed along the path is bound to the path itself and can’t be pried apart from the timing of the keyframes that shape it. TIP: XY path and Poly path can be flipped into one another from the contextual menu. That lets you switch methods to fit the moment without redoing your animation. The strength of the XY path modifier is that you can pin an exact XY coordinate to a precise time for tighter control.

XY Path shows X and Y curves in the Spline Editor yet carries no Displacement control.

### Switching Default Paths

To make XY path the default path type, go in Fusion Studio to Fusion > Preferences > Globals, or, within DaVinci Resolve, to Fusion > Fusion Settings. Inside the Settings window, pick the Defaults category and set the Point With drop-down menu to XY Path. From then on, keyframing the Center X/Y parameter or picking Animate from CenterX/Y’s contextual menu calls up an XY path modifier rather than a Polyline path.

### Types of Control Points

In the viewer, an XY path’s control points are tied to the control points on the X and Y curve over in the Spline Editor. Both hold the same count of points, and dropping a control point in one place drops it in the other too. A Polyline path doesn’t work that way. Polyline paths are built from locked and unlocked points. What makes a point locked is the manner in which it was added to the Polyline. A locked point on the motion path in the viewer has a matching point on the Displacement spline in the Spline Editor; an unlocked point has no such counterpart. Each behaves differently, as laid out below.

### Locked Points

On a motion path, locked points play the role keyframes do. You make them by shifting the playhead and then moving the animated control. Such a point declares that the animated control has to sit at a particular position on a particular frame. In the viewer, locked points show up as larger hollow squares. Every locked key has a matching point on the path’s Displacement curve in the Spline Editor.

### Locked points on a path in the viewer

Removing a locked point from the motion path reshapes the motion’s overall timing.

To alter a path’s duration by way of locked points: 1 Wire an object to a Transform node. 2 Set the spot where you want the motion path to begin.

A graphic set on the right-hand side of the frame 3 Park the playhead at frame 0. 4 Pick the Transform node and, in the Inspector, click the Keyframe button just right of the Center X/Y parameter. That attaches the path modifier and lays down the path’s first locked point. 5 Park the playhead at frame 45. 6 Drag the object’s center to the lower middle of the screen.

Advancing the playhead and relocating the bee drops a second locked point That establishes the second locked point.

7 Open the Spline Editor and bring up Path1’s Displacement spline.

### The path’s Displacement spline with locked keyframes

With a value of 0.0, the control sits at the path’s opening. Once the Displacement spline reads 1.0, the control sits at the path’s close. 8 Grab the keyframe at frame 45 in the Displacement spline and drag it over to frame 50. The motion path now runs 50 frames, and its shape hasn’t budged. Try pulling this point’s value from 1.0 down to 0.75 and it won’t take, because as the animation’s final point its value in the Displacement spline has to stay 1.0. 9 Park the playhead on frame 100 and drag the bee center up to the screen’s top-left corner.

Shifting locked points alters a motion path’s duration while leaving its shape alone That drops one more locked point and gives the path a new endpoint.

### Unlocked Points

Unlocked points come about when you tack extra points onto the motion path while in Insert and Modify modes. Such points serve to reshape the motion path overall without directly touching the motion’s timing. In other words, you can pile on as many unlocked points as you like to rework a motion path, and none of it disturbs the timing of that path’s animation. That makes refining a motion path spatially far easier once you’ve nailed the animation’s timing temporally. Unlocked points carry no counterpart on the path’s Displacement spline. In the viewer they show as smaller, solid square points. To put unlocked points onto a motion path, proceed like so: 1 Pick a motion path spline by tapping Tab to cycle through controls until the path is the one selected. 2 To drop points along a path, click the Insert and Modify button on the toolbar. 3 Click the path and lay down two fresh points: one midway between the first and second points, the other midway between the second and third. Those two newly added points don’t appear on the motion path’s Displacement spline. They’re unlocked points, there to shape the motion but disconnected from the path’s timing.

Unlocked points placed on the motion path don’t show on the Displacement spline Unlocked points can go onto the Displacement spline too. Extra unlocked points in the Spline Editor can be put to work making the object’s motion hold for a moment.

To stall motion along a motion path with an unlocked point: Grab a locked point on the Displacement spline, then keep Command pressed as you drag that point horizontally to a different frame. The point is duplicated as an unlocked point at the new frame.

Build a hold in the motion by duplicating locked points Grasping how locked and unlocked points differ hands you separate command over the spatial and temporal sides of motion paths.

### Locking and Unlocking Points

Flip an unlocked point into a locked one, or the reverse, by selecting the point(s) and picking the Lock Point option off the contextual menu.

### Tips for Manipulating Motion Paths

Several different approaches let you build and edit motion paths within the viewer.
