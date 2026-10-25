# Refraction and bump maps

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](attenuation-and-alpha-detail.md) / [Next section](3d-geometry-visibility-parameters.md)
<a id="source-bump-maps"></a> <a id="source-camera-node-used-for-a-projection-map"></a> <a id="source-geometry"></a> <a id="source-project-a-texture-onto-a-catcher-material"></a> <a id="source-project-using-the-uvmap-node"></a> <a id="source-projection-mapping"></a> <a id="source-refraction"></a> <a id="source-using-a-bump-map"></a> <a id="source-using-a-height-map"></a> <a id="source-using-the-projectorcamera-tool-to-project-light"></a>

### Refraction

Refraction shows up only where transparency exists in the background material, which generally gets steered through the Opacity slider and/or the alpha channel of whatever material or texture feeds the Background Material Texture input. The Reflect node offers the following material inputs:

- Background Material: Sets the refraction opacity along with the reflection’s base color.
- Reflection Color Material: The environment reflection.
- Reflection Intensity Material: A multiplier for the reflection.
- Refraction Tint Material: The environment refraction.
- Bump Map Texture: Normal perturbing map for environment reflection/refraction vectors.

Handling reflection and refraction can get fiddly. Below are a few techniques to ease it:

- As a rule, lean on a modest amount of reflection, somewhere between 0.1 and 0.3 strength. Higher values suit surfaces such as chrome.
- Bump maps can lend detail to the reflections/refractions. Reach for the same bump map within the Illumination model shader that you pair with Reflect.
- Where detailed reflections aren’t called for, lean on a fairly small cube map, say 128 x 128 pixels, and blur the image out.
- The alpha of refracted pixels gets set to 1 even though those pixels are technically transparent. Refracted pixels raise their alpha by the reflection intensity.
- Should the refraction stay invisible even with a texture wired into the Refraction Tint Material input, take a second look at the background material’s alpha/opacity values.

### Bump Maps

Bump mapping helps lend detail and tiny irregularities onto an object’s surface look. What bump mapping does is reshape the object’s geometry or change its silhouette.

Split screen of a sphere—half with bump map, half without To lay on a bump map, you typically wire an image holding the bump information into the BumpMap node. That bump map then gets wired into the Bump input on a Material node. Two routes exist for building a 3D material’s bump map: by way of a height map and by way of a bump map.

Image connected to a BumpMap connected to a CookTorrance material node

### Using a Height Map

A height map is an image where a pixel’s value stands for the height. You can pick which color channel drives bump creation. White stands for high and black for low; what sets the bumpiness, though, isn’t a pixel’s value in the height map but rather how that value shifts across a pixel’s neighborhood.

### Using a Bump Map

A bump map is an image holding normals tucked into the RGB channels. TIP: Normals get produced by 3D modeling and animation software as a means of fooling the eye into perceiving smooth surfaces, even though the geometry that builds the models leans only on triangles to assemble the objects. Normals are 3 float values (nx, ny, nz) whose components sit within the range [–1, +1]. Since only positive values can be stored within Fusion’s integer images, the normals get packed out of the range [–1, +1] and into the range [0, 1]: each is scaled by 0.5, then 0.5 is added on. To handle the unpacking, you can lean on Brightness Contrast or a Custom node. Were you to wire a bump map straight into a material’s bump map input, incorrect lighting would result. Fusion blocks you from doing this, however, because Fusion leans on a different coordinate system for the lighting calculation. You first have to route through a BumpMap, which anticipates a packed bump map or height map and performs the bump map’s conversion so it ends up behaving correctly.

Should your bump mapping look off, here are a few things worth checking:

- Confirm the nodes are wired correctly. The height/bump map ought to feed into a BumpMap and then, in turn, ought to feed into the bump map input on a material.
- Shift the precision of the height map to win less banding across the normals. For low frequency images, float32 may be required.
- Tune the Height scale on the BumpMap. This scales the bump map’s overall effect.
- Confirm you set the type to HeightMap or BumpMap to align with the image input. Fusion cannot work out which type of image you have.
- Verify High Quality is on (right-click within the transport controls bar and pick High Quality off the contextual menu). Certain nodes such as Text+ yield an anti-aliased version in High Quality mode that will markedly lift bump map quality.
- Should you be leaning on an imported normal map image, confirm it is packed [0–1] across RGB and sits in tangent space. The packing can happen within Fusion, but the conversion to tangent space cannot.

### Projection Mapping

Projection is a technique for texturing objects by way of a camera or projector node. That can pay off for texturing objects across multiple layers, laying a texture over multiple separate objects, casting background shots from the camera’s vantage, image-based rendering techniques, and a great deal more. Fusion offers three routes to projection mapping.

