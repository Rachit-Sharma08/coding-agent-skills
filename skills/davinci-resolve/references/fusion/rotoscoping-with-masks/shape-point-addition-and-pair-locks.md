# Adding additional points to the shape and locking unlocking point pairs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rotoscoping with masks.
[Chapter index](INDEX.md) / [Previous section](point-editor-dialog-with-offset-values-and-reduce-points.md)
<a id="source-a-control-point-set-to-follow-published-points"></a> <a id="source-adding-additional-points-to-the-shape"></a> <a id="source-adding-and-removing-points-from-an-animated-mask"></a> <a id="source-animating-polyline-masks"></a> <a id="source-lockingunlocking-point-pairs"></a> <a id="source-publishing-specific-control-points"></a> <a id="source-removing-animation-from-a-polyline-mask"></a> <a id="source-the-publish-points-controls-in-the-inspector"></a> <a id="source-the-published-point-in-the-viewer"></a>

### Adding Additional Points to the Shape

Not every point on the inner shape needs a counterpart on the outer shape, and the reverse holds too. You’re free to drop extra control points onto either shape to fine-tune it. Animation is kept independently per polyline; even so, when you move an inner-shape point that is parented to an outer-shape point, both splines receive a keyframe. Moving a parented point on the outer shape keyframes only the outer shape’s spline. Moving a point that isn’t parented keyframes nothing but that one spline. You can switch this off completely for the polyline by choosing Polygon: Outer Polygon > Follow Inner Polyline from the contextual menu.

### Locking/Unlocking Point Pairs

To parent more control points, select the points you want, right-click in the viewer, and pick Lock Point Pairs from the contextual menu of either spline. Doing so parents the chosen outer-shape point to the chosen inner-shape point. Whatever animation either point already carries survives the parenting. To break that parenting on a point, select it, right-click in the viewer, and clear Lock Point Pairs in the contextual menu.

### Animating Polyline Masks

Putting masks into motion turns out to be remarkably simple. As soon as Polygon or B-Spline masks land in the Node Editor, the spline’s control points stand ready for animation. To animate one, just shift the playhead to a different frame and reshape the mask there. That deposits a fresh keyframe in both the Spline Editor and the Timeline Editor. The single keyframe holds the placement of every control point on that mask for that frame. After two or more keyframes exist, the polygon or B-Spline form interpolates on its own from each keyframe to the next. TIP: A shape’s center point and rotation aren’t animated automatically. Only the control points get that treatment. To animate the center position or the rotation, switch on keyframes for that parameter from the Inspector. To retime the whole mask animation, adjust the Keyframe horizontal position spline through the Spline Editor or the Timeline Editor. More points may be dropped onto the mask whenever you need to sharpen the shape as parts of the image gain detail.

### Removing Animation from a Polyline Mask

Should you want a Polyline mask held still, you can strip away its automatic animation. Within the Inspector for the mask, right-click near the foot of the panel where the label reads Right Click Here For Shape Animation. Then choose Remove Bézier Spline from the contextual menu. If animating it appeals to you later on, right-click that same spot once more and choose Animate.

### Adding and Removing Points from an Animated Mask

Adding a point to an animated mask drops the new point into the shape across every keyframe. Removing a point strips it from all of the animated mask’s keyframes.

### Publishing Specific Control Points

Even though a lone keyframe lets you animate a polyline’s entire shape in one move, the Spline Editor and Timeline by default surface just a single keyframe for the whole shape at any frame. That default behavior comes in handy for rapidly morphing one shape into another, yet it leaves no room for particular control points that have to be keyframed on their own apart from the rest of the shape’s points. When a tricky mask calls for finer timing or interpolation on individual control points, you can break out one or more specific points on a polyline by publishing them.

Keep in mind that publishing a control point on a polyline pulls that point off the shared animation spline. Thereafter, that one control point is animated solely through its own keyframes on its own spline. Having been removed, the point loses any link to paths, modifiers, expressions, or trackers tied to the main polyline spline. Either of these publishes the selected point or points:

- Click on the Publish Points button in the Polyline toolbar.
- Select Publish Points from the Polyline’s contextual menu.

The Polyline mask controls gain a new coordinate control for every point you publish, labeled Point 0, Point 1, and onward.

### The Publish Points controls in the Inspector

Published points are flagged onscreen by rendering that control point noticeably larger than the rest. After a published point exists, you can wire it to a tracker, path, expression, or modifier by right-clicking the control and picking the option you want from the point’s contextual menu.

### The published point in the viewer

Using “Publish to Path” to Preserve Animation Publishing a point discards whatever animation that point already held. If keeping that animation matters, though, the “Publish to Path” option is the route to take. That Polyline contextual menu command publishes the chosen points and turns their existing animation into a path. The Publish to Path button in the Polyline toolbar does the same. Using “Follow Published Points” to Add Points On occasion you’ll want control points sitting between two published points to ride along with the published points’ motion while holding onto their relative offset and shape. To that end, points within a Polyline mask can be told to “Follow Published Points” from the Polyline’s contextual menu.

Once a point on an effect mask is set to follow points, it appears as a diamond rather than the usual small box.

### A control point set to Follow Published Points

With this mode active, the new “following” control points hold their placement relative to how any published points in the mask move, all while trying to preserve that mask segment’s shape. In contrast to published points, the following points’ positions remain animatable, which lets that segment’s shape morph across time.
