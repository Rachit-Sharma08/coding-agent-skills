# Falloff and fast noise texture and gradient 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Falloff, Fast noise texture, Gradient 3D.
[Chapter index](INDEX.md) / [Previous section](catcher-and-cubemap-and-falloff.md) / [Next section](gradient-3d-and-sphere-map.md) / [Falloff 3Fa](catcher-and-cubemap-and-falloff.md)
<a id="source-basic-node-setup-4"></a> <a id="source-basic-node-setup-5"></a> <a id="source-color-variation"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-controls-tab-3"></a> <a id="source-controls-tab-4"></a> <a id="source-falloff-controls"></a> <a id="source-fast-noise-texture-3fn"></a> <a id="source-fast-noise-texture-controls"></a> <a id="source-fast-noise-texture-node-overview"></a> <a id="source-gradient-3d-3gd"></a> <a id="source-gradient-node-overview"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-output-mode"></a> <a id="source-the-fast-noise-texture-node"></a> <a id="source-the-gradient-node"></a>

### Inspector

### Falloff controls

### Controls Tab

The parameters across the Controls tabs tune the tint and opacity belonging to the Face On material as well as the Glancing material. The blend between the pair is governed by a Falloff slider.

### Color Variation

- Two Tone: A pair of ordinary Color controls set the Glancing and Face On colors.
- Gradient: One Gradient control sets the Glancing and Face On colors. You can put this toward all kinds of effects—building Toon Shaders, for one.

Face On Color The Face On Color sets the color of the surface parts that face the camera. When a Face On texture map is supplied, the color value you give here is multiplied against the texture's color values. Dialing back the material's opacity lowers the color and Alpha values of the Face On material, turning the material transparent. Glancing Color The Glancing Color sets the color of the surface parts more perpendicular to the camera. When the Glancing material port has a valid input, that input is multiplied by this color. Dialing back the material's opacity lowers the color and Alpha values of the Glancing material, turning the material transparent. Falloff This value governs the transition between Glancing and Face On strength. It behaves much like a gamma operation laid on a gradient, blending one value into another. Material ID This slider fixes the numeric identifier handed to this material. The value is rendered into the MatID auxiliary channel if the matching option is switched on in the renderer.

### Common Controls

Settings Tab Across the other 3D nodes the Inspector’s Settings tab is mirrored. The complete account of these common controls sits near the chapter’s finish in the “The Common Controls” section.

### Fast Noise Texture [3FN]

### The Fast Noise Texture node

### Fast Noise Texture Node Overview

The Fast Noise Texture node is the procedural, resolution-independent counterpart to the 2D Fast Noise node. It generates a noise texture straight away as a material for use with 3D nodes. It also offers a 3D volumetric mode for building seamless textures together with nodes that supply UVW texture coordinates (much like the UV Map 3D node set to XYZ-to-UVW or Camera).

### Inputs

The Fast Noise Texture node carries an optional input for hooking up a 2D image or material. SourceMaterial: The Source Materials input takes a 2D image or a 3D material. That image is then reshaped by the noise pattern.

### Basic Node Setup

The Fast Noise Texture node below serves to generate a resolution-independent 3D texture for an FBX imported model.

A Fast Noise Texture node builds a seamless texture, putting UVW coordinates to use.

### Inspector

### Fast Noise Texture controls

### Controls Tab

The parameters of the Fast Noise Texture node govern the look and, in 2D, the animation of the noise.

### Output Mode

- 2D: Works out the noise texture from 2D texture coordinates (UV). Under this setting the noise pattern can be varied smoothly through animation.
- 3D: Works out the noise texture from 3D texture coordinates (UVW). A node such as Shape 3D supplies a third texture coordinate on its own; failing that, the UV Map node can build a 3D texture space. With the 3D setting, animating the noise pattern isn't supported.

Detail Raise this slider's value to coax a finer level of detail out of the noise result. Bigger values stack on more layers of increasingly detailed noise without touching the overall pattern. High values take longer to render yet can yield a more natural result (not every graphics card supports higher detail levels in hardware). Brightness This control tunes the overall Brightness of the noise map. Contrast This control raises or lowers the overall Contrast of the noise map. It can play up the noise's effect. Scale The Scale slider lets you size the noise map, shifting it from gentle variation across the whole image to a tighter overall texture effect. This value represents how the noise scales along the UV axis. Scale Z (3D only) Within texture space, the Scale Z value scales the noise texture along the W-axis. For a 3D texture map, W points perpendicular to the UV plane. Seethe (2D only) Through the Seethe control, the 2D noise pattern varies smoothly. Seethe Rate (2D only) Like the Seethe control above, the Seethe Rate likewise makes the noise map evolve and shift. The Seethe Rate fixes how fast the noise changes each frame, driving an automatic animated drift in the noise with no need for spline animation. Discontinuous Ordinarily, the noise function interpolates between values to form a smooth continuous gradient of results. Tick the Discontinuous checkbox to carve hard discontinuity lines along some of the noise contours. The upshot is a dramatically different effect. Invert Tick the Invert checkbox to invert the noise, producing a negative image of the original pattern. This works best with Discontinuous switched on too. Material ID This slider fixes the numeric identifier handed to this material. The value is rendered into the MatID auxiliary channel if the matching option is switched on in the renderer.

### Common Controls

Settings Tab The Settings tab found in the Inspector recurs throughout the other 3D nodes. Look for a detailed treatment of these common controls at the chapter’s tail end in the “The Common Controls” section.

### Gradient 3D [3Gd]

### The Gradient node

### Gradient Node Overview

The Gradient 3D node serves to texture objects with an assortment of gradient types. It carries many of the same controls as the Background node. Although the gradient can't be transformed directly within 3D space, it can be oriented with the nodes below: Texture Transform Node: The Texture Transform node can tune the mapping per pixel. UV Map Node: The UV Map node can tune the mapping per vertex (use the XYZtoUVW mode). It carries onscreen controls, so you can watch what the gradient is doing. Reaching for this node is the recommended route since it evaluates faster. Out of the box the gradient is linear, sweeping from -1 to +1 along the Z-axis. For UVW mapping, each primitive within the Shape 3D node is able to emit a third texture coordinate.

### Inputs

The Gradient node has no Inputs. The node's output wires into a material input on 3D geometry.

### Basic Node Setup

The Gradient 3D node below produces a resolution-independent 3D texture for an FBX imported model. Placing a UV Map tool after the geometry makes positioning within UVW space easiest.

A Gradient 3D node producing a resolution-independent gradient texture, placed by the UV Map tool
