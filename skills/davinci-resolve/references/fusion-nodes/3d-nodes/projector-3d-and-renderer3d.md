# Projector 3D and renderer3d

Version: DaVinci Resolve 20.3 Reference Manual. Context: Projector 3D, Renderer3d.
[Chapter index](INDEX.md) / [Previous section](projector-3d-controls.md) / [Next section](renderer3d-anti-aliasing.md) / [Continue Renderer3D 3Rn / OpenGL UV Renderer](renderer3d-anti-aliasing.md) / [Projector 3D 3Pj](point-cloud-3d-and-projector-3d.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-lighting"></a> <a id="source-opengl-controls"></a> <a id="source-render-3d-controls"></a> <a id="source-render-3d-open-gl-controls"></a> <a id="source-renderer3d-3rn"></a> <a id="source-renderer3d-node-introduction"></a> <a id="source-software-controls"></a> <a id="source-the-renderer-3d-node"></a>

### Common Controls

Transform and Settings Tabs A great many 3D nodes share the leftover Transform and Settings tabs. You’ll find them described under this chapter’s closing “The Common Controls” section.

### Renderer3D [3Rn]

### The Renderer 3D node

### Renderer3D Node Introduction

Taking the 3D environment and turning it into a 2D image is the job of the Renderer 3D node, which uses either a default perspective camera or a camera already in the scene. Each 3D scene within a composition wraps up with one or more Renderer 3D nodes. To generate the final image, the Renderer node carries both a software and an OpenGL render engine. Third-party plugins may furnish further render engines as well. The software render engine leans solely on the system’s CPU to produce its rendered images. Typically far slower than the OpenGL render engine, it nonetheless gives identical results on every machine, which makes it indispensable for renders that span a network. Soft shadows demand the Software mode, which on the whole handles all the available illumination, texture, and material features. By contrast, the OpenGL render engine taps the graphics card’s GPU processor to speed up rendering the 2D images. Results can shift a little between systems, hinging on precisely which graphics card sits inside. Outcomes from the OpenGL renderer can be swayed by the graphics card driver too. Thanks to the OpenGL render engine’s speed, tailored supersampling and lifelike 3D depth of field options become feasible. Soft shadows lie beyond the OpenGL renderer’s reach. When you need soft shadows, reach for the software renderer. As with the bulk of nodes, you’ll locate the Renderer’s motion blur settings beneath the Common Controls tab. Take note that for scenes holding particle systems, the Motion Blur settings on the pRender nodes have to line up precisely with those on the Renderer 3D node. If they don’t, the subframe renders clash and throw out unexpected (and incorrect) results. NOTE: The Open GL renderer honors the Color Depth option found in the Image tab of the Renderer 3D node. On some graphics cards this may drag down performance when rendering to int16 or float32.

### Inputs

Two inputs sit on the Renderer 3D node. Its primary scene input receives the Merge 3D, or any other 3D nodes, that you need flattened to 2D. Output from the Renderer 3D is constrained by the effect mask. SceneInput: This mandatory orange scene input takes a 3D scene you intend to convert into 2D. EffectMask: The blue effects mask input relies on a 2D image to mask whatever the node outputs.

### Basic Node Setup

Every 3D scene has to conclude with a Renderer 3D node. Its purpose is to turn a 3D scene into a 2D image. In the example below, the Renderer 3D node grabs a Merge 3D node’s output and renders that 3D scene as a 2D image.

Here a Renderer 3D sits immediately downstream of a Merge 3D, turning that 3D scene into a 2D image Multilayer Support By default the Renderer 3D tool emits layers and builds several lighting passes to set up for compositing. It turns out seven discrete layers: Shadow, Diffuse, Specular, Ambient, Reflect, Refract, and Fog. While the renderer still delivers a finished result, each pass that contributes to that image is now reachable on its own, handing you extra command over the end result. These layers can be previewed straight in the viewer via the layer preview control. To assemble a single combined output, employ any compositing node such as Merge, MultiMerge or Channel Booleans. Every pass should be ‘added’ together, save for Shadow, which has to be Multiplied.

### Inspector

### Render 3D controls

### Controls Tab

Camera Which of the scene’s cameras does the rendering is picked through the Camera menu. Choosing Default grabs the very first camera in the scene. Where no camera turns up, the fallback perspective view steps in. Eye Configuring how stereoscopic projects render happens via the Eye menu. Picking Mono disregards the camera’s stereoscopic settings. The Left and Right choices shift the camera according to the stereo Separation and Convergence options set in the camera, yielding either left- or right-eye output. Selecting Stacked layers the two images vertically rather than placing them side by side. Layers lets the left and right eyes emerge as separate layers. Reporting Whether the node writes warnings and errors generated during rendering to the console is governed by this section’s first pair of checkboxes. The second pair tells the node whether to halt rendering the moment a warning or error shows up. By default all four checkboxes on this node are on. Renderer Type The render engines on offer are enumerated by this menu. Fusion ships three of them: the software renderer, OpenGL renderer, and the OpenGL UV render engine. More renderers can arrive through third‑party plugins. Whatever controls appear under this drop-down menu come from the render engine itself. They shift according to what each renderer makes available. For that reason, every renderer gets its own write-up below.

### Software Controls

Output Channels Apart from the customary Red, Green, Blue, and Alpha channels, the software renderer is able to bake these further channels into the image. Switching on extra channels eats more memory and processing time, so reserve them for when they’re actually needed.

- RGBA: Selecting this directs the renderer to generate the image’s Red, Green, Blue, and Alpha color channels. Because they’re mandatory, these channels can’t be switched off.
- Z: Turning this on enables the Z-channel render. Each pixel in the Z-channel holds a value standing for that pixel’s distance away from the camera. Bear in mind the Z-channel values can’t carry anti-aliasing. Wherever several depths overlap in a pixel, the nearest depth value wins for that pixel.
- Coverage: Turning this on enables the Coverage channel render. Held within the Coverage channel is data about which Z-buffer pixels supply coverage (those overlapping other objects). It assists nodes leaning on the Z-buffer to deliver a touch of anti-aliasing. Each pixel’s value here reports, in percentage terms, how much of that pixel the foreground object makes up.
- BgColor: Turning this on enables the BgColor channel render. What this channel holds are the color values belonging to objects sitting behind the pixels covered in the Coverage channel.
- Normal: Turning this on enables the X, Y, and Z Normals channel render. Pixel values across these three channels signal the orientation (direction) of every pixel within 3D space. Each axis is captured by a color channel whose values span the range [–1,1].
- TexCoord: Turning this on enables the U and V mapping coordinate channel render. The texture coordinates of each pixel reside in these channels. Even though the 3D system handles texture coordinates internally as three-component UVW, Fusion images retain only the UV components. Those components land in the Red and Green color channel.
- ObjectID: Turning this on enables the ObjectID channel render. Any object in the 3D environment may receive a numeric identifier at creation time. The pixels of this floating-point image channel hold the values given to whichever objects formed the pixel. A blank pixel carries an ID of 0, and the channel accepts values up to 65534. A single Object ID can be shared across multiple objects. This buffer comes in handy for pulling mattes from the shapes of scene objects.
- MaterialID: Turning this on enables the Material ID channel render. Any material in the 3D environment may receive a numeric identifier at creation time. The pixels of this floatingpoint image channel hold the values given to whichever materials formed the pixel. A blank pixel carries an ID of 0, and the channel accepts values up to 65534. A single Material ID can be shared across multiple materials. This buffer is handy for pulling mattes off a texture; say, a mask gathering every pixel that makes up a brick texture.

### Lighting

- Enable Lighting: Ticking the Enable Lighting checkbox causes whatever lights exist in the scene to illuminate objects. With no lights around, every object renders black.
- Enable Shadows: Ticking the Enable Shadows checkbox has the renderer cast shadows, though it gives up a little speed.

### OpenGL Controls

### Render 3D Open GL controls

Output Channels On top of the customary Red, Green, Blue, and Alpha channels, the OpenGL render engine can likewise bake the channels below into the image. Activating extra channels draws on more memory and processing time, so keep them for occasions that truly call for them.

- RGBA: Picking this instructs the renderer to build the image’s Red, Green, Blue, and Alpha color channels. Being required, these channels cannot be turned off.
- Z: This switches on the Z-channel render. A value sits in each Z-channel pixel that conveys how far that pixel lies from the camera. Keep in mind anti-aliasing can’t be folded into the Z-channel values. Where multiple depths stack in one pixel, the closest depth value is what that pixel takes.
- Normal: This switches on the X, Y, and Z Normals channel render. The pixel values in these three channels point to the orientation (direction) each pixel holds in 3D space. Every axis is conveyed by a color channel whose values run from [–1,1].
- TexCoord: This switches on the U and V mapping coordinate channel render. Sitting in these channels are the texture coordinates of each pixel. Despite the 3D system handling texture coordinates internally as three-component UVW, Fusion images keep only the UV components. Those components get mapped onto the Red and Green color channels.
- ObjectID: This switches on the ObjectID channel render. At creation, each object in the 3D environment can take a numeric identifier. Sitting in this floatingpoint image channel are the values handed to whatever objects spawned the pixel. Blank pixels carry an ID of 0, and the channel reaches values as high as 65534. One Object ID may be shared among several objects. This buffer proves useful for drawing mattes from the shapes of objects in a scene.
- MaterialID: This switches on the Material ID channel render. At creation, each material in the 3D environment can take a numeric identifier. Sitting in this floating‑point image channel are the values handed to whatever materials spawned the pixel. Blank pixels carry an ID of 0, and the channel reaches values as high as 65534. One Material ID may be shared among several materials. This buffer proves useful for drawing mattes from a texture—for instance, a mask gathering every pixel forming a brick texture.
