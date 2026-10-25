# Sony raw use camera metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sony raw.
[Chapter index](INDEX.md) / [Previous section](red-and-sony-raw.md) / [Sony RAW](red-and-sony-raw.md)
<a id="source-sony-media-and-slog"></a> <a id="source-use-camera-metadata"></a>

### Use Camera Metadata

The most basic camera metadata controls on offer for exposure and color.

- Exposure: Raises or drops image lightness, measured in units tied to ASA values. Should your exposure change push image data past the highest white level, there’s no cause for concern — every bit of image data is kept and can be recovered in later passes. +800 is unity. The range is +1 to +65,535.
- Color Temp: Meant to shift the “warmth” of the image and tunable in degrees Kelvin. Lower figures compensate for “warmer” lighting, while higher figures compensate for “cool” lighting. +6500 is unity. The range is +2000 to +50,000.
- Tint: Surfaces only once White Balance is set to anything besides As Shot. Its job is to shift the image’s green-to-magenta balance, handy for shots with fluorescent tinting. Lower figures introduce green to offset magenta lighting, while higher figures introduce magenta to offset green lighting. 0 is unity. The range is –150 to +150.

### Sony Media and SLog

Sony’s in-house SLog gamma setting — which yields flat-contrast, wide-gamut image data that holds onto detail and leaves you plenty of room to adjust — turns up on a number of other Sony cameras too. Much as you would with clips shot in the ARRI ALEXA’s Log-C gamma, SLog clips have to be normalized: either through Resolve Color Management (RCM), through a hands-on tweak of color and contrast, or by laying on a LUT, all using the methods covered earlier. Sony puts forward two approaches when a LUT is involved. Should your end goal be Log media destined for film printing, a 1D LUT can convert SLog clips into the standard Cineon (or Log-C) curve. And if instead you intend to deliver a normalized format, a purpose-built LUT will carry out that conversion. To dig deeper, look online for Sony’s paper “SLog: A new LUT for digital production mastering and interchange applications.”
