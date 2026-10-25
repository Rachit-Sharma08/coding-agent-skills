# Tracker and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tracker, Common controls.
[Chapter index](INDEX.md) / [Previous section](tracker-layering-merge-and-position-controls.md) / [Tracker Tra](tracker-a-tracker-node-branched-from-the-node-tree.md)
<a id="source-common-controls"></a> <a id="source-display-options-tab"></a> <a id="source-inspector"></a> <a id="source-match-move-settings"></a> <a id="source-motion-blur"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-common-tracking-controls-settings-tab"></a> <a id="source-the-tracker-display-options-tab"></a> <a id="source-tracking-nodes-part-6"></a>

- Bi_Linear: The first approach is Bi-Linear, where the foreground image maps into the background with no effort made to correct for perspective distortion. This matches how earlier versions of Fusion behaved.
- Perspective: The foreground image maps into the background while accounting for perspective distortion. This is the preferred setting, since it maps to the real world better than the older Bi‑Linear setting does.

Corner Selector (Corner or Perspective Positioning) The moment the Tracker's operation lands on either Corner or Perspective Positioning modes, four drop-down menus surface. These options pick which trackers map onto each of the rectangle's four corners. This proves handy when a Tracker has more than four patterns selected and you must decide which patterns the positioners draw on. Rotate Clockwise and Counter-Clockwise Buttons (Corner or Perspective Positioning) Only when the Tracker's operation has been pointed at either Corner or Perspective Positioning modes do these controls surface. Their job is to spin the foreground image by 90 degrees before it's laid onto the background.

Stabilize Settings The Tracker node automatically puts out several steady and unsteady position outputs that other controls in the Node Editor can be wired to. The Stable Position output supplies X and Y coordinates for matching or reversing motion across a sequence. These controls stay available even where the operation isn't set to Match Move, since the Stable Position output is forever on hand for connection to other nodes.

### Match Move Settings

What these settings settle is how the tracking data gets correlated with the reference pattern when making transforms. Pivot Type What the Pivot type menu settles is how the anchor point for rotation gets chosen.

- Tracker Average: Averages the location out of the tracking points.
- Selected Tracker: Offers a menu where one of the current trackers can be picked

as the pivot point.

- Manual: Shows X and Y position number fields in which you can place the pivot points by hand.

Reference What the Reference mode settles is the "snapshot frame," based on the frame where the pattern first gets selected. Every bit of Stabilization aims to return the image back to that reference.

- Select Time: Lets you pick the current frame.
- Start: The Snapshot Frame is taken to be the first frame in the tracked path. Every bit of Stabilization

aims to return the image back to that reference.

- Start and End: The Start and End Reference mode departs somewhat from all the other Reference

modes. Where the others mean to grab a snapshot frame that all stabilization returns to, freezing the image in place, the Start and End mode means to smooth out existing motion without stripping it away. This mode averages the motion running between the Start and End of the path, tracing a straight line across those points. With this mode active, it exposes the Reference Intermediate Points control. Raising this control's value raises the count of points along the path that the Reference draws on, smoothing the motion away from a straight line between Start and End without rendering it wholly linear.

- End: The Snapshot Frame is taken to be the last frame in the tracked path. Every bit of Stabilization aims to return the image back to that reference.

TIP: Out of the box, within the Spline Editor the Tracker shows just one displacement path for the tracked data. Should you want the tracked points' X and Y paths shown in that same editor, head to Preferences > Globals > Splines.

### Display Options Tab

What the Display Options tab lets you do is shape the look of the onscreen controls in the viewer.

### The Tracker Display Options tab

Show Pattern Names What this option defines is whether the Tracker's pattern names show up in the viewer. Switch it off to view the pattern rectangle instead. Enlarged Pattern on Dragging What this option defines is whether a magnified thumbnail view appears while you position the pattern rectangle. Enlargement Scale The zoom factor put to use when positioning the pattern rectangle once the above option is switched on. TIP: Scripts may likewise tap a tracker's outputs (the ones shown within the Connect to… menu). The full roster runs as follows. First the overall position and axis outputs: SteadyPosition: Steady Position UnsteadyPosition: Unsteady Position SteadyAxis: Steady Axis. Then the size and angle outputs: SteadySize: Steady Size UnsteadySize: Unsteady Size SteadyAngle: Steady Angle UnsteadyAngle: Unsteady Angle. Next, the outputs tied to an individual tracker: Position1: Tracker 1 Offset position PerspectivePosition1: Tracker 1 Perspective Offset position. After those come the axis-resolved entries — PositionX1: Tracker 1 Offset X position (3D Space) PositionY1: Tracker 1 Offset Y position (3D Space) PerspectivePositionX1: Tracker 1 Perspective Offset X position (3D Space) PerspectivePositionY1: Tracker 1 Perspective Offset Y position (3D Space). Rounding out the set are the steadiness entries: SteadyPosition1: Tracker 1 Steady Position UnsteadyPosition1: Tracker 1 Unsteady Position (the same pattern carries on for the 2nd, 3rd, and onward)

