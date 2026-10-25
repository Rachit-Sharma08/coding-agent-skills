# The inspector and video

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the edit page.
[Chapter index](INDEX.md) / [Next section](cropping-and-cropping-section-of-the-video-inspector-panel.md)
<a id="source-the-transform-section-of-the-video-inspector-panel"></a> <a id="source-transform"></a> <a id="source-using-the-inspector"></a> <a id="source-using-the-inspector-in-the-edit-page"></a> <a id="source-using-the-inspector-in-the-edit-page-part-1"></a> <a id="source-video"></a>

### Using the Inspector in the Edit Page

Every control for changing, resizing, retiming, and otherwise adjusting whatever pertains to a clip, transition, or effect on the Edit page Timeline lives in the Inspector.

### Using the Inspector

A redesign of the Inspector now makes locating particular controls and tweaking everyday clip settings simpler. Rather than one long vertical list, the Inspector’s various aspects are sorted into panels, each one in charge of a specific grouped set of parameters for your clip. You bring up the Inspector by clicking the Inspector Panel at the upper-right end of the User Interface toolbar. The Inspector splits into separate Video, Audio, Effects, Transition, Image, and File panels. Whichever Inspector panels don’t apply to your clip or selection appear grayed out.

The Inspector Panel icon located at the top right of the UI toolbar The Inspector panels with Video, Audio, and File parameters open for adjustment, the rest grayed out. Ways to work the controls in the Inspector:

- To turn a control on or off: Click the toggle sitting to the left of the control’s name. An orange dot on the right signals the control is on. A gray dot on the left signals it’s off.
- To expose a control’s parameters: Double-click the control’s name.
- To restore controls to default values: Click the reset button found at the right of the control’s name.

### Video

A huge selection of controls for working the size, speed, and opacity of your clips sits in the Inspector’s Video panel.

### Transform

### The Transform section of the Video Inspector panel

For resizing and repositioning your clips, the Transform group carries these parameters:

- Zoom X and Y: Lets you enlarge the image or scale it down. You can link the X and Y parameters to hold the image’s aspect ratio, or unlink them to stretch or compress the image along a single axis.
- Position X and Y: Shifts the image around inside the frame so pan and scan adjustments become possible. X slides the image left or right, while Y slides it up or down.
- Rotation Angle: Spins the image about the anchor point.
- Anchor Point X and Y: Sets the coordinate on the clip around which every transform is centered.
- Pitch: Tilts the image toward or away from the camera about an axis that runs through the

middle of the image, left to right. Positive values send the image’s top away while bringing its bottom forward. Negative values bring the top forward while sending the bottom away. The larger the value, the more extreme the stretch.

- Yaw: Tilts the image toward or away from the camera about an axis through the image’s center running top to bottom. Positive values bring the image’s left forward and send its right away. Negative values send the left away and bring the right forward. The larger the value, the more extreme the stretch.
- Flip Image: A pair of buttons flips the image along different axes. Flip Horizontal control: Mirrors the image across the X-axis, left to right. Flip Vertical control: Mirrors the clip across the Y-axis, flipping it upside down.

Smart Reframe (Studio Version Only)

The Video Inspector panel’s Smart Reframe section Smart Reframe, as a feature, streamlines rapid reframing of material across drastic aspect ratio shifts. It comes in handy when you’ve shot a 16:9 horizontal video yet need a vertical 9:16 version for mobile phones and social media deliverables, or when fitting 4:3 archival footage into a 2.39:1 widescreen movie. You can drive Smart Reframe by hand or let the DaVinci Resolve Neural Engine run it automatically.

- Object of Interest: Tools for choosing the subject the resize will build its framing around.
- Auto: DaVinci Resolve’s Neural Engine examines the clip and settles on its most representative

object. It’s your only choice when more than one clip is selected for Smart Reframing.

- Reference Point: Lets you adjust by hand a bounding box drawn around the subject you want to

reframe around.

- Mode: Tools for confining the AI reframing to a single axis.
- Auto: Smart Reframe adjusts a clip’s pan and tilt however much it judges necessary to reframe

the target properly.

- Pan Only: Smart Reframe limits itself to the clip’s pan (left and right) motion.
- Tilt Only: Smart Reframe limits itself to the clip’s tilt (up and down) motion.
- Reframe: Pressing this button runs the Smart Reframe command. How long it takes hinges

on the length and quantity of clips.
