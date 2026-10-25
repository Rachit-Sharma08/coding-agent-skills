# Renderer3d and replace material 3D and replace normals 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Renderer3d, Replace material 3D, Replace normals 3D.
[Chapter index](INDEX.md) / [Previous section](renderer3d-anti-aliasing.md) / [Next section](replace-normals-3d-and-replicate-3d-and-ribbon-3d.md) / [Renderer3D 3Rn](projector-3d-and-renderer3d.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-control-tab"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-replace-material-3d-3rpl"></a> <a id="source-replace-material-3d-controls"></a> <a id="source-replace-material-3d-node-introduction"></a> <a id="source-replace-normals-3d-3rpn"></a> <a id="source-replace-normals-3d-controls"></a> <a id="source-replace-normals-node-introduction"></a> <a id="source-the-replace-material-3d-node"></a> <a id="source-the-replace-normals-3d-node"></a>

### Common Controls

Image and Settings Tabs The rest of the controls for the Image and Settings tabs are shared across many 3D nodes. You'll find their descriptions in the “The Common Controls” section toward the end of this chapter.

### Replace Material 3D [3Rpl]

### The Replace Material 3D node

### Replace Material 3D Node Introduction

The Replace Material 3D node swaps the material applied to every piece of geometry in the input scene for its own material input. Whatever lights or cameras sit in the input scene get passed along untouched. How far the replacement reaches can be capped through Object and Material identifiers within the Inspector. Its reach can additionally be narrowed to individual channels, which makes it feasible to apply an entirely different material on the Red channel, say. Because the Text 3D node carries no material input, you can call on the Replace Material to attach material shaders onto the text.

### Inputs

The Replace Material node carries two inputs: one for the 3D scene, object, or 3D text holding the original material, plus a material input for the fresh replacement material. SceneInput: The orange scene input takes a 3D scene or 3D text whose material you wish to swap. MaterialInput: The green material input takes either a 2D image or a 3D material. Supply a 2D image and it acts, for the node's built-in basic material, as that material's diffuse texture map. Hook up a 3D material and the basic material gets switched off.

### Basic Node Setup

The Replace Material 3D node drops in right after the 3D object or scene whose material you wish to swap. Below, it's put to work swapping the default material on a Text 3D node for a chrome shader.

Replace Material 3D swapping out the default material that sits on a Text 3D node Inspector

### Replace Material 3D controls

### Controls Tab

Enable Through this checkbox the material replacement is switched on. It isn't the same thing as the red switch up in the upper-left corner of the Inspector. That red switch shuts the tool down completely and lets the image pass through with no change. The enable checkbox is confined to the effect portion of the tool. Other portions, such as scripts in the Settings tab, keep processing as usual.

Replace Mode The Replace Mode section presents four ways to swap each RGBA channel:

- Keep: Stops the channel from getting swapped by the input material.
- Replace: Swaps the material for the matching color channel.
- Blend: Mixes the materials with one another.
- Multiply: Multiplies the channels coming from both inputs.

Limit by Object ID/Material ID Switch this on and a slider shows up where the IDs you want can be dialed in. Other objects hold on to their materials. With both options switched on, an object has to meet both conditions.

### Common Controls

Material and Settings Tabs The rest of the controls for the Material and Settings tabs are shared across many 3D nodes. You'll find their descriptions in the “The Common Controls” section toward the end of this chapter.

### Replace Normals 3D [3RpN]

### The Replace Normals 3D node

### Replace Normals Node Introduction

Within 3D modeling, normals are the vectors that establish which direction light bounces off surfaces. The Replace Normals node serves to swap the normals/tangents on incoming geometry, in effect nudging an object's surface between smooth and flat. Every piece of geometry wired to the node's scene input is touched. Lights/Cameras/PointClouds/Locators/Materials, along with other non-mesh nodes, pass through untouched. The normals/tangents this node touches are Per-vertex normals/tangents, not Per-face normals/tangents. For tangents to be worked out, the input geometry has to carry texture coordinates. At times geometry carries no texture coordinates, or the texture coordinates got set to All during the FBX import because they weren't present on the FBX.

### Inputs

For the 3D scene or incoming geometry, the Replace Normals node carries just one input. SceneInput: The orange scene input takes a 3D scene or 3D geometry holding the normal coordinates you wish to alter.

### Basic Node Setup

The Replace Normals 3D node drops in right after the 3D object or scene whose normals you wish to alter. Below, it's put to work smoothing the material on an imported 3D model.

Replace Normals 3D used to smooth normals on 3D geometry Inspector

### Replace Normals 3D controls

### Control Tab

The options within the Control tab concern repairing 3D geometry and then recalculating normals/tangents. Pre-Weld Position Vertices At times position vertices end up duplicated within a geometry despite sharing the same position, which throws off the calculation of normals/tangents. Whatever pre-welding yields gets discarded; it leaves the output geometry's position vertices untouched. Recompute Governs when normals/tangents get recalculated.

- Always: The mesh's normals get recalculated every time.
- If Not Present: The mesh's normals get recalculated solely when they're absent.
- Never: The normals never get calculated. This option proves handy while animating.

Smoothing Angle Neighboring faces whose angles in degrees fall under this value get their shared edges smoothed across. A value one would commonly pick for the Smoothing Angle sits between 20 and 60 degrees. Special-case code exists for 0.0f and 360.0f (f stands for floating-point value). Set to 0.0f, faceted normals come out; that's handy for artistic effect. Ignore Smooth Groups Set this to False and two faces carrying different Smooth Groups won't be smoothed across (for instance, a cube's faces or a cylinder's top surfaces carry different Smooth Groups). Tick this On and make the smoothing angle large enough, and a cube's faces do get smoothed across. For now there's no means of visualizing Smooth Groups inside Fusion. Flip Normals Flipping of tangents can prove confusing now and then. Flip takes effect when the mesh carries tangent vectors. Most meshes in Fusion carry no tangent vectors until they hit a Renderer 3D, though. As well, while you view tangent vectors in the viewers, those tangent vectors get made when they don't already exist. The confusing part is that if you view a Cube 3D carrying no tangent vectors and press the FlipU/FlipV button, nothing occurs. That stems from there being no tangent vectors to make, though later the GL renderer can make some (unflipped) tangent vectors. NOTE: There are five points you ought to keep in mind while dealing with normals. #1 The FBX importer recalculates the normals when they're absent, but a higher-quality result is available from the Replace Normals node. #2 Bump maps may now and then hinge on the model's normals. Specifically, after you reduce a complex high polygon model to a low polygon model + bump map, those normals together with the bump map can end up “linked.” Recalculating the normals here can make the model look odd. The bump map was meant to go with the original normals. #3 Most primitives in Fusion aren't built carrying tangents; when called for, they get built on the fly by a Renderer 3D and cached. #4 At present tangents are needed solely for bump mapping. Should a material call for bump mapping, then tangents get built. Such tangents get built using a few default settings (Smoothing Angle, and so on, for instance). If you'd rather Fusion not build tangents automatically, the Replace Normals node lets you build them by hand. #5 Every computation runs within the local coordinates of the geometries rather than within the coordinate system of the Replace Normals 3D node. That can cause trouble whenever a non-uniform scale has been applied to the geometry ahead of Replace Normals 3D being applied.
