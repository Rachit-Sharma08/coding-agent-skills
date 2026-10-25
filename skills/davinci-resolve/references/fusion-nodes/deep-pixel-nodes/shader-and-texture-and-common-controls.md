# Shader and texture and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Shader, Texture, Common controls.
[Chapter index](INDEX.md) / [Previous section](depth-blur-and-fog-and-shader.md) / [Shader Shd](depth-blur-and-fog-and-shader.md)
<a id="source-basic-node-setup-4"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-deep-pixel-nodes-part-2"></a> <a id="source-inputs-4"></a> <a id="source-inspector-1"></a> <a id="source-motion-blur"></a> <a id="source-settings-tab"></a> <a id="source-shader-tab"></a> <a id="source-texture-controls"></a> <a id="source-texture-node-introduction"></a> <a id="source-texture-tab"></a> <a id="source-texture-txr"></a> <a id="source-the-common-controls"></a> <a id="source-the-texture-node"></a>

### Shader Tab

What the Shader tab serves is adjusting the falloff of the Diffuse and Specular light along with the tint color of the specular highlight. Diffuse and Specular Switched on, these checkboxes let you edit the Diffuse and/or Specular Shader curves inside the Shader spline window. In and Out These choices serve to show and edit point values along the spline. Specular Color Lean on the Diffuse curve to shape the diffuse shading and the Specular curve to drive the specular shading. Drag a box across several points to group-select them. A right-click brings up a menu carrying choices for tuning the spline curves.

### Common Controls

Settings Tab A copy of the Settings tab in the Inspector also turns up across the other Deep Pixel nodes. Those shared controls get covered thoroughly at this chapter’s close within the “The Common Controls” section.

### Texture [Txr]

### The Texture node

### Texture Node Introduction

What the Texture node governs is the texture mapping of elements within a rendered image. The Texture node depends on U and V Map channels being present in a 3D-rendered image wired into the main Image input. Should those channels be absent, this node does nothing. NOTE: Background pixels may carry U and V values of 0.0, which pins those pixels to the color of the texture’s corner pixel. To hold texturing to particular objects, lean on an effect mask drawn from the object’s Alpha or from its Object or Material ID channel.

### Inputs

Three inputs come with the Texture node: one carrying the main image with UV map channels, one carrying a texture map image, plus another carrying an effect mask to bound the region where the replace texture lands.

Input: This orange input takes a 2D image carrying UV channels. Should the UV channels be missing from the images, this node does nothing. Texture: The green texture map input supplies the texture that gets wrapped around objects, swapping out the current texture. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the texture to just the pixels falling inside the mask. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

You slot the Texture node in after a 2D image holding a Texture UV channel. Down below, a Renderer 3D serves to attach texture coordinates onto 3D text. The Texture node can then serve to reshape those coordinates by way of a fresh texture wired into the green texture input.

A Texture node put to work reshaping the texture coordinates and laying texture onto a Text 3D node Inspector

### Texture controls

### Texture Tab

The Texture tab controls let you flip, swap, scale, and offset the UV texture image wired into the texture input. Flip Horizontal and Vertical This pair of buttons lets you mirror the texture image across its horizontal axis and/or its vertical axis. Swap UV With this checkbox ticked, the source image’s U and V channels trade places.

Rotate 90 Tick this checkbox and the texture map image turns 90 degrees. U and V Scale These controls alter the scaling of the U and V coordinates that map the texture. Shifting these values effectively grows and shrinks the texture map as it lands. U and V Offset Nudge these controls to offset the U and V coordinates. Shifting the values makes the texture appear to slide along the object’s geometry.

### Common Controls

Settings Tab A copy of the Settings tab in the Inspector also turns up across the other Deep Pixel nodes. Those shared controls get covered in the “The Common Controls” section below.

### The Common Controls

The nodes that carry out Deep Pixel compositing operations share a number of identical controls within the Inspector. What this section describes is the controls held in common across the Deep Pixel nodes.

### Inspector

### Settings Tab

