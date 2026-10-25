# Channel boolean and cook torrance

Version: DaVinci Resolve 20.3 Reference Manual. Context: Channel boolean, Cook torrance.
[Chapter index](INDEX.md) / [Previous section](blinn-and-channel-boolean.md) / [Next section](cook-torrance-common-controls.md) / [Continue Cook Torrance 3CT / Common Controls](cook-torrance-common-controls.md) / [Channel Boolean 3Bol](blinn-and-channel-boolean.md)
<a id="source-basic-node-setup-2"></a> <a id="source-channel-boolean-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-cook-torrance-3ct"></a> <a id="source-cook-torrance-controls"></a> <a id="source-cook-torrance-node-introduction"></a> <a id="source-diffuse-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-specular-1"></a> <a id="source-the-cook-torrance-node"></a> <a id="source-transmittance-1"></a>

### Channel Boolean controls

### Controls Tab

The Controls tab carries a section per RGBA channel. Each channel holds two input menus named Operand A and Operand B, and the Operation menu picks which function runs on the pair. Operand A/B One Operand menu exists for every output RGBA channel, letting you choose the input information you want feeding that channel.

Red/Green/Blue/Alpha FG Red/Green/Blue/Alpha BG Black/White/Mid Gray Hue/Lightness/Saturation FG Hue/Lightness/Saturation BG Luminance FG Luminance BG X/Y/Z Position FG U/V/W Texture FG U/V/W EnvCoords FG X/Y/Z Normal

Pulls the foreground material's color information. Pulls the background material's color information. Pins the channel's value to 0, 0.5, or 1. Pulls the foreground material's color information, recasts it into the HLS color space, and drops the chosen information into the matching channel. Pulls the background material's color information, recasts it into the HLS color space, and drops the chosen information into the matching channel. Pulls the foreground material's color information and works out the channel's luminance value. Pulls the background material's color information and works out the channel's luminance value. Pins the channel's value to where the pixel sits in 3D space, with the vector information handed back in eye space. Maps the foreground material's texture space coordinates onto the channels. Maps the environment texture space coordinates onto the channels. Place it ahead of nodes that alter the environment texture coordinates, such as the Reflect 3D node. Pins the channel's value to the chosen axis of the normal vector, the vector being handed back in eye space.

Operation Sets the Operation by which the operands are merged.

`A` `B` `1-A` `1-B` `A+B` `A-B` `A*B` `A/B` `min(A,B)` `max(A,B)` `avg(A,B)`

Draws on Operand A alone for the output channel. Draws on Operand B alone for the output channel. Takes the value of Operand A away from 1. Takes the value of Operand B away from 1. Sums the values of Operand A and B. Takes the value of Operand B away from A. Multiplies the values of both Operands together. Divides A by the value of Operand B. Weighs the values of Operands A and B against each other and yields the smaller. Weighs the values of Operands A and B against each other and yields the larger. Yields the mean value of both Operands.

Material ID This slider hands this material its numeric identifier. The renderer writes that value into the MatID auxiliary channel when the matching option is turned on.

### Common Controls

Settings Tab The Inspector's Settings tab shows up again across other 3D nodes. These shared controls receive a thorough write-up at the chapter's end, under “The Common Controls.”

### Cook Torrance [3CT]

### The Cook Torrance node

### Cook Torrance Node Introduction

As a fundamental illumination material, the Cook Torrance node can be laid onto geometry within the 3D scene. Its diffuse calculation runs close to what the basic material and the Blinn node use, yet its specular highlights are worked out through an optimized Fresnel/Beckmann equation. You reach for this illumination model mainly when shading metal or other glossy, strongly reflective surfaces. What the Cook Torrance node puts out is a 3D Material you can wire into the material inputs of any 3D geometry node.

### Inputs

The Cook Torrance node carries six inputs that take 2D images or 3D materials. Through them you govern the overall color and image applied to the 3D object, along with the color and texture driving the specular highlight. Every one of these inputs scales the texture map's pixels by the like-named parameters living in the node, which gives you a tidy way to scale portions of the material. Diffuse Color Material: The orange Diffuse Color material input takes a 2D image or a 3D material to act as the object's overall color and texture. Specular Color Material: The green Specular Color material input takes a 2D image or a 3D material to act as the specular highlight's color and texture. Specular Intensity Material: The magenta Specular Intensity material input takes a 2D image or a 3D material for adjusting the specular highlight's intensity. Should that input be a 2D image, the map is built from the Alpha channel and the color channels are thrown away. Specular Roughness Material: The white Specular Roughness material input takes a 2D image or a 3D material to act as a map for tweaking the specular highlight's roughness. The texture map's Alpha gets multiplied by the roughness control's value. Specular Refractive Index Material: The white Specular Refractive Index material input takes a 2D image or a 3D material, treating its RGB channels as the refraction texture. Bump Map Material: A 3D material is all that the white Bump Map material input will take. The usual route is to wire the texture into a Bump Map node, then run that Bump Map node into this input, where the RGB information is read as texture-space normals. Every one of these inputs scales the texture map's pixels by the like-named parameters living in the node, which gives you a tidy way to scale portions of the material. Once a node sports this many inputs, wiring them up precisely gets tricky. Press and hold the Option (macOS) or Alt (Windows) key as you drag another node's output across the node tile, and keep Option or Alt down as you let go of the left mouse button. Up pops a compact drop-down menu naming every input the node exposes; click the one you want to seal the connection.

