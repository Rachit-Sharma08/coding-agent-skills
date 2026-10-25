# Lighting hierarchies and shadow maps

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](camera-view-focus-plane-and-depth-of-field.md) / [Next section](attenuation-and-alpha-detail.md)
<a id="source-3d-compositing-basics-part-3"></a> <a id="source-alpha"></a> <a id="source-diffuse"></a> <a id="source-force-all-materials-non-transmissive"></a> <a id="source-hard-shadow-cast-by-a-spotlight"></a> <a id="source-lighting-hierarchies"></a> <a id="source-material-components"></a> <a id="source-material-examples-from-the-bin"></a> <a id="source-materials-and-textures"></a> <a id="source-multiplicative-and-additive-bias"></a> <a id="source-opacity"></a> <a id="source-shadow-maps"></a> <a id="source-shadow-softness"></a> <a id="source-soft-shadow-controls-in-the-control-panel"></a> <a id="source-specular"></a>

### Lighting Hierarchies

Lights ordinarily stay on their side of a Merge, because the Pass Through Lights checkbox is off by default. That gives you a way to govern which objects are lit by which lights. Take the two node trees below, where two shapes and an ambient light feed a Merge3D node, which then connects to a second Merge3D node that also takes a plane and a spotlight. On the left, this tree's first Merge3D node has Pass Through Lights off, so only the two shapes show up lit. On the right, Pass Through Lights is on, so both the foreground shapes and the background image plane get lit.

With Pass Through Lights off, only the two front shapes light up (left); with Pass Through Lights on, every shape wired to both Merge3D nodes lights up (right) Lighting Options Most geometry-generating nodes carry extra options for lighting. These options set how each individual object responds to lights and shadows in the scene.

- Affected By Lights: With the Affected By Lights checkbox on, scene lights act on the geometry.
- Shadow Caster: When on, the object throws shadows onto other objects in the scene.
- Shadow Receiver: With this checkbox on, the object takes on shadows.

3D objects have individual lighting controls that govern how each object responds to light and shadows Shadows Spotlight, Point Light, and Directional light are all capable of casting shadows in the 3D viewer, though Point and Directional lights require the Renderer3D node's Rendering Type to be Hardware Renderer. Spotlight runs with either the Hardware or Software renderers. By default these lights cast shadows, yet those shadows stay hidden in the viewer until you switch shadows on with the viewer toolbar button. Nor will shadows turn up in the Renderer3D output unless the Shadows option is on for that renderer. To keep a spotlight from casting shadows, turn off the Enable Shadows checkbox in the node's Inspector.

An image with spotlight casting a variable soft shadow

To read more about shadow controls, consult the "Spotlight" section within Chapter 90, "3D Light Nodes," of the DaVinci Resolve Reference Manual, or Chapter 30 of the Fusion Reference Manual.

### Shadow Maps

A shadow map is an internal depth map recording every pixel's depth within the scene. That data drives the assembly of the shadow layer a spotlight produces. You will find all the shadow map controls in the Spotlight Inspector. Shadow quality leans heavily on the shadow map's size. Bigger maps make better-looking shadows but lengthen render times. The broader the spotlight's cone, or the more falloff it has, the bigger the shadow map must be for usable quality. The Shadow Map Size control's value fixes the depth map's size in pixels. As a rule, trial and error reveals a point of diminishing returns past which enlarging the shadow map stops improving the shadow. Making shadow maps any bigger than necessary is not advised. The Shadow Map Proxy control sets a percentage by which the shadow map is scaled for quick interactive previews such as Autoproxy and LoQ renders. A value of 4, say, equals a 40% proxy.

### Shadow Softness

By default, the spotlight makes shadows with hard edges, but options exist for constant and variable soft shadows. Hard-edged shadows render markedly faster than either Soft Shadow option. Shadows lacking softness usually look aliased unless the shadow map size is big enough. Often, softness is brought in to mask the aliasing instead of enlarging the shadow map, which conserves memory and avoids overrunning the graphics hardware's limits.

### Soft Shadow controls in the Control panel

Set the spotlight's shadow softness to None and you get crisp, sharply defined shadows. The Constant option produces shadows whose softness is even throughout, no matter the shadow's distance from the casting geometry. The Variable option produces shadows that grow softer the farther they sit from the geometry casting them. That looks more realistic, though such shadows are a bit trickier to control. Choosing this option brings up extra controls for tuning the shadow's falloff, along with sliders for minimum and maximum softness.

### Hard shadow cast by a spotlight

