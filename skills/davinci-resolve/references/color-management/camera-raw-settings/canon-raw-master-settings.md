# Canon raw master settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Canon raw.
[Chapter index](INDEX.md) / [Previous section](arri-and-blackmagic-raw.md) / [Next section](canon-raw-and-cinemadng-and-nikon-raw.md)
<a id="source-camera-raw-settings-part-2"></a> <a id="source-canon-raw"></a> <a id="source-master-settings-2"></a> <a id="source-project-settings-2"></a>

### Canon RAW

Canon RAW (CRW) comes out of a range of Canon cameras.

### Master Settings

With these parameters you set the decode quality and method that raw clips get converted to once they’re debayered.

- Decode Quality: Debayers your Canon RAW files at one of three resolutions — Full, Half, or Quarter — to help slower systems perform. Media at a lower resolution is poorer in quality but quicker to handle and process. When you need to, pick a lower resolution that gives smoother real time playback on performance-limited systems as you work, then bump it up to a higher quality for the final render. On the Deliver page, within its Render Settings list, sits a checkbox reading “Force debayer res to highest quality” that makes this workflow simple to follow.
- Decode Using: Whatever you pick here governs whether every bit of Canon RAW media across the project gets decoded with the original Camera Metadata settings (the default choice), with Project settings — where you specify custom settings to apply to all clips — or with the Canon RAW default settings.

### Project Settings

A range of settings in Canon RAW can be tweaked to alter how the debayered result looks in terms of image quality. Only when the White Balance drop-down menu sits at Custom do the Color Temp and Tint parameters become available.

- White Balance: The first seven choices supply White Balance presets, which set the Color Temp and Tint parameters for you. Those choices are Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash. The eighth choice, Custom, opens up the Color Temp and Tint parameters for you to adjust.
- Color Space: Pick Canon Cinema Gamut or other common colorspaces.
- Gamma: Pick a Canon Log version or Rec 709.
- Sharpness: A sharpness filter tied to debayering, applied to give the look of heightened

image detail. Unity sits at 20. Its range runs from 0 to 100.

- Highlights: Lets you pull back blown-out highlight detail in high-dynamic-range footage selectively by easing this parameter down, smoothly knitting the recovered highlights into the untouched midtones for a natural look. 0 is unity. The range is –100 (minimum) through +100 (maximum).
- Shadows: Lets you brighten or darken shadow detail at your discretion. Pushing this value up pulls back shadow detail captured beneath 0 percent while sparing the midtones. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Color Boost: Lets you lift, in a natural way, the saturation across regions that hold little saturation, an operation sometimes called vibrance. It can equally be used to drop the saturation of those low-saturation regions. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Saturation: Tunes the color intensity throughout the image. Here unity sits at 0, with a span of –100 (minimum) up to +100 (very high).
- Midtone Detail: Push this parameter up and the contrast across image regions rich in edge detail rises, boosting the sense of sharpness, sometimes called definition. Pull it down into negative territory and regions carrying little detail get softened while the high-detail areas stay untouched. Here unity sits at 0, with a span of –100 (minimum) up to +100 (very high).
- Lift: Tunes the media’s black point, lifting or dropping it while rescaling every midtone value sitting between it and the white point. However you set this control, all image data stays intact and remains recoverable in later adjustments. The range is –100 to +100.
- Gain: Tunes the media’s white point, lifting or dropping it while rescaling every midtone value sitting between it and the black point. However you set this control, all image data stays intact and remains recoverable in later adjustments. 0 is unity. The range is –100 to +100.
- Contrast: Pushing contrast up drives shadows down and pulls highlights up, while midtones at 50 percent stay put. However you set this control, all image data stays intact and remains recoverable in later adjustments. 0 is unity. The range is –100 to +100.
