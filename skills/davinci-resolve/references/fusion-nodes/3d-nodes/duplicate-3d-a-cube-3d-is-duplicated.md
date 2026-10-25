# Duplicate 3D a cube 3D is duplicated

Version: DaVinci Resolve 20.3 Reference Manual. Context: Duplicate 3D.
[Chapter index](INDEX.md) / [Previous section](custom-vertex-3d-and-displace-3d-and-duplicate-3d.md) / [Next section](duplicate-3d-transform-method.md) / [Duplicate 3D 3Dp](custom-vertex-3d-and-displace-3d-and-duplicate-3d.md)
<a id="source-a-cube-3d-is-duplicated"></a> <a id="source-basic-node-setup-3"></a> <a id="source-controls-tab-2"></a> <a id="source-duplicate-3d-controls"></a> <a id="source-inputs-3"></a> <a id="source-inspector"></a>

### Inputs

By default the Duplicate 3D node carries one input where a 3D scene connects. Depending on the node's settings, an optional Mesh input shows up. SceneInput: The orange Scene Input is a required input. Whatever scene or object you wire here gets duplicated per the settings in the Inspector's Control tab. MeshInput: A green optional mesh input surfaces once the Region tab's Region menu is set to mesh. That mesh can be any 3D model, whether built in Fusion or imported.

### Basic Node Setup

A Duplicate 3D node's output usually feeds a Merge 3D node, folding it into a bigger scene. The 3D geometry you want copied, here a Cube 3D, wires into the orange input.

### A Cube 3D is duplicated

### Inspector

### Duplicate 3D controls

### Controls Tab

Every parameter for creating, offsetting, and scaling copies of the object wired to the node's scene input lives in the Controls tab. Copies This range control sets how many copies get made. Each copy duplicates the previous one, so with this control at [0,3] the parent is copied, then that copy is copied, then the copy of the copy, and onward. That opens up some intriguing effects once transformations are laid on each copy through the controls below. Raising the First Copy above 0 drops the original object and leaves only the copies on view. Time Offset The Time Offset slider shifts any animations applied to the source geometry by a fixed amount per copy. Try setting the value to -1.0, say, using as your source a cube animated to spin on the Y-axis. A frame earlier is what the first copy displays; the second copy reaches back another frame; and onward. On textured planes this works to great effect—where successive frames of a clip can be displayed, for instance.
