# Film Look Creator color and glow

Version: DaVinci Resolve 20.3 Reference Manual. Studio version only.

[Film emulation effects](INDEX.md)

<a id="source-bloom"></a> <a id="source-color-settings"></a> <a id="source-film-look"></a> <a id="source-halation"></a> <a id="source-split-tone"></a> <a id="source-vignette"></a>

### Film Look

These controls let you shape the base film look's overall parameters.

- Film Look Blend: Tunes how strong the initial default base film look is, before you touch other parameters.
- Skin Bias: Tunes the film look's skin tones. Negative values lend warm, darker, more saturated skin tones, whereas positive values lend brighter, rosier, less saturated ones.
### Color Settings

These controls let you reshape the color information behind the film look. A 3D LUT will carry these effects.

- Exposure: A photometric control that shifts the exposure in stops (+/- 5).
- Contrast: Reshapes the overall S-curve transfer function to add contrast to or strip it from the shot.
- Highlights: Reshapes the roll-off at the S-curve's top, letting you rein in or stretch out the

shot's brightest regions.

- Fade: Reshapes the roll-off at the S-curve's bottom, letting you rein in or stretch out the

shot's darkest regions.

- White Balance: Through chromatic adaptation, this control imitates how the source footage might

have looked had it been shot under different lighting. It is set in degrees Kelvin.

- Tint: Lets you shift the clip's green/magenta balance to even out footage shot under

narrow-spectrum lighting like fluorescent tubes or sodium vapor streetlights.

- Skin Bias: Lets you shift the image's skin tones, running from -1 (warmer, darker, more saturated) to +1 (rosy, brighter, less saturated). It also comes in handy when you, say, push tint one way and then call on Skin Bias to even the image back out.
- Subtractive Sat: Lets you tune the image's overall saturation in a manner that hews closer to a subtractive approach.
- Richness: Works on the already more saturated regions, laying subtractive saturation onto just those areas. Handy for deepening and enriching the image, or for easing off slightly on the more saturated regions.
- Bleach Bypass: Recreates this familiar look by stacking a desaturated, higher-contrast copy of the image back onto itself.
### Split Tone

These controls tint shadows and highlights along opposing hue angles — say, orange into the highlights and teal into the shadows for a more contemporary cinematic feel. A 3D LUT will carry these effects.

- Enable Split Tone: Switches this effect on or off.
- Split Tone Mode: Pick between the Strong and Natural settings.
- Amount: How intense the split tone is. This value has to exceed 0 before any effect shows.
- Hue Angle: This slider sets which complementary hues land on the shadows and highlights.
- Pivot: This control fixes where in luma the hue transition falls. Pushed to its extremes of 0.000 or

  1.0000, the pivot lets you drop a single tint onto the shadows or the highlight.
### Vignette

These controls are a pared-down window for dropping a vignette onto the shot. When you want finer command, switch this setting off and turn to the Vignette effect instead.

- Enable Vignette: Switches the vignette on or off.
- Amount: Sets how intense the vignette's darkened regions are.
- Size: Sets how far the vignette pushes into the frame.
### Halation

These controls offer a pared-down way to wrap soft glows around the edges of the subjects in your frame, echoing this trait of motion picture film. For finer command, switch this setting off and turn to the Halation effect instead.

- Enable Halation: Switches the Halation effect on or off.
- Highlights Only: Confines the Halation effect to the edges of highlights alone.
- Amount: Lets you fix how intense the halation is.
- Radius: Lets you fix how far the glow spreads out from the edges.
- Saturation: Lets you tune the halation's color intensity.
- Hue: Lets you tint the glow with a chosen color.
### Bloom

These controls let you bring a faint glow around the edges of highlights.

- Enable Bloom: Switches the Bloom effect on or off.
- Amount: Lets you fix how intense the bloom is.
- Radius: Lets you fix how far the bloom spreads out from the edges.

Read [Film Look Creator setup and color spaces](film-look-creator-overview.md) for the shared prerequisites.
