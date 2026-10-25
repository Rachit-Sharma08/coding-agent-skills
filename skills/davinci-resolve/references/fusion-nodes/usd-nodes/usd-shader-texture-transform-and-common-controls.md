# Ushader and utexture and utexturetransform and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ushader, Utexture, Utexturetransform, Common controls.
[Chapter index](INDEX.md) / [Previous section](usd-lights-normalmap-and-shader-nodes.md) / [uShader uSd](usd-lights-normalmap-and-shader-nodes.md)
<a id="source-basic-node-setup"></a> <a id="source-controls"></a> <a id="source-inputs-7"></a> <a id="source-inspector-6"></a> <a id="source-introduction-1"></a> <a id="source-settings-tab"></a> <a id="source-shader-model"></a> <a id="source-shader-model-materialx"></a> <a id="source-shader-model-usd"></a> <a id="source-the-common-controls"></a> <a id="source-the-usd-texture"></a> <a id="source-the-usd-texture-transform"></a> <a id="source-the-ushader-controls-in-materialx-mode"></a> <a id="source-the-ushader-controls-in-usd-mode"></a> <a id="source-the-utexture-controls"></a> <a id="source-the-utexture-transform-controls"></a> <a id="source-transform-tab"></a> <a id="source-usage-1"></a> <a id="source-usage-2"></a> <a id="source-utexture-utx"></a> <a id="source-utexturetransform-utxf"></a>

### Basic Node Setup

Here the uShader takes an input off the uTexture node, alters that texture, and then forwards it to the uReplace Material node. uReplace Material, in turn, is choosing particular materials out of the MonsterJumpDown USD scene onto which the freshly altered texture gets applied.

### Inspector

### The uShader controls in USD mode

### Shader Model

This is where you decide which toolset to use, picking the USD tools or the MaterialX tools.

### Shader Model: USD

Diffuse Mode Diffuse captures a surface's underlying qualities on their own, leaving out extras such as reflections or specular highlights.

- Color: Supplies controls for changing the shape's diffuse color. Emissive Emissive lays a scene-wide lighting effect onto a shape, building a coat of color above the texture already there. You can take it to varying intensities, and it serves to fake the emission of light.

Workflow Mode Lets you toggle the mode between Metallic and Specular.

- Metallic: Switch this on and the Metallic slider appears. That slider lends objects a reflective character, giving them a metal-like look by boosting how reflective a shape is.
- Specular: Switch this on and the Specular Color controls surface. Specular Color fixes the color of the light bouncing off a glossy surface; the more specular a material gets, the shinier it looks.

Roughness Shapes how much light a surface reflects and scatters, so depending on the value the result looks smoother or more textured; it's central to believable reflections. Clearcoat Alters a surface's look by stacking a glossy layer above it, imitating a protective coating, and it sees frequent use for materials such as car paint or polished metal. Clearcoat Roughness Tunes how flawed or how smooth that overlaid glossy layer is, which can sway the realism and reflectivity of materials like car paint or polished metal. Opacity Lowers the opacity of both material and object, affecting the shape's color and Alpha values.

### Shader Model: MaterialX

### The uShader controls in MaterialX mode

### Controls

An open standard kept up by the Academy Software Foundation, MaterialX exists for authoring material and look-development content in a platform-independent way. It evolves continually, and the most recent specifications live on the MaterialX website: materialx.org

### uTexture [uTx]

### The USD Texture

### Introduction

When you want to make a material/surface inside the uShader, this tool is what brings a texture file in. The uTexture pulls in image files and turns them into the material/surface over in the uShader.

### Inputs

Image Input: As you put a texture on a USD object — or light a scene by way of uDomeLight — the Image Input pulls frames from whatever Fusion node is already there. So in place of a pre-rendered image for the texture, you may rely on Fusion tools, video inputs and generated graphics included. With it connected, the Inspector tucks away the File Name control, and the Image Input takes precedence over any image file sourced earlier. Run a node into the Image Input of uShape or uReplaceMaterial and the picture comes through as a diffuse texture. The File Name path stops at a lone frame for a texture, but the Image Input unlocks animated textures, which grants more room to maneuver in lighting and texturing.

### Usage

### The uTexture controls

Once the node sits in the Node Editor, click the Browse button to pick an image file off your hard drive. As another route, drag an image straight from the Media Pool onto the “File Name” control in the Inspector to load one that's already been brought into DaVinci Resolve.

The “Source Color Space” control governs how the uTexture tool interprets the image. For the best outcome with a Normals image, be sure to choose Linear. Meanwhile, the U/V Address Mode controls give you a handy say over what happens to the image's edges when scaling leaves them exposed.

### uTextureTransform [uTXF]

### The USD Texture Transform

Introduction uTextureTransform hands you fine-grained command over the scale, rotation, and position of every texture file you've loaded. Using uTexture Transform, the size, orientation, and placement of any texture file coming from the uTexture node are quick and simple to adjust.

### Usage

### The uTexture Transform controls

With uTextureTransform, position it just past a uTexture node and just ahead of a uShader node. The node operates only in the span between the loaded texture and uShader. Set the Scale, Rotation, and Position settings however suits you. Scale grows or shrinks the texture file's size, whereas Position shifts the file about inside your project. Rotation, for its part, turns the texture file to whatever angle you have in mind.

### The Common Controls

A number of the same Inspector controls show up on every node that performs USD operations. What this section covers are those controls shared across the USD nodes.

### Transform Tab

Most USD nodes carry the Transform tab within the Inspector. Its controls mirror those of the uTransform node, which you can also use on its own. Translation Transform controls place the USD shape within 3D space. Rotation Order These buttons let you choose the sequence in which rotation is applied along each of the object's axes. XYZ, for instance, rotates the X-axis first, the Y-axis next, and the Z-axis last. Rotation These controls spin the shape about its pivot point. Tick the Use Target checkbox and the rotation references the target's position; leave it clear and the global axis governs instead. Pivot The pivot point is whatever an object turns around. Ordinarily an object turns about its own center, taken as a pivot of 0,0,0, but these controls can shift the pivot away from center. Scale With the Lock X/Y/Z checkbox ticked, you get one scale slider that resizes the object as a whole. Clear that Lock checkbox and separate X, Y, and Z sliders appear, opening up scaling along any dimension.

### Settings Tab

Every tool in the USD category carries the Settings tab in the Inspector, and its controls stay uniform, behaving identically from tool to tool. Hide Incoming Connections Tick this checkbox to conceal the connection lines coming in from upstream nodes, which tidies up a node tree and makes it easier to follow. Once it's on, the Inspector shows an empty field for each of a node's inputs. Drag a connected node out of the node tree into that field and the incoming connection line disappears, so long as the node stays unselected in the node tree; select it there and the line returns. Comments You jot notes onto a tool through the Comments field. Click the empty field and type your text. After a note goes on a tool, a little red square shows at the node's lower-left corner while the full tile is on view, or a small text bubble icon turns up on the right when nodes are collapsed. To read the note in the Node Editor, hover the mouse pointer over the node and the tooltip appears. Scripts From the Settings tab, three Scripting fields are present on every Fusion tool. Each holds an edit box where you enter scripts that run as the tool renders. For fuller detail on scripting nodes, turn to the Fusion scripting documentation.
