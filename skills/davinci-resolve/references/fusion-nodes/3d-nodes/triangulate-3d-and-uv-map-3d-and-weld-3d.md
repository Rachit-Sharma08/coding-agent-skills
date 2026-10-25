# Triangulate 3D and uv map 3D and weld 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Triangulate 3D, Uv map 3D, Weld 3D.
[Chapter index](INDEX.md) / [Previous section](transform-3d-and-triangulate-3d.md) / [Next section](weld-3d-and-common-controls.md) / [Triangulate 3D 3Tri](transform-3d-and-triangulate-3d.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-the-uvmap-3d-node"></a> <a id="source-the-weld-3d-node"></a> <a id="source-triangulate-3d-controls"></a> <a id="source-triangulate-3d-nodes-connected-after-an-imported-model"></a> <a id="source-uv-map-3d-3uv"></a> <a id="source-uv-map-3d-controls"></a> <a id="source-uv-map-3d-node-introduction"></a> <a id="source-weld-3d-3we"></a> <a id="source-weld-3d-node-introduction"></a>

### Basic Node Setup

Place the Triangulate 3D node downstream of the geometry you intend to triangulate.

### Triangulate 3D nodes connected after an imported model

### Inspector

### Triangulate 3D controls

### Controls Tab

This node has no controls.

### Common Controls

Settings Tab Other 3D nodes carry the same Settings tab found here in the Inspector. A full account of these shared controls appears at this chapter’s end within “The Common Controls” section.

### UV Map 3D [3UV]

### The UVMap 3D node

### UV Map 3D Node Introduction

What the UV Map 3D node does is swap out the UV texture coordinates on the scene’s geometry. Those coordinates instruct Fusion on the way a texture is laid onto an object. You can tweak the overall properties of whichever mapping mode is chosen, yet you cannot reach in and hand-edit the UV coordinates of single vertices inside Fusion. Onscreen controls that appear in the viewers serve only as a reference and aren’t adjustable. Camera Projections with UV Map 3D With the Camera Mapping mode you can cast texture coordinates onto geometry by way of a camera. After picking Camera in the Mapping mode menu, attach the Camera 3D node you intend to use for generating the UV coordinates. NOTE: This does not literally cast an image through the camera. Feed the picture you want projected into the diffuse texture input of whichever material the objects carry. As the texture lands, it relies on the UV coordinates the camera produced. Since this is a projection of texture and not of light, the texture’s Alpha channel properly drives the geometry’s opacity. Look at the Camera 3D and Projector 3D nodes for other ways to handle projection. If you like, the projection can be pinned to the vertices the way it looks on a chosen frame. That breaks when the mesh’s vertex count varies over time, because Fusion has to align the mesh between the reference time and the current time. Put plainly, vertices must not be added, removed, or reordered. Consequently, projection locking won’t hold for many particle systems, nor for primitives whose subdivisions are animated, nor for duplicate nodes carrying non-zero time offsets. NOTE: The UV Map 3D node lays neither a texture nor a material on the mesh; all it touches are the texture coordinates the materials draw from. That can be puzzling, since the material typically sits upstream, as the Basic Node Setup example below shows.

### Inputs

There are two inputs on the UV Map 3D node: one taking a 3D scene or 3D object, and a second optional one taking a Camera 3D node. Scene Input: Wire the orange scene input to the 3D scene or 3D object you intend to triangulate. CameraInput: This input is meant for the output of the Camera 3D node. It shows up only after the Camera Map mode menu has been switched to Camera.

### Basic Node Setup

Position the UV Map 3D node downstream of all the geometry and switch it to Camera Map. Hooking a camera up to the UV map lets you align the texture using a centered camera position together with the 3D geometry.

Set downstream of the Merge 3D, the UV Map 3D has a camera wired in so the texture aligns Inspector

### UV Map 3D controls

### Controls Tab

In the UV Map 3D Controls tab you can choose among Planar, Cylindrical, Spherical, XYZ, and Cubic mapping modes, all of which work on basic Fusion primitives as well as on imported geometry. You can dial in the position, rotation, and scale of the texture coordinates for precise control over how the texture looks. There’s also an option that pins the UV this node generates to animated geometry by way of a reference frame. That keeps textures from sliding across animated geometry.

Map Mode The Map mode menu sets the way the texture coordinates get built. Think of this menu as choosing the virtual geometry that casts the UV space onto the object.

- Planar: Creates the UV coordinates using a plane.
- Cylindrical: Creates the UV coordinates using a cylindrical-shaped object.
- Spherical: The UVs are created using a sphere.
- XYZ to UVW: Each vertex’s position coordinates get mapped straight over into UVW coordinates.

This is used for working with procedural textures.

- CubeMap: The UVs are created using a cube.
- Camera: Switches on the node’s Camera input. Once a camera is wired into the node, the

texture coordinates are created based on camera projection. Orientation X/Y/Z Sets which reference axis is used to align the Map mode. Fit A click on this button fits the Map mode to the input scene’s bounding box. Center Clicking here relocates the Map mode’s center onto the center of the input scene’s bounding box. Lock UVs on Animated Objects When the object is animated, enable this option to pin the UVs to it. Doing so also exposes the Ref Time slider, letting you pick a reference frame for the UV mapping. With this in use, animating the UV map parameters becomes unnecessary. Setting up the UV map at the reference time is sufficient. Size X/Y/Z Sets the size of the projection object. Center X/Y/Z Sets the position of the projection object. Rotation/Rotation Order These buttons choose the sequence in which rotation is applied along each of the object’s axes. As an example, XYZ rotates the X-axis first, then the Y-axis, and the Z-axis last. Rotation X/Y/Z Sets the projection object’s orientation per axis, separately from the rotation order. Tile U/V/W Sets how many times a texture repeats inside the projected UV space along the relevant axis. Keep in mind the UVW coordinates get transformed, not a texture. For best results pair it alongside the Create Texture node. Flip U/V/W Mirrors, about the relevant axis, the texture coordinates. Flip Faces (Cube Map Mode Only) Mirrors the texture coordinates across the cube’s individual faces.

NOTE: Getting the most out of the UV Map 3D node is easier with a basic grasp of how 2D images get mapped onto 3D geometry. Applying a 2D image to a 3D surface turns it into a texture map whose UV coordinates dictate how the picture lands on the object. Every vertex of a mesh carries a (U, V) texture coordinate pair describing how the object looks once it is unwrapped and laid flat. The various mapping modes each take a different approach to figuring out how the vertices flatten into a 2D texture. To alter the texture coordinates on a mesh with the UV Map 3D node, you’ll get the best results sticking to the default coordinate system of that mesh or primitive. The usual chain therefore reads Shape 3D > UV Map 3D > Transform 3D. You’d leave the Transformation tab of the Shape node at its defaults, and let the Transform 3D node placed after the UV Map 3D handle whatever positioning the node needs in the scene. Changing or animating the Shape node’s transform makes the texture creep across the shape, which is usually unwanted. The UV Map 3D node alters texture coordinates per vertex rather than per pixel. When the geometry the UV map covers is poorly tessellated, unwanted artifacts can show up.

### Common Controls

Settings Tab Other 3D nodes carry the same Settings tab found here in the Inspector. A full account of these shared controls appears at this chapter’s end within “The Common Controls” section.

### Weld 3D [3We]

### The Weld 3D node

### Weld 3D Node Introduction

Now and then 3D geometry carries vertices that ought to have been joined as the geometry was built but, for whatever reason, were left separate. The result can be artifacts, particularly where the two vertices carry differing normals. As an example, you might run into:

- The different normals produce hard shading/lighting edges where none were intended.
- Should you Displace 3D those vertices down their normals, cracking occurs.
- Missing pixels or doubled-up pixels in the rendered image.
- Particles pass through the tiny invisible cracks.

Rather than going back to your 3D modeling application to mend these “duplicated” vertices, the Weld 3D node lets you handle it right in Fusion. Weld 3D fuses together vertices whose positions are identical or very nearly so. Use it to clear up cracking that shows when vertices get displaced by welding the geometry ahead of the Displace. No user controls exist for choosing vertices. As it stands, the node fuses only position vertices; it leaves normals, texcoords, and every other vertex stream untouched. Thus, even though two vertices now share the same position, their normals retain their former values. In some cases that yields hard edges.
