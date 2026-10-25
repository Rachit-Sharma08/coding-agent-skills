# Aux deep channels and optical flow workflows

Version: DaVinci Resolve 20.3 Reference Manual. Context: Optical flow and stereoscopic nodes.
[Chapter index](INDEX.md) / [Previous section](stereoscopic-overview-and-optical-flow-overview.md) / [Next section](stereo-materials-and-disparity.md)
<a id="source-advanced-optical-flow-processing"></a> <a id="source-optical-flow-workflows"></a> <a id="source-opticalflow"></a> <a id="source-repair-frame-tween"></a> <a id="source-smoothmotion"></a> <a id="source-stereo-camera"></a> <a id="source-stereoscopic-workflows"></a> <a id="source-timespeed-timestretcher"></a> <a id="source-working-with-aux-deep-channels"></a>

### Working with Aux Deep Channels

Some image formats are able to hold channels beyond RGBA color; these go by the name aux deep channels. Stereo Disparity and OpticalFlow operate right on auxiliary deep channels. The aux channels that Fusion handles are:

- RGBA: The ordinary colors.
- Z: The eyespace Z coordinate tends to be negative, since in eyespace Fusion’s camera rests at (0, 0, 0) and faces down the Z-axis. The value begins at Z = 0 at the camera focal point and grows steadily more negative as objects recede deeper into the scene.
- Coverage: How much of the pixel the frontmost pixel occupies, expressed as a percentage and used for antialiased Z-compositing.
- Object ID: Integers a user assigns to meshes.
- Material ID: Integers a user assigns to materials.
- Texture Coords: Texture coordinates kept in normalized form as (u, v) pairs.
- Normal Vector: Normal vector (nx, ny, nz), whose components usually fall in the range [–1, +1].
- Background Color: What color the pixel would be once the frontmost layer is taken away, used for antialiased Z-compositing.
- Vector: A forward motion vector — an offset (vx, vy) that relates each pixel’s spot in one frame to where that same pixel lands in the following frame.
- Back Vector: A backward motion vector — an offset (vx, vy) relating each pixel’s spot in one frame to where that same pixel sat in the preceding frame.
- World Position: Where the pixel lives in world coordinates, given as (wx, wy, wz).
- Disparity: An offset (dx, dy) linking a pixel across the Left > Right or Right > Left frames.

A handful of these extra channels feed particular Fusion nodes. For instance:

- Merge can lean on the Z channel for a depth merge. When the Coverage and BackgroundColor channels exist, it handles antialiased edges more cleanly during the Z merge.
- The bulk of image-processing nodes (BrightnessContrast among them) expose options on their common controls tab that confine processing according to MaterialID and ObjectID.
- The Z channel is consumed by the Fog and DepthBlur nodes.
- The TexCoord channel is consumed by the Texture node.
- The Normal channel is consumed by the Shader node.

Inside Fusion there are a few routes for fetching or producing those extra channels. For instance:

- The Renderer3D node can produce the majority of these channels.
- The OpticalFlow node creates the Vector and BackVector channels, which TimeStretcher

and TimeSpeed are then able to consume.

- The Disparity node creates the Disparity channels, after which DisparityToZ, NewEye, and

StereoAlign nodes can consume the Disparity channels.

- The OpenEXR format lets you bring aux channels into Fusion or send them out by laying out a

mapping from EXR attributes onto Fusion Aux channels through CopyAux.

### Optical Flow Workflows

Running the Optical Flow analysis is not a real-time task; how long it takes hinges on your machine, the clip’s resolution, and how long the clip runs. For that reason the usual approach is to pre-generate the motion vectors ahead of time — running the analysis overnight or on a render farm — and store the output as an OpenEXR sequence. The Optical Flow toolset is built around four categories of nodes that respectively generate, destroy, pass through, or construct the motion vectors.

### OpticalFlow

The Optical Flow node produces the Vector and BackVector data. For best results you'd normally route the Optical Flow output into a Saver, writing the image out as OpenEXR files that hold the motion vectors inside an aux channel.

### TimeSpeed, TimeStretcher

Smooth slow-motion at either a steady or shifting rate is achievable through the TimeSpeed or TimeStretcher nodes. Whenever Optical Flow motion vectors already sit in an image’s aux channel, switching on Flow mode within the TimeSpeed or TimeStretcher Interpolation settings will exploit the Vector and BackVector channels. Flow mode needs either an upstream OpticalFlow node producing the hidden channels or an OpenEXR Loader feeding those channels in. The nodes draw on the Vector/BackVector data to interpolate the motion channel and afterward discard that data on output, because the incoming Vector/BackVector channels no longer hold. For deeper coverage of TimeSpeed or TimeStretcher, consult Chapter 111, “Miscellaneous Nodes,” within the DaVinci Resolve Reference Manual, together with Chapter 51 of the Fusion Reference Manual.

### SmoothMotion

You can apply SmoothMotion to even out the Vector and BackVector channels or to smooth disparity within a stereo 3D clip. The node passes through, alters, or creates fresh aux channels yet leaves them in place rather than destroying them.

### Repair Frame, Tween

What sets the Tween and Repair Frame nodes apart from ordinary optical flow nodes is that the OpticalFlow analysis and motion vector generation are baked right into them. Tween examines two frames and produces an in-between frame, handy for rebuilding a frame that's missing or damaged. Repair Frame inspects the frames flanking the current one and mends scratches, dust marks, and the like. Since these nodes rely on flow values across non-sequential frames, they can't reuse the optical flow held in the input image’s Vector/BackVector channels; instead they have to recompute each frame's flow, carry out their work, then discard the flow channels. As a result, these nodes are heavy on computation. For deeper coverage of Tween or Repair Frame, consult Chapter 112, “Optical Flow,” within the DaVinci Resolve Reference Manual, or else Chapter 52 of the Fusion Reference Manual.

### Advanced Optical Flow Processing

A quicker GPU-based Optical Flow algorithm ships inside the Optical Flow, Repair Frame, and Tween nodes. After you drop the Optical Flow, Repair Frame, or Tween node into a comp, the Inspector presents a Method drop-down menu from which selecting Advanced turns on the GPU-based algorithm. That Advanced method matches the very Optical Flow algorithm running on the other DaVinci Resolve pages. Picking Classic from the same Method drop-down menu in the Inspector reverts to the older CPUbased algorithm, preserving compatibility with comps built in earlier versions; that choice can also work better for certain Stereo3D processing.

### Stereoscopic Workflows

Disparity captures how the left and right image differ. Nodes draw on the Disparity map to register and fine-tune the stereo pair of images. The Disparity node studies a stereo pair of images and creates an X&Y disparity map. In practice you bring in a left and right stereo image pair and run them through the Disparity node. Once that Disparity map exists, other nodes can act on the images. TIP: While wiring stereo pairs through the node tree, confirm that the left and right images feed the left and right inputs of the Disparity node. Producing disparity, much like Optical Flow, is heavy on computation, so the standard tactic is to pre-generate these channels beforehand — overnight or on a render farm — and write them out as an EXR sequence. That philosophy shapes the whole toolset.

### Stereo Camera

A stereoscopic camera can be configured in one of two ways. The usual route is to drop in a Camera 3D and dial in the eye separation and convergence distance parameters. The alternative is to wire a second camera into the RightStereoCamera input port of the Camera 3D. As you look through the original camera or render, that connected camera supplies the right-eye content.

A stereoscopic camera setup may rely on just one camera or on a pair of linked cameras.