### Using the Projector/Camera Tool to Project Light

With lighting switched on, a Camera 3D or Projector 3D can stand in as a light carrying every lighting feature. Once Camera Projection is switched on or you reach for a projector, you can pick whether the projection acts like a spotlight or an ambient light; alpha channels, however, cannot be projected. Overlapping projections sum together like any other light node. An internal clipping plane (around 0.01 distance off the camera) bounds how near the projector or camera can come to the projection’s receivers.

### Camera node used for a projection map

### Project a Texture onto a Catcher Material

Should you prefer not to deal with light sources, you can reach for the projector or camera as a texture projector. To run without lighting, a catcher is needed in order to take the texture and lay it onto a material. Only objects on this material will take the projection. That brings certain upsides, such as the projection of alpha channels, plus texturing other channels like specular color or roughness. With the software renderer in play, overlapping projections can be merged in assorted ways (mean, median, blend, and so forth) by way of the Catcher node. With the OpenGL renderer in play, one catcher per projector gets used, and the outcomes can be merged through another material. As with the Light Projection technique, an internal clipping plane (around 0.01 distance off the camera) bounds how near the projector/camera can come to the projection receivers.

Camera projection paired with a Catcher node (this example comes from an earlier Fusion release)

### Project Using the UVMap Node

This mode needs a camera plus a UVMap3D node sitting downstream of the objects the texture is being projected onto. Within the Inspector, once the UVMap Map mode is set to Camera, it pulls the information off the camera and mints fresh UVs for the input objects, which then drive the texturing. Because the UVs sit tucked into the mesh’s vertices, the object has to be tessellated enough. Textures get assigned onto the object like any other texturing technique. The UVs can be pinned to the vertices at a chosen frame through the Ref Time slider. That pinning holds only so long as vertices aren’t created, destroyed, or reordered (for instance, projection locking will not work on particles since they get created/destroyed, nor will it work on a Cube3D while its subdivision level slider is animated). TIP: Projected textures can be permitted to slide over an object. Should the object shift relative to the Projector 3D, or alternatively, once you group the pair beneath a Merge3D, the two shift as a single unit while the texture holds pinned to the object. Within the following slice of a far larger composition, an image (the Loader1 node) gets thrown into 3D space by being mapped across five planes (Shape3D nodes renamed ground, LeftWall, RightWall, Building, and Background), positioned as required inside a Merge3D node to lay reflections onto a 3D car destined for compositing into that scene.

A slice of a composition busy casting a street-scene image into 3D space Whatever the Merge3D node that gathers those planes into a scene puts out then gets handed to a UV Map node, which alongside a Camera3D node correctly casts every one of these planes into 3D space so they look as they would through that camera in the scene. Ahead of this UVMap projection, you can see the planes laid out in space at left, where each plane carries the scene texture mapped onto it. At right sits the image following the UVMap projection, where you can see the scene once more looks “normal,” save for a car-shaped hole brought into the scene.

Five planes setting a street scene into 3D space ahead of UV Projection (left), alongside the UV Map node at work casting those planes so they read as though seen through a camera within the scene (right) This is now a 3D scene, though, primed for a digital car to be set within it, taking reflections and lighting and throwing shadows into the scene as if it belonged there.

The fresh 3D scene throwing reflections and lighting onto a 3D car while taking on the shadows that car produces

### Geometry

Fusion offers five nodes for building geometry. Those nodes can serve a range of purposes. As an instance, the Image Plane 3D mainly serves to drop image clips into a 3D scene, whereas the Shapes node can lend extra building blocks to a 3D set, and Text 3D can lend three-dimensional motion graphics for title sequences and commercials. Although the “3D Nodes” chapter treats each node in more depth, a rundown of the 3D creation nodes follows below. Cube 3D The Cube 3D builds a cube whose six inputs let you map a different texture onto every face of the cube. Image Plane 3D The Image Plane 3D serves as the basic node for setting a 2D image into a 3D scene on a plane scaled automatically. Shape 3D Several basic primitive shapes for piecing a 3D scene together come with this node. Planes, cubes, spheres, cylinders, cones, and toruses are all within its reach. Text 3D The Text 3D is a 3D rendition of the Text+ node. This version supports beveling and extrusion yet lacks support for the multi-layered shading model that Text+ offers. Particles Wire a pRender node into a 3D view and it will push its particles out into the 3D environment. Those particles then get rendered by way of the Renderer3D rather than the Particle renderer.

For further detail, turn to Chapter 114, “Particle Nodes,” within the DaVinci Resolve Reference Manual; that content also lives at Chapter 54 of the Fusion Reference Manual.
