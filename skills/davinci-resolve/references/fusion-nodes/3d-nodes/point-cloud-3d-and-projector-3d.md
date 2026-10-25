# Point cloud 3D and projector 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Point cloud 3D, Projector 3D.
[Chapter index](INDEX.md) / [Previous section](override-3d-and-point-cloud-3d.md) / [Next section](projector-3d-controls.md) / [Continue Projector 3D 3Pj / Projection Mode](projector-3d-controls.md) / [Point Cloud 3D 3PC](override-3d-and-point-cloud-3d.md)
<a id="source-additional-toolbar-and-shortcuts"></a> <a id="source-basic-node-setup-4"></a> <a id="source-camera-projection-vs-projection-3d-node"></a> <a id="source-controls-tab-4"></a> <a id="source-inputs-4"></a> <a id="source-inspector-3"></a> <a id="source-projector-3d-3pj"></a> <a id="source-projector-3d-controls"></a> <a id="source-projector-3d-node-introduction"></a> <a id="source-the-projector-3d-node"></a>

### Additional Toolbar and Shortcuts

Each action below is paired with its shortcut key:

- Delete Selected Points — Del
- Select All — Shift+A
- Find Points — Shift+F
- Rename Selected Points — F2
- Create New Point — Shift+C
- Toggle Names on None/Selected/Published/All Points — Shift+N
- Toggle Locations on None/Selected/Published/All Points — Shift+L
- Publish Selected Points — Shift+P
- Unpublish Selected Points — Shift+U
- Create a Shape at Selected Points — Shift+S
- Create and Fit an ImagePlane to Selected Points — Shift+I
- Create a Locator at Selected Points — Shift+O

### Projector 3D [3Pj]

### The Projector 3D node

### Projector 3D Node Introduction

You use the Projector 3D node to cast an image onto 3D geometry. There are plenty of uses for this: layering multiple textures onto objects, spreading one texture over several separate objects, casting background plates from the camera’s vantage point, image-based rendering tricks, and beyond. The Projector node is merely one among several nodes able to cast images and textures, each method bringing its own pros and cons. For further reading, turn to Chapter 85, “3D Compositing Basics,” within the DaVinci Resolve Reference Manual, or else Chapter 25 of the Fusion Reference Manual. You can let projected textures “slide“ across the object whenever the object shifts relative to the Projector 3D, or instead bundle the two inside a Merge 3D so they travel together and the texture stays pinned to the object. Grasping what the Projector 3D node can and can't do comes easiest if you treat the Projector as a flavor of the SpotLight node. Because the Projector 3D node is in truth a light, several notable things follow when it runs in Light or Ambient Light projection mode:

- Lighting has to be switched on before the projection's results show up.
- The light the projector throws counts as diffuse/specular light. That means it's

swayed by the surface normals and can generate specular highlights. If you'd rather avoid that, set the Projector 3D to project into the Ambient Light channel.

- Switching on Shadows makes Projector 3D cast shadows.
- As with any other light, the light a Projector 3D emits reaches only objects feeding into the first Merge 3D that lies downstream of the Projector 3D node in the node tree.
- Turning on the Merge 3D’s Pass Through Lights checkbox lets the projection illuminate objects further downstream.
- The light a Projector 3D emits is steered by the Lighting options settings on objects together with the Receives Lighting options on materials.
- In Light or Ambient Light mode, Alpha values within the projected image don't clip geometry. Reach for Texture mode instead.
- When two projections overlap, their light contributions sum together.

To cast re-lightable textures or textures for non-diffuse color channels (Specular Intensity or Bump, say), turn to the Texture projection mode instead:

- A projection in Texture mode lands only on objects that use the Catcher node's output for some or all of the material applied to that object.
- A Texture mode projection clips the geometry by the Alpha channel of the projected image.

Consult the section covering the Catcher node for more detail.

### Camera Projection vs. Projection 3D Node

