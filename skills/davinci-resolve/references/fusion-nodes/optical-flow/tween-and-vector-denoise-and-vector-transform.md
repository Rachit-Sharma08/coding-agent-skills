# Tween and vector denoise and vector transform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tween, Vector denoise, Vector transform.
[Chapter index](INDEX.md) / [Previous section](repair-frame-and-smooth-motion-and-tween.md) / [Next section](vector-transform-controls.md) / [Continue Vector Transform VXf / Controls Tab](vector-transform-controls.md) / [Tween Tw](repair-frame-and-smooth-motion-and-tween.md)
<a id="source-basic-node-setup-4"></a> <a id="source-basic-node-setup-5"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-the-tween-controls-tab"></a> <a id="source-the-vector-denoise-controls-tab"></a> <a id="source-the-vector-denoise-node"></a> <a id="source-the-vector-transform-node"></a> <a id="source-vector-denoise-node-introduction"></a> <a id="source-vector-denoise-vdn"></a> <a id="source-vector-transform-node-introduction"></a> <a id="source-vector-transform-vxf"></a> <a id="source-vector-warping-toolset-studio-version-only"></a>

### Inspector

### The Tween Controls tab

### Controls Tab

The Controls tab carries options for how frames get tweened. It also carries controls for adjusting the optical flow analysis, the same as those on the Optical Flow node. Interpolation Parameter This option pins down where your interpolated frame falls relative to source frames A and B. Setting the Interpolation Parameter to 0.0 produces frame A, a value of 1.0 produces frame B, and a value of 0.5 lands you midway between A and B.

Depth Ordering Depth Ordering settles which parts of the image render on top, through either Fastest On Top or Slowest On Top. The scenarios below explain these options best. Picture a locked-off camera shot with a car crossing the frame: the background holds still and so emits small, slow vectors, whereas the car emits larger, faster ones. Here Fastest On Top is the Depth Ordering, since the car paints over the background. Picture instead a shot where the camera pans to follow the car: now the background owns the faster vectors and the car the slower ones, so Slowest On Top becomes the Depth Ordering method. Clamp Edges In certain conditions this option clears the transparent gaps that may surface at the edges of interpolated frames. Clamp Edges brings on a stretching artifact close to the frame’s edges, most noticeable when objects pass through or the camera moves. Owing to those artifacts, it’s smart to apply Clamp Edges only for fixing small gaps around the borders of an interpolated frame. Edge Softness This slider appears only once Clamp Edges is on. It works to lessen the stretchy artifacts Clamp Edges may bring in. Enabling more than one of the Source Frame and Warp Direction checkboxes can double the stretching effect near the edges. When that occurs, hold the softness rather low, around 0.01. With just a single checkbox enabled, a larger softness near 0.03 is fine. Source Frame and Warp Direction Through these checkboxes you select which frames and vectors form the in-between frames. Each method you tick is blended into the result.

- Prev Forward: Pulls the preceding frame, then interpolates the new frame from the Forward vector.
- Next Forward: Pulls the following frame in the sequence, then interpolates the new frame from the Forward vector.
- Prev Backward: Pulls the preceding frame, then interpolates the new frame from the Back Forward vector.
- Next Backward: Pulls the following frame in the sequence, then interpolates the new frame from the Back vector.

Optical Flow Options These settings adjust the optical flow analysis. Refer to the Class and Advanced Controls section covering the Optical Flow node earlier in this chapter.

### Common Controls

Settings Tab As before, the Inspector’s Settings tab is replicated across the other Optical Flow nodes. The shared controls get a thorough treatment in the “The Common Controls” section that follows.

### Vector Warping Toolset (Studio Version Only)

The Vector Warping 2D imaging toolset below lets you map and warp a reference frame onto every other frame in the sequence. It proves handy for face replacements, digital makeup, sign replacements, and the like, letting you track and warp assets right alongside the background. In its most basic form, you:

- Apply VFX changes—make-up, face paint, scars, black eyes—on a single frame,
- Make sure the reference frame’s regions stay visible throughout the frames you’re tracking,
- Add Vector Warp, set the reference frame, choose Generate + Texture Map, and track the changes onto

the sequence using optical flow.

### Vector Denoise [VDn]

### The Vector Denoise node

### Vector Denoise Node Introduction

This tool performs a general-purpose averaging across neighboring frames. Though it resembles temporal noise reduction, the source pixels being averaged are motion vector compensated.

### Inputs

One orange image input belongs to the Vector Denoise node. Input: A 2D image is what the orange image input takes. That image has to come with precomputed Vector and Back Vector channels, whether made by an Optical Flow node or stored in EXR format with vector channels.

### Basic Node Setup

For the Vector and Back Vector channels it requires, the Vector Denoise node draws on the Optical Flow node’s output, then strips noise across several frames.

A Vector Denoise node drawing on the Optical Flow node’s Vector and Back Vector channels

### Inspector

### The Vector Denoise Controls tab

### Controls Tab

The Controls tab is where you adjust the Vector Denoise settings. Average: Specify the temporal window as a number of frames. Threshold: Set an upper limit so flashes and brief highlights are skipped while pixel values are averaged.

### Common Controls

Settings Tab Likewise, the Inspector’s Settings tab carries over to the other Optical Flow nodes. These shared controls are spelled out fully at this chapter’s end, in the “The Common Controls” section.

### Vector Transform [VXf]

### The Vector Transform node

### Vector Transform Node Introduction

This tool permits custom transforms on the vector channel information, so tracking data can be resized, rotated, and translated before being applied to another image or sequence. Reach for it to mimic the transfer of kinetic energy, object responses, and differences in material properties within a dynamic scene.

### Inputs

The Vector Transform node comes with an orange image input plus an attenuate mask input. Input: A 2D image is what the orange image input takes. Attenuate Mask: A mask shape is what the white input takes.

### Basic Node Setup

For the Vector and Back Vector channels it needs, the Vector Transform node draws on the Optical Flow node’s output, then transforms the vector channel information. A Vector Transform node drawing on the Optical Flow node’s Vector and Back Vector channels Inspector
