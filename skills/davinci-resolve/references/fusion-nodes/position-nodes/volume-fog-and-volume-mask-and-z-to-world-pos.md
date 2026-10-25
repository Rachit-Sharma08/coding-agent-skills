# Volume fog and volume mask and z to world pos

Version: DaVinci Resolve 20.3 Reference Manual. Context: Volume fog, Volume mask, Z to world pos.
[Chapter index](INDEX.md) / [Previous section](volume-fog-shape-tab.md) / [Next section](z-to-world-pos-and-common-controls.md) / [Volume Fog VLF](volume-fog-shape-tab.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-camera-tab-1"></a> <a id="source-color-tab-1"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab"></a> <a id="source-examples"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-shape-tab-1"></a> <a id="source-the-volume-mask-camera-tab"></a> <a id="source-the-volume-mask-color-tab"></a> <a id="source-the-volume-mask-node"></a> <a id="source-the-volume-mask-shape-tab"></a> <a id="source-the-z-to-world-position-controls-tab"></a> <a id="source-the-z-to-world-position-node"></a> <a id="source-volume-mask-node-introduction"></a> <a id="source-volume-mask-vlm"></a> <a id="source-z-to-world-pos-node-introduction"></a> <a id="source-z-to-world-pos-z2w"></a>

### Examples

Across these examples, we view a volume from outside. To the left, you see the Volume Fog under straight accumulation. That is, the Do Lighting option has been switched off.

To the right, the same volume appears with lighting/scattering switched on and a single point light. Here the Volume grows a little more complex.

On the left, straight accumulation; in the middle, lighting, scattering, and a single point light; and on the right, the scene’s light has been repositioned, which likewise alters the volume’s appearance.

### Volume Mask [VLM]

### The Volume Mask node

### Volume Mask Node Introduction

Out of images carrying XYZ Position channels, the Volume Mask node fashions volumetric masks. One use, for instance, is isolating objects for color correction without having to track or rotoscope the scene. For a fuller account of how this technology operates and what imagery it expects, see the “WPP Concept” section appearing later in this chapter.

### Inputs

These three inputs show up on the Volume Mask node in the Node Editor: Image: A 2D image carrying a World Position Pass in the XYZ Position channels feeds the orange image input. Mask Image: To refine the mask, you can wire an image into the green mask image input. Effect Mask: A mask shape — built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools — feeds the blue input. Wiring a mask here confines the volume mask to particular regions.

### Basic Node Setup

In the example, a MediaIn labeled RGBA holds the principal rendered image drawn from a 3D scene. A World Position Pass coming from a 3D-rendered scene carries the label WPP_PASS. The Channel Booleans node maps the X position pass onto the red channel, Y onto the green channel, and Z onto the blue channel. Pulling the 3D position data out of the World Position Pass, the Volume Mask tool drops a mask into 3D space. That mask then serves as an effect mask on a color corrector, letting you selectively color correct objects within a 3D scene.

For color correction within a 3D scene, a Volume Mask tool puts the World Position Pass to work Inspector

### The Volume Mask Shape tab

### Shape Tab

How big the Volume Mask is and where it sits are governed by the Shape tab. To set the position and orientation, you may either drag the Pick buttons into the viewer or work the Translation, Rotation, and Scale controls. Shape This menu toggles between a spherical or rectangular mask dropped into your image. You can refine the mask further through the mask image input. Translation Pick Slide the Pick button into the viewer to grab XYZ coordinates off any 3D scene or 2D image carrying XYZ values, like a rendered World Pass, in order to set the Volume Mask’s center. While picking off a 2D image, confirm it’s rendered in 32-bit float so you keep full precision. X, Y, Z Offset Use these controls to set the mask’s center by hand, or animate them, or wire them to other Fusion controls. Rotation Pick Drag the Pick button into the viewer to grab rotational values off any 3D scene or 2D image carrying them, like an XYZ Normal pass, in order to reorient the mask. While picking off a 2D image, like an XYZ Normal pass, confirm it’s rendered in 32-bit float and use World Space coordinates so you keep full precision and the correct rotational values. X, Y, Z Rotation These controls spin the mask about its center. X, Y, Z Scale Stretch the mask along any axis out from its center to refine the overall Size value named below further. Size How large, across X, Y, and Z, the created mask is overall. Soft Edge Sets how strongly the Volume fades inward from its outer edge toward its center, producing a softer look.

### The Volume Mask Color tab

### Color Tab

The color and blending of the mask image are managed from the Color tab.

Color Lets you alter the color of the generated Volume Mask. This adds onto whatever color the connected mask image already supplies. Subtractive/Additive Slider As with the Merge node, this value governs whether the mask composites onto the image in Additive or Subtractive mode, yielding a brighter or dimmer mask look. Mask Only Outputs the generated mask against a black background, which can then serve as a mask on a Color Corrector for further refinement.

### The Volume Mask Camera tab

### Camera Tab

To evaluate a Volume flawlessly, you can wire a camera or 3D scene into the node’s Scene input. Camera Should the connected Scene input carry several cameras, this drop-down menu lets you choose the right one needed to evaluate the Volume. In place of wiring up a camera, position values may also be supplied by hand or by routing the XYZ values onto separate controls. Translation Pick Slide the Pick button into the viewer to grab XYZ coordinates off any 3D scene or 2D image carrying XYZ values, like a rendered World Pass, in order to set the camera’s center. While picking off a 2D image, confirm it’s rendered in 32-bit float so you keep full precision. X, Y, Z Offset Use these controls to set the camera’s center by hand, or animate them, or wire them to other Fusion controls.

### Common Controls

Settings Tab The Inspector’s Settings tab is mirrored across the other Position nodes as well. A thorough description of these common controls appears at this chapter’s close, under “The Common Controls” section.

### Z to World Pos [Z2W]

### The Z to World Position node

### Z to World Pos Node Introduction

The Z to World Pos node serves either to build a World Position Pass out of a Z channel plus a 3D Camera, or to derive a Z channel out of a World Position Pass plus a 3D Camera. Producing a World Position Pass from Z-depth comes in handy when your 3D application can’t create a WPP on its own. It’s also useful when 3D-tracking software emits a per-pixel Z-depth alongside the 3D Camera. In that way, the Volume Mask and Volume Fog can be brought to bear on real-world scenes. How good the resulting WPP turns out hinges chiefly on how good the incoming Z channel is. For a fuller account of how this technology operates and what imagery it expects, see the “WPP Concept” section.

### Inputs

These inputs show up on the node tile within the Node Editor: Image: Depending on the operation you want, the orange image input accepts an image holding either a World Position Pass or a Z-depth pass. Effect Mask: A mask shape — built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools — feeds the blue input. Wiring a mask here confines the World Position Pass to particular regions. Scene Input: A 3D scene input holding a 3D Camera connects to the magenta scene input.

### Basic Node Setup

In the example, a MediaIn labeled RGBA holds the principal rendered image drawn from a 3D scene. A Z-depth pass coming from a 3D-rendered scene carries the label Z_PASS. The Channel Booleans node maps the Aux Z channel into the red, green, or blue channel. After the Channel Booleans node comes the Z to World Position node, and an imported 3D camera matching the RGBA image is wired into the 3D camera input on the Z to World Position node. Following the Z to World Position node sits a Channel Booleans node, which can remap the X, Y, and Z positions for use by other nodes.

Out of a Z-depth pass, a Z to World Position node builds a World Position Pass Inspector

### The Z to World Position Controls tab

### Controls Tab

Whether you’re producing a World Position Pass or a Z channel is set in the Controls tab. When the connected scene holds more than one camera, this tab additionally chooses which camera drives the calculation. Mode This menu toggles between making a Z channel out of a World Position Pass or the reverse. Camera Should the connected Scene input carry several cameras, this drop-down menu lets you choose the right one needed to evaluate the image.

### Common Controls

Settings Tab The Inspector’s Settings tab is mirrored across the other Position nodes as well. A thorough description of these common controls appears at this chapter’s close, under “The Common Controls” section.
