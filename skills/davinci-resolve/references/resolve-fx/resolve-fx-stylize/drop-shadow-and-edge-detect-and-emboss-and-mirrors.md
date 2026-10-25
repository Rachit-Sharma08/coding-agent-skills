# Drop shadow and edge detect and emboss and mirrors

Version: DaVinci Resolve 20.3 Reference Manual. Context: Drop shadow, Edge detect, Emboss, Mirrors.
[Chapter index](INDEX.md) / [Previous section](blanking-fill-and-defocus-background.md) / [Next section](mirror-pencil-sketch-prism-blur-and-scanline-effects.md)
<a id="source-advanced-options-1"></a> <a id="source-channels"></a> <a id="source-detection"></a> <a id="source-drop-shadow-1"></a> <a id="source-edge-detect"></a> <a id="source-emboss"></a> <a id="source-filters"></a> <a id="source-main"></a> <a id="source-mirrors"></a> <a id="source-the-shot-before-the-edge-effect"></a>

### Drop Shadow

Adds a basic drop shadow to any clip, shaping the shadow from that clip's native or generated alpha channel.

- Shadow Strength: Sets how solid the drop shadow looks.
- Drop Angle: Sets the angle at which the drop shadow appears. At 0 the drop

shadow is centered.

- Drop Distance: Pushes the drop shadow out farther along the Drop Angle direction
- Blur: Softens the drop shadow.
- Color: Tints the drop shadow.

### Edge Detect

An edge detection effect that picks out high-contrast boundaries, with options to control which edges become outlines. Once the edges are picked out, you can use this to sharpen soft clips or build a glow around a subject.

(Top) Original image, (Bottom) Image with default edge detect applied

### Main

- Mode: Lets you switch between RGB and Grayscale edges. RGB is the default. RGB locates edges from color and brightness together, whereas Grayscale finds edges from brightness changes alone.
- Edge color: (enabled only when Mode is Grayscale) Lets you colorize the edge outlines produced.

### Detection

These controls govern the strength and parameters of the edges found.

- Edge Width: Sets the thickness of the edges produced.
- Brightness: Sets how bright you want the edges.
- Gamma: Lays a gamma curve over the edge detection. A gamma under one lifts mid-strength edges in brightness, so more edges count as "detected," while a gamma over one darkens mid-strength edges, paring the edges down to all but the strongest found.
- Blur: Softens the final result so the edges blend in more naturally.
- Edge Mask Overlay: This checkbox lays the edges over the current frame so you can watch the filter's results. Clear this box to see only the detected edges.

### Filters

These controls set how the edges merge with the original frame.

- Preprocess: Lets you pick which de-noising filtering method to apply. The default is None. Filter: Cuts texture and strips out detail at the Scale parameter chosen below. Flatten: Smooths the image's even areas, keeping edges only where they part one flat region from another. The Strength parameter below sets how much of this smoothing happens.
- Half-Edges Only: Edges turn up between regions of differing brightness. With this option you choose which half of an edge is retained. By default it is None, so both halves of the edge remain. Keep Light Side: Edge keeps only the brighter half of the edge. Handy, say, for a light-wrap effect on a person's face, since only the lighter (face side) of the edge is kept, holding the added light-wrap brightness to the face alone and off the background. The HalfEdge Gain slider lets you push the edge brightness up further, apart from the main Brightness control. Keep Dark Side: Edge keeps only the darker half of the edge. Handy, say, for a glow effect on a person's face, since only the darker (background side) of the edge is kept, letting a halo form around the face but not over it. The Half-Edge Gain slider lets you push the edge brightness up further, apart from the main Brightness control.

### Advanced Options

These controls give you access to a few advanced parameters for the effect.

- Normalize Per Frame: Brings every incoming frame to a steady brightness level, so edges stay visible as the scene's brightness shifts or flickers. Turn this on when your scene's content keeps changing in brightness; otherwise leave the box clear.
- Clamp Brightness: Stops the output edges from going too bright when the content's contrast runs too high.

Suppose, for instance, you wanted a faint glow around the woman in the frame below using edge detect:

- Choose RGB Edges, tick the Edge Mask Overlay box, and set the Blur near .5 to fold them subtly into the frame.
- Then choose Flatten from the Preprocess control to even out the image's fine detail, so only the highlights off the woman's hat, arm, and phone get detected, along with the bright fluorescent light on the wall. Those are the bits we want to "glow." Set the Strength slider to taste.
- After that, choose "Keep Dark Side" in the Half-Edges Only box. This makes the glow spread outward from the edges rather than onto the woman and the light. Set the Half-Edge Gain slider to taste.

### The shot before the Edge effect

That same image carrying the Edge Detect effect alone, set with the parameters laid out above

The Edge Detect outcome; note how the glow spreads from the light and rings the woman's hat, arm, and phone.

### Emboss

An emboss effect carrying several options for producing different sorts of outline and emboss looks.

- Emboss Style: This pop-up lets you pick from Relief, Emboss Over, Sobel, and Laplacian kinds of embossing.
- Power: Sets how strong the emboss effect is.
- Angle: Sets the apparent angle from which the emboss effect is rendered.

### Channels

Three checkboxes let you opt to use the Red, Green, and Blue channels in building this effect.

### Mirrors

An effect for reflecting a portion of the image in whatever direction you choose. In its plainest form, it makes a split mirror effect like the one at the close of Prince's "When Doves Cry." In its most elaborate form, you can stack multiple reflections to spin up whirling Kaleidoscope patterns in the image.
