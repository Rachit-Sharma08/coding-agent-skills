# You can warp color in different color spaces and color space found underneath the grid controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color warper.
[Chapter index](INDEX.md) / [Previous section](hue-saturation-chroma-luma-mode-and-color-warper-interface.md) / [Next section](modifiers-and-range.md)
<a id="source-color-warper-part-2"></a> <a id="source-hue--saturation-controls"></a> <a id="source-the-color-space-found-underneath-the-grid-controls"></a> <a id="source-tools"></a> <a id="source-you-can-warp-color-in-different-color-spaces"></a>

### You Can Warp Color in Different Color Spaces

Down in the lower-right corner of the warping grid, a drop-down menu picks which color space governs how you work the image's colors. Each color space maps the image's colors onto the two-dimensional warping grid in its own way, and a given one might make a particular image easier to handle as you intend by fanning certain color ranges out more broadly.

### The color space found underneath the grid controls

The available color spaces are:

- HSV
- HSL
- HSY
- HSP

### Hue – Saturation Controls

True to its name, the Hue-Saturation mode lets you shift hue and saturation together. For most people it is probably the most instinctive mode to operate in, since the image's spread of hues and saturation is laid out radially, exactly as on the Vectorscope; indeed a Vectorscope graph of the image sits beneath the “wheel” grid of control points you use to push color around. By default, dragging any point on this grid affects the colors right around that point, the ones falling between the point you are moving and the radial grid's neighboring “spokes” that are either beyond that point's reach or locked down. In truth, you can drag these radial control points far past the line of the grid's adjacent spokes to warp those colors into completely different hues.

The control point you are adjusting leaves the points on neighboring columns alone, those columns running from the outer ring in to this control's center, even after you drag the point clear past them. Reshaping color through control points feels much like sliding color around a color wheel. Carrying a control point radially along the grid's circumference alters the hue of the colors that point represents. Bring a control point nearer the center and those colors lose saturation, while pulling one toward the grid's edge gains saturation for them. The sections ahead lay out how the various tools in this mode operate to let you work these radial control points in differing ways.

### Tools

Every one of the tools on offer gives you a different way to work the warping grid's control points once you click it.

- Selection Tool: The mode the tool defaults to. Once active, you can target control points one at a time (clicking a lone point, or command-clicking to add several), or grab a whole batch by dragging a marquee around them; right-clicking a point lets you deselect, unlock, or reset it. Holding Shift while you click locks a point in position without nudging it. It's the handiest mode for sampling a color and tweaking it on the spot by dragging directly inside the Viewer.
- Draw Selection: With this active, you gather control points by holding the mouse down and tracing across every point you wish to include. It suits broad yet deliberate sweeps over groups of points.
- Pin/De-Pin: Activating this lets you fasten several control points at once, whether you click them one by one or drag across the ones you intend to pin or release.
- Pull Points: Once chosen, clicking any spot on the warp grid — including the gaps between points — draws every nearby control point inward toward the click. Use it to soften color contrast across a chosen band of hues.
- Push Points: Once chosen, clicking any location on the warp grid — even the empty space between points — shoves every control point within reach outward, away from the click. Use it to heighten color contrast across a chosen band of hues.
