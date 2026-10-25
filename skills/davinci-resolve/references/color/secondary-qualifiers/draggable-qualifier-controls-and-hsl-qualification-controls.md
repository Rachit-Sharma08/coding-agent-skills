# Draggable qualifier controls and hsl qualification controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary qualifiers.
[Chapter index](INDEX.md) / [Previous section](hsl-qualification-and-color-picker.md) / [Next section](clean-black-and-before-after-raising-black-clip.md)
<a id="source-3d-qualifier-controls"></a> <a id="source-draggable-qualifier-controls"></a> <a id="source-hsl-qualification-controls"></a> <a id="source-luma-qualification-controls"></a> <a id="source-matte-finesse-controls"></a> <a id="source-pre-filter"></a> <a id="source-rgb-qualification-controls"></a> <a id="source-rgb-qualification-controls-1"></a> <a id="source-the-3d-qualifier-mode"></a> <a id="source-the-hsl-qualifier-controls-in-close-up"></a> <a id="source-the-matte-finesse-controls"></a>

### Draggable qualifier controls

### HSL Qualification Controls

Among the Qualifier palette modes, the HSL Qualifier is the most flexible. It's also the most approachable conceptually and the simplest to tune by hand when you'd rather not sample the picture at all. Picking a range and a softness across the three color components — hue, saturation, and luma — lets you single out all sorts of vivid subjects, or bands of brightness and saturation in the frame.

### The HSL Qualifier controls in close up

A major and frequently overlooked benefit of the HSL Qualifier is that the Hue, Sat, and Lum buttons let you switch each of the three HSL components on or off; these toggles sit to the left of every qualifier range control's label. As a result you can disregard certain color components and concentrate on the ones that matter more. Say you want to grab only the saturated regions of a frame no matter their hue or brightness — switch off the Hue and Lum qualifiers, leaving Sat as the sole component sampling the picture.

Keying on saturation alone to pick out the picture's most saturated area The HSL parameters include:

- Hue Center: Sets the midpoint of the band of Hue that gets isolated.
- Hue Width: Sets how broad the isolated band of hue is. Pushing this parameter wider or tighter expands or contracts the hue range around the present Hue Center.
- Hue Soft: Broadens or tightens the falloff on each side of the active hue range.
- Hue Symmetry: Lets you adjust the Hue Soft falloff angle on just one side, right or left. Reducing it steepens the softness on the right of the hue range; increasing it steepens the softness on the left.
- Sat Low/High: A pair of parameters that set the top and bottom of the saturation band you're isolating.
- Sat Low Soft/High Soft: A pair of parameters that set the upper and lower softness tapering away beyond the active saturation band.
- Lum Low/High: A pair of parameters that set the top and bottom of the luma band you're isolating.
- Lum Low Soft/High Soft: A pair of parameters that set the upper and lower softness tapering away

outside the current range of luma.

### RGB Qualification Controls

With the RGB Qualifier mode you isolate range and softness within an image's Red, Green, and Blue channels. Building a qualification by hand this way isn't always intuitive, yet it offers an alternate route to picking out ranges of the RGB color space that might otherwise be awkward. Begin by sampling the picture, after which you can stretch or shrink each channel's isolated value range. There are times when dialing in these controls is the quicker route to isolating a particular run of continuous color.

### RGB qualification controls

The RGB parameters include:

- Red Low/High: A pair of parameters that set the top and bottom of the isolated Red channel band.
- Red Low Soft/High Soft: A pair of parameters that set the upper and lower softness tapering away beyond the active red band.
- Blue Low/High: A pair of parameters that set the top and bottom of the isolated Blue channel band.
- Blue Low Soft/High Soft: A pair of parameters that set the upper and lower softness tapering away beyond the active blue band.
- Green Low/High: A pair of parameters that set the top and bottom of the isolated Green channel band.
- Green Low Soft/High Soft: A pair of parameters that set the upper and lower softness tapering away beyond the active green band.

### Luma Qualification Controls

The Luma Qualifier mode just extracts a key from the Luma channel on its own. It amounts to the HSL qualifier with H and S switched off. This one-component keyer is handier than it appears; isolating a band of highlights, midtones, or shadows across the frame to shift color temperature selectively is a frequent move.

The Luma Keyer mode automatically disables the Hue and Saturation controls Bear in mind too that luma is the crispest keyable component when your footage is heavily compressed. Keys that come out grainy or blocky under HSL qualification can end up cleaner if you rely on the Luma Qualifier alone, though you'll give up chromatic precision in exchange. Four parameters drive the Luma Qualifier: Lum Low/High: A pair of parameters that set the top and bottom of the isolated luma component band. Lum Low Soft/High Soft: A pair of parameters that set the upper and lower softness tapering away outside the current range of luma.

### 3D Qualifier Controls

