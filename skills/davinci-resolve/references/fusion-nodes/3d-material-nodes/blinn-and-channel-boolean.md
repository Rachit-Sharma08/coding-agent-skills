# Blinn and channel boolean

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blinn, Channel boolean.
[Chapter index](INDEX.md) / [Next section](channel-boolean-and-cook-torrance.md)
<a id="source-3d-material-nodes"></a> <a id="source-3d-material-nodes-part-1"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-blinn-3bl"></a> <a id="source-blinn-controls"></a> <a id="source-blinn-node-introduction"></a> <a id="source-channel-boolean-3bol"></a> <a id="source-channel-boolean-node-introduction"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-diffuse"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-specular"></a> <a id="source-the-blinn-node"></a> <a id="source-the-channel-boolean-node"></a> <a id="source-transmittance"></a>

### 3D Material Nodes

This section covers the 3D Material nodes you have on hand for building 3D composites in Fusion. The abbreviation beside each node name works in the Select Tool dialog while hunting for tools, as well as in scripting references.

Throughout this document, treat node graphs that display MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a difference is called out.

### Blinn [3Bl]

### The Blinn node

### Blinn Node Introduction

As a fundamental illumination material, the Blinn node can be laid onto geometry within the 3D scene. It spells out how an object reacts to light and supplies several texture map inputs so you can finely steer the material's diffuse, specular, and bump map parts. That standard basic material sitting in the Materials tab of most geometry nodes is really a pared-down take on the Blinn node, the chief distinction being that the Blinn node hands you extra texture map inputs on top of diffuse alone. What the Blinn node puts out is a 3D Material you can wire into the material inputs of any 3D geometry node. Within Fusion, the Blinn model figures the highlight from the dot product of the surface normal against the half angle vector between the light source and viewer (dot(N, H)), which won't always line up with the Blinn illumination model that other 3D applications employ.

### Inputs

The Blinn node carries five inputs that take 2D images or 3D materials. Through them you govern the overall color and image applied to the 3D object, plus the color and texture driving the specular highlight. Every one of these inputs scales the texture map's pixels by the like-named parameters living in the node, giving you a tidy way to scale portions of the material. Diffuse Texture: The orange Diffuse Texture input takes a 2D image or a 3D material to serve as the object's main texture map. Specular Color Material: The green Specular Color material input takes a 2D image or a 3D material to serve as the color texture map across specula highlight regions. Specular Intensity Materials: The magenta Specular Intensity material input takes a 2D image or a 3D material for adjusting how intense the specular highlights are. Should that input be a 2D image, the map is built from the Alpha channel while the color channels are thrown away. Specular Exponent Material: The teal Specular Exponent material input takes a 2D image or a 3D material acting as a falloff map for the material's specular highlights. Should that input be a 2D image, the map is built from the Alpha channel while the color channels are thrown away. Bump Map Material: The white Bump Map material input takes a 3D material only. The usual route is to wire the texture into a Bump Map node, then run that Bump Map node into this input. Here the RGB information is read as texture-space normals.

Once a node sports this many inputs, wiring them up precisely gets tricky. Press and hold the Option (macOS) or Alt (Windows) key as you drag another node's output across the node tile, and keep Option or Alt down as you let go of the left mouse button. Up pops a compact drop-down menu naming every input the node exposes; click the one you want to seal the connection. As another route, dragging a node's output with the right mouse button calls up that same menu.

### Basic Node Setup

You route a Blinn node's output into the material input of whichever 3D scene or 3D geometry node you mean to shade. The Blinn inputs accept images for the diffuse color material (orange) and the specular color material (green), which can yield a smooth, glossy material.

A Blinn shader with diffuse and specular color materials connected Inspector

### Blinn controls

### Controls Tab

For the Blinn node, the Controls tab is the main one. It steers the color and shininess laid across the 3D geometry's surface.

### Diffuse

Diffuse captures the underlying surface traits before any extras such as reflections or specular highlights enter the picture. On top of fixing an object's base color, the diffuse color also sets the object's transparency, and the Alpha within a diffuse texture map lets you render parts of the surface see-through. Diffuse Color A material's Diffuse Color is the base color it shows when lit indirectly or by ambient light. Supply a diffuse texture map and the color value entered here gets multiplied against the texture's color values. Alpha This slider fixes the material's Alpha channel value, acting on diffuse and specular colors alike and on the material's Alpha value in the rendered output. Supply a diffuse texture map and the Alpha value set here gets multiplied against the texture map's Alpha values. Opacity Lowering the material's opacity drops the color and Alpha values of both the specular and diffuse colors together, turning the material transparent.

### Specular