Choosing the Variable option exposes the Spread, Min Softness, and Filter Size sliders. One side effect of the technique behind variable softness shadows is that the blur applied to the shadow map can grow effectively boundless as the shadow's distance from the geometry rises. These controls rein the shadow map in by capping the softness calculation at a sensible limit. Where that limit kicks in is set by the filter size. A larger filter size raises the shadow's greatest possible softness. Shrinking it can trim render times yet may also cap the shadow's softness or even clip it. As a value, it is expressed as a percentage of the shadow map size. For further detail, consult "Spotlight" within Chapter 90, "3D Light Nodes," of the DaVinci Resolve Reference Manual, or Chapter 30 of the Fusion Reference Manual.

### Multiplicative and Additive Bias

Shadows are basically textures laid onto objects in the scene, and now and then they "fight." Z-fighting crops up when parts of an object that ought to receive shadows instead render on top of the shadow, because they sit at the very same spot in 3D space.

What shadow map Z-fighting produces (Left), alongside the shadow corrected via Biasing (Righht)

In the Shadows group of Spotlight parameters, two Biasing sliders operate by nudging a small depth offset that pulls the shadow off the surface it shadows, clearing the Z-fighting. Too little bias and objects may shadow themselves. Too much and the shadow may pull away from the surface.

The Spotlight Inspector controls hold the Multiplicative and Additive Bias sliders together with the Non-Transmissive Materials checkbox Aim to move the Multiplicative Bias slider until most of the Z-fighting clears, then move the Additive Bias slider to wipe out what is left. A softer shadow will likely demand a higher bias. For some especially stubborn frames you may even have to animate the bias to land a proper result.

### Force All Materials Non-Transmissive

The way light travels through a semi-transparent material weighs heavily on how the shadow an object casts looks. This transmittance behavior is normally set in each object's Materials tab. Choosing Force All Materials Non-Transmissive in the Spotlight Inspector, however, overrides that, so the shadow map the node produces disregards transmittance altogether.

### Materials and Textures

Rendering a 3D scene requires the renderer to weigh both an object's shape and its appearance. An object's geometry sets its shape, while the material on the object sets its appearance. Fusion offers an assortment of ways to put materials and textures onto geometry, letting you hand your 3D objects whatever surface qualities you want. Nodes that spell out how the geometry answers to light go by the name illumination models. The illumination models bundled in are Blinn, CookTorrance, Ward, and Phong. You will find these nodes under the 3D > Material category of nodes in the Effects Library. Most materials take textures too, which are usually 2D images. Textures sharpen an object's look further by layering on photorealistic detail, transparency, or special effects. More involved textures such as bump maps, 3D textures, and reflection maps live in the 3D > Texture category as well. Materials can also be stacked to form elaborate, richly detailed composite materials. Every node that builds or loads geometry into a 3D scene also hands it a default material. That default is the Blinn illumination model, but you can replace it with one of several nodes that output a 3D material. A few of these materials grant finer control over how the geometry answers to light, offering inputs for diffuse and specular texture maps, bump mapping, and environmental maps that imitate reflection and refraction.

### Material examples from the bin

### Material Components

Every standard illumination model has traits in common that are worth grasping.

### Diffuse

A material's Diffuse parameters govern how an object looks where light is soaked up or scattered. This diffuse color and texture form an object's base look before reflections enter in. An object's opacity is usually set in the material's diffuse component.

### Alpha

The Alpha parameter sets how transparent the object is to diffuse light. It leaves specular levels and color alone. Yet should alpha's value, whether from the slider or a Material input from the diffuse color, sit at or very near zero, those pixels, the specular highlights among them, get skipped and vanish.

### Opacity

The Opacity parameter dims the entire material, the specular highlights included. This value cannot be mapped; it acts on the whole material.

### Specular

A material's Specular parameters govern the highlight of an object where light bounces toward the current viewpoint. The result is a highlight laid on top of the diffuse component. The more specular a material, the glossier it reads. Surfaces such as plastics and glass usually carry white specular highlights, whereas metallic surfaces like gold carry specular highlights that tend to pick up their color from the material color. Specularity comprises color, intensity, and exponent. The specular color decides the color of light reflecting off a shiny surface. Specular intensity sets how bright the highlight is.

Three spheres, left to right: diffuse only, specular only, and combined What the specular exponent governs is the falloff of the specular highlight. Push the value higher and the falloff grows sharper while the specular component shrinks.

Left to right: white, complimentary, and matching specular colors Transmittance With the software renderer, the Transmittance parameters set how light travels through a semi-transparent material. As an illustration, a solid blue pitcher throws a black shadow, whereas one built from translucent blue plastic would throw a far lower density blue shadow. Those transmittance parameters are vital to conjuring the look of stained glass.

TIP: A material’s opacity and transmittance can be tuned independently of each other. A surface can be fully opaque and yet pass 100% of the light that lands on it, so in a way it acts as a luminous/emissive surface. Transmissive surfaces can be reined in further by way of the Alpha and Color Detail control.
