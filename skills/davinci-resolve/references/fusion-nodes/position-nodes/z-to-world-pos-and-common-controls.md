# Z to world pos and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Z to world pos, Common controls.
[Chapter index](INDEX.md) / [Previous section](volume-fog-and-volume-mask-and-z-to-world-pos.md) / [Z to World Pos Z2W](volume-fog-and-volume-mask-and-z-to-world-pos.md) / [Next section](common-controls-motion-blur.md)
<a id="source-different-coordinate-spaces"></a> <a id="source-inspector-1"></a> <a id="source-position-nodes-common-settings-tab"></a> <a id="source-position-nodes-part-2"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-invisible-sphere"></a> <a id="source-the-scene-input"></a> <a id="source-what-is-a-wpp"></a> <a id="source-wpp-concept"></a>

### WPP Concept

For footage carrying XYZ Position channels, the Position nodes in Fusion open up a wholly fresh approach to working with masks and Volumetrics. Z to World provides the means to build those channels out of a Z channel together with 3D Camera information. Across this overview, we call the World Position Pass the WPP.

### What Is a WPP?

Every pixel’s XYZ position in 3D space is read by the WPP as an RGB color value. For example, a pixel located at 0/0/0 produces a pixel whose RGB value is 0/0/0, so it comes out black. A pixel located at 1/0/0 within the 3D scene yields a pixel that’s fully red. Naturally, when a pixel’s coordinates run to something like -60/75/123, the WPP reads those numbers as RGB color values too. Given how vast a 3D scene can become, the WPP channel ought always to be rendered in 32-bit floating point to deliver the needed accuracy. The image below presents a 3D rendering of a scene centered at 0/0/0 in 3D Space together with its matching WPP. For clearer viewing, the WPP here has been normalized.

### Different Coordinate Spaces

WPPs can be rendered across different Coordinate Spaces. Among these are World Space, Eye Space, and Object Space. The image below shows how those various spaces look, though the nodes in Fusion call for the WPP to be rendered in World Space.

### The Scene Input

These nodes provide a Scene input, which may be either a 3D camera or a 3D scene that holds a camera. While the Z to World node depends on the camera, Volume Mask and Volume Fog can produce their output with no camera attached at all, or with the camera position left at 0/0/0. Even so, attaching a camera that aligns with the original camera the WPP was rendered from, or setting the camera’s position yourself, sharpens the accuracy and look of the resulting fog or mask dramatically.

### The “Invisible Sphere”

So far the example scene carries an empty background, meaning nothing sits in the scene beyond the ground plane and the cubes. Apply fog to a scene like that, one larger than the ground plane, and the outcome resembles the “w/o Sphere” example below, since, lacking any WPP information out past the ground plane, the value that results comes to 0/0/0, so the fog spills into that region as well.

To work around that, drop an invisible bounding sphere into your scene so it generates “dummy” WPP values that help the Fog node build the right volume, as the “with Sphere” example below demonstrates.

### The Common Controls

Several identical controls in the Inspector are shared by the nodes that perform Position operations. This section covers the controls common across Position nodes.

### Inspector

### Position nodes Common Settings tab

### Settings Tab

Found on every tool in the Position category, the Settings tab lives in the Inspector. Its controls stay consistent and behave the same way for each tool.

Blend The Blend control mixes between the tool’s untouched image input and the tool’s final, altered output. Set the blend value to 0.0 and the result coming out matches the image going in exactly. As a rule this makes the tool bypass processing completely and pass the input directly through to the output. Process When Blend Is 0.0 Here the tool still runs even though the input value reads zero. That comes in handy when a node is scripted to kick off a task while its value sits at 0.0. Red/Green/Blue/Alpha Channel Selector Use these four buttons to confine the tool’s effect to particular color channels. The filtering typically takes place after the tool itself has run. As an illustration, deselecting the Red button on a Blur tool causes the blur to hit the image first, after which the red channel from the original input is laid back over the red channel of the outcome. Certain exceptions exist, namely tools where deselecting these channels makes the tool skip that channel’s processing outright. Such tools usually carry a matching set of RGBA buttons on the tool’s Controls tab, and in that situation the buttons on the Settings and Controls tabs match. Apply Mask Inverted Switching on Apply Mask Inverted flips the tool’s entire mask channel. That mask channel is the merged product of every mask either fed into or built inside a node. Multiply by Mask Turning this on multiplies the masked image’s RGB values by the values of the mask channel, so every pixel left out of the mask (that is, set to 0) turns black/transparent. Use Object/Use Material (Checkboxes) Certain 3D applications can write to file formats carrying extra channels. The EXR format in particular holds Object and Material ID channels, which work as a mask for the effect. These checkboxes decide whether those channels get used when present, and the precise Material ID or Object ID involved is picked with the controls that follow. Correct Edges This checkbox shows up only once the Use Object or Use Material checkboxes are active. It switches the technique used for handling overlapping object edges within a multi-object image. With it on, the Coverage and Background Color channels help isolate and refine the effect along an object’s edge. Leave it off (or lack any Coverage or Background Color channels) and aliasing can show up along the mask’s edge. For deeper detail on the Coverage and Background Color channels, turn either to Chapter 78, "Understanding Image Channels," found within the DaVinci Resolve Reference Manual, or else to Chapter 18 over in the Fusion Reference Manual Object ID/Material ID (Sliders) These sliders let you pick which ID builds a mask out of an image’s object or material channels. The Sample button works just like the Color Picker, pulling IDs from whatever the viewer is showing. Note that the image or sequence has to have been rendered by a 3D software package that included those channels.
