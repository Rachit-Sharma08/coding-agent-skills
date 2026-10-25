# Weld 3D and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Weld 3D, Common controls.
[Chapter index](INDEX.md) / [Previous section](triangulate-3d-and-uv-map-3d-and-weld-3d.md) / [Weld 3D 3We](triangulate-3d-and-uv-map-3d-and-weld-3d.md) / [Next section](common-controls-common-materials-tab.md)
<a id="source-3d-nodes-part-9"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3d-tab"></a> <a id="source-common-controls-tab"></a> <a id="source-controls-tab-3"></a> <a id="source-coordinate-transform-3d"></a> <a id="source-inputs-3"></a> <a id="source-inspector-1"></a> <a id="source-lighting"></a> <a id="source-modifier"></a> <a id="source-the-common-controls"></a> <a id="source-visibility"></a> <a id="source-weld-3d-controls"></a> <a id="source-weld-3d-modifier-tools"></a>

### Inputs

The Weld 3D node carries one input for the 3D scene or 3D object you want to repair. Scene Input: Wire the orange scene input to the 3D scene or 3D object you intend to fix.

### Basic Node Setup

Set the Weld 3D node downstream of geometry suffering from duplicate-vertex trouble. Such problems sometimes surface when the geometry is displaced. When that happens, dropping the weld after the geometry yet ahead of the Displace 3D can mend things.

Weld 3D is placed after the 3D geometry that needs repair Inspector

### Weld 3D controls

### Controls Tab

On the Weld 3D node, the Controls tab offers a single Weld Mode menu. You decide between welding vertices or fracturing them. Fracture Fracturing inverts welding, so every vertex is unwelded. Consequently all polygon adjacency data is thrown away. As an example, an Image Plane 3D ordinarily consists of joined quads sharing vertices. Fracture the image plane and it turns into a cluster of disconnected quads. Tolerance Under auto mode, the Tolerance figure is worked out for you. That covers most situations. You can also set it by hand where needed.

USAGE Reach for Weld 3D when the geometry gives you trouble. Don’t scatter it everywhere just because it exists, since it adds to render time. Weld 3D is meant as a mesh robustness tool, not as a mesh editing tool for merging vertices. If the gap between the vertices you intend to weld is visible in the 3D view, odds are you’re misusing Weld 3D. Strange results can follow when you try it; proceed at your own risk. LIMITATIONS A tolerance set too high can make edges and faces collapse into points. When a model spreads its detail across several orders of scale, settling on a tolerance figure can be tough or even impossible. Imagine, for instance, a model of the International Space Station bearing both many large polygons and many extremely small ones. Set the tolerance too high and small polygons that shouldn’t merge will; set it too low and some large polygons stay unmerged. Vertices a long way from the origin may not merge as they should. The cause is that bignumber + epsilon can come out exactly equal to bignumber under float math. That’s one argument for merging in local coordinates rather than world coordinates. On occasion, Weld 3D-ing a mesh degrades it. Consider Fusion’s cone. Its top vertex is presently duplicated once per neighboring face, each copy holding a different normal. Weld the cone and the top vertices fuse into a single normal, throwing the lighting off. Weld 3D is not multithreaded. WARNING: Do not abuse Weld 3D as a way to simplify (cut the polygon count of) meshes. Its purpose is to efficiently fuse vertices separated by only tiny amounts, on the order of a 0.001 distance.

### Common Controls

Settings Tab Other 3D nodes carry the same Settings tab found here in the Inspector. A full account of these shared controls appears at this chapter’s end within “The Common Controls” section.

### Modifier

### Coordinate Transform 3D

Owing to the hierarchical structure of Fusion’s 3D node tree, an object’s starting position in the 3D scene frequently does not reflect where the object currently sits. Picture an image plane whose position starts out as 1, 2, 1, yet later nodes downstream in the 3D scene then scale, offset, and rotate it until it ends up at an absolute location of 10, 20, 5. That makes it tricky to link a downstream object in the composition straight to an upstream object’s position. You can attach the Coordinate Transform modifier to any group of XYZ coordinate controls and have it compute an object’s present position anywhere in the scene hierarchy. To bring in a Coordinate Transform modifier, just right-click a number field on any node and pick Modify With/CoordTransform Position from the Controls’ contextual menu.

### Inspector

### Weld 3D modifier tools

Target Object Connect this control to the 3D node that supplies the original coordinates you want transformed. To hook up a node, drag it from the node tree and drop it into the Text Edit control, or right-click the control and pick the node from the contextual menu. Typing the node’s name straight into the control works as well. Sub ID The Sub ID slider lets you single out one sub-element of certain geometry types, such as a particular character made by a Text 3D node or a specific copy spawned by a Duplicate 3D node. Scene Input Connect this control to the 3D node that emits the scene holding the object at its new location. To hook up a node, drag it from the node tree and drop it into the Text Edit control, or right-click the control and pick an object from the Connect To submenu.

### The Common Controls

Several identical controls in the Inspector are shared by nodes that work with 3D geometry. The controls common to 3D nodes are described in this section.

