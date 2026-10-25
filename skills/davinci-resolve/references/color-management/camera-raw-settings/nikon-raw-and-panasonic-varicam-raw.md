# Nikon raw and panasonic varicam raw

Version: DaVinci Resolve 20.3 Reference Manual. Context: Nikon raw, Panasonic varicam raw.
[Chapter index](INDEX.md) / [Previous section](canon-raw-and-cinemadng-and-nikon-raw.md) / [Next section](phantom-cine-master-settings.md) / [Nikon RAW](canon-raw-and-cinemadng-and-nikon-raw.md)
<a id="source-master-settings-1"></a> <a id="source-master-settings-2"></a> <a id="source-panasonic-varicam-raw"></a> <a id="source-project-settings-1"></a> <a id="source-project-settings-2"></a> <a id="source-use-camera-metadata-2"></a> <a id="source-use-camera-metadata-3"></a>

### Master Settings

With these parameters you set the decode quality and method that raw clips get transformed into during debayering.

- Decode Quality: For Nikon RAW files, lets you run the debayer at a resolution of Full, Half, or Quarter so slower systems carry less strain. Media at a lower resolution is lower in quality yet quicker to handle and process. If you must, pick a lower resolution setting that gives smoother real time playback on limited-performance systems as you work, then bump up to a higher quality at final render. A “Force debayer res to highest quality” checkbox over in the Render Settings list of the Deliver page makes this workflow simple to follow.
- Decode Using: Whatever you choose here dictates whether all Nikon RAW media across the project is decoded with the original Camera Metadata settings (the default pick), with Project settings where you set custom values for every clip, or with the Nikon RAW default settings.

### Project Settings

Nikon RAW carries an assortment of settings you can tweak to reshape the image quality of the debayered output. You can only reach the Color Temp and Tint parameters when the White Balance drop-down menu is set to Custom.

- White Balance: The opening seven entries supply White Balance presets that adjust the Color Temp and Tint parameters on their own. They include Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash. An eighth entry, Custom, opens the Color Temp and Tint parameters up for hand adjustment.
- Color Space: Pick one of the common video colorspaces.
- Gamma: Pick N-Log or one of the common video colorspaces.
- Sharpness: A sharpness filter specific to debayering, applied to give the look of heightened

image detail. 20 is unity. The range is 0 to 100.

- Highlights: Lets you reclaim blown-out highlight detail in high-dynamic-range

footage selectively by easing this parameter down, achieving a smooth marriage of the recovered highlights and the unadjusted midtones for a natural-looking outcome. 0 is unity. The range is –100 (minimum) through +100 (maximum).

- Shadows: Lets you brighten or darken shadow detail as you choose. Raising this value reclaims shadow detail recorded under 0 percent while leaving the midtones be. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Color Boost: Lets you raise, naturally, the saturation across low-saturation regions, an operation sometimes called vibrance. It can likewise drop the saturation of those low-saturation regions. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Saturation: Adjusts the color intensity across the picture. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Midtone Detail: Raise this parameter and contrast in image regions carrying heavy edge detail goes up, lifting the impression of sharpness, sometimes called definition. Drop it into a negative value and regions holding scant detail soften, while high-detail areas are left be. Here unity sits at 0, with a span of –100 (minimum) up to +100 (very high).
- Lift: Adjusts the media’s black point, raising or lowering it while rescaling all the midtone values between it and the white point. However you handle this control, the whole of the image data is retained and can be recovered down the line. The range is –100 to +100.
- Gain: Adjusts the media’s white point, raising or lowering it while rescaling all the midtone values between it and the black point. However you handle this control, the whole of the image data is retained and can be recovered down the line. Unity sits at 0, with a span of –100 to +100.
- Contrast: Raising contrast pushes shadows down and lifts highlights, while midtones at 50 percent go untouched. However you handle this control, the whole of the image data is retained and can be recovered down the line. Unity sits at 0, with a span of –100 to +100.

### Use Camera Metadata

Here sit the most basic camera metadata controls on offer for exposure and color.

- Lens Distortion: Tick this box to switch on automatic Lens Distortion Correction.
- Lens Vignette: Tunes the correction strength so you can rein in vignetting.
- Exposure: Lifts or lowers image lightness in units relative to ƒ-stops. Should your intended

exposure move push image data above the maximum white level, don’t fret; the whole of the image data is retained and can be recovered down the line. Unity sits at 0, with a span of –5 to +5.

