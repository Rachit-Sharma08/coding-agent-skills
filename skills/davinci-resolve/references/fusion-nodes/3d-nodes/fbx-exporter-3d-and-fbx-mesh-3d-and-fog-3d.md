# Fbx exporter 3D and fbx mesh 3D and fog 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fbx exporter 3D, Fbx mesh 3D, Fog 3D.
[Chapter index](INDEX.md) / [Previous section](duplicate-3d-and-extrude-3d.md) / [Next section](fog-3d-and-image-plane-3d.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-fbx-exporter-3d-fbx"></a> <a id="source-fbx-exporter-controls"></a> <a id="source-fbx-exporter-node-introduction"></a> <a id="source-fbx-mesh-3d-controls"></a> <a id="source-fbx-mesh-3d-fbx"></a> <a id="source-fbx-mesh-3d-node-introduction"></a> <a id="source-fog-3d-3fo"></a> <a id="source-fog-3d-node-introduction"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-the-fbx-exporter-node"></a> <a id="source-the-fbx-mesh-node"></a> <a id="source-the-fog-3d-node"></a>

### FBX Exporter 3D [FBX]

### The FBX Exporter node

### FBX Exporter Node Introduction

The FBX Exporter node offers a way to export a Fusion 3D scene out to the FBX scene interchange format. Each Fusion node becomes a single object in the exported file. Objects, lights, and cameras carry the name of the node that produced them. You can set the node to export a single file covering the whole scene, or to write one frame per file. Within the Fusion Studio application, keep the Preferences > Global > General > Auto Clip Browse setting at Enabled (default)—or, over in DaVinci Resolve, keep the equivalent Fusion > Fusion Settings > General > Auto Clip Browse setting enabled—and then dropping this node into a composition pops open a file browser for picking where the file gets saved. Once you've configured the node, the FBX Exporter behaves much like a Saver node: pressing the Render button on the toolbar renders out the file. Past the FBX format itself, the node exports as well to these: the 3D Studio .3ds, Collada .dae, Autocad .dxf, and Alias .obj formats.

### Inputs

The FBX Exporter node carries a single orange input. Input: The output of the 3D scene you wish to export connects into the orange input on the FBX Exporter node.

### Basic Node Setup

What the FBX Exporter 3D node takes as input is any 3D scene you want to export. Below, the node sits as a separate branch off the Duplicate 3D node. Only the objects the Duplicate 3D node generates get exported.

An FBX Exporter 3D branched off from the Duplicate 3D node

### Inspector

### FBX Exporter controls

### Controls Tab

The Controls tab gathers all the parameters you'd use to determine how the FBX file is built and which scene elements get exported. Filename This Filename field serves to show the location and file the node outputs. Click the Browse button to bring up a file browser dialog and switch the location where the file is saved. Format This menu serves to set the output file's format. Not every feature of this node is supported across all file formats. The .obj format, for one, doesn't handle animation. Version The Version menu serves to pick the available versions for the chosen format. The menu's contents shift dynamically to mirror the available versions for that format. Where the selected format offers just one option, this menu stays hidden. For the FBX formats, a Default choice resolves to FBX2011. Frame Rate Whatever frame rate the FBX scene carries is set from this menu. Scale Units By This slider alters the working units in the exported FBX file. Changing it can streamline workflows where your destination 3D software runs a different scale. Geometry/Lights/Cameras These three checkboxes govern whether the node tries to export the named scene element. Deselecting Geometry and Lights while leaving Cameras selected, for example, would output only the cameras presently in the scene.

Render Range Turning on this checkbox writes the Render Range data into the export file so that the FBX scene's time range is known to other applications. Reduce Constant Keys Turning on this option automatically drops keyframes whenever the neighboring keyframes carry the same value. File Per Frame (No Animation) Turning on this option compels the node to export one file per frame, producing a sequence of numbered files. This switches off the export of animation. Turn on this checkbox to expose the Sequence Start Frame control, where you can set the sequence's first frame to a custom value. Sequence Start Frame Turning on this checkbox brings up a thumbwheel control where you assign a particular start frame to the numbering sequence that goes onto the rendered filenames. For instance, with Global Start set to 1 and frames 1–30 rendered, files are ordinarily numbered 0001–0030. Set the Sequence Start frame to 100, and the rendered output is numbered from 100–131 instead.

### Common Controls

Settings Tab The controls on the Settings tab are shared by many 3D nodes, and you'll find their descriptions in "The Common Controls" section at the close of this chapter.

### FBX Mesh 3D [FBX]

### The FBX Mesh node

### FBX Mesh 3D Node Introduction

The FBX Mesh 3D node serves to import polygonal geometry from scene files saved in the FilmBox (FBX) format. It can likewise import geometry out of OBJ, 3DS, DAE, and DXF scene files. This gives you a way to handle more elaborate geometry than Fusion's built-in primitives offer. As this node imports geometry, all the geometry in the FBX file is merged into one mesh carrying a single pivot and transformation. The FBX Mesh node disregards any animation applied to the geometry. As an alternative, in Fusion Studio the File > Import > FBX Scene menu, or in DaVinci Resolve the Fusion > Import > FBX Scene menu, can import an FBX scene. That option spawns individual nodes for each camera, light, and mesh in the file. It can also be used to preserve the objects' animation. Leave the Preferences > Global > General > Auto Clip Browse option in Fusion Studio (or, in DaVinci Resolve, the Fusion > Fusion Settings > General > Auto Clip Browse option) at Enabled (default), and then dropping this node into a composition pops open a file browser for choosing the file you wish to import.

### Inputs

SceneInput: This orange scene input is an optional hookup, there in case you want to fold additional 3D geometry nodes together with the FBX file you've imported. Material Input: Serving as the material input, the green input takes either a 2D image or a 3D material. Feed it a 2D image and that image becomes a diffuse texture map for the node's basic material tab. Connect a 3D material instead, and the basic material tab is disabled.

### Basic Node Setup

You can run the FBX Mesh 3D node on its own without anything else wired to it. Its output runs into a Merge 3D, so the FBX model becomes part of some larger scene. In the example below, the FBX Mesh 3D node also carries a chrome material connected to its material input.

### Inspector

An FBX Mesh 3D node with chrome material applied

### FBX Mesh 3D controls

### Controls Tab

Common controls take up most of the Controls tab. The FBX-specific controls present on this tab are mainly informational rather than adjustments.

Size The Size slider governs the size of the imported FBX geometry. FBX meshes tend to come in far larger than Fusion's default unit scale, so this control helps when you need to scale the imported geometry to suit the Fusion environment. FBX File This field shows the filename and file path of the FBX mesh currently loaded. Click the Browse button to open a file browser you can use to track down a new FBX file. The node's name notwithstanding, it can also load an assortment of other formats.

FBX ascii FBX 5.0 binary Autocad DXF 3D Studio 3Ds Alias OBJ Collada DAE

(_.fbx) (_.fbx) (_.dxf) (_.3ds) (_.obj) (_.dae)

Object Name This input displays the name of the mesh being imported from the FBX file. Leave this field blank, and the FBX geometry's contents come in as a single mesh. You can't edit this field; Fusion sets it when you use the File > Import > FBX Scene menu. Take Name FBX files may hold multiple instances of an animation, known as Takes. This field displays the name of the animation take to draw from the FBX file. Leave this field blank, and no animation gets imported. You can't edit this field; Fusion sets it when you use the File > Import > FBX Scene menu. Wireframe Turning on this checkbox makes the mesh render only the object's wireframe. Wireframe rendering is supported solely by the OpenGL renderer in the Renderer 3D node.

### Common Controls

Controls, Materials, Transform, and Settings Tabs The remaining Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID controls are ones that many 3D nodes share. So too are the Materials, Transform, and Settings tabs. You'll find their descriptions in "The Common Controls" section at the close of this chapter.

### Fog 3D [3Fo]

### The Fog 3D node

### Fog 3D Node Introduction

The Fog 3D node lays fog over the scene based on a depth cue. It's the 3D counterpart of the Fog node in the Deep Pixel category. Built to operate entirely in 3D space, it takes full advantage of anti-aliasing and depth of field effects while rendering. In essence, the Fog 3D node retextures the scene's geometry by applying a color correction tied to each object's distance from the camera. An optional density texture image can introduce variation into the correction.
