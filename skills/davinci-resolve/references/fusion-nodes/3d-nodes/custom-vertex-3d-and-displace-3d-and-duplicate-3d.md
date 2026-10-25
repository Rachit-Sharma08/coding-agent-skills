# Custom vertex 3D and displace 3D and duplicate 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom vertex 3D, Displace 3D, Duplicate 3D.
[Chapter index](INDEX.md) / [Previous section](camera-3d-and-cube-3d-and-custom-vertex-3d.md) / [Next section](duplicate-3d-a-cube-3d-is-duplicated.md) / [Continue Duplicate 3D 3Dp / Transform Method](duplicate-3d-transform-method.md) / [Custom Vertex 3D 3CV](camera-3d-and-cube-3d-and-custom-vertex-3d.md)
<a id="source-basic-node-setup-2"></a> <a id="source-camera-displacement"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-config-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-custom-vertex-3d-node-config-tab"></a> <a id="source-custom-vertex-3d-node-intermediate-tab"></a> <a id="source-custom-vertex-3d-node-lut-tab"></a> <a id="source-custom-vertex-3d-node-points-tab"></a> <a id="source-custom-vertex-3d-node-setup-tab"></a> <a id="source-displace-3d-3di"></a> <a id="source-displace-3d-controls"></a> <a id="source-displace-3d-node-introduction"></a> <a id="source-duplicate-3d-3dp"></a> <a id="source-duplicate-3d-node-introduction"></a> <a id="source-inputs-2"></a> <a id="source-intermediate-tab"></a> <a id="source-lut-tab"></a> <a id="source-point-controls"></a> <a id="source-setup-tab"></a> <a id="source-the-displace-3d-node"></a> <a id="source-the-duplicate-3d-node"></a>

### Custom Vertex 3D node Points tab

### LUT Tab

LUTs 1-4 Four LUT splines come with the Custom Vertex 3D node. A LUT is a lookup table that hands back a value taken from the LUT spline's height. To reach the LUT values, for instance, you call getlut1(float x), getlut2(float x),... with x = 0 … 1. Expressions in the Setup and Intermediate tabs can reach these controls' values through the getlut# function. Setting the R, G, B, and A expressions to getlut1(r1), getlut2(g1), getlut3(b1), and getlut4(a1) respectively, for instance, would make the Custom Vertex 3D node act like the Color Curves node. The Config tab's options let you rename these controls so their purpose reads more plainly, though expressions still see the values as lut1, lut2,...lut8.

### Custom Vertex 3D node LUT tab

### Setup Tab

Setups 1-8 As many as eight separate expressions can be worked out in the Setup tab of the Custom Vertex 3D node. Each Setup expression is evaluated once per frame, ahead of every other calculation. Its results then become available to the node's other expressions as variables s1, s2, s3, and s4. Picture them as global setup scripts that the intermediate and channel scripts can call on for each vertex.

### Custom Vertex 3D node Setup tab

For instance, Setup scripts can carry a vertex from model space into world space. NOTE: Because these expressions evaluate just once per frame rather than per pixel, there's no point pulling in channel variables such as r1, g1, b1, and the like, nor per-pixel variables such as X and Y. Permitted values cover constants, variables like n1…n8, time, W and H, and the like, plus functions such as sin() or getr1d().

### Intermediate Tab

Intermediates 1-8 A further eight expressions can be worked out in the Intermediate tab. Each Intermediate expression runs once per vertex, after the Setup expressions have been evaluated. The results come back as variables i1, i2, i3, i4, i5, i6, i7, i8, which channel scripts can call on. Picture them as "per vertex setup" scripts. You might, for example, run the script to make the new vertex (i.e., new position, normal, tangent, UVs, etc.) or to carry it from world space back into model space.

### Custom Vertex 3D Node Intermediate tab

### Config Tab

Random Seed This sets the seed feeding the rand() and rands() functions. Hit the Reseed button to drop a random value into the seed. You may need this control where several Custom Vertex 3D nodes must each yield different random results. Number Controls Eight sets of Number controls exist, matching the eight sliders over in the Numbers tab. Untick the Show Number checkbox to hide the matching Number slider, or change its name through the Name for Number text field.

### Point Controls

Eight sets of Point controls exist, matching the eight controls over in the Points tab. Untick the Show Point checkbox to hide the matching Point control along with its crosshair in the viewer. In the same way, change the control's name through the Name for Point text field.

### Custom Vertex 3D node Config tab

### Common Controls

Settings Tab The Settings tab's controls are shared by many 3D nodes, and you'll find their descriptions in the "The Common Controls" section at the close of this chapter.

### Displace 3D [3Di]

### The Displace 3D node

### Displace 3D Node Introduction

Working from a reference image, the Displace 3D node pushes an object's vertices along their normals. Where to sample the image is worked out from the geometry's texture coordinates. Bear in mind while using Displace 3D that it shifts only existing vertices and won't subdivide surfaces to add detail. For a finer displacement, raise the subdivision amount on the geometry being displaced. Note too that the displacement image's pixels may hold negative values. TIP: Running a particle system through a Displace 3D node turns off the Always Face Camera option set in the pEmitter. Particles aren't handled as point-like objects; all four of a particle's vertices get displaced on their own, which may or may not be what you're after.

### Inputs

The two inputs below appear on the Displace 3D node within the Node Editor: SceneInput: For the Displace 3D node the orange scene input is the required one. Through it you connect another node that builds or holds a 3D scene or object. Input: A 2D image used to displace the object wired into the Scene input connects through this green input. Supply no image and the node essentially hands the scene through untouched to its output. So while it isn't strictly a required input, there's little point in adding this node unless you wire this input up correctly.

### Basic Node Setup

A Displace 3D node's output usually feeds a Merge 3D node, folding it into a bigger scene. The 3D geometry you want displaced wires into the orange input, and in this example a Fast Noise node does the displacing. A Fast Noise node doing the displacing of an image sitting on an Image Plane 3D Inspector

### Displace 3D controls

### Controls Tab

Two tabs run along the top of the Displace 3D Inspector. The main one, the Controls tab, holds the dedicated Displace 3D controls.

Channel Sets which channel of the connected input image drives the geometry's displacement. Scale and Bias With these sliders you scale (magnify) and bias (offset) the displacement. Bias gets applied first, scale after.

### Camera Displacement

- Point to Camera: Tick the Point to Camera checkbox and each vertex shifts toward the camera in place of along its normal. One use for this option is displacing a camera's image plane. Viewed through the camera, the displaced camera image plane looks unchanged, yet it's deformed in 3D space, which lets you comp in other 3D layers that interact correctly in Z.
- Camera: With the Point to Camera option on, this menu picks which camera in the scene sets the camera displacement.

### Common Controls

Settings Tab The Settings tab's controls are shared by many 3D nodes, and their descriptions live in the "The Common Controls" section at the close of this chapter.

### Duplicate 3D [3Dp]

### The Duplicate 3D node

### Duplicate 3D Node Introduction

Much like the 2D version known as the Duplicate node, the Duplicate 3D node can copy any geometry in a scene, applying a running transformation to each, to build repeating patterns and intricate arrays of objects. The Jitter tab's options permit non-uniform transformations, things like random positioning or sizes.
