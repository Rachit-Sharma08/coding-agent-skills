# Common controls motion blur

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](common-controls-background-node-image-tab.md) / [The Common Controls](common-controls-background-node-image-tab.md)
<a id="source-motion-blur"></a>

### Motion Blur

- Motion Blur: This switches the rendering of Motion Blur on or off for the tool. With this control switched on, the tool’s anticipated motion drives the motion blur that the virtual camera’s shutter would create. With the control switched off, none is produced.
- Quality: Quality sets how many samples go into building the blur. A quality setting of 2 prompts Fusion to make two samples on each side of an object’s real motion. Bigger values yield smoother output yet lengthen the render time.
- Shutter Angle: Shutter Angle governs the angle of the virtual shutter that generates the motion blur effect. Wider angles yield more blur but lengthen the render times. A value of 360 equals leaving the shutter open across one full frame exposure. You can push past that, and higher values lend themselves to interesting effects.
- Center Bias: Center Bias shifts where the center of the motion blur sits. That makes it possible to build motion trail effects.
- Sample Spread: Tweaking this control alters how much weight each sample receives. The brightness of the samples shifts as a result.

Use GPU There are three options on the user GPU menu. Switching the menu to Disable shuts off hardware-accelerated rendering through your computer’s graphics card. Enabled draws on the hardware, while Auto employs a capable GPU when one exists and drops back to software rendering should no capable GPU be present Comments You use the Comments field to attach notes to a tool. Click inside the field and enter the text. Once a note is attached to a tool, a tiny red square turns up in the node’s lower-left corner while the full tile is shown, or a tiny text bubble icon turns up on the right once nodes are collapsed. To read the note in the Node Editor, rest the mouse pointer over the node and the tooltip appears. Scripts Each tool in Fusion offers three Scripting fields reached through the Settings tab. Every one holds edit boxes for entering scripts that run while the tool renders. For deeper detail on scripting nodes, please refer to the Fusion scripting documentation.
