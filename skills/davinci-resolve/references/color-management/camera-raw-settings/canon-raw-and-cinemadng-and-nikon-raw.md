# Canon raw and cinemadng and nikon raw

Version: DaVinci Resolve 20.3 Reference Manual. Context: Canon raw, Cinemadng, Nikon raw.
[Chapter index](INDEX.md) / [Previous section](canon-raw-master-settings.md) / [Next section](nikon-raw-and-panasonic-varicam-raw.md) / [Canon RAW](canon-raw-master-settings.md)
<a id="source-cinemadng"></a> <a id="source-cinemadng-files-and-blackmagic-design-film"></a> <a id="source-master-settings"></a> <a id="source-nikon-raw"></a> <a id="source-project-settings"></a> <a id="source-use-camera-metadata"></a> <a id="source-use-camera-metadata-1"></a>

### Use Camera Metadata

Here sit the most basic camera metadata controls on offer for exposure and color.

- Exposure: Raises or drops image lightness in units tied to ƒ-stops. Even if the exposure tweak you want pushes image data past the top white level, there’s no cause for concern; all image data stays intact and remains recoverable in later adjustments. 0 is unity. The range is –5 to +5.
- Color Temp: Available only when White Balance sits at something besides As Shot. Built to shift the “warmth” of the picture. Tunable in Kelvin. Lower figures compensate for “warmer” lighting, while higher ones compensate for “cool” lighting. +6500 is unity. The range is +2000 to +50,000.
- Tint: Available only when White Balance sits at something besides As Shot. Built to shift the picture’s green-to-magenta balance, for images carrying fluorescent tinting. Lower figures introduce green to counter magenta lighting, while higher ones introduce magenta to counter green lighting. 0 is unity. The range is –150 to +150.

### CinemaDNG

An open format able to hold high-resolution raw image data across a wide dynamic range, CinemaDNG is one of the formats the Blackmagic Design Camera records whenever you shoot in raw mode. With the Highlight Recovery checkbox ticked, CinemaDNG images decode at full dynamic range. Better debayering for raw CinemaDNG media shot on any of the Blackmagic Design cameras arrived in DaVinci Resolve version 11.2.1. The “Apply Pre Tone Curve” setting governs whether you get the older debayering method (when on) or the newer, visually upgraded one (when off).

### Master Settings

These parameters let you choose, for raw CinemaDNG clips, the decode quality plus the white balance, color space, and gamma they convert to as they are debayered.

- Decode Quality: For CinemaDNG raw files, lets you run the debayer at a resolution of Full, Half, or Quarter so slower systems carry less strain. Media at a lower resolution is lower in quality yet quicker to handle and process. If you must, pick a lower resolution setting that gives smoother real time playback on limited-performance systems as you work, then bump up to a higher quality at final render. A “Force debayer res to highest quality” checkbox over in the Render Settings list of the Deliver page makes this workflow simple to follow.
- Decode Using: Whatever you choose here dictates whether all CinemaDNG media across the project is decoded with the original Camera Metadata settings (the default pick), with Project settings where you set custom values for every clip, or with the CinemaDNG default settings.
- Apply Pre Tone Curve: Leave this checkbox off (the default for new projects made in DaVinci Resolve 11.2.1 or newer) and DaVinci Resolve debayers CinemaDNG raw media through an upgraded method that looks better, especially for media shot on any of the Blackmagic Design cameras. Turn this checkbox on (the default for projects made in older versions of DaVinci Resolve) and the older debayering method comes back for backward compatibility. That said, switching Pre Tone Curve on may also give nicer results for CinemaDNG raw files originating elsewhere. If you’re bringing in .dng media from cameras other than Blackmagic Design ones, test both settings and see which debayering you like.
- Apply Soft Clip: Offered only while Apply Pre Tone Curve is off. With it on, high dynamic range portions of the signal (super-white highlights) are reclaimed as visible image detail you can work with, much like reaching for the Highlights control to recover these otherwise clipped portions of the signal.

### Project Settings

CinemaDNG carries an assortment of settings you can tweak to reshape the image quality of the debayered output. You can only reach the Color Temp and Tint parameters when the White Balance drop-down menu is set to Custom.

- Color Science: Lets you pick which version of camera color science decodes your CinemaDNG media.

Camera Metadata: Grabs whichever version of color science the camera picked at the moment of shooting. Gen 4: The first version of color science offered for recording and decoding CinemaDNG media.

- White Balance: The opening seven entries supply White Balance presets that adjust the Color Temp and Tint parameters on their own. They include: Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash. An eighth entry, Custom, opens the Color Temp and Tint parameters up for hand adjustment.
- Color Space: Several color spaces can be set, hinging on the workflow you intend:

