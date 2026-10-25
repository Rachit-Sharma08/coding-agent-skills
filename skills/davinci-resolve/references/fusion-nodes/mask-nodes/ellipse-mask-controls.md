# Ellipse mask controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ellipse mask.
[Chapter index](INDEX.md) / [Previous section](b-spline-mask-and-ellipse-mask.md) / [Next section](mask-paint-mask-paint-node-introduction.md) / [Ellipse Mask Elp](b-spline-mask-and-ellipse-mask.md)
<a id="source-common-controls-2"></a> <a id="source-controls-tab-2"></a> <a id="source-ellipse-mask-controls"></a> <a id="source-inspector-2"></a>

### Inspector

Ellipse mask node creating a colored circle by masking a background node

### Ellipse Mask controls

### Controls Tab

The Controls tab lets you refine how the ellipse looks once it's drawn in the viewer. Show View Controls The Show View Controls checkbox flips the mask's onscreen controls in the viewer on or off. Switch it off and the onscreen controls — center position, polylines, angles, and more — stay hidden even with the node selected. Level The Level control fixes the transparency of the pixels in the mask channel. At 1.0 the mask comes out fully opaque (unless a soft edge applies). Lower values make the mask partly transparent. This matches lowering an effect's blend control. NOTE: Dropping a mask's level drops the values of all pixels the mask covers in the mask channel. For instance, put a Circle mask over a Rectangle mask, and lowering the Circle mask's level lowers the values of all of the mask-channel pixels, even though the Rectangle mask underneath remains opaque.

Filter This control picks the filtering algorithm applied when Soft Edge is added to the mask.

- Box: The fastest approach, with quality reduced. Box works best for tiny amounts of blur.
- Bartlett: Also termed a Pyramid filter, Bartlett gives a solid balance between speed

and quality.

- Multi-box: Selecting this filter surfaces the Num Passes slider, letting you govern the

quality. At 1 and 2 passes, the output equals Box and Bartlett in turn. At 4 passes and up, the output usually matches Gaussian, in less time and with no edge “ringing.”

- Gaussian: Using a genuine Gaussian approximation, the Gaussian filter renders excellent results, though it lags the other filters a little. From time to time it can yield an extremely slight edge “ringing” on floating-point pixels.

Soft Edge Use the Soft Edge slider to blur (feather) the mask with the chosen filter. Higher values make the edge fade well past the mask's boundaries. A value of 0.0 produces a crisp, well‑defined edge. Border Width The Border Width control adjusts how thick the mask's edge is. With the solid checkbox on, the border fattens or thins the mask. When the mask isn't solid, the mask shape renders as an outline, its width set by the Border Width setting. Paint Mode Wiring a mask into the effect mask input displays the Paint mode menu. Paint mode determines how the mask arriving at the effect mask input merges with the mask the node makes.

- Merge: The default for all masks. The new mask merges into the input mask.
- Add: The new mask's values add onto the input mask's values.
- Subtract: Within the overlapping areas, the new mask's values subtract from the input mask's values.
- Minimum: Comparing the input mask's values with the new mask, this returns the lowest

(minimum) value.

- Maximum: Comparing the input mask's values with the new mask, this returns the highest

(maximum) value.

- Average: This averages (half the sum) the new mask alongside the input mask.
- Multiply: This multiplies the input mask's values by the new mask's values.
- Replace: Across every overlap, the new mask fully replaces the input mask. Regions that

read zero (completely black) in the new mask don't touch the input mask.

- Invert: Areas of the input mask covered by the new mask get flipped; white turns

black and the reverse. Gray areas in the new mask flip partway.

- Copy: This mode discards the input mask outright and uses the new mask for every value.
- Ignore: This mode discards the new mask outright and uses the input mask for every value.

Invert Tick this checkbox to flip the whole mask. Unlike the Invert Paint mode, the checkbox affects every pixel, whether or not the new mask covers them. Solid With the Solid checkbox on, the mask fills to transparent (white) unless inverted. With it off, the spline renders only as an outline whose thickness the Border Width slider controls.

Center X and Y These controls set the placement of the Ellipse mask. Width This control hands you independent command of the ellipse mask's Width. Beyond the slider in the mask's controls, you can drag the width (left or right edge) of the mask interactively in the viewer with the pointer. Whatever you change shows up in this control. Height Height hands you independent command of the ellipse mask's height. Beyond the slider in the mask's controls, you can drag the height (top or bottom edge) of the mask interactively in the view with the pointer. Whatever you change shows up in this control. To resize the mask while keeping the aspect ratio, drag the onscreen control between the edges (diagonal). That shifts both the width and height in proportion. Angle Alter the mask's rotational angle by sliding the Angle control left or right. You can also type values into the number fields supplied. Otherwise, work the onscreen controls by dragging the small circle at the tip of the dashed angle line to interactively set the ellipse's rotation.

### Common Controls

Image and Settings Tabs Other mask nodes carry copies of the Inspector's Image and Settings tabs too. The closing “The Common Controls” section of this chapter covers these shared controls in detail.
