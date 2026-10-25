# Composite modes and transparency effects and composite mode and opacity controls in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing and transforms in the timeline.
[Chapter index](INDEX.md) / [Next section](lighten-and-lighter-color.md)
<a id="source-add"></a> <a id="source-color"></a> <a id="source-color-burn"></a> <a id="source-color-dodge"></a> <a id="source-composite-mode-and-opacity-controls-in-the-timeline"></a> <a id="source-composite-modes-and-transparency-effects"></a> <a id="source-compositing-and-transforms-in-the-timeline"></a> <a id="source-compositing-and-transforms-in-the-timeline-part-1"></a> <a id="source-darken"></a> <a id="source-darker-color"></a> <a id="source-difference"></a> <a id="source-divide"></a> <a id="source-exclusion"></a> <a id="source-hard-mix"></a> <a id="source-hardlight"></a> <a id="source-hue"></a> <a id="source-more-about-composite-modes"></a> <a id="source-normal"></a>

### Compositing and Transforms in the Timeline

A great many of the compositing and transform effects in DaVinci Resolve live on the Edit page as well. Plenty of these effect types can be brought into DaVinci Resolve, among them composite modes, opacity settings, and clips that carry alpha channels. After they're inside DaVinci Resolve, the Edit page lets you adjust these effects. Or, if you prefer, DaVinci Resolve's own controls let you build effects from the ground up.

### Composite Modes and Transparency Effects

Composite modes are effects that combine one superimposed clip with another through assorted mathematical operations, leaning on standard image-processing math per color channel, where black pixels hold a value of 0, white pixels hold a value of 1, and the gradations of gray in between map to decimal values (so 0.5, for instance, stands for 50% gray). When composite modes blend a pair of clips on the Timeline, each pairing of pixels across the three color channels gets combined according to that particular composite mode's math. The outcomes can produce transparency effects, lift image exposure, and merge several images in many inventive and useful ways.

Two source clips combined with the Subtract composite mode When you work with composite modes, it's easy to drive portions of the resulting image past the maximum or under the minimum brightness values. That image data isn't clipped, though, even where such regions of the picture look like flat white or black. Out-of-range data produced by a composite mode effect is held onto and can be recovered by later image-processing operations on the Color page. As you import XML project files, DaVinci Resolve brings in whatever composite modes the clips in the original sequence used. Where needed, you can then swap a clip's composite mode for one that suits the grade you're building better. Naturally, you can also apply composite modes to clips that never had them, layering in fresh effects of your own. Every composite mode works together with the Opacity slider (sitting below the Composite Mode pop-up menu in the Inspector) to render a clip more or less transparent on top of whatever compositing is already happening. Composite modes can be applied to clips superimposed over other clips on the Timeline. They're available, however, within a grade on the Color page too, by way of the Layer Mixer node, where you can blend differently graded versions of an image in inventive ways. The Add and Overlay composite modes, for instance, can be handy for crafting glow effects, while Subtract and Difference can yield more surreal results.

Handling composite modes over on the Edit page is straightforward. To assign or swap a clip's composite mode: Pick a clip on the Timeline, open the Video Inspector, then choose an option out of the Composite Mode pop-up menu.

### Composite mode and Opacity controls in the Timeline

To turn a clip's composite mode off: Pick a clip on the Timeline, open the Inspector, then choose Normal out of the Composite Mode pop-up menu.

### More About Composite Modes

Ten composite modes are on offer. For clarity, plain image math is used here to explain the available Composite Mode effects.

### Normal

No image compositing happens. The whole frame is filled by either the Timeline's topmost image or, in the Layer Mixer node, its bottom input.

### Add

Each pairing of pixels across both superimposed layers is summed. Layer order doesn't matter. The result can be a striking brightening of light areas across both images, with picture regions blown out to maximum white; to build hot glow effects, this is often done by summing the brighter part of an image onto itself. Image data climbing above 1.0 is retained and can be recovered by later color correction operations. Conversely, black areas in either image leave the combined image untouched (0 + n = n).

### Color

Rebuilds two layers from HSL image components: the bottom layer's Luma is joined to the top layer's Hue and Saturation.

### Color Burn

The bottom layer is inverted, then divided by the top layer, and that result is itself inverted.

### Color Dodge

The bottom layer's pixels are divided by the top layer, which has been inverted.

### Darken

Each pairing of pixels in every color channel is compared, and the darker of the two becomes the output. Layer order doesn't matter. Darken serves you well when you want the darker features of both layers to win out, though for any particular pixel the output might come out as a color found in neither source layer at that pixel.

### Darker Color

For each pairing of pixels, all three color channels from the bottom layer are summed, and all three color channels from the top layer are summed. Those results are compared, and the darker pixel of the two layers becomes the output. Layer order doesn't matter. Darker Color serves you well when you want the darker features of both layers to win out. Unlike the Darken composite mode, the result is always a specific color drawn from either the bottom or top layer.

### Difference

The absolute value of the top layer minus the bottom layer is taken and returned as the result, always a positive number. Layer order doesn't matter. People often reach for this Blend mode to set two differently processed versions of a single image side by side, checking for any alterations and judging how big they are.

### Divide

Takes the bottom layer and divides it by the top layer. A color over itself yields = 1.0, that is white, whereas a color over white (1.0) yields = itself.

### Exclusion

Much like the Difference composite mode, but it yields lower contrast.

### Hard Mix

The bottom layer's R, G, and B channel values get summed with those same R, G, and B channel values from the top layer. Layer order doesn't matter. Can yield extreme effects.

### Hardlight

Hardlight is Overlay's opposite. Every bottom layer pixel above 50% is Multiplied, while every bottom layer pixel at 50% and below is Screened.

### Hue

Rebuilds two layers from HSL image components: the bottom layer's Luma and Saturation are joined to the top layer's Hue.