Rec. 709: Decodes into the standard color space that the Rec. 709 standard defines for high definition video. P3 D60: Targets the standard P3 color space that the DCI standard defines for digital cinema projection. Blackmagic Design: Resolves to a log-encoded color space, remapping the raw data toward an approximation of the Log-C standard. Picking Blackmagic Design Film also pushes the Gamma setting to Blackmagic Design Film. This setting yields flat-contrast image data that holds onto image detail with broad latitude for adjustment, which suits it as a jumping-off point for detailed grading and likewise fits log workflows aimed at film output.

- Gamma: Five gamma settings exist, hinging on the jumping-off point you want for further grading.

  2.4: A plain power-function gamma setting often used for broadcast. 2.6: A plain power-function gamma setting often used for digital cinema projection. Rec. 709: A gamma of 2.35, holding a linear segment close to black, which comes near the EBU recommended gamma for broadcast. sRGB: A gamma of 2.2, holding a linear segment close to black, intended for display on computer monitors alongside the sRGB color space. Linear: A plain linear gamma setting. Blackmagic Design Film: A log-encoded gamma setting coming close to Cineon encoding, the main distinction being that extra data sits in the darkest stretch of the Blackmagic Design Film signal. Choose this setting and the right variation of gamma gets applied based on your particular sensor, whether 4K or 4.6K. Blackmagic Design Video: A normalized gamma setting that hands you a fast jumping-off point for grading if you’d rather not start from a log-encoded image.

- Highlight Recovery: A checkbox that folds in extra highlight sensor data that the standard decoding matrix usually clips off. When your highlights are badly clipped, you may dig out extra image detail this way, though it might carry odd color artifacts.
- Sharpness: A sharpness filter specific to debayering, applied to give the look of heightened image detail. 20 is unity. The range is 0 to 100.
- Highlights: Lets you reclaim blown-out highlight detail in high-dynamic-range footage selectively by easing this parameter down, achieving a smooth marriage of the recovered highlights and the unadjusted midtones for a natural-looking outcome. 0 is unity. The range is –100 (minimum) through +100 (maximum).
- Shadows: Lets you brighten or darken shadow detail as you choose. Raising this value reclaims shadow detail recorded under 0 percent while leaving the midtones be. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Color Boost: Lets you raise, naturally, the saturation across low-saturation regions, an operation sometimes called vibrance. It can likewise drop the saturation of those low-saturation regions. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Saturation: Adjusts the color intensity across the picture. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Midtone Detail: Raise this parameter and contrast in image regions carrying heavy edge detail goes up, lifting the impression of sharpness, sometimes called definition. Drop it into a negative value and regions holding scant detail soften while high-detail areas are left be. Here unity sits at 0, with a span of –100 (minimum) up to +100 (very high).
- Lift: Adjusts the media’s black point, raising or lowering it while rescaling all the midtone values between it and the white point. No matter how you work this control, every bit of image data is kept and stays recoverable in later adjustments. The range is –100 to +100.
- Gain: Adjusts the media’s white point, raising or lowering it while rescaling all the midtone values between it and the black point. No matter how you work this control, every bit of image data is kept and stays recoverable down the line. Unity sits at 0, with a span of –100 to +100.
- Contrast: Raising contrast pushes shadows down and lifts highlights, while midtones at 50 percent go untouched. No matter how you work this control, every bit of image data is kept and stays recoverable down the line. Unity sits at 0, with a span of –100 to +100.

### Use Camera Metadata

Here sit the most basic camera metadata controls on offer for exposure and color.

- Exposure: Lifts or lowers image lightness in units relative to ƒ-stops. Should the exposure move you want push image data above the maximum white level, don’t fret; every bit of image data is kept and stays recoverable down the line. Unity sits at 0, with a span of –5 to +5.
- Color Temp: Reachable only when White Balance is set to anything other than As Shot. Made to change the “warmth” of the picture. Adjustable in Kelvin. Smaller values correct for “warmer” lighting, while larger ones offset “cool” lighting. Here unity sits at +6500, with a span of +2000 to +50,000.
- Tint: Reachable only when White Balance is set to anything other than As Shot. Made to change the green-to-magenta balance of the picture, for images carrying fluorescent tinting. Smaller values add green to offset magenta lighting, while larger ones add magenta to offset green lighting. Unity sits at 0, with a span of –150 to +150.

### CinemaDNG Files and Blackmagic Design Film

Blackmagic Design’s log-encoded Blackmagic Design Film gamma setting, which yields flat-contrast, wide-gamut image data that holds onto image detail with broad latitude for adjustment, is a tweaked take on the standard Cineon curve. Those tweaks, though, are meant to play to the strengths of the sensors inside the Blackmagic Design cameras. Just as with clips shot on Cineon, the ARRI ALEXA’s Log-C gamma, or Sony’s own S-Log or S-Log2 formats, clips using Blackmagic Design Film need normalizing, whether through Resolve Color Management (RCM), through a hand-done adjustment to color and contrast, or by laying on a LUT, using the same methods covered earlier.

### Nikon RAW

Nikon RAW (NEF) comes out of an assortment of Nikon cameras.
