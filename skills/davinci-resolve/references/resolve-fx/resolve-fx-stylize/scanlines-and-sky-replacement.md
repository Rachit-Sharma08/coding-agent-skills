# Scanlines and sky replacement

Version: DaVinci Resolve 20.3 Reference Manual. Context: Scanlines, Sky replacement.
[Chapter index](INDEX.md) / [Previous section](mirror-pencil-sketch-prism-blur-and-scanline-effects.md) / [Scanlines](mirror-pencil-sketch-prism-blur-and-scanline-effects.md) / [Next section](sky-replacement-artificial-sky.md)
<a id="source-appearance"></a> <a id="source-color"></a> <a id="source-composite"></a> <a id="source-resolve-fx-stylize-part-2"></a> <a id="source-selecting-the-replacement-sky"></a> <a id="source-selecting-the-sky-to-be-replaced"></a> <a id="source-sky-mask-adjustments"></a> <a id="source-sky-replacement"></a> <a id="source-source-sky-appearance"></a>

### Appearance

Let you tailor the kind of scanline effect you are after.

- Line Frequency: Sets how many or how few lines overlay the image; with fewer lines, they automatically widen as they spread evenly across the image.
- Line Sharpness: Blurs the boundary between each line, softening the effect.
- Line Angle: Rotates the lines to any angle; the default of 0 gives

horizontal lines.

- Line Width: Widens or narrows the blanking lines that hide the image

(black by default but tinted by the Color 2 parameter), thereby letting more or less image show through.

- Line Shift: Offsets the lines laid over the image. Animating Line Shift produces a rolling scanlines effect.

### Color

Lets you tint and shift the channels of the alternating scanlines this filter makes. Taken to extremes, it can spawn many other stylistic effects.

- Color 1 and Color 2: Color picker and eyedropper controls for tinting each alternating set of lines (the eyedroppers sample a color from the RGB image fed into the current node).
- Red, Green, and Blue Offset: Offsets the individual channels.
- Scanlines Only: Lets you view the scanlines on their own as you adjust them.

### Composite

Lets you decide how the scanlines effect composites against the original image.

- Scanlines Only: Outputs an image made up solely of the scanline pattern you built. Good for producing assorted patterned textures and mattes.
- Composite Type: Lets you pick which composite mode blends the scanline effect into the image.

### Sky Replacement

Swapping a dull, washed-out sky for a livelier one, or matching skies captured on separate days, are routine colorist jobs that the Sky Replacement effect makes more efficient. Choosing Sky Replacement over conventional compositing methods gives you a tight, purpose-built toolset that lets you:

- Match the foreground dynamically to the sky's brightness and color cast.
- Use Tracking options so the sky travels along with the clip's camera movement.
- Add believable computer generated sky elements, such as sky color, horizon haze, clouds,

and light sources.

(Left) The bland sky as shot, (Right) The same image carrying a fresh, better looking sky.

### Selecting the Sky to be Replaced

Worth noting is that the Sky Replacement effect performs no sky selection on its own; instead it accepts that selection from other tools and concentrates on blending it seamlessly into either a background plate of a different sky or its own artificial sky generator. Keeping the sky selection apart from the replacement tools is a deliberate choice, since qualifying a sky is usually easy while landing a clean mask at the horizon is not. That arrangement lets the colorist reach for the right qualifier (HSL, Window, Magic Mask, etc.) for a given scene and then hand it off to the Sky Replacement effect. A further upside is that the Sky Replacement effect can live on the same node as your qualifier, so you select and replace the sky within a single node and update both tools together as you go. To pick the sky to be replaced and feed it to the Sky Replacement FX: 1 Within a color node, reach for any Qualifier (Power Window, HSL, 3D, Magic Mask, etc.) and key the sky and horizon cleanly. 2 Next, drag the Sky Replacement effect out of the Effects Library and drop it on that same node. 3 Or build a new color node, run the alpha output of the earlier node (blue square) into the new node's alpha input (blue triangle), and drag the Sky replacement effect from the Effects Library onto the new node.

### Selecting the Replacement Sky

With your original sky qualified, you face two choices for what replaces it: an artificially generated sky (built in the Sky Replacement Parameters below), or fresh footage of a previously shot sky serving as a background plate. To wire a sky background plate into the Sky Replacement FX: 1 Inside a color node, qualify the sky, then add the Sky Replacement FX. 2 Right-click the node carrying the Sky Replacement FX and choose Add OFX Input from the drop‑down menu. An extra color and alpha input show up on the node. 3 Drag the sky background plate clip out of the Media Pool into the Node tree, creating a new external matte from that clip. 4 Off the external matte, hang a serial node to form a new color node, letting you reposition and grade the sky background plate as needed. 5 Wire the new color node's color output (green square) into the Sky Replacement color input (the lower green triangle on the node). The background plate's video now drives the sky replacement.

The node tree illustrating the way to bring your own sky background plate footage into the Sky Replacement effect.

### Sky Mask Adjustments

These options let you make final tweaks to the source mask coming from whichever qualifier you used.

- Preview Mask: Tick this box to view the mask as a black and white matte; white marks where the new sky shows through.
- Shift Edge: Moves the mask boundary toward or away from the horizon.
- Refine: Fits the mask boundary to the image edges.
- Black Level: Sets the mask's transparency level.
- White Level: Sets the mask's opacity level.

### Source Sky Appearance

These tools tailor the look of the new incoming sky. They do nothing to the artificial sky and act only on a video clip used as a sky background plate.

- Color Space: Tunes the color space of the sky coming in. Falls back to timeline settings by default.
- Gamma: Tunes the gamma of the sky coming in. Falls back to timeline settings by default.
- Detail: Tunes the midtone detail of the sky coming in.
- Brightness: Tunes the brightness of the sky coming in.
- Saturation: Tunes the saturation of the sky coming in.
- Temperature: Tunes the color temperature of the sky coming in.
- Tint: Tunes the tint of the sky coming in.
- Opacity: Tunes the opacity of the sky coming in, for when you'd like to mix it with the sky drawn from the

original footage.

The identical car shot, now with more dramatic storm footage standing in as the replacement sky and tuned through the Source Sky Appearance tools.
