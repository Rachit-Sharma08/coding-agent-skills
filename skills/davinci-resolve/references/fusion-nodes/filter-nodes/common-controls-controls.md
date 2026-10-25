# Common controls controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](filter-node-and-rank-filter-node-and-common-controls.md) / [The Common Controls](filter-node-and-rank-filter-node-and-common-controls.md)
<a id="source-motion-blur"></a>

### Motion Blur

- Motion Blur: This flips the rendering of Motion Blur on the tool on or off. With this control on, the tool's predicted motion drives the motion blur that the virtual camera's shutter would create. With the control off, no motion blur is made.
- Quality: Quality sets how many samples build the blur. A quality setting of 2 has Fusion make two samples on either side of an object's true motion. Bigger values give smoother results but lengthen the render time.
- Shutter Angle: Shutter Angle steers the angle of the virtual shutter producing the motion blur effect. Wider angles make more blur but lengthen the render times. A value of 360 equals leaving the shutter open for one full frame exposure. Higher values are allowed and can drive interesting effects.
- Center Bias: Center Bias shifts where the center of the motion blur sits. That opens the door to motion trail effects.
- Sample Spread: Tweaking this control shifts the weighting handed to each sample. That changes the brightness of the samples.

Comments You use the Comments field to attach notes to a tool. Click into the empty field and type your text. Once a note is on a tool, a little red square shows in the lower-left corner of the node while the full tile is shown, or a small text bubble icon shows on the right while nodes are collapsed. To read the note inside the Node Editor, rest the mouse pointer over the node so the tooltip appears. Scripts Every tool in Fusion offers three Scripting fields from the Settings tab. Each holds an edit box where you can drop scripts that run while the tool renders. For deeper detail on scripting nodes, turn to the Fusion scripting documentation.
