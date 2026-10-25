# Face refinement skin texture

Version: DaVinci Resolve 20.3 Reference Manual. Context: Face refinement studio version only.
[Chapter index](INDEX.md) / [Previous section](face-refinement-detection.md) / [Next section](face-refinement-side-lighting.md) / [Face Refinement (Studio Version Only)](depth-map-and-face-refinement.md)
<a id="source-beauty-automatic-controls"></a> <a id="source-skin-grading"></a> <a id="source-skin-texture"></a> <a id="source-smoothing-controls"></a>

### Skin Texture

Three operating modes sit under the Skin Texture controls, letting you pick the approach you'd like for governing skin texture. Beauty Automatic and Beauty Advanced supply the texture controls from the Beauty plugin, whereas Smoothing supplies the texture adjustment controls that were available previously.

### Beauty Automatic Controls

Automatic mode surfaces simple controls for smoothing detail or making it coarser.

- Amount: Lets you set how much smoothing or coarsening gets applied.
- Scale: Lets you dial down or up the amount of smoothing or coarsening that's achieved

across the span of the Amount slider.

### Smoothing Controls

- Smoothing: This slider strips detail from the regions singled out by the Skin Mask controls, smoothing the complexion. How it behaves hinges on where the Detail Size and Detail sliders beneath it are set. You may find that Smoothing can go much further as you push Detail up via the Detail Size and Detail sliders covered below.
- Detail Size and Detail: After working the Smoothing slider, these sliders let you selectively reintroduce subtle skin details into the image; Detail Size sets the largest detail size you want returned to the face, and Detail is a sharpening operation that controls how visible these small details become. Pairing smoothing with a gentle preservation of small details yields a far more lifelike result than leaving the whole face unnaturally smooth.

(Left) The original image, (Right) Only smoothing complexion,

Applying Detail Size and Detail to restore lifelike texture across the smoothed output (effect overstated for print) Beauty Advanced These controls are the same as the Advanced controls in the Beauty plugin, addressed earlier in this chapter.

### Skin Grading

With these controls you can make color tweaks to the whole face.

- Contrast: This slider lets you brighten the face naturally by holding the shadows dark even as you lift the face, which makes it simple to lift actors clear of the background.
- Midtone: Lets you give the skin tone a more luminous quality.
- Color boost: Targets saturation specifically in the least-saturated portions of the face.
- Tint: Offers a narrow band of natural hues leaning on orange through red (yet reaching

to green and magenta) for adjusting complexion.

- Desaturate shadow: This slider lets you selectively pull saturation out of the darkest facial shadows

to keep things looking natural, or to strip saturation harder to stylize the face another way. It also helps when the plugin's other adjustments leave the shadows too colorful. Pushing this slider into negative values instead adds saturation.

- Shine Removal: This slider acts as an inverse contrast adjustment meant to tone down sweat and shine on someone's face, though pushing this slider into negative values will instead emphasize shine.
