# Red and sony raw

Version: DaVinci Resolve 20.3 Reference Manual. Context: Red, Sony raw.
[Chapter index](INDEX.md) / [Previous section](red-master-red-settings.md) / [RED](red-master-red-settings.md) / [Next section](sony-raw-use-camera-metadata.md)
<a id="source-camera-raw-settings-part-4"></a> <a id="source-decoder-settings"></a> <a id="source-master-settings"></a> <a id="source-project-settings-1"></a> <a id="source-sony-raw"></a> <a id="source-use-camera-metadata"></a>

### Decoder Settings

This second batch of settings holds further controls for fine-tuning the debayering of RED raw image data. Which controls surface rests on which Color Science setting is picked above. A good many of the settings here are color correction adjustments, several echoing comparable controls over in the Color page. The FLUT and DRX controls, though, govern the exposure of the debayered media being fed into the DaVinci Resolve image processing pipeline, and so let you reclaim image detail from R3D source media in any case where detail in the highlights or shadows is being clipped or crushed by the default settings and would otherwise stay out of reach to DaVinci Resolve.

- De-noise: Lays image-wide noise reduction across the picture. Seven settings exist, running mild to maximum, that let you weigh noise reduction against whatever image degradation might follow.
- OLPF Compensation: (color science versions 1 and 2) OLPF compensation lays a low pass filter over the image to cut color moiré. Four options exist: Off (the default), Low, Medium, and High.
- Image Detail: (color science versions 1 and 2) Governs the demosaicing algorithm used for the software decoding of R3D media. You can pick a level of sensor detail extraction: Low, Medium, and High (recommended). Should you be running a RED ROCKET card, this setting goes unheeded, since a fixed algorithm takes over instead.
- FLUT: (color science versions 1 and 2) A gain operation letting you push or pull the ISO in finer increments. 0 is unity. The range is –8 to +8.
- Contrast: Pushing contrast up pulls shadows down and lifts highlights, while the midtones at 50 percent go untouched. At the 100 and 0 percent boundaries the image is compressed in place of being clipped. Here 0 is unity. The range is –1 to +1.
- Saturation: (color science versions 1 and 2) Sets how intense the image's color runs. Its unity sits at 1, and it runs across a range from 0 (minimum) up through 5.0 (very high).
- DRX: (color science versions 1 and 2) A Dynamic Range control (X) letting you reclaim highlights while weighing in Color Temperature (degrees Kelvin) and Tint. For it, 0 marks unity, with 1.0 as the maximum value.
- Shadow: (color science version 1 and 2) Hands you control over the toe (low range) belonging to the FLUT adjustment. Here too 0 is unity. The range is –2 to +2.
- Brightness: Sets image lightness. Image data gets compressed rather than clipped at 100 and 0 percent. 0 is unity. The range is –10 to +10.
- Flashing pixel adjust: A setting that lays on noise reduction to clear or curb any flashing pixels captured off the sensor. Levels are: None, Low, Medium, and High.

For IPP2 workflows, three more parameters open up, though they function solely while DaVinci Resolve runs DaVinci YRGB Color Managed color science with the Project Settings' Color Management panel having its Timeline to Output Gamut Mapping set to RED IPP2 Gamut Mapping. Mirrored over in the Color Management panel once switched on, these controls let you tone map wide gamut media that's being graded down toward a smaller gamut, Rec. 709 among them.

The RED IPP2 Gamut Mapping controls that surface in the Color Management tab of the Project Settings

- Output Tone Map: (color science IPP2) Hands you an easy setting for fixing the resulting contract as wide dynamic range images undergo tone mapping into standard dynamic range (SDR) output. The settings on offer: None, Low, Medium, and High. Low yields less contrast, whereas High yields more.
- Highlight Roll Off: (color science IPP2) Through five settings you set how far the highlights get rolled off so they sit inside the current gamut. On offer: None, Hard, Medium, Soft, and Very Soft. Hard delivers the least roll-off, while Very Soft delivers the most. The setting plays off the HDR Peak Nits slider below.
- HDR Peak Nits: (color science IPP2) Sets how much highlight compression Highlight Roll Off carries out.

### Use Camera Metadata

The most basic camera metadata settings for exposure and color that are on offer.

- ISO: A gain operation that holds the black point at 0 while pushing the image's white point up or down, scaling everything between them linearly. Pushing the ISO up only leaves boosted highlights more compressed; no clipping happens. 320 is unity. The range is 50–6400.
- Exposure Adjust: Raises or lowers image lightness in units tied to ƒ-stops. Reaching for exposure to push the image past 100 or pull it below 0 clips, rather than compresses, the image data that travels onward to the DaVinci Resolve image processing pipeline. For this control 0 is unity. The range is –7 to +7.
- Color Temp: Built to shift the image's "warmth" while keeping the scene's white elements looking neutral. You adjust it in degrees Kelvin. Drop the value to correct for "warmer" lighting; raise it to correct for "cool" lighting. The parameter exists specifically to tune RED linear light image data toward the most photometrically accurate correction. For it, 5600 is unity. The range is 1700 to 10,000.
- Tint: Color balance correction for images carrying a green or magenta color cast, like those shot under fluorescent or sodium vapor bulbs. The parameter exists specifically to tune RED linear light image data toward the most photometrically accurate correction. Here 0 is unity. The range is –100 to +100.

### Sony RAW

Sony builds several digital cinema cameras, the F65 and F55 among them, that capture wide latitude, high-gamut media — recording either through Sony's 12-bit SR codec, or instead as 16-bit raw media files. Because Sony's cameras steer clear of a traditional Bayer pattern, special debayering is called for with F65 raw media, and the image data gets demosaiced through the raw controls and parameters below.

