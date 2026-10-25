# Animating using motion paths and types of motion paths

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating with motion paths.
[Chapter index](INDEX.md) / [Next section](spline-motion-path-and-displacement-curve.md)
<a id="source-animating-using-motion-paths"></a> <a id="source-animating-with-motion-paths"></a> <a id="source-animating-with-motion-paths-part-1"></a> <a id="source-controlling-speed-and-orientation-along-a-path"></a> <a id="source-path-modifier"></a> <a id="source-polyline-path"></a> <a id="source-types-of-motion-paths"></a>

### Animating with Motion Paths

By traveling along a chosen spline shape, layers and 3D objects produce motion path animations. This chapter covers building, editing, and applying motion paths within Fusion.

### Animating Using Motion Paths

Splines (polylines) — paint strokes and masks among them — become motion paths once a path modifier is attached to them. It’s the path modifier that lays out the movement turning everyday spline shapes into motion paths. You add the path modifier one of two ways: explicitly, by applying it onto the Center X/Y or Pivot X/Y parameters; or implicitly, when you keyframe the Center or the Pivot parameters. Whichever route you take, the spline path shows up in the viewers and is then tuned visually there. Across every motion path, the viewer’s coordinate control stands for where an object or effect sits — for example, the center of a Transform or Rays node as it slides along the path. Onscreen, coordinate controls take the form of vertical and horizontal positioning arrows or an X.

A Center Offset onscreen control belonging to an object’s Transform node The nodes listed below carry parameters you can animate with path modifiers to shift an image about the composition. They include, though aren’t restricted to:

- Transform: Animate Center X/Y to drift an image about.
- DVE: Animate Center X/Y to drift an image about.
- Merge: Animate Center X/Y to drift the connected Foreground image about.
- Paint: Animate Stroke Controls > Center X/Y to drift a stroke about.
- Camera 3D node: Translation X/Y/Z
- Shape 3D node: Translation X/Y/Z

These nodes below carry parameters you can animate with paths to swing the direction of a visual effect. They include, though aren’t restricted to:

- Directional Blur: Animate Center X/Y to redirect the blur.
- Hot Spot: Animate Primary Center X/Y to drift the hot spot about.
- Rays: Animate Center X/Y to vary the angle the rays shoot out at.
- Polygon/BSpline/Ellipse/Rectangle/Triangle mask: Animate Center X/Y to

shift the mask.

- Corner Positioner: Animate Top Left/Top Right/Bottom Left/Bottom Right X/Y to relocate

each corner of the corner-pinned effect.

- Vortex: Animate Center X/Y to relocate the heart of the warping effect.

NOTE: A one-dimensional value — blur strength or merge angle, say — can’t take a motion path. You can, though, lean on the Spline Editor to shape values like these visually.

### Types of Motion Paths

Motion paths come in three varieties: Polyline paths, XY paths, and 3D motion paths meant for 3D scenes.

- Applying the path modifier produces a Polyline path. Two splines describe it: one carrying the path’s shape in the viewer, and a Displacement spline carrying the object’s speed along the path, shown over in the Spline Editor. As the default kind of path modifier, the Polyline path is what most of this chapter’s material presumes you’re using.
- For its part, the XY path modifier draws on one spline for the point’s X position and a second for the Y. Fuller coverage of the XY path modifier comes later in this chapter.
- 3D motion paths apply solely to positional controls inside 3D scenes.

### Polyline Path

Of all the motion paths, Polyline paths are the simplest to handle. The spline shape in the viewer governs the path’s shape, while one Displacement curve in the Spline Editor governs the acceleration along it. The plainest route to a Polyline motion path is keyframing a Transform node’s Center X/Y parameter in the Inspector. To build a Polyline motion path from the Center X/Y parameter in the Inspector: 1 Park the playhead on the frame where the motion starts. 2 In the Inspector, click the gray Keyframe button just right of the Center X and Y parameters. That step puts the path modifier into the Inspector’s Modifiers tab. 3 Dial in the Center X and Y for the opening keyframe’s position. 4 Park the playhead on the frame where the motion ought to shift or halt. 5 In the Inspector, alter the Center X and Y parameters, which sets a keyframe for the new spot automatically. 6 Back in the viewer, reshape and refine the motion path by choosing a control point and reaching for any of the spline controls on the viewer toolbar. 7 Open the Spline Editor and tweak the Displacement spline to steer the object’s speed along the path. Keyframing Center X/Y isn’t the sole way to attach the path modifier. Another approach attaches it to the Center X/Y parameter, done either in the Inspector or through the viewer’s coordinate control.

