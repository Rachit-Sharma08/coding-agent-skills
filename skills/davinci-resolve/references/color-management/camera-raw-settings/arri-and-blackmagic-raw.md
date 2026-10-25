# Arri and blackmagic raw

Version: DaVinci Resolve 20.3 Reference Manual. Context: Arri, Blackmagic raw.
[Chapter index](INDEX.md) / [Previous section](arri-camera-raw-decoding-explained.md) / [Next section](canon-raw-master-settings.md) / [ARRI](arri-camera-raw-decoding-explained.md)
<a id="source-arri-media-and-log-c"></a> <a id="source-blackmagic-raw"></a> <a id="source-braw-files-and-blackmagic-design-film"></a> <a id="source-braw-sidecar-metadata-files"></a> <a id="source-master-settings-1"></a> <a id="source-modifying-sidecar-files"></a> <a id="source-project-settings-1"></a> <a id="source-use-camera-metadata-1"></a>

### ARRI Media and Log-C

Most often, ALEXA media is captured with Log-C gamma and color processing, a close cousin of the Cineon Log gamma curve that Kodak created to deliver flat-contrast, wide-gamut image data holding onto image detail with broad latitude for adjustment. No ALEXA raw parameter governs this, so for Rec. 709 monitoring and deliverables you have to “normalize” Log-C clips by one of three methods. One way is to let Resolve Color Management (RCM) normalize log-encoded media automatically according to which type of media it is. Another is to build your own adjustment that normalizes Log-C clips during grading, using the Color page parameters. That route hands you the greatest flexibility, since you’ll craft custom settings that wring out the most image data available in every scene. A third way is to apply a LUT that normalizes Log-C clips, giving you a quick launch point for more grading. Used that way, LUTs may go on either as an output LUT — when nothing but ALEXA raw media fills the entire Timeline — or as a LUT applied to a single node of a grade, when you’re blending ALEXA raw media with other formats. This offers a quick, easy way to linearize ALEXA media, which can come in handy for generating dailies for offline editing. A single LUT, though, might not fit every clip. When you’re putting individual LUTs on each

clip, you can build several LUTs, each carrying different contrast settings, so as to reap the speed gains of LUTs while still accounting for how individual clips differ. ARRI hosts an online LUT generator you can use to build custom LUTs for a range of color correction applications, located at: https://www.arri.com/en/learn-help/learn-helpcamera-system/tools/lut-generator

### Blackmagic RAW

A raw format that Blackmagic Design built, used across a range of Blackmagic cameras. The format leans on the greater processing power of today’s cameras to carry out a degree of in-camera pre-processing (noise management, sensor profiling, and edge reconstruction among them) so as to partly de-mosaic the image and then re-encode the outcome, taking the originating image sensor’s characteristics into account. Encoding is done in a way that still permits the usual raw controls later on, yet keeps files efficiently compressed (within a custom non-linear 12-bit space) and not taxing to decode and use. BRAW media may be encoded either at a Constant Bitrate (with variable compression of 3:1, 5:1, 8:1, and 12:1) or at Constant Quality (with a variable bitrate).

### BRAW Sidecar Metadata Files

BRAW files were built to carry descriptive metadata that supports look management from the set all the way through post. That metadata lives both inside the .braw files themselves and within .sidecar files stored next to the media. Whenever a metadata .sidecar file exists, it always wins out over the embedded metadata when it comes to decoding. With no .sidecar file present, though, decoding the .braw file reverts to the embedded metadata.

### Modifying Sidecar Files

The Camera Raw palette on the Color page lets you Update a BRAW clip’s sidecar file to reflect changes you made to the Camera Raw settings. Hit Update Sidecar to commit changes, and hit Export Frame to write out a one-frame image for reference.

### Master Settings

With these parameters you set the decode quality and method that raw clips get converted to once they’re debayered.

