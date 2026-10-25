# Ucamera universal scene descriptor USD files

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ucamera.
[Chapter index](INDEX.md) / [Next section](ucamera-and-uduplicate.md)
<a id="source-a-very-simple-usd-import-node-tree"></a> <a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-film-back"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-the-prim-selection-pick-button"></a> <a id="source-the-ucamera-controls-tab"></a> <a id="source-the-uloader-node"></a> <a id="source-the-usd-loader"></a> <a id="source-ucamera-uca"></a> <a id="source-universal-scene-descriptor-usd-files"></a> <a id="source-usd-nodes"></a> <a id="source-usd-nodes-part-1"></a> <a id="source-usd-scene-tree-dialog-for-object-selection-in-usd-files"></a>

### USD Nodes

This section walks through the Universal Scene Descriptor (USD) nodes that ship inside Fusion.

You can type the short code printed alongside each node name into the Select Tool dialog while hunting for a tool, and those same codes turn up in scripting references too. Within this text, whenever a node tree pictures MediaIn nodes in DaVinci Resolve, treat them as equivalent to Loader nodes in Fusion Studio, except where a difference is explicitly called out.

### Universal Scene Descriptor (USD) Files

The Universal Scene Descriptor USD framework is a collection of open standards for laying out, assembling, and simulating a 3D environment. Rather than being merely a basic container, the USD file format is an open source 3D scene description meant for authoring and exchanging 3D content between many different applications. Both DaVinci Resolve and Fusion are able to read USD (.usdc, .usdz, and .usda) 3D data, covering geometry, lighting, cameras, materials, and animation. Fusion now includes a fresh set of USD tools that let you reshape, re-light, and render these USD files.

### The USD Loader

With the uLoader you can bring USD files in and tweak their options.

### The uLoader node

To Import a USD file: 1 Drop a uLoader tool into your Fusion Composition. 2 Pick the USD file you intend to bring in using the File Browser. Should you need to swap that file later on, you can do it from the uLoader Inspector without breaking your node tree. 3 Wire the output of the uLoader into a uMerge tool. 4 Attach whatever other USD tools you need, such as uCamera or any of the uLights, to work on the scene. 5 Route the output of the uMerge tool to a uRenderer. 6 Send the output of the uRenderer along to the MediaOut tool.

### A very simple USD import node tree

### USD Scene Tree Dialog for Object Selection in USD Files

Acting as an easy-to-read visual hierarchy, the Scene Tree window depicts USD scenes. From it you can pick out and edit single elements within a USD scene. The USD Scene Tree matters for targeted effects driven by the uVisibility, uVariant, uReplace Material, and uTransform nodes, and it also serves to override imported scene objects within uCamera and the assorted USD light tools. You bring up the USD Scene Tree by clicking the Pick button inside the Prim Selection box on certain USD tools.

### The Prim Selection Pick button

The tree lays out the USD hierarchy, while the type column tells you which sort of asset each entry is. You can pick, filter, isolate, and single out particular elements within a USD scene so you can concentrate on logical components and apply precise adjustments. Hold Command to toggle-select several objects at once, and use Shift to grab a range of objects with one click.

The USD Scene Tree dialog

### uCamera [uCa]

The USD Camera Node uCamera Node Introduction The uCamera node builds a virtual camera so you can look at the USD scene inside its 3D environment. It mirrors the controls found on actual cameras closely, which makes lining up live-action or 3D-rendered elements as smooth as it can be. Placing cameras into a 3D composite lets you frame the elements of that composite however you like and animate the camera across a scene to produce moving camera shots.

### Inputs

A single yellow Scene Input is provided for hooking up a USD scene. From there you can fine-tune whatever cameras already live inside the scene.

### Basic Node Setup

You should wire the output of a uCamera node into a uMerge node so it becomes part of a USD 3D scene alongside other assets and nodes.

