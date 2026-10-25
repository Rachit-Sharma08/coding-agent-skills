# Lat long patcher and panomap and spherical camera

Version: DaVinci Resolve 20.3 Reference Manual. Context: Lat long patcher, Panomap, Spherical camera.
[Chapter index](INDEX.md) / [Previous section](immersive-patcher-and-lat-long-patcher.md) / [Next section](spherical-camera-and-common-controls.md) / [Lat Long Patcher LLP](immersive-patcher-and-lat-long-patcher.md)
<a id="source-basic-node-setup-2"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-fromto"></a> <a id="source-input-1"></a> <a id="source-inspector-1"></a> <a id="source-mode"></a> <a id="source-panomap-node-introduction"></a> <a id="source-panomap-pam"></a> <a id="source-spherical-camera-3sc"></a> <a id="source-spherical-camera-node-introduction"></a> <a id="source-spherical-stabilizer"></a> <a id="source-the-lat-long-patcher-controls-tab"></a> <a id="source-the-panomap-controls-tab"></a> <a id="source-the-panomap-node"></a> <a id="source-the-spherical-camera-node"></a> <a id="source-the-spherical-stabilizer-node"></a>

### The Lat Long Patcher Controls tab

### Controls Tab

You use the Controls tab to pull out a portion of an equirectangular image and later put it back. The Rotation controls let you home in on the precise piece you mean to repair.

### Mode

- Extract: Draws a de-warped 90-degree square image out of the equirectangular image.
- Apply: Warps a 90-degree square image and merges it onto the equirectangular image. Since the square image's alpha comes into play, this lets things such as paint strokes or text laid over a transparent black background carry onto the original equirectangular image, sidestepping any double-filtering that de-warping and re-warping the original would cause.
- Apply180: Apply this to extract and patch a VR180 image. It hands you the means to lay conventional 2D effects, paint among them, onto a 180 distorted clip.

Rotation Order These buttons set the sequence in which the rotations happen about each axis. Take XYZ, for instance: it spins first about the X axis (pitch/tilt), next about the Y axis (pan/yaw), and finally about the Z axis (roll). You may settle on whichever of the six possible orderings you like. Rotation These dials turn the spherical image about each of the X, Y, and Z axes, giving you separate command over pitch/tilt, pan/yaw, and roll in turn.

### Common Controls

Settings Tab Across the other VR nodes, the Inspector's Settings tab shows up again unchanged. A full account of these common controls waits at this chapter's close, in the “The Common Controls” section.

### PanoMap [PAM]

### The PanoMap node

NOTE: The VR category, together with the PanoMap node, exists solely within Fusion Studio and DaVinci Resolve Studio.

### PanoMap Node Introduction

What the PanoMap node does is translate images from one spherical layout into another — say, turning a cube map into an equirectangular format. While converting, the node is also able to rotate the spherical images.

### Input

Two inputs sit on the PanoMap node. Its orange input takes a 2D image in equirectangular, cube map or other spherical formats. An effect mask input exists too, though VR nodes seldom call for it. Image Input: The orange Image input takes a spherical-formatted 2D RGBA image, which then gets converted into another spherical format. Effect Mask: An effect mask input is on hand here, even if VR nodes make little use of it.

### Basic Node Setup

For the example below, a Loader node holding a Lat Long image links into the input of a PanoMap node. The PanoMap node then converts that image into an H-Cross format, after which it links into whichever image-processing operation you require.

A PanoMap used to convert from one VR format to another

### Inspector

### The PanoMap Controls tab

### Controls Tab

The Controls tab is where you set both the format of the incoming image and the output format you're after.

### From/To

- Auto: Auto reads the incoming image layout off the metadata and the image frame aspect.
- VCross and HCross: VCross and HCross are a cube's six square faces arranged into a cross, either vertically or horizontally, the forward view sitting at the cross's middle within a 3:4 or 4:3 image.
- VStrip and HStrip: VStrip and HStrip are a cube's six square faces set vertically or horizontally in a row, sequenced Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z) within a 1:6 or 6:1 image.
- LatLong: LatLong is one 2:1 image carrying an equirectangular mapping.
- VR 180 is a 1:1 180 degree stereoscopic image.
- Immersive is the format used by Apple Vision Pro.

Rotation Order These buttons set the sequence in which the rotations happen about each axis. Take XYZ, for instance: it spins first about the X axis (pitch/tilt), next about the Y axis (pan/yaw), and finally about the Z axis (roll). You may settle on whichever of the six possible orderings you like. Rotation These dials turn the spherical image about each of the X, Y, and Z axes, giving you separate command over pitch/tilt, pan/yaw, and roll in turn.

### Common Controls

Settings Tab Across the other VR nodes, the Inspector's Settings tab appears once more unchanged. These common controls get a thorough write-up at the end of this chapter, within the “The Common Controls” section.

### Spherical Camera [3SC]

### The Spherical Camera node

### Spherical Camera Node Introduction

You won't find the Spherical Camera in the Effects Library's VR category — it lives in the 3D category instead. Even so, because it sees regular use in building and repairing VR content, it gets a mention here. The Spherical Camera lets the 3D Renderer node put out an image spanning every viewing angle, arranged across a handful of formats. Such an image might serve as a skybox texture or a reflection map, say, or be viewed inside a VR headset. The Image Width setting on the 3D Renderer determines how big each square cube face is, so that the finished image can come out as a multiple of that size both across and down. To read further about the Spherical Camera node, turn to Chapter 89, "3D Nodes," within the DaVinci Resolve Reference Manual, or to Chapter 29, over in the Fusion Reference Manual.

### Spherical Stabilizer

### The Spherical Stabilizer node

NOTE: You'll find the VR category and the Spherical Stabilizer node in Fusion Studio and DaVinci Resolve Studio alone.
