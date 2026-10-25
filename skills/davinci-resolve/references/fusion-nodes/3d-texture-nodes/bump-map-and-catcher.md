# Bump map and catcher

Version: DaVinci Resolve 20.3 Reference Manual. Context: Bump map, Catcher.
[Chapter index](INDEX.md) / [Next section](catcher-and-cubemap-and-falloff.md)
<a id="source-3d-texture-nodes"></a> <a id="source-3d-texture-nodes-part-1"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-bump-map"></a> <a id="source-bump-map-3bu"></a> <a id="source-bump-map-controls"></a> <a id="source-bump-map-node-overview"></a> <a id="source-catcher-3ca"></a> <a id="source-catcher-node-overview"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-normals-map"></a> <a id="source-notes-on-bump-maps"></a> <a id="source-the-bump-map-node"></a> <a id="source-the-catcher-node"></a>

### 3D Texture Nodes

This chapter walks through the 3D Texture nodes on hand for building 3D composites in Fusion. The abbreviation beside each node name works in the Select Tool dialog while hunting for tools, and across scripting references.

For the sake of this document, node trees that show MediaIn nodes in DaVinci Resolve stand in interchangeably for Loader nodes in Fusion Studio, except where noted otherwise.

### Bump Map [3Bu]

### The Bump Map node

### Bump Map Node Overview

The Bump Map node turns a grayscale (height map) image into a bump map, taking its input straight from a bump map made by the Create Bump Map node. What the node puts out is a material.

### Inputs

The Bump Map node holds one orange input where you attach a 2D image meant as the bump map texture, or where it accepts the Create Bump Map node's output. ImageInput: Use the orange Image input to attach a 2D RGBA image driving the bump calculation, or a ready-made bump map from the Create Bump map node.

### Basic Node Setup

The Bump Map node wires into the Bump Map material input on any of the material shader nodes. In the example below, a Fast Noise node makes an image that connects to the Bump Map node. The Bump Map node's output then connects to the Bump Map material input on a Ward node.

A Bump Map wired into the Bump Map material input of a material node.

### Inspector

### Bump Map controls

### Controls Tab

Every parameter for modifying the input source and the look of the bump map sits on the Controls tab. Source Image Type Flip between Height Map, which produces a bump map much like the Create Bump Map node does, and Bump Map, which anticipates a bump map made by the Create Bump Map node. Filter Size The bump information comes from a custom filter, and you size that filter through the drop-down menu. Height Channel Picks the channel the grayscale information is pulled from. Clamp Z Normal Clips the lower values of the blue channel within the resulting bump texture. Height Scale Alters the contrast of the resulting values in the bump map. Push this value up and the bump map grows more visible. Texture Depth Optionally turns the resulting bump map texture into whatever bit depth you want. Wrap Mode Wraps the image at its borders, so the filter yields a correct result when seamless tile textures are in play.

### Common Controls

Settings Tab Other 3D nodes carry a copy of the Inspector’s Settings tab. You’ll find these common controls covered in full toward this chapter’s end within the “The Common Controls” section.

### Notes on Bump Maps

Bump mapping carries some muddled terminology, varying by where you read about it. The Fusion conventions go like this: Height Map

### Bump Map

A grayscale image containing a height value per pixel

### Normals Map

An image whose RGB channels hold normals that modify the existing normals (normally supplied in tangent space)

An image whose RGB channels hold normals that replace the existing normals (normally supplied in tangent or object space)

### Catcher [3Ca]

### The Catcher node

### Catcher Node Overview

The Catcher material exists to “catch” texture-mode projections thrown from Projector 3D and Camera 3D nodes. Those caught projections become a texture map that the Catcher material lays onto whatever geometry it connects to. Grasping the Catcher node is easier once you grasp the difference between light-based projections and texture-based projections. On the Projector 3D or Camera 3D nodes, choosing Light in the projection mode menu merely tacks the projected image's RGB channel values onto the diffuse texture of whatever geometry falls inside the projection cone. As a result, you can't clip geometry away through an image's Alpha channel while in light mode projections. Imagine wanting to throw an image of a building onto an image plane for a set extension shot. First you rotoscope the image to mask the windows out, which lets the geometry of the rooms behind the wall show through in the finished composite. Project that image as light, though, and the Alpha channel goes ignored, leaving the masked windows opaque. Hook the Catcher into the diffuse texture map of the image plane's material, then flip the projection mode menu on the Projector 3D or Camera 3D node away from Light or Ambient Light mode and over to Texture mode, and the projected image is applied as a texture map. Used this way for the example above, the windows would turn transparent, and you'd be able to see the geometry behind the window. This approach beats light projection mainly because the Catcher can project Alpha onto an object and asks for no lighting to be switched on. Another plus is that the Catcher isn't confined to a material's diffuse input, so projecting specular intensity maps, or even reflection and refraction maps, becomes possible. NOTE: For the Catcher material to work, the scene must hold a Projector 3D or Camera 3D node configured to throw an image in Texture mode onto whatever object the Catcher attaches to. With no projection present, or one not switched to Texture mode, the Catcher merely leaves the object transparent and invisible.

### Inputs

The Catcher node has no inputs. The node's output wires into the diffuse color material input of the Blinn, Cook Torrance, or another material node applied to the 3D geometry.

### Basic Node Setup

A Catcher node's output should wire into the material input of your 3D geometry node. A camera is arranged as a projector with an image fed into the camera's image input. With the camera set to texture projection mode, the Catcher node decides which geometry takes on the texture.

A Catcher node's output wired into the input of the geometry node taking on the texture projection Inspector
