# Lighting multiple merge3d nodes and transforming merge3d scenes

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](an-overview-of-3d-compositing-and-3ds-max-or-lightwave.md) / [Next section](3d-view-navigation-camera-and-light-transforms.md)
<a id="source-a-3d-viewers-default-perspective-view"></a> <a id="source-lighting-multiple-merge3d-nodes"></a> <a id="source-loading-3d-nodes-into-the-viewer"></a> <a id="source-opengl-renderer"></a> <a id="source-opengl-uv-renderer"></a> <a id="source-software-renderer"></a> <a id="source-software-vs-gpu-rendering"></a> <a id="source-the-3d-viewer"></a> <a id="source-the-renderer3d-node"></a> <a id="source-the-transform-tab-of-a-merge3d-node"></a> <a id="source-transforming-merge3d-scenes"></a> <a id="source-transforming-upstream-lighting-downstream"></a>

### Lighting Multiple Merge3D Nodes

After you've joined several Merge3D nodes, there's a simple mechanism for governing the degree to which lights wired into upstream Merge3D nodes reach the output of other Merge3D nodes sitting downstream. The Controls tab of every Merge3D node holds one checkbox, Pass Through Lights, that allows lighting to carry through an upstream Merge3D node's output so it falls on objects attached to downstream Merge3D nodes.

Switching on Pass Through Lights lets lights wired into upstream Merge3D scenes illuminate the downstream Merge3D scenes too By default this checkbox is off, so you can light objects in one Merge3D scene without fretting over whether that lighting bleeds onto geometry hooked into other Merge3D nodes further down the chain. As an illustration, you might want a spotlight to brighten a building wall inside one Merge3D node and not have it spill across the grass or pavement at the base of that wall built in a separate Merge3D node. In the figure below, the left image shows the cone and torus wired to a downstream node staying dark beneath the light in an upstream node while Pass Through Lights is off, whereas the right image shows everything lit once Pass Through Lights is switched on.

On the left, lights striking the text inside one Merge3D node leave the cone and torus that were added in a downstream Merge3D node untouched. On the right, switching Pass Through Lights on within the upstream Merge3D node causes those same lights to fall on the downstream shapes as well.

### Transforming Merge3D Scenes

A Transform tab is part of every Merge3D node. The transform parameters there move, scale, and rotate every object gathered inside that Merge3D node as a group, lighting and particles included. Each of these transformations pivots around one shared point. That mechanism underpins parenting throughout the 3D environment. When you transform a Merge3D node that's wired to other Merge3D nodes, the outcome hinges on whether the node you're transforming is upstream or downstream:

- Transform a downstream Merge3D node and every upstream node feeding it moves along too, behaving as though the whole thing were one scene.
- Transform an upstream Merge3D node, by contrast, and the downstream Merge3D nodes stay put, which lets you confine a transform to just that one node's scene.

### The Transform tab of a Merge3D node

### Transforming Upstream, Lighting Downstream

In intricate scenes made from many combined Merge3D nodes, a frequent approach is to reserve one final downstream node for gathering the light and camera nodes that illuminate the finished scene, while keeping the upstream Merge3D nodes available for handling object transforms and animation. That way you can move and animate portions of the overall scene without the risk of inadvertently disturbing the scene's master lighting setup or cameras — unless of course you've deliberately wired upstream lights or cameras that are supposed to travel with the geometry you're transforming.

A sample 3D scene driven by several cooperating Merge3D nodes; the upstream Merge3D nodes lay out the 3D objects in the scene, and the final Merge3D node (orange) handles the framing and lighting.

### The Renderer3D Node

Each 3D node you place emits a full 3D scene. That differs from most conventional 3D modeling and animation software, where every object lives within a single global scene environment. What it means is that the scene from a Camera 3D node and the scene from an image plane stay independent until a Merge3D node fuses them into one scene, and that Merge3D node itself emits a complete 3D scene. This 3D scene data, however, can't be composited against the other 2D images in your comp, nor can it be rendered out, until a Renderer3D node first renders it inside the node tree. Put more precisely, 3D nodes that emit 3D scenes can't be wired straight into inputs expecting 2D images. As an example, an ImagePlane3D node's output won't connect directly to a Blur node's input, and a Merge3D node's output won't connect straight into an ordinary Merge node. You first have to drop a Renderer3D node at the tail of your 3D scene to convert it into 2D images, which you can then composite and tweak exactly like any other 2D image in the comp.

A Merge3D output wired into a Renderer3D node so the result becomes 2D image data To make its image, the Renderer3D draws on one of the scene's cameras (usually one wired to a Merge3D node). When it locates no camera, it falls back to a default perspective view. Because that fallback view seldom lands on a helpful angle, most artists construct their 3D scenes with a camera or more included. Whatever the Renderer3D outputs can be set to any resolution, with choices for fields processing, color depth, and pixel aspect.

### Software vs. GPU Rendering

