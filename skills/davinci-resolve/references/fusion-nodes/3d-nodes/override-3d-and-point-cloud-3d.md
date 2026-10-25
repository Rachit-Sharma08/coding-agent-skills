# Override 3D and point cloud 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Override 3D, Point cloud 3D.
[Chapter index](INDEX.md) / [Previous section](locator-3d-and-merge-3d-and-override-3d.md) / [Next section](point-cloud-3d-and-projector-3d.md) / [Override 3D 3Ov](locator-3d-and-merge-3d-and-override-3d.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-inputs-3"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-onscreen-contextual-menu"></a> <a id="source-override-3d-connected-to-a-replace-material-node"></a> <a id="source-override-3d-controls"></a> <a id="source-point-cloud-3d-3pc"></a> <a id="source-point-cloud-3d-controls"></a> <a id="source-point-cloud-3d-node-introduction"></a> <a id="source-the-point-cloud-3d-contextual-menu-options"></a> <a id="source-the-pointcloud-3d-node"></a>

### Basic Node Setup

The Override 3D node often teams up with the Replace Material node to generate isolated passes. In the node tree below, for instance, a scene branches off to an Override node that switches off each node's Affected by Lights property, then runs into a Replace Material node that lays on a Falloff shader to yield a falloff pass of the scene.

### Override 3D connected to a Replace Material node

### Inspector

### Override 3D controls

### Controls Tab

How the controls on the Controls tab work is simple enough. You begin by choosing the option to override through the Do [Option] checkbox, which exposes a control for setting that option's own value. The individual options aren't documented here; for a full description of each, look to any geometry creation node covered in this chapter — the Image Plane, Cube, or Shape nodes among them. Do [Option] Switches on the override for this option. [Option] With the Do [Option] checkbox enabled, the control for the property itself appears. The new value then overrides the property's control values across all upstream objects.

### Common Controls

Settings Tabs Controls shared by most 3D nodes live on the Settings tab. You'll find each described within “The Common Controls” section that closes this chapter.

### Point Cloud 3D [3PC]

### The PointCloud 3D node

### Point Cloud 3D Node Introduction

Typically a Point Cloud amounts to a host of null objects spawned by 3D tracking or modeling software. Coming from 3D tracking software, the points usually stand for each of the patterns that were tracked to build the 3D camera path. Such point clouds help you pin down a ground plane and line up other 3D elements with the tracked image. The Point Cloud 3D node builds a point cloud either by importing a file out of a 3D tracking application or by generating one when you run the Camera Tracker node. NOTE: A null object is an unseen 3D object carrying every one of the same transform properties a visible 3D object has.

### Inputs

The Point Cloud carries just one input, meant for a 3D scene. SceneInput: This orange input takes a 3D scene.

### Basic Node Setup

You view and wire up the Point Cloud 3D node by way of a Merge 3D node, which folds it into the broader 3D scene.

Point Cloud 3D connected and viewed through a Merge 3D

### Inspector

### Point Cloud 3D controls

### Controls Tab

From the Controls tab you can pull the point cloud in from a file and govern how it looks in the viewer. Style The Style menu lets you show the point cloud either as cross hairs or as points in the viewer. Lock X/Y/Z Clear this checkbox to gain separate control over how long the X, Y, and Z arms of each point in the cloud are. Size X/Y/Z These sliders let you enlarge the onscreen crosshairs that stand in for each point. Density This slider sets the likelihood that a given point gets shown. At a value of 1, every point appears; at 0.2, only every fifth point shows. Color Reach for the standard Color control to tint the onscreen crosshair controls. Import Point Cloud Pressing the Import Point Cloud button opens a dialog for bringing a point cloud in from another application.

Among the formats it reads you'll find Alias's Maya, plus the 3DS Max ASCII Scene Export, alongside NewTek's LightWave and Softimage XSI's

.ma .ase .lws .xsi.

Make Renderable Sets whether the point cloud shows in the OpenGL viewer and in final renderings the OpenGL renderer produces. The software renderer doesn't yet support drawing visible crosshairs for this node. Unseen by Camera This checkbox surfaces once the Make Renderable option is on. Tick the Unseen by Cameras checkbox and the point cloud stays visible in the viewers but isn't rendered into the output image by the Renderer 3D node.

### Common Controls

Transform and Settings Tabs The Transform and Settings tabs that remain are shared by many 3D nodes; their write-ups appear in “The Common Controls” section closing out this chapter.

### Onscreen Contextual Menu

Often, one or more points within an imported point cloud get hand-assigned to follow the position of a particular feature. Such points generally bear names that set them apart from the cloud's other points. To check a point's present name, rest the mouse pointer right on top of it, and shortly a little tooltip surfaces showing the point's name. Selecting the Point Cloud 3D node tacks a submenu onto the viewer’s contextual menu carrying several options that make it easy to find, rename, and pull these points away from the rest of the point cloud.

### The Point Cloud 3D contextual menu options

These are the options the contextual menu offers: Find: Choosing this from the viewer contextual menu brings up a dialog for searching out and selecting a point by name, and every point matching the pattern gets selected. Rename: Rename any point by choosing Rename from the contextual menu. Enter the new name in the dialog that appears and press Return. The point then takes that name with a four-digit number appended. As an example, the Name window is window0000, so multiple points read window0000, window0001, and onward. A name has to be a valid Fusion identifier (meaning no spaces, and it can't begin with a number). Delete: Choosing this removes whatever points are currently selected. Publish: By default, a cloud point's precise position stays hidden. To reveal it, select the points and then pick the Publish option from this contextual menu. Doing so adds a coordinate control to the control panel for each published point, showing that point’s current location.
