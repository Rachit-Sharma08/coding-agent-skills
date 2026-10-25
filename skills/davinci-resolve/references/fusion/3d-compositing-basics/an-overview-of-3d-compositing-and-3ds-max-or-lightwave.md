# An overview of 3D compositing and 3ds max or lightwave

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Next section](merge3d-lighting-and-scene-transforms.md)
<a id="source-3d-compositing-basics"></a> <a id="source-3d-compositing-basics-part-1"></a> <a id="source-3d-compositing-fundamentals"></a> <a id="source-3ds-max-or-lightwave"></a> <a id="source-an-overview-of-3d-compositing"></a> <a id="source-creating-a-minimal-3d-scene"></a> <a id="source-geometry-nodes"></a> <a id="source-the-elements-of-a-3d-scene"></a> <a id="source-the-merge3d-node"></a>

### 3D Compositing Basics

Here we walk through many of the nodes that build 3D composites, what each one does, and the ways they pair up so you can assemble convincing 3D scenes.

### An Overview of 3D Compositing

Conventional image-layer compositing happens in two dimensions. Stacked images carry just enough depth to mark one layer as the foreground and another as the background. That clashes with how production actually works, because every image is either shot through a live-action camera that moves freely along all three axes within a scene that genuinely has depth, or it originates inside a real 3D modeling and rendering package. The Fusion Node Editor gives you a GPU-accelerated 3D compositing space with support for imported geometry, point clouds, and particle systems, letting you handle jobs like these:

- Converting 2D images into image planes in 3D space
- Creating rough primitive geometry
- Importing mesh geometry from FBX or Alembic scenes
- Creating realistic surfaces using illumination models and shader compositing
- Rendering with realistic depth of field, motion blur, and supersampling
- Creating and using 3D particle systems
- Creating, extruding, and beveling 3D text
- Lighting and casting shadows across geometry
- 3D camera tracking
- Importing cameras, lights, and materials from 3D applications such as Maya,

### 3ds Max, or LightWave

- Bringing in matched cameras plus point clouds out of packages like SynthEyes or PF Track

An example 3D scene in Fusion

### 3D Compositing Fundamentals

The 3D category of nodes — encompassing the Light, Material, and Texture subcategories — collaborate to build 3D scenes. You'll find nodes that author geometry, bring in geometry, reshape geometry, set up lights and cameras, and pull all those pieces into one scene. Almost every node of this kind lives together inside the 3D category of nodes found in the Effects Library.

The 3D category of nodes in the Effects Library Helpfully, you never have to declare anywhere whether the whole composition is meant to be 2D or 3D, since any quantity of 2D and 3D "scenes" can blend together fluidly into one result. That said, for everything to behave correctly, the nodes building those scenes have to be wired up in particular arrangements.

### Creating a Minimal 3D Scene

Building a 3D scene is about as simple as it gets, provided you wire the necessary nodes together correctly. The bare minimum is wiring a geometry node (a Text3D node, for example) into a Renderer3D node, which yields a 2D image you can blend with the other 2D images of your comp, as pictured below. The catch is that you'll end up with nothing more than flatly shaded geometry, though you can still tint and reposition it in the Inspector through the controls built into whatever geometry node you happen to be working with.

A basic 3D scene where a Text3D node feeds straight into a Renderer3D node

In practice, most 3D scenes you set out to build will likely involve three to five nodes so the result is framed and lit more effectively. The typical set includes:

- Any single geometry node on offer (for instance Text3D or Image Plane 3D)
- A light node (such as DirectionalLight or SpotLight)
- A camera node
- A Merge3D node
- A Renderer3D node

Wire all of these up the way the illustration below shows, producing the correspondingly richer 3D scene also pictured below.

