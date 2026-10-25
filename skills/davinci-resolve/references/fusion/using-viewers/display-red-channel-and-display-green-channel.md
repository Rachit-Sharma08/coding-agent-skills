# Display red channel and display green channel

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](viewer-and-subview-types-and-magnifier.md) / [Next section](3d-viewer-lighting-shadows-and-transparency.md)
<a id="source-changing-cameras-in-a-3d-viewer"></a> <a id="source-changing-the-pov-of-a-3d-viewer"></a> <a id="source-copying-a-viewers-pov-to-a-camera"></a> <a id="source-display-alpha-channel"></a> <a id="source-display-blue-channel"></a> <a id="source-display-green-channel"></a> <a id="source-display-red-channel"></a> <a id="source-display-z-buffer-channel"></a> <a id="source-panning-scaling-and-rotating-a-3d-viewer"></a> <a id="source-pov-labels"></a> <a id="source-the-3d-viewer"></a> <a id="source-viewer"></a> <a id="source-viewing-auxiliary-channels"></a> <a id="source-viewing-multilayer-files-studio-version-only"></a> <a id="source-viewing-objects-via-wireframe"></a>

### Display red channel

G

### Display green channel

B

### Display blue channel

A

### Display alpha channel

Z

### Display Z-buffer channel

### Viewing Auxiliary Channels

Beyond the RGBA and Z channels they handle through keyboard shortcuts, the viewers can show other channels too. File formats like OpenEXR frequently carry auxiliary image data that opens up extra control and compositing options when you work with rendered 3D images. To pull auxiliary image data into a viewer, either click the arrow beside the RGB button on its right to open the drop-down menu, or right-click in the viewer and select an option from the contextual menu’s Channels submenu.

### Viewing Multilayer Files (Studio Version Only)

Fusion can deftly manage multilayer image workflows, supporting EXR, Stereoscopic 3D, and PSD assets. On the Fusion viewers you can view a list of layers and interact with the layers of each node through the Settings tab in the Inspector. Because this layer structure persists across the whole toolset, you can confine a tool to a single layer while the remaining layers pass through untouched.

### Viewer

With a multilayer file loaded, you can preview individual layers in the Viewer by choosing a layer from the dropdown list. A file lacking layer support offers only a ‘default’ entry in the drop-down menu.

Choosing only the Asteroids layer of a multilayer file for viewing, by way of the Viewer’s Layer drop-down

### The 3D Viewer

Assembling a composite in 3D space calls for something different than ordinary 2D compositing. Whenever a node from the 3D category — or certain particle systems — is selected, the scene is shown in a 3D Viewer. That 3D Viewer renders a representation of the composite inside a genuine GPU-accelerated 3D environment. For further detail on the 3D controls, consult Chapter 85, “3D Compositing Basics,” within the DaVinci Resolve Reference Manual, or Chapter 25 of the Fusion Reference Manual.

### Panning, Scaling, and Rotating a 3D Viewer

Navigation in the 3D Viewer largely mirrors how you navigate the 2D Viewer. The same controls handle panning and zooming even though you’re now moving through a 3D space. When you view a 3D scene, however, panning shifts the viewpoint and therefore the center point used for scaling and rotation as well. Pairing panning with rotation lets you take the viewpoint anywhere in the scene. One other minor difference is that a 3D scene has a lower scale limit. Keep zooming past that limit and the viewpoint instead moves forward (a “dolly”). The mouse wheel advances slowly, whereas the keyboard advances faster.

Crucially, the 3D Viewer hands you extra control to rotate the view across the scene’s three dimensions, so you can study your scene from many different angles while you work. Rotating within a 3D Viewer is done one of these ways:

- With the Option key held, drag to the left or right while using the middle mouse button.
- Keep both the middle and right mouse buttons pressed as you drag.

The rotation pivots around the middle of the view. TIP: You can apply these same rotation controls to the 3D Histogram subview as well.

### Viewing Objects via Wireframe

3D composites handle not only 2D images on image planes but also true geometry — such as that made by the Particle system, the Text 3D node, imported FBX meshes, and the basic primitives of the 3D toolset. A Wireframe view makes it easier to see through a mesh or to gauge the geometry’s density. Catching a change in an ImagePlane3D’s Subdivision level is much easier in wireframe than in the rendered image. To render 3D geometry as wireframe, do this: right-click the 3D Viewer and pick 3D Options > Wireframe off the contextual menu.

### Changing the POV of a 3D Viewer

Compositing a 3D scene frequently means viewing it from several angles to verify the position and animation are right. Although the 3D Viewer uses a perspective camera that lets you look at the 3D scene from any angle, you can also flip the 3D Viewer to a view from the scene’s front, top, left, or right side — together known as Orthographic views. And if your scene contains a camera or spotlight, you can point the viewer at the scene from that object’s vantage point. To switch the 3D viewpoints: right-click the viewer and select an entry from the contextual menu’s Camera submenu. Among the choices are Perspective, Front, Top, Left, and Right.

### Changing Cameras in a 3D Viewer

When the 3D scene holds one or more camera objects, they appear as choices in the contextual menu. Spotlights and other lights or objects within the scene are listed under the Other submenu. Selecting any of these objects makes the 3D Viewer jump to the scene as seen from that object’s vantage point. While you look “through“ an object and rotate, pan, or zoom, the viewer instead alters the rotation, position, and scale of that camera, light, or other object.

### Copying a Viewer’s POV to a Camera

Often you’ll set up your scene using the default perspective view and then wish that vantage point (POV) to become your main camera’s point of view. With the Copy PoV To command you can effortlessly position and orient a camera, light, or other object to match the viewer’s current vantage point. To transfer the viewer’s point of view onto a camera, follow these steps: 1 Dial in the vantage point you want on a 3D Viewer by zooming, panning, and rotating it. 2 Add a camera to your 3D scene. 3 Right-click anywhere inside the 3D Viewer and pick Camera > Copy PoV To > Camera3DNameOfCamera off the contextual menu. The Camera3D’s controls then take on the position and angle values from the viewer. TIP: Because the Copy PoV To command operates in the object’s own coordinate space, any transformations a downstream node applies are ignored.

### POV Labels

As you change the viewer’s POV, a text label in the viewer’s lower-left corner keeps you informed of which POV is showing. Right-clicking that label directly, or the axis control just above it, serves as a shortcut to the Camera submenu, letting you readily pick a different viewpoint.

The Viewpoint label and Axis control in a 3D Viewer
