# Transform 3D and triangulate 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Transform 3D, Triangulate 3D.
[Chapter index](INDEX.md) / [Previous section](text-modifier-behavior.md) / [Next section](triangulate-3d-and-uv-map-3d-and-weld-3d.md)
<a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-import-transform-browser"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-pivot-controls"></a> <a id="source-rotation"></a> <a id="source-scale"></a> <a id="source-the-transform-3d-node"></a> <a id="source-the-triangulate-3d-node"></a> <a id="source-transform-3d-3xf"></a> <a id="source-transform-3d-controls"></a> <a id="source-transform-3d-node-introduction"></a> <a id="source-transform-3d-onscreen-transformation-controls"></a> <a id="source-translation"></a> <a id="source-triangulate-3d-3tri"></a> <a id="source-triangulate-3d-node-introduction"></a>

### Transform 3D [3XF]

### The Transform 3D node

### Transform 3D Node Introduction

You can apply the Transform 3D node to move, spin, or resize every element inside a scene without a Merge 3D node being needed. That comes in handy for hierarchical transforms, or for shifting objects that get merged into one scene several times over. The controls it exposes match those in the Transformation tabs of the other 3D nodes.

### Inputs

A single mandatory input on the Transform node accepts a 3D scene or a 3D object. Scene Input: Wire the orange scene input to a 3D scene or 3D object so an extra layer of transformation controls is applied.

### Basic Node Setup

On top of whatever transforms already exist on the 3D node before it, the Transform 3D node layers additional 3D position, rotation, and pivot control. Chain several Transform 3D nodes one after another to construct parenting or hierarchical movement.

Transform 3D nodes strung together to create a parenting hierarchy Inspector

### Transform 3D controls

### Controls Tab

For the Transform 3D node, the Controls tab is the main tab. It carries controls that move, spin, or resize all elements inside a scene without a Merge 3D node being required.

### Translation

- X, Y, Z Offset: These controls place the 3D element wherever you want within 3D space.

### Rotation

- Rotation Order: These buttons pick the sequence in which rotation is applied along each of the object’s axes. As an example, XYZ rotates the X-axis first, then the Y-axis, and the Z-axis last.
- X, Y, Z Rotation: Turn the object about its pivot point with these controls. When the Use Target checkbox is on, rotation is measured against the target’s position; if it isn’t, the global axis governs instead.

### Pivot Controls

- X, Y, Z Pivot: An object turns around its pivot point. By default an object spins about its own center, treated as a pivot at 0,0,0. Use these controls to shift the pivot away from that center.

### Scale

- X, Y, Z Scale: With the Lock X/Y/Z checkbox checked, only one scale slider appears. It changes the object’s overall size. Clear the Lock checkbox and separate X, Y, and Z sliders appear, letting you scale along any dimension.

NOTE: While the Lock checkbox is checked, you cannot scale individual dimensions, not even by dragging particular axes of the Transformation widget while in Scale mode.

Use Target Turning on the Use Target checkbox brings up a group of controls for placing an XYZ target. With Use Target active, the object continuously turns so it faces the target. Its rotation is then measured relative to that target. Import Transform Brings up a file browser in which you pick a scene file that your 3D application saved or exported. The supported formats are:

LightWave Scene Max Scene Maya Ascii Scene dotXSI

.lws .ase .ma .xsi

The Import Transform button brings in transformation data alone. To bring in 3D geometry, lights, and cameras, look instead at the File > FBX Import option in the menus.

### Import Transform Browser

Onscreen Transformation Controls The Onscreen Transformation controls offer another route to the same settings found in the Inspector. The viewer supplies modes for moving, rotating, and scaling. Switch the mode of the onscreen controls by clicking one of the three buttons in the toolbar running down the side of the viewer. You can also toggle between modes via these keyboard shortcuts: Q handles translation, W handles rotation, and scaling uses E. Across all three modes, drag a single axis of the control to affect only that axis, or drag the control’s center to affect all three at once. By default the scale sliders on most 3D nodes are locked, producing uniform scaling on all three axes. Clear the Lock X/Y/Z Scale checkbox to resize an object along just one axis.

### Transform 3D onscreen transformation controls

### Triangulate 3D [3Tri]

### The Triangulate 3D node

### Triangulate 3D Node Introduction

What sets the Triangulate 3D node apart is that it carries no controls whatsoever. The node converts polygon shapes into triangles. A quad made of four points, for example, ends up as two triangles. Its job is to break complicated polygon shapes down into a mesh so they process more readily.

### Inputs

A single mandatory input on the Triangulate 3D node accepts a 3D scene or a 3D object. Scene Input: Wire the orange scene input to the 3D scene or 3D object you intend to triangulate.
