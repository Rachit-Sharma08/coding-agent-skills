# Warper curves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Warper studio version only.
[Chapter index](INDEX.md) / [Previous section](vortex-and-warper.md) / [Next section](warper-and-waviness.md) / [Warper (Studio Version Only)](vortex-and-warper.md)
<a id="source-advanced-options"></a> <a id="source-curves"></a> <a id="source-on-screen-controls"></a> <a id="source-points"></a> <a id="source-selected-curve"></a> <a id="source-selected-points"></a>

### Curves

- Add: While this mode is active, you add points to build a curve or shape to warp around.
- Adjust: While this mode is active, you reshape the curve or shape you’ve built apart

from the warp.

- Warp: While this mode is active, the picture warps around the curves or shapes you’ve

built and refreshes live as you shift them.

- Render a Reference Grid: Tick this box to lay a reference grid over the picture, so you can gauge

exactly how strongly the warp touches each region of the frame.

- Origin Reference: Moving this slider changes how visible the original curve

and point positions are. Drag right to raise their intensity, drag left to make them transparent.

- Position Keyframing: Keyframes the positions of the curve points.
- Warp Keyframing: Keyframes the warps of the curve points.
- Warp Strength: Drag this slider to intensify or weaken the warp's distortion effect.

### Selected Points

- Symmetric: Renders the chosen point (or every point along the chosen curve) symmetric relative to the chosen control point.
- Corner: Turns the chosen point (or every point along the chosen curve) into hard corners.
- Rounded: Turns the chosen point (or every point along the chosen curve) into rounded corners equipped with

spline controls.

- Reset Handle Adjustments (Warp mode): Click this button to return a point's spline curve tweaks

to neutral.

- Reset Warp (Warp mode): Click this button to send the warp back to its original neutral condition.

### Selected Curve

- Show All Handles: This checkbox switches on or off every spline handle for all the points along a curve.
- Open/Close: Click this button to flip between closing a curve (joining the last point to the first point) and opening it (cutting that connection).
- Warper/Limiter: Click this button to swap a curve between a warper and limiter curve. A limiter curve stops warping inside the area it covers.
- Delete: Deletes an entire curve.

### Points

- Render a Reference Grid: Tick this box to lay a reference grid over the picture, so you can gauge exactly how strongly the warp touches each region of the frame.
- Positions: Keyframes the positions of the points in the Viewer.
- Show Origin Locations: Reveals where every point in the Warper originally sat.
- Clear All Points: Wipes out every added point and resets the Warper to neutral.
- Reset Warp: Sends the Warper back to neutral yet keeps every added point at its

origin position.

- Warp Strength: Drag this slider to intensify or weaken the warp's distortion effect.

### On-Screen Controls

- Show: Shows the on-screen controls in the Viewer.
- Auto Hide: Displays the on-screen controls in the Viewer but conceals them only while they're being adjusted,

so you can watch the finished picture as you make changes.

- Hide: Hides the on-screen controls in the Viewer.
- Warp Boundaries (Points Only): This pop-up menu provides three options for showing which

regions of the picture get locked off by limiter points you set on the picture. None: Conceals this information and is the default setting. As Border: Draws a red line at the edge where warping turns locked off. As Mask: Dims the region that limiter points shield from warping.

- Scale Controls: This slider lets you shrink or enlarge the control points or warp vector handles to whatever size suits the work at hand.

### Advanced Options

- Limits: A pop-up menu lets you decide how the picture's edges behave while you're warping it.

Pin at Corners: Holds the picture's four corners fixed, yet lets the sides bow in or out as you warp and lets blanking sneak in. Around the Edges: Holds the entire width and height of all four edges fixed while you warp, blocking blanking. Distant: Holds in place picture areas that sit n pixels off, though the default setting is quite loose. Manual (Free-Floating): Permits warping the whole picture without anchoring any part, enabling extreme warps across an entire picture edge, but obliging you to set at least one limiter point before you add a warp point.

- Elasticity: A pop-up menu lets you pick one of three ways to interpolate how the picture flexes around a Warp point: Fabric, Rubber (the default), and Jelly. Fabric yields the “most pointy” warps, whereas Jelly yields the gentlest curved warps. Rubber lands midway between those two extremes..
