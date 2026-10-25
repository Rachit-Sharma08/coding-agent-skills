# Gamut limiter and gamut mapping and invert color

Version: DaVinci Resolve 20.3 Reference Manual. Context: Gamut limiter, Gamut mapping studio version only, Invert color.
[Chapter index](INDEX.md) / [Previous section](despill-and-false-color.md)
<a id="source-gamut-limiter"></a> <a id="source-gamut-mapping-studio-version-only"></a> <a id="source-invert-color"></a>

### Gamut Limiter

Allows you to confine the gamut to a chosen standard. This comes in handy when the delivery color space carries a wide gamut, like Rec. 2020, yet the QC specification demands narrowing things to a tighter gamut like P3, so as to cap how much saturation the final output is permitted. Since this is a limiting operation, any out-of-bounds values get hard clipped. You can apply this plugin whether or not Resolve Color Management happens to be turned on. Being a limiter, it ought to sit near the end of any node tree, keeping valuable image data from getting clipped.

- Current Gamut: Pick whichever timeline gamut the image is presently relying on.
- Current Gamma: Pick whichever timeline gamma the image is presently relying on.
- Limit Gamma to: Pick here the gamut you intend to clamp the image down to.

The choices in these menus mirror those of the Resolve Color Management menus over in the Color Management panel. To learn more about what each of these parameters offers, consult Chapter 9, “Data Levels, Color Management, and ACES.”

### Gamut Mapping (Studio Version Only)

The Color Space Transform plugin offers Gamut Mapping controls suited to workflows that call for converting one color space into another whose gamut is vastly wider or narrower. These controls match exactly those in the Color Space Transform plugin’s Gamut Mapping group and resemble the ones in the Color Management panel of the Project Settings.

- Gamma: A pop-up menu where you declare which kind of gamma the clip is meant to carry, so dial this in to whatever fits that image (it might align with the timeline color space, though that hinges on your working method).
- Tone Mapping Method: Switches on tone mapping for workflows that demand converting one color space into another of vastly wider or narrower dynamic range, automatically stretching or squeezing image contrast to land on a pleasing outcome free of clipping.

None: Turns off Input DRT Tone Mapping. The Input to Timeline Color Space conversion gets no tone mapping whatsoever, yielding a plain 1:1 mapping into the Timeline Color Space. Clip: Hard clips every out-of-bounds value. Simple: Relies on a basic curve for the transformation, squeezing or stretching the highlights and/or shadows of the timeline dynamic range to sit better within the output dynamic range. Keep in mind that the “Simple” option maps across roughly 5500 nits down to 100 nits, so converting from an HDR source above 5500 nits to an SDR target can still leave some highlight clipping past 5500 nits. Luminance Mapping: Behaves like DaVinci, yet proves more precise whenever the Input Color Space of all your media sits within one standards-based color space, like Rec. 709 or Rec. 2020. DaVinci: With this choice the transform is tone mapped using a gentle luminance roll-off through the shadows and highlights, plus measured desaturation of image values in the very lightest and darkest regions. It serves especially well for wide-gamut camera media and is a solid pick when blending footage shot on different cameras. Saturation Preserving: This choice keeps the gentle luminance roll-off in the shadows and highlights, but spares dark shadows and bright highlights from desaturation, making it a capable option for colorists who prefer to push color further. Yet since over-saturated highlights can read as unnatural, two parameters are surfaced to deliver some user-tunable automatic desaturation.

- Sat. Rolloff Start: Defines a threshold, in nits (cd/m2), where saturation begins falling off alongside highlight luminance. The point where the rolloff starts.
- Sat. Rolloff Limit: Defines a threshold, in nits (cd/m2), where the image becomes fully desaturated. The point where the rolloff ends.

Max Input/Output Luminance: Ticking these boxes and dragging the slider beneath them lets you state the input image's lowest and highest luminance in nits. Working both sliders in tandem, you decide which value of the Input Gamma maps onto which value of the Output Gamma. Avg. Input Luminance: Serves to offset wide gaps in how adapted the viewer's vision is when a bright image appears on an HDR display compared with the same image on an SDR display. For the majority of “average” images this setting performs best somewhere between 0–10. That said, when converting extremely bright images (a noon snow scene, for instance), a larger value brings out more detail in the highlights.

- Gamut Mapping Method: Suits workflows that involve converting one color space into another of vastly wider or narrower gamut, automating the stretch or squeeze of image saturation to reach a pleasing, natural-looking result without clipping. Picking Saturation Mapping lets you remap the image's saturation values. Doing so activates the Saturation Knee and Saturation Max. controls.

The Saturation Knee slider fixes the image level where saturation mapping kicks in. Anything beneath that level stays unremapped. Every saturation value at that level and above gets remapped per the Saturation Max. slider. A value of 1.0 stands for full saturation within the output color space currently chosen. The Saturation Max slider establishes the fresh ceiling toward which you wish to lift or drop all saturation values sitting above the Saturation Knee setting. A value of 1.0 stands for full saturation within the output color space currently chosen.

- Apply Forward OOTF: Tick this box to move the image from scene referred over to display referred color management.
- Apply Inverse OOTF: Tick this box to move the image from display referred back to scene referred color management.

### Invert Color

A plugin in the Color category that inverts any color channel, the Alpha channel included, simply by ticking the right box. This modest plugin has 101 uses across advanced workflows, particularly when you must invert Alpha or Key channels for some specific purpose. It isn't a “film negative” plugin; it performs a plain inversion.
