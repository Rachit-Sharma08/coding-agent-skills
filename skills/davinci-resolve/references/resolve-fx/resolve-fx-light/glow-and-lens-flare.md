# Glow and lens flare

Version: DaVinci Resolve 20.3 Reference Manual. Context: Glow, Lens flare studio version only.
[Chapter index](INDEX.md) / [Previous section](cinematic-haze-and-glow.md) / [Next section](lens-flare-element-types.md) / [Continue Lens Flare (Studio Version Only) / Elements](lens-flare-element-types.md) / [Glow](cinematic-haze-and-glow.md)
<a id="source-aperture"></a> <a id="source-atmosphere"></a> <a id="source-global-corrections"></a> <a id="source-lens-flare-preset"></a> <a id="source-lens-flare-studio-version-only"></a> <a id="source-light-source-masking"></a> <a id="source-position"></a> <a id="source-select-output"></a>

### Atmosphere

- Add Atmosphere: Tick this box to switch the Atmosphere effect on or off.
- Strength: Governs how much the light patterns vary.
- Detail: Governs the relative fineness of that variation; lower settings yield finer detail and higher

settings yield coarser detail.

- Scale: Governs how large the noise pattern is.
- H vs. V Ratio: Governs the horizontal-versus-vertical proportion of the variations' spread.
- Evolution: How far the noise pattern should shift.
- Seethe: How much it should evolve on its own at each frame from the outset

### Lens Flare (Studio Version Only)

Recreates a variety of lens flares produced as light passes through an aperture of your chosen shape and ricochets among the stacked optical elements inside a lens. Four sets of controls hand you plenty of room to tailor the presets into an effect of your own:

### Select Output

The Select Output dropdown lets you toggle between these viewing modes:

- Flare Alone: Displays the flare on its own, which makes adjustment easier.
- Final Result: (Default) Displays the lens flare composited over the current clip.

### Lens Flare Preset

Pick a flare style from the Lens Flare Preset drop-down. Once you tweak the controls to build an effect of your own, this drop-down flips to Custom.

### Light Source Masking

Three extra controls up top let you build a quick-and-dirty luma key, producing a mask you can use to hide the lens flare behind foreground objects in the scene. Say you're applying a lens flare to stand in for the sun crossing behind trees: these controls let those tree silhouettes shift and reshape the flare source to suit.

- Enable Light Source Masking: This checkbox turns on the Mask Threshold and Virtual Light Source Size sliders. From there you can pick either Source Mask or Magnified Source Mask to view the mask that raising the Mask Threshold slider generates.
- Mask Threshold: Pushing this slider up draws a fast Luma Key that hides darker foreground objects (trees set against the horizon, for instance) and keeps the flare to picture regions where the flaring light source can “shine through” (here, shining between the trees on the horizon).
- Virtual Light Source Size: This slider sets how rapidly a flare's center vanishes behind the luma-keyed mask you've built; larger values (standing in for bigger light sources) make a flare fade more gradually as it travels “behind” an image feature that the Mask Threshold slider is keying out.

### Position

The Position parameters let you move the X and Y Position of the simulated source driving the flare. You have three avenues for repositioning the flare.

- You can Adjust the X and Y Position sliders.
- You can enable the OpenFX Overlay in the Viewer and drag the on-screen control.
- You can motion track scene elements with the FX Tracker.

Ticking the Move With Sizing checkbox keeps the lens flare's relative spot in the frame even when the Input and Editing sizing change.

### Global Corrections

The Global Corrections group holds parameters for swiftly tuning the flare effect's overall look.

- Global Scaling: Lets you scale every part of the flare effect up or down together.
- Anamorphism: Lets you stretch all flare elements sideways to mimic the stretch of an anamorphic

lens.

- Lens Center X and Y position: Lets you shift the center of the simulated lens producing the

flaring, the point around which the flare's various parts pivot.

- Global Defocus: Lets you blur the whole flaring effect to soften it.
- Global Brightness: Lets you push the overall amount of flaring up or down.
- Global Saturation: Lets you tune the overall color strength of the flaring.
- Colorise Result: Lets you decide the degree of flare tinting, or none. With this left at its 0 default, zero

colorization happens whatsoever.

- Colorization Color: Lets you pick a color for tinting the flare through the Colorize Result

slider above. Either a color control or an eyedropper works for sampling color from the current node's source RGB image.

### Aperture

The Aperture parameters let you specify the aperture of the simulated camera rig that the flare passes through. The shape these parameters set shapes the look of each flare's “starburst element,” along with that of any aperture-shaped “ghost elements” you switch on.

- Aperture Blades: Sets how many blades the aperture contains. You can choose from 3 to 16 (defaults to 6). Lens flare diffraction is symmetric, so an odd blade count yields twice as many rays as there are blades, whereas an even count gives you a ray count equal to the blades.
- Angle: Sets the angle of the resulting Aperture shape.