Within the Specular section, the parameters spell out the look of the surface's specular highlight, and these values get evaluated differently under each illumination model. Specular Color Specular Color sets the color of light bouncing off a glossy surface. A more specular material reads as glossier. Materials such as plastics and glass usually throw white specular highlights, while metallic surfaces like gold show specular highlights that take their color from the material color itself. Supply a specular texture map and the value entered here gets multiplied against the texture's color values. Specular Intensity Specular Intensity governs how forceful the specular highlight is. Supply the specular intensity texture and this value gets multiplied against the texture's Alpha value. Specular Exponent Specular Exponent governs the specular highlight's falloff. A larger value makes the falloff sharper and the material smoother and glossier. Supply the specular exponent texture and this value gets multiplied against the texture map's Alpha value.

### Transmittance

Transmittance governs how light travels through a material. Take a solid blue sphere, which throws a black shadow, versus one of translucent blue plastic, which would throw a far lighter blue shadow. A distinct Opacity option exists too. Opacity decides how see-through the actual surface renders. Fusion lets you tune opacity and transmittance on their own, which can feel odd at first to anyone new to 3D software. You can indeed have a surface that is wholly opaque yet still passes 100% of the light reaching it, in effect turning it into a luminous/ emissive surface. Attenuation Attenuation sets how much color makes it through the object. To give an object transmissive shadows, dial the attenuation to (1, 1, 1), meaning all of the green, blue, and red light travels through. Set this color to RGB (1, 0, 0) and the material lets through 100% of the red striking the surface but none of the green or blue. This serves well for “stained glass”styled shadows. Alpha Detail With the Alpha Detail slider at 0, the object's Alpha channel is disregarded and the whole object throws a shadow. Push it to 1 and the Alpha channel dictates which parts of the object throw a shadow. Color Detail The Color Detail slider tints the light crossing the surface by the diffuse color + texture colors. Reach for it to cast a shadow carrying the color details of the texture on the object. Raising the slider from 0 to 1 folds more diffuse color + texture color into the shadow. Keep in mind that the object's Alpha and opacity are skipped while transmitting color, so even an object with solid Alpha can still send its color into the shadow. Saturation The Saturation slider rules the saturation of the color component handed to the shadow. Drop it to 0.0 and you get monochrome shadows. Receives Lighting/Shadows These checkboxes decide whether scene lighting and shadows touch the material. Switch them off and the object stays fully lit and/or unshadowed. Two-Sided Lighting This in effect renders the surface two sided by appending a second set of normals pointing the other way on the surface's backside. It usually sits off to speed up rendering, but you can enable it for 2D surfaces or for objects that aren't fully sealed, so the reverse or interior surfaces show as well. Ordinarily, a 3D application shows only a surface's front face and culls the back, so a camera orbiting a plane in such an application would find the plane vanish once it swung behind. Making a plane two sided in a 3D application amounts to stacking a second plane onto the first, spun 180 degrees so its backside normals face the other direction. So when you orbit around the back, what greets you is that second image plane, its normals pointing the opposite way.

When you make a surface two sided, Fusion behaves precisely as those 3D applications do. The muddle over what two-sided lighting accomplishes stems from Fusion not culling back-facing polygons out of the box. Orbit a one-sided plane in Fusion and you still catch it from the backside (though what you see is the frontside carried straight through to the back as if transparent). Turning the plane two sided in effect tacks a second set of normals onto the plane's backside. NOTE: Things can get genuinely confusing the moment you make the surface transparent, since the same rules hold and the outcome runs counter to intuition. View a transparent two-sided surface from the front while it is lit from behind, and it reads as unlit. Material ID This slider assigns the numeric identifier given to this material. That value is written into the MatID auxiliary channel whenever the matching option is switched on in the renderer.

### Common Controls

Settings Tab Other 3D nodes carry the same Settings tab found in the Inspector. A full account of these shared controls comes later, within this chapter's “The Common Controls” section.

### Channel Boolean [3Bol]

### The Channel Boolean node

### Channel Boolean Node Introduction

The Channel Boolean (don't mix it up with the 2D Channel Booleans) lets you remap and reshape the channels of 3D materials through mathematical operations. Say you want a material's red channel to drive a scalar input on an illumination model that reads the Alpha channel (e.g., Blinn. SpecularExponent) — you can remap the channels right here. On top of that, it opens the door to geometry-specific data such as texture space coordinates and normals.

### Inputs

The Channel Boolean Node has two inputs: one carrying the foreground material and one carrying the background material. Each input takes either a 2D image or a 3D material such as the Blinn, Cook-Torrence, or Phong node. BackgroundMaterial: The orange background material input takes a 2D image or a 3D material. ForegroundMaterial: The green foreground input likewise takes a 2D image or a 3D material.

### Basic Node Setup

The material 3D Channel Boolean finds plenty of uses. More often than not it serves to merge material looks or work over UV texture coordinates In the example below, the Channel Boolean node fuses the Cook Torrance and Blinn materials. Drawing on the math operands inside the Channel Boolean, it switches, inverts, and blends the two inputs to conjure a neon flickering effect.

A Channel Boolean merging and acting upon a pair of Cook Torrance and Blinn nodes Inspector
