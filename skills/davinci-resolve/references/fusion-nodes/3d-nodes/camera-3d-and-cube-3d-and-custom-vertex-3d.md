# Camera 3D and cube 3D and custom vertex 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera 3D, Cube 3D, Custom vertex 3D.
[Chapter index](INDEX.md) / [Previous section](camera-3d-control-visibility.md) / [Next section](custom-vertex-3d-and-displace-3d-and-duplicate-3d.md) / [Camera 3D 3Cm](bender-3d-and-camera-3d.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-cube-3d-3cb"></a> <a id="source-cube-3d-controls"></a> <a id="source-cube-3d-node-introduction"></a> <a id="source-custom-vertex-3d-3cv"></a> <a id="source-custom-vertex-3d-node-introduction"></a> <a id="source-custom-vertex-3d-node-numbers-tab"></a> <a id="source-custom-vertex-3d-node-vertex-tab"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-numbers-tab"></a> <a id="source-points-tab"></a> <a id="source-the-cube-3d-node"></a> <a id="source-the-custom-vertex-3d-node"></a> <a id="source-tips-for-camera-3d"></a> <a id="source-vertex-tab"></a>

### Tips for Camera 3D

Camera Projection: While importing a camera from a 3D application that doubles as a projector, confirm the Fit Resolution Gate options sit in agreement across both the Controls tab and the Projection tab. Only the former sets itself automatically to whatever the 3D app had in use. You may need to set the latter by hand. Image Plane: The camera's image plane is more than a virtual guide in the viewers. It's real geometry that you can project onto as well. Putting a different image on the image plane calls for inserting a Replace Material node after your Camera node. Parallel Stereo: Reaching true Parallel Stereo mode can be done three ways:

- Connect an additional external (right) camera to the green Right Stereo Camera

input of your camera.

- Create separate left and right cameras.
- With Toe-In or Off Axis in play, push the Convergence Distance slider out to an enormous

value of 999999999. Rendering Overscan: Rendering an image with overscan means you also have to alter your scene's Camera3D. Because overscan settings don't travel along with camera data out of 3D applications, this holds for cameras you've imported through .fbx or .ma files too. The fix is to bump the film back's width and height up by whatever factor accounts for the extra pixels on every side.

### Cube 3D [3Cb]

### The Cube 3D node

### Cube 3D Node Introduction

A simple primitive geometry type, the Cube 3D node can produce a plain cube. On top of that, the node offers six extra image inputs for mapping a texture onto the cube's six faces. Often cubes serve as shadow-casting objects and for environment maps. To explore other basic primitives, look at the Shape 3D node in this chapter.

### Inputs

These optional inputs turn up on the Cube3D node within the Node Editor: SceneInput: Through the orange scene input you connect another node that builds or holds a 3D scene or object. That extra geometry merges into the Cube3D. NameMaterialInput: These six inputs assign the materials that go onto the cube's six faces. Either a 2D image or a 3D material can wire into these inputs. Any textures or materials placed on the Cube3D never carry over to 3D objects connected at the Cube's SceneInput.

### Basic Node Setup

A Cube 3D node's output usually feeds a Merge 3D node, folding it into a bigger scene. During 3D tracking, the Cube 3D frequently stands in as a placeholder for the real geometry that isn't on hand yet.

Cube 3D node wired into a 3D scene that was exported out of the Camera Tracker node Inspector

### Cube 3D controls

### Controls Tab

The Inspector's opening tab is the Controls tab. Inside it sit the main controls that set the Cube 3D node's overall size and shape. Lock Width/Height/Depth Ticking this checkbox binds the cube's Width, Height, and Depth dimensions as one. With it ticked, only a Size control appears; otherwise you get separate Width, Height, and Depth sliders. Size or Width/Height/Depth When the Lock checkbox is ticked, just the Size slider shows; otherwise separate sliders appear for Width, Height, and Depth. Since the Size and Width sliders are one control under two names, any animation put on Size carries to Width as well once the controls are unlocked. Subdivision Level The Subdivision Level slider sets how many subdivisions go into building the image plane. Because the 3D viewers and renderer rely on vertex lighting, every bit of lighting is worked out at the 3D geometry's vertices and interpolated from there. So the more subdivisions a mesh holds, the more vertices there are to carry the lighting. As an illustration, build a sphere and keep its subdivisions low so it looks chunky. With lighting switched on, the object reads as a sphere yet shows some fracturing owing to the wide spacing between vertices. Raise the subdivisions and the vertices draw closer, smoothing the lighting out. That makes raising subdivisions handy while you tune lights interactively. Cube Mapping Tick the Cube Mapping checkbox and the cube wraps its first texture over all six faces through a standard cubic mapping technique. This method counts on a texture arranged in a cross shape. Wireframe Tick this checkbox and the mesh renders nothing but the object's wireframe whenever the OpenGL renderer in the Renderer 3D node is doing the rendering.

### Common Controls

Controls, Materials, Transform, and Settings Tabs Many 3D nodes share the remaining controls covering Object ID, Normals/Tangents, Blend Mode, Matte, Lighting, and Visibility. The Materials, Transform, and Settings tabs hold true the same way. You'll find their descriptions in the "The Common Controls" section at the close of this chapter.

### Custom Vertex 3D [3CV]

### The Custom Vertex 3D node

### Custom Vertex 3D Node Introduction

For 3D geometry, the Custom Vertex 3D node is an advanced custom node carrying out per vertex manipulations. With a fair bit of scripting or C++ programming under your belt, the structure and terminology the Custom node uses should feel familiar. By way of scripting math functions plus lookup tables drawn from images, you can shift vertex positions on 3D geometry. Vertices amount to more than mere positions in 3D space. Normals, texture coordinates, vectors, and velocity are all open to manipulation. As an example, Custom Vertex 3D can set a flat plane waving like a flag, or build spiral models. Alongside a 3D scene input and three image inputs, the Inspector carries as many as eight number fields and up to eight XYZ position values pulled from other controls and parameters across the node tree. NOTE: Altering a 3D object's X, Y, and Z positions leaves the normals/tangents alone. Afterward you can run a ReplaceNormals node to recompute the normals/tangents.

TIP: Every attribute isn't present on all geometry. Most Fusion geometry, for instance, lacks vertex colors, save for particles and certain imported FBX/Alembic meshes. None of the geometry currently carries environment coordinates, and velocities belong to particles alone. When an attribute is missing from the input geometry, a default value is assumed for it.

### Inputs

Four inputs sit on the Custom Vertex 3D node. Of those four, only the orange scene input is mandatory. SceneInput: The orange scene input receives 3D geometry or a 3D scene from a 3D node's output. This is the 3D scene or geometry that the Custom Vertex 3D node's calculations operate on. ImageInput1, ImageInput2, ImageInput3: Colored green, magenta, and teal, the three image inputs are optional ones available for compositing. NOTE: Attributes absent from the input geometry get created whenever the expression for an attribute is nontrivial. The attribute values are supplied as in the point above. Should the input geometry lack normals, for example, the values of (nx, ny, nz) always come out (0,0,1). To alter that, you might run a ReplaceNormals node beforehand to generate them.

### Basic Node Setup

Whatever object you mean to manipulate wires into the orange scene input of the Custom Vertex 3D node. Its output usually feeds a Merge 3D node, folding it into a bigger scene.

Custom Vertex 3D node manipulating an Image Plane 3D node Inspector

### Custom Vertex 3D node Vertex tab

### Vertex Tab

The Vertex tab's fields let you run vertex calculations across these attributes: Velocity, UV Tangents, Environment Coordinates, Texture Coordinates, Vertex Color, Normals, and Position. Three XYZ Position values in world space define the vertices as px, py, pz. Normals state, as a vector, the direction the vertex faces as nx, ny, nz. The point's Red, Green, Blue, and Alpha color make up the vertex color as vcr, vcg, vcb, vca.

### Numbers Tab

Numbers 1-8 Numbers are variables fronted by a dial control that can be animated or wired to modifiers just like any other control. Within per-vertex equations the numbers serve two forms—evaluated at the present frame as n1, n2, n3, n4,… or, for an arbitrary moment t, as n1_at(float t), n2_at(float t), n3_at(float t), n4_at(float t). Expressions over in the Setup and Intermediate tabs can read these controls' values. Through the Config tab you can rename them and keep them out of the viewer.

### Custom Vertex 3D node Numbers tab

### Points Tab

Points 1-8 Rather than the vertices, the point controls stand for points within the Custom Vertex 3D tool. These eight point controls bring 3D X,Y,Z position controls for placing points at the current time: (p1x, p1y, p1z, p2x, p2y, p2z) or at any time: p1x_at(float t), p1y_at(float t), p1z_at(float t), p2x_at(float t), p2y_at(float t), p2z_at(float t), where t is the time you want. You might, for instance, use a point to mark a spot in 3D space for the vertices to rotate about. Through the Config tab they can be renamed and hidden from the viewer. Being ordinary positional controls, they can be animated or wired to modifiers like any other node.
