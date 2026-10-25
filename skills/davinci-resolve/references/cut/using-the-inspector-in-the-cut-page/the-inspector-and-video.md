# The inspector and video

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the cut page.
[Chapter index](INDEX.md) / [Next section](dynamic-zoom-and-composite.md)
<a id="source-cropping"></a> <a id="source-the-cropping-section-of-the-video-inspector-panel"></a> <a id="source-the-transform-section-of-the-video-inspector-panel"></a> <a id="source-transform"></a> <a id="source-using-the-inspector"></a> <a id="source-using-the-inspector-in-the-cut-page"></a> <a id="source-using-the-inspector-in-the-cut-page-part-1"></a> <a id="source-video"></a>

### Using the Inspector in the Cut Page

Every control needed to alter, rescale, retime, or otherwise tweak whatever clip, transition, or effect sits on the Cut page Timeline is gathered inside the Inspector.

### Using the Inspector

To make pinpointing a given control simpler and to streamline tweaking the settings you touch most, the Inspector got a fresh layout. Rather than one tall, scrolling column, its sections are now split into panels, each devoted to a related cluster of parameters for the clip at hand. Click the Inspector Panel near the top-right of the User Interface toolbar to turn it on. Its contents divide across separate Video, Audio, Effects, Transition, Image, and File panels. Any panel that has no bearing on the current clip or selection appears dimmed.

The Inspector Panel icon in the upper right of the UI toolbar

The Inspector panels with the Video, Audio, and File parameters open for tweaking; the rest sit dimmed. Ways to work the controls inside the Inspector:

- To activate or deactivate a control: Hit the toggle sitting to the left of the control’s name. An orange dot over on the right signals the control is on. A gray dot over on the left signals it is off.
- To reveal a control’s parameters: Double-click the control’s name.
- To reset controls to their defaults: Press the reset button found to the right of the control’s name.

### Video

A broad set of controls for reshaping the size, speed, and opacity of your clips lives on the Video panel of the Inspector.

### Transform

### The Transform section of the Video Inspector panel

For rescaling and relocating a clip, the Transform group offers these parameters:

- Zoom X and Y: Lets you scale the image larger or smaller. You can link the X and Y parameters to hold the image’s aspect ratio fixed, or unlink them to stretch or compress the image along a single axis only.
- Position X and Y: Shifts the image inside the frame so pan and scan moves can be made. X slides the image left or right, while Y slides it up or down.
- Rotation Angle: Rotates the image around the anchor point.
- Anchor Point X and Y: Sets the spot on that clip that every transform pivots around.
- Pitch: Spins the image toward or away from the lens around a horizontal axis through its middle, running left to right. With positive numbers the upper edge tilts back while the lower edge swings toward you; negative numbers do the reverse, pulling the top forward and pushing the bottom back. The bigger the value, the more pronounced the stretching becomes.
- Yaw: Spins the image toward or away from the lens around a vertical axis through its middle,

running top to bottom. Positive numbers swing the left edge toward you while the

right edge tilts back. Negative numbers tilt the left edge away and pull the right

side forward. Larger values exaggerate the stretch further.

- Flip Image: Two buttons let you flip the image in different dimensions.

Flip Horizontal control: Mirrors the image across the X-axis, swapping left and right.

Flip Vertical control: Mirrors the clip across the Y-axis, flipping it upside down.

Smart Reframe (Studio Version Only)

Within the Video Inspector panel, the Smart Reframe area holds a feature that speeds up the job of reframing footage when the aspect ratio shifts dramatically. It comes in handy whenever, say, you captured a 16:9 horizontal shot but now must deliver a vertical 9:16 cut for phones and social platforms, or you’re dropping 4:3 archival clips into a 2.39:1 widescreen film. You can run Smart Reframe by hand or have the DaVinci Resolve Neural Engine do it for you automatically.

- Object of Interest: Controls for picking the subject the resize will build its framing around. Auto: DaVinci Resolve’s Neural Engine studies the clip and settles on the object it finds most representative. When you’ve selected more than a single clip for Smart Reframing, this becomes the sole choice.

Reference Point: Lets you hand-tune a bounding box drawn around the subject you want to reframe around.

- Mode: Controls for confining the AI reframing to one specific axis. Auto: As it sees fit, Smart Reframe shifts a clip’s pan and tilt to reframe the target correctly.

Pan Only: Here Smart Reframe touches only the clip’s pan (left and right) movement. Tilt Only: Here Smart Reframe touches only the clip’s tilt (up and down) movement.

- Reframe: Pressing this button runs the Smart Reframe command. How long it takes depends on how many clips there are and how long they run.

### Cropping

### The Cropping section of the Video Inspector panel

The image’s cropping parameters are governed by the Video Inspector.

- Crop Left, Right, Top, and Bottom: Trims away, measured in pixels, any of the image’s four edges. Once a clip is cropped, transparency opens up there, letting anything below it become visible.
- Softness: Lets you blur the edges of a crop. A negative setting softens the

borders on the inside of the crop box, while a positive setting softens the borders

beyond the crop box.

- Retain Image Position: Tick this checkbox and the crop parameters stay pinned in place as you resize the image with the Transform tool above. Leave it unticked and the crop is scaled and repositioned right along with the image.
