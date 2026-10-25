# Immersive patcher and lat long patcher

Version: DaVinci Resolve 20.3 Reference Manual. Context: Immersive patcher, Lat long patcher.
[Chapter index](INDEX.md) / [Next section](lat-long-patcher-and-panomap-and-spherical-camera.md)
<a id="source-apple-immersive-option-in-the-viewer-360-views-menu"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-fusion-vr-180-support-studio-version-only"></a> <a id="source-immersive-patcher-imp"></a> <a id="source-immersive-patcher-introduction"></a> <a id="source-input"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-lat-long-patcher-llp"></a> <a id="source-lat-long-patcher-node-introduction"></a> <a id="source-the-immersive-patcher-controls"></a> <a id="source-the-immersive-patcher-node"></a> <a id="source-the-lat-long-patcher-node"></a> <a id="source-vr-nodes"></a> <a id="source-vr-nodes-1"></a>

### VR Nodes

This chapter walks through the Virtual Reality (VR) nodes that Fusion provides.

Each node name has an abbreviation beside it that you can type into the Select Tool dialog while hunting for tools, and that also serves in scripting references. Throughout this document, take node trees that show MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where it says otherwise.

With Fusion's collection of VR nodes you can build and repair spherical (360°) video, the kind commonly called Virtual Reality, or VR. For years now, dome productions, planetariums, and similar special-venue theaters have leaned on the adaptability of Fusion together with its 3D system to make and ship specialized content. That equirectangular (lat-long) format so often chosen for 360° video works much like how a globe gets flattened onto a world map, the poles running along the image's top and bottom edges and the forward viewpoint sitting in the middle. TIP: Stereo VR is achievable by stacking a pair of Lat Long images, assigning one to each eye.

A VR Sphere shown both in the Node Editor and within Fusion's 3D viewer

Fusion handles a handful of widespread spherical image formats and converts among them with ease. VCross and HCross: These are a cube's six square faces arranged into a cross, either vertically or horizontally, the forward view sitting at the cross's middle within a 3:4 or 4:3 image. VStrip and HStrip: These are a cube's six square faces set vertically or horizontally in a row, sequenced Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z) within a 1:6 or 6:1 image. LatLong: This is one 2:1 image carrying an equirectangular mapping. Both spherical video and live 3D scenes from the comp can be sent straight to headsets, the Oculus Rift and HTC Vive included. Fusion's “Fix it in post” tools for VR streamline a handful of key jobs that crop up regularly in productions of this sort.

### Fusion VR 180 Support (Studio Version Only)

Several of Fusion's established VR tools have gained support for a 180-degree angle of view. By concentrating on a forward-facing view, the 180-degree VR format lets you make immersive content while easing the production workflow for VR experiences.

### Apple Immersive Option in the Viewer 360 Views Menu

Within the 2D Viewer windows, Fusion can decode Apple Immersive content. Switch this on by clicking the option menu in a Fusion Viewer and picking 360(o) View > Immersive out of the context menu.

### Immersive Patcher [ImP]

### The Immersive Patcher node

### Immersive Patcher Introduction

With the Immersive Patcher tool you can briefly ‘undistort’ a portion of an immersive clip so that tracking, painting and compositing become easier on a flat plane. When you're done, a second Immersive Patcher re-distorts the immersive signal and folds the freshly composited pieces back into the scene.

### Inputs

Within the Node Editor, the Immersive Patcher node carries two inputs. Input: The orange input takes either an immersive or an ordinary 2D output. Metadata: The metadata input takes metadata fed from another node.

### Basic Node Setup

In essence, the Immersive Patcher is built to operate in pairs:

- Send an immersive video clip through an Immersive Patcher node, using Undistort to turn it into an ordinary image.
- Set the Rotation and Angle of view so they frame the region you intend to alter.
- After that, lean on Fusion's broad toolset to composite and reshape the image just as you normally would.
- After that, run a second Immersive Patcher node to Distort it back into an Immersive Video.
- After that, bring in a merge node to fold your edits back into the original immersive video clip.

IMPORTANT: For the image to hold together, both Immersive Patchers need identical Rotation and Angle of view settings. Simplest route: duplicate the first Immersive Patcher and paste it to make the second.

Routing an immersive video clip through an Immersive Patcher that undistorts the picture, next layering on a multipoly and transform operation, then re-distorting the picture by means of a second Immersive patcher, and finally merging it back together with the original immersive video clip.

### Inspector

### The Immersive Patcher Controls

- Mode: A pair of choices lets you either Distort (turn the image from 2D into Immersive Video) or Undistort (turn Immersive Video into a 2D image) the input.
- Rotation: These controls spin the immersive video around until the region you mean to alter sits in the frame.
- Angle of View: This control sets the angle of view presented inside the VR headset.

### Lat Long Patcher [LLP]

### The Lat Long Patcher node

NOTE: Only Fusion Studio and DaVinci Resolve Studio offer the VR category along with the Lat Long node.

### Lat Long Patcher Node Introduction

Equirectangular stitched images frequently call for patches, paintwork, or assorted VFX. What the Lat Long Patcher does is pull out and de-warp a portion of a lat-long (equirectangular) image for treatment, then warp and merge the fixes back atop the original. You're able to swiftly grab a portion of the spherical image to patch or paint and then lay it back onto the original image. Bear in mind that both the Extract and Apply modes rely on matching rotations, which means a node's action can be undone with ease by a copy or instance carrying the same rotation settings.

### Input

There are two inputs on the Lat Long Patcher node. Its orange input takes a 2D image in equirectangular form, the X-axis standing for 0–360 degrees longitude and the Y-axis for –90 to +90 degrees latitude. An effect mask input exists too, though VR nodes seldom call for it. Image Input: The orange image input takes a equirectangular (lat-long) 2D RGBA image. Effect Mask: An effect mask input is on hand here, even if VR nodes make little use of it.

### Basic Node Setup

The Loader node feeds into the input of a Lat Long Patcher node. That Lat Long Patcher node has its output set to Extract, after which it links into whichever image-processing operation you require. A second Lat Long Patcher node, this one set to Apply, takes its input from the processed extraction and lays it back atop the original source.

Two Lat Long Patchers used to repair a section Inspector
