# Multimerge and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Multimerge, Common controls.
[Chapter index](INDEX.md) / [Previous section](merge-and-multimerge.md) / [MultiMerge MMrg](merge-and-multimerge.md)
<a id="source-inspector-1"></a> <a id="source-layer-list"></a> <a id="source-layers"></a> <a id="source-merge-controls"></a> <a id="source-merge-setting-inspector"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a>

### Layer List

Every foreground input you connect to the MultiMerge node spawns a new layer, added in turn within the Layer List. That list is ordered hierarchically from top to bottom, with the upper layers sitting above the ones beneath them in the image. There are a few ways to shape this layer arrangement. To Select a Layer: Click a layer in the Layer List to make it active. The active layer's Merge controls show up at the foot of the Inspector, and the pipe running to that layer's input on the MultiMerge node picks up a faint glow in the node tree. Hold the Shift key as you click to grab a range of layers, or the Command key to grab several non-adjacent ones. A right-click on any layer brings up a contextual menu holding these options:

- Go To Source: Picks out the tool feeding that layer's input on the MultiMerge node and surfaces the tool's parameters in the Inspector.
- Split Here: Spins up another connected MultiMerge node on its own and divides the current layers across the two. The layer chosen for the split, together with every layer above it, peels off into a new MultiMerge node, while the original MultiMerge node ties into the background input of that new MultiMerge node.
- Rename Layer X: Brings up a dialog box for relabeling the chosen layer.
- Rename Layer to Match Source: Swaps the layer's name to match the name of the

tool it's connected to.

- Set Layer X to Default: Returns the layer's merge settings below to their default state.
- Delete Layer: Removes the layer outright from the Layer List and unplugs the pipe from the

original tool, though the original tool itself stays.

To Move a Layer up or down the List: Grab the Layer name and drag it higher or lower in the list. A grey line marks the spot where the layer will come to rest. Release the mouse button to commit the move. To Rename a Layer: Out of the box, each layer borrows its name from the input tool. For a more meaningful Layer's name, double-click that name and type a replacement into the text field. Alternatively, right-click a Layer's name and choose Rename Layer off the contextual menu. To Disable/Enable a Layer: Ticking or clearing the box beside the Layer's name switches that layer on or off accordingly. Switching a layer off mutes that input's share of the MultiMerge's overall composite without removing it. To Replace a Layer: By design, unplugging the pipe from the MultiMerge's input leaves the layer sitting in its spot within the Layer List, but with a strike-through on its name to signal that nothing's hooked up at the moment. This lets you rapidly cycle and try out a number of input sources (clips, graphics, and so on) into the same layer without forever reshuffling your Layer List order. Keyframing the Layer List: The Layer List can itself be keyframed by way of the standard keyframe controls off to the list's right. The parameters open to keyframing are layer order along with layer enable and disable.

### Merge Controls

Every layer owns a separate, independent set of Merge controls that surface here once the layer is selected. For a thorough rundown of how the Merge controls behave, turn to this chapter's earlier section headed Merge [Mrg].

### The Common Controls

A handful of the same Inspector controls appear on the Merge, MultiMerge, and Dissolve nodes alike. What this section lays out are the controls those two nodes hold in common.

### Inspector

### Merge Setting Inspector

### Settings Tab

Both tools in the Composite category carry the Settings tab within the Inspector. Even third-party color-type plugin tools sport the Settings controls. They stay uniform and behave identically across tools, though a tool here and there throws in one or two of its own options, which are likewise covered here. Blend The Blend control mixes between the tool's original image input and its final altered output image. With the blend value at 0.0, the outgoing image matches the incoming one exactly. As a rule, that prompts the tool to bypass processing altogether, copying the input straight through to the output.