### Common Controls Tab

### Common Controls 3D tab

You’ll usually find these controls in the lower portion of the Controls tab. They show up in nodes that build or hold 3D geometry.

### Visibility

- Visible: With this option on, the object appears in the viewers and in final renders. Turn it off and the object is neither shown in the viewers nor rendered into the output image by the Renderer 3D node. A non-visible object also casts no shadows.
- Unseen by Cameras: With the Unseen by Cameras checkbox on, the object stays visible in the viewers (provided the Visible checkbox isn’t off), apart from when seen through a camera. The Renderer 3D node also leaves it out of the output image. Even so, shadows an unseen object casts still appear when the software renderer in the Renderer 3D node draws them, though the OpenGL renderer does not.
- Cull Front Face/Back Face: Reach for these options to stop certain polygons in the geometry from being rendered and shown. With Cull Back Face on, polygons turned away from the camera neither render nor cast shadows. With Cull Front Face on, polygons turned toward the camera neither render nor cast shadows. Switching on both produces the same outcome as clearing the Visible checkbox.
- Suppress Aux Channels for Transparent Pixels: In earlier Fusion releases, the software and Open GL render options in the Renderer 3D node threw out transparent pixels. To be

more specific, any pixel whose R,G,B,A read 0 was dropped by the software renderer, while the GL renderer dropped a pixel once its A read 0. That behavior is now a choice. Why opt in is to obtain aux channels (e.g., Normals, Z, UVs) over the transparent regions. Imagine, for instance, that you mean to swap the texture on a 3D element which is transparent in some spots for a texture transparent in other spots. Then it pays to have the transparent regions write aux channels (UVs in particular). Or, imagine you’re adding depth of field. You likely don’t want the Z-channel written over transparent areas, because that hands you a false depth. Bear in mind, too, that the exclusion keys off the final pixel color, lighting included if it’s active. So a specular highlight sitting on a clear glass material isn’t touched by this checkbox.

### Lighting

- Affected by Lights: Clearing this checkbox keeps scene lights from influencing the object. The object then neither takes nor casts shadows, and it appears at the full brightness of its color, texture, or material.
- Shadow Caster: Clearing this checkbox stops the object from casting shadows on other objects in the scene.
- Shadow Receiver: Clearing this checkbox stops the object from receiving shadows other objects in the scene cast.

Matte Switching on the Is Matte option applies a special texture that makes the object not only invisible to the camera but also hides everything sitting directly behind the camera. This option takes precedence over all textures. Where Fog 3D and Soft Clipping are concerned, turn to “3D Compositing Basics” (Chapter 85) within the DaVinci Resolve Reference Manual, or to Chapter 25 of the Fusion Reference Manual. Is Matte: Once active, objects whose pixels lie behind the matte object’s pixels in Z are not rendered. Switching on the Is Matte checkbox brings up two more options. Opaque Alpha: With the Is Matte checkbox on, the Opaque Alpha checkbox forces the matte object’s Alpha value to 1. Infinite Z: This option drives the value in the Z-channel to infinite. The checkbox shows up only while the Is Matte option is on. Blend Mode A Blend mode determines which technique the renderer uses to fold this object into the rest of the scene. These blend modes are basically the same as those covered in the 2D Merge node section. For a thorough rundown of each mode, see that node’s section. The blending modes were first intended for 2D images. Putting them to work in a lit 3D environment can yield unwanted results. For the best outcome, apply the Apply modes within unlit 3D scenes using the software option of the Renderer 3D node.

- OpenGL Blend Mode: This menu chooses which blending mode applies as the geometry runs through the OpenGL renderer inside the Renderer 3D node. The same mode governs how the object looks in the viewers. For now the OpenGL renderer handles only a limited set of blending modes.
- Software Blend Mode: This menu chooses which blending mode applies as the geometry runs through the software renderer. At present the software renderer covers every mode laid out in the Merge node documentation, with the sole exception of the Dissolve mode.

Normal/Tangents Normals are conceptual lines standing perpendicular to each point across an object’s surface. They mark the precise direction and orientation of each polygon on a piece of 3D geometry. That direction and orientation is what governs how the object is shaded. Tangents, by contrast, are lines lying within the plane of the surface. Each one runs tangent to a point on the surface. These tangent lines describe the orientation of the textures you map onto the surface of 3D geometry.

- Scale: This slider lengthens or shortens the vectors drawn for both normals and tangents.
- Show Normals: Renders blue vectors that usually project out past the surface of the geometry.

Such normal vectors give a sense of how the various regions of the surface catch light depending on the angle the light strikes them.

- Show Tangents: Renders green vectors for Y and red vectors for X. Those X and Y vectors stand for the orientation of the image or texture being mapped onto the geometry.

Object ID This slider chooses which ID is used to build a mask from an image’s object. Operate the Sample button just as you would the Color Picker to lift IDs from the picture shown in the viewer. The image or sequence has to have been rendered out of a 3D software package that included those channels.
