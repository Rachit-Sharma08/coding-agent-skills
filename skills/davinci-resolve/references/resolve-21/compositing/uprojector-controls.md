# Uprojector controls

Version: DaVinci Resolve 21 New Features Guide. Context: Uprojector.
[Chapter index](INDEX.md) / [Previous section](macro-edior-and-enter-a-name-for-your-macro.md) / [Next section](uprojector-and-ucatcher-and-createreliefmap.md)
<a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-fusion-part-2"></a> <a id="source-inputs"></a> <a id="source-uprojector-upj"></a>

### uProjector [uPj]

The uProjector node uProjector Node Introduction An image gets thrown onto USD geometry by the uProjector node. It serves plenty of ends: layering texture onto objects, spreading one texture over several separate objects, casting background plates from the camera’s vantage point, image-based rendering techniques, and beyond. The uProjector node is only one of a handful of nodes able to project images and textures, and each approach has its trade-offs. You can let projected textures “slide“ over an object as that object shifts relative to the uProjector, or instead bundle the pair into a uMerge so they move together and the texture stays pinned to the object. Grasping the uProjector node’s strengths and limits comes easiest when you treat the uProjector as a spin on the uDisk node.

- Lighting has to be switched on before any projection result shows up.
- Whatever light the projector emits counts as diffuse/specular light, which means it is

affected by the surface normals and can cause specular highlights.

- Switching Shadows on makes uProjector throw shadows.
- A uProjector’s projected light reaches every object sitting downstream of the uProjector

in the USD node tree.

- Within Light mode, the projected image’s Alpha values won’t clip geometry. Lean on Texture

mode instead.

- Should two projections overlap, their light contributions sum together.

For re-lightable textures, or textures bound for non-diffuse color channels (Specular Intensity or Bump, say), switch to the Texture projection mode instead:

- A Texture-mode projection lands only on objects whose material — in whole or in part — draws on the uCatcher node’s

output applied to that object.

- Such projections clip the geometry by the Alpha channel of the

projected image. The uCatcher node’s section holds further detail.

uCamera Projection vs. uProjection Node The uCamera node carries a projection feature of its own, and it’s the right pick when the projection should align to a camera, since this node grants finer command over aperture, film back, and clip planes. The uProjector node, by contrast, was built to serve as a custom light in USD scenes for layering and texturing, offering tighter control over light intensity, color, decay, and shadows.

### Inputs

Two inputs sit on the uProjector: one for the scene you’re projecting onto and one for the projected image. SceneInput: The orange scene input takes a USD scene. With a scene wired in here, any transformations placed on the spotlight ripple through the rest of the scene as well. ProjectiveImage: The white input looks for a 2D image to drive the projection, and this connection is mandatory.

### Basic Node Setup

By way of illustration, the uProjector node beneath casts a light (Background1) onto USD primitives. Every set element feeds into a uMerge, which pushes the projected set out into a larger scene holding camera, lights, and further elements. Routing the uProjector node into either uMerge node yields the same outcome. uProjector texturing groups of shapes to construct a set Inspector

uProjector controls

### Controls Tab

Color Ahead of being cast into the scene, the input image is multiplied by this color. Intensity This slider dials the projection’s Intensity whenever the Light and Ambient Light projection modes are active. Under Texture mode, the same option scales the texture’s Color values once they’ve been multiplied by the color. Exposure This alters how much light falls across a scene, much in the spirit of Intensity. Color Temperature/Enable This fixes a light source’s color temperature, defaulting to 6500K — daylight temperature. Diffuse Response This governs how much the light adds to a material’s Diffuse color. Specular Response This governs how much the light adds to a material’s Specular color. Decay Type By default a uProjector uses Quadratic Decay, so intensity tapers off with Distance. Linear decay reads similarly, whereas No Decay holds the light at one intensity everywhere in the scene. Decay Rate This is how fast the projected light fades across distance; a smaller decay rate makes the projection stronger. Shaping Focus Tweaking this draws the projection inward from its edges toward the centre. Shaping Cone Angle The Shaping Cone Angle is the width of the cone over which the projector pours out its full intensity; a bigger angle means a wider cone, capped at 180 degrees. Normalize Intensity Tick this checkbox and the projection’s Width and Height snap to default values. Clear it to expose separate Width and Height figures you can tune by hand. Fit Method The Fit Method decides how the projection seats inside the projection cone. Worth knowing up front: though this documentation might say “cone,” the uProjector and Camera USD nodes don’t actually project a cone — it’s nearer a pyramid of light whose apex rests at the camera/projector. The uProjector node forever projects a square pyramid of light, meaning its X and Y angles of view match. The Camera USD node’s pyramid of light, on the other hand, can come out non‑square depending on the camera’s Film Back. The aspect of whatever image feeds the uProjector/Camera USD leaves the pyramid’s X/Y angles alone; instead the image is scaled to seat within the pyramid per the fit options.

Should the pyramid’s aspect (AovY/AovX) and the image’s aspect (height _ pixelAspectY)/(width _ pixelAspectX) line up, the fit options aren’t needed and every one of them behaves identically. Once those two aspects diverge — the pyramid’s being set by the Film Back settings in Camera USD — the fit options start to matter. Take Fit by Width, which spreads the image’s width across the width of the Camera USD pyramid; here, if the image’s aspect ratio outstrips the pyramid’s, part of the projection spills vertically beyond the pyramid. There are five options:

- Inside: Scales the image evenly so its longest side just fits within the cone. Put differently, the picture grows as large as it can while still staying entirely inside the light's pyramid. Because of this, no area beyond that pyramid will ever pick up any of the projected light.
- Width: Scales the image evenly so its width sits within the cone. Keep in mind the picture may still spill past the cone along its height.
- Height: Scales the image evenly so its height sits within the cone. Keep in mind the picture may still spill past the cone along its width.
- Outside: Scales the image evenly so its shortest side fits within the cone. Put another way, the picture shrinks as much as it can while still ensuring it blankets the whole pyramid (that is, the pyramid sits fully within the image). As a result, every pixel of any object inside the light's pyramid is always lit.
- Stretch: Scales the image unevenly so that it precisely fills the projector's cone.