- Color Temp: Reachable only when White Balance is set to anything other than As Shot. Made to change the “warmth” of the picture. Adjustable in Kelvin. Smaller values correct for “warmer” lighting, while larger ones offset “cool” lighting. Here unity sits at +6500, with a span of +2000 to +50,000.
- Tint: Reachable only when White Balance is set to anything other than As Shot. Made to change the green-to-magenta balance of the picture for images carrying fluorescent tinting. Smaller values add green to offset magenta lighting, while larger ones add magenta to offset green lighting. Unity sits at 0, with a span of –150 to +150.

### Panasonic Varicam RAW

Panasonic Varicam RAW (CRW) comes out of an assortment of Panasonic cameras (like the VariCam 35 and VariCam Pure 4K) recording onto Codex VRAW recorders.

### Master Settings

With these parameters you set the decode quality, white balance, color space, and gamma that raw clips get transformed into during debayering.

- Decode Quality: For Varicam RAW files, lets you run the debayer at a resolution of Full, Half, or Quarter so slower systems carry less strain. Media at a lower resolution is lower in quality yet quicker to handle and process. If you must, pick a lower resolution setting that gives smoother real time playback on limited-performance systems as you work, then bump up to a higher quality at final render. A “Force debayer res to highest quality” checkbox over in the Render Settings list of the Deliver page makes this workflow simple to follow.
- Decode Using: Whatever you choose here dictates whether all Varicam RAW media across the project is decoded with the original Camera Metadata settings (the default pick), with Project settings where you set custom values for every clip, or with the Varicam RAW default settings.

### Project Settings

Panasonic Varicam RAW carries an assortment of settings you can tweak to reshape the image quality of the debayered output. You can only reach the Color Temp and Tint parameters when the White Balance dropdown menu is set to Custom.

- White Balance: The opening seven entries supply White Balance presets that adjust the Color Temp and Tint parameters on their own. They include: Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash. An eighth entry, Custom, opens the Color Temp and Tint parameters up for hand adjustment.
- Sharpness: A sharpness filter specific to debayering, applied to give the look of heightened image detail. 20 is unity. The range is 0 to 100.
- Highlights: Lets you reclaim blown-out highlight detail in high-dynamic-range footage selectively by easing this parameter down, achieving a smooth marriage of the recovered highlights and the unadjusted midtones for a natural-looking outcome. 0 is unity. The range is –100 (minimum) through +100 (maximum).
- Shadows: Lets you brighten or darken shadow detail as you choose. Raising this value reclaims shadow detail recorded under 0 percent while leaving the midtones be. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Color Boost: Lets you raise, naturally, the saturation across low-saturation regions, an operation sometimes called vibrance. It can likewise drop the saturation of those low-saturation regions. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Saturation: Adjusts the color intensity across the picture. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Midtone Detail: Raise this parameter and contrast in image regions carrying heavy edge detail goes up, lifting the impression of sharpness, sometimes called definition. Drop it into a negative value and regions holding scant detail soften while high-detail areas are left be. Here unity sits at 0, with a span of –100 (minimum) up to +100 (very high).
- Lift: Adjusts the media’s black point, raising or lowering it while rescaling all the midtone values between it and the white point. However you handle this control, the whole of the image data is retained and can be recovered down the line. The range is –100 to +100.
- Gain: Adjusts the media’s white point, raising or lowering it while rescaling all the midtone values between it and the black point. However you handle this control, the whole of the image data is retained and can be recovered down the line. Unity sits at 0, with a span of –100 to +100.
- Contrast: Raising contrast pushes shadows down and lifts highlights, while midtones at 50 percent go untouched. However you handle this control, the whole of the image data is retained and can be recovered down the line. Unity sits at 0, with a span of –100 to +100.

### Use Camera Metadata

Here sit the most basic camera metadata controls on offer for exposure and color.

- Color Temp: Reachable only when White Balance is set to anything other than As Shot. Made to change the “warmth” of the picture. Adjustable in Kelvin. Smaller values correct for “warmer” lighting, while larger ones offset “cool” lighting. Here unity sits at +6500, with a span of +2000 to +50,000.
- Tint: Reachable only when White Balance is set to anything other than As Shot. Made to change the green-to-magenta balance of the picture, for images carrying fluorescent tinting. Smaller values add green to offset magenta lighting, while larger ones add magenta to offset green lighting. Unity sits at 0, with a span of –150 to +150.
