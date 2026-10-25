# Stereoscopic overview and optical flow overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Optical flow and stereoscopic nodes.
[Chapter index](INDEX.md) / [Next section](aux-deep-channels-and-optical-flow-workflows.md)
<a id="source-optical-flow-and-stereoscopic-nodes"></a> <a id="source-optical-flow-and-stereoscopic-nodes-part-1"></a> <a id="source-optical-flow-nodes"></a> <a id="source-optical-flow-overview"></a> <a id="source-overview"></a> <a id="source-stereoscopic-nodes"></a> <a id="source-stereoscopic-overview"></a> <a id="source-toolset-overview"></a>

### Optical Flow and Stereoscopic Nodes

This chapter walks through the wide range of stereoscopic and optical flow‑based nodes that Fusion offers, along with the workflows tied to them.

### Overview

Within Fusion you'll find 3D stereoscopic and optical flow-based nodes. They can operate jointly or on their own to build, fix, and refine 3D stereoscopic shots.

Stereoscopic comp displayed in the viewers.

### Stereoscopic Overview

Every stereoscopic capability is woven directly into Fusion’s 3D environment. A stereoscopic image may be built from one camera (which exposes eye separation and convergence distance) paired with a Renderer 3D that handles the virtual left and right eye. Alternatively, you can pair two separate cameras to act as a stereo camera rig. These stereoscopic nodes help resolve trouble that arises when shooting in 3D stereo — for instance 3D rig misalignment, mismatched mirror polarization between the images, timing sync problems across cameras, color alignment, convergence, and difficulties with eye separation. On top of that, the stereo nodes are handy for producing depth maps.

### Optical Flow Overview

Optical Flow studies how a clip moves and produces motion vectors spanning adjacent frames. The node yields X and Y vectors pointing from the prior frame to the present one (Back Vectors) plus toward the upcoming frame in the sequence (Forward Vectors). After the calculation finishes, that optical flow data feeds other nodes so you can build silky slow motion, retime clips at variable rates, fill in absent frames, and even fix disparity within stereo 3D clips. NOTE: The stereoscopic nodes on the Fusion page operate separately from the stereoscopic tooling found on the remaining DaVinci Resolve pages.

### Toolset Overview

What follows is a summary of the nodes you can reach.

### Optical Flow Nodes

- Optical Flow > OpticalFlow: Examines the movement across adjacent frames within a sequence and produces motion vectors that downstream nodes can apply for retiming, motion blur, and similar effects.
- Miscellaneous > TimeSpeed: Changes a clip's playback rate to a fixed value via Flow Interpolation mode.
- Miscellaneous > TimeStretcher: Alters a clip's rate across changing speeds via Flow Interpolation mode.
- Optical Flow > RepairFrame: Builds a fresh frame from the motion vectors that span two

neighboring frames.

- Optical Flow > SmoothMotion: Evens out the color or aux channels by leaning on motion vectors.
- Optical Flow > Tween: Blends two non-sequential images together to manufacture a new frame.
- Color > CopyAux: Moves aux channels — motion vectors included — into RGBA with greater efficiency than

Channel Booleans.

### Stereoscopic Nodes

- Stereo > Anaglyph: Merges stereo images into one anaglyph image you can view.
- Stereo > Combiner: sStacks individual stereo images into a single stacked pair

so they can be handled together.

- Stereo > Disparity: Computes disparity across left/right images.
- Stereo > DisparityToZ: Turns disparity into Z-depth.
- Stereo > Global Align: Manually nudges each stereo eye for rough alignment of stereo images.
- Stereo > NewEye: Swaps the left and/or right eye for interpolated eyes.
- Stereo > Splitter: Breaks a stacked stereo image apart into left and right images.
- Stereo > StereoAlign: Tunes vertical alignment, convergence, and eye separation.
- Stereo > ZToDisparity: Turns Z-depth into disparity.
