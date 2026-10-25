# Optical flow and repair frame

Version: DaVinci Resolve 20.3 Reference Manual. Context: Optical flow, Repair frame.
[Chapter index](INDEX.md) / [Next section](repair-frame-and-smooth-motion-and-tween.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-optical-flow"></a> <a id="source-optical-flow-advanced-controls"></a> <a id="source-optical-flow-node-introduction"></a> <a id="source-optical-flow-of"></a> <a id="source-optical-flow-part-1"></a> <a id="source-repair-frame-node-introduction"></a> <a id="source-repair-frame-rep"></a> <a id="source-the-opticalflow-node"></a> <a id="source-the-repair-frame-node"></a>

### Optical Flow

This chapter walks through the Optical Flow nodes that Fusion provides.

The shorthand printed beside each node name works in the Select Tool dialog while you hunt for tools, and it also serves in scripting references. Throughout this document, unless stated otherwise, node trees that depict MediaIn nodes in DaVinci Resolve stand in equally for Loader nodes in Fusion Studio.

### Optical Flow [OF]

### The OpticalFlow node

### Optical Flow Node Introduction

Using an Optical Flow algorithm, this node examines whatever clip feeds its input. Picture optical flow as a per-pixel motion vector that ties features together across a run of frames. Whatever optical flow it computes lands in the output’s Vector and Back Vector aux channels. Other nodes — the Vector Motion Blur or Vector Distort, say — can then draw on those channels. That said, Optical Flow has to render twice when you wire it into a Time Stretcher or Time Speed node. Those nodes expect the channels A. FwdVec and B. BackVec in that sequence, yet Optical Flow turns out A. BackVec and A. FwdVec as it processes. Should you find optical flow too sluggish, think about rendering it out to OpenEXR files via a Saver node. TIP: When the footage input flickers from one frame to the next, it pays to deflicker it first.

### Inputs

A lone orange image input belongs to the Optical Flow node. Input: A 2D image is what the orange background input takes. That image is the run of frames you want optical flow computed for. The Optical Flow node’s output carries both the image and vector channels. To view the vector channels, right-click in the viewer and pick Channel > Vectors, then Options > Normalize Color Range.

### Basic Node Setup

Whatever frames feed the background input are what the Optical Flow node examines. By trimming a Loader or MediaIn down to just the range you require, you keep it from analyzing frames it doesn’t need. From there, the node’s output can feed any node that makes use of vector channels, a Time Stretcher among them. TIP: While analyzing Optical Flow vectors, think about placing a Smooth Motion node after it with smoothing turned on for the forward/ backward vectors.

An Optical Flow node generating motion vectors on-the-fly. Alternatively, should the Optical Flow node prove too slow at analyzing the frames, consider rendering it out in an OpenEXR format through a Saver node. After that, import the rendered EXR file as a fresh image whose vector channels are already embedded.

An Optical Flow node rendered out through a Saver node.

### Inspector

### Optical Flow advanced controls

Controls Tab (Advanced) Once you drop an Optical Flow, Repair Frame, or Tween node into a Comp, a Method drop-down in the Inspector lets you pick between an Advanced GPU-based algorithm and a Classic CPUbased one. That Advanced method is the very same Optical Flow algorithm employed across other DaVinci Resolve pages. Warp Count Lowering this slider speeds up the optical flow computations. To grasp what this option does, bear in mind that the optical flow algorithm warps one image step by step until it lines up with the other. Past a certain point convergence is achieved, and any further warps simply squander computation time. You’re free to adjust this value to hasten the computations, though it’s wise to keep an eye on what the optical flow is doing as you do.

Iteration Count Lowering this slider hastens the computations. Notably, as with the Warp Count, pushing this option upward eventually hits diminishing returns and stops producing meaningfully better output. Out of the box this value is set to a level that ought to converge across every conceivable shot, and you can frequently lower it without hurting the disparity’s quality. Smoothness This governs how smooth the optical flow is. More smoothness helps with noise, whereas less smoothness teases out more detail. Half Resolution The Half Resolution checkbox exists solely to accelerate the optical flow calculation. It scales the input images down and tracks them to derive the optical flow. Controls Tab (Classic) Selecting Classic from the Inspector’s Method drop-down lets you fall back on the older CPUbased algorithm so Comps built in earlier versions stay compatible. This method can also suit certain Stereo3D processing better. With the Classic method, one slider at the top of the Inspector boosts performance by making proxies. The other parameters in the Advanced section fine-tune the Optical Flow vector calculations. Their defaults make a solid baseline. Most of the time the advanced settings need no adjustment; many of them give only small or diminishing returns. Even so, depending on how they’re set, rendering time can swing by as much as 10x. To trim process time, your best opening move is to experiment with the Proxy, Number of Iterations, and Number of Warps sliders and to switch the filtering to Bilinear. Proxy (for Tracking) The Proxy slider exists solely to speed up the optical flow calculation. It shrinks the input images by the proxy scale and tracks them to derive the optical flow. Computation time runs roughly in proportion to the image’s pixel count. So a proxy scale of 2 yields a 4x speedup, and a proxy scale of 3 yields a 9x speedup. Smoothness This dictates how smooth the optical flow comes out. Greater smoothness copes with noise, while lesser smoothness surfaces more detail. Edges This slider offers another take on smoothness, but ties it to the color channel. Its effect is essentially to set how closely edges in the flow trail edges in the color images. Set it low and the optical flow grows smoother and tends to overshoot edges. Set it high and detail from the color images begins leaking into the optical flow, which you don’t want. Edges in the flow wind up hugging the color-image edges more tightly. That can leave streaked-out edges once the optical flow is used for interpolation. As a loose rule of thumb, lower the value when you’re using the disparity to make a Z-channel for post effects such as Depth of Field. When the disparity drives interpolation instead, you might prefer a higher value.

Match Weight This control fixes a threshold governing how neighboring clusters of foreground/background pixels get matched across a span of frames. At a low value, large structural color features are what gets matched. At higher values, small sharp color variations get matched instead. A sound value for this slider usually falls in the [0.7, 0.9] range. In stereo 3D work, nudging this option higher tends to sharpen the matching where differences arise from smoothly shifting shadows or local lighting variances between the left and right images. Even so, you should still color match or deflicker the initial images where needed so they resemble one another as closely as possible. This option also assists with local variances such as lighting differences caused by light traveling through a mirror rig. Mismatch Penalty This option dictates how the penalty for mismatched regions climbs as they grow more dissimilar. The slider lets you strike a balance between Quadratic and Linear penalties. Quadratic comes down hard on large dissimilarities, whereas Linear shrugs off dissimilar matches more readily. Pushing this slider toward Quadratic tends to leave a disparity peppered with more small random variations, while Linear delivers smoother, more pleasing results. Warp Count Lowering this slider hastens the optical flow computations. Notably, the computation time scales linearly with this option. To make sense of what it does, recall that the optical flow algorithm warps one image incrementally until it agrees with the other. Once convergence is reached, further warps merely burn computation time. Fusion’s default is set high enough that convergence should always occur. You can adjust the value to speed things along, but it’s wise to watch what the optical flow is doing meanwhile. Iteration Count Lowering this slider hastens the computations. Here too, the computation time scales linearly with this option. As with the Warp Count, raising this option eventually meets diminishing returns and won’t deliver meaningfully better results. By default it’s set to a level expected to converge across all possible shots, and you can often drop it without eroding the disparity’s quality. Filtering This option steers the filtering operations applied during flow generation. Catmull-Rom filtering produces better results, but flipping Catmull-Rom on also drives the computation time up sharply.

### Common Controls

Settings Tab The Inspector’s Settings tab is mirrored across the other Optical Flow nodes as well. A full account of these shared controls appears at this chapter’s close, in the “The Common Controls” section.

### Repair Frame [REP]

### The Repair Frame node

### Repair Frame Node Introduction

Repair Frame swaps out damaged or missing frames, or pieces of frames marred by scratches or other fleeting temporal artifacts. Three frames are needed: the repair frame plus its two neighbors. You don’t need a separate Optical Flow node to make motion vectors here, because the Repair Frame node works out the optical flow itself — though that can slow processing down. Rather than passing aux channels through, Repair Frame wipes them once the computation finishes. Look to the Optical Flow node for its controls and settings details. TIP: When your footage shifts color from one frame to the next, the repair can sometimes show, since Repair Frame has to borrow color values from the surrounding frames to fill the gap. Reach for deflickering, color correction, or a soft-edged mask to cut down on artifacts like these.

### Inputs

The Repair Frame node carries two inputs. One hooks up the 2D image you want repaired; the other takes an effect mask. Input: The orange input handles the chief 2D image slated for repair. Effect Mask: A mask shape goes into the blue input — one drawn from polylines, simple primitive shapes, paint strokes, or bitmaps produced by other tools. Wiring a mask here keeps the repairs to specific regions.

### Basic Node Setup

The Repair Frame node studies the incoming MediaIn node and fixes single-frame defects such as dust or scratches.

A Repair Frame node configured to study a MediaIn node by way of its internal optical flow analysis.
