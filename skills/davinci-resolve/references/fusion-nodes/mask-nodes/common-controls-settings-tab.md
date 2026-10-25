# Common controls settings tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](common-controls-image-tab.md) / [The Common Controls](wand-mask-and-common-controls.md)
<a id="source-common-mask-settings-controls"></a> <a id="source-motion-blur"></a> <a id="source-settings-tab"></a>

### Common Mask Settings controls

### Settings Tab

Every tool in the Mask category carries the Settings tab inside the Inspector, and even third-party plugin tools expose these Settings controls. They stay uniform and behave identically from tool to tool, though a handful of tools add one or two unique options, which this section addresses as well.

### Motion Blur

- Motion Blur: This switch turns the tool’s Motion Blur rendering on or off. Switched on, it draws on the tool’s predicted motion to generate the blur produced by the virtual camera’s shutter; switched off, no blur at all is generated.
- Quality: Quality sets how many samples go into building the blur. With a setting of 2 in place, Fusion lays down two samples on each side of an object’s true motion. Higher figures smooth the result further but lengthen render time.
- Shutter Angle: Shutter Angle dictates the angle of the virtual shutter behind the motion blur. Wider angles add blur while extending render times, and a value of 360 matches keeping the shutter open across one entire frame exposure. You may go above that for unusual effects.
- Center Bias: Center Bias shifts where the middle of the motion blur sits, making motion-trail looks achievable.
- Sample Spread: Tweaking this control alters how much weight each sample carries, which changes how bright the samples appear.

Use GPU This menu offers three choices. Picking Disable shuts off hardware-accelerated rendering that relies on your computer’s graphics card. Enabled draws on that hardware, while Auto taps a capable GPU whenever one exists and otherwise drops back to software rendering. Comments Into the Comments field you can attach notes for a tool: click the blank field and type your text. Once a note exists, a tiny red square shows in the node’s lower-left corner while the full tile is visible, or a little text-bubble icon shows on the right once the nodes are collapsed. Hovering the pointer over the node in the Node Editor brings up the tooltip so you can read the note. Scripts From the Settings tab, every Fusion tool exposes three Scripting fields. Each is an edit box where you place scripts that run while the tool renders. The Fusion scripting documentation covers node scripting in greater depth.
