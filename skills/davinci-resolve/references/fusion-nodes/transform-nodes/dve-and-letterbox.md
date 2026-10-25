# Dve and letterbox

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dve, Letterbox.
[Chapter index](INDEX.md) / [Previous section](camera-shake-and-crop-and-dve.md) / [Next section](letterbox-and-planar-transform.md) / [DVE DVE](camera-shake-and-crop-and-dve.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-2"></a> <a id="source-letterbox-lbx"></a> <a id="source-letterbox-node-introduction"></a> <a id="source-masking-tab"></a> <a id="source-the-dve-controls-tab"></a> <a id="source-the-dve-masking-tab"></a> <a id="source-the-letterbox-node"></a>

### Basic Node Setup

In the example here, the DVE node lands between the MediaIn2 node and the Merge's foreground input. The MediaIn1 node is reshaped within the DVE node and laid over the top of the MediaIn1 node.

The DVE node modifying the foreground input of a Merge node

### Inspector

### The DVE Controls tab

### Controls Tab

Every transform parameter for the DVE lives on the Controls tab. Pivot X, Y, and Z Sets where the axis of rotation and scaling sits. By default this is 0.5, 0.5 for X and Y—the image's center—and 0 for Z, which sits at the middle of Z space. Rotation Order These buttons let you choose the sequence in which rotations get applied to the image. XYZ Rotation Reach for these controls to spin the image around the pivot on the X-, Y-, and Z-axis. Center X and Y This sets where the center of the DVE image sits onscreen. The default of 0.5, 0.5 drops the DVE in the image's center. Z Move This pushes the image in and out along the Z-axis. When animated, it visually resembles an object drawing closer from far away. Perspective This layers extra perspective onto an image that has been rotated on the X- or Y-axis, much like adjusting a camera's Field of View and zoom.

### Masking Tab

The DVE node permits pre-masking of the image it receives. That makes it possible to build transformations out of the masked region of the image while the rest of the image stays untouched.

### The DVE Masking tab

In contrast to ordinary effect masks, here the masking happens before the transformation. Every one of the usual mask types works on the DVE mask. Black Background Switch this on to wipe the region beyond the mask out of the transformed image. Fill Black Switch this on to wipe the region inside the mask (prior to transformation) out of the DVE’s input, in effect cutting the masked region out of the image. Turning on both Black Background and Fill Black leaves only the masked, transformed region visible. Alpha Mode This decides how the DVE treats the image's alpha channel while merging the transformed image regions over the untransformed image.

- Ignore Alpha: Makes the input image’s alpha channel be disregarded, leaving every masked area opaque.
- Subtractive/Additive: Decide whether, internally, the pre-masked DVE image is laid over the input image as Subtractive or as Additive. You need an Additive setting whenever the foreground DVE image is premultiplied—that is, its color-channel pixels have already been multiplied by the alpha-channel pixels. Because of that, transparent pixels always come out black, given that anything times 0 stays 0. The background gets obscured (multiplied by the inverse of the foreground alpha), after which the foreground pixels are simply added on top.

A Subtractive setting is required whenever the foreground DVE image has not been premultiplied. The compositing approach resembles an Additive merge, except the foreground DVE image is first scaled by its own alpha to strip out any background pixels lying beyond the alpha area.

### Common Controls

Settings Tab Other Transform nodes carry a copy of the same Settings tab found here in the Inspector. You will find a full account of these shared controls under the “The Common Controls” section at this chapter's close.

### Letterbox [LBX]

### The Letterbox node

### Letterbox Node Introduction

Reach for the Letterbox node when you need to fit existing images to the frame size and aspect ratios of some other format. Most often it is used to turn film-resolution images into HD-sized frames so they can be viewed on an external television monitor. Where aspect ratios differ, horizontal or vertical black edges get added automatically to make up the difference. This node genuinely alters the image's resolution. NOTE: Since this node alters the image's physical resolution, animating the controls is discouraged.

### Inputs

A 2D image for letterbox/cropping wires into the Letterbox node's lone input. Input: The primary 2D image you intend to letterbox/crop attaches to the orange input.

### Basic Node Setup

In the example below, the Letterbox node serves to alter the resolution of the Merge node’s output. According to how the resolution gets changed, either side pillars or a horizontal letterbox mask is laid in to “fill in” the part of the frame the Merge node output leaves uncovered.

The Letterbox node changing the Merge output resolution while inserting letterbox masking as required.
