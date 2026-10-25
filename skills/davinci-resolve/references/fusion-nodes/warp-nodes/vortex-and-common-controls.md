# Vortex and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vortex, Common controls.
[Chapter index](INDEX.md) / [Previous section](perspective-positioner-and-vector-distortion-and-vortex.md) / [Vortex Vtx](perspective-positioner-and-vector-distortion-and-vortex.md)
<a id="source-common-controls-4"></a> <a id="source-controls-tab-3"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-motion-blur"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-vector-distortion-controls-tab-1"></a> <a id="source-warp-common-controls-tab"></a>

### Inspector

### The Vector Distortion Controls tab

### Controls Tab

Parameters for tuning the position, size, and strength of the Vortex effect appear on the Controls tab. Center X and Y This control places the center of the Vortex effect on the image. By default it sits at 0.5, 0.5, which puts the effect in the image's center. Size Size alters how large an area the Vortex affects. You can drag the effect's circumference in the viewer or work the Size slider. Angle Drag the rotation handle in the viewer or work the thumbwheel control to alter how much rotation the Vortex carries. A higher angle value means a stronger swirling effect. Power Pushing the Power slider up shrinks the Vortex while tightening it. In effect it concentrates the swirl within the given image area.

### Common Controls

Settings Tab Other Warp nodes share the same Settings tab found in the Inspector. Full coverage of these common controls appears in the following "The Common Controls" section.

### The Common Controls

A number of identical controls in the Inspector are shared across nodes that perform Warp operations. The controls common to Warp nodes are covered in this section.

### Inspector

### Warp Common Controls tab

### Settings Tab

Every tool in the Warp category carries the Settings tab found in the Inspector. Even third-party Warp-type plugin tools include these Settings controls. They stay consistent and behave the same way for every tool. Blend The Blend control mixes between the original image fed into the tool and the modified output the tool finally produces. Where the blend value sits at 0.0, the outgoing image matches the incoming image exactly. Usually this will make the tool skip processing altogether, passing the input directly through to the output.

Process When Blend Is 0.0 Even with the input value at zero, the tool still processes. This proves handy when the node is scripted to set off a task, while the node's value reads 0.0. Red/Green/Blue/Alpha Channel Selector Use these four buttons to confine the tool's effect to chosen color channels. Typically this filter takes hold once the tool has finished processing. For instance, with the Red button on a Blur tool deselected, the blur will apply to the image first, and afterward the original input's red channel will be copied back across the result's red channel. Exceptions exist, such as tools for which deselecting these channels makes the tool skip processing that channel altogether. Tools of that sort will usually carry an identical set of RGBA buttons on the tool's Controls tab. In such a case, the buttons on the Settings and the Controls tabs match. Apply Mask Inverted Turning on the Apply Mask Inverted option flips the tool's entire mask channel. That mask channel combines every mask connected to or created within a node. Multiply by Mask Choosing this option will have the masked image's RGB values multiplied by the mask channel's values. This will turn every image pixel left out of the mask (that is, set to 0) black/transparent. Use Object/Use Material (Checkboxes) Certain 3D software can render to file formats carrying extra channels. The EXR file format notably supports Object ID and Material ID channels, usable as a mask for the effect. Whether those channels will be used, when present, is governed by these checkboxes. Which specific Material ID or Object ID is affected gets picked through the Object and Material ID sliders explained below. Correct Edges This checkbox surfaces only once the Use Object or Use Material checkboxes are on. It switches the method used for handling overlapping object edges within a multi-object image. With it on, the Coverage and Background Color channels serve to separate and refine the effect along the object's edge. Where this option is off (or no Coverage or Background Color channels exist), the mask's edge may show aliasing. To dig deeper into how the Coverage and Background Color channels work, turn to Chapter 78, "Understanding Image Channels," within the DaVinci Resolve Reference Manual, or else Chapter 18 over in the Fusion Reference Manual.

Object ID/Material ID (Sliders) These sliders pick which ID will build a mask out of an image's object or material channels. Operate the Sample button just like the Color Picker: to lift IDs from the image shown in the viewer. The image or sequence has to have been rendered by a 3D software package that included those channels.

### Motion Blur

- Motion Blur: This switches the rendering of Motion Blur on the tool on or off. With this control switched on, the tool's predicted motion drives the motion blur produced by the virtual camera's shutter. With the control switched off, no motion blur gets created.
- Quality: Quality sets how many samples build the blur. A quality setting of 2 will have Fusion create two samples on either side of an object's actual motion. Bigger values give smoother results yet lengthen the render time.
- Shutter Angle:L Shutter Angle governs the angle of the virtual shutter that produces the motion blur effect. Wider angles yield more blur but lengthen the render times. Set to a value of 360 the shutter stays open for one full frame exposure. Going higher is possible and can yield interesting effects.
- Center Bias: Center Bias shifts where the center of the motion blur sits. That allows motion trail effects to be created.
- Sample Spread: Tweaking this control alters how each sample is weighted. That changes how bright the samples are.

Use GPU Three settings live on the Use GPU menu. Setting the menu to Disable shuts off GPU hardwareaccelerated rendering. Enabled puts the GPU hardware to work rendering the node. Auto taps a capable GPU when one exists and drops back to software rendering whenever a capable GPU is absent. Hide Incoming Connections Turning on this checkbox can conceal the connection lines from incoming nodes, leaving a node tree that looks cleaner and reads more easily. With it on, empty fields for each input on a node show in the Inspector. Dragging a connected node out of the node tree into the field will hide that incoming connection line for as long as the node stays unselected in the node tree. Once the node is selected in the node tree, the line returns. Comments Use the Comments field to attach notes to a tool. Click inside the empty field and type the text. Once a note is attached to a tool, a small red square shows at the node's lower-left corner while the full tile is on display, or a small text bubble icon shows at the right while nodes are collapsed. To view the note inside the Node Editor, rest the mouse pointer over the node so the tooltip appears. Scripts From the Settings tab, every tool in Fusion offers three Scripting fields. Each holds edit boxes for adding scripts that run while the tool renders. For more on scripting nodes, refer to the Fusion scripting documentation.
