# Disparity to z outputs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Disparity to z.
[Chapter index](INDEX.md) / [Previous section](combiner-and-disparity-and-disparity-to-z.md) / [Disparity To Z D2Z](combiner-and-disparity-and-disparity-to-z.md) / [Next section](disparity-to-z-and-global-align-and-new-eye.md)
<a id="source-basic-node-setup-3"></a> <a id="source-camera-tab"></a> <a id="source-controls-tab-2"></a> <a id="source-disparity-to-z-node-introduction"></a> <a id="source-inputs-3"></a> <a id="source-inspector-3"></a> <a id="source-outputs-1"></a> <a id="source-stereo-nodes-part-2"></a> <a id="source-the-disparity-to-z-camera-tab"></a> <a id="source-the-disparity-to-z-controls-tab"></a>

### Disparity to Z Node Introduction

Disparity To Z accepts a 3D camera plus an image that carries a disparity channel as its inputs, and it returns that same image now bearing a freshly computed Z channel. As an option, the node can also write Z out into the RGB channels. Ideally you connect either a stereo Camera 3D or a tracked stereo camera into Disparity To Z. Yet when no camera is attached, the node hands you artistic controls for deciding a Z channel. The depth this node builds is handy for post effects such as fogging or depth of field (DoF). The Z values it returns grow less accurate the larger (in the negative direction) they become. That happens because disparity tends toward a fixed value as Z heads toward -infinity. Hence Z = -1000 and Z = -10000 and Z = -100000 might all map to D=142. 4563 and D=142. 4712 and D=142. 4713. Notice that a mere 0.0001 of D separates 10,000 from 100,000 in Z. The maps that disparity yields simply aren't precise enough to draw distinctions of that kind.

### Inputs

The Disparity To Z node's three inputs take the left and right images along with a camera node. Left Input: Wire either the left eye image or the stack image into the orange input. Right Input: Wire the right eye image into the green input. You can only use this input when the Stack Mode menu rests on Separate. Stereo Camera: Wire a stereo camera node into the magenta input.

### Outputs

In a break from how most Fusion nodes behave, Disparity To Z exposes two outputs, one for each eye. Left Output: This carries the left eye image bearing a new Z channel, or a Stacked Mode image bearing a new disparity channel. Right Output: This carries the right eye image bearing a new Z channel. The output appears solely when Stack Mode is set to Separate.

### Basic Node Setup

Disparity To Z takes in a 3D camera together with stereo images that hold a disparity channel. What it returns is an image carrying a freshly computed Z channel.

A Disparity to Z node creates an image with a Z channel.

### Inspector

### The Disparity To Z Controls tab

### Controls Tab

On top of writing Z values into the Z channel, this tab bumps the color channels up to float32 and emits the Z values into the color channels in the form {z, z, z, 1}. This option is handy for a fast peek at the Z channel. NOTE: Z values run negative, turning more negative as your distance from the camera grows. Since the viewers display only 0.0 to 1.0 color, any other data must be remapped through a normalization step to fall within a 0-1 display range. To pull that off, right-click within the viewer and pick Options > Show Full Color Range. Output Z to RGB Instead of confining the Z values to the linked aux channel alone, this copies them into the RGB channels so any of Fusion's nodes can work on them further. Refine Z The Enable checkbox sharpens the depth map using the RGB channels. That refinement nudges the flow's edges into tighter agreement with the color channels' edges. The trade-off is that unwanted detail from the color channels begins surfacing in the flow. It can be worth trying this option to ease off harsh edges for Z-channel post effects such as depth of field or fogging.

HiQ Only Switching this checkbox on confines the Refine Z option to running only while rendering sits at High Quality. To confirm High Quality is on, right-click just to either side of the transport controls in the main toolbar. Strength Raising this slider accomplishes two things at once. It evens out the depth across regions of constant color and shifts edges in the Z channel so they track edges in the RGB channels. The drawback of pushing the refinement is that texture from the color channel starts appearing in the Z channel. You'll want to strike a balance between the two. Radius This sets the radius used by the smoothing algorithm. Stack Mode This menu sets how the input images are stacked. With Separate selected, the Right Input and Output emerge, and you must wire in distinct left and right images. Swap Eyes Switching on this checkbox swaps the left and right images.

### The Disparity To Z Camera tab

### Camera Tab

When accurate real-world Z values matter because you're trying to line an effect up with a scene that already exists, turn to the External Camera options to recover precise Z values. Where any Z-buffer will do and you aren't fussy about the exact way it's offset and scaled, or where no camera is on hand, the Artistic option may come in handy.

- External Mode: The node exposes an input for hooking up an existing stereo Camera 3D. That can be either a lone stereo Camera 3D (i.e., one whose eye separation is non-zero), or a pair of (tracked) Camera 3Ds joined through the Camera 3D > Stereo > Right Camera input.
- Artistic Mode: Lacking a camera, you can work these controls to yield an “artistic” Z channel whose values won't be physically correct yet remain useful. To rebuild the Disparity > Z Curve, choose (D, Z) values for one point up front and one point in the back.

TIP: Should artistic mode feel a touch too “artistic” and you'd rather tune more physically-grounded parameters (e.g., convergence and eye separation), spin up a dummy Camera 3D, wire it into the Disparity To Z > Camera input, and then play with the Camera 3D's controls.

Foreground Disparity (Pick from Left Eye) Once the camera Mode sits on Artistic, you gain a Foreground Disparity slider. It holds the disparity belonging to the nearest foreground object. The depth value named in the Foreground Depth control is where it gets mapped. Should any object's disparity fall beyond the range [ForegroundDisparity, BackgroundDisparity], its disparity gets clamped to that range, which flattens patches of the Z channel, so be sure the values you choose bracket the true disparity range. Background Disparity (Pick from Left Eye) Once the camera Mode sits on Artistic, a Background Disparity becomes available. It holds the disparity belonging to the farthest background object. The depth value named in the Background Depth control is where it gets mapped. Picture this input as the ceiling on disparity values for objects sitting at -infinity. The value here is meant for the left eye. Over in the right eye, the matching value carries the same magnitude but flips negative. Foreground Depth This is where Foreground Disparity ends up mapped. Read it as the depth of the closest object. Bear in mind the values here run positive in depth. Background Depth This is where Background Disparity ends up mapped. Read it as the depth of the farthest object. Falloff Falloff shapes the depth curve stretching between the foreground and background depths you asked for. With Hyperbolic chosen, the disparity-depth curve roughly follows depth = constant/ disparity. With Linear chosen, the curve follows depth = constant \* disparity. Hyperbolic leans toward stressing Z features up front, whereas linear hands foreground and background features equal weight in the Z channel. Absent a particular reason, go with Hyperbolic, since it tracks physics more closely, while Linear bears no relation to nature and exists purely for artistic effect.
