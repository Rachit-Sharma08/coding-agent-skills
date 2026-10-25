# Sphere map and texture 2D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sphere map, Texture 2D.
[Chapter index](INDEX.md) / [Previous section](sphere-map-basic-node-setup.md) / [Next section](texture-2d-and-texture-transform-and-common-controls.md) / [Sphere Map 3SpM](gradient-3d-and-sphere-map.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-sphere-map-controls"></a> <a id="source-spherical-mapping-differences"></a> <a id="source-texture-2d-3tx"></a> <a id="source-texture-node-overview"></a> <a id="source-the-texture-2d-node"></a>

### Inspector

### Sphere Map controls

### Controls Tab

The Controls tab in the Inspector governs how the image input is mapped onto the sphere map. Angular Mapping Tweaks the texture coordinate mapping so the poles look less squashed and regions of the texture cover equal-area patches on the sphere. It converts the latitude-line mapping from a hemispherical fisheye into an angular fisheye. Because this mapping tries to keep area constant, it becomes simpler to paint over or alter a sphere map, since the image isn't as crowded at the poles. Rotation Provides controls for spinning the texture map. Material ID This slider assigns the numeric identifier given to this material. The value gets rendered into the MatID auxiliary channel whenever the matching option is switched on in the renderer. The node looks for an image whose aspect ratio is 2:1. If that isn't the case, the image gets clamped per these rules:

- 2 \* width > height: The width gets sized to the sphere, leaving clamped edges showing at the poles.
- 2 \* width < height: The height gets sized to the sphere, with clamping occurring around the 0-degree

longitude line.

### Common Controls

Settings tab The Inspector's Settings tab repeats across the other 3D nodes. Full descriptions of these shared controls appear later in this chapter under the "The Common Controls" section.

Sphere Map vs. Connecting the Texture to a Sphere Directly Rather than routing it through the Sphere Map node first, you can hook an equirectangular texture map straight to a sphere. Doing so renders differently once you drop the start/end angle and latitude below 360°/180°. In the former scenario the texture ends up squashed. With the Sphere Map node in place, the texture is cropped instead. Compare:

### Spherical mapping differences

NOTE: Feeding the texture straight into the sphere also flips it horizontally. To undo that, run it through a Transform node first.

### Texture 2D [3Tx]

### The Texture 2D node

### Texture Node Overview

The Texture 2D node writes metadata for an image that's serving as a texture map. By default an image spans (0,0) to (1,1) UV, although you can change that. The Texture node depends on U and V Map channels being present within 3D rendered images. Without those channels, this node does nothing. NOTE: Background pixels can carry U and V values of 0.0, which paint those pixels with the color of the texture's corner pixel. To confine texturing to particular objects, apply an effect mask keyed to the object's Alpha, or to its Object or Material ID channel.

Further detail lives in the DaVinci Resolve Reference Manual under Chapter 78, "Understanding Image Channels," or over in the Fusion Reference Manual at Chapter 18.

### Inputs

Image Input: The orange image input expects a 2D image.

### Basic Node Setup

In the example below, the Texture 2D node receives a 2D gradient out of the Background node and writes the UV metadata onto it. That metadata then drives how the texture lands on the FBX geometry. When the UV Map tool is available to you, it's the recommended choice, since it can be quicker and offers onscreen controls.

Here a Texture 2D node assigns the 3D texture metadata onto the incoming image.
