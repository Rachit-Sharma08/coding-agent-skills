# Ribbon 3D and shape 3D and soft clip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ribbon 3D, Shape 3D, Soft clip.
[Chapter index](INDEX.md) / [Previous section](replace-normals-3d-and-replicate-3d-and-ribbon-3d.md) / [Next section](soft-clip-basic-node-setup.md) / [Continue Soft Clip 3SC / Basic Node Setup](soft-clip-basic-node-setup.md) / [Ribbon 3D 3Ri](replace-normals-3d-and-replicate-3d-and-ribbon-3d.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-4"></a> <a id="source-common-controls-5"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-ribbon-3d-controls"></a> <a id="source-ribbon-3d-generates-lines-distorted-by-additional-nodes"></a> <a id="source-shape-3d-3sh"></a> <a id="source-shape-3d-controls"></a> <a id="source-shape-3d-node-introduction"></a> <a id="source-soft-clip-3sc"></a> <a id="source-soft-clip-node-introduction"></a> <a id="source-spherical-mapping-differences"></a> <a id="source-the-shape-3d-node"></a> <a id="source-the-soft-clip-node"></a>

### Inputs

The Ribbon 3D node carries a pair of inputs: one taking the destination geometry that holds the vertices, plus one for the 3D geometry you wish to replicate. 3D Scene: The orange input takes a 3D scene or geometry. Material: The input takes the 2D texture for the ribbon. Neither wired input is required.

### Basic Node Setup

In the example below, a Ribbon 3D node is put to work building lines. A gradient background is wired in to “colorize” the lines. Further nodes then follow the Ribbon 3D to bend and warp the lines.

### Ribbon 3D generates lines distorted by additional nodes

### Inspector

### Ribbon 3D controls

### Controls Tab

The Controls tab fixes the count of ribbon strands plus their size, length, and spacing. Number of Lines How many parallel lines get drawn spanning the start point through to the end point. Line Thickness Within the user interface, line thickness is allowed to hold a floating-point value, though some graphics cards permit only integer values. Some cards may permit only lines equal to or thicker than one, or top out at a certain value. Subdivision Level How many vertices sit on each line running from start point to end points. The greater that count, the more precise and smoother 3D displacement looks. Ribbon Width Fixes how far apart the lines sit from one another. Start XYZ control to fix the start point of the ribbon. End XYZ control to fix the end point of the ribbon. Ribbon Rotation Permits rotation of the ribbon about the virtual axis laid out by start point and end points. Anti-Aliasing Lets you lay anti-aliasing on the rendered lines. Reaching for anti-aliasing isn't necessarily advised. Switched on, there may be gaps between the line segments. That's especially noticeable at high values of line thickness. Once again, how the lines get drawn rests entirely on the graphics card, which means these artifacts can differ from card to card.

### Common Controls

Controls, Materials, and Settings Tabs Within the Controls tab, the controls covering Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID recur across many 3D nodes. Likewise the Inspector's Materials tab plus Settings tab appear again in other 3D nodes. A detailed account of these shared controls sits toward this chapter's end in the “The Common Controls” section.

### Shape 3D [3Sh]

### The Shape 3D node

### Shape 3D Node Introduction

The Shape 3D node serves to turn out several basic primitive 3D shapes, planes, cubes, spheres, and cylinders among them.

### Inputs

The Shape 3D offers a pair of optional inputs. Folding additional geometry in with the Shape 3D is the scene input's job, whereas texture mapping the Shape 3D object falls to the material input. SceneInput: Even though the Shape 3D builds its own 3D geometry, you can reach for the orange scene input to fold in an additional 3D scene or geometry. MaterialInput: The green input takes either a 2D image or a 3D material. Supply a 2D image and it acts, for the node's built-in basic material, as that material's diffuse texture map. Hook up a 3D material and the basic material gets switched off.

### Basic Node Setup

In the example below, four Shape 3D nodes are put to work building the primitives of a 3D set. Two of the Shape 3D nodes get wired together, forming a more elaborate primitive shape. Those shapes can then be paired with a Projector 3D to texture them using a realistic material.

Shape 3D nodes paired with a Projector 3D so as to build a realistic 3D set

### Inspector

### Shape 3D controls

### Controls Tab

The Controls tab lets you pick a shape and reshape its geometry. Different controls surface depending on the particular shape you opt to build. Shape This menu lets you pick the primitive geometry that the Shape 3D node turns out. The rest of the controls in the Inspector shift to suit the chosen shape.

- Lock Width/Height/Depth: [plane, cube] Tick this checkbox and the width, height, and depth controls get locked together as a single size slider. Otherwise, individual controls over the shape's size along each axis are on offer.
- Size Width/Height/Depth: [plane, cube] Serves to govern the shape's size.

Cube Mapping With Cube chosen in the shape menu, the Cube relies on cube mapping to lay on the Shape node's texture (a 2D image wired to the material input on the node). Radius With a Sphere, Cylinder, Cone, or Torus chosen in the shape menu, this control fixes the radius of the chosen shape. Top Radius With a cone chosen in the Shape menu, this control serves to set a radius for the top of a cone, making truncated cones possible to build. Start/End Angle With the Sphere, Cylinder, Cone, or Torus shape chosen in the Shape menu, this range control fixes how much of the shape gets drawn. A start angle of 180° together with an end angle of 360° would draw only half of the shape.

Start/End Latitude With a Sphere or Torus chosen in the Shape menu, this range control serves to crop or slice the object by laying out a latitudinal subsection of it. Bottom/Top Cap With Cylinder or Cone chosen in the Shape menu, the Bottom Cap and Top Cap checkboxes serve to decide whether the end caps of these shapes get built or whether the shape stays open. Section With the Torus chosen in the Shape menu, Section governs the thickness of the tube that makes up the torus. Subdivision Level/Base/Height The Subdivision controls serve to fix the tessellation of the mesh across all shapes. The higher the subdivision, the more vertices each shape carries. Wireframe Tick this checkbox and the mesh renders only the wireframe for the object.

### Common Controls

Controls, Materials, Transform and Settings Tabs Within the Controls tab, the controls covering Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID recur across many 3D nodes. Likewise the Inspector's Materials tab, Transforms tab, and Settings tab appear again in other 3D nodes. A detailed account of these shared controls sits in the “The Common Controls” section, found toward this chapter's end. Using a Sphere Map versus wiring the texture straight onto a sphere: rather than running it through the Sphere Map node first, you can connect a LatLong (equirectangular) texture map directly to a sphere. That yields a different rendering once you set the start/end angle and latitude below 360°/180°. In the first case, the texture comes out squashed. With the Sphere Map node in use, the texture comes out cropped. Compare:

### Spherical mapping differences

NOTE: Pipe the texture straight into the sphere and it also gets mirrored horizontally. You can alter this by running a Transform node first.

### Soft Clip [3SC]

### The Soft Clip node

### Soft Clip Node Introduction

The Soft Clip node serves to fade out geometry and particles that draw near the camera. That helps sidestep the visible “popping off” that plagues many particle systems and 3D flythroughs. This node closely resembles the Fog 3D node, in that it hinges on the geometry's distance from the camera.

### Inputs

The Soft Clip carries only a single input for a 3D scene that has a camera wired to it. SceneInput: The orange scene input is a required connection. It takes a 3D scene input carrying a Camera 3D node.
