# Output drt tone mapping and use inverse drt for SDR to HDR conversion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Data levels color management and ACES.
[Chapter index](INDEX.md) / [Previous section](input-drt-tone-mapping-options.md) / [Next section](graphics-white-level-and-display-hdr-on-viewers-if-available.md)
<a id="source-apply-resize-transformations-in"></a> <a id="source-color-space-aware-grading-tools"></a> <a id="source-output-drt-tone-mapping"></a> <a id="source-use-inverse-drt-for-sdr-to-hdr-conversion"></a> <a id="source-use-white-point-adaptation"></a>

### Output DRT Tone Mapping

This control becomes available only when the Resolve Color Management presets menu sits on Custom Settings. For workflows that call for converting one color space into a second whose gamut is far wider or far narrower, an extra cluster of settings has been introduced that can assist in automating the necessary growth or shrinkage of image data toward an attractive outcome. Picking from the choices in the Output DRT drop-down menu will shrink or stretch your image data as required throughout the Timeline to Output Color Space transformation that RCM applies when a timeline is being monitored or rendered, so that the end result either avoids clipping or makes fuller use of the new color space. The intent here is not to deliver your finished grade. Instead, it aims to hand you a quicker launching point, whenever you require one, before you move on to your own deeper grade of the outcome. Below are a few illustrations of the purposes the Gamut Mapping controls of RCM can serve:

1 When you're handling high-dynamic-range log-encoded media and your working output happens to be Rec. 709 while you edit, switching on Gamut Mapping allows RCM to apply saturation and tone mapping so you get a more instantly appealing picture whose highlight detail stays unclipped. 2 When you're handling standard-dynamic-range log-encoded media and your working output is an HDR format, switching on Gamut Mapping allows RCM to apply saturation and tone mapping to stretch the picture's highlights to HDR intensity, yielding an image with stronger immediate punch on HDR displays.

(Before/After) Gamut Mapping applied so high‑dynamic-range footage is fitted automatically within the Rec. 709 color space. Within the Output DRT (Display Rendering Transform) drop-down menu you'll find these choices.

- None: The Timeline to Output Color Space conversion gets no tone mapping at all, producing a plain 1:1 output with neither softness nor rolloff. Any image data beyond the gamut gets clipped.
- Simple: Works well when transforming color from HDR down to SDR.
- Luminance Mapping: Behaves like DaVinci, but offers more precision when every clip resides in a single

standards-based color space, such as Rec. 709 or Rec. 2020, applied to both the Timeline and Output.

- DaVinci: This choice tone maps your output using a gentle luminance roll-off through the shadows and

highlights, along with measured desaturation of pixel values in the darkest and brightest regions of the picture. It was engineered to yield smooth, natural-looking highlights and shadows as you stretch and compress the values of your footage, with no extra settings required. It works especially well for wide-gamut camera media and serves as a strong choice when mixing footage from several cameras.

- Saturation Preserving: This choice carries a gentle luminance roll-off through the shadows and highlights to ward off clipping. It manages this while keeping dark shadows and bright highlights saturated, making it a useful pick for colorists who prefer pushing color a touch harder. Because excessive saturation in the brightest parts of a picture can appear unnatural, though, two parameters are surfaced to deliver some automatic desaturation that the user can tune. Sat. Rolloff Start: Lets you define a threshold, measured in nits (cd/m2), where saturation begins to fall away together with highlight luminance. Beginning of the rolloff. Sat. Rolloff Limit: Lets you define a threshold, measured in nits (cd/m2), where the picture becomes fully desaturated. End of the rolloff.
- RED IPP2: With this choice you can apply RED IPP2 tone mapping when outputting to an SDR format like Rec. 709; two settings are surfaced for shaping how the output behaves. Output Tone Map: Sets which variety of tone mapping gets applied to what you output. Options include: None, Low, Medium, and High. Highlight Roll Off: Determines the variety of highlight rolloff applied to keep clipping at bay. Choose from None, Hard, Medium, Soft, and Very Soft. HDR peak nits: With a slider you select the peak nit value you intend to tone map toward. Defaults to 10,000 nits.

### Use Inverse DRT for SDR to HDR Conversion

This control becomes available only when the Resolve Color Management presets menu sits on Custom Settings. A device rendering transform (DRT) generally comes into play when high dynamic range media is being converted into a color space/mastering standard of lower dynamic range. Building a color transform running from SDR to HDR is therefore an "inverse" procedure that stretches the dynamic range of SDR media up to HDR standards. The mechanism behind this is that levels sitting at 100 nits are remapped to the ceiling value chosen for the Timeline Working Luminance parameter, while every other image level is tone mapped deliberately to hand you a solid launching point for grading SDR media into an HDR program. There's a second purpose for this setting as well. Once it's switched on, you're able to output Rec. 709 clips whose color matches the input exactly, with no compression applied to the highlights. NOTE: Switching on "Use Inverse DRT for SDR to HDR Conversion" can amplify noise in imported SDR media that contains broad flat stretches of bright color.

### Use White Point Adaptation

This control runs a chromatic adaptation transform to compensate for differing white points across color spaces.

- Clear this box if your goal is simply to see the input color space's white point untouched within the output color space. As an example, when you'd like to use a P3-D60 mastered clip inside a P3-D65 timeline purely for reference.
- Tick this box to run the chromatic adaptation transform that converts the input white point so it aligns with the output color space's white point. As an example, when you'd like a P3-D60 mastered clip to intercut with other footage mastered in a P3-D65 timeline.

NOTE: This control becomes available only when the Resolve Color Management presets menu sits on Custom Settings.

### Color Space Aware Grading Tools

Within DaVinci Resolve version 17, both Resolve Color Management and ACES let "color space aware" palettes — including the new HDR palette — carry controls that behave consistently regardless of which color space the source footage came from or which Timeline Color Space you happen to use. Additional palettes, the Qualifier and Curves palettes among them, turn color space aware once you tick the "Use Color Space Aware Grading Tools" checkbox inside the Color Management panel of the Project Settings (which is enabled by default). While color space aware grading tools are in use, you ought not enable HDR Mode on the node you're currently grading.

- For the Qualifier palette, this lets Qualifiers build high-quality keys exactly as you'd anticipate, regardless of the source footage's color space or the Timeline Color Space in play.
- For the Curves palette, this lets each curve's overall span line up better with the present clip's full data range, which makes curve tweaks simpler and more precise.

NOTE: This control becomes available only when the Resolve Color Management presets menu sits on Custom Settings.

### Apply Resize Transformations In

While Resolve Color Management is active, a fresh "Apply Resize Transformations In" Project Setting shows up in the Color Management panel as long as the Resolve Color Management presets menu sits on Custom Settings. This setting lets you pick which color space handles your resizing operations. Resizing normally happens in Linear, yet some specialized workflows gain from resizing within other color spaces, so this option lets you select whichever suits best. The choices available are:

- Timeline: Carries out every resizing operation in the Timeline Color Space.
- Log: Employs a Log Color Space when resizing. Helpful for sidestepping artifacts in particular high-contrast

pictures, like titles and star fields.

- Linear: Generally yields the strongest results across most SDR media.
- Linear Mapped: Generally yields the strongest results across most HDR media.
- Gamma: Included should you ever find a use for this option.
- Gamma Mapped: Generally yields the strongest results when blending SDR media with

wide gamut and log-encoded footage on a single timeline.
