# Vortex and warper

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vortex, Warper studio version only.
[Chapter index](INDEX.md) / [Previous section](dent-and-lens-distortion-and-ripples.md) / [Next section](warper-curves.md)
<a id="source-add-adjust-and-warp-modes"></a> <a id="source-curve-drawing-commands"></a> <a id="source-drawing-curves-in-the-warper"></a> <a id="source-editing-splines"></a> <a id="source-selection"></a> <a id="source-vortex"></a> <a id="source-warp-mode-curves"></a> <a id="source-warp-mode-points"></a> <a id="source-warper-settings"></a> <a id="source-warper-studio-version-only"></a>

### Vortex

Vortex starts off as an S shaped distortion, yet tweaking its parameters yields many kinds of warping effects.

- X and Y position: A pair of sliders shift where the warp is centered.
- Size: Sets the warp's diameter.
- Angle: Sets both the direction and strength of the warp effect; an Angle under 0 spins the

picture leftward, while an Angle above 0 spins the picture rightward.

- Power: Turns the affected region so there's a sharper edge separating the warped part from the rest.
- Swirl: Strengthens the result, winding the picture into a tighter swirl still.
- Edge Behavior: The choices in this pop-up clear away blanking that negative

distortion causes, filling black regions through one of several modes you choose; choices are Black (takes no action, keeping the blanking), Reflect, Wrap-Around, and Replicate.

### Warper (Studio Version Only)

The Warper is a free-form picture warper that relies on points or curves to nudge and stretch parts of a picture as though it were stretched rubber. Although the Warper carries plenty of options and settings, beginning with it is genuinely simple.

### Warp Mode Points

To warp some part of the picture, choose Points for the Warp mode, click somewhere on the picture to drop a warp point, then drag to shove that region of the picture wherever you'd like. Warp points appear gray. Out of the box, warp points act on the whole picture, which stays pinned at its corners. This setup makes warping broad swaths of the picture easy, for instance when you need to warp a picture edge to remove a boom dip.

(Left) the unaltered frame, (Right) that frame warped using one control point To “pin down” regions of the picture you'd rather leave alone, Shift-click to set limiter points (shown red). Pairing warp points with limiter points lets you rapidly build highly precise warps that squish and stretch picture features however you choose.

(Left) the unaltered frame, (Right) that frame warped using control (gray) plus limiter (red) points While working, Option-click any warp or limiter point you no longer want to remove it. For a clean slate, click the Reset Warp control over in the Inspector. Both warp and limiter points accept keyframes through the Positions and Warp Strength parameters.

### Warp Mode Curves

The Curves mode of the Warper builds the warp along a curve or shape rather than around plain points on a grid. That gives you finer control over your selection and yields a more organic‑looking warp on the picture. Curves mode brings extra drawing tools and keyboard shortcuts into the Viewer.

To trace a curve, choose Warp Mode Curves first, then click in the Viewer at the spot the curve should begin, drag the line to where the next point belongs, and click once more. Keep dragging lines and clicking points until the rough line or shape is in place. A curve may stay open or be closed off into a shape.

### Add, Adjust, and Warp modes

As you build a curve, you start in Add mode; this is where you lay down the first curve or shape, but as soon as you close the shape or hit Esc to quit drawing, the Warper by default moves you into Adjust mode, where you reshape the curve without tacking on more points. Next you move to Warp mode to relocate the original curve points elsewhere, which is what actually carries out the warp. You can make as many curves or shapes as you'd like to draw, and whenever one curve crosses another a point is dropped automatically at the crossing. You're free to flip back and forth between Add, Adjust, and Warp modes whenever you need.

### Curve Drawing Commands

Although most curve editing happens naturally by clicking and dragging inside the Viewer, a handful of extra keyboard commands exist too.

- Esc: Stops drawing.
- Enter: Seals the curve by joining its final point back to its first point; alternatively, just click that first point

a second time to close the shape.

- Click: Anywhere across the picture to begin a fresh curve.
- Click: Anywhere along a curve that already exists to drop in one more point.
- Click and Drag: Places a point and pulls its spline handles outward to tune how it curves.
- Shift-Click: Anywhere across the picture to begin a limiter curve. Such a curve outlines a shape

or region where warping is suppressed. The limiter curve shows up red.

- Option-Click: Starts a fresh line in Add mode, no matter whether you happen to be in Adjust or

Warp modes at the time.

- Delete: Removes a selected point or points.

### Drawing curves in the Warper

In this example, the limiter (red) shape encircling the 1 ball keeps it from warping. The straight line on the left pulls the table down and to the left along its edge, which the origin reference (dotted lines) marks as the warp's starting point while the solid line marks where the warp currently sits. The curve spanning the cluster of balls on the right reveals the spline handles belonging to whichever point is selected.

### Editing Splines

Out of the box, your “curves” resemble sharp lines more than smooth flowing curves. You shape the curve's smoothness by tweaking a point's spline handles. A point's spline handle becomes visible when you click straight on the point. Should the handles stay hidden, hold the Command key and pull the handles out from the point. Spline handles come paired by default, so moving one swings the other the opposite way. You can also work a single spline handle on its own by holding Command and clicking the lone spline handle you intend to move.

### Selection

To pick curves and points for editing, click straight on them inside the viewer. Click the shape a second time to wrap it in a bounding box. You may select the entire shape, one point, or drag a selection box around specific points. Hold shift while dragging to make a freeform selection lasso rather than a box. With the box set, scaling the points is done by dragging the bounding box at its edges. Rotate the selection by moving the mouse close to a box edge until the rotate tool shows, then click and drag to spin it. Hold Option and drag to scale the shape about the box's geometric center.

Once a bounding box surrounds a curve, you can both scale and rotate that curve.

### Warper Settings

Warp Mode: Pick the control mode used to apply the warp, either Curves or Points.
