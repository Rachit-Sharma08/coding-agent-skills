# Urenderer and ureplacematerial and ushape

Version: DaVinci Resolve 20.3 Reference Manual. Context: Urenderer, Ureplacematerial, Ushape.
[Chapter index](INDEX.md) / [Previous section](urenderer-image-tab.md) / [Next section](ushape-and-uswitch-and-utransform.md) / [uRenderer uRn](urenderer.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-the-ureplacematerial-controls"></a> <a id="source-ureplacematerial-urm"></a> <a id="source-ushape-ush"></a>

### Common Controls

Settings Tab Other USD nodes carry a duplicate of the Inspector's Settings tab as well. Full descriptions of these common controls appear in this chapter's closing "The Common Controls" section.

### uReplaceMaterial [uRM]

The uReplaceMaterial node uReplaceMaterial Node Introduction With the uReplaceMaterial node you can swap an object's material for a new one. That new material may be a standard color material, a texture file, or a MaterialX file. You can apply it to every object in the scene, or confine it to particular objects via the Prim Selection controls.

### Inputs

Two inputs feed the uReplaceMaterial node. Scene Input: A USD scene file from a uLoader tool is what the yellow input takes in. Material Input: Material files arrive at the green input from assorted tools such as uMaterialX, uShader, or even pulled from a separate USD scene through a uLoader tool. Image Input: Whether you're texturing a USD object or lighting a scene with uDomeLight, the Image Input lets you draw frames from any existing Fusion node. That hands you the choice of feeding in Fusion tools (video inputs and generated graphics among them) rather than a pre-rendered image to serve as a texture. Once it's connected, the Inspector hides the File Name control, and the Image Input takes precedence over whatever image file was previously sourced. Tying a node to the Image Input on uShape or uReplaceMaterial lays the image down as a diffuse texture. Where the File Name option only sources a single frame as a texture, the Image Input opens the door to animated textures, lending more flexibility to lighting and texturing.

### Basic Node Setup

Connect the material output to the rest of the USD tools.

A straightforward node tree where a uReplaceMaterial tool receives input from a USD scene named Walkstop, swaps out a material in that scene, and then hands the scene off to a uTransform node so its transform parameters can be tweaked.

### Inspector

### The uReplaceMaterial controls

### Controls

With the uReplaceMaterial controls you alter which materials a USD scene uses.

- Prim Selection: Pick brings up the Scene Tree window, where you single out particular materials or objects within a USD scene.

Invert Prim Selection: Tick this box and the Prim Selection inverts, leaving out the materials or objects sitting in the Selected Prims box.

- Type: Choose which kind of material should take the original's place.

Color: Picks a standard Color material and opens the color controls. Texture: Brings up a file requester for loading a texture file. MaterialX: Brings up a file requester for loading a MaterialX file, or for choosing a Material from a file tied to the node's green Material input. Pick this option and every other control closes.

- Diffuse: Lets you recolor the material or load a texture.

Color: Brings up a standard color picker for choosing the material's new color. Red: Tunes how much red is in the Material. Green: Tunes how much green is in the Material. Blue: Tunes how much blue is in the Material.

- Emissive: Emissive lends a shape a global lighting effect, laying a color layer over the texture already there. Its intensity is adjustable across various levels, and it serves to mimic the emission of light.

Color: Brings up a standard color picker for choosing the lighting's new color. Red: Tunes how much red is in the lighting. Green: Tunes how much green is in the lighting. Blue: Tunes how much blue is in the lighting.

- Workflow Mode: Lets you set the mode between Metallic and Specular.
- Metallic: Once enabled, this control reveals the Metallic slider. That slider lends objects a reflective

character, conjuring the look of metal and boosting a shape's reflective properties.

- Specular: Once enabled, this surfaces the Specular Color controls. Specular Color fixes the color of light bouncing off a shiny surface; the more specular the material, the glossier its look.
- Roughness: Shapes how much light a surface reflects and scatters, lending it a smoother or rougher appearance per the setting. It's central to producing believable reflections.
- Clearcoat: Alters a surface's look by laying a glossy layer over it, imitating a protective coating. Materials such as car paint or polished metal commonly use it.
- Clearcoat Roughness: Dials in how flawed or smooth that overlaid glossy layer appears. It can sway the realism and reflection of materials like car paint or polished metal.
- Opacity: Cuts the opacity of the material and object, affecting the shape's color and Alpha values.
- Opacity Threshold: Tunes the point at which opacity begins showing.

### Common Controls

Settings Tab The Inspector's Settings tab is replicated across other USD nodes too. You'll find these common controls covered thoroughly within the "The Common Controls" section that closes this chapter.

### uShape [uSh]

The USD Shape node uShape Node Introduction The uShape node serves to generate a handful of basic primitive 3D shapes, among them capsule, torus, planes, cubes, spheres, and cylinders.

### Inputs

Image Input: As you texture a USD object — or light a scene using uDomeLight — the Image Input makes it possible to pull frames out of any existing Fusion node. This lets you supply Fusion tools (such as video inputs and generated graphics) in place of a pre-rendered image to act as a texture. After connection, the Inspector's File Name control disappears, and the Image Input supersedes any image file sourced earlier. Hooking a node up to the Image Input on uShape or uReplaceMaterial puts the image down as a diffuse texture. Whereas the File Name option draws in just one frame as a texture, the Image Input makes animated textures possible, granting added flexibility in lighting and texturing.

### Basic Node Setup

The uShape node turns out a 3D shape that's then merged with a uCamera node so you can adjust the view.