### Basic Node Setup

You route a Cook Torrance node's output into the material input of whichever 3D scene or 3D geometry node you mean to shade. The Cook Torrance inputs accept images for the diffuse color material (yellow) and the specular color material (green), which can yield a smooth, glossy material.

A Cook Torrance shader with diffuse and specular color materials connected

### Inspector

### Cook Torrance controls

### Controls Tab

On the Controls tab you'll find parameters for tuning the Cook Torrance shader node's main color, highlight, and lighting properties.

### Diffuse

Diffuse stands for the fundamental surface traits before extras like reflections or specular highlights come into play. Beyond fixing an object's base color, the diffuse color also governs how transparent the object is, and a diffuse texture map's Alpha can render chosen parts of the surface see-through. Diffuse Color The Diffuse Color of a material is the base color it presents under indirect or ambient lighting. Hand it a diffuse texture map and the color value here is multiplied against the texture's color values. Alpha This slider fixes the material's Alpha channel value, weighing equally on diffuse and specular colors and on the material's Alpha value in the rendered output. Hand it a diffuse texture map and the Alpha value here is multiplied against the texture map's Alpha values. Opacity Pulling down the material's Opacity cuts the color and Alpha values of the specular and diffuse colors in equal measure, rendering the material transparent.

### Specular

The Specular section's parameters lay out how the surface's specular highlight looks, and each illumination model evaluates these values its own way. Specular Color Specular Color fixes the color of light reflecting off a glossy surface. The more specular the material, the glossier it reads. Plastics and glass typically carry white specular highlights, whereas metallic surfaces such as gold draw their highlight color from the material color. Hand it a specular texture map and the value here is multiplied against the texture's color values. Specular Intensity Specular Intensity rules how strong the specular highlight comes across. Hand it the specular intensity texture and this value is multiplied against the texture's Alpha value. Roughness The specular highlight's Roughness captures how the highlight spreads across the surface. A larger value broadens the falloff and lends the surface a more brushed, metallic feel. Hand it the roughness texture map and this value is multiplied against the texture's Alpha value. Do Fresnel Ticking this checkbox folds Fresnel calculations into the material's illumination model, yielding more believable metal surfaces by factoring in the material's refractiveness. Refractive Index This slider surfaces once the Do Fresnel checkbox is ticked. The Refractive Index bears only on the highlight calculations; it does not actually refract light through transparent surfaces. Hand it the refractive index texture map and this value is multiplied against the input's Alpha value.

### Transmittance

Transmittance rules how light makes its way through a material. Consider a solid blue sphere, which throws a black shadow, against one of translucent blue plastic, which would throw a far fainter blue shadow. A separate Opacity option is on hand as well. Opacity decides how transparent the actual surface comes out when rendered. Fusion lets you tune opacity and transmittance independently — a notion that may strike newcomers to 3D software as odd at first. You really can have a surface that is fully opaque yet still passes 100% of the light reaching it, which in effect turns it into a luminous/ emissive surface. Attenuation Attenuation rules how much color travels through the object. To grant an object transmissive shadows, set the attenuation to (1, 1, 1), so all of the green, blue, and red light passes through. Set this color to RGB (1, 0, 0) and the material lets 100% of the red striking the surface through while blocking the green and blue. You can lean on this to fashion “stained glass”-styled shadows.

Alpha Detail Hold the Alpha Detail slider at 0 and the object's Alpha channel is passed over, so the whole object throws a shadow. Raise it to 1 and the Alpha channel decides which parts of the object throw one. Color Detail The Color Detail slider colors the light crossing the surface by the diffuse color + texture colors. Turn to it to cast a shadow that carries the color details of the texture on the object. Nudging the slider from 0 toward 1 pours more diffuse color + texture color into the shadow. Mind that the object's Alpha and opacity are bypassed while color is transmitted, so an object with solid Alpha can still pour its color into the shadow. Saturation The Saturation slider commands the saturation of the color component sent to the shadow. Bring it to 0.0 and the shadows come out monochrome. Receives Lighting/Shadows These checkboxes decide whether the scene's lighting and shadows reach the material. Switch them off and the object stays fully lit and/or free of shadow. Two-Sided Lighting This in effect makes the surface two sided by tacking on a second set of normals that point the other way on the surface's backside. It normally rests off to keep rendering quick, but you can switch it on for 2D surfaces or for objects that aren't fully sealed, so their reverse or interior surfaces become visible too. Typically a 3D application shows only a surface's front face and culls the back, so a camera circling a plane in such an application would watch the plane disappear upon reaching the backside. Making a plane two sided in a 3D application comes down to laying a second plane atop the first, turned 180 degrees so its backside normals point the opposite way. Hence, swinging around the back reveals that second image plane with its normals facing the other direction. NOTE: This can grow rather bewildering once the surface goes transparent, since the same rules persist and hand you a counterintuitive result. Look at a transparent two-sided surface from the front while it is lit from behind, and it appears unlit. Material ID This slider hands this material its numeric identifier. That value lands in the MatID auxiliary channel whenever the matching option is enabled in the renderer.