Hooking the uCamera node up to a uMerge node hands standard camera controls over to a USD scene. If you show a uCamera node on its own in the viewer, you see nothing but an empty scene, because the camera has nothing to look at. To watch the scene through the camera, display the uMerge node that the uCamera feeds into, or any node positioned downstream of that uMerge. Next, right-click within the viewer and pick uCamera > [Camera name] from the contextual menu. You can also right-click the axis label in the lower corner of each USD viewer to bring up the Camera submenu. Because the viewer aspect can differ from the camera aspect, the camera view might not line up exactly with the real edges of the image that the uRenderer node produces. Turning on guides marks out the slice of the view the camera captures and helps you frame the shot. Right-click within the viewer and pick an option under the Guides > Frame Aspect submenu. The default choice adopts the format set in the Composition > Frame Format preferences. To switch the guides on or off, choose Guides > Show Guides from the viewers’ contextual menu, or press the Command-G (macOS) or Ctrl-G (Windows) keyboard shortcut while the viewer is active.

### Inspector

### The uCamera Controls tab

### Controls Tab

The Controls tab holds several of the most essential camera settings, including its film back properties, focal length, and clipping plains. Override Selection Clicking the Pick button lets you pick out a camera that already exists in an attached USD file, so you can adjust the cameras within an imported scene. Projection Type Use the Projection Type menu to switch between Perspective and Orthographic cameras. As a rule, cameras in the real world are perspective cameras. An orthographic camera relies on parallel orthographic projection, an approach in which the view plane sits perpendicular to the viewing direction. The result is a parallel camera output free of perspective distortion. For orthographic cameras, the only controls shown are those for the near and far clipping planes plus one that sets the viewing scale. Near/Far Clip Clipping planes restrict which geometry in a scene gets rendered according to how far an object sits from the camera’s focal point. They make sure that objects sitting right up against the camera, along with objects so distant they serve no purpose, are left out of the final rendering. The default perspective camera disregards this setting unless you turn off the Adaptive Near/Far Clip checkbox sitting beneath the Near/Far Clip control. Because the clip values are expressed in units, a far clipping plane of 20 means anything farther than 20 units from the camera stays invisible to it. Likewise, a near clipping plane of 0.1 means anything nearer than 0.1 units is hidden as well. NOTE: Keeping a tighter span between the near and far clipping planes yields better precision across every depth calculation. Should a scene start rendering odd artifacts on far-off objects, try pushing the Near Clip plane farther out.

Exposure With this turned on, the renderer sets the camera’s Near/Far Clipping plane on its own to fit the bounds of the scene. Doing so supersedes whatever you entered in the Near and Far clip range controls covered earlier. Orthographic cameras cannot use this option. Focal Length On an actual lens, the focal length measures the gap from the lens’s center out to the film plane. A shorter focal length places the focal plane nearer the rear of the lens. Focal length is given in millimeters. The angle of view and the focal length controls tie directly together. A shorter focal length widens the angle of view, so adjusting either control updates the other automatically to stay in sync. You can express how angle of view relates to focal length with the formula angle = 2 \* arctan[aperture / 2 / focal_ length]. Plug in the vertical aperture size for the vertical angle of view, and the horizontal aperture size for the horizontal angle of view. Focal Distance Much like the focal point on a real camera, this setting sets how far the camera sits from an object and feeds into the depth-of-field calculation. F Stop This sets the aperture size of the synthetic lens; it has an impact on exposure and also factors into the depth-of-field calculation.

### Film Back

Here you can manage the technical parameters belonging to the part of the camera that isn’t the lens. Horizontal/Vertical Aperture The Horizontal Aperture Width and Vertical Aperture Height sliders govern the size of the camera’s aperture, which on a real camera is the part that admits light. On video and film cameras, the aperture refers to how wide the opening is that determines the exposed area of each frame, a measurement also known as sensor size. Lens Shift X/Y Gives you controls for manually shifting the camera lens in width and in height. Shutter Close/Open These set the moments at which the camera shutter opens and shuts; they bear on Exposure and Motion Blur. Stereo Role When the camera is stereo, this picks the center of role for the pair of cameras, choosing left, center, or right.
