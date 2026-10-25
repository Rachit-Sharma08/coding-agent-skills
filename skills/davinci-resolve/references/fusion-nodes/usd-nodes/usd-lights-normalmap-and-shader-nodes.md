# Udome light and urectangle light and usphere light and unormalmap and ushader

Version: DaVinci Resolve 20.3 Reference Manual. Context: Udome light, Urectangle light, Usphere light, Unormalmap, Ushader.
[Chapter index](INDEX.md) / [Previous section](usd-volume-and-light-nodes.md) / [Next section](usd-shader-texture-transform-and-common-controls.md) / [uDome Light uDo](usd-volume-and-light-nodes.md)
<a id="source-controls-tab-3"></a> <a id="source-controls-tab-4"></a> <a id="source-controls-tab-5"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a> <a id="source-inputs-6"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-inspector-5"></a> <a id="source-introduction"></a> <a id="source-the-unormal-map-controls"></a> <a id="source-the-usd-dome-light-controls"></a> <a id="source-the-usd-normal-map"></a> <a id="source-the-usd-rectangle-light-controls"></a> <a id="source-unormalmap-unm"></a> <a id="source-urectangle-light-url"></a> <a id="source-usage"></a> <a id="source-usd-material"></a> <a id="source-ushader-usd"></a> <a id="source-usphere-light-usl"></a>

### Inputs

Scene Input: links in a USD scene, which then lets you alter whatever lights are already present. Image Input: Whether you're texturing a USD object or lighting a scene through uDomeLight, the Image Input draws frames from any Fusion node already in your comp. That means you can feed in Fusion tools — video inputs and generated graphics among them — rather than relying on a pre-rendered image for the texture. Once it's connected, the Inspector hides the File Name control, and the Image Input supersedes whatever image file was sourced beforehand. Wire a node into the Image Input on uShape or uReplaceMaterial and the image arrives as a diffuse texture. Where the File Name route only pulls in a single frame as a texture, the Image Input opens up animated textures, lending more latitude for both lighting and texturing.

### Inspector

### The USD Dome Light controls

### Controls Tab

You configure the uDome light's color and brightness in the Controls tab, while the Transform tab manages the light source's position, direction, and scale. Override Selection A press of the Pick button picks out a light that's already in an attached USD file, the means by which an imported scene's lights get adjusted. Color This standard Color control assigns the light's color.

Intensity This slider sets the light's intensity, with 0.2 standing for 20% percent light. Exposure Similar in effect to Intensity, this varies the amount of exposure the light gives a scene. Color Temperature/Enable This establishes the color temperature of a light source, defaulting to 6500K, which equals daylight temperature. Diffuse Response Regulates how much the light pours into a material's Diffuse color. Specular Response Regulates how much the light pours into a material's Specular color. Normalize This smooths the light's contribution over the scene. Guide Radius This determines how big the dome wrapping the scene is. By default it's large and distant, like the outdoors, but you can shrink the radius to mimic a room-sized space. Texture File/Browse This loads an image to map onto the Domelight. Texture Format Sphere-mapped images may be held in several schemes, the usual ones being Lat-Long, MirrorBall, Angular, and Cube Mapped Vertical Cross.

### uRectangle Light [uRL]

The USD Rectangle light uRectangle Light Node Introduction This emitter, the uRectangle, presents a flat profile, comparable to a softlight or a window . Its color and brightness are set from the Controls tab, while the light source's position, direction, and scale fall to the Transform tab.

### Inputs

There's a single yellow Scene Input for connecting a USD scene, and through it you can reshape any lights the scene already contains.

### Inspector

### The USD Rectangle Light controls

### Controls Tab

The Controls tab handles setting the uDome light's color and brightness, and the Transform tab oversees the light source's position, direction, and scale. Override Selection Click the Pick button to adopt a light that already exists in an attached USD file, the way you adjust the lights of an imported scene. Color Apply this standard Color control to color the light. Intensity This slider determines the light's intensity, where 0.2 maps to 20% percent light. Exposure In the same vein as Intensity, this adjusts how much the light exposes a scene. Color Temperature/Enable This nails down a light source's color temperature; its default of 6500K equals daylight temperature. Diffuse Response Manages how much the light contributes to a material's Diffuse color. Specular Response Manages how much the light contributes to a material's Specular color. Normalize This regularizes the light's contribution throughout the scene.

Shaping Focus This marks the focus point of this light's lens effect. Shaping Cone Angle Sets the angle across which the light spreads. Width Sets how wide the light reads. Height Sets how tall the light reads.

### uSphere Light [uSL]

The USD Sphere light uSphere Light Node Introduction A uSphere light is a local light resembling a point light, except that it also carries a radius. An onscreen control accompanies it, and rotating that control settles which direction the light points from in the scene.

### Inputs

One Scene Input, colored yellow, lets you attach a USD scene, and with it attached you're free to adjust the lights already standing in the scene.

### Inspector

### Controls Tab

You dial in the uSphere light's color and brightness from the Controls tab, and the Transform tab takes over the light source's position, direction, and scale. Override Selection Pressing the Pick button picks up a light already living in an attached USD file, your means for adjusting an imported scene's lights. Color Lean on this standard Color control to set the light's hue. Intensity This slider rules the light's intensity, where 0.2 represents 20% percent light. Exposure Like Intensity before it, this changes how far the light exposes a scene. Color Temperature/Enable This sets the color temperature for a light source, with a 6500K default that matches daylight temperature. Diffuse Response Sets the degree to which the light feeds a material's Diffuse color. Specular Response Sets the degree to which the light feeds a material's Specular color. Normalize This evens the light's contribution across the scene. Treat as Point This reduces the light to a plain classic point source. Radius This sets the sphere light's size.

### USD Material

With the uTexture, uTextureTransform, uNormalMap, and uShader nodes you can pull textures straight into your USD scene and work on them there, skipping the step of bundling them into a USD file beforehand. These tools lend extra freedom and control to the USD workflow you run on the Fusion page.

A sample texture replacement node tree built from the USD Materials tools The uTexture, uTextureFormat, and uNormalMap tools are meant to surround and route a texture into the uShader tool, where the USD or MaterialX models reshape its appearance. Typically the uShader hooks into a uReplaceMaterial node, which picks out the particular regions of the whole USD scene that should receive the new texture. The upshot is that you can cycle through texture changes entirely inside Fusion, with no need to touch the original USD scene over in external 3D modeling software.

### uNormalMap [uNm]

### The USD Normal Map

### Introduction

A handful of controls in the uNormalMap tool let you tweak a “normals” texture ahead of handing it to the uShader. You can therefore work the texture over in different ways and make sure it suits exactly what you need. With whatever adjustments completed, the reworked image then travels on to the uShader.

### Usage

### The uNormal Map controls

For uNormalMap, drop it in following a uTexture node and ahead of a uShader node. It functions solely in the gap between the loaded texture and uShader.

### uShader [uSd]

The USD Shader uShader Node Introduction The uShader node builds materials and looks by drawing on either the USD or the MaterialX shader tools. Paired with uReplaceMaterial, it offers a simple, intuitive path for cycling material changes onto a USD source.

### Inputs

Variable inputs on the uShader node let you bring assorted assets into the tool — a texture, say, fed through a uTexture node. As you make a connection, a drop list presents every possible connection to pick from. Attaching a texture to any input switches off that input's slider and reveals fresh Channel, Scale, and Bias controls, so you can decide which channel the property draws on along with its strength and base values.

Connect a uTexture node onto the uShader node and a drop list appears, laying out every input available to connect to.
