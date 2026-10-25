# Modifiers and range

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color warper.
[Chapter index](INDEX.md) / [Previous section](color-warper-color-space-selection.md) / [Next section](tools-buttons-and-modifiers.md)
<a id="source-auto-lock-controls"></a> <a id="source-axis-angle"></a> <a id="source-chroma-luma-controls"></a> <a id="source-modifiers"></a> <a id="source-range"></a> <a id="source-smoothing-controls"></a> <a id="source-the-original-image"></a> <a id="source-tools"></a>

### Modifiers

Every one of the Modifier buttons reshapes your selections and the chosen control points across the warping grid in its own fashion the instant you press it.

- Increase Falloff/Smooth Selection: With one or several control points already chosen, pressing this grows the selection outward to take in every neighboring point that rings it.
- Decrease Falloff/Smooth Selection: With a cluster of control points chosen, pressing this trims the selection inward by dropping the outermost ring, so only the interior points stay chosen.
- Invert Selection: Pressing this flips every point's state — the unselected become selected and the selected become deselected. Handy when you intend to color-grade each of the two halves of the warping grid on its own.
- Convert Selection to Pin: Pressing this fastens whatever control points are presently chosen.
- Select/Pin Column: With at least one control point chosen, pressing this grows

the selection so it covers every column holding one or more already-chosen points.

- Select/Pin Ring: With at least one control point chosen, pressing this grows

the selection so it spans each ring circling the center that holds one or more chosen points.

- Select/Pin All, Deselect/Pin All: Pressing this flips the entire warping grid between fully selected and fully cleared.
- Reset Selection/Pins: With at least one control point chosen, pressing this returns them to their starting default spot on the warping grid while keeping them chosen.

### Range

The Range control offers a quick way to grab a batch of control points that map to one defined band of colors.

- Range: A gradient displays the spread of hues that the warping grid currently shows. Pulling the left and right handles of the Range selection box automatically picks every control point tied to the hues sitting inside that box. It's a swift route to selecting all the points across a color band so you can shift them together.

### Auto Lock Controls

The Auto Lock controls let DaVinci Resolve automatically fence off a border of control points around whichever point you pick and modify, which makes pinpoint color tweaks far simpler to pull off.

- Auto Lock: Switches this behavior on and off.
- X Points Border: Sets the distance, measured in points away from the one you're modifying, of the

ring of locked control points that walls in your adjustment. The footprint this covers hinges on the number of points you pick and on the warping grid's resolution. Finer grids mean the same point distance fences off a tighter patch of color.

### Smoothing Controls

The smoothing controls let you "ease off" a change you've applied by gradually nudging one or more chosen control points back toward where they started in the warping grid.

- Smooth Chroma: Every press of this rotates the chosen control points' angle around the rim of the circular warping grid back toward their starting spot, drawing the adjusted colors' hue ever nearer the image's original hues. Saturation stays put.
- Reset Chroma: Returns the angle of all chosen control points to those points' original hues. Saturation tweaks remain untouched.
- Smooth Saturation: Every press of this slides a control point's position nearer its starting place relative to the center of the circular warping grid, which pulls the saturation there closer to the node's input image saturation. Hue stays put.
- Reset Saturation: Returns the distance from the center for all chosen control points to those points' original image saturation.
- Reset Luma: Returns luma to the original image values.

### Chroma-Luma Controls

The Chroma-Luma mode lets you reshape the hue and brightness of the image's colors together. It might not strike you as an especially natural way to operate, since the grid controls sit atop colors mapped as the differing faces of an RGB cube. Even so, once you grasp how stacked adjustments play off one another here — plus the leverage of locking control points to confine your work to specific zones of the two grids — some potent moves open up. Whether you sample the image or push the grid's control points by hand, dragging any point on this grid alters the image color that point stands for. Moving up or down shifts brightness, with up brightening that portion of the image and down darkening it. Moving sideways shifts hue, governed by which span of hues the two Chroma-Luma warping controls display and which of them you're working on. Out of the box, only the four outer corners of this control are locked, so any change you apply to a control point pushes and pulls every other color across the image according to your move. Operating this way, repeated changes to many colors steadily pin individual colors down, each change warping the colors lying between to keep a seamless shift from one adjustment to the next. It can be a fine route to applying a broad stylistic look to the image.

### The original image

The outcome of stacking several interacting color changes across the whole Chroma Luma grid Another tack with this mode is to perform more surgical corrections by hand-locking the colors in the image you'd rather leave alone. You manage this with the Selection tool, Shift-clicking any value inside the Viewer, or Shift-clicking any control point on the grid control. Pinning down the colors you don't wish to alter frees you to work a narrower band of colors without disturbing the whole image. As an alternative, this is precisely where the Auto Lock controls prove their worth. Switching them on lets you pick the kind of zone you want to touch (a vertical column, a horizontal row, or a square patch), then decide how wide a color zone to work (one or two points out from the chosen point). Bear in mind that the warping grid's present resolution likewise shapes how wide the resulting color zone turns out. Coarser grids let you handle broader color zones, whereas finer grids let you fine-tune a tighter color band.

The Auto Lock controls let you apply pinpoint changes to particular slices of the warping grid. With these turned on, a single click on the image or warping grid picks a control point and automatically walls off the grid zone you mean to concentrate your change on. In the example below, a medium-resolution grid is paired with the Auto Lock controls set to wall off a 2-point rectangular zone. So clicking the skin of the woman's face and dragging shifts a slice of the available reds inside the walled-off grid zone.

Applying a precise color tweak inside a walled-off section of the Chroma Luma grid The sections that follow lay out how each of the tools on offer in this mode operates to let you push these radial control points around in different fashions.

### Axis Angle

In Chroma-Luma mode, one extra control surfaces beneath the warping grids — a slider called Axis Angle. Sliding it left or right shifts the span of hues each of the two warping grids puts on display, which lets you work over differing color bands.

### Tools

Every available tool lets you push the warping grid's control points around in its own way whenever you click it.
