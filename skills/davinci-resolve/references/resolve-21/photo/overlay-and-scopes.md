# Overlay and scopes

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Previous section](capture-and-scopes.md) / [Next section](looks-and-adjustments.md)
<a id="source-histogram"></a> <a id="source-inspector"></a> <a id="source-overlay"></a> <a id="source-raw"></a> <a id="source-scopes-1"></a> <a id="source-source-cropping"></a> <a id="source-source-transform"></a>

### Overlay

With this toolset you can lay an existing image over the Capture Live View. It is a help when composing for model placement, aspect ratio, or simply lining up with an earlier shot.

- Overlay Image: Hit the Browse button and select whichever image you want laid over the Capture Live View window.
- Zoom X/Y: Scale the overlay image larger or smaller as required to fit the shot in the Capture Live View window.
- Center Position X/Y: Shift the overlay image up or down as required to fit the shot in the Capture Live View window.
- Opacity: Adjust this slider to change the transparency of the overlay image.
- Flip: Click these icons to flip the overlay image horizontally or vertically.

### Inspector

Opening the Inspector lets you tweak RAW and Photo parameters for photos, adjust any Effects you have applied, and supply File metadata. Ways to bring parameters up in the Inspector:

- If the Inspector is already open: Simply choosing a clip or an effect brings its controls into view within the Inspector.
- If the Inspector is closed: Click on the Inspector tab.

NOTE: Across the top, the Inspector turns on different tabs that move you between separate pages of parameters. As an example, selecting a RAW photo activates the RAW tab. Choosing an ordinary post-debayered photo such as a .jpg switches the RAW section off. The effects tab likewise stays off by default until you apply an effect to a photo.

### Scopes

The Photo Page opens on the Histogram Scope, though any of the other scopes in DaVinci Resolve are available to you. For more about which scopes are available and the way each works, turn to Chapter 127, “Viewers, Monitoring, and Video Scopes,” located in the DaVinci Resolve Reference Manual.

### Histogram

- RGB/YRGB: Lets you switch between viewing only the RGB histograms or the RGB histograms together with the luminance (Y) channel.
- Gain: Drag the slider to boost or cut the histogram signal. This touches only the histogram, leaving the image untouched.
- Graticule: Drag the slider to lighten or darken the histogram scale.
- Show Reference Levels: Tick this box to place user-adjustable level lines onto the histogram.
- Low: Lets you set the brightness level of the low level line.
- High: Lets you set the brightness level of the high level line.
- Reset View: Resets the histogram to the default values.

### RAW

These controls let you work on the image through its pre-debayered RAW data settings. RAW editing stays nondestructive and is generally calibrated to your specific camera, which makes it the favored route for adjusting exposure and color. When your file is not a RAW format, this tab appears grayed out.

