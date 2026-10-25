# Urenderer image tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Urenderer.
[Chapter index](INDEX.md) / [Previous section](urenderer.md) / [Next section](urenderer-and-ureplacematerial-and-ushape.md) / [uRenderer uRn](urenderer.md)
<a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-image-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-usd-renderer-controls"></a> <a id="source-usd-renderer-image-controls"></a>

### Inputs

Two inputs feed the uRenderer node. Its primary scene input accepts the uMerge or whatever other USD nodes require conversion to 2D, while the effect mask constrains the uRenderer output. SceneInput: A required input, the orange scene input takes in a USD scene you intend to convert to 2D. EffectMask: A 2D image fed to the blue effects mask input masks the node's output.

### Basic Node Setup

A uRenderer node has to close out every USD scene. Its role is to turn a 3D scene into a 2D image. In the example below, the uRenderer node receives the output of a uMerge node and renders the 3D scene as a 2D image.

Here the uRenderer node receives what the uMerge node feeds it and collapses it down to a 2D image for display.

### Inspector

### USD Renderer controls

### Controls Tab

Camera Use the Camera menu to pick which of the scene's cameras renders the image. With the Default setting, the first camera the scene contains is used; when none is found, the default perspective view steps in instead.

Renderer Type The render engines on offer are listed in this menu. At present, Storm is the sole renderer available. Output AOVs As Layers Permits AOVs to come out as layers, leaving you free to render every required element from a single uRenderer. Tick the Output AOVs as Layers checkbox and each existing AOV emerges as its own separate layer. AOV AOV, or Arbitrary Output Variable, refers to extra passes the render can produce; these go by Deep Channels or Auxiliary channels as well. Color is one example; Depth and Camera Depth are others.

- Color: Produces the chief full-color render of the USD scene, textures and lighting included
- Depth: Produces a black-and-white depth map. This depth map gets normalized on every frame, presenting dynamic black-to-white values.
- PrimID: Produces a numeric value per distinct prim within the USD scene.
- Camera Depth: Produces a precise camera depth map, computing where the camera sits

relative to the USD scene. Rendered as a float 32bit image, it looks black on first sight. Lighting Governs the manner in which the USD scene gets lit.

- None: Disables all lighting.
- Camera: Enabled objects are lit by the default camera light
- Scene: Enabled objects are lit by any lights in the USD scene.
- Enable Sky Dome: When ticked, the sky dome texture shows up and is rendered

out of the uRenderer. Complexity Sets the level of detail rendered: Low, Medium, or High detail. Aux Channel Z Switching this option on renders the Z channel, the depth channel that captures how far each pixel sits from the camera. With it enabled, the camera depth map renders to the Z channel. Film Back Fit Sets how the rendered image is fitted to the camera's Film Back. When the rendered images don't share the same relative dimensions as the film back, these options decide how the image should be fitted. Max Iterations Sets how many iterations of the rendering algorithm get processed.

### USD Renderer Image controls

### Image Tab

Process Mode: Picks whether the node's output is handled as Full Frames or through one of the listed interlaced methods. Image: Governs the output image's size and aspect ratio.

- Width/Height: Sets the pixel dimensions of the node's output.
- Pixel Aspect XY: Sets a custom pixel aspect ratio for non-square video formats.
- Auto Resolution: Matches the resolution to the Timeline resolution. Clear it to set the

width/height above by hand.

- Depth: Sets the bit depth of the uRenderer's output by hand.

Domain Overscan Permits extra pixels to render beyond the data window, useful for things like camera stabilization and lens distortion operations. Overscan Permits extra pixels to render beyond the display window, useful for things like camera stabilization and lens distortion operations. Render Color Space Lets you render the output into Linear or sRGB color spaces.

Source Color Space The Color Space Type menu fixes the media's color space to support a linear workflow. Unlike the Gamut tool, it performs no actual color space conversion; instead it writes the source space data into the metadata when that metadata isn't already there. Downstream, that metadata can then feed a Gamut tool set to From Image, or a Saver where explicit output spaces have been defined.

- Auto: Passes along any metadata that might be in the incoming image.
- Space: Lets the user pick the color space among an assortment of options.

Source Gamma Space The Curve Type menu either detects automatically or lets you pick the image's Gamma setting, and offers the choice to strip the Gamma curve away to support a linear workflow.

- Auto: Carries forward whatever metadata the incoming image may hold.
- Space: Lets you pick a particular setting from a Gamma Space drop-down menu, while a

visual graph shows you a depiction of the gamma setting you chose.

- Log: Much like the Log-Lin node, this option surfaces particular log-encoded gamma profiles so

you can pick whichever one suits your content. A visual graph depicts the log setting you chose. Pick Cineon from the Log Type menu and extra options appear for fine-tuning the gamma output: Lock RGB, Level, and Soft Clip, along with Film Stock Gamma, then Conversion Gamma plus a Conversion table.

- Remove Curve: Based on the chosen gamma space, or the gamma space detected under Auto mode, the matching gamma curve is stripped from the material, in effect converting it to output in a linear color space.
- Pre-Divide/Post-Mujltiply: Where needed, lets you turn "straight" Alpha channels into pre-multiplied Alpha channels.
