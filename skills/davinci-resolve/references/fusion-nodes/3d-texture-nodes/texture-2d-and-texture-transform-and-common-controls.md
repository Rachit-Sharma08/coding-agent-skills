# Texture 2D and texture transform and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Texture 2D, Texture transform, Common controls.
[Chapter index](INDEX.md) / [Previous section](sphere-map-and-texture-2d.md) / [Next section](common-controls-settings-tab.md) / [Texture 2D 3Tx](sphere-map-and-texture-2d.md)
<a id="source-basic-node-setup-1"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-1"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-texture-2d-controls"></a> <a id="source-texture-transform-3tt"></a> <a id="source-texture-transform-controls"></a> <a id="source-texture-transform-node-overview"></a> <a id="source-the-common-controls"></a> <a id="source-the-texture-transform-node"></a>

### Inspector

### Texture 2D controls

### Controls Tab

The Inspector's Controls tab carries these options. U/V Offset Use these sliders to shift the texture along the U and V coordinates. U/V Scale Use these sliders to resize the texture along the U and V coordinates.

Wrap Mode When a texture gets transformed within the texture space (via the controls below or the UV Map node), regions beyond the image borders might end up mapped onto the object. The Wrap Mode dictates how the image fills those regions.

- Wrap: This folds the picture's edges around onto the image's borders.
- Clamp: Texturing draws on the color found at the edges of the images. The behavior here resembles the

Duplicate mode in the Transform node.

- Black: Along its borders the image gets clipped, with a black color at Alpha = 0 substituted there.
- Mirror: The image is mirrored in both X and Y.

Texture Filtering Mode How the texture gets filtered varies depending on whether the Renderer 3D node is set to the Software Renderer or the OpenGL renderer. Inside either render engine you can pick high-quality anti-aliasing or low quality. The texture filtering mode supplies distinct filtering choices across the two render engines and the two anti-aliasing settings.

- Nearest: As the most basic filtering approach, it runs very fast but may introduce artifacts as textures are scaled.
- Bilinear: A conventional isotropic filtering approach for resampling textures across several resolutions.

Works well for magnification of textures.

- Trilinear: A step up from Bilinear filtering. Trilinear is usually the stronger pick when

scaling down textures

- Anisotropic: The top-quality filtering approach, which factors in the camera orientation along with polygon

perspective into account.

- SAT: SAT (Summed Area Table) delivers high-quality filtering, though it may demand

more memory than other options. Works very well on smaller bitmaps.

### Common Controls

Settings Tab The Inspector's Settings tab repeats across the other 3D nodes. Full descriptions of these shared controls appear later in this chapter under the "The Common Controls" section.

### Texture Transform [3TT]

### The Texture Transform node

### Texture Transform Node Overview

You can rely on the Texture Transform node to translate, rotate, and scale a 3D object's UVW texture coordinates. Although its input may also be an image, what it outputs is always a material.

### Inputs

The Texture Transform node carries a lone input where you attach the image or material you intend to transform. Material Input: The orange Material input takes a 2D image or 3D material whose texture coordinates get transformed by the controls in the Inspector.

### Basic Node Setup

In the example below, the Texture Transform node accepts a 2D image, transforms it, and emits a material destined for use on 3D geometry.

A Texture Transform node transforms a texture applied to 3D geometry.

### Inspector

### Texture Transform controls

NOTE: Not all Wrap modes are supported by all graphics cards.

### Controls Tab

The Controls tab for the Texture Transform node carries plenty of standard transform controls for transforming the texture through UVW coordinates. Translation The U, V, W translation sliders move the texture along the U, V, and W axes. Rotation Rotation Order buttons fix the sequence in which the rotation gets applied. Together with those buttons, the UVW dials set the rotation around the UVW axes. Scale U, V, W sliders resize the texture along the UVW axes. Pivot U, V, W Pivot establishes the anchor point used for rotation and scaling. Material ID This slider assigns the numeric identifier given to this material. The value gets rendered into the MatID auxiliary channel whenever the matching option is switched on in the renderer.

### Common Controls

Settings Tab The Inspector's Settings tab repeats across the other 3D nodes. Full descriptions of these shared controls appear in the "The Common Controls" section that follows.

### The Common Controls

Nodes that work with 3D geometry share a set of identical controls within the Inspector. This section covers the controls common to the 3D Texture nodes.