As covered earlier in the chapter, within DaVinci Resolve the 3D Qualifier behaves quite unlike the other qualifiers. Here you draw strokes across the regions you want to isolate, which feeds samples into the Sample list — some adding to the key (dragging with the pointer) and some removing from it (Option-dragging with the pointer). The workflow is dead simple, but additional controls are on hand as well.

### The 3D Qualifier mode

The 3D Stroke Pickers: Picker: Selects the starting color to qualify. Drawing longer strokes generally yields a stronger key. Picker -: Takes a color region back out of the qualifier; you can also reach this by holding the Option key. Picker +: Adds another color region on top of the first qualifier. Invert: Flips the present key, so qualified zones become unqualified and the reverse. Show Paths: A checkbox toggling whether the sampling strokes you draw stay visible. Hiding the strokes has no bearing on the key whatsoever. Auto-B/W Highlight: Switch this checkbox on and the viewer flips into Highlight B/W mode as you draw a stroke, giving you a clearer live look at the key being made. Releasing the button returns the viewer to whatever mode it was in. Colorspace: A drop-down for picking whether your color sampling happens in YUV colorspace, or in HSL, HSP, or LAB colorspaces. The default is YUV, but when results disappoint you can clear the Qualifier palette and try the others to find what works best. Strokes list: Every stroke you draw shows up here as a sampled row. The color patch on the left shows the mean color you sampled; click it to momentarily disable a color sample and judge how much it adds to the whole key. A plus or minus badge tells you whether the patch contributes to or removes from the key. Next come the mean red, green, and blue values, and a trash can icon on the right deletes any sample from the list. The 3D Qualifier Modes: Soft: Gives the key a gentler edge that tolerates Chroma and Luma tweaks more readily. The softer falloff suits cases such as a face lit by gradual changes in light. Pair this mode with the Shadow / Midtone / Highlight Matte Finesse Controls to dial in the outcome. Flat: The default mode. Every picked color keys at 100%, with allowances made for minor color shifts. It's the prime mode for chroma keying a green or blue screen. On top of that, raising the Pre-Filter value in the Matte Finesse controls can yield a smoother, flatter key. Tight: Keys only the precise color you picked and adds no softening across color ranges. The exact color you selected is the only color affected. Expect single-pixel-level sharpness. It's handy for tough keying tasks where you adjust filter and softness by hand in the Matte Finesse Controls. Luma: Acts like the Tight setting but throws out all chroma information. Use this mode for black and white footage. Despill: When you're pulling a blue or green screen key with the 3D qualifier to make transparency, this slider applies an automatic correction that strips blue or green spill from the picture while preserving its original color.

The 3D Qualifier Chroma and Luma Adjustments, with the Strokes List colors on display. The Color Space box and the Brightness Range make up the bulk of the Chroma and Luma adjustment area. The Color Space box is arranged much like the Color Wheels, primaries ringing its perimeter. Which Color Space you pick in the 3D Qualifier dictates the precise colors and arrangement. Underneath the Color Space sits the Brightness Range as a bar that runs from black on the left to white on the right. The specific colors you grabbed with the pickers in the Strokes List sit inside the Color Space and Brightness Range. The instruments ringing the box shift the colors within it in assorted ways so you can preview how the key reacts. The 3D Qualifier Chroma & Luma Adjustments: Chroma Tolerance: Drag left or right to widen or shrink the span of colors the key captures. Chroma Softness: Drag left or right to alter how responsive the key is to nearby colors. This sets whether the key cuts off hard or eases across similar colors. Adaptive Chroma Softness: Switching on this icon lets the keyer behave evenly across both heavily saturated and washed-out parts of the picture together. You'll want it left on most of the time. The exception is If you can't get manual chroma softness right in Soft or Flat mode, then switching Adaptive Chroma Softness off hands you a wider working range. Adaptive Chroma Softness is automatically disabled in Tight and Luma modes, since it runs counter to how those modes work. X: Shifts your chosen color region inside the color space, altering its chroma by its horizontal placement. Y: Shifts your chosen color region inside the color space, altering its chroma by its vertical placement. Angle: Shifts your chosen color region inside the color space, altering its chroma by how far it rotates around the center origin.

Low: Grows or shrinks the key's dark zones within the brightness range. High: Grows or shrinks the key's bright zones within the brightness range. Low Soft: Governs how sharply defined the low side of the brightness range is. This sets whether the key cuts off hard or eases across similar brightness levels. High Soft: Governs how sharply defined the high side of the brightness range is. This sets whether the key cuts off hard or eases across similar brightness levels.

### Matte Finesse Controls

Once the sample controls and qualifier parameters have given you the best key you can manage, it may still carry flaws that the regular adjustments can't easily address. Trouble like jittery edges, gaps, or grainy patches is often quickly remedied with the Matte Finesse controls. Acting on the matte itself, these controls process the output of the Qualifier controls, so depending on your goal they may serve well in some cases and poorly in others.

### The Matte Finesse controls

### Pre-FIlter

This slider tries to tidy up the picture ahead of color sampling. It can help when your footage carries MPEG blocking artifacts.
