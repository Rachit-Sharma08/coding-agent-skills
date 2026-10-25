# Key output controls and qualifier controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Combining keys and using mattes.
[Chapter index](INDEX.md) / [Previous section](the-key-mixer-and-adding-two-keys-together.md)
<a id="source-key-output-controls"></a> <a id="source-qualifier-controls"></a> <a id="source-the-many-uses-of-key-output-gain"></a> <a id="source-using-the-key-palette-to-adjust-key-mixer-controls"></a>

### Key Output Controls

- Qualifier invert: Flips the key as a whole.
- Gain: Acting on the key output, this parameter dictates how strongly that node figures into the grade as a whole. With Gain at 0 the node does nothing whatsoever, whereas the default of 1.00 lets the node's adjustments come through at full strength. Pushed to its ceiling of 2.00, it boosts the intensity of any portion of the key output sitting below 100 percent white. This parameter can also keyframe the key output, fading that node's contribution in or out across a single set of keyframes.
- Offset: Lets you tune the contrast of the Output key. It does nothing when the whole key is 100 percent white (a solid key).

### Qualifier Controls

- Qualifier invert: Flips the key produced by that node's Qualifier palette.
- Qualifier matte: Lets you flip how the keys from the Qualifier and Window palettes interact between Matte and Mask modes. Under Matte mode (the default), the Qualifier and Windows palettes merge by intersection. Under Mask mode, they're summed together instead.
- Gain: Lets you push the strength of the key from the Qualifier palette up or down.
- Offset: Lets you tune the contrast of the key from the Qualifier palette.

### Using the Key Palette to Adjust Key Mixer Controls

Opening the Key palette while a Key Mixer node is selected gives you these controls to adjust:

The Key palette and its controls as they appear with a Key Mixer selected

- Input list: A roster of every input wired to the Key Mixer. Each row on the roster carries these controls:

Input name: The label of each node connection attached to that key mixer, like Input Link 1, Input Link 2, and so forth. Input invert: Flips the key arriving at this specific input. Off by default. Input mask: Toggles the key input between Matte and Mask modes. Under Matte mode (on) the key input merges by intersection with the other inputs wired to the Key mixer. Under Mask mode (off by default), the key input is summed onto the other key inputs wired to the Key mixer. Gain parameter: Dials the strength of that input matte's share of the resulting output matte up or down. Offset parameter: Tunes the contrast of that input matte's share of the resulting output matte.

- Output invert: Flips the combined upshot of all the various Input Link interactions.
- Gain: This parameter raises or lowers the strength of the resulting output key. With Gain

set to 0 it drives every input to black, whereas the default of 1.00 sends out the merged mattes at full strength. Pushed to its ceiling of 2.00, it boosts the intensity of any portion of the key output below 100 percent white, which in practice can “grow” soft edges. This parameter can likewise keyframe the key output, fading that node's contribution in or out across one set of keyframes.

- Offset: Lets you tune the contrast of the Output key.

### The Many Uses of Key Output Gain

A number of the methods covered here and over in “Secondary Qualifiers,” can be tailored even further through the Key Output Gain parameter, which makes it simple to govern how strongly a node bears on your grade with one move. For the example below, a clip gets two plain Serial nodes, the first widening image contrast while the second leans on assorted controls to pour intense warmth into the highlights.

A tint laid over the image's highlights alone Were you to decide you wanted to cut back the warmth the second node introduced without reworking the controls you used to build the effect, you could open the Key palette and bring the Key Output Gain parameter down to fade the effect in a single move.

A side-by-side look at four takes on this grade through the Split Screen controls' Versions option, each at a different Output Gain — 1, .75, .5, and.25 This same idea applies to governing the strength of individual nodes combined in parallel, of nodes combined through the Layer node, or simply to dialing back the effect of any node in the node tree you'd like to “turn down” a touch.