The Camera 3D node offers a projection feature too, and it's the one to reach for when the projection should match a camera, since this node grants more say over aperture, film back, and clip planes. The Projector 3D node, on the other hand, was built to serve as a custom light in 3D scenes for layering and texturing, giving you finer control over light intensity, color, decay, and shadows.

### Inputs

The Projector 3D carries two inputs: one for the scene you're casting onto and one for the image being cast. SceneInput: The orange scene input takes a 3D scene. Wire a scene here and transformations applied to the spotlight ripple through to the rest of the scene as well. ProjectiveImage: The white input anticipates a 2D image to drive the projection. This connection is mandatory.

### Basic Node Setup

For instance, the Projector 3D node below casts a texture (MediaIn2) onto 3D primitives to fashion a simple 3D set. Every set element wires into a Merge 3D, which sends the projected set out into a bigger scene holding a camera, lights, and other elements. Alternatively, you could drop the Projector 3D node between the two Merge 3D nodes; doing so, though, would let the transform controls in the Projector 3D node act on the whole scene.

Projector 3D texturing groups of shapes to construct a set

### Inspector

### Projector 3D controls

### Controls Tab

Enabled With this checkbox on, the projector acts on the scene; clear it to switch the projector off. It's not the same thing as the red switch at the Inspector's upper-left corner. That red switch shuts the tool down entirely and hands the image along untouched, whereas the Enabled checkbox covers only the effect portion of the tool. Other parts, such as scripts in the Settings tab, keep processing as usual. Color The input image gets multiplied by this color ahead of being cast into the scene. Intensity This slider sets the projection's Intensity while the Light and Ambient Light projection modes are in use. Under Texture mode, the option scales the texture's Color values once they've been multiplied by the color. Decay Type A projector starts out at No Falloff, so its light hits geometry with the same intensity no matter how far the geometry sits from the projector. To make the intensity drop off over distance, switch the Decay type to either Linear or Quadratic modes. Angle The node's Cone Angle is the breadth of the cone within which the projector puts out its full intensity. A larger angle widens the cone angle, up to a ceiling of 90 degrees. Fit Method The Fit Method decides how the projection is fitted inside the projection cone.

The first point to grasp is that even though this documentation might say “cone,” the Projector 3D and Camera 3D nodes don't actually cast a cone; what they cast is closer to a pyramid of light whose apex sits at the camera/projector. The Projector 3D node forever casts a square pyramid of light—that is, its X and Y angles of view match. The Camera 3D node's pyramid of light can come out non‑square according to how the camera's Film Back is set. The aspect of the image wired into the Projector 3D/Camera 3D doesn't shift the pyramid's X/Y angles; rather, the image is scaled to fit the pyramid per the fit options. Whenever the pyramid's aspect (AovY/AovX) and the image's aspect (height _ pixelAspectY)/ (width _ pixelAspectX) coincide, the fit options aren't needed and they all behave identically. But once the image's aspect and the pyramid's (as governed by the Film Back settings in Camera 3D) differ, the fit options start to matter. Fit by Width, for one, fits the image's width across the width of the Camera 3D pyramid; here, if the image has a larger aspect ratio than the pyramid does, part of the projection spills vertically past the pyramid. Five options exist:

- Inside: The image is scaled uniformly so its largest dimension just fits inside the cone. Put another way, it scales the image as large as it can while keeping the image entirely inside the pyramid of light. The upshot is that nothing beyond the pyramid of light ever catches any projected light.
- Width: The image is scaled uniformly so its width fits inside the cone. Mind that the image may still spill past the cone along its height.
- Height: The image is scaled uniformly so its height fits inside the cone. Mind that the image may still spill past the cone along its width.
- Outside: The image is scaled uniformly so its smallest dimension just fits inside the cone. Put another way, it scales the image as small as it can while still covering the whole pyramid (so the pyramid sits entirely within the image). The upshot is that every pixel of every object inside the pyramid of light is always lit.
- Stretch: The image is scaled non-uniformly so it covers the projector's cone exactly.
