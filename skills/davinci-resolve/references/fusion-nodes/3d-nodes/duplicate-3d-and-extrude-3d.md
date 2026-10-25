# Duplicate 3D and extrude 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Duplicate 3D, Extrude 3D.
[Chapter index](INDEX.md) / [Previous section](duplicate-3d-transform-method.md) / [Next section](fbx-exporter-3d-and-fbx-mesh-3d-and-fog-3d.md) / [Duplicate 3D 3Dp](custom-vertex-3d-and-displace-3d-and-duplicate-3d.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-duplicate-3d-jitter-tab"></a> <a id="source-duplicate-3d-region-tab"></a> <a id="source-extrude-3d-3ex"></a> <a id="source-extrude-3d-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-jitter-tab"></a> <a id="source-region-tab"></a> <a id="source-the-extrude-3d-node"></a> <a id="source-the-extrude3d-controls-tab"></a>

### Jitter Tab

The controls on the Jitter tab let you randomize the position, rotation, and size of every copy generated over on the Controls tab.

### Duplicate 3D Jitter tab

Random Seed The Random Seed slider serves to produce a random starting point for the quantity of jitter given to the duplicated objects. Two Duplicate nodes carrying identical settings but distinct random seeds yield two entirely different outcomes. Randomize Press the Randomize button to auto generate a random seed value. Jitter Probability Moving this slider sets the proportion of copies the jitter touches. Setting it to 1.0 affects 100% of the copies, whereas 0.5 affects only half of them.

Time Offset Use the Time Offset slider to shift any animations applied to the source geometry by a fixed amount for each copy. As an example, set the value to –1.0 and feed in a cube animated to spin on the Y-axis as the source. The first copy displays the animation as it was a frame earlier; the second copy displays animation from a frame before that, and so on. Applied to textured planes, this can be highly effective—say, where each copy can present successive frames of a clip. Translation Jitter Across the duplicated objects, this trio of controls tunes how much the X, Y, and Z translation varies. Rotation Jitter For the duplicated objects, this trio of controls tunes how much the X, Y, and Z rotation varies. Pivot Jitter Among the duplicated objects, this trio of controls tunes how much the rotational pivot center varies. Only the extra jitter rotation is touched here, never the rotation the Rotation settings on the Controls tab produce. Scale Jitter For the duplicated objects, this control tunes how much the scale varies. Switch off the Lock XYZ checkbox to vary the scale independently across all three axes.

### Region Tab

The controls on the Region tab let you mark out an area in the viewer where copies are allowed to show up or are kept from showing up. As with most Fusion parameters, this area can be animated so the copied object pops on and off the screen according to the region's shape and setting.

### Duplicate 3D Region tab

Region Tab The Region section holds two settings governing the region's shape and the effect the region has on the duplicate objects.

- Region Mode: The Region Mode menu offers three options. The default, labeled "Ignore region," skips the node altogether and leaves the copies of objects exactly as set on the Controls and Jitter tabs. The menu entry labeled "When inside region" makes the copied objects show up only while their position lands inside the region this tab defines. The final menu entry, "When not Inside region," makes the copied objects show up only while their position lands outside the region this tab defines.
- Region: The Region menu fixes the region's shape. Among the five options are the cube, sphere, and rectangle primitive shapes. The mesh option lets you wire a 3D model into the node's green mesh input. That green input shows up only once the Region menu is set to Mesh. The All setting points to the whole scene. This lets the copies pop on and off when the Region mode is animated. Once the Region menu is set to Mesh, four more options become visible. They are covered below.

Winding Rule: Drawing on four common techniques, the Winding Rule menu decides how the mesh of polygons is read as an area of volume and, in turn, how copies find the vertices in the mesh. Intricate overlapping regions of a mesh may produce an irregular fit. Switching to a different technique from this menu can occasionally yield a closer match between the mesh and how the copies read the mesh shape. Winding Ray Direction: A 3D model consists of a mesh of vertices built from flat polygons. As this becomes a volume for a region, the Winding Ray Direction decides the alignment direction for each polygon's volume (like depth extrude). Limit by Object ID: With a scene that holds multiple meshes wired into the node's green Mesh input, all of those meshes act as the region. Turning on this checkbox lets you use the Object ID slider to pick the ID for the mesh you want as the Region. Object ID: While the Limit by Object ID checkbox is on, this slider picks the number ID of the mesh object you want for the Region.

### Common Controls

Settings Tab The controls on the Settings tab are shared by many 3D nodes, and you'll find their descriptions in "The Common Controls" section at the close of this chapter.

### Extrude 3D [3Ex]

### The Extrude 3D node

### Extrude 3D Node Introduction

The Extrude3D tool works on Fusion's shape tools, taking flat shapes and turning them into dynamic, three-dimensional objects by way of controlled extrusion, driving the shape's edges out into the Z-axis. Extra beveling can be added for polished edges and chamfers.

### Inputs

This node carries three inputs: a shape connection plus two material connections. BevelMaterialInput: This pink-colored material input accepts a 2D image or, alternatively, a 3D material. From whichever source feeds it (in Fusion Studio a Loader node, or in DaVinci Resolve a MediaIn node), it draws the bevel's texture. Where a 2D image is supplied, it serves as a diffuse texture map feeding the Inspector's Basic Material tab. Wire in a 3D material rather than an image, and that Basic Material tab switches off. ShapeInput: A Shape node is what this yellow input expects—namely the 2D shape destined to be beveled and extruded into 3D space. MaterialInput: This green-colored material input accepts a 2D image or, alternatively, a 3D material. From whichever source feeds it (in Fusion Studio a Loader node, or in DaVinci Resolve a MediaIn node), it draws the shape's texture. Where a 2D image is supplied, it serves as a diffuse texture map feeding the Inspector's Basic Material tab. Wire in a 3D material rather than an image, and that Basic Material tab switches off.

### Basic Node Setup

The Extrude 3D node mainly serves to build a 3D shape out of a 2D shape. The Shape Node node feeds into the Extrude 3D node, which in turn feeds a Merge 3D node. View that Merge 3D node and you'll see the Extrude 3D node along with whatever other elements are wired to it.

Wiring a simple sRectangle Shape node into an Extrude 3D node carries the rectangle over into 3D space.

A simple sRectangle extruded into 3D space and beveled

### Inspector

### The Extrude3D Controls tab

### Controls Tab

The Controls tab serves to define the polygon characteristics, among them extrusion depth and beveling. Extrusion Style Two choices exist: Classic and Custom. Classic produces a standard uniform extrusion, whereas Custom reveals an Extrusion Profile graph where you can add points and manipulate them to build one-off custom extrusions, such as picture frames and knurled buttons. Extrusion Depth This slider fixes the extruded width of the polygon. Extrusion Subdivisions This slider fixes how many subdivisions fall within the smoothed parts of the extrusion profile. Bevel Depth Raise the Bevel Depth slider's value past zero to put a bevel on the polygon. Bevel Width This slider determines how wide the polygon's bevel runs. Smoothing Angle With this control you adjust the smoothing angle that the bevel's edges receive. Bevel Front/Back These checkboxes let you turn on beveling for the front and back faces of the polygon separately.

### Common Controls

Materials, Transform, and Settings Tabs Within the Inspector, the Materials tab along with the Transforms tab and the Settings tab show up on other 3D nodes too. These common controls get a full description at this chapter's close in "The Common Controls" section.
