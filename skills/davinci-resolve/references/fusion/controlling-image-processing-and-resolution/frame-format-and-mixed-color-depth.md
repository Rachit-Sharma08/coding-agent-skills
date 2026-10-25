# Frame format color depth settings and combining images with different color depths

Version: DaVinci Resolve 20.3 Reference Manual. Context: Controlling image processing and resolution.
[Chapter index](INDEX.md) / [Previous section](clip-resolution-changes-and-mixed-resolution-compositing.md)
<a id="source-accessing-extended-highlights-and-shadows"></a> <a id="source-advantages-of-floating-point-processing"></a> <a id="source-clipping-out-of-range-values"></a> <a id="source-combining-images-with-different-color-depths"></a> <a id="source-detecting-extended-highlight-and-shadow-values"></a> <a id="source-greater-accuracy"></a> <a id="source-the-frame-format-color-depth-settings"></a> <a id="source-using-float-with-8-bit-hd-video"></a>

### The Frame Format Color Depth settings

Unsure which color depth a tool processes at? Rest the pointer on the node's tile in the Node Editor and a tooltip naming that node's color depth shows up on the Status bar.

Hover over a node to read its Color Bit Depth setting. TIP: For images carrying 10-bit or 12-bit dynamic range or more, such as Blackmagic RAW or Cinema DNG files, set the Inspector's Depth menu to either 16-bit float or 32-bit float, which holds onto highlight detail throughout compositing.

### Combining Images with Different Color Depths

Images of differing color depths can live together within one composition. Once such images are merged, the bit depth output is dictated by the image coming from the node's background input, with the foreground image brought into line to match.

### Advantages of Floating-Point Processing

Floating-point processing brings two big upsides that justify its heavier RAM appetite and slower renders. For one, floating-point values carry more accuracy than integer values do. For another, it holds onto shadow and highlight values that reach past the usual tonal range.

### Greater Accuracy

Working in 16- or 32-bit floating point keeps you from the accuracy loss that 8- or 16-bit integer processing can introduce. It comes down to this: integer values have no room for fractional or decimal numbers, so rounding creeps into every image operation. Floating-point processing, by allowing decimal or fractional values per pixel, never has to snap a pixel's values to the nearest integer. The payoff is color precision that stays all but flawless however many operations an image goes through.

Picture an 8-bit pixel whose red value is 75 (dark red); halve it with a Color Correction tool and the pixel's red value becomes 37.5. Because integers can hold no decimal or fractional values, that figure rounds down to 37. Then doubling the pixel's brightness with a second Color Correction tool ought to restore the original 75, but rounding makes 37 x 2 come out to 74. In that very plain example, integer rounding cost the red value a whole point of precision. The trouble is that it can breed visible banding across a run of color corrections, and the same kind of thing crops up when merging or transforming images. The longer the chain of operations applied to an image, the more color precision rounding eats away under 8- or 16-bit integer processing.

### Accessing Extended Highlights and Shadows

A growing share of productions now record out-of-range images, thanks to digital cinema bodies such as the Blackmagic URSA Mini Pro and even the Pocket Cinema 6K camera. Such cameras grab RAW images of very high dynamic range and hold onto color detail even in frames that are badly over- or underexposed. That extended white color detail can also produce lovely, natural-looking results once it's blurred, glowed, color corrected, or simply faded or dissolved. You can certainly handle these RAW images with integer data, but going that way discards the extended-range values, wiping out all detail in the highlights and shadows. Float processing eases work with logarithmic RAW images a great deal by keeping highlight and shadow detail intact. Take an 8-bit pixel with a red value of 200 (bright red) and run a Color Gain tool to double the red channel's brightness: the math gives 200 x 2, or 400. Yet 8-bit color values can only span 0 through 255, so the pixel's value gets clipped to 255, pure red. Halve the brightness now and you land on half of 255, or 127 (rounded), rather than the starting 200. Process colors in floating point, by contrast, and pixel values brighter than white or darker than black survive — nothing is clipped. The viewer still shows the pixel as pure red, but had float processing stood in for 8-bit, that second pass halving the gain would have carried the pixel back to its original 200.

### Using Float with 8-Bit HD Video

Float color depths carry some worth with 8-bit HD video too, whenever the images demand heavy color correction. Choosing float helps hold precision by sidestepping the rounding errors that plague 8-bit processing, as covered above.

### Detecting Extended Highlight and Shadow Values

Even though floating-point processing keeps extended values under 0.0 and over 1.0 — the so-called “out-of-range values” — the viewer goes on showing them as plain black or white. That can leave you hard-pressed to gauge an image's overall dynamic range.

To find out whether a viewed image holds out-of-range values: Right-click within the viewer and pick Options > Normalized Color Range.

Reach for the Normalized Color Range pop-up menu to spot out-of-range images. Switching this display mode on rescales the image's color values so the brightest color maps to 1.0 (white) and the darkest maps to 0.0 (black). The 3D Histogram subview lends another hand in picturing an image's out-of-range colors. For fuller detail, the DaVinci Resolve Reference Manual covers this under Chapter 69, “Using Viewers.”, while the Fusion Reference Manual addresses it in Chapter 7.

### Clipping Out-of-Range Values

Processing in floating point, you may now and then run into cases where an image's out-of-range values have to be clipped. Checkboxes on the Brightness/Contrast tool exist to clip out-of-range values to 0 or 1. Some files, for example, hold out-of-range alpha values. Because the alpha channel stands for a pixel's opacity, going beyond fully transparent or beyond fully opaque makes little sense, and compositing an image like that can yield surprises. To clip alpha values under 0 and over 1 with ease, bring in a Brightness/ Contrast toolset to Clip Black and Clip White while leaving only the Alpha checkbox ticked.

The Clip White and Clip Black settings within Brightness/Contrast serve to clip mattes. As another option, clip the range by dropping in a Change Depth node and moving to 8-bit or 16-bit integer color depths.