- Decode Quality: Debayers your .braw files at one of four resolutions — Full, Half, Quarter, or Eighth — to help slower systems perform. Media at a lower resolution is poorer in quality but quicker to handle and process. When you need to, pick a lower resolution that gives smoother real time playback on performance-limited systems as you work, then bump it up to a higher quality for the final render. On the Deliver page, within its Render Settings list, sits a checkbox reading “Force debayer res to highest quality” that makes this workflow simple to follow.
- Decode Using: Whatever you pick here governs whether every bit of .braw media across the project gets decoded with the original Camera Metadata settings (the default choice), with Project settings — where you specify custom settings to apply to all clips — or with the Blackmagic Raw default settings.

### Project Settings

These parameters let you set the color science, white balance color space, gamma, and other visual options that steer how the image is transformed to fit your program and RCM.

- Color Science: Lets you pick which version of camera color science to decode .braw media with.

Camera Metadata: Picks whichever color science version the camera was set to at the moment of shooting. Gen 4: When it comes to recording .braw media and decoding it, this is the original color science version on offer. Gen 5: A fresher curve with more of a film feel, built for improved skin tones and a high contrast/saturation color response.

- White Balance: The first seven choices supply White Balance presets, which set the Color Temp and Tint parameters for you. Those choices are Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash. The eighth choice, Custom, opens up the Color Temp and Tint parameters for you to adjust. As Shot is the default.
- Color Space: Debayering .braw data means picking a color space to turn the raw signal into. Keep in mind the color space you pick is only a launch point for further correction. No workflow obliges you to pick one color space over another, and every setting produces high-quality image data fit for further color correction. Pick whichever color space hands you the most agreeable launch point for your specific project.

Blackmagic Design: For digital cinema work shot on Blackmagic Design cameras, this supplies a wide gamut color space. Rec. 709: Its decode lands in whatever standard color space the Rec. 709 standard sets out for high definition video. As a launch point you may find it handy, though programs bound for video don’t require it. Rec. 2020: Its decode lands in whatever standard color space gets set out, for UHD video, high definition video, and more, by the Rec. 2020 standard. As a launch point you may find it handy, though programs bound for video don’t require it. DCI-P3 D65: Its decode handles RGB-encoded image data carrying a D65 white point, intended for monitoring done on a P3-compatible display. DCI-P3 Theater: This setting suits adaptive viewing of DCI-P3 within a theater whose projector runs a D60 white point. CIE 1931 XYZ D65: For output into an XYZ color space holding a D65 adaptive white point, here’s a specialty setting. CIE 1931 XYZ D50 (PCS): For output into an XYZ color space holding a D50 adaptive white point — the kind the DNG image format’s profile connection space depends on — here’s another specialty setting.

- Gamma: A handful of choices let you pick a gamma profile to apply while debayering .braw media. Which works best really comes down to how you prefer to work, given that every one of them hands back high-quality image data while, inside DaVinci Resolve’s image processing pipeline, the signal goes unclipped. Although some of these choices produce a range of image data that clips on output, every bit of that image data is held “under the hood” and can be used and pulled back in your grade.

Blackmagic Design Film: A log-encoded, “film workflow”-leaning choice crafted specifically for version 4 of the Blackmagic Design color science. The choice is meant to pack as much information as it can from wide latitude BMD cameras into the 0–1023 data range. Picking this setting carries all the source media’s dynamic range into a signal that transcodes to other formats with no compromise. It is not, however, a viewable image and needs grading to normalize it into an image deliverable to audiences.

Blackmagic Design Video: For standard-dynamic-range HD and UHD display, this is the standardized gamma curve. On wide-latitude images, highlights do clip, yet every bit of image data is kept internally so grading can pull it back when needed. Blackmagic Design Extended Video: Much like the one above but SDR-compatible, this gamma curve compresses highlights so as to keep more highlight detail inside the image’s visible range. It’s intended as a quick launch point for grading SDR images. Highlights clip less often, yet still every bit of image data is kept internally so grading can pull it back when needed. Blackmagic Design Custom: For specialty workflows. Linear: A scene linear setting, fit for specialty workflows and visual effects. Rec. 2100 Hybrid Log Gamma: Jointly built by the BBC and NHK, this is the standardized gamma curve serving the HLG standard of high‑dynamic-range (HDR) video. Rec. 2100 ST2084 (PQ): The way Dolby Vision and HDR10+ encode it, this is the standardized gamma curve serving high-dynamic-range (HDR) video. The PQ curve is its other name.