To attach a Polyline path to the Center X/Y parameter: 1 Park the playhead on the frame where the motion starts. 2 Place the object’s (or effect’s) center coordinate control at its opening position. 3 Now right-click that onscreen center coordinate control in the viewer — or, alternatively, the Center X and Y parameter over in the Inspector — and pick Path from the control’s contextual menu. Applying a path modifier to the center of a Transform node A path modifier now sits on the object, so even without a keyframe you can drag it to start laying a motion path in the viewer. 4 Advance the playhead to a fresh frame. 5 Drag the onscreen coordinate control, or change the Offset or Center values in the Inspector. The motion path gains a keyframe automatically, and a polyline is traced from the first keyframe to the new one.

A pair of keyframes set a few frames apart reveal a motion path that marks the animation’s direction.

6 Where the center control sits gets interpolated between the two keyframes. Keep tacking on points by advancing the playhead and resetting the object’s position until the whole motion path you’re after exists. With motion paths, closing the spline path isn’t required; leaving it open is fine. 7 When you’re done, switch the polyline into Insert and Modify mode by picking a point on the path and hitting Command-I, or by clicking the Insert and Modify button on the toolbar. Don’t fret over the motion path’s overall shape just yet. You can refine that shape later by dropping more points onto the polyline and reworking the ones already there. One last alternative for making a motion path is to draw the spline shape first and then wire a path modifier to it. With any of Fusion’s spline tools, draw the path’s shape and then hook the path modifier up to that published spline. After those two are joined together, keyframe the Displace parameter to carry an image along the path. This route comes in handy when you want a paint stroke or mask shape serving as a motion path. To press a mask shape or paint stroke into service as a path: 1 Draw a polygon mask, or a paint stroke, shaped like the path you mean to use. Closing the mask shape isn’t necessary.

An open Polyline mask shape 2 Once the shape is drawn, click the Insert and Modify button on the viewer toolbar so the mask shape stays an open spline. 3 From here you can grab any control point along the spline and press Shift-S to smooth it or Shift-L to make it linear. Every mask polyline ships with animation switched on, which usually isn’t what you want for a motion path. That keyframe animation has to go when you’re working from a mask shape. 4 Down at the bottom of the Inspector, right-click the “Right-click here for shape animation” label and pick Remove Polygon1Polyline.

Right-clicking at the bottom of the Inspector to strip auto-keyframing off a mask shape 5 Right-click at the bottom of the Inspector once more and choose Publish so other nodes can reach this spline shape. (With a paint stroke, first make the Stroke editable by clicking the Make Editable button in the Stroke Controls.) Doing this lights up the Modifiers tab with the Published Polyline modifier. That published spline can then dictate the shape of splines in other nodes. 6 Wire a Transform node to the image meant to trail the path. 7 Over in the Inspector, right-click the Center X/Y parameter and pick Path. That sends a path modifier into the Modifiers tab. 8 Still in the Inspector, open the Modifiers tab and double-click Path1’s heading to expose its parameters. A keyframe already sits on the Displacement parameter by default. Get rid of it so you can place your own. 9 Click the red keyframe button just right of the Displacement parameter to clear it.

Clear the automatic displacement keyframe before you lay down your own keyframes. 10 Down at the bottom of the Modifiers tab, right-click “Right-click here for shape animation” and pick Connect To > Polygon1Polyline. 11 For a fast look at where your object ended up, drag the Displacement slider to and fro. 12 The Size parameter is there if you need to scale the whole path. The Displacement slider is built to be keyframed so the object animates along the path.

### Path Modifier

Functionally, the method you pick to spawn the path modifier changes nothing. Each of the approaches above is merely a different road to the same destination. No matter how you choose to add the path modifier, the Modifiers tab holds the controls for the path.

Making a path puts controls into the Inspector’s Modifiers tab. Those path modifier controls in the Inspector let you reposition, resize, and rotate the entire path shape. Over in the Spline Editor, the Displacement parameter appears as a spline that fixes the object’s position along the path, while the Heading Offset handles orientation along it.

### Controlling Speed and Orientation along a Path

Each Polyline path carries its own Displacement spline over in the Spline Editor. That Displacement spline stands for acceleration — that is, where the animated object falls along its path — expressed as a value somewhere between 0.0 and 1.0.

A Poly path’s Displacement curve captures how an object accelerates on a path. Lower values land nearer the path’s start, and higher values creep ever nearer its finish.

Picture, for example, a bumblebee bobbing up and down while crossing the screen. Getting the bee to speed up through its rises and dips yet ease off at the peaks and troughs is a job for the Displacement curve.
