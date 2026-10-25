# Phantom cine project settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Phantom cine.
[Chapter index](INDEX.md) / [Previous section](phantom-cine-master-settings.md) / [Next section](red-master-red-settings.md) / [Phantom Cine](phantom-cine-master-settings.md)
<a id="source-camera-raw-settings-part-3"></a> <a id="source-project-settings-3"></a>

### Project Settings


The settings below, covering exposure, color, and sharpness, are on offer.

- Gamma: For setting the debayered output's gamma, three options exist:
- Rec. 709
- Log 1
- Log 2
- Lift: Shifts the media's black point up or down, scaling every midtone value that falls between it and the white point. No matter how you set this control, the full image data stays intact and stays retrievable through later adjustments. The range is –100 to +100.
- Gain: Shifts the media's white point up or down, scaling every midtone value that falls between it and the black point. No matter how you set this control, the full image data stays intact and stays retrievable through later adjustments. 0 is unity. The range is –100 to +100.
- Contrast: Pushing contrast up pulls shadows down and lifts highlights, while the midtones at 50 percent go untouched. No matter how you set this control, the full image data stays intact and stays retrievable through later adjustments. 0 is unity. The range is –100 to +100.
- Sharpness: A sharpness filter tied to debayering, laid on to lend the look of heightened image detail. 20 is unity. The range is 0 to 100.
- Highlights: Lets you readily pull back blown-out highlight detail in high-dynamic-range media by easing this parameter down, delivering a seamless blend between the recovered highlights and the untouched midtones for a natural-looking outcome. 0 is unity. The range is –100 (minimum) through +100 (maximum).
- Shadows: Lets you brighten or darken shadow detail selectively. Pushing this value up recovers shadow detail captured below 0 percent, while the midtones stay put. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Color Boost: Lets you lift the saturation of low-saturation regions in a natural-looking way, a move sometimes called a vibrance operation. It can equally pull the saturation of low-saturation regions down. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Saturation: Sets the image's color intensity. 0 is unity. The range is –100 (minimum) through +100 (very high).
- Midtone Detail: Push this parameter up and the contrast across image regions carrying high edge detail rises, heightening the sense of image sharpness, a quality sometimes called definition. Pull this parameter down into negative territory and image regions carrying little detail get softened, while the high-detail areas stay untouched. 0 is unity. The range is –100 (minimum) through +100 (very high).
