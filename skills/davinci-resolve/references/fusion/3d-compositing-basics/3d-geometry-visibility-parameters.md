# Common visibility parameters and a 3D geometry nodes visibility parameters

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](refraction-and-bump-maps.md) / [Next section](importing-an-fbx-scene-fbx-scene-import-dialog.md) / [Continue Importing an FBX Scene / FBX Scene Import Dialog](importing-an-fbx-scene-fbx-scene-import-dialog.md)
<a id="source-a-3d-geometry-nodes-visibility-parameters"></a> <a id="source-adding-fbx-models"></a> <a id="source-common-visibility-parameters"></a> <a id="source-importing-an-fbx-scene"></a>

### Common Visibility Parameters

Visibility parameters live within the Controls tab on most 3D geometry-producing nodes, surfaced through a disclosure control. Those parameters let you steer an object’s visibility within the viewers and within the final render.

### A 3D geometry node’s visibility parameters

Visible Leave the Visibility checkbox unticked and the object won’t show within a viewer, nor will a Renderer3D render it into the output image. An object that isn’t visible throws no shadows. This is usually on by default, so the objects you build show within both the viewers and final renders. Unseen by Cameras Tick the Unseen by Cameras checkbox and the object will show within the viewers but go invisible when the scene gets viewed through a camera, so a Renderer3D will not render the object into the output image. Shadows an Unseen object throws will still show. Cull Front Face/Back Face Lean on these options to cull (leave out) rendering of certain polygons within the geometry. Tick Cull Back Face and every polygon whose normals face away from the view will go unrendered and throw no shadows. Tick Cull Front Face and every polygon whose normals face away from the view will likewise get left out. Ticking both checkboxes lands the same outcome as unticking the Visible checkbox. Ignore Transparent Pixels in Aux Channels For any bit of geometry, the Renderer3D throws out transparent pixels within the auxiliary image channels. The reason this is the default is to keep aux channels (such as normals, Z-channel, UVs) from filling in where blank space or full transparency belongs. As an example, say in post you want to lend some fog onto the rendered image. Had you fully transparent geometry up front touching the Z-channel, you’d land incorrect fog rendering. Untick this checkbox and the transparency goes unconsidered while every aux channel gets filled across every pixel. That could pay off where you wanted to swap the texture on a 3D element that’s fully transparent across certain areas for a texture that’s transparent across different areas; having the whole object set aux channels (UVs in particular) would come in handy.

### Adding FBX Models

The Filmbox FBX format is a scene interchange format that eases moving 3D scene information from one application across to another. Fusion’s FBX format support stretches model import support over to other 3D files such as Collada and OBJ.

### Importing an FBX Scene

To bring in a whole FBX scene, you add an FBXMesh3D node onto your node tree. Once prompted to pick a scene or object file, Fusion brings it in to build a composition carrying the same lights, cameras, materials, and geometry held within an FBX file.
