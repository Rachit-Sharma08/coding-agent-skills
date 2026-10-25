# Repair frame and smooth motion and tween

Version: DaVinci Resolve 20.3 Reference Manual. Context: Repair frame, Smooth motion, Tween.
[Chapter index](INDEX.md) / [Previous section](optical-flow-and-repair-frame.md) / [Next section](tween-and-vector-denoise-and-vector-transform.md) / [Repair Frame REP](optical-flow-and-repair-frame.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-smooth-motion-node-introduction"></a> <a id="source-smooth-motion-sm"></a> <a id="source-the-repair-frame-controls-tab"></a> <a id="source-the-smooth-motion-controls-tab"></a> <a id="source-the-smooth-motion-node"></a> <a id="source-the-tween-node"></a> <a id="source-tween-node-introduction"></a> <a id="source-tween-tw"></a>

### Inspector

### The Repair Frame Controls tab

### Controls Tab

The Controls tab holds options for how the frames get repaired. It carries controls for tuning the optical flow analysis too, the same ones found on the Optical Flow node. Depth Ordering Depth Ordering decides which portions of the image render on top, via either Fastest On Top or Slowest On Top. The scenarios below illustrate these options best. Take a locked-off camera shot with a car crossing the frame: the background stays put and so emits small, slow vectors, while the car emits larger, faster ones. Here the depth ordering is Fastest On Top, since the car paints over the background. Now take a shot where the camera pans to follow the car: the background carries the faster vectors and the car the slower ones, making Slowest On Top the right Depth Ordering method. Clamp Edges In some situations this option clears away the transparent gaps that can crop up at the edges of interpolated frames. Clamp Edges introduces a stretching artifact near the frame’s edges, most apparent when objects pass through it or the camera moves. On account of those artifacts, it’s best to reserve clamp edges for fixing only the small gaps around an interpolated frame’s borders. Edge Softness This slider shows up only while Clamp Edges is on. It helps tame the stretchy artifacts Clamp Edges might introduce. Turning on more than one of the Source Frame and Warp Direction checkboxes can double up the stretching effect near the edges. When that happens, keep the softness fairly low, around 0.01. With just one checkbox on, you can afford a larger softness near 0.03.

Source Frame and Warp Direction With these checkboxes you decide which frames and vectors build the in-between frames. Whatever methods you tick get blended into the final result.

- Prev Forward: Grabs the preceding frame and leans on the Forward vector to interpolate the new one.
- Next Forward: Grabs the following frame in the sequence and leans on the Forward vector to interpolate the new one.
- Prev Backward: Grabs the preceding frame and leans on the Back Forward vector to interpolate the new one.
- Next Backward: Grabs the following frame in the sequence and leans on the Back vector to interpolate the new one.

Optical Flow Options These settings adjust the optical flow analysis. Refer to the Classic and Advanced Controls section covering the Optical Flow node earlier in this chapter.

### Common Controls

Settings Tab The Inspector’s Settings tab recurs across the other Optical Flow nodes as well. You’ll find these shared controls laid out fully at the end of this chapter, under “The Common Controls.”

### Smooth Motion [SM]

### The Smooth Motion node

### Smooth Motion Node Introduction

By drawing on optical flow to consult neighboring frames, the Smooth Motion node smooths assorted AOV (Arbitrary Output Variables) channels within a clip. One use is smoothing the Disparity channel of a stereo 3D clip, where it helps cut temporal edge/fringing artifacts, but it can equally smooth a broad set of channels such as vectors, normals, and Z. The image feeding the node’s input must already hold precomputed Vector and Back Vector channels; without them, this tool writes error messages into the Console window. Tick the channels you’d like temporally smoothed. Note that if a channel you’ve marked for smoothing isn’t there, Smooth Motion neither fails nor emits any error messages. You can also turn it on the Vector and Back Vector channels; at times, though, that worsens the interpolated results when the shot holds conflicting motions or objects that move erratically, jitter, or bounce rapidly.

TIP: Stringing two or more Smooth Motion nodes together gives you extra smoothing. A single Smooth Motion node looks at the previous, current, and next frames for a total of 3; two of them look at 5 frames; and three of them look at 7. A further approach with two Smooth Motion nodes is to let the first one smooth the Vector and Back Vector channels. Then have the second Smooth Motion smooth the channels you’re after (Disparity, for example). That way the smoothed vector channels are what smooth Disparity. You might also experiment with feeding the smoothed motion channels back to smooth the motion channels.

### Inputs

A single orange image input belongs to the Smooth Motion node. Input: A 2D image is what the orange image input takes. That image is the run of images you want smooth motion computed for. It must already carry precomputed Vector and Back Vector channels, whether produced by an Optical Flow node or saved into EXR format with vector channels.

### Basic Node Setup

For the Vector and Back Vector channels it needs, the Smooth Motion node draws on the Optical Flow node’s output. From there, the Smooth Motion node can smooth those channels or the AO channels.

A Smooth Motion node drawing on the Optical Flow node’s Vector and Back Vector channels.

### Inspector

### The Smooth Motion Controls tab

### Controls Tab

On the Controls tab sit checkboxes for whichever channels you want smoothed. Should a channel you’ve marked for smoothing be absent from the input image, Smooth Motion won’t fail and won’t write any error messages to the Console. Channel Smooth Motion reaches beyond just the RGBA channels; it applies to the other AOV channels as well.

### Common Controls

Settings Tab Here too, the Inspector’s Settings tab repeats across the other Optical Flow nodes. A detailed write-up of these shared controls sits at the end of this chapter, within “The Common Controls.”

### Tween [Tw]

### The Tween node

### Tween Node Introduction

Tween rebuilds a missing frame by interpolating across two neighboring frames using the optical flow. In what it does, Tween nearly matches Time Speed and Time Stretcher. The key distinction is that it operates on two images that aren’t consecutive members of a sequence. Because of that, it can’t tap the Vector or Back Vector aux channels held in the images. The Tween node works out the optical flow on its own, so there’s no need to put an Optical Flow node ahead of it. Whatever optical flow it produces is discarded rather than written back into the output frames. Since optical flow rests on color matching, it’s wise to color correct your images to agree beforehand. Likewise, if noisy images give you grief, stripping some of the noise out in advance can help. Tween destroys any incoming aux channels. Consult the Optical Flow node for its controls and settings details.

### Inputs

The Tween node sports two image inputs plus an effects mask input. Input 0: The orange input, marked input 0, holds the frame preceding the one you’re generating. Input 1: The green input, marked input 1, holds the frame following the one you’re generating. Effect Mask: A mask shape goes into the blue input — one made from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Hooking a mask up here confines the Tween to specific regions.

### Basic Node Setup

The Tween node takes two inputs, one for each of the two frames flanking the one you’re generating. In the example below, the earlier frame, frame 01, feeds the orange input 0, while the later frame, frame 03, feeds the green input 1. The Tween node then produces frame 02 and outputs the sequence.

The Tween node takes two neighboring frames and produces the one in between.