- Decode Quality: Debayers your RAW files at one of three resolutions — Full, Half, or Quarter — easing the burden on slower machines. Lower-resolution media looks worse but is quicker to handle and process. If needed, drop to a lower resolution that keeps real time playback smooth on limited hardware while you work, then move up to higher quality for the final render. Picking Project Settings ties the decode quality of every photo to the project settings.
- White Balance: The first choice keeps the white balance recorded in camera as shot. The remaining choices supply White Balance presets that set the Temperature and Tint parameters for you. They cover Daylight, Cloudy, Shade, Tungsten, Fluorescent, and Flash.
- Color Space: Lets you pick which color space the photo is edited and delivered in. With RAW settings it is usually wise to pick a color space from your camera’s maker, or one of the common video standards.
- Gamma: Lets you pick the gamma curve applied to the image — either one from your camera’s maker or a gamma matching a common video standard.
- Temperature: Tunes the white balance color temperature, meant to shift the “warmth” of the image. It is adjustable in degrees Kelvin. Lower readings compensate for “warmer” lighting, while higher readings compensate for “cool” lighting.
- Tint: Meant to shift the green-to-magenta balance of the image for shots with fluorescent tinting. Lower readings add green to offset magenta lighting, while higher readings add magenta to offset green lighting.
- Exposure: Raises or lowers the image’s brightness in units tied to ƒ-stops. Should your exposure change push image data past the maximum white level, no need to worry; every bit of image data survives and can be recovered in later adjustments. 0 is unity. The range is –5 to +5.
- Sharpness: A sharpness filter tied to the debayer that lends the image a look of greater detail. 10 is unity. The range is 0 to 100.
- Highlights: Makes it simple to win back blown-out highlight detail in high-dynamic-range media by lowering this control, blending the recovered highlights smoothly into the untouched midtones for a natural look. 0 is unity. The range is –100 (minimum) through +100 (maximum).
- Shadows: Lets you selectively brighten or darken shadow detail. Raising this value recovers shadow detail captured below 0 percent while leaving the midtones untouched. 0 is unity. The range is -100 (minimum) through +100 (very high).
- Color Boost: Lets you naturalistically lift saturation in areas that are low in saturation, an effect sometimes called vibrance. It can equally be used to drop saturation in such regions. Here unity sits at 0 while the available span runs from –100 (minimum) up to +100 (very high).
- Saturation: Tunes the color intensity of the image. Here unity sits at 0 while the available span runs from –100 (minimum) up to +100 (very high).
- Midtone Detail: Raising this control lifts the contrast in image regions rich in edge detail to heighten the sense of sharpness, an effect sometimes called definition. Pushing it to a negative value softens regions that hold little detail while leaving high-detail areas alone. Here unity sits at 0 while the available span runs from –100 (minimum) up to +100 (very high).
- Lift: Tunes the black point of the media, raising or lowering it while scaling every midtone value between it and the white point. However you set this control, all image data is preserved and can be recovered in later adjustments. The range is –100 to +100.
- Gain: Tunes the white point of the media, raising or lowering it while scaling every midtone value between it and the black point. However you set this control, all image data is preserved and can be recovered in later adjustments. 0 is unity. The range is –100 to +100.
- Contrast: Raising contrast deepens shadows and lifts highlights while keeping midtones at 50 percent unchanged. However you set this control, all image data is preserved and can be recovered in later adjustments. 0 is unity. The range is –100 to +100.

These controls let you tune the transform, cropping, color, and exposure of your image.

### Source Transform

- Zoom X/Y: Lets you enlarge the image or scale it down. The X and Y parameters can be locked together to hold the image’s aspect ratio, or unlocked to stretch or squeeze the image in a single direction.
- Position X/Y: Repositions the image inside the frame, allowing pan and scan moves. X slides the image left or right, while Y slides it up or down.
- Rotation Angle: Rotates the image around the center point.
- Pitch: Tips the image toward or away from the camera about an axis that runs through the

middle of the image, left to right. Positive values send the top away and pull the bottom forward. Negative values pull the top forward and send the bottom away. Larger values stretch the image more severely.

- Yaw: Tips the image toward or away from the camera about an axis that runs through the middle of the image, top to bottom. Positive values pull the left forward and send the right away. Negative values send the left away and pull the right forward. Larger values stretch the image more severely.
- Flip Image: Two buttons let you flip the image in different dimensions.
- Flip Horizontal control: Mirrors the picture across the X axis, swapping its left and right sides.
- Flip Vertical control: Mirrors the picture across the Y axis, flipping it top to bottom.

### Source Cropping

- Ratio: Lets you choose a width-to-height ratio for the image. Pick from the common still photo ratios, or leave it As Shot to keep your camera’s native ratio.
- Lock Aspect Ratio: Tick this box to hold the aspect ratio fixed across any of the cropping functions below. With it locked, cropping the image always moves the other cropping sliders to match the aspect ratio; with it unlocked, cropping changes the ratio.
- Crop Left/Right/Top/Bottom: Trims away each of the image’s four edges, measured in pixels.
