# Introduction to the color warper and chroma warp

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color warper.
[Chapter index](INDEX.md) / [Next section](hue-saturation-chroma-luma-mode-and-color-warper-interface.md)
<a id="source-chroma-warp"></a> <a id="source-chroma-warp-stroke"></a> <a id="source-chroma-warp-tools"></a> <a id="source-color-warper"></a> <a id="source-color-warper-part-1"></a> <a id="source-introduction-to-the-color-warper"></a> <a id="source-pin-points"></a> <a id="source-the-chroma-warp-tools"></a> <a id="source-using-the-chroma-warp-in-normal-mode"></a> <a id="source-using-the-chroma-warp-in-point-to-point-mode"></a>

### Color Warper

As a robust toolset, the Color Warper handles everything from pinpoint tweaks to single elements within the frame to broad, sweeping changes that build distinctive looks. Each of the Color Warper's two modes makes it simple to shift hues with the Chroma Warp, or to reshape a pair of color attributes at once, whether that pairing is saturation and hue or lightness and hue. That capability sets the Color Warper apart from curves, which restrict you to altering a lone color characteristic per pass.

### Introduction to the Color Warper

Two distinct modes make up the Color Warper: Chroma Warp, and Hue-Saturation / Chroma-Luma. The aim of either mode is to bend one group of colors into another while keeping a gentle falloff that qualifiers on their own would struggle to deliver. On any given node, though, you have to commit to either the Chroma Warp or the Hue-Saturation / Chroma-Luma controls.

### Chroma Warp

You will find the Chroma Warp as a mode within the Color Warper Palette. It shares its goal with the Color Warper Hue-sat / chroma-luma controls, namely producing smooth, accurate transitions across color ranges. Where it parts ways is the method: the Chroma Warp draws strokes onto a chromaticity diagram instead of nudging mesh points to apply its changes. Either approach yields excellent output, yet only one of the two can run on a single node, so you commit to either the traditional Color Warper or the Chroma Warp.

The Chroma Warp chromaticity diagram on the left, with its toolset over on the right At the heart of the Chroma Warp interface sits a chromaticity diagram, with the spread of the image's present colors laid over it in white (much like a vectorscope rendering) and the toolset off to the left. Because that chromaticity diagram is perceptually uniform, the gaps between its points track closely with the visual differences you perceive in the image while working the Chroma Warp. The Chroma Warp also ignores exposure, so once a Chroma Warp is in place, later shifts in luminance will not undo your qualified selection. Your opening choice is whether to run the Chroma Warp in Normal or Point to Point modes.

### Using The Chroma Warp in Normal Mode

Reach for this mode whenever you want a color to flow organically into another across the whole span of colors sitting between the two, such as deepening an entire sky toward a richer blue. Pick the color range you intend to alter by:

- Picking the starting color with the qualifier eyedropper in the Viewer, and then dragging toward where the replacement color sits on the chromaticity diagram. As you drag across the color ranges, the Viewer refreshes, which lets you settle precisely on the change you are after.
- Clicking the color as it appears within the chromaticity diagram itself, and then dragging in the direction of whatever color you mean to swap it for.

Whichever route you take, a blue dot on the chromaticity diagram marks the color you began with, while an orange dot stands for the destination color. An arrow joins the two to convey the extent of the change. Surrounding the vector, an orange outline traces every color that has been touched. Pull the points in toward the white point (that small circle in the diagram) to drain saturation, or push them out toward the edges to boost a color's saturation.

The Chroma Warp running in Normal mode, simultaneously pushing the grass tones toward more yellow and the sky toward a deeper blue.

### Using The Chroma Warp in Point to Point Mode

Turn to this mode to single out one color and convert it wholesale into a different one, for instance taking a shirt from blue all the way to yellow without passing through green. Identify the particular color you wish to alter by:

- Sampling the source color via the qualifier eyedropper in the Viewer, then dragging in the direction of the replacement color on the chromaticity diagram. The Viewer keeps updating as you drag among the colors, so you can comfortably home in on the precise destination color you have in mind.
- Clicking the color where it shows up inside the chromaticity diagram, then dragging toward whichever color you want it to become.

By either method, the color you started from shows as a blue dot on the chromaticity diagram and the target color as an orange dot, with an arrow linking them to express the extent of the change. Here an orange outline wraps around both dots, marking the selection range of the original color and the final one. Dragging the points in toward the white point (the small circle in the diagram) strips saturation away, whereas dragging them toward the edges raises a color's saturation.

The Chroma Warp running in Point to Point mode, shifting only the shirt's color from blue over to yellow. TIP: Several Normal and Point to Point selections can run together inside one node, opening the door to very sophisticated color changes.

### Pin Points

With this tool you drop a pin that marks a color range to be held out of the selected range. Say you were recoloring a sign from red to green, but its yellow lettering happened to land in the band between those hues; you could place a pin point on the yellow text so it stays out of the color change. A second scenario would be pinning an actor's skin tones, keeping their skin constant no matter how the colors around them shift. Setting a pin point works just like the selection described above: either qualify a color straight off the image in the Viewer, or click the color within the chromaticity diagram.

Dropping a pin point around the white point so neutral tones avoid taking on a tint through a Chroma Warp operation TIP: Should the tool start introducing tinting, try parking a Pin Point on the chromaticity diagram's white point (the center circle), which pulls every neutral gray out of the color adjustment.

### The Chroma Warp tools

### Chroma Warp Tools

The Chroma Warp toolset is your gateway to the Warp's principal color-selection parameters.

- Add Stroke (Normal): Switches the Chroma Warp over to Normal mode for selecting a color range.
- Add Stroke (Point to Point): Switches the Chroma Warp into Point to Point mode for selecting one particular color.
- Add Pin Point: Lets you drop a pin that marks a color to be kept out of the selected range.
- Select: Lets you grab an existing range and drag it about the chromaticity diagram.
- Delete Strokes or Points: Lets you remove particular strokes and points already laid down on the Chroma Warp. Just click one of a range's points, then click the trashcan icon.

### Chroma Warp Stroke

Use the Chroma Warp stroke tools to tweak and sharpen whatever selection you have built.

- Chroma Range: Move this slider to dictate how many neighboring colors fall inside the range. Smaller ranges tighten the color selection, while larger ranges sweep in more of the surrounding colors.
- Exposure: Sliding this control dims or lifts the selection only at the ending circle (the orange dot), with negative values darkening and positive values brightening.
- Tonal Range Low: Sliding this control aims your change mainly at the darker areas of the originally selected color, sparing the lighter areas. The effect is global, reaching every stroke on the chromaticity diagram.
- Tonal Range High: Sliding this control aims your change mainly at the lighter areas of the originally selected color, sparing the darker areas. The effect is global, reaching every stroke on the chromaticity diagram.
- Tonal Range Pivot: This slider fixes the starting split between Tonal Range Low and Tonal Range High from which those tools branch apart.
- Normal/Point to Point Toggle: Clicking either icon flips a Normal selection into a Point to Point one, or the reverse.
