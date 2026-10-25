# Fog 3D and image plane 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fog 3D, Image plane 3D.
[Chapter index](INDEX.md) / [Previous section](fbx-exporter-3d-and-fbx-mesh-3d-and-fog-3d.md) / [Next section](locator-3d-locator-3d-node-introduction.md) / [Fog 3D 3Fo](fbx-exporter-3d-and-fbx-mesh-3d-and-fog-3d.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-4"></a> <a id="source-common-controls-5"></a> <a id="source-controls-tab-3"></a> <a id="source-controls-tab-4"></a> <a id="source-fog-node-controls"></a> <a id="source-image-plane-3d-3im"></a> <a id="source-image-plane-3d-controls"></a> <a id="source-image-plane-3d-node-introduction"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-radial-vs-perpendicular-fog-effect"></a> <a id="source-the-image-plane-3d-node"></a>

### Inputs

Within the Node Editor the Fog 3D node carries two inputs, though just one is required for the Fog 3D to cast itself over a 3D scene. SceneInput: Feeding this required orange-colored input is the output of a 3D scene that the fog gets "projected" onto. DensityTexture: A 2D image is what this optional green-colored input takes. Whatever fog color the node creates gets multiplied by the pixels of that image. While preparing the density texture's image, keep in mind that, in effect, the camera projects that texture onto the scene.

### Basic Node Setup

The Fog 3D node goes after the Merge 3D node that holds the scene. View the Fog node and you'll see fog laid over the 3D scene's objects according to where each one sits along Z.

A Fog 3D node placed after the Merge 3D scene

### Inspector

### Fog node controls

### Controls Tab

The Controls tab brings together every parameter you'd use to govern the Fog's appearance and how it casts over the scene's geometry. Enable This checkbox lets you switch parts of the node's processing on or off. It's not the same as the red switch at the upper-left corner of the inspector. The red switch shuts the tool off entirely and passes the image through untouched. The Enable checkbox is confined to the tool's effect portion. Other parts such as scripts in the Settings tab still process as usual. Show Fog in View By default, the fog this node creates shows up only when the scene is viewed through a camera node. Turn this checkbox on, and the fog becomes visible in the scene from every point of view. Color This control serves to set the fog's color. That color is also multiplied by the density texture image, where one is wired into the node's green input. Radial By default, the fog forms from the perpendicular distance to a plane (parallel with the near plane) running through the eye point. With the Radial option checked, the radial distance to the eye point is used in its place. The trouble with perpendicular distance fog is that as you move the camera around, objects on the left or right side of the frustum grow less fogged as they drift toward the center, even though they stay the same distance from the eye. Radial fog corrects this. Radial fog isn't always what you want, however.

For instance, while fogging an object near the camera, such as an image plane, the image plane's center could come out unfogged while its edges are fully fogged.

### Radial vs. Perpendicular fog effect

Type This control serves to set the kind of falloff given to the fog.

- Linear: Sets a linear falloff for the fog.
- Exp: Produces an exponential nonlinear falloff.
- Exp2: Produces a stronger exponential falloff.

Near/Far Fog Distance Expressed as units of distance out from the camera, this control gives the fog's range across the scene. The Near Distance sets where the fog begins, while the Far Distance marks the point where the fog reaches its full effect. Fog accumulates, so the farther an object sits from the camera, the thicker the fog ought to look.

### Common Controls

Settings Tab The controls on the Settings tab are shared by many 3D nodes, and you'll find their descriptions in "The Common Controls" section at the close of this chapter.

### Image Plane 3D [3Im]

### The Image Plane 3D node

### Image Plane 3D Node Introduction

The Image Plane node makes 2D planar geometry inside 3D space. It's most often used to stand in for 2D images on "cards" within the 3D space. The image plane's aspect comes from the aspect of the image wired to the material input. If you don't want the image's aspect ratio reshaping the "card" geometry, reach for a Shape 3D node instead.

### Inputs

Between this node's two inputs, the material input is the primary connection for laying an image over the planar geometry the node produces. SceneInput: A 3D scene is what this orange input expects. Because the node turns out flat, planar geometry, that input isn't required. MaterialInput: This green-colored material input accepts a 2D image or a 3D material. From whatever source feeds it (in Fusion Studio a Loader node, or in DaVinci Resolve a MediaIn node), it draws the rectangle's texture and aspect ratio. Where a 2D image is supplied, it serves as a diffuse texture map feeding the Inspector's basic material tab. Wire in a 3D material rather than an image, and that basic material tab switches off.

### Basic Node Setup

Chiefly, the Image Plane 3D node carries a video clip into a 3D composite. The MediaIn or Loader node feeds the Image Plane 3D node, which in turn feeds a Merge 3D node. View that Merge 3D node and you'll see every Image Plane 3D node, plus whatever other elements are wired to it.

Multiple Image Plane 3D nodes connected to a Merge 3D

### Inspector

### Image Plane 3D controls

### Controls Tab

Common controls fill most of the Controls tab. Sitting at the top of the Inspector, the Image Plane specific controls permit only minor tweaks. Lock Width/Height With this checked, the plane's subdivision goes on evenly in X and in Y. Unchecked, it gives you a pair of sliders for governing the X and Y subdivisions separately. The default here is on. Subdivision Level The Subdivision Level slider determines the count of subdivisions used while the image plane is built. Where the Open GL viewer and renderer run Vertex lighting, a mesh with more subdivisions offers more vertices for carrying the lighting. High subdivisions can therefore help while you work interactively with lights. Wireframe Turning on this checkbox makes the mesh render only the object's wireframe when the OpenGL renderer is in use.

### Common Controls

Controls, Materials, Transform, and Settings Tabs Plenty of 3D nodes hold the same remaining controls—Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID—and likewise the Materials, Transform, and Settings tabs. You'll find their descriptions in "The Common Controls" section at the close of this chapter.
