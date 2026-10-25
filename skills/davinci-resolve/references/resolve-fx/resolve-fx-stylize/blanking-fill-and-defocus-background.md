# Blanking fill and defocus background

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blanking fill, Defocus background.
[Chapter index](INDEX.md) / [Previous section](abstraction-and-blanking-fill.md) / [Next section](drop-shadow-and-edge-detect-and-emboss-and-mirrors.md) / [Blanking Fill](abstraction-and-blanking-fill.md)
<a id="source-adjust-mask"></a> <a id="source-advanced-options"></a> <a id="source-defocus-background"></a> <a id="source-drop-shadow"></a> <a id="source-effects"></a> <a id="source-fill-appearance"></a>

### Fill Appearance

These controls reshape how the image used to fill the blanking area looks.

- Blend Edges: Feathers the seam where the original image meets the blanking fill area.
- Blur Background: Sets how strongly or faintly the image filling the

blanking fill area is blurred.

- Fade Amount: Fades or tints the blanking fill area. At 0, no fade applies. At 1.000,

the blanking area becomes a solid color set by the Fade Color control.

- Fade Color: A combined color picker and eyedropper for choosing a color to

fade, tint, or fill the blanking fill area with.

### Drop Shadow

These controls add a drop shadow that "lifts" the foreground image off the blanking fill image.

- Shadow Strength: Sets how solid the drop shadow looks.
- Drop Angle: Sets the angle at which the drop shadow appears. At 0 the

drop shadow is centered.

- Drop Distance: Pushes the drop shadow out farther along the Drop Angle direction
- Blur: Softens the drop shadow.
- Color: Tints the drop shadow.

### Defocus Background

The Defocus Background effect blurs only an image's background and gives you a thorough toolset for imitating a shot taken with a shallow depth of field.

(Left) The starting image, its background busy and distracting. (Right) The Defocus Background effect blurring that background to calm the distraction and imitate a shallower depth of field On its own, the Defocus Background effect neither qualifies nor isolates the foreground subject. Before you can use Defocus Background, the foreground subject has to be isolated first with an effect or mask from another tool such as Magic Mask or a Power Window. Defocus Background can then go on the same node, or you can feed in the key output from an earlier node.

Wiring the Magic Mask's key output into the Defocus Background effect; for Defocus Background to function, it needs a key produced by another tool such as Magic Mask or a Power Window.

### Adjust Mask

These controls tune the mask that splits the sharply focused areas from the ones you want blurred.

- Mask Preview: Ticking this box brings up a black and white preview of your mask. The mask's white areas stay sharp, while its black areas are the ones blurred by the mask controls below. It is handy to keep visible as you refine the mask, then switch off to view the output of the Effects and Advanced options.
- Mask Invert: Ticking this box flips the mask, turning white areas black and the reverse.
- Mask Blur: This control sizes the Blur around the mask, letting you blend

the foreground and background together smoothly.

- Mask Contrast: This sets how hard the boundary is between the focused and blurred

regions of the matte.

- Adjust Pivot: This lets you place where the boundary falls between the focused and blurred regions

of the matte.

The Mask Preview option reveals where the defocus operations occur (the black areas).

### Effects

These controls establish the chief traits of the blurred area.

- Blur: This slider sets the size and degree of blur applied to the blurred area.
- Saturation: This slider sets how saturated the blurred area is. At 1.000 (default) saturation is full, while 0.000 renders the blurred areas monochrome.
- Colorize: This slider sets how much color tints the blurred areas. 0.000 is the default (no colorization).
- Color: This is the color picker for the Colorize operation above.

### Advanced Options

These controls let you tweak a few of the physical traits of the blurred area.

- Blur Type: This picks the blurring algorithm behind the blur. The options are Lens blur or Gaussian blur.
- Anamorphism (Lens Blur): This slider sets the blur's aspect ratio so it matches various lens types.
- Highlights (Lens Blur): Lets you set how the image's highlights act on the blur, dilating or eroding the image.
