# Delta keyer node introduction delta keyer key tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delta keyer node introduction.
[Chapter index](INDEX.md) / [Previous section](delta-keyer-initial-setup.md) / [Next section](delta-keyer-node-introduction-and-depth-map.md) / [Delta Keyer Node Introduction](chroma-keyer-and-delta-keyer-node-introduction.md)
<a id="source-fringe-tab"></a> <a id="source-key-tab"></a> <a id="source-matte-tab"></a> <a id="source-pre-matte-tab"></a> <a id="source-the-delta-keyer-fringe-tab"></a> <a id="source-the-delta-keyer-key-tab"></a> <a id="source-the-delta-keyer-matte-tab"></a> <a id="source-the-delta-keyer-pre-matte-tab"></a> <a id="source-the-delta-keyer-tuning-tab"></a> <a id="source-tuning-tab"></a>

### The Delta Keyer Key tab

### Key Tab

Keying typically kicks off on the Key tab, whose job is picking out the screen color. Background Color This refers to the hue of the blue or green screen, occasionally known as the screen color. With the Delta Keyer, build the key by grabbing the screen color out of the image using the background color Eyedropper. Pre-Blur Lays down a blur ahead of alpha generation. That can ease certain noise, edge enhancements, and artifacts present in the source image. Gain Boosting Gain strengthens the screen color's pull, pushing those regions toward greater transparency. Balance A color difference keyer such as the Delta Keyer weighs the gap between the leading channel (set by the chosen background color) against the remaining pair of channels. Tweaking balance sets how those other two channels are proportioned. At 0 it takes the minimum of the other two, at 1 the maximum, and at 0.5 an even split of each.

Lock Alpha/Spill Removal Color Balance Reference Unlock this and you can feed different color references into alpha generation versus how much background color gets pulled out of the image. Left enabled, spill and color are treated as one. Color Balance Reference These Color balance reference controls compensate for lighting or white balance that may be sapping the background color's purity and saturation. Drawing on the reference of a neutral-colored object, a correction kicks in while the key is built and the amount of background color subtraction is gauged, all without changing the background color that gets subtracted.

### The Delta Keyer Pre Matte tab

### Pre Matte Tab

You can think of the Pre Matte tab as a garbage matte keyer running ahead of the delta keyer stage. Its role is smoothing out the screen color before the finer key happens. Having picked the first screen color, jump to the Pre Matte tab and choose PreMatte Out from the view mode menu atop the Inspector. Because Pre Matte deals in color ranges, begin by dragging a bounding box over regions whose lighting differs from that first screen color pick. Widen the selection with Soft range and trim its edges with Erode. With a more uniform screen selection in hand, head to the Matte tab. Soft Range Soft Range broadens both the span of selected color and the screen color's rolloff. Erode Erode pulls in the pre matte's edge so the edge detail avoids clipping.

Blur This eases the pre matte's edges. Pre Matte Range These readouts refresh on their own to mirror whatever color is currently selected. They nudge the selection a little, though all you really need to do is pick colors in the viewer. Lock Color Picking Turning on this checkbox stops the chosen range from creeping wider when you grab additional colors from the view. Switching it on once you've settled on the matte color is wise. Every other control on the node stays editable. Reset Pre Matte Ranges Pressing this clears the entire color selection by resetting the ranges, yet leaves all the remaining slider and control values intact.

### The Delta Keyer Matte tab

### Matte Tab

The Matte tab polishes the key's alpha, folding in whatever solid and garbage masks are wired into the node. As you work here, flip the viewer over to the Delta Keyer's final-output alpha channel. Threshold This range slider fixes the lower threshold with the left handle and the upper threshold with the right handle. Anything sitting under the lower threshold turns black or transparent in the matte. Anything above the upper threshold turns white or opaque. Values caught between the two keep their relative transparency. Restore Fringe This rebuilds the matte's edge around the keyed subject. Keying frequently clips the subject's edge wherever hair appears, and Restore Fringe recovers that edge while the matte stays solid.

Erode/Dilate Grows or shrinks the matte. Blur Eases the matte. Clean Foreground Fills the matte's faintly transparent (light gray) zones. Clean Background Clips off the matte's lower dark range. Replace Mode Sets how matte tweaks put color back into the image.

- None: Color stays put. Matte processing leaves the color alone.
- Source: The hue taken from the original image.
- Hard Color: One flat color.
- Soft Color: A flat color scaled by how much background color got stripped out initially.

Replace Color The hue applied by the Hard Color and Soft Color replace modes.

### The Delta Keyer Fringe tab

### Fringe Tab

Within the Delta Keyer, the Fringe tab takes care of most spill suppression. Spill suppression is a kind of color correction aimed at pulling the screen color off the matte's fringe. Spill itself is the screen color bleeding through the alpha channel's semitransparent regions. With blue- or green-screen keying, that typically leaves the background hue showing along the foreground subject's edges.

Spill Method This picks how aggressive the algorithm is when it applies spill suppression to the image.

- None: Pick None whenever no spill suppression is called for.
- Rare: Strips out hardly any spill color, the gentlest option of the bunch.
- Medium: Suits green screens best.
- Well Done: Suits blue screens best.
- Burnt: Suits blue screens best. Reserve this mode for the most stubborn shots only.

Spill Suppression Hold this slider at 0 and the image gets no spill suppression at all. Raising it dials up how strongly the spill method acts. Fringe Gamma Reach for this control to brighten or darken the fringe or halo ringing the keyed image. Fringe Size This grows or shrinks how big the fringe or halo around the keyed image is. Fringe Shape Fringe Shape shoves the fringe out toward the image's outer edge or draws it inward toward the fringe's inner edge. You'll notice it most when the Fringe Size value runs large. Cyan/Red, Magenta/Green, and Yellow/Blue These three controls let you color-correct the image's fringe. They come in handy for nudging semitransparent pixels that still hold the old background's color so they match the new background.

### The Delta Keyer Tuning tab

### Tuning Tab

An advanced panel, the Tuning tab lets you set how large the shadow, midtone, and highlight ranges are. Reshaping those ranges lets you tie the strength of the matte and spill suppression to tonal values.

Range Controls These range controls spell out how much color counts as belonging to the image's shadows, midtones, and highlights. The spline controls make it simple to reshape the tonal span of each Shadow and Highlight tonal map. Simple/Smooth Press Simple and the range turns linear. Press Smooth and the ranges take on a gentle tonal gradient. Lock Alpha/Spill Removal Tuning Turn this checkbox off and distinct tuning controls govern alpha generation versus how much background color gets subtracted from the image.

- Shadows: Tunes the key's strength across the background's darker regions.
- Midtones: Tunes the key's strength across the background's midtone regions.
- Highlights: Tunes the key's strength across the background's brighter regions.