That same text, now framed and lit by wiring Text3D, Camera, and SpotLight nodes into a Merge3D node Here's a quick run-through of how this node tree functions: the geometry node (Text3D in this case) builds an object for the scene, then the Merge3D node acts as a virtual stage where that geometry meets the light and camera nodes, yielding a framed, lit outcome complete with highlights and shadows, and finally the well-named Renderer3D node renders that 3D scene into a 2D image you can subsequently combine with the rest of the 2D images in your comp. These nodes matter so much, in fact, that they sit at the right end of the toolbar, letting you spin up 3D scenes any time the need arises. Notice that the left-to-right sequence of the 3D toolbar buttons mirrors the usual order in which you reach for these nodes. As a result, clicking each button in turn from left to right is guaranteed to lay down a correctly built 3D scene that's ready for further work, just as the previous screenshot shows.

The 3D nodes available from the toolbar include the ImagePlane3D, Shape3D, Text3D, Merge3D, Camera3D, SpotLight3D, and Renderer3D nodes

### The Elements of a 3D Scene

Every 3D node falls into one of several groupings.

### Geometry Nodes

To bring 3D geometry into a comp, reach for the ImagePlane3D node, the Shape3D node, the Cube3D node, or the Text3D node, or alternatively import a model through the FBX Mesh 3D node. On top of that, pEmitter nodes let you add particle geometry to your scenes. Any of these can feed into a Merge3D node, whether on their own or several at a time, so you can build rich results out of multiple combined pieces. A richer 3D scene that brings together a number of geometry nodes, among them the Text3D, Shape3D, and ImagePlane3D nodes Texturing Geometry On its own, a geometry node carries nothing but a single flat color. You can change the appearance of 3D geometry, though, by texturing it with clips (stills or footage), by routing it through material nodes like the Blinn and Phong nodes to build richer textures from blends of 2D images and environment maps, or by grabbing a ready-made shader out of the Templates > Shader bin of the Effects Library, which is stocked with materials and texture presets you can drop straight in. For basic geometric primitives, texturing is as easy as wiring an image (a still or footage) or a Templates-bin shader from the Effects Library directly into the material input of a Shape3D, Cube3D, or another node that accepts it, as the figure below illustrates.

An image fed into the material input of a Shape3D node configured as Torus — the source image at left, and the textured torus at right When it comes to shading or texturing Text3D nodes, the texture has to be applied a particular way, because each such node is really a scene whose individual 3D objects (the characters) operate together. The example that follows applies the RustyMetal shader preset onto a Text3D node by way of the ReplaceMaterial3D node. What's notable about the ReplaceMaterial3D node is that it textures every geometric object in a scene simultaneously — so dropping a ReplaceMaterial3D node downstream of a Text3D node textures all of that node's characters. Place a ReplaceMaterial3D node after a Merge3D node instead, though, and you'll retexture every last geometric object being merged in that Merge3D node, which is a powerful thing to be able to do.

Texturing the geometry from a Text3D node by routing a shader through a ReplaceMaterial3D node placed downstream of whichever object you mean to shade

### The Merge3D Node

A Merge3D node pulls the output of one or several 3D nodes into a unified scene. In contrast to the Merge2D node, scene ordering here isn't confined to just foreground and background inputs. The Merge3D node instead accepts as many inputs as you care to attach, and the combined output reflects where each object sits in absolute 3D space. Pulling numerous objects into a single 3D scene by way of the Merge3D node Combining Objects Directly The Merge3D node offers an organized route to combining objects, but you can equally well join 3D objects such as Text3D and Shape3D nodes by wiring one 3D object node's output into the input of another, as the next screenshot demonstrates. Doing so means you'll rely on each node's own internal transform parameters to directly set position, size, and rotation, yet a downstream 3D object node's transform control also drives every upstream 3D object node along with it. The same holds for lights and the Camera3D node, which is a quick way to bundle objects that always belong together — a bundle you can wire into a Merge3D node afterward for extra lighting and an eventual hookup to a Renderer3D node.

Joining one Shape3D node straight into another to merge them Transforming the final downstream 3D object carries every upstream object along with it; the last Shape3D node is the one being viewed, with both visible Combining Multiple Merge3D Nodes On top of that, one Merge3D node can be joined to another Merge3D node, so you're able to assemble compound 3D scenes built from several "sub-scenes," each one constructed inside its own Merge3D node.

You can build elaborate scenes using multiple Merge3D nodes connected together
