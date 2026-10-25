# Spherical camera and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Spherical camera, Common controls.
[Chapter index](INDEX.md) / [Previous section](lat-long-patcher-and-panomap-and-spherical-camera.md) / [Spherical Camera 3SC](lat-long-patcher-and-panomap-and-spherical-camera.md)
<a id="source-append-to-track"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-1"></a> <a id="source-inspector-2"></a> <a id="source-settings-tab"></a> <a id="source-spherical-stabilizer-node-introduction"></a> <a id="source-the-common-controls"></a> <a id="source-the-spherical-stabilizer-controls-tab"></a> <a id="source-the-vr-common-controls"></a>

### Spherical Stabilizer Node Introduction

Because VR live action so often relies on handheld cameras, shaky footage tends to be a recurring headache. The Spherical Stabilizer node finds and tracks visible features in the footage on its own, then studies how they move to work out pan, tilt, and roll rotations. With the tracking complete, you can then smooth or steady the footage's rotation.

### Inputs

A lone orange input sits on the Spherical Stabilizer node. Image: This orange image input node needs a spherical-layout image; acceptable forms include Lat Long (2:1 equirectangular) VR 180, Horizontal/Vertical Cross, and Horizontal/Vertical Strip.

### Basic Node Setup

For the example below, a 2:1 Lat Long image links into the input of the Spherical Stabilizer node. After the image has been stabilized, what the Spherical Stabilizer node puts out is a steadied clip.

A Spherical Stabilizer configured to settle a 2:1 Lat Long clip Inspector

### The Spherical Stabilizer Controls tab

### Controls Tab

On the Controls tab sit the parameters that kick off the tracking and shape the results toward stabilization or smoothing. Reject Dominant Motion Outliers While Tracking When this control is switched on (which is the default), any features moving against the grain of the majority get disregarded. Doing so helps the node tune out the movement of the shot's subjects, favoring instead the steady, dependable markers of the surroundings.

Track Controls Pressing these buttons launches the tracking and analysis of the shot. Keep in mind that the reference frame for stabilization is taken to be the first frame that gets tracked.

- Track Backward from End Frame begins running the track in reverse, beginning at the end of the current render range.
- Track Backward from Current Time begins running the track in reverse, beginning at the current frame.
- Stop halts tracking while keeping every result gathered up to that point.
- Track Forward from Current Time begins running the track forward, beginning at the start of the current render range.
- Track Forward from Start Frame begins running the track forward, beginning at the current time.

### Append to Track

- Replace makes the Track Controls throw out whatever tracking results came before and put the freshly created track in their place.
- Append tacks the new tracking results onto any tracks made earlier.

Stabilization Strength This control adjusts how much smoothing or stabilization gets applied, running from 0.0 (no change) up to 1.0 (maximum). Smoothing The Spherical Stabilizer node is able to strip every bit of rotation from a shot, locking the forward viewpoint (Still mode, 0.0), or it can gently iron out any panning, rolling, or tilting to make viewing more comfortable (Smooth mode, 1.0). The slider lets you pick either extreme or land anywhere between them. Offset Rotation A shot is frequently a touch off-level and needs its horizon straightened, or perhaps you want to bring a deliberate pan back in once the shot has been fully stabilized. The Offset Rotation controls give you extra hands-on command over how the Spherical Stabilizer rotates the footage, covering pitch/tilt (X), pan/yaw (Y), and roll (Z) in turn. That rotation always runs in the order X, Y, Z.

### Common Controls

Settings Tab Across the other VR nodes, the Inspector's Settings tab turns up again unchanged. A detailed account of these common controls appears just below, in the “The Common Controls” section.

### The Common Controls

The nodes that take on VR operations have a set of identical controls in the Inspector in common. What follows lays out the controls shared across the VR nodes.

### Inspector

### The VR Common controls

### Settings Tab

Every tool in the VR category carries the Settings tab within the Inspector. Its controls stay the same and behave identically from one tool to the next. Apply Mask Inverted Switching on the Apply Mask Inverted option flips the whole mask channel for that tool. The mask channel itself is the pooled outcome of every mask either fed into or produced within a node. Use GPU There are three settings on the Use GPU menu. Choosing Disable shuts off hardware-accelerated rendering that would otherwise use your computer's graphics card. Auto draws on a capable GPU when one is on hand and drops back to software rendering whenever a capable GPU isn't.

Hide Incoming Connections Ticking this checkbox lets you conceal the connection lines coming from upstream nodes, which makes a node tree read more cleanly and clearly. With it on, the Inspector shows an empty field for each input on a node. Drag a connected node out of the node tree into that empty field and the incoming connection line stays hidden for as long as the node isn't selected within the node tree. Select the node in the node tree, though, and the line shows again. Comments You use the Comments field to attach notes to a tool. Click into the empty field and type your text. Once a note is on a tool, a small red square shows in the node's lower-left corner while the full tile is on view, or a small text bubble icon shows on the right when nodes are collapsed. To read the note in the Node Editor, rest the mouse pointer on the node so the tooltip appears. Scripts Every tool in Fusion offers three Scripting fields on the Settings tab. Each holds an edit box into which you place scripts that execute as the tool renders. To learn more about scripting nodes, please refer to the Fusion scripting documentation.
