# Arri camera raw decoding explained

Version: DaVinci Resolve 20.3 Reference Manual. Context: Arri.
[Chapter index](INDEX.md) / [Next section](arri-and-blackmagic-raw.md)
<a id="source-arri"></a> <a id="source-camera-raw-decoding"></a> <a id="source-camera-raw-decoding-explained"></a> <a id="source-camera-raw-image-inspector"></a> <a id="source-camera-raw-project-palette-in-the-color-page"></a> <a id="source-camera-raw-project-settings"></a> <a id="source-camera-raw-project-settings-1"></a> <a id="source-camera-raw-settings"></a> <a id="source-camera-raw-settings-part-1"></a> <a id="source-color-page-image-processing"></a> <a id="source-deliver-page-output"></a> <a id="source-master-settings"></a> <a id="source-project-settings"></a> <a id="source-raw-image-data"></a> <a id="source-the-image-inspector-for-a-blackmagic-raw-file"></a> <a id="source-use-camera-metadata"></a>

### Camera Raw Settings

Every setting offered for each of the camera raw formats DaVinci Resolve supports is examined closely in this chapter. You’ll find these settings within the Camera Raw panel of the Project Settings, through the Inspector on the Media, Cut, and Edit pages, or inside the Camera Raw palette on the Color page.

### Camera Raw Decoding Explained

The “raw” in camera raw media formats refers to the way they grab unprocessed color space data straight off the sensor of whichever digital cinema camera shot the footage. Because raw image data can’t be read by a person, it has to be debayered or demosaiced so that the original raw data becomes image data ready to feed into DaVinci Resolve’s image processing pipeline.

### Raw Image Data

### Camera Raw Decoding

### Color Page Image Processing

### Deliver Page Output

The first image processing step to run is raw decoding, and it runs ahead of everything else on the Color page — even ahead of the Source bar in the Node Editor. That makes it worth recognizing that the best conversion from raw image data into DaVinci Resolve-friendly image data is the one that holds onto as much image data as possible for further work. Because DaVinci Resolve’s image processing pipeline carries every transformed bit of raw data at 32-bit floating point accuracy with remarkable fidelity, the chief value of the Camera Raw parameters lies in dialing in whatever opening adjustments give grading its best possible launch point. The Raw Profile menu is where you reach each set of Camera Raw settings. What follows describes the settings offered for each of the camera raw media formats that DaVinci Resolve supports.

### Camera Raw Project Settings

Inside the Project Settings, the Camera Raw panel holds parameter groups, one for every camera raw media format DaVinci Resolve supports. Working with these Camera Raw panel parameters lets you replace the original camera metadata recorded at capture time and adjust every piece of camera raw media across your whole project all at once.

### Camera Raw project settings

Different format-specific controls accompany each supported camera format. The Camera Raw palette on the Color page mirrors these same controls, so that — once Decode Using is set to Clip — you can tune the Camera Raw parameters clip by clip for individual clips in a Timeline.

### Camera Raw project palette in the Color page

### Camera Raw Image Inspector

Within the Inspector, the Image panel surfaces the Camera Raw parameters. Should the video clip sit in a Raw format, that particular camera’s Raw controls appear for you to adjust. This panel can likewise adjust Raw still images from Nikon (NEF) and Canon (CR2) cameras.

### The Image Inspector for a Blackmagic RAW file

### ARRI

Recording on the ARRI ALEXA can produce ProRes, DNxHD, or raw image data. In raw mode, image data comes straight off the Bayer sensor and has to be debayered by DaVinci Resolve.

### Master Settings

Debayering ARRI ALEXA media couldn’t be much simpler. Only three Master settings exist.

- Decode Quality: Debayers your ARRI ALEXA raw files at one of three resolutions — Full, Half, or Quarter — so that slower systems run better. Media at a lower resolution is poorer in quality yet quicker to handle and process. When you need to, pick a lower resolution that gives smoother real time playback on performance-limited systems as you work, then bump it up to a higher quality for the final render. On the Deliver page, within its Render Settings list, sits a checkbox reading “Force debayer res to highest quality” that makes this workflow simple to follow.
- Decode Using: Whatever you pick here governs whether every bit of ARRI ALEXA media across the project gets decoded with the original Camera Metadata settings (the default choice), with Project settings — where you specify custom settings to apply to all clips — or with the ARRI default settings.
- Import Media at Open Gate Resolution: Lets DaVinci Resolve reach the “open gate” region of clips shot on ALEXA cameras that support that mode, yielding a 3.4K image with additional room for repositioning and stabilization.