### Common Controls

Settings Tab The Settings tab in the Inspector also has a duplicate in other Tracking nodes. These common controls get a full description toward the end of this chapter under "The Common Controls" section.

### The Common Controls

Several identical controls in the Inspector are shared by nodes that carry out tracking operations. The controls common across Tracking nodes are described in this section.

### Inspector

### The Common Tracking Controls Settings tab

### Settings Tab

Every tool in the Tracking category carries the Settings tab in the Inspector. The controls stay consistent and behave the same way from one tool to the next.

Blend The Blend control mixes between two things: the image the tool took in to begin with and the finished, altered image the tool puts out. With the blend value at 0.0, the outgoing image matches the incoming image. Ordinarily this leads the tool to bypass processing altogether, copying the input straight through to the output. Process When Blend Is 0.0 The tool runs its processing even when the input value sits at zero. This can come in handy if the node is scripted to fire off a task while the node's value rests at 0.0. Red/Green/Blue/Alpha Channel Selector These four buttons serve to confine the tool's effect to particular color channels. This filter typically gets applied after the tool has finished processing. To give an example, if the Red button on a Blur tool is switched off, the blur gets applied to the image first, and then the red channel from the original input is copied back over the result's red channel. There are a few exceptions, such as tools where switching these channels off makes the tool skip processing that channel outright. Tools that behave this way will generally carry a set of identical RGBA buttons on the Controls tab within the tool. Here the buttons on the Settings and the Controls tabs are one and the same. Apply Mask Inverted Switching the Apply Mask Inverted option on inverts the tool's complete mask channel. The mask channel is the pooled result of every mask wired into or generated within a node. Multiply by Mask Picking this option makes the masked image's RGB values get multiplied by the mask channel's values. As a result, any image pixel the mask excludes (in other words, set to 0) goes black/transparent. Use Object/Use Material (Checkboxes) Certain 3D software is able to render into file formats supporting extra channels. The EXR file format notably supports Object ID and Material ID channels, which can serve as a mask for the effect. These checkboxes settle whether those channels get used, where present. Which specific Material ID or Object ID is affected gets chosen through the next set of controls. Correct Edges This checkbox surfaces only once the Use Object or Use Material checkboxes are ticked. It flips the method used to deal with the overlapping edges of objects within a multi-object image. With it switched on, the Coverage and Background Color channels serve to separate and sharpen the effect around the object's edge. With this option switched off (or where neither Coverage nor Background Color channels are present), the mask's edge may show aliasing. To read further about the Coverage and Background Color channels, turn to Chapter 78, "Understanding Image Channels," within the DaVinci Resolve Reference Manual, or to Chapter 18 of the Fusion Reference Manual.

Object ID/Material ID (Sliders) Turn to these sliders to pick which ID will build a mask out of the object or material channels of an image. Put the Sample button to work the same way you would the Color Picker: to lift IDs off the image shown in the viewer. The image or sequence must have come out of a 3D software package with those channels rendered in.

### Motion Blur

- Motion Blur: Flips the rendering of Motion Blur on the tool on or off. With the control switched on, the tool draws on its predicted motion to generate the blur that the virtual camera's shutter would have caused. Leave it switched off and nothing is blurred.
- Quality: How many samples Fusion uses to build the blur depends on Quality. Pick a quality of 2 and Fusion lays down two samples on each side of an object's real motion. Bumping the value up smooths the look but lengthens how long the render takes.
- Shutter Angle: This sets the angle the virtual shutter opens to in order to generate the motion blur. Wider angles yield heavier blur at the cost of longer renders. Set it to 360 and that matches keeping the shutter open across one entire frame of exposure. You can go above that for unusual looks.
- Center Bias: Center Bias shifts where the midpoint of the motion blur sits. With it you can build motion trail looks.
- Sample Spread: Tweaking this changes how much weight each sample carries, which alters how bright the samples appear.

Use GPU Three choices live in the Use GPU menu. Choosing Disable switches off GPU hardware-accelerated rendering. Enabled hands the node's rendering to the GPU hardware. Auto reaches for a capable GPU when one exists and quietly drops back to software rendering whenever none is present. Hide Incoming Connections Tick this checkbox and the connection lines coming from upstream nodes can be concealed, which leaves a node tree tidier and more legible. With it ticked, the Inspector shows an empty field for every input on the node. Drag a connected node out of the node tree onto that field and its incoming line disappears for as long as the node stays unselected in the node tree. Select that node in the node tree again and the line comes back. Comments Notes get attached to a tool through the Comments field. Click into the blank field and type your text. Once a note exists, a tiny red square shows in the node's lower-left corner while the full tile is on display, or a little text-bubble icon shows on the right once nodes are collapsed. Hover the pointer over the node in the Node Editor and its tooltip reveals the note. Scripts Each tool in Fusion carries three Scripting fields on the Settings tab. Every one holds an edit box where you can drop scripts that run while the tool renders. To dig deeper into scripting nodes, turn to the Fusion scripting documentation.