The Settings tab in the Inspector shows up on every tool inside the Deep Pixel category. Those Settings controls even appear on third-party Deep Pixel-type plugin tools. The controls stay consistent and behave alike for each tool, though some tools do carry one or two individual options likewise covered here. Blend What the Blend control serves is mixing between the tool’s original image input and the tool’s final reshaped output image. With the blend value at 0.0, the outgoing image matches the incoming image. Ordinarily that makes the tool bypass processing altogether, copying the input straight across to the output. Process When Blend Is 0.0 The tool still runs even where the input value is zero. That can come in handy where this node’s processing is scripted to kick off another task, yet the node’s value sits at 0.0. Red/Green/Blue/Alpha Channel Selector These four buttons serve to hold the tool’s effect to particular color channels. This filter often gets applied once the tool has run. As an example, deselect the red button on a Blur tool, and the blur lands on the image first, after which the red channel from the original input copies back over the result’s red channel. A few exceptions exist, such as tools where deselecting these channels makes the tool bypass processing that channel altogether. The tools that behave this way generally carry an identical set of RGBA buttons on the Controls tab within the tool. Here, the buttons across the Settings and the Controls tabs match. Apply Mask Inverted Switching on the Apply Mask Inverted option flips the tool’s entire mask channel. That mask channel is the merged outcome of every mask wired into or produced within a node. Multiply by Mask Pick this option and the masked image’s RGB values get multiplied against the mask channel’s values. That drives every pixel of the image lying outside the mask (that is, set to 0) to turn black/ transparent. Use Object/Use Material (Checkboxes) Certain 3D software can render to file formats that carry extra channels. Notably, the EXR file format carries Object and Material ID channels, usable as a mask for the effect. These checkboxes decide whether those channels get used when present. Which particular Material ID or Object ID is affected gets picked through the next set of controls. Correct Edges This checkbox surfaces only where the Use Object or Use Material checkboxes are ticked. It flips the method used to cope with overlapping object edges across a multi-object image. Switched on, the Coverage and Background Color channels serve to separate and sharpen the effect around the object’s edge. Leave this option off (or have no Coverage or Background Color channels on hand) and aliasing may show along the mask’s edge. For further detail, consult Chapter 78, “Understanding Image Channels,” within the DaVinci Resolve Reference Manual; the same material sits at Chapter 18 of the Fusion Reference Manual.

Object ID/Material ID (Sliders) Lean on these sliders to pick which ID builds a mask from an image’s object or material channels. Work the Sample button the same way as the Color Picker: to lift IDs off the image shown in the viewer. The image or sequence has to have been rendered out of a 3D software package carrying those channels. Use GPU The Use GPU menu carries three settings. Setting the menu to Disable shuts off hardware-accelerated rendering by way of your computer’s graphics card. Enabled puts the hardware to work. Auto draws on a capable GPU where one exists, yet drops back to software rendering when no capable GPU is on hand.

### Motion Blur

- Motion Blur: This switches the tool’s Motion Blur rendering on or off. With the control enabled, the blur is generated from the tool’s estimated motion as it would appear through the virtual camera’s shutter. Leave the control disabled and nothing is blurred.
- Quality: This figure sets how many samples go into building the blur. Choosing a value of 2 for example prompts Fusion to lay down a pair of samples on each flank of an object’s true path. Bigger numbers yield cleaner output at the cost of longer renders.
- Shutter Angle: This dictates how wide the virtual shutter opens while the motion blur effect is generated. Wider angles yield heavier blur while pushing render times up. Setting it to 360 matches a shutter held open across one entire frame of exposure. You may go beyond that, which opens the door to some interesting effects.
- Center Bias: This shifts where the midpoint of the motion blur falls, making motion-trail looks achievable.
- Sample Spread: Tweaking this control changes how heavily each sample counts, which in turn alters how bright the samples appear.

Comments The Comments field lets you attach notes to a tool. Click inside the field and enter your text. Once a tool carries a note, a tiny red square shows up in the node’s lower-left corner while the full tile is on screen, or a little text-bubble icon shows on the right side once nodes are collapsed. Hovering the mouse pointer over the node surfaces the tooltip so you can read the note inside the Node Editor. Scripts Every Fusion tool offers three Scripting fields, reached through the Settings tab. Each one holds an edit box where you can drop scripts that run while the tool renders. Turn to the Fusion scripting documentation if you need fuller detail on scripting nodes.