With the Renderer3D node you pick either a software renderer or an OpenGL renderer, swapping some measure of rendered image quality for speed, and swapping depth of field rendering for soft shadow rendering, according to what a given piece of your comp calls for. You pick the rendering method from a Renderer Type pop-up menu, which the Inspector shows on the Controls tab among each Renderer3D node's parameters. Software Renderer is the default.

The Renderer Type option in the Controls tab of a Renderer3D node

### Software Renderer

For producing the final output, the software renderer is the usual pick. The software renderer isn't the speediest way to render, but it carries two benefits. The first is that the software renderer copes easily with textures far bigger than half your GPU's largest texture size, so reach for the software renderer whenever your texture images run past 8K and you want the best possible quality.

The second benefit is that you need the software renderer to render "constant" and "variable" soft shadows whose Spread is adjustable, something the OpenGL renderer simply can't do. Such soft shadows look more natural; you switch them on within the Shadows parameters in the Controls tab of light nodes, where you pick a Sampling Quality and a Softness type and set the Spread, Min Softness, and Filter Size sliders. The software renderer also honors alpha channels inside shadow maps, so transparency can vary how dense a shadow appears.

With the Renderer3D node "Renderer Type" drop-down on OpenGL Renderer, soft shadows and outsized textures are off the table (left). Switch that same dropdown to Software Renderer, and higher-quality textures plus soft shadows become available (right).

### OpenGL Renderer

To render the image, the OpenGL renderer leans on your machine's GPU; the geometry and textures get uploaded to the graphics card, and OpenGL shaders then generate the output. This path can yield high-quality images that work perfectly for final rendering, and it can run potentially many times quicker than the software renderer, though it does come with restrictions on certain rendering effects — soft shadows can't be drawn, and the OpenGL renderer additionally disregards alpha channels while rendering shadows, so a shadow is always thrown by the whole object. Because it's so fast, on the other hand, the OpenGL renderer surfaces extra Accumulation Effects controls that switch on depth of field rendering for shallow-focus looks. The snag is that you can't get soft shadow rendering and depth of field rendering at the same time, so for any one 3D scene you render you'll have to decide which matters more. Don't Forget That You Can Combine Rendered Scenes in 2D It might feel like a hard wall that one renderer can't put out both soft shadows and depth of field, but remember that you're free to build several 3D scenes — each on a different renderer — and bring them together in 2D afterward. Beyond that, you can also render auxiliary channels that feed 2D image processing nodes such as AmbientOcclusion, DepthBlur, and Fog, building pseudo-3D effects from the images you've rendered.

### OpenGL UV Renderer

Pick the OpenGL UV Renderer option, and a Renderer3D node puts out an "unwrapped" rendition of the textures sitting on the upstream objects, at whatever resolution you've set in the Image tab of that Renderer3D node.

On the left, a 3D scene rendered the usual way; on the right, that very scene put through the Renderer3D node's OpenGL UV Renderer mode That special output image serves to bake texture projections or materials down to a texture map, for either of two purposes:

- Baking out projections can speed up a render.
- Baking projections down also frees you to edit the texture with the comp's other 2D nodes,

or even through third-party paint software (assuming you write this image out on its own as a graphics file) before you map it back onto the geometry. Imagine, say, that you've got a scene at a street corner where a shop sign carries a phone number you'd like to alter. Track the scene, hold standing geometry for the sign, and you can project the footage onto that geometry, run a UV render, swap the digits with a Paint node, and then reapply the result to the mesh through a Texture2D. Retouching textures is another job the UV renderer handles well. You might stitch together several DSLR stills of a place, project them all onto the mesh, render out the UV, fix up the seams, and reapply it to the mesh. Or you could project tracked footage of a road full of cars, UV render the projection off the geometry, run a temporal median filter over the frames, and lay a "clean" road surface back down.

### Loading 3D Nodes into the Viewer

Loading a 3D node into the viewer flips it to a 3D Viewer, where you can pan, zoom, and spin the scene in 3D so that making adjustments in three dimensions is straightforward.

### The 3D Viewer

How well the interactive 3D Viewer performs hinges heavily on the machine's graphics hardware, since it depends on OpenGL support. Your workstation GPU's onboard memory, along with its speed and feature set, dramatically affects how fast and capable the 3D Viewer is. Load any node carrying a 3D output into any viewer and that viewer's display type changes to a 3D Viewer. At first, the scene's contents show through a default perspective view.

### A 3D Viewer's default perspective view

You change the viewpoint by right-clicking inside the viewer and picking the viewpoint you want from those offered in the Camera submenu. As a shortcut to that Camera submenu, right-click the axis label shown in the viewer's bottom corner.

Right-click the Axis label of the viewer to change the viewpoint Alongside the standard Perspective, Front, Top, Left, and Right viewpoints, any cameras and lights present in the scene as candidate viewpoints appear too. You can even view the scene through a Merge3D or Transform3D by choosing it from the contextual menu's Camera > Other submenu. Moving through the scene and observing it from a range of viewpoints aids positioning, alignment, and lighting, plus other facets of your composite.

Cameras, lights, plus Merge3D and Transform3D nodes you're able to jump to all appear in the Perspective drop-down menu as well.
