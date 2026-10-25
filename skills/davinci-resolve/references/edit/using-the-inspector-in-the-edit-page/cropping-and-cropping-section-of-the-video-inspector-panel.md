# Cropping and cropping section of the video inspector panel

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the edit page.
[Chapter index](INDEX.md) / [Previous section](the-inspector-and-video.md) / [Next section](video-inspector-stabilization.md)
<a id="source-composite"></a> <a id="source-cropping"></a> <a id="source-dynamic-zoom"></a> <a id="source-speed-change"></a> <a id="source-the-composite-section-of-the-video-inspector-panel"></a> <a id="source-the-cropping-section-of-the-video-inspector-panel"></a> <a id="source-the-speed-change-controls-in-the-video-inspector"></a>

### Cropping

### The Cropping section of the Video Inspector panel

The image’s cropping parameters are governed by the Video Inspector.

- Crop Left, Right, Top, and Bottom: Lets you trim away the four edges of the image in pixels. Cropping

a clip opens up transparency so whatever lies beneath becomes visible.

- Softness: Lets you blur a crop’s edges. A negative value softens the edges

inside the crop box, whereas a positive value softens those outside it.

- Retain Image Position: Ticking this checkbox pins the crop parameters in place while you resize the image with the Transform tool above. Clearing it makes the crop scale and reposition right along with the image.

### Dynamic Zoom

The Dynamic Zoom section of the Video Inspector panel Switched off by default, the Dynamic Zoom controls make pan and scan effects that zoom into or out of a clip quick and painless. Enabling the Dynamic Zoom group lights up two Inspector controls that operate in tandem with the Dynamic Zoom onscreen adjustment controls. For more on working the Dynamic Zoom controls, refer to Chapter 50, “Compositing and Transforms in the Timeline.”

- Dynamic Zoom Ease: Lets you set how the motion these controls create speeds up. The choices are Linear, Ease In, Ease Out, and Ease In and Out.
- Swap: Pressing this button flips the start and end transforms behind the dynamic zoom effect.

### Composite

### The Composite section of the Video Inspector panel

When clips sit layered over other clips in the Timeline, composite modes let you blend them together.

- Composite Mode: This picks which composite mode merges the layered clips. With the default “Normal,” no compositing mode is in effect.

For more on Composite Modes, refer to Chapter 50, “Compositing and Transforms in the Timeline.”

- Opacity: On top of any compositing already happening, this slider raises or lowers a clip’s transparency.

### Speed Change

### The Speed Change controls in the Video Inspector

Your clip’s speed can be altered right inside the Video Inspector’s Speed Change controls. One advantage of this route is that it’s present on both the Cut and Edit pages.

- Direction: Chooses how the clip moves — forward, backward, or freeze frame.
- Speed %: Moving this slider alters the clip’s motion as a percentage. The value

accepts keyframes.

- Frames Per Second: Moving this slider alters the clip’s motion by raising or lowering the

number of frames per second at which the clip plays back. The value accepts keyframes.

- Duration: You can pick a clip’s length outright by entering a specific duration

here in HH:MM:SS:FF format. The clip’s speed then adjusts on its own so every frame plays within that precise span of time.

- Ripple Sequence checkbox: Switch this checkbox on if you want the speed change you’re about to apply to ripple the Timeline, nudging every clip after the current one forward or back to make room for its new size.
- Pitch Correction checkbox: Ticking this box runs pitch correction on the clip’s attached audio so that, even as the audio duration shifts to track the picture speed, it still sounds natural. Bear in mind that pitch correction across large speed changes may not sound as clean as it does across small ones.
