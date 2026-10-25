# Merge and multimerge

Version: DaVinci Resolve 20.3 Reference Manual. Context: Merge, Multimerge.
[Chapter index](INDEX.md) / [Previous section](merge-alpha-resizing-and-reference-controls.md) / [Next section](multimerge-and-common-controls.md) / [Merge Mrg](merge-node-inputs-and-composite-operators.md)
<a id="source-a-typical-multimerge-node-structure-in-davinci-resolve"></a> <a id="source-basic-node-setup"></a> <a id="source-channels-tab"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-merge-node-channels-tab"></a> <a id="source-multimerge-mmrg"></a> <a id="source-multimerge-node-introduction"></a> <a id="source-resolution-handling"></a> <a id="source-the-multimerge-node"></a>

### Channels Tab

### Merge node Channels tab

Controls on the Channels tab give the Merge node the means to draw on the Z-channels carried inside each image, settling what sits in front and what sits behind throughout a Merge operation. The controls below are how you tailor the result.

- Perform Depth Merge: Defaults to off. Switch it on and both images' Z-channel drives the composite order. Alpha channels still spell out transparency, but it's the Z-Depth channel values that fix how image elements stack front to back. Should either image lack a Z-channel, this checkbox's state is disregarded and no depth compositing happens. Where Z-Depth channels do exist, clearing this checkbox keeps them out of the operation.
- Foreground Z-Offset: This slider applies an offset to the foreground image's Z value. Hit the Pick button to lift a value from a displayed image's Z-channel, or key one in through the slider or input boxes. Raise the value and the foreground image's Z-channel shifts farther off along the Z-axis; lower it and the foreground draws nearer.
- Subtractive/Additive: During Z-compositing, background image pixels can end up composited in the output's foreground whenever that pixel's Z-buffer sits closer than the foreground pixel's Z. This slider decides whether such pixels merge in an Additive or a Subtractive mode, working precisely like its counterpart slider over in the Merge tab. Merged atop a background of another color, the original background still peeks through the semitransparent regions. An Additive merge holds the image's transparencies but folds their values into the background.

### Common Controls

Settings Tab The Inspector's Settings tab is likewise mirrored across both the Dissolve and Merge nodes. Those shared controls get their description in the “The Common Controls” section coming up.

### MultiMerge [MMrg]

### The MultiMerge node

### MultiMerge Node Introduction

With the MultiMerge node you can bring several sources together inside a layer-based structure. Where the standard Merge tool takes just one foreground input, MultiMerge spins up a fresh consecutive foreground input every time you drag a new source onto the tool. Those inputs join the Layer List in the Inspector, shown as a stack running top to bottom in a hierarchy. The layers sit so that the one nearest the foreground rides at the list's top and the one nearest the background rests at the bottom. Every layer carries its own separate, independent set of Merge controls (refer to the Merge node above) that turn up in the Inspector's lower half, so you can tune position, size, composite modes, and the rest for each source input on its own. As a composite grows more involved, you can wind up with heaps of standard Merge nodes strewn across the node tree. MultiMerge serves to gather those Merge nodes into one, acting as an organizing aid while letting you direct the order of operations in a layer-based setting rather than a node-based one. In principle you could composite and arrange hundreds of distinct layers with a single MultiMerge node on your node tree.

A sky replacement composite that once took three separate Merge nodes (previous page) gives way to a lone Multi Merge node (above). A faint glow marks the pipe of whichever layer is currently selected in the Layer List (Actors node to MultiMerge node).

### Inputs

These image inputs come on the MultiMerge node: Background: The orange background input takes the first of the images you mean to composite together, and you ought to wire up the background input before the foreground input. Foreground: The foreground inputs take each later image to be composited, usually a foreground subject meant to sit ahead of the background. Running a pipe from a new source onto the MultiMerge node spontaneously adds a fresh foreground input on the node plus a fresh layer in the Layer List. All foreground inputs carry a white color. Effect Mask: (Optional) The effect mask input lets you confine merging to a portion of the output image — wherever the mask reads white (where the foreground image appears in front of the background) — and lets the background image alone show through wherever the mask reads black.

### Basic Node Setup

A MultiMerge node is usually wired up like this: several input images feeding the foreground inputs, one background input, and the output running on to the composition's next node. The effect mask input goes unused in this example, since that's the more common arrangement.

### A typical MultiMerge node structure in DaVinci Resolve

### Resolution Handling

Although images of any resolution may be wired into the MultiMerge node's background and foreground inputs, it's whichever image feeds the background input that sets the output's resolution.

### Inspector

The MultiMerge node's Layer List. Layer 4's input has been unplugged (its name struck through) and switched off (unchecked). The Luma Key layer is mid-rename, the Sky layer is switched off (unchecked), and the Actors layer is switched on (checked).
