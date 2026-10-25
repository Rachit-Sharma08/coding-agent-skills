# Ranges mask Fusion controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ranges mask Fusion.
[Chapter index](INDEX.md) / [Previous section](polygon-mask-and-ranges-mask-fusion.md) / [Ranges Mask RNG FUSION](polygon-mask-and-ranges-mask-fusion.md) / [Next section](ranges-mask-fusion-and-rectangle-mask.md)
<a id="source-controls-tab-1"></a> <a id="source-inspector-2"></a> <a id="source-mask-nodes-part-3"></a> <a id="source-rangers-mask-controls"></a>

### Inspector

### Rangers Mask controls

### Controls Tab

The Controls tab serves to refine how the image wired into the orange input becomes the ranges mask. Show View Controls The Show View Controls checkbox switches the display of the mask's onscreen controls in the viewer on or off. With the checkbox off, those onscreen controls, center position, polylines, angles, and the rest, stay out of sight even while the node is selected.

Level The Level control fixes the transparency level of the mask channel's pixels. When the value reads 1.0, the mask is fully opaque (save for a soft edge). Lower values leave the mask partly transparent, the same outcome as turning down an effect's blend control. NOTE: Lowering a mask's level lowers the values of all pixels the mask covers in the mask channel. As an example, with a Circle mask placed above a Rectangle mask, lowering the Circle mask's level lowers the values of all the pixels in the mask channel, although the Rectangle mask beneath remains opaque. Filter This control chooses which filtering algorithm is used as Soft Edge is applied to the mask.

- Box: This method is the fastest, at the cost of quality. Box fits best where only a little blur is needed.
- Bartlett: Sometimes called a Pyramid filter, Bartlett balances speed against quality well.
- Multi-box: Selecting this filter surfaces the Num Passes slider for governing the quality. With 1 and 2 passes the output matches Box and Bartlett in turn, and at 4 passes or above it generally equals Gaussian, in less time and with no edge "ringing."
- Gaussian: Resting on a true Gaussian approximation, the Gaussian filter gives excellent results yet runs slightly slower than the rest. From time to time it can leave an extremely faint edge "ringing" on floating-point pixels.

Soft Edge Drag the Soft Edge slider to feather (blur) the mask via the chosen filter. The higher the value, the farther the edge fades beyond the mask's boundaries. A value of 0.0 yields a crisp, welldefined edge. Paint Mode Wiring a mask into the effect mask input surfaces the Paint mode menu. The Paint mode decides how the mask reaching the effect mask input and the mask formed in the node are merged.

- Merge: Merge is the default for all masks. The new mask blends into the input mask.
- Add: The new mask's values are combined onto the input mask's values.
- Subtract: Throughout the overlapping areas, the new mask values are subtracted from the input mask's values.
- Minimum: Placing the input mask's values next to the new mask, this returns the lowest

(minimum) value.

- Maximum: Placing the input mask's values next to the new mask, this returns the highest

(maximum) value.

- Average: Works out the mean (half the total) across the new mask together with the input mask.
- Multiply: Takes the input mask’s values and multiplies them by those of the new mask.
- Replace: Wherever the two overlap, the new mask stands in fully for the input mask. Spots reading

zero (completely black) over in the new mask leave the input mask untouched.

- Invert: Wherever the new mask covers the input mask, those areas flip; white shifts to

black and the reverse. Gray patches in the new mask end up partly inverted.

- Copy: This mode throws out the input mask altogether and draws every value from the new mask.
- Ignore: This mode throws out the new mask altogether and draws every value from the input mask.

Invert Ticking this checkbox flips the whole mask. Unlike the Invert Paint mode, the checkbox reaches every pixel, no matter whether the new mask covers it or not. Center X and Y The position of the ranges mask is adjusted through these controls. Fit Input This menu decides how the image source is dealt with when it doesn’t match the dimensions of the generated mask. As an example, below, a 720 x 576 image source (yellow) goes toward generating a 1920 x 1080 mask (gray). Crop: When the image source is smaller than the generated mask, it lands according to the X/Y controls, screening off only part of the mask. When the image source is larger than the generated mask, it lands according to the X/Y controls and is trimmed at the mask’s borders. Stretch: The image source is pulled in X and Y to fill out the generated mask’s full dimensions. That can introduce visible distortion of the image source. Inside: The image source scales evenly until one of its dimensions (X or Y) meets the inside dimensions of the mask. Depending on how the image source and mask background compare in size, either the width or else the height of the image source may get cropped to suit the corresponding dimension of the mask.

Width: The image source scales evenly until its width (X) meets the mask’s width. Hinging on the relative dimensions of the image source and mask, the Y dimension of the image source might fall short of the mask’s Y dimension, leading either to cropping of the image source in Y or to the image source not spanning the mask’s height fully.

Height: The image source scales evenly until its height (Y) meets the mask’s height. Hinging on the relative dimensions of the image source and mask, the X dimension of the image source might fall short of the mask’s X dimension, leading either to cropping of the image source in X or to the image source not spanning the mask’s width fully.

Outside: The image source scales evenly until one of its dimensions (X or Y) meets the outside dimensions of the mask. Hinging on the relative dimensions of the image source and mask, either the width or the height of the image source may be cropped or fall short of the corresponding dimension of the mask.

Channel The Channel menu sets which Channel of the input image goes toward building the mask. What you can pick from spans the red, green, blue, plus alpha channels; the hue, luminance, or saturation values; or else the input image’s auxiliary coverage channel (where one is supplied). Shadows/Midtones/Highlights These buttons pick which range the node sends out as a mask. White pixels stand for the pixels reckoned to belong to the range, while black pixels lie outside it. Picking Shadows, for instance, would render pixels reckoned as shadows white and pixels that aren’t shadows black. Mid gray pixels sit only partway in the range and miss out on the full force of any color adjustments to that range.

Channel The Channel selection buttons in this tab let you pull a mask from the range of one particular color channel. By default, Fusion turns to the luminance channel as the color ranges are examined. Mini Spline Editor You set the reach of the ranges by working the spline handles. Four spline points exist, each carrying a single Bézier handle. The pair of handles up top mark where the shadow and highlight ranges begin; the pair down below mark where the range ends. Falloff is governed through the Bézier handles. No dedicated control exists for the midtones range, since its span is taken as the gap between the shadow and highlight ranges. Put another way, once the low and high masks are in place, the midtones are all that remains. The X and Y text controls beneath the Mini Spline Editor let you key in exact positions for whichever Bézier point or handle is selected. Presets This drops the splines into two widely-used setups. The Simple button yields a plain linear-weighted selection, whereas the Smooth button leans on a more natural falloff.
