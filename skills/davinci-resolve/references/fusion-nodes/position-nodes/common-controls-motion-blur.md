# Common controls motion blur

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](z-to-world-pos-and-common-controls.md) / [The Common Controls](z-to-world-pos-and-common-controls.md)
<a id="source-motion-blur"></a>

### Motion Blur

- Motion Blur: Use this to enable or disable Motion Blur rendering for the tool. Once enabled, the tool relies on its predicted motion to create the blur that the virtual camera’s shutter would cause; once disabled, none is produced.
- Quality: The Quality value fixes how many samples build the blur. When it is set to 2 Fusion places two samples on either side of an object’s real motion. Raising the figure yields a smoother result at the cost of longer render time.
- Shutter Angle: This determines the angle of the virtual shutter responsible for the motion blur effect. Bigger angles mean more blur and slower render times, and 360 corresponds to leaving the shutter open for an entire single-frame exposure. Going higher is permitted and useful for unusual looks.
- Center Bias: Center Bias relocates where the motion blur’s center lies, which opens up motion-trail effects.
- Sample Spread: Changing this control rebalances the weight assigned to each sample, thereby influencing how bright those samples look.

Use GPU Three options live in the Use GPU menu. Choosing Disable switches off rendering that is accelerated by the GPU hardware. Enabled puts that GPU hardware to work rendering the node, while Auto employs a capable GPU when present and otherwise retreats to software rendering. Hide Incoming Connections Ticking this checkbox lets you conceal the connection lines arriving from upstream nodes, giving a node tree a tidier, more readable look. With it active, the Inspector shows a blank field for each of a node’s inputs. Drag a connected node out of the node tree into one of those fields and its incoming line stays hidden as long as that node is not selected in the node tree; select it there and the line comes back. Comments The Comments field exists for jotting notes onto a tool: click the empty field and type away. After a note is added, a small red square turns up in the node’s lower-left corner while the full tile is shown, or a small text-bubble icon turns up on the right after the nodes collapse. Position the mouse pointer over the node within the Node Editor and the tooltip surfaces so the note can be read. Scripts Each Fusion tool provides three Scripting fields under the Settings tab. Every one is an edit box for inserting scripts that execute while the tool renders. Refer to the Fusion scripting documentation for fuller details on scripting nodes.
