# Input drt tone mapping options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Data levels color management and ACES.
[Chapter index](INDEX.md) / [Next section](output-drt-tone-mapping-and-inverse-drt.md) / [Input DRT Tone Mapping](sdr-hdr-conversion-and-advanced-rcm.md)
<a id="source-203-nit-support-for-sdr-to-hdr"></a> <a id="source-advanced-rcm-setup"></a> <a id="source-after-an-automatic-sdr-to-hdr-conversion"></a> <a id="source-choosing-a-timeline-color-space"></a> <a id="source-data-levels-color-management-and-aces-part-3"></a> <a id="source-dual-setting-resolve-color-management"></a> <a id="source-gamut-limiting-restricting-values-within-a-larger-gamut"></a> <a id="source-input-drt-tone-mapping"></a> <a id="source-setting-the-input-color-space"></a> <a id="source-single-setting-resolve-color-management"></a> <a id="source-single-setting-vs-dual-setting-rcm"></a> <a id="source-the-davinci-intermediate-oetf-encoding-sdr-levels"></a> <a id="source-the-davinci-intermediate-oetf-seen-encoding-hdr-levels"></a> <a id="source-the-davinci-wide-gamut-color-space"></a> <a id="source-timeline-working-luminance"></a>

### Input DRT Tone Mapping

This control surfaces only while the Resolve Color Management presets menu sits on Custom Settings. RCM has always reworked the color primaries of differing media formats to agree with one another inside the shared Timeline Color Space. In this updated release, the Input DRT (Display Rendering Transform) drop-down menu offers an assortment of options that let DaVinci Resolve tone map the image data of SDR and HDR clips automatically so they agree more closely once fit into the Timeline Color Space currently chosen. Though the options differ in their specifics, all are automated input-to-timeline color transforms that accomplish the following:

- Media that is log-encoded, or that uses a 2.4 gamma transfer function, gets mapped so its black point, its midtones at 18% gray, and its white levels line up with those of HDR media. Where it is required, highlight data is stretched with care so that every Timeline clip’s highlights, SDR or HDR alike, receive comparable handling.
- Raw formats — among them BRAW, RED, and ARRI RAW — together with media on HDR transfer functions, undergo only minimal mapping across an HDR span of tonality.
- All color transforms into the Timeline Color Space are done without clipping.

The intent is to spread each Timeline clip’s image data, whether SDR or HDR media, across a comparable histogram, with shadows, midtones, and highlights laid out so as to make a friendlier starting point for grading. One upshot is that grades made for one kind of media largely carry over well to other kinds. A range of options is given for the specifics of how this Input to Timeline Color Space transform happens. They all accomplish the same end yet bring different advantages.

- None: With this choice, Input DRT Tone Mapping is switched off. The Input to Timeline Color Space conversion receives no tone mapping whatsoever, which yields a plain 1:1 mapping into the Timeline Color Space.
- Simple: Works well when transforming color from HDR down to SDR.
- Luminance Mapping: Behaves like DaVinci, yet delivers greater precision whenever every clip's Input Color Space

sits within one standards-based color space — for instance Rec. 709 or Rec. 2020.

- DaVinci: Here the transform is tone mapped with a gentle luminance roll-off across the shadows and

highlights, plus measured desaturation of pixel values in the darkest and brightest regions of the picture. It works especially well for wide-gamut camera media and serves as a strong choice when combining footage shot on several cameras.

- Saturation Preserving: This choice carries a gentle luminance roll-off through the shadows and highlights, yet achieves this while keeping dark shadows and bright highlights saturated, making it a worthwhile pick for colorists who prefer pushing color aggressively. Because excessive saturation in the brightest parts of a picture can appear unnatural, though, two parameters are surfaced to deliver some automatic desaturation that the user can tune.

Sat. Rolloff Start: Lets you define a threshold, measured in nits (cd/m2), where saturation begins to fall away together with highlight luminance. Beginning of the rolloff. Sat. Rolloff Limit: Lets you define a threshold, measured in nits (cd/m2), where the picture becomes fully desaturated. End of the rolloff.
