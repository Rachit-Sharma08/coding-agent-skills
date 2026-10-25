# The inspector and adjusting media pool clips in the inspector

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the media page.
[Chapter index](INDEX.md) / [Next section](lens-correction-and-retime-and-scaling.md)
<a id="source-adjusting-media-pool-clips-in-the-inspector"></a> <a id="source-composite"></a> <a id="source-cropping"></a> <a id="source-dynamic-zoom"></a> <a id="source-the-composite-section-of-the-video-inspector-panel"></a> <a id="source-the-cropping-section-of-the-video-inspector-panel"></a> <a id="source-the-transform-section-of-the-video-inspector-panel"></a> <a id="source-transform"></a> <a id="source-using-the-inspector"></a> <a id="source-using-the-inspector-in-the-media-page"></a> <a id="source-using-the-inspector-in-the-media-page-part-1"></a> <a id="source-video"></a>

### Using the Inspector in the Media Page

The Inspector gathers every control needed to modify, resize, retime, and otherwise tweak anything to do with a clip, transition, or effect on the Media page Timeline.

### Using the Inspector

A redesign of the Inspector has made it simpler to locate particular controls and to set common settings for your clips. Rather than one long vertical list, the Inspector’s various facets are now sorted into panels, each governing a specific grouped set of parameters for your clip. To turn the Inspector on, click the Inspector Panel over in the User Interface toolbar’s upper-right section. The Inspector divides into distinct Video, Audio, Effects, Transition, Image, and File panels. Any Inspector panel that has no bearing on your clip or selection shows up grayed out. The Inspector Panel icon up at the right of the UI toolbar

The Inspector panels with Video, Audio, and File parameters open for adjustment; the rest sit grayed out. Ways to work the controls in the Inspector:

- To activate or deactivate a control: Click the toggle sitting left of that control’s name. An orange dot off to the right signals the control is activated. A gray dot off to the left signals the control is deactivated.
- To reveal a control’s parameters: Double-click the control’s name.
- To reset controls to their defaults: Click the reset button sitting right of that control’s name.

### Adjusting Media Pool Clips in the Inspector

Media Pool clips can be modified straight in the Inspector, ahead of editing those clips into a timeline. That lets you alter the parameters of source media so that clips later edited into a timeline carry those new settings along. As an example, you can ready your material before editing by altering the clip’s file and RAW settings, tuning the audio levels and EQ, or handing it a particular lens correction, and so on. Once that’s done, every part of that clip would arrive in your timeline with the right Inspector parameters already set. To adjust Media Pool clips in the Inspector: 1 Within the Media Pool Panel of the Media, Cut, Edit, or Fairlight pages, pick one or more clips. 2 Bring up the Inspector panel, then tweak any parameters across the Video, Audio, Image and File tabs. Those parameter changes get saved with the Media Pool clip and carry over whenever any part of that clip is edited into the Timeline. Naturally, each clip’s Inspector parameters can be tweaked further once it sits in the Timeline, and those Timeline parameters stand apart from the Media Pool Inspector settings. Put another way, whatever further adjustments you apply to the clip in the Timeline leave that same clip’s adjustments already in the Media Pool untouched.

### Video

The Video Panel of the Inspector surfaces a huge range of controls built to handle the size, speed, and opacity of your clips.

### Transform

### The Transform section of the Video Inspector panel

The Transform group carries these parameters for resizing and repositioning your clips:

- Zoom X and Y: Lets you enlarge the image or shrink it. The X and Y parameters may be linked to hold the image’s aspect ratio, or unlinked to stretch or squeeze the image along one direction alone.
- Position X and Y: Shifts the image within the frame, making pan and scan adjustments possible. X drives the image left or right, while Y drives it up or down.
- Rotation Angle: Spins the image about the anchor point.
- Anchor Point X and Y: Sets the coordinate on that clip around which every transform is centered.
- Pitch: Tips the image toward or away from the camera along an axis that runs through the

middle of the image, from left to right. Positive values send the top of the image back and draw the bottom forward. Negative values draw the top of the image forward and send the bottom back. The larger the value, the more extreme the stretch.

- Yaw: Tips the image toward or away from the camera along an axis that runs through the middle of the image from top to bottom. Positive values draw the left of the image forward and send the right back. Negative values send the left of the image back and draw the right forward. The larger the value, the more extreme the stretch.
- Flip Image: A pair of buttons let you flip the image in different dimensions. Flip Horizontal control: Mirrors the image along the X-axis, left to right. Flip Vertical control: Mirrors the clip along the Y-axis, flipping it upside down.

### Cropping

### The Cropping section of the Video Inspector panel

The Video Inspector governs the image’s cropping parameters:

- Crop Left, Right, Top, and Bottom: Lets you trim, in pixels, the four sides of the image. Cropping a clip yields transparency so that whatever lies beneath shows through.
- Softness: Lets you blur a crop’s edges. A negative value softens the edges inside the crop box, whereas a positive value softens the edges outside the crop box.
- Retain Image Position: Ticking this checkbox pins the crop parameters in place as you resize the image with the Transform tool above. Unticking it scales and positions the crop right along with the image.

### Dynamic Zoom

The Dynamic Zoom section sitting within the Video Inspector panel The Dynamic Zoom controls, off to begin with, make pan and scan effects that zoom into or out of a clip quick and painless. Switching the Dynamic Zoom group on brings two controls alive in the Inspector that operate hand-in-hand with the Dynamic Zoom onscreen adjustment controls. For more on working the Dynamic Zoom controls, refer to Chapter 50, “Compositing and Transforms in the Timeline.”

- Dynamic Zoom Ease: Lets you set how the motion these controls produce accelerates. Your choices are Linear, Ease In, Ease Out, and Ease In and Out.
- Swap: This button flips the start and end transforms that build the dynamic zoom effect.

### Composite

### The Composite section of the Video Inspector panel

Composite modes serve to blend clips superimposed over other clips in the Timeline.

- Composite Mode: This picks the kind of composite mode used to blend the superimposed clips. The default “Normal” signals that no compositing mode is applied.

For more on Composite Modes, refer to Chapter 50, “Compositing and Transforms in the Timeline.”

- Opacity: This slider renders a clip more or less transparent on top of whatever compositing is already underway.
