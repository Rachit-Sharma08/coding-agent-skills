# Tools buttons and modifiers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color warper.
[Chapter index](INDEX.md) / [Previous section](modifiers-and-range.md)
<a id="source-auto-lock-controls-1"></a> <a id="source-modifiers-1"></a> <a id="source-range-1"></a> <a id="source-smoothing-controls-1"></a> <a id="source-the-auto-lock-controls"></a> <a id="source-the-modifier-buttons"></a> <a id="source-the-range-control"></a> <a id="source-the-smoothing-controls"></a> <a id="source-the-tools-buttons"></a>

### The Tools buttons

- Grid 1/Grid 2 tabs: Because the Chroma-Luma controls present two grids covering two separate spans of hue and luma, these tabs let you choose which grid reacts whenever the image gets sampled inside the Viewer, plus which grid the Tools controls govern.
- Selection Tool: The mode the tool defaults to. Once active, you can target control points one at a time (clicking a lone point or command-clicking several) or grab a batch by dragging a marquee around them. Holding Shift while you click locks points in place without nudging them, and right-clicking a point lets you de-select, unlock, and reset it. It's the handiest mode for sampling a color and tweaking it on the spot by dragging directly inside the Viewer.
- Draw Selection: With this active, you gather control points by holding the mouse down and tracing over every point you wish to include. It suits broad yet deliberate sweeps over groups of points.
- Pin/De-Pin: Activating this lets you fasten several control points at once, whether you click them one by one or drag across the ones you intend to pin or release.
- Pull Points: Once chosen, clicking any spot on the warp grid — including the gaps between points — draws every nearby control point inward toward the click. Use it to soften color contrast across a chosen band of hues.
- Push Points: Once chosen, clicking any location on the warp grid — even the empty space between points — shoves every control point within reach outward, away from the click. Use it to heighten color contrast across a chosen band of hues.

### Modifiers

Every one of the Modifier buttons reshapes your selections and the chosen control points across the warping grid in its own fashion the instant you press it.

### The Modifier buttons

- Increase Falloff/Smooth Selection: With one or several control points already chosen, pressing this grows the selection outward to take in every neighboring point that rings it.
- Decrease Falloff/Smooth Selection: With a cluster of control points chosen, pressing this trims the selection inward by dropping the outermost ring, so only the interior points stay chosen.
- Invert Selection: Pressing this flips every point's state — the unselected become selected and the selected become deselected. Handy when you intend to color-grade each of the two halves of the warping grid on its own.
- Convert Selection to Pin: Pressing this fastens whatever control points are presently chosen.
- Select/Pin Column: With at least one control point chosen, pressing this grows

the selection so it covers every column holding one or more already-chosen points.

- Select/Pin Row: With at least one control point chosen, pressing this grows the

selection so it spans every row holding one or more already-chosen points.

- Select/Pin All, Deselect/Pin All: Pressing this flips the selected state of the whole

warping grid on or off.

- Reset Selection/Pins: With at least one control point chosen, pressing this returns

them to their starting default spot on the warping grid while keeping them chosen.

### Range

The Range control offers a quick way to grab a batch of control points that map to one defined band of colors.

### The Range control

- Range: A gradient displays the spread of hues that the warping grid currently shows. Pulling the left and right handles of the Range selection box, or dragging inside the range control to fix both edges, automatically picks every control point tied to the hues sitting inside that box. After you've fixed a range, you can shift it left or right by dragging the middle of the selection. It's a swift route to selecting all the control points across a color band so you can shift them together.

### Auto Lock Controls

The Auto Lock controls let DaVinci Resolve automatically fence off a border of control points around whichever point you pick and modify, which makes pinpoint color tweaks far simpler to pull off. They come in especially handy on the Chroma-Luma warping grid.

### The Auto Lock controls

- Auto Lock: Switches this behavior on and off.
- X Points Border: Sets the distance, measured in points away from the one you're modifying, of the

ring of locked control points that walls in your adjustment. The footprint this covers hinges on the number of points you pick and on the warping grid's resolution. Finer grids mean the same point distance fences off a tighter patch of color.

- Lock Column: Lets you confine your change to every control point inside one column of the rectangular Chroma-Luma graph. That column's width follows from the border width controls. Handy when you mainly want to shift the brightness of a color band while nudging the hues a touch.
- Lock Row: Lets you confine your change to every control point inside one row of the rectangular Chroma-Luma graph. That row's height follows from the border width controls above. Handy when you mainly want to shift the hue of a color band while nudging the brightness a touch.
- Lock Region: Lets you confine your change to every control point inside a rectangular zone around the chosen point. Handy when you want to work a focused patch of color matching a clear-cut feature of the image, such as a particular-colored hat, shirt, foliage, or skin tone. Tighter zones yield more precise changes than wider ones.

### Smoothing Controls

If you reckon you've pushed a change a little too far and need to dial it back somewhat, the Smooth controls let you do that step by step, or begin afresh if you must.

### The Smoothing controls

- Smooth Chroma: Every press of this glides chosen control points left or right, back toward where they began, drawing the adjusted colors' hue ever nearer the image's original hues. Luma stays put.
- Reset Chroma: Returns the position of all chosen control points to those points' original hues. Luma tweaks remain untouched.
- Smooth Luma: Every press of this glides chosen control points up or down, back toward where they began, drawing the adjusted colors' luma ever nearer the image's original luma. Chroma stays put.
- Reset Luma: Returns the position of all chosen control points to those points' original luma. Chroma tweaks remain untouched.
