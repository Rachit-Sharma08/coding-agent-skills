# Catcher and cubemap and falloff

Version: DaVinci Resolve 20.3 Reference Manual. Context: Catcher, Cubemap, Falloff.
[Chapter index](INDEX.md) / [Previous section](bump-map-and-catcher.md) / [Next section](falloff-and-fast-noise-texture-and-gradient-3d.md) / [Catcher 3Ca](bump-map-and-catcher.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-catcher-controls"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-cube-map-controls"></a> <a id="source-cube-map-node-overview"></a> <a id="source-cubemap-3cu"></a> <a id="source-falloff-3fa"></a> <a id="source-falloff-example"></a> <a id="source-falloff-node-overview"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-1"></a> <a id="source-sample-cube-map"></a> <a id="source-the-cube-map-node"></a> <a id="source-the-falloff-node"></a>

### Catcher controls

### Controls Tab

The Options on the Controls tab govern how the Catcher gathers up multiple projections. Enable Tick this checkbox to enable or disable the node. It differs from the red switch in the upper-left corner of the Inspector. That red switch shuts off the tool entirely and passes the image along untouched. The Enable checkbox is confined to the effect portion of the tool. Other portions, such as scripts in the Settings tab, keep processing as usual. Color Mode The Color mode menu governs how the Catcher blends the light from multiple projectors. It has no bearing on the outcome when just one projector is in the scene. The control is meant for the Renderer 3D node's software renderer and does nothing once the OpenGL renderer is in use.

Alpha Mode The Alpha mode governs how the Catcher blends the Alpha channels from multiple projectors. It has no bearing on the outcome when just one projector is in the scene. This setting targets the Renderer 3D node's software renderer and stays inert whenever the OpenGL renderer handles the job. Threshold The Threshold can leave certain low values out of the accumulation calculation. For instance, in the Median Accumulation mode, a threshold of 0.01 would drop any pixel valued below 0.01 from the median calculation. Restrict by Projector ID When on, the Catcher accepts light solely from projectors whose ID matches. Projectors carrying a different ID are passed over. Material ID This slider fixes the numeric identifier handed to this material. The value is rendered into the MatID auxiliary channel if the matching option is switched on in the Renderer 3D node.

### Common Controls

Settings Tab The Inspector’s Settings tab repeats across the other 3D nodes. A thorough rundown of these common controls waits at the chapter’s close in the “The Common Controls” section.

### CubeMap [3Cu]

### The Cube Map node

### Cube Map Node Overview

The Cube Map node builds texture maps from separate images, one for each face of the cube. It can equally pull the individual cube faces out of a single image holding an unfolded cube in the Vertical or Horizontal Cross layouts. You produce a cube map by mounting six cameras at 90 degrees angle of views, pointing up, down, left, right, front, and back. The node hands you options for setting the reference coordinate system and rotation of the resulting texture map. The Cube Map node typically serves to make environment maps for distant regions (skies or horizons, say) or reflection and refraction maps.

### Sample cube map

### Inputs

This node's Inputs change with how the Layout menu is set in the Inspector. One input covers a 2D image for the entire cube, while six inputs can each accept a separate 2D image per cube side. CrossImage: The orange Cross Image input is on view by default, or any time the Inspector's Layout menu shows Vertical Cross or Horizontal Cross. That input accepts a 2D image. CubeMap.[DIRECTION]: These six multi-colored inputs surface solely when the Inspector's Layout menu reads Separate Images. Every input accepts an image lined up with the left, right, top, bottom, front, and back faces.

### Basic Node Setup

The Cube Map node draws on a vertical or horizontal cross image, here represented by the MediaIn2 node wired into the orange cross image input. You use the Cube Map node much as you'd use the Sphere Map node. It builds an environment that wraps around the geometry connected to a Shader node.

A Cube Map node fed a cross image input, which builds an environment for the Shape 3D

### Inspector

### Cube Map controls

### Controls Tab

Layout The Layout menu sets the type and count of inputs for the cube map texture. The valid options are:

- Separate Images: Choosing this puts six inputs on the node, one per cube face. Should the separate images be non-square or of unequal size, they're rescaled into the biggest 1:1 image able to hold them all.
- Vertical Cross: Choosing this puts a single input on the node. The image ought to be a cube's unwrapped texture with every face laid out in a Vertical Cross arrangement, the height exceeding the width. Where the cross image's aspect isn't 3:4, the CubeMap node trims it down to fit the applicable aspect ratio.
- Horizontal Cross: Choosing this puts a single input on the node. The image ought to be a cube's unwrapped texture with every face laid out in a Horizontal Cross arrangement, the width exceeding the height. Where the cross image's aspect isn't 4:3, the CubeMap node trims it down to fit the applicable aspect ratio.

Coordinate System The coordinate system menu fixes the position values used as the image is turned into a texture.

- Model: Picks this to orient the texture along the object local coordinate system.
- World: Picks this to orient the resulting texture by the global or world coordinate system.
- Eye: Picks this to line the texture map up with the camera or viewer's coordinate system.

Rotation The rotation controls split into buttons selecting the order in which rotation runs along each axis of the texture. As an example, XYZ would apply rotation to the X axis first, next the Y axis, and finally the Z axis. The rotation controls' other half are dials that spin the texture around its pivot point. Warn About Bad Dimensions Ticking this checkbox throws a warning message onto the console when the dimensions of the supplied image fall short of the requirements for the chosen orientation mode. Material ID This slider fixes the numeric identifier handed to this material. The value is rendered into the MatID auxiliary channel if the matching option is switched on in the renderer.

### Common Controls

Settings Tab The same Settings tab in the Inspector shows up on the other 3D nodes. These common controls get their full explanation at the end of the chapter, under the “The Common Controls” section.

### Falloff [3Fa]

### The Falloff node

### Falloff Node Overview

The Falloff node blends two materials or textures according to the incidence angle between the camera and the object the material sits on. It comes in handy when you'd like one material for the portions of geometry that bounce light straight back at the camera and a different material for the portions that send light back into the scene.

### Falloff example

### Inputs

The Falloff node's two Inputs serve to connect two images or materials. One reflects back toward the camera, while the other reflects away from the camera into the scene. Face On Material: The orange Face On material input takes a 2D image or a 3D material. Supply a 2D image and it becomes a diffuse texture map by way of the basic material shader. This input handles the material reflecting straight back to the camera Glancing Material: The green Glancing material input takes a 2D image or a 3D material. Supply a 2D image and it becomes a diffuse texture map by way of the basic material shader. This input handles the material reflecting away from the camera into the scene. While this node's inputs can be images, its output is always a material.

### Basic Node Setup

The Falloff node below governs the strength of the Blinn material and the Reflect material. Connect the Falloff node's Face On input to whatever material should appear on the object's camera-facing sides, and connect the Glance input to whatever material should appear on the sides that don't face the camera head-on. So the Falloff node uses one input for the camera-facing material and another for the material turned away from the camera.
