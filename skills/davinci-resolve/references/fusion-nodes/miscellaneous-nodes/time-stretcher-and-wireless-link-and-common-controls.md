# Time stretcher and wireless link and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Time stretcher, Wireless link, Common controls.
[Chapter index](INDEX.md) / [Previous section](time-stretcher-inputs.md) / [Next section](common-controls-common-miscellaneous-settings-tab.md) / [Time Stretcher TST](switch-and-time-speed-and-time-stretcher.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-example"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-the-common-controls"></a> <a id="source-the-time-stretcher-controls"></a> <a id="source-the-wireless-link-node"></a> <a id="source-wireless-link-node-introduction"></a> <a id="source-wireless-link-wire"></a>

### Basic Node Setup

Just as with the Time Speed node, wiring up the Time Stretcher amounts to nothing more than feeding a 2D image into the node’s orange background input.

A MediaIn node whose timing is ramped across a range of speeds inside the Time Stretcher node.

### Inspector

### The Time Stretcher controls

Source Time This setting picks which frame of the source sequence sampling starts from. The moment a Time Stretcher node joins the node tree, its Source Time control already holds a Bézier spline whose lone keyframe sits at 0.0. Where that keyframe lands depends on the playhead time as the node is dropped into the node tree. NOTE: You may not see the Source Time spline right away, not until you pick Edit from the Source Time’s contextual menu, or until Display all Splines is chosen from the Spline Window’s contextual menu. Interpolate Mode Through this menu you set how the speed change is computed so playback looks better, which matters most for clips that have been slowed. The menu holds three options.

- Nearest: The least demanding and simplest processing approach; frames simply get dropped for quick motion or repeated for slow motion.
- Blend: Likewise light on the processor yet capable of smoother output; neighboring duplicate frames are cross-dissolved to even out slow or fast motion.
- Flow: The most demanding option but also the finest in quality for speed effects. Drawing on vector channels precomputed by an Optical Flow node, fresh frames are synthesized to build slow or fast motion. Outcomes can be remarkably smooth when a clip’s motion runs linear. That said, two elements moving across each other in opposite directions, or erratic camera movement, may introduce unwanted artifacts.

Sample Spread Only visible with Interpolation set to Blend, this slider sets how strongly the interpolated frames weigh on the current frame. At 0.5 it mixes 50% of the preceding frame with 50% of the following frame and 0% of the current frame. Depth Ordering Shown only when Interpolation is on Flow, the Depth Ordering decides which portions of the picture draw on top. An example explains it best. With a locked-off camera and a car crossing the frame, the static background yields small, slow vectors. The car yields larger, faster ones. Here the Depth Ordering is Fastest on Top, because the car paints over the background.

When instead the camera pans along with the car, it’s the background that now carries the faster vectors and the car the slower ones, so the Depth ordering would switch to Slowest on Top. Clamp Edges This checkbox surfaces only with Interpolation set to Flow. In some cases it can clear the transparent gaps that occasionally show along the borders of interpolated frames. Clamp Edges may introduce a stretching artifact near the frame’s borders, most noticeable where objects pass through or where the camera moves. Given those artifacts, reserve clamp edges for closing only the minor gaps around the rim of an interpolated frame. Edge Softness This slider appears only when Interpolation is Flow and Clamp Edges is switched on. It works to lessen the stretchy artifacts that Clamp Edges can bring about. If more than one of the Source Frame and Warp Direction checkboxes is active, the stretching near the edges can double up. When that happens, hold the softness fairly low, near 0.01. With just one checkbox on, a higher softness around 0.03 is fine. Source Frame and Warp Direction These checkboxes appear only with Interpolation set to Flow. They govern which frames and which vectors go into building the in-between frames. Every method you tick is blended into the outcome.

- Prev Forward: Builds the new frame by interpolating from the prior frame along the Forward vector.
- Next Forward: Builds the new frame by interpolating from the subsequent frame along the Forward vector.
- Prev Backward: Builds the new frame by interpolating from the prior frame along the Back Forward vector.
- Next Backward: Builds the new frame by interpolating from the subsequent frame along the Back vector.

### Example

Be certain the playhead sits on either the first or the last frame of the clip you mean to affect in the project. Drop the Time Stretcher node into the node tree. That places one point on the Source Time spline at the current frame. Across the entire Global Range the Source Time value will read zero. Set Source Time to the frame number you want pulled from the original source, at whatever moment in the project it should appear. Compressing a 100-frame sequence down to 25 frames goes like this: 1. Move the Current Time to frame 0. 2. Set the Source Time control to 0.0. 3. Step ahead to frame 24. 4. Set the Source Time to 99. 5. Confirm the spline result is linear. 6. Fusion renders 25 frames by interpolating those 100 frames down to a span of 25.

7. Hold the final frame for 30 frames, then run the clip backward at normal speed. Picking up from the example above, work through the steps that follow. 8. Step ahead to frame 129. 9. Right-click the Source Time control and pick Set Key from the menu. 10. Step ahead to frame 229 (129 + 100). 11. Set the Source time to 0.0.

### Common Controls

Settings Tab The Inspector’s Settings tab also recurs across the other miscellaneous nodes. Those shared controls get a full write-up later in this chapter under the “The Common Controls” section.

### Wireless Link [Wire]

### The Wireless Link node

### Wireless Link Node Introduction

By linking one 2D node to another 2D node without a wire, the Wireless Link node cuts down on the snarl of connection lines in a node tree. Useful though Wireless Links can be, aim to leave as much of the node tree on view as you can; otherwise you forfeit one of a node tree’s key advantages.

### Inputs

This node has no inputs.

### Basic Node Setup

This node requires no setup whatsoever. It stands alone and links “wirelessly” by way of the control found in the Inspector.

### Inspector

### Controls Tab

Inside the Wireless Link node, the Controls tab offers just one Input field for the node being linked. Input To put the Wireless Link node to work, in the Node Editor drag the 2D node onto the Wireless Link node’s Input field. Whatever you alter on the source node is mirrored wirelessly in the Wireless Link node. The Wireless Link node’s output can then feed a node placed nearby.

### Common Controls

Settings Tab The Inspector’s Settings tab also recurs across the other miscellaneous nodes. Those shared controls get a full write-up in the “The Common Controls” section that follows.

### The Common Controls

Nodes performing miscellaneous tasks share several identical Inspector controls. The controls common to the miscellaneous nodes are covered in this section.
