# ColorTone Diffuser

Version: DaVinci Resolve 20.3 Reference Manual. 

[Film emulation effects](INDEX.md)

<a id="source-colortone-diffuser"></a> <a id="source-the-original-image"></a> <a id="source-colortone-diffuser-1"></a>

### ColorTone Diffuser

Designed to imitate a diffusion filter ringed by a rectangle of user-adjustable colored lights, the ColorTone Diffuser is one such effect. As you change those lights' color and intensity, their light scatters off the diffusion elements set into the glass filter sitting right in the camera's image path. This lets you craft particular artistic and creative looks that post tools alone had a hard time delivering, until now.
### The original image

The image with the ColorTone Diffuser “Teal Soft” preset
### ColorTone Diffuser

- Presets: Offers a collection of ColorTone presets to audition on your footage as jumping-off points. Its default, Clean Slate, leaves everything untouched and frees you to build your own custom look.
- 3D LUT Compatible: Switches off every control that a LUT can't carry.
- Color Space Overrides: These controls let you swap the effect's input gammas and color spaces should you need to set them by hand for a display referred workflow. The default, “Use timeline,” lines up with the color spaces you've chosen in the Color Management section of the Project Settings.

Input Color Space: Fixes the input color space; pick one from the drop-down menu. Input Gamma: Fixes the input gamma; pick one from the drop-down menu.

- Diffusion: Spills the bright regions outward, bleeding them into neighboring parts of the frame.

Resolution: Set how much blur lands on the image to recreate the slight resolution loss as light comes through the filter. Diffusion: Tick this box to switch Diffusion on or off. Amount: How strong the diffusion effect is. Radius: How large the diffusing area is.

- Shadow Soft Clip: Shields the shadows from the ColorTone Diffuser's reach. Whatever falls below this level skips the filter. Shadow Clip: Tick this box to enable or disable Shadow Clipping. Threshold: Set the lowest black level the ColorTone Diffuser is allowed to touch. Softness: How gradually the black level is held back at the threshold.
- Highlight Soft Clip: Keeps the highlights clear of the ColorTone Diffuser's reach. Whatever sits above this level skips the filter. Highlight Clip: Tick this box to enable or disable Highlight Clipping. Threshold: Set the highest bright level the ColorTone Diffuser is allowed to touch. Softness: How gradually the bright level is held back at the threshold.
- Tone Lights: These govern the hue of the ring lights scattering off the filter's diffusive elements. Intensity: Governs the overall level of tone light cast across the frame. Bias Red / Green / Blue: The proportion of a given color within the Tone Light. Since these controls hinge on the content and read more clearly in shadows, brighter footage may show little visible change.
- Tone Light Falloff: Imitates how the light dims toward the filter's edges and intensifies at its center. Underneath, a vignette mask is what maps where the effect lands. Apply Falloff Mask: Tick this box to switch the Tone Light Falloff on or off. Preview Falloff Mask: Ticking this box surfaces the Falloff Mask's vignette in the viewer, where darker regions take less of the effect and white more. Size: Set how large the mask's center is. Softness: Sets how soft the mask grows as you travel out from its center. Amount: How forcefully the mask shapes the effects.

In a Falloff Mask preview, the effect reads more strongly across the mask's white regions

- Image Adjustments: Hands you fundamental exposure, contrast, and saturation controls. Making these tweaks here in the node folds everything into the LUT, sparing you from stacking another grade above the node. Enable Adjustments: Tick this box to switch on the Image Adjustments. Show Advanced Clipping Options: Ticking this box brings up a further set of shadow and highlight softclip controls that behave just like the ones above. These, however, run at the plugin's end rather than its start, which can stop blow outs from being reshaped by the original shadow and highlight softclip controls. Exposure: Tunes the Brightness / Gain. Contrast: Tunes the Contrast. Saturation: Tunes the Saturation.
