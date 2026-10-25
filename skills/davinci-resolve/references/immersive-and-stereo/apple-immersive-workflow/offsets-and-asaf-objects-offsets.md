# Offsets and asaf objects offsets

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](head-and-room-simulation.md) / [Next section](spatial-filter-and-asaf-scene-spatial-filter.md)
<a id="source-asaf-objects--metadata"></a> <a id="source-asaf-objects--offsets"></a> <a id="source-asaf-objects--reverb"></a> <a id="source-asaf-scene--gain-control"></a> <a id="source-asaf-scene-controls"></a> <a id="source-asaf-scene-transform"></a> <a id="source-gain"></a> <a id="source-metadata"></a> <a id="source-offsets"></a> <a id="source-reverb"></a> <a id="source-transform"></a>

### Offsets

The Radius Offset parameter tacks on as much as 200 meters to the distance the 3D Panner's Radius parameter sets. This control appears only where the Fairlight mixer has the track's Panner plugin set to 3D Spherical.

### ASAF Objects – Offsets

When the 3D Panner is showing the Cartesian View, the X, Y, and Z Offsets laid out below appear in this section: X Offset: Fixes the offset on the panner's Left/Right parameter, ranging from -200 m to +200m. Y Offset: Fixes the offset on the panner's Front/Back parameter, ranging from -200 m to +200m. Z Offset: Fixes the offset on the panner's Down/Up parameter, ranging from -200m to +200m.

### Reverb

You switch this reverb effect on by ticking the Reverb checkbox sitting above the Mix control, which governs how much reverb reaches the ASAF Object.

### ASAF Objects – Reverb

NOTE: This Reverb section only affects ASAF Objects.

### Metadata

Rather than handling it in the Track Index, you can use this part of the Audio Inspector to attach the right metadata information to the object through the settings below:

### ASAF Objects – Metadata

- Content Type: Through this drop-down menu, the object gets classed as either Music and Effects or Interactive.
- M & E Tag: Where the content carries a Music and Effects tag, this dropdown's options let you pin the object down further—say, Music, Effects, Dialogue, Narration, etc.
- Interactivity: Where the content was tagged Interactive, picking an entry from this list narrows the object down further, to something like Commentary or Audio Description.
- Salience: Hands the object audio a level of importance, helping the ASAF export encoder rank it against the project's other ASAF objects.
- Language: Through this dropdown you set the content's language.
- Post Reverb: While active, the object is configured so the playback application — Vision Pro, for one — can read the room characteristics of the users' listening environment and, should they choose, layer in a fitting reverb setting. Post Reverb stacks on top of whatever reverb settings the ASAF Object Reverb noted above applies. It leaves the output from the ASAF Renderer plugins untouched, though.

### ASAF Scene Controls

### Gain

Switched on by ticking the Gain Enable checkbox, this plugin raises or drops the ASAF Scene's gain in line with whatever level the Gain control sets.

### ASAF Scene – Gain Control

### Transform

You reach for the Transform controls laid out below to make positional changes inside an ASAF Scene.

### ASAF Scene –Transform

- Mirror Left/Right: Tick this checkbox to swap sounds' positions from left to right by flipping the whole scene.
- Mirror Up/Down: Fill this checkbox in to flip sound's vertical placement by turning the scene upside down.
- Mirror Front/Back: Tick this checkbox for a front-to-back flip of the whole scene, swapping where sounds sit along the front–back axis.
- Rotation Enable: Filling the checkbox in switches on the Yaw, Pitch, and Roll parameters and applies them per their respective values.
- Yaw: Swings the scene left or right about the vertical axis.
- Pitch: Tips the scene forward or back about the horizontal axis.
- Roll: Tilts or rolls the scene from side to side.