### Master Settings

Through these parameters you settle the decode quality, white balance, color space, and gamma into which Sony raw clips get converted as debayering happens.

- Decode Quality: Sets the image quality of the decoded Sony raw data passed along to the DaVinci Resolve image processing pipeline, no matter the Play Quality setting. Whichever Decode Resolution you pick weighs directly on real time performance, and decoding performance hinges entirely on your system's hardware capabilities. Where needed, you can pick a lower resolution setting that yields better real time playback on systems with limited performance as you work, then move up to a higher quality once you

render the final output. Following such a workflow is made simple by a "Force debayer res to highest quality" checkbox, found within the Deliver page's Render Settings list.

- Decode Using: Whichever option you pick sets whether every bit of F65 media across the project gets decoded through the original Camera Metadata settings (the default pick), through Project settings where you assign custom settings to apply across all clips, or through the Sony default settings.

### Project Settings

These settings steer the core methods used to debayer Sony raw media. The picks you make here set the basic color and contrast you're opting to pull out of the camera raw image data.

- White Balance: The first seven options hand you White Balance presets, which set the Color Temp and Tint parameters on their own. Those options take in: Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash. An eighth option, Custom, opens the Color Temp and Tint parameters up for you to adjust.
- Color Space: A range of color spaces are adjustable, depending on the workflow you have in mind:

Rec. 709: Decodes into the standard color space the Rec. 709 standard lays down for high definition video. P3 D60: Decodes RGB-encoded image data carrying a D60 white point, meant for monitoring on a display that's P3-compatible. SGamut: Decodes into the wider S-gamut color space from Sony, built to hand you the broadest range of image data for adjustment. SGamut3: Its gamut lines up with SGamut exactly, though color reproduction lands more accurate, as stated in the Sony whitepaper "Technical Summary for S-Gamut3Cine/S-Log3 and S-Gamut3/S-Log3". SGamut3.Cine: As laid out in that same Sony whitepaper, "Technical Summary for S-Gamut3Cine/S-Log3 and S-Gamut3/S-Log3", S-Gamut3.Cine is built to hand you a more conventionally log-encoded workflow whose color reproduction runs a touch wider than the P3 gamut. P3: Decodes into RGB-encoded image data carrying a D61 white point, meant for use when putting out media for DCI mastering. ACES: Decodes into image data that maps onto the ACES profile for whichever camera was used.

- Gamma: Five gamma settings are on offer, depending on the starting point you want for further grading.

Gamma 2.4: A straightforward power-function gamma choice that broadcast work typically relies on. Gamma 2.6: The same plain power-function gamma, but the one ordinarily chosen for digital cinema projection. Rec. 709: A gamma curve suited to a Rec. 709 display. SLog: These Sony SLog gammas aren’t meant to be viewed directly; instead they hand you broad latitude for grading work — 14-stops by Sony’s own figures. 18% gray sits at 38%. SLog2: Compared with SLog, this one carries a half-stop offset so a wider dynamic range becomes possible. 18% gray sits at 32%. SLog3: A take on SLog that Sony calls “easier to grade.” 18% gray sits at 40%. As the Sony paper titled “Technical Summary for S-Gamut3Cine/S-Log3 and S-Gamut3/S-Log3” lays out, this gamma targets a more conventional log-encoded pipeline, with a curve close to — though not exactly matching — Cineon workflows. Linear: A plain linear gamma choice.

- Lift: Moves the media’s black point up or down, rescaling every midtone value that falls between it and the white point. However you set this control, none of the image data is lost — it stays available to pull back in later passes. The range is –100 to +100.
- Gain: Moves the media’s white point up or down, rescaling every midtone value sitting between it and the black point. Whatever you do with this control, the full image data remains and can be recovered in later passes. 0 is unity. The range is –100 to +100.
- Contrast: Pushing contrast higher pulls shadows down and lifts highlights, but midtones at 50 percent stay put. No matter how you set this control, all the image data survives and is recoverable in later passes. 0 is unity. The range is –100 to +100.
- Sharpness: A debayer-specific sharpening filter that lends the look of crisper detail. 20 is unity. The range is 0 to 100.
- Highlights: Pulling this parameter down makes it simple to claw back clipped highlight detail in high-dynamic-range media, blending the recovered highlights smoothly into the untouched midtones for a natural-looking outcome. 0 is unity. The range is –100 (minimum) through +100 (maximum).
- Shadows: Lets you brighten or darken shadow detail at will. Pushing this value up brings back shadow detail captured below 0 percent without disturbing the midtones. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Color Boost: Lets you lift the saturation of weakly saturated regions in a natural way — what’s often called a vibrance operation. It can equally pull down saturation in those low-saturation regions. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Saturation: Governs how intense the image’s colors appear. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Midtone Detail: Push this parameter up and the contrast within high-edge-detail regions climbs, boosting the sense of sharpness — sometimes called definition. Drop it to a negative figure and low-detail regions soften while the high-detail areas are spared. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Enable ICVFX: When you shoot VFX inside a virtual production workflow, the background LED wall lighting blends with the ordinary lighting falling on foreground people. Ticking this box lets you correct for that combined lighting.

LED Wall Kelvin: Set the LED wall’s color temperature here. Light Blend: Sets how the ordinary lighting and the LED wall lighting are proportioned against each other. At a value of 100 you get the ordinary lighting on its own (the same as having ICVFX mode disabled). At a value of 0 only the LED wall lighting remains.
