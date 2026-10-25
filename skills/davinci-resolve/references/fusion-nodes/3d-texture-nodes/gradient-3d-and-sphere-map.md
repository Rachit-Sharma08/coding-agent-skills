# Gradient 3D and sphere map

Version: DaVinci Resolve 20.3 Reference Manual. Context: Gradient 3D, Sphere map.
[Chapter index](INDEX.md) / [Previous section](falloff-and-fast-noise-texture-and-gradient-3d.md) / [Next section](sphere-map-basic-node-setup.md) / [Continue Sphere Map 3SpM / Basic Node Setup](sphere-map-basic-node-setup.md) / [Gradient 3D 3Gd](falloff-and-fast-noise-texture-and-gradient-3d.md)
<a id="source-common-controls-5"></a> <a id="source-controls-tab-5"></a> <a id="source-gradient-3d-controls"></a> <a id="source-gradient-3d-modes"></a> <a id="source-inputs-6"></a> <a id="source-inspector-4"></a> <a id="source-sphere-map-3spm"></a> <a id="source-sphere-map-node-overview"></a> <a id="source-the-spheremap-node"></a>

### Inspector

### Gradient 3D controls

### Controls Tab

The Controls tab for the Gradient node governs the pattern and colors that make up the gradient texture. Gradient Type Picks which type or pattern the gradient follows. Linear: A plain linear gradient. Reflect: Resting on the Linear mode, this gradient mirrors itself at the center of the textured range. Square: The gradient is applied with a square pattern. Cross: Much like the Reflect mode, though Cross draws on two axes to apply the gradient. Radial: The Radial mode applies the gradient with a circular pattern.

### Gradient 3D modes

Gradient Bar The Gradient control is a bar where you can add, modify, and remove the gradient's color stops. Every triangular color stop along the Gradient bar stands for one color in the gradient. Both the color and the point's position can be animated. On top of that, a From Image modifier can be laid on the gradient to evaluate it from an image.

Interpolation Space By default the gradient interpolates linearly from point to point in RGB color space. That can occasionally throw up unwanted colors. Choosing a different color space may give a better result. Scale Lets you size the gradient. Offset Lets you pan through the gradient. Repeat Sets how the gradient's left and right borders are handled. Once: As you shift the gradient with the Gradient Offset control, the border colors hold their values. Shifting the default gradient leftward yields a white border on the left, while shifting it rightward yields a black border on the right. Repeat: As you shift the gradient with the Gradient Offset control, the border colors wrap around. Shifting the default gradient leftward yields a sharp jump from white to black, while shifting it rightward yields a sharp jump from black to white. Ping Pong: As you shift the gradient with the Gradient Offset control, the border colors ping-pong back and forth. Shifting the default gradient leftward makes the edge fade from white back to black, while shifting it rightward makes the edge fade from black back to white.

From top to bottom, gradients in Once, Repeat, and Ping Pong respectively, with the gradient shifted leftward Sub Pixel Fixes the accuracy with which the gradient is built. Material ID This slider fixes the numeric identifier handed to this material. The value is rendered into the MatID auxiliary channel if the matching option is switched on in the renderer.

### Common Controls

Settings Tab Every other 3D node duplicates this Inspector Settings tab. A full description of these common controls appears where the chapter wraps up, in the “The Common Controls” section.

### Sphere Map [3SpM]

### The SphereMap node

### Sphere Map Node Overview

The Sphere Map node can build simulated environment mapping, also known as reflection mapping. Ray trace rendering a reflective scene can eat up a lot of time, but sphere map-based reflection mapping can produce 360-degree reflections faster with little loss of accuracy. As an example, when crafting a reflective environment, a sphere map is created, big enough to surround the 3D object in your scene. The sphere gets mapped with the environment you want reflected and connects to the Reflection Color input on a Reflect node.

### Inputs

The single image input on the Sphere Map node takes a 2D image texture in an equirectangular format (where the X-axis stands for 0–360 degrees longitude, and the Y-axis stands for –90 to +90 degrees latitude.) ImageInput: The orange Image input takes a 2D RGBA image. Ideally this is an equirectangular image showing the full vertical and horizontal angle of view up to 360 degrees.