- Highlight Recovery: A checkbox letting you fold in extra highlight sensor data that the standard decoding matrix usually clips. Where your peak highlights are heavily clipped, this can recover extra image detail, though it may carry odd color artifacts.
- Gamut compression: Keeps monochromatic, heavily saturated light sources (neon signs, LEDs, and so on) from clipping the gamut.
- Apply LUT: Puts color metadata onto the BRAW file from whichever LUT source you chose.
- LUT source: Pick the color metadata either from the sidecar file or from the metadata

embedded in the clip.

- Saturation: Tunes how intense the image’s color is. Unity sits at 1. Its range runs from 0 (desaturated)

up to +4 (extremely high).

- Contrast: Lifts contrast by raising the top of the signal and dropping the bottom of the signal

about the Midpoint slider (covered below). Push this value up to add contrast, drop it to reduce contrast. Unity sits at 1. Its range runs from 0 (minimum contrast) to +2 (maximum contrast).

- Midpoint: The level around which contrast gets stretched or squeezed. Unity sits at 0.41. Its range runs from 0 (black) to +1 (maximum white).
- Highlight Rolloff: Lets you reach back into blown-out highlight detail within high-dynamicrange media by lowering this parameter, blending the recovered highlights smoothly into the untouched midtones for a natural-looking outcome. Unity sits at 1. Its range runs from 0 (minimum) up to +2 (maximum).
- Shadow Rolloff: Lets you brighten or deepen shadow detail at will. Pushing this value up recovers shadow detail captured beneath 0 percent while sparing the midtones. Unity sits at 1. Its range runs from 0 (minimum) up to +2 (very high).
- White Level: A gain setting that tunes the highlights.
- Black Level: A lift setting that tunes the shadows.
- Use Video Black Level: A legacy video setting that pushes pedestal into the video signal. For folks running video gear from back when shoulder pads were in fashion.

### Use Camera Metadata

These are the most basic camera metadata settings on offer for exposure and color. Clear the Use Camera Metadata checkboxes to switch the controls on.

- Exposure: Raises or drops image lightness in units tied to ƒ-stops. Should your planned exposure change lift image data past the maximum white level, there’s nothing to fear; all image data stays intact and can be pulled back in later adjustments. Unity sits at 0. Its range runs from –5 to +5.
- Color Temp: Available only once White Balance is set to anything besides As Shot. Built to change how “warm” the image looks. It’s adjustable in Kelvin. Lower numbers compensate for “warmer” lighting, while higher numbers compensate for “cool” lighting. Unity sits at +5500. Its range runs from +2000 to +50,000.
- Tint: Available only once White Balance is set to anything besides As Shot. Built to shift the green to magenta balance of the image, for footage with fluorescent tinting. Lower numbers add green to offset magenta lighting, while higher numbers add magenta to offset green lighting. Unity sits at 0. Its range runs from –150 to +150.

### BRAW Files and Blackmagic Design Film

Blackmagic Design’s logarithmically encoded Blackmagic Design Film gamma setting — which yields flat-contrast, wide-gamut image data that holds onto image detail with broad latitude for adjustment — is a reworked take on the standard Cineon curve. Those reworkings, however, are meant to play to the strengths of the sensors inside the Blackmagic Design cameras. Just as with Cineon clips — or with the Log-C gamma of the ARRI ALEXA, or with Sony’s own S-Log and S-Log2 formats — clips relying on Blackmagic Design Film will need normalizing, whether through Resolve Color Management (RCM), through a manual color and contrast adjustment, or by putting a LUT on them, using the techniques covered earlier.
