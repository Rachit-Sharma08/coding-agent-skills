# 3D keyer behavior options

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D keyer.
[Chapter index](INDEX.md) / [Next section](3d-keyer-and-alpha-matte-shrink-and-grow-and-hsl-keyer.md)
<a id="source-3d-keyer"></a> <a id="source-behavior-options"></a> <a id="source-key-adjustments"></a> <a id="source-resolve-fx-key"></a> <a id="source-resolve-fx-key-part-1"></a> <a id="source-selection-range-controls"></a> <a id="source-the-3d-keyer-selection-range-controls"></a> <a id="source-usage-options"></a>

### Resolve FX Key

Among DaVinci Resolve’s tools are several Resolve FX devoted to compositing and keying work, each applied straight on the Timeline.

### 3D Keyer

Built on the Color page’s 3D Qualifier, the 3D Keyer Resolve FX gives a quick, straightforward route to pulling a key that isolates a band of color in the picture by dragging your mouse pointer across the parts of the image you wish to key. Every drag across the image that adds to or trims the cloud of values carves into a three-dimensional depiction of all the colors on hand; you can view this in the tool’s Key Map box, and it is the source of the 3D Keyer’s name. TIP: Should your goal be isolating a band of luma values in the picture, the HSL or Luma keyer hands you finer control. The 3D Keyer makes a solid first choice when you’re after a key on a blue screen or green screen background. Through its workflow of dragging the mouse pointer over the screen color you want gone, with live feedback, it delivers precise control. Where the 3D Keyer shines most is the speed at which you can sample regions of the picture to lift out of the final key. That same trait can turn into a drawback, though, where your opening samples fail to yield satisfying results, since, unlike the Delta Keyer on the Fusion page, few avenues exist for tuning the key while it’s being built. On the flip side, for well-lit subjects you’re keying, two or three samples are all it takes. A handful of long strokes tend to do a finer job of consistently grabbing a band of like colors, much like a broad brush. By contrast, five to ten short strokes behave like a fine brush and will grab only a very narrow band of color you’ve marked out.

### Selection Range Controls

The Inspector’s Selection Range buttons let you set up a key by sampling Viewer pixels with the mouse pointer.

### The 3D Keyer Selection Range controls

- Picker: Picks the opening color to qualify. Strokes drawn longer tend to hand you a stronger key. On the Edit page, the Timeline Viewer Overlay has to sit at Open FX.
- Picker -: Lets you pick a further color to drop from the present qualification; also reachable by holding the Option key.
- Picker +: Picks a further color region to fold into the present qualification.
- Invert: Flips the present key; qualified regions turn unqualified and the reverse.
- Stroke: Shows the roster of picked (+) and unpicked (-) colors, alongside each one’s respective

RGB values.

- Delete Stroke: Drops whichever stroke is presently chosen in the Stroke drop-down menu.
- Reset: Clears every stroke and returns the 3D Keyer to its default state.

### Behavior Options

The basic parameters and modes of the 3D Keyer are set through these controls.

- Colorspace: Through this drop-down menu you pick whether your color sampling happens in YUV, HSL, HSP, or LAB colorspaces. YUV stands as the default, but should you find the results unsatisfactory, you can reach for another colorspace off the drop-down menu to see whether it fares better. There are assorted theoretical differences between these, yet the strongest pick always rides on the task.
- Soft: Lends the key a softer edge that proves more forgiving of Chroma and Luma adjustments. That gentler drop-off suits cases such as subtle light shifts across a face. Pair this mode with the Shadow/Midtone/Highlight Matte Finesse controls to fine tune the outcome.
- Flat: The default mode. Every color you pick is 100% keyed, with adjustments handling small color variations. This is the suggested mode for chroma keying a green or blue screen. On top of that, raising the Pre-Filter setting within the Matte Finesse controls can deliver a smoother, flatter key.
- Tight: Keys only the precise color band picked and lays on no softening drawn from color ranges. Single pixel sharpness levels are what you’d expect. This serves for tough keying work, calling for hand-tuning the filter and softness within the Matte Finesse controls.
- Luma: Behaves much like the Tight setting yet disregards all chroma data, letting you key off brightness level rather than color.
- Despill: When you’re leaning on the 3D qualifier to pull a blue or green screen key for transparency, this slider lets you dial in color correction that strips blue or green spill out of the picture while holding onto the image’s original color.

### Usage Options

The user feedback tools the 3D Keyer shows in the Viewer are governed by these settings. On the Edit page, you have to set the Timeline Viewer Overlay to Open FX.

The Key Map, sitting at the upper left, depicting a qualifier that aims to grab the background sand (blue lines) while dropping the pirate’s hats (red lines)

- Show Paths: A checkbox letting you toggle on and off whether the lines you’re drawing to sample the image stay visible. Hiding lines leaves the key untouched.
- Smart Show Paths: Tick this checkbox and the lines show only while they’re being drawn, vanishing once the mouse button is let go.
- Auto-B/W Highlight: Tick this checkbox and the Viewer flips on its own to Highlight B/W mode as a line is drawn, the better to reveal the resulting key live. Let the mouse button go and the Viewer reverts to whatever viewing mode it began in.
- Show Key Map: Tick this box to bring the Key Map into the Viewer. Two parts make up the Key Map: the Color Space box plus the Brightness Range. That Color Space box gets laid out much the way the Color Wheels are, with primary colors arranged around its rim. Which exact colors and layout appear hinges on the Color Space you settle on within the 3D Keyer. The Brightness Range shows as a bar below the Color Space, its left end black and its right end white. Inside the Color Space and Brightness Range sit the individual colors you chose by way of the pickers within the Strokes List.
- Key Map Zoom: Sets the Key Map’s zoom level, letting you reach finer detail when needed.

### Key Adjustments

This batch of tools lets you tune by hand how the key gets built from the sampled colors. What these tools do shows up in the Key Map, when it’s on.

- Chroma Tolerance: Drag left or right to widen or narrow the band of colors the key grabs.
- Chroma Softness: Drag left or right to shift how sensitive the key is to like colors it grabs. This sets whether the key acts as a hard cutoff or a soft pickup of like colors.
- Adaptive Chroma Softness: Ticking this box lets the keyer behave steadily across both heavily saturated and desaturated regions of the picture at once. Most of the time you’ll want this left on. The exception comes when you’re struggling to hand-tune chroma softness in Soft or Flat mode; switching Adaptive Chroma Softness off then hands you more range to work within. Adaptive Chroma Softness shuts off on its own in Tight and Luma modes since it runs counter to how those modes work.
- Chroma Tilt: Shifts your chosen color region around the color space, altering its chroma per its vertical placement.
- Chroma Shift: Shifts your chosen color region around the color space, altering its chroma per its horizontal placement.
- Chroma Rotate: Shifts your chosen color region around the color space, altering its tint and temperature per how it rotates about the central origin point.
- Luma Low: Widens or narrows the key’s dark regions across the brightness range.
- Luma High: Widens or narrows the key’s bright regions across the brightness range.
- Low Softness: Sets how sharply defined the brightness range’s low end is. This sets

whether the key acts as a hard cutoff or a soft pickup of like brightness levels.

- High Softness: Sets how sharply defined the brightness range’s high end is. This sets

whether the key acts as a hard cutoff or a soft pickup of like brightness levels. TIP: Each of the parameters above can be key-framed, letting you animate the key across time. As an instance, you might have qualified a shirt while the actor passes through differently colored light within a scene. By key framing those same parameters, you can keep the very same key on that shirt as its colors change over time.
