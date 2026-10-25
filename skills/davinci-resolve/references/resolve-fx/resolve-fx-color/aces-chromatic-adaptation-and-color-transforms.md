# ACES chromatic adaptation and color transforms

Version: DaVinci Resolve 20.3 Reference Manual. Context: ACES transform, Chromatic adaptation, Color compressor studio version only, Color space transform.
[Chapter index](INDEX.md) / [Next section](gamut-stabilization-contrast-dctl-and-dehaze.md)
<a id="source-aces-transform"></a> <a id="source-chromatic-adaptation"></a> <a id="source-color-compressor-studio-version-only"></a> <a id="source-color-space-transform"></a> <a id="source-color-space-transform-1"></a> <a id="source-resolve-fx-color"></a> <a id="source-resolve-fx-color-part-1"></a> <a id="source-tone-mapping"></a>

### Resolve FX Color

What these plugins deliver are color-processing techniques you won't find in any of the Color Page palettes on the Color page, and they bundle in a handful of color-management tools usable beyond Resolve Color Management (RCM).

### ACES Transform

This one carries out the same sort of color transforms handled by the ACES Input Device Transform and ACES Output Device Transform parameters over in the Color Management panel, yet it doesn't require ACEScc or ACEScct to be switched on.

- ACES Version: Once you've picked one of the ACES color science options, this pop-up unlocks so you can settle on which version of ACES to run.
- Input Transform: From this pop-up menu you choose the IDT (Input Device Transform) used to process the image. The choices it offers match those found in the Color Management panel of the Project Settings.
- Output Transform: This pop-up menu is where you pick an ODT (Output Device Transform) for converting the image data so it can be monitored on your calibrated display and when a timeline gets exported from the Deliver page. The choices it offers match those found in the Color Management panel of the Project Settings.
- Gamut Compress Type: Here you decide which flavor of ACES Gamut compression the node applies. Either choice can keep highly saturated monochromatic light sources (LEDs, neon signs, tail lights, etc.) from clipping the gamut.

For a fuller picture of what these parameters bring to the table, head to Chapter 9, "Data Levels, Color Management, and ACES." NOTE: The ACES transforms this plugin performs are done correctly, relying on the transforms the Academy lays down, while the Color Transform plugin instead converts colormetrically into the ACES color space—an approach that isn't genuinely correct for ACES pipelines.

### Chromatic Adaptation

Belonging to the Color category, this plugin lets you accurately convert an image that was lit or processed on the assumption of one given color temperature over to a different, user-chosen color temperature. The conversion shifts how every color in the image looks to human vision in just the way a fresh illuminant would—be that illuminant a light in the scene being captured or the color temperature of a display the image appears on. The plugin proves handy whenever you need to carry out particular color-temperature conversions within color-management pipelines, or to dial in precise color-temperature tweaks as part of a creative grade.

- Method: A range of transform methods is on offer in the Method pop-up menu, with CAT02 as the default. Every entry in the Method pop-up menu relies on a distinct set of measurement data to build its own CAT matrix that steers the conversion. Because of that, each method puts its accuracy emphasis on a different group of colors. To illustrate:

CAT02 carries a non-linear component that counters the way extremely saturated blues tend to drift purple, a common shortcoming of rival methods. For the broadest spread of measured data sets it tends to deliver the best outcome, and it shines with emissive sources (displays) and dim viewing surroundings. Bradford Linear sees frequent use as well, even though it's a method where extremely saturated blues will go purple over the course of the transform. It performs nicely both for emissive sources in dim rooms and for reflective sources (theater screens) in dark settings.

Von Kries ranks among the oldest of the commonly used methods, though it too is one where extremely saturated blues will go purple during the transform. Both it and all the rest are on hand should you need to match work produced in some other image-processing application.

- Source/Target Illuminant: You steer this conversion through pop-up menus that set the Illuminant Type for the source (usually whatever color temperature the camera was dialed to) and for the target you'd like the image converted to. With either group of controls, you may select a Standard Illuminant off a list, a Color Temperature by way of a slider, or CIE 1931 xy coordinate values. This conversion is remarkably precise, since the image first moves from the Timeline Color Space into XYZ, and then it's converted to match the LMS (long, medium, short) color space that mirrors how the human eye's cones respond to colors under various illuminants.
- Current Color Space and Gamma: This plugin further accounts for the clip's current color space and gamma, which default to whatever the current timeline is set to. Should you want to alter these values, the Color Space and Gamma menus let you do so.

