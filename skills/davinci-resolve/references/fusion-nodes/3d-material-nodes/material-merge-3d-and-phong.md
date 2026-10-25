# Material merge 3D and phong

Version: DaVinci Resolve 20.3 Reference Manual. Context: Material merge 3D, Phong.
[Chapter index](INDEX.md) / [Previous section](cook-torrance-common-controls.md) / [Next section](phong-and-reflect-and-stereo-mix.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-blend"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-diffuse"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-material-merge-3d-3mm"></a> <a id="source-material-merge-controls"></a> <a id="source-material-merge-node-introduction"></a> <a id="source-phong-3ph"></a> <a id="source-phong-controls"></a> <a id="source-phong-node-introduction"></a> <a id="source-specular"></a> <a id="source-the-material-merge-node"></a> <a id="source-the-phong-node"></a>

### Material Merge 3D [3MM]

### The Material Merge node

### Material Merge Node Introduction

Two distinct materials can be fused together by the Material Merge node. It serves to composite Material nodes — pairing several illumination materials (Blinn, Cook Torrance) with texture nodes (Bump Map, Reflection) to assemble intricate shader networks. On top of that, the node offers a way to stamp a fresh material identifier onto the merged result.

### Inputs

For the pair of materials being joined, the Material Merge node supplies two inputs. Background Material: The orange Background material input takes a 2D image or a 3D material, which becomes the background material. Foreground Material: The green Foreground material input takes a 2D image or a 3D material, which becomes the foreground material. Under the basic shading model, any 2D image is read as a diffuse texture map.

### Basic Node Setup

A Material Merge node’s output feeds the material input of a 3D scene or 3D geometry node. In the example that follows, the Material Merge node draws a background base layer off the Blinn shader and blends it with a more heavily textured bump map layer.

A Material Merge node that fuses a Blinn-based shader (teal underlay) with a Ward-based shader (orange underlay)

### Inspector

### Material Merge controls

### Controls Tab

A lone slider on the Controls tab blends the two materials with one another.

### Blend

How the Material Merge blends echoes the Dissolve (DX) node used for images. Each input’s share of the mix between the two materials or textures is governed by the slider’s value. Even though a 2D image may stand in for a material at either the background or foreground input, what leaves this node is always a material. In a departure from the 2D Dissolve node, here both foreground and background inputs must be present. Material ID Through this slider you assign the numeric identifier carried by the resulting material. Whenever the matching renderer option is switched on, that figure is written into the MatID auxiliary channel.

### Common Controls

Settings Tab This Inspector Settings tab appears again throughout the rest of the 3D nodes. The shared controls it holds get a thorough write-up where the chapter ends, in “The Common Controls.”

### Phong [3Ph]

### The Phong node

### Phong Node Introduction

As a basic illumination material, the Phong node can be laid onto geometry sitting in the 3D scene. It defines the object’s reaction to light and exposes several texture map inputs so you can finely tune the material’s diffuse, specular, and bump map components. Although its highlight resembles the one the Blinn model yields, the Phong node tends to be chosen for glossy, polished plastic surfaces.

### Inputs

The Phong node carries five inputs, each taking a 2D image or a 3D material. They steer the overall color and imagery of the 3D object and likewise the color and texture feeding the specular highlight. Every one of them scales the texture map’s pixels by the like-named parameter on the node itself, an efficient way to dial portions of the material up or down. Diffuse Material: The orange Diffuse material input takes a 2D image or a 3D material that supplies the object’s main color and texture. Specular Color Material: The green Specular Color material input takes a 2D image or a 3D material that supplies the highlight color and texture for the object. Specular Intensity Material: The magenta Specular Intensity material input takes a 2D image or a 3D material acting as an intensity map for the material’s highlights. Should the input be a 2D image, its Alpha channel builds the map while the color channels are thrown out. Specular Exponent Material: The teal Specular Exponent material input takes a 2D image or a 3D material acting as a falloff map for the material’s specular highlights. Should the input be a 2D image, its Alpha channel builds the map while the color channels are thrown out. Bump Map Material: The white Bump Map texture input takes only a 3D material. The usual route is to wire the texture into a Bump Map node and then route that Bump Map node into this input. The RGB data here serves as texture-space normals. With a node carrying this many inputs, precise connections can be tricky. While dragging another node’s output across the node tile, press and keep holding the Option or Alt key, still holding it as you let go of the left mouse button. Up pops a small drop-down listing every input the node offers. Click the one you want to finish the connection.

### Basic Node Setup

A Phong node’s output wires into the material input of a 3D scene or 3D geometry node. In the example beneath, the Phong node pulls a base Color Diffuse input from the Fast Noise node plus a bump map texture that another Fast Noise node produces.

A Phong node with a diffuse color and Bump Map input

### Inspector

### Phong controls

### Controls Tab

On the Controls tab sit the parameters that tune the main color, highlight, and lighting behavior of the Phong shader node.

### Diffuse

Diffuse captures the underlying surface traits before extras such as reflections or specular highlights come into play. Beyond setting an object’s base color, the diffuse color additionally governs the object’s transparency. A diffuse texture map’s Alpha lets you render selected parts of the surface see-through. Diffuse Color The Diffuse Color of a material is the base hue it shows when lit by indirect or ambient light. With a diffuse texture map present, the color value entered here is multiplied against the texture’s color values. Alpha This slider fixes the material’s Alpha channel value. It acts on diffuse and specular colors alike and on the material’s Alpha value in the rendered output. With a diffuse texture map present, the Alpha value entered here is multiplied against the Alpha values in the texture map. Opacity Lowering a material’s Opacity pulls down the color and Alpha values of both specular and diffuse colors together, turning the material transparent.

### Specular

Settings in the Specular section dictate how the surface’s specular highlight looks, and each illumination model interprets these values its own way. Specular Color Specular Color picks the hue of light bouncing off a shiny surface. A more specular material reads as glossier. Plastics and glass usually show white specular highlights, while metals such as gold carry highlights tinted by the material color itself. With a specular texture map present, the value here is multiplied by the texture’s color values. Specular Intensity Specular Intensity sets how pronounced the specular highlight becomes. When the specular intensity texture is present, this value is multiplied by that texture’s Alpha value. Specular Exponent Specular Exponent governs the highlight’s falloff. A larger value sharpens that falloff and renders the material smoother and glossier. When the specular exponent texture is present, this value is multiplied by the texture map’s Alpha value.
