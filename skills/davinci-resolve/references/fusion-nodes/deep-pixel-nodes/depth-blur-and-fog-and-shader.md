# Depth blur and fog and shader

Version: DaVinci Resolve 20.3 Reference Manual. Context: Depth blur, Fog, Shader.
[Chapter index](INDEX.md) / [Previous section](ambient-occlusion-and-depth-blur.md) / [Next section](shader-and-texture-and-common-controls.md) / [Depth Blur DBl](ambient-occlusion-and-depth-blur.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-depth-blur-controls"></a> <a id="source-fog-controls"></a> <a id="source-fog-fog"></a> <a id="source-fog-node-introduction"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-shader-controls"></a> <a id="source-shader-node-introduction"></a> <a id="source-shader-shd"></a> <a id="source-the-fog-node"></a> <a id="source-the-shader-node"></a>

### Depth Blur controls

### Controls Tab

Parameters for dialing in how much blur lands and how deep the blurred zone runs sit on the Controls tab. It additionally offers choices for picking channels apart from the Z channel as the blur map. Filter This menu picks which filter drives the blur.

- Box: This lays a plain depth-based box blur effect onto the image.
- Soften: This lays on a depth-based general softening filter effect.
- Super Soften: This lays on a depth-based high-quality softening filter effect.

Blur Channel Pick one of these choices to set which channel governs how much blur each pixel receives. The channel drawn from the main image input is what’s used, unless an image gets wired into the node’s green Blur Image input.

Lock X/Y Switched on, this control binds the X and Y Blur sliders together so blurring stays symmetrical. Blur Size This slider serves to set how strong the horizontal and vertical blurring is. Focal Point Only when the Blur channel menu is set to draw on the Z channel does this control show. Lean on this control to pick how far off the simulated point of focus sits. Drop the value and the Focal Point moves nearer the camera; raise it and the Focal Point moves farther off. Depth of Field This control serves to set how deep the in-focus zone runs. With the focal point sitting at the center of the region, every pixel whose Z-value falls inside the region holds focus. As an example, were the focal point picked off the image and set to 300, with the depth of field set to 200, any pixel carrying a Z-value between 200 and 400 would stay in focus. Z Scale Scales the Z-buffer value by whatever amount you pick. Raise the value and the distances within the Z-channel stretch out. Drop it and they pull in. This proves handy for overstating the depth effect. It can equally serve to soften the blur’s boundaries. Certain images carrying small depth values may call for the Z-scale to sit fairly low, under 1.0.

### Common Controls

Settings Tab A copy of the Settings tab in the Inspector also turns up across the other Deep Pixel nodes. Those shared controls get covered thoroughly at this chapter’s close within the “The Common Controls” section.

### Fog [Fog]

### The Fog node

### Fog Node Introduction

What the Fog node serves is building simulated fog looks across 3D-rendered images that hold a valid Z-buffer channel. Depending on which Z-channel planes you pick, the fog can sit ahead of or behind the assorted elements of a rendered image.

### Inputs

Three inputs come with the Fog node: one carrying the main image with a Z channel, one carrying a blur image, plus another carrying an effect mask to bound the region where the depth blur lands.

Input: This orange input is the lone connection that’s required. It takes a 2D image carrying a Z channel. That Z channel sets how much fog applies across the differing regions of the picture. Blur Image: The green second image input hooks up an image serving as the fog’s source. Supply no image and the fog ends up a single color. As a rule, some sort of noise map gets wired in here. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the fog to just the pixels falling inside the mask. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

You normally drop the Fog node in after a Renderer 3D node. That Renderer 3D node has to have Z-Depth switched on among its output channels.

A Fog node slotted in as a 2D post process following the Renderer 3D node Inspector

### Fog controls

### Controls Tab

Parameters for dialing in the fog’s density and color sit on the Controls tab. Z-Buffer Near Plane and Far Plane These controls serve to pick how far the fog reaches within the scene. To set a value, drag the Pick button onto a spot in the image you’re viewing where the plane should sit. The Near Plane serves to pick the depth at which the fog tapers off to nothing. The Far Plane serves to pick the depth at which the fog turns opaque. Z Depth Scale This choice scales the Z-buffer values by whatever amount you pick. Raise the value and the distances within the Z-channel stretch out, whereas dropping it pulls those distances in. This proves handy for overstating the fog effect. Fog Color This choice shows and governs the present fog color. Alpha tunes the fog’s transparency value. Fog Opacity Lean on this control to tune the opacity across every channel of the fog.

### Common Controls

Settings Tab A copy of the Settings tab in the Inspector also turns up across the other Deep Pixel nodes. Those shared controls get covered thoroughly at this chapter’s close within the “The Common Controls” section.

### Shader [Shd]

### The Shader node

### Shader Node Introduction

The Shader node can steer the lighting, reflection mapping, and 3D shading of elements within a rendered image. What the node depends on is the normal map channel being present in a rendered image. Should that channel be absent, this node does nothing.

### Inputs

Three inputs come with the Shader node: one carrying the main image with normal map channels, one carrying a reflection map, plus another carrying an effect mask to bound the region where the depth blur lands. Input: This orange input is the lone connection that’s required. It takes a 2D image carrying a normals channel.

Reflection Map Image: The green reflection map image input casts an image onto every element in the scene, or onto elements singled out by the Object and Material ID channels within the Common Controls. Reflection maps perform best as 32-bit floating point, equirectangular formatted images Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the shader to just the pixels falling inside the mask. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

You slot the Shader node in after a 2D image holding a Normals channel. Down below, a Renderer 3D serves to attach a Normals channel onto an image. The Shader node draws on the normals to refine how the surface looks, with a reflection map wired in.

The Shader node drawing on normals out of a Renderer 3D together with a reflection input Inspector

### Shader controls

### Controls Tab

The Controls tab for the Shader node carries parameters for tuning how the overall surface responds to light sources. You can reshape the ambient, diffuse, specular, and reflection traits of the image wired into the orange image input. Light Tab Parameters covering basic lighting brightness plus reflections sit on the Controls tab. Ambient What Ambient governs is the Ambient color present throughout the scene or on the chosen object. This is a baseline level of light laid onto every pixel, even across fully shadowed areas.

Diffuse This choice governs the Diffuse color present throughout the scene or for the chosen object. This is the object’s normal color, thrown back equally in every direction. Specular This choice governs the Specular color present throughout the scene or for the chosen object. This is the color of the glossy highlights bounced toward the eye off a light source. Reflection This choice governs the Reflection contribution throughout the scene or for the chosen object. High settings leave objects looking mirrored, while low settings layer on faint reflections for a polished feel. With no reflection map wired in, it does nothing. Reflection Type This menu sets which kind of reflection mapping projects the image arriving at the second input. Screen: Screen makes the reflection map look as though it were cast onto a screen sitting behind the point of view. Spherical: Spherical makes the reflection map look as though it were cast onto an enormous sphere wrapping the entire scene. Refraction: Refraction makes the reflection map look as though it were refracting or warping in line with the scene’s geometry. Equator Angle What Equator Angle governs is the left-to-right angle of the light the Shader node produces and maps for the scene or the chosen object. Polar Height What Polar Height governs is the top-to-bottom angle of the light the Shader node produces and maps for the scene or the chosen object.