NOTE: Keep in mind that every method on the list nails neutral colors flawlessly; where they part ways is purely in how each handles the conversion of various bands of saturated color.

### Color Compressor (Studio Version Only)

This filter gives you the ability to squeeze a span of colors toward one chosen target color. It performs at its best on similarly hued regions you've already isolated using a secondary qualifier or window. As an example, when you're adjusting something unevenly lit—a soda can or a dress that has to hold a very specific hue—you can isolate the item and reach for this filter to drive its span of Hue, Saturation, and Luminance nearer to the target color you've pinned down with the color picker.

(Before/After) Employing the Color Compressor plugin within a secondary operation to squeeze the jacket's starting spread of hues down into a tight "target" range

- Target Color: A color control letting you settle on a particular color or sample one out of the image with the eyedropper. Whatever color values you select here are the ones every other color gets nudged toward.
- Compress Hue, Compress Saturation, and Compress Luminance: With these sliders you can separately tighten the span of colors you're adjusting in the image so it tracks the image ever more closely. At 0, no compression happens; at 0.500 the image's original range of colors has been shifted halfway between their starting values and those of the Target Color; and at 1.000 the original color range has been forced to match the Target Color exactly.

### Color Space Transform

This carries out the same kind of color transforms that LUTs do, but rather than relying on lookup tables, the plugin draws on the very math used by Resolve Color Management (RCM) to perform extremely clean color transforms without any clipping.

### Color Space Transform

It surfaces four pop-up menus for setting an Input Colorspace, Input Gamma, Output Colorspace, and Output Gamma, so you can run controlled transforms from the Input settings over to the Output settings directly inside a grade. You needn't have Resolve Color Management switched on to make use of this filter. With the Swap button you can flip the color and gamma space conversion in a hurry.

### Tone Mapping

Switching on tone mapping via Tone Mapping Method accommodates pipelines where one color space has to be turned into another carrying a hugely larger or smaller dynamic range, automating a stretch or squeeze of image contrast in a way that yields a pleasing result free of clipping.

- None: Picking this turns off Input DRT Tone Mapping. Not a bit of tone mapping touches the Input to Timeline Color Space conversion, so you end up with a plain 1:1 mapping to the Timeline Color Space.
- Clip: Hard clips all out-of-bounds values.
- Simple: Leans on a plain curve to carry out this conversion, squeezing or stretching the

highlights and/or shadows of the timeline's dynamic range so they sit better within the output dynamic range. Bear in mind that the "Simple" option maps somewhere between roughly 5500 nits and 100 nits, so when you're going from an HDR source carrying upward of 5500 nits to an SDR destination, the highlights past 5500 nits may still see a bit of clipping.

- Luminance Mapping: Works just like DaVinci, but lands more accurately when every piece of your media shares a single standards-based Input Color Space, like Rec. 709 or Rec. 2020.
- DaVinci: With this option the transform gets tone mapped using a gentle luminance roll-off through the shadows and highlights, plus measured desaturation of image values in the very brightest and darkest stretches of the picture. It comes in especially handy with wide-gamut camera media and makes a solid pick when you're blending footage from several cameras.
- Saturation Preserving: This option likewise applies a gentle luminance roll-off in the shadows and highlights, yet does it without draining saturation from the dark shadows and bright highlights, which makes it a good fit for colorists fond of pushing color harder. Still, since over-saturated highlights can read as unnatural, two parameters are surfaced to hand you some adjustable automated desaturation.

Sat. Rolloff Start: Here you fix a threshold, measured in nits (cd/m2), where saturation begins falling off in step with highlight luminance. This marks where the rolloff begins. Sat. Rolloff Limit: Here you fix a threshold, again in nits (cd/m2), where the image ends up fully desaturated. This marks where the rolloff ends.

- Use Custom Max Input/Output: Ticking these boxes and moving the slider underneath lets you spell out the input image's minimum and maximum luminance in nits. Working the two sliders in tandem, you can decide which value of the Input Gamma maps over to which value of the Output Gamma.
- Adaptation: This compensates for big swings in the viewer's state of visual adaptation between watching a bright image on an HDR display and seeing that same image on an SDR display. With most "average" images, a setting somewhere between 0–10 works best. That said, when you're converting very bright images (a snow scene at midday, for instance), a higher value will tease out more detail within the highlights.
