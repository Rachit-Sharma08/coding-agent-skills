# Halation

Version: DaVinci Resolve 20.3 Reference Manual. Studio version only.

[Film emulation effects](INDEX.md)

<a id="source-dye-layer-reflections"></a> <a id="source-halation-studio-version-only"></a> <a id="source-isolation"></a> <a id="source-processing-color-space"></a> <a id="source-basic-grain"></a> <a id="source-global-adjustments"></a> <a id="source-secondary-glow"></a>

### Halation (Studio Version Only)

An effect that recreates the faint light scatters, reflections, and analog blooms produced as light bounces back through the dye layers of motion picture film. Typically it shows up as a delicate red/orange-tinted glow ringing bright, high-contrast areas such as lights or reflections. Halation can equally arise from light bouncing inside processing and development gear, or within the camera body. Such small imperfections lend digital files a quietly organic, analog feel.

The Halation effect can lend an organic, analog look to your digital files. Original (L), Halation (R). A range of tools and controls hands you precise say over just how the halation comes across.

Before the Halation effect is applied 

The same image carrying the Halation effect; observe how the halation appears in the water reflections and on the woman wearing the white t-shirt.
### Processing Color Space

Allows you to pick the color space used by the Halation effect. By default it matches whatever the current timeline uses.
### Isolation

Which parts of your clips end up producing halation halos is set by the Isolation controls.

- Threshold: Sets the low clip level used by the Halation effect.
- Normalization: Sets the high clip level used by the Halation effect.
- Film Saturation Level: The point past which all color gets suppressed and pushed to white. This proves handy in HDR workflows, keeping the resulting Halation effects visible at HDR brightness levels.
- View Isolated Regions: Displays solely the regions singled out for producing the Halation effect.

The View Isolated Regions checkbox reveals which areas the halation is going to act on.
### Dye Layer Reflections

Through the Dye Layer Reflections controls you can fine-tune the physical traits of the halation glow.

- Strength: Sets how bright the reflection is.
- Gamma: Sets the manner in which the glow spreads out.
- Saturation: Sets how intense the glow's color appears.
- Spread: Sets how far the dye reflection reaches.
- Fine Tune Relative Spread: Ticking this box lets you adjust the red, green, and

blue reflection distances by hand.
### Secondary Glow

Extra halation traits come from the Secondary Glow controls.

- Strength: Sets how bright the secondary glow is.
- Gamma: Sets how the glow spreads out.
- Spread: Sets how far the glow extends around bright detail.
- Filter: Confines the glow's color to the chosen color.
### Basic Grain

This is a pared-down slice of the Film Grain effect offering fast grain settings. Should you want more, you can place a full Film Grain effect instance just after the Halation effect on the same node for finer detail.

- Append Gain internally: Switches on the simplified grain control.
- Strength: Introduces grain into the halation layer.
- Size: Sets how large the grains are within the halation layer.
- Softness: Softens the grain texture.
- Saturation: Applies saturation to the grain.
### Global Adjustments

- View Glow Alone: This checkbox displays the Halation effect by itself before it merges into the frame. Switching it on comes in handy while you adjust any of the tools above.

The View Glow Alone checkbox presents the Halation effect on its own, kept separate from the underlying image rather than blended with it.

- Reduce Highlights: Dials back the effect in places where it would lighten the scene without feeding the halo. In practice this keeps the halo along a region's edges while sparing the region itself from being blown out.
- Aspect Ratio: Stretches or compresses the glow and grain along the horizontal axis for anamorphic projects.
- Detail Loss: Strips away fine detail the film stock wouldn't realistically have resolved, by defocusing the

image beneath the effect.
