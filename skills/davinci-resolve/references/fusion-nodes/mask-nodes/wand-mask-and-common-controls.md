# Wand mask and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Wand mask, Common controls.
[Chapter index](INDEX.md) / [Previous section](triangle-mask-and-wand-mask.md) / [Next section](common-controls-image-tab.md) / [Continue The Common Controls / Image Tab](common-controls-image-tab.md) / [Wand Mask Wnd](triangle-mask-and-wand-mask.md)
<a id="source-controls-tab-2"></a> <a id="source-inspector-2"></a> <a id="source-the-common-controls"></a> <a id="source-wand-mask-controls"></a>

### Inspector

### Wand Mask controls

### Controls Tab

The Controls tab serves to fine-tune how the mask looks once the Wand has made a selection in the viewer.

Show View Controls The Show View Controls checkbox switches the display of the mask’s onscreen controls in the viewer on or off. With this checkbox off, onscreen controls — center position, polylines, angles, and the rest — stay hidden, even while the node is selected. Level The Level control fixes the transparency level of the pixels within the mask channel. At a value of 1.0, the mask is fully opaque (barring a soft edge). Lower values leave the mask partly transparent. The outcome matches turning down an effect’s Blend control. NOTE: Dropping a mask’s level pulls down the values of every pixel the mask covers within the mask channel. As an example, when a Circle mask sits over a Rectangle mask, lowering the Circle mask’s level pulls down the values of all the pixels in the mask channel, even while the Rectangle mask underneath stays opaque. Filter This control picks the filtering algorithm put to work when Soft Edge is applied to the mask.

- Box: This one is fastest, though quality is reduced. Box works best for small amounts of blur.
- Bartlett: Otherwise termed a Pyramid filter, Bartlett offers a decent balance between speed and quality.
- Multi-box: Picking this filter surfaces the Num Passes slider and hands you control of the quality. At 1 and 2 passes, the results equal Box and Bartlett, respectively. From 4 passes on up, the results are usually as fine as Gaussian, quicker and with no edge “ringing.”
- Gaussian: Built on a true Gaussian approximation, the Gaussian filter returns excellent results, yet runs a little slower than the rest. In certain cases it may yield an extremely slight edge “ringing” on floating-point pixels.

Soft Edge Reach for the Soft Edge slider to blur (feather) the mask through the chosen filter. Raising the value makes the edge fade off well past the mask’s boundaries. A value of 0.0 makes a sharp, crisply-defined edge. Paint Mode Wiring a mask into the effect mask input reveals the Paint mode menu. The Paint mode decides how the mask coming into the effect mask input and the mask the node builds get combined.

- Merge: Merge is the default across all masks. The new mask blends into the input mask.
- Add: The new mask’s values pile onto the input mask’s values.
- Subtract: Across the overlapping areas, the new mask values come off the input mask’s values.
- Minimum: Weighing the input mask’s values against the new mask, this shows the lowest

(minimum) value.

- Maximum: Weighing the input mask’s values against the new mask, this shows the highest

(maximum) value.

- Average: Works out the mean (half the total) across the new mask together with the input mask.
- Multiply: Takes the input mask’s values and multiplies them by those of the new mask.
- Replace: Wherever the two overlap, the new mask stands in fully for the input mask. Anywhere the new mask holds zero (completely black), the input mask is left as it was.
- Invert: Wherever the new mask covers the input mask, those areas flip; white turns into black and back the other way. Gray stretches of the new mask come through partly inverted.
- Copy: This mode throws out the input mask altogether and draws every value from the new mask.
- Ignore: This mode throws out the new mask altogether and draws every value from the input mask.

Invert Ticking this checkbox flips the whole mask. Unlike the Invert Paint mode, this checkbox reaches every pixel, no matter whether the new mask covers it. Selection Point A pair of X and Y coordinates, the Selection Point pins down where within the source image the Wand mask draws its opening color sample. In the viewers this control also appears as a crosshair. You can set the selection point by hand, or wire it to a tracker, a path, or other expressions. Color Space The Color Space button group fixes which color space is used while choosing the mask’s source color. Among the spaces the Wand mask can run in are RGB, YUV, HLS, and LAB. Channel Through the Channel button group you decide whether the masked color comes from all three of the image’s color channels, from the alpha channel, or from a single channel alone. Exactly what the buttons are labeled hinges on the color space chosen for the Wand mask operation. Where the color space is RGB, the choices are R, G, or B. Where YUV is the color space, the choices are Y, U, or V. Range The Range slider governs the spread of colors around the source color taken into the mask. Left at 0.0, only pixels sharing the source’s exact color count as part of the mask. The higher you set it, the more nearby colors in the source are taken as wholly part of the mask. Range Soft Edge The Range Soft Edge fixes the falloff range of the colors picked. Any pixel inside the range set above counts as 100% within the mask. With the soft range at 0.0, no further pixels are weighed for the mask. Raising the soft range pulls in more colors that sit close to, yet not quite inside, the range covered by the mask. Those pixels turn out semitransparent in the mask

### The Common Controls

Several identical controls in the Inspector are shared among nodes that build masks. The controls common to mask nodes are described in this section.
