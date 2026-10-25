# Beauty and custom mixer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Beauty studio version only, Custom mixer.
[Chapter index](INDEX.md) / [Previous section](beauty-operating-mode.md) / [Next section](depth-map-and-face-refinement.md) / [Beauty (Studio Version Only)](beauty-operating-mode.md)
<a id="source-advanced-options"></a> <a id="source-blend"></a> <a id="source-combine"></a> <a id="source-custom-mixer"></a> <a id="source-detail-recovery"></a> <a id="source-grain"></a> <a id="source-texture-recovery-1"></a>

### Detail Recovery

These parameters let you bring back the parts of the source video surrounding the image edges, returning detail to the image.

- Strength: Sets how much detail is recovered.
- Width: Governs how far out on each side of the edges image detail is recovered.
- Gamma: Governs whether every edge is recovered or only the stronger ones. A higher gamma trims down the number of edges recovered.
- Blur: Softens the edge map where detail is due to be recovered.
- Preview Edges/Details: Tick this checkbox to reveal the areas where image detail is set

to be recovered; that lets you watch firsthand how the section's other controls bear on the image.

- Preview Recovery: Tick this checkbox to reveal the actual detail under recovery on its own against a neutral gray background.

### Texture Recovery

Through these parameters you bring back stretches of fine texture from the source video across flat areas held apart from the edges.

- Texture: Sets how much recovered texture is restored.
- Scale: Lets you fix a threshold beneath which texture is pulled from the source image and

laid onto the result.

- Detail/Edge Balance: Lets you tilt the recovery toward all textures (a negative value), or solely toward

stronger details such as edges (a positive value).

- Preview Texture: Tick this checkbox to reveal the actual texture under recovery on its own against a

neutral gray background.

### Grain

These parameters let you lay grain over the image to mimic detail in video areas carrying poor texture or none at all. Grain shows up only in smooth areas and steers clear of the recovered edges.

- Strength: Governs how much grain is added to the image.
- Size: Governs how big the individual grains are.
- Softness: Softens the grain texture.
- Saturation: Applies saturation to the grain.

### Custom Mixer

Think of the Custom Mixer as a more capable take on the Layer node. It accepts two inputs and merges them according to the second input's Alpha channel. Its controls let you mix sources, blend effects, and interpolate among grades with per-channel command and mixing options. You can wield this tool in numerous ways to govern the relative intensity between the sources, or just as a stand-in for the Layer Node but driven by sliders. Add the Custom Mixer straight into the node graph rather than dropping it on top of a Corrector node. To bring the Custom Mixer into your Node Graph, drag its icon out of the Effects library's Resolve FX Refine section right into the Node Graph. You may also drop it onto an existing link in the Node Graph to set it inline. Here's how the Custom Mixer node gets wired. The first and second RGB (Green) inputs serve as input 1 and input 2 in turn. The alpha of the second input drives the blend of input 2 onto input 1. The 1st input's Alpha leaves the result alone; it travels through the node to the output key.

How the Custom Mixer Node connects: Input 1 sits at the Green triangle above, with Input 2 at the Green triangle below. Input 2's alpha drives the blend of Input 2 over Input 1 and is the value you adjust within the Custom Mixer controls.

The Custom Mixer carries two principal modes selected via the Mix mode; both act the same way, differing only in the controls used to alter how the input shapes the output.

### Blend

Blends the second input over the first. Its usual range runs from 0 (entirely input 1) to 1 (entirely input 2), yet you can push the blend factor as much as 10 times higher or lower by typing values straight into the fields. That lets you heighten the contrast between inputs past what either looks like alone. Every slider can be keyframed on its own.

- Blend Input 2 onto 1: Governs each source's strength, drawing on the color channels of the chosen color space (RGB, YUV, XYZ, etc.). With the Gang checkbox cleared, these are adjustable one by one.
- Gang: Tick this box to gang the custom mixer's channels together, or clear it to adjust them separately.

### Combine

Merges the inputs together, letting you shift how strongly each input contributes to the mix. The usual range spans 0 (entirely input 1) to 1 (entirely input 2), though you can drive the blend factor as much as 10 times more or less by entering values straight into the fields. That lets you amplify the contrast between inputs past how either appears on its own. Each slider keyframes independently.

- Input 1 Contribution: Governs input 1's source strength, drawing on the color channels of the chosen color space (RGB, YUV, XYZ, etc.). These adjust individually when the Gang checkbox is cleared.
- Input 2 Contribution: Governs input 2's source strength, drawing on the color channels of the chosen color space (RGB, YUV, XYZ, etc.). These adjust individually when the Gang checkbox is cleared.
- Offset: Governs the combination's offset, drawing on the color channels of the chosen color space (RGB, YUV, XYZ, etc.). These adjust individually when the Gang checkbox is cleared.
- Gang: Tick this box to gang the custom mixer's channels together, or clear it to adjust them separately.

### Advanced Options

Sets the composite type along with the resulting mix's color space and gamma.

- Composite Type: Picks, from the drop-down menu, the composite type the mixer uses.
- Color Space: Picks the Color Space applied to the blend. It defaults to the current

Timeline color space.

- Gamma: Picks the Gamma applied to the blend. It defaults to the current Timeline color space.

In the Custom Mixer's starting setup, Node 1 holds the original image while Node 2 is the same but with a Noise Reduction effect on it. In the Custom Mixer's final setup, raising the blend factor by 7 has the mixer add noise to the image instead. For that example, applying the Noise Reduction FX to Node 2 and wiring the identical image from Node 1 straight into the Custom Mixer leaves the noise pattern from the effect itself as the inputs' sole difference. Manually pushing the blend above 1 mixes in more noise than you began with. Thus, pairing Noise Reduction with the Custom Mixer lets you genuinely heap extra noise onto an image that exactly matches the original grain pattern, with no need to hunt down a comparable external grain or noise source.
