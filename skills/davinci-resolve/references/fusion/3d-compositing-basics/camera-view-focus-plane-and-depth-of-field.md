# Quickly viewing a scene through a camera and plane of focus and depth of field

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](transformations-and-transform-tab-of-a-merge3d-node.md) / [Next section](lighting-hierarchies-and-shadow-maps.md)
<a id="source-ambient-light"></a> <a id="source-cotrolling-lighting-within-each-3d-object"></a> <a id="source-directional-light"></a> <a id="source-enabling-lighting-in-the-viewer"></a> <a id="source-enabling-lighting-to-be-rendered"></a> <a id="source-importing-cameras"></a> <a id="source-lighting-and-shadows"></a> <a id="source-lighting-types-explained"></a> <a id="source-plane-of-focus-and-depth-of-field"></a> <a id="source-point-light"></a> <a id="source-quickly-viewing-a-scene-through-a-camera"></a> <a id="source-spotlight"></a> <a id="source-the-lighting-button-under-the-viewer"></a> <a id="source-the-select-camera-dialog"></a>

### Quickly Viewing a Scene Through a Camera

Once a camera is in a scene, viewing it "through the camera" takes only a quick setup. To look at the scene through the camera: 1 Select the Merge3D node the camera is wired to, or any node downstream of that Merge3D. 2 Load the chosen Merge3D or downstream node into a viewer. 3 Right-click the axis label in the viewer's bottom corner and pick the camera name. Since the viewer's frame can differ from the camera frame, it may not line up with the true bounds of the image the Renderer3D node will render. When your scene has no Renderer3D node yet, you can fall back on Guides that stand in for the camera's framing. To read more about Guides, consult Chapter 69, "Using Viewers." within the DaVinci Resolve Reference Manual, or Chapter 7 of the Fusion Reference Manual.

### Plane of Focus and Depth of Field

Cameras carry a plane of focus, for whenever depth of field rendering is on hand. Here is how to switch on depth of field rendering in your scenes. To render depth of field within a 3D scene: 1 You have to add a Renderer3D node at the tail of your 3D scene. 2 With the Renderer3D node selected, choose OpenGL Renderer for the Renderer Type. 3 Open the Accumulation Effects disclosure control that shows up, then tick the Enable Accumulation Effects checkbox in the OpenGL render.

Turning on Enable Accumulation Effects enables additional depth of field controls Switching on "Enable Accumulation Effects" brings up a Depth of Field checkbox plus Quality and Amount of DoF Blur sliders for tuning the depth of field effect. These controls touch only the perceived quality of the rendered depth of field. The depth of field actually produced rests entirely on the camera's setup and its position relative to the other 3D objects in your scene. Selecting your scene's Camera3D node to view its controls in the Inspector adds a new Focal Plane checkbox to the Control Visibility group. Switching it on reveals the green focal plane indicator in the 3D Viewer, helping you picture what the Focal Plane slider does; that slider sits in the top group of parameters on the Camera3D node's Controls tab.

Turning on the Focal Plane checkbox in the Camera3D node To read more about these particular camera controls, consult Chapter 89, "3D Nodes," within the DaVinci Resolve Reference Manual, or Chapter 29 of the Fusion Reference Manual.

### Importing Cameras

To match cameras across applications, you can bring in camera paths and positions from many popular 3D applications. Fusion can import animation splines from Maya and XSI straight away in their own native spline formats. Animation on cameras from 3ds Max and LightWave gets sampled and keyframed on every frame. To import a camera out of another application, do this: 1 Select the camera within the Node Editor. 2 Down at the Inspector's bottom, click the Import Camera button. 3 Using the file browser, locate and select the scene holding the camera you wish to import. A dialog box presenting several options shows up. With the Force Sampling checkbox on, Fusion samples each frame of the motion no matter the format.

### The Select Camera dialog

TIP: For parented or rigged cameras, baking the camera animation inside the 3D application before bringing it into Fusion tends to give more dependable results.

### Lighting and Shadows

Light sources can be dropped into a scene to build richly detailed lighting environments and atmosphere. Four kinds of lights are available in 3D scenes: ambient, directional, point, and spotlights.

### Enabling Lighting in the Viewer

A scene with no lights runs on a default directional light, but that vanishes on its own the moment you add a 3D light object. Yet even after light objects join your scene, lighting and shadows stay invisible in the viewer until you first switch on lighting through the viewer contextual menu, right-clicking anywhere inside a viewer and choosing 3D Options > Lighting or Shadows to enable one or the other or both.

### Enabling Lighting to Be Rendered

The Renderer3D node renders no lighting effects until the Enable Lighting and/or Shadows checkboxes are ticked in the Inspector.

### The Lighting button under the viewer

NOTE: Whenever lighting is off in the viewer or in final renders, the image looks as though a 100% ambient light is illuminating it.

### Cotrolling Lighting within Each 3D Object

Every node that builds or merges geometry also carries lighting options for setting how each object responds to light:

- Merge3D nodes carry a Pass Through Lights checkbox that decides whether lights tied to an upstream Merge3D node also light up objects tied to downstream Merge3D nodes.
- ImagePlane3D, Cube3D, Shape3D, Text3D, and FBXMesh3D nodes carry a set of Lighting controls letting you toggle three controls: Affected by Lights, Shadow Caster, and Shadow Receiver.

Each 3D object carries its own lighting controls for steering how it reacts to light and shadows

### Lighting Types Explained

Below is a fuller account of each light type in Fusion.

### Ambient Light

Ambient light serves to establish a baseline light level for the scene, since it spreads a generally even illumination across it. Present everywhere yet seeming to issue from no particular source, ambient light casts no shadows and tends to fill in a scene's shadowed regions.

### Directional Light

A directional light consists of parallel rays that illuminate the whole scene from a single direction, forming a wall of light. The sun makes a fine example of a directional light source.

### Point Light

A point light is a sharply defined light with a small, distinct source, much like a light bulb, that radiates from that point in every direction.

### Spotlight

A spotlight is a more advanced point light that casts a sharply defined cone of light with falloff. It is the sole light that yields shadows.

From left to right: Directional light, point light, and spotlight Every Light node shows onscreen controls in the viewer, though not all controls bear on every light type. For the ambient light, position changes nothing. The directional light can be rotated, but its position and scale are disregarded. The point light disregards rotation. The spotlight responds to both position and rotation.