Process When Blend Is 0.0 The tool keeps processing even with the input value at zero. That can help when this node's processing is scripted to set off another task while the node's value sits at 0.0. Red/Green/Blue/Alpha Channel Selector These four buttons pin the tool's effect to chosen color channels. The filter usually kicks in after the tool has run. Deselect the red button on a blur tool, say, and the blur applies to the image first, after which the original input's red channel is copied back over the result's red channel. A few exceptions exist, like tools where clearing these channels makes the tool skip that channel's processing outright. Such tools generally carry a matching set of RGBA buttons on the tool's Controls tab, and in that case the Settings and Controls tab buttons are one and the same. Apply Mask Inverted Switching on the Apply Mask Inverted option flips the tool's entire mask channel. That mask channel is the pooled result of every mask wired into or produced within a node. Multiply by Mask Choosing this option multiplies the masked image's RGB values by the mask channel's values, turning every image pixel outside the mask (that is, set to 0) black/transparent. Use Object/Use Material (Checkboxes) Certain 3D software can render to file formats carrying extra channels. The EXR file format notably supports Object and Material ID channels, which can serve as a mask for the effect. These checkboxes settle whether those channels get used when present, and the precise Material ID or Object ID affected is set through the next batch of controls. Correct Edges This checkbox shows up only with the Use Object or Use Material checkboxes ticked. It flips the approach taken to overlapping object edges in a multi-object image. Switched on, it draws on the Coverage and Background Color channels to separate out and sharpen the effect around an object's edge. Left off (or with no Coverage or Background Color channels on hand), aliasing can creep in along the mask's edge. For more on the Coverage and Background Color channels, the DaVinci Resolve Reference Manual treats them under Chapter 78, “Understanding Image Channels,” while the Fusion Reference Manual handles them at Chapter 18. Object ID/Material ID (Sliders) These sliders choose which ID builds a mask from an image's object or material channels. Work the Sample button much as you would the Color Picker, lifting IDs straight off the image shown in the view. The image or sequence has to have been rendered from a 3D software package that included those channels.

Use GPU The Use GPU menu offers three settings. Choosing Disable shuts off hardware-accelerated rendering on your computer's graphics card. Enabled puts that hardware to work. Auto taps a capable GPU whenever one is present and drops back to software rendering when none is Motion Blur

- Motion Blur: This flips the rendering of Motion Blur on the tool on or off. Switched on, the tool's predicted motion drives the motion blur that the virtual camera's shutter would create. Switched off, no motion blur appears.
- Quality: Quality fixes how many samples build the blur. Set Quality to 2 and Fusion lays down two samples on each side of an object's true motion. Bigger values smooth the result while lengthening the render time.
- Shutter Angle: Shutter Angle governs the virtual shutter's angle behind the motion blur effect. Wider angles deepen the blur but stretch the render times. A value of 360 amounts to leaving the shutter open across one full frame exposure, and you can go higher still for intriguing effects.
- Center Bias: Center Bias shifts where the motion blur's center falls, which opens the door to motion trail effects.
- Sample Spread: Tweaking this control alters how much weight each sample carries, which bears on the samples' brightness.

### Layers

- Process Layers: Choose the layer whose effects you want processed from:
- Default Layer (default) - Applies the effect to the base/unnamed layer alone, sparing the others.
- All Layers - Applies the effect across every layer on offer.
- Custom - Lets you pick among the other available layers to apply the effect to, leaving the rest untouched.
- Input Layer: The Input Layer enumerates all layers coming from the default input's upstream node. Whatever layer you select can serve the current tool or, on its own, somewhere further down the node tree.
- Effect Mask Layer: When the tool carries an Effect Mask input, this control enumerates the available layers able to supply mattes for the tool.

Comments You attach notes to a tool through the Comments field. Click into the field and type your text. Once a note rides on a tool, a small red square shows at the node's lower left corner while the full tile is on view; should nodes be collapsed instead, a small text bubble icon turns up over on the right. To read the note in the node editor, rest the mouse pointer on the node and the tooltip appears. Scripts From the Settings tab, three Scripting fields sit on every Fusion tool. Each holds an edit box where you place scripts that run as the tool renders. For deeper detail on scripting nodes, turn to the Fusion scripting documentation.