### Project Settings

You can tune the color and exposure of ALEXA clips with the decoder settings below.

- Lift: Shifts the media’s black point up or down while scaling every midtone value sitting between it and the white point. No matter how far you push this control, all image data stays intact and can be pulled back in later adjustments. Its range runs from –100 to +100.
- Gain: Shifts the media’s white point up or down while scaling every midtone value sitting between it and the black point. No matter how far you push this control, all image data stays intact and can be pulled back in later adjustments. Unity sits at 0. Its range runs from –100 to +100.
- Contrast: Pushing contrast up drops shadows and lifts highlights, leaving midtones at 50 percent untouched. No matter how far you push this control, all image data stays intact and can be pulled back in later adjustments. Unity sits at 0. Its range runs from –100 to +100.
- Tint: Shifts color balance to slide the image between magenta and green; handy for balancing footage carrying a magenta or green cast, like that from sodium vapor or fluorescent bulbs. Unity sits at 0. Its range runs from –150 to +150.
- Sharpness: A sharpness filter tied to debayering, applied to give the look of heightened image detail. Unity sits at 0 here, with 10 as the default. Its range runs from 0 to 100.
- Highlights: Lets you reach back into blown-out highlight detail within high-dynamic-range media simply by lowering this parameter, blending the recovered highlights smoothly into the untouched midtones for a natural-looking outcome. Unity sits at 0. Its range runs from –100 (minimum) up to +100 (maximum).
- Shadows: Lets you brighten or deepen shadow detail at will. Pushing this value up recovers shadow detail captured beneath 0 percent while sparing the midtones. Unity sits at 0. Its range runs from –100 (minimum) up to +100 (very high).
- Color Boost: Lets you lift the saturation of weakly saturated areas in a lifelike way, an operation sometimes called vibrance. It can equally drop the saturation of weakly saturated areas. Unity sits at 0. Its range runs from –100 (minimum) up to +100 (very high).
- Saturation: Tunes how intense the image’s color is. Unity sits at 0. Its range runs from –100 (minimum) up to +100 (very high).
- Midtone Detail: Push this parameter up and the contrast across image regions carrying heavy edge detail climbs, boosting the sense of image sharpness — sometimes called definition. Drop this parameter into negative territory and image regions holding little detail soften while heavily detailed areas stay as they are. Unity sits at 0. Its range runs from –100 (minimum) up to +100 (very high).
- Decode as monochrome: Tick this box and the ArriRaw footage decodes purely in black and white. The setting is built for the Alexa Monochrome line of cameras. Apply it to ordinary ARRI Raw and it merely throws away the color information. Any RAW controls touching color — saturation, color temp, and the like — stop having any effect.

### Use Camera Metadata

These are the most basic camera metadata settings on offer for exposure and color.

- Color Temp: Shifts color balance to change how “warm” the image looks. It’s adjustable in Kelvin. Lower numbers compensate for “warmer” lighting, while higher numbers compensate for “cool” lighting. Unity sits at +2000. Its range runs from +2000 to +11,000.
- Tint: Available only once White Balance is set to anything besides As Shot. Built to shift the green to magenta balance of the image, for footage with fluorescent tinting. Lower numbers add green to offset magenta lighting, while higher numbers add magenta to offset green lighting. Unity sits at 0. Its range runs from –12 to +12.
- Exposure: Raises or drops image lightness in units tied to ASA values. Should your planned exposure change lift image data past the maximum white level, there’s nothing to fear; all image data stays intact and can be pulled back in later adjustments. Unity sits at 160. Its range runs from +160 to +3200.
- Finetune Red: Advanced debayer setting.
- Finetune Green: Advanced debayer setting.
- Finetune Blue: Advanced debayer setting.
