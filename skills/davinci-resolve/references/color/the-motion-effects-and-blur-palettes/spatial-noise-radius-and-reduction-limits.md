# Spatial nr radius how large should you go and limiting noise reduction in useful ways

Version: DaVinci Resolve 20.3 Reference Manual. Context: The motion effects and blur palettes.
[Chapter index](INDEX.md) / [Previous section](motion-effects-palette-and-noise-reduction-controls.md) / [Next section](mist-and-mist-including-mist-mix-control.md)
<a id="source-blur"></a> <a id="source-controlling-the-order-of-operations-for-noise-reduction"></a> <a id="source-limiting-noise-reduction-in-useful-ways"></a> <a id="source-motion-blur"></a> <a id="source-motion-blur-controls"></a> <a id="source-sharpen"></a> <a id="source-sharpening-with-coring-softness-and-level"></a> <a id="source-spatial-nr-radius-how-large-should-you-go"></a> <a id="source-the-blur-palette"></a> <a id="source-the-motion-effects-and-blur-palettes-part-2"></a>

### Spatial NR Radius, How Large Should You Go?

A bigger NR Radius can do wonders for high-detail regions in shots where your Spatial noise reduction is running hard, yet you don't always have to leap to the large Radius setting, which carries the highest precision. Quite often, while assessing an image under noise reduction, you simply won't perceive the extra quality, and you'll burn processing time on correction you never needed. It pays to judge the full-frame image on a display large enough to reveal the noise within the same viewing context your intended audience will have. Pushing a clip's zoom way in during noise reduction can tempt you toward higher-quality settings than the shot warrants, because a heavily magnified slice of an image surfaces subtle shifts that vanish at actual size.

### Limiting Noise Reduction in Useful Ways

Just like every other Color page correction, noise reduction can be reined in through HSL Qualification or Power Windows. That lets you aim your effort at an image's worst trouble spots — shadows and background areas, say — while leaving alone the parts you'd rather not touch, such as faces or the better-lit stretches of the frame. You can also press Spatial NR into service instead of Blur operations for a gentler kind of complexion smoothing, using the HSL qualifier or a window to single out an actor's skin tone for focused reduction.

### Controlling the Order of Operations for Noise Reduction

A dedicated node lets you drop noise reduction in anywhere along your image processing tree. When an image carries noise that your planned corrections might amplify — bumping the contrast of underexposed clips tends to bring out whatever noise lurks inside — two routes to noise reduction open up:

- Apply noise reduction at the beginning of a node tree: Tackling noise up front clears it before your intended adjustments can turn it into a problem. The picture can come out smoother, though the image's edge detail may read as a touch softer.
- Apply noise reduction at the end of a node tree: The other route is to do your adjustments first and then run noise reduction in a separate node afterward. Here the noise-reduced regions may end up a little less smooth, but the image's edge detail can look noticeably sharper for it.
- Apply noise reduction to only one color channel of an image: With the Splitter/Combiner nodes you can also confine noise reduction to a single color component. Grading a clip whose Blue channel is noisy, for instance, lets you steer reduction exactly where it counts. Singling out one color channel for reduction is likewise doable through the Channels selection

reached by right-clicking a node. Picking the channel numbers in that node that match your color space (RGB, YUV, LAB, etc.) keeps the reduction confined to just those channels. Neither outcome wins outright — which one suits you hinges on the image at hand and the look you're chasing (some shots you might want softer, others sharper). The takeaway is that DaVinci Resolve's node-based image processing puts the choice of technique in your hands. NOTE: When noise reduction and color adjustments share a single node, the noise reduction runs first and the color adjustments follow.

### Motion Blur

Drawing on optical-flow motion estimation, the Motion Blur settings graft synthetic motion blur onto clips that have none. That comes in handy when a program shot at a fast shutter speed turns out, in hindsight, to strobe too much. By reading the motion inside a clip, the Motion Blur settings can blur the image selectively according to how fast and in which direction each moving element in the scene travels.

### Motion Blur controls

A trio of parameters governs how much motion blur lands and at what quality:

- Motion Est. Type: Choosing Better maps pixels more accurately but leans harder on the processor. Faster yields a rougher approximation while going easier on the processor.
- Motion Range: Sets which speed of motion to weigh when marking out the regions that get blurred.
- Motion Blur: Push this parameter up for more motion blur on the image, pull it down for less. Its scale spans 0–100; at 0 there is no motion blur, and 100 gives the most.

### The Blur Palette

Three operating modes make up the Blur palette—blur, sharpen, and mist. Although the Blur and Sharpen modes overlap somewhat in what they do, each one carries its own controls that the others don't. As with nearly everything on the Color page, you can confine the Blur palette's work as a secondary operation via HSL Qualifiers, Windows, or Imported mattes, which makes targeting specific parts of the image straightforward. A good many of the palette's controls are built from three ganged sliders — one red, one green, one blue. Out of the box those ganged sliders shift in unison, so every color channel takes the same hit. A small white button beside each control's name unlinks the sliders, letting you push individual color channels by differing amounts.

### Blur

Blur, the default mode, lets you lay down a remarkably high-quality Gaussian blur — or an equally high-quality sharpening pass — on your image. Of the modes, this one keeps the controls simplest.

Blur Radius controls are ganged by default, but can be unganged Two linked parameter sets adjust how far the blur or sharpening reaches and how directional it is. Which of the two you get hinges on which way you move the Radius control.

- Radius: This sits at the heart of adding blur or sharpening. Left at its default of 0.50, nothing is applied to the image. Nudging the radius slider up grows the blur, while pulling it down grows the sharpness, and the floor of 0.00 delivers the sharpest possible result.

TIP: When the Radius slider is maxed at 1.00 and the image still isn't blurry enough, tack on another node and run a second blur there. Hovering over one of the bars and spinning your mouse scroll wheel will also drive the radius up.

- H/V Ratio: Adds directionality to the operation in play. Held at its default of 0.50, the image is worked equally in the horizontal and vertical directions. Raising H/V Ratio steers the effect more along the horizontal axis, while lowering it steers the effect more along the vertical axis.

### Sharpen

Even though the Blur controls can sharpen too — just lower the Radius sliders instead of raising them — the dedicated Sharpen mode hands you extra controls made specifically for shaping sharpening passes.

### Sharpening with Coring Softness and Level

- Radius: This is the central control for laying on blur or sharpening. Sitting at its default of 0.50 means no effect reaches the image. Pushing the radius slider up raises the blur all the way to a ceiling of 1.00, whereas dropping it raises the sharpness, with the floor of 0.00 yielding the maximum sharpness.
- H/V Ratio: Brings directionality to the operation in play. At its default of 0.50, both the horizontal and vertical directions of the image are worked equally. Raising H/V Ratio biases the effect toward the horizontal axis, while lowering it biases the effect toward the vertical axis.
- Scaling: Boosts how much scaling the Radius control applies during sharpening passes. For blur effects, the scaling parameter does nothing once Radius sits at 0.50 or higher.

Operating in tandem, the Coring Softness and Level parameters confine sharpening to just the picture’s most detailed regions that stand to gain the most from it, working off a threshold of image detail you specify through the Level and Softness parameters.

- Level: This is the slider to reach for first. Pushing its value up sets the point above which image detail is left out of the sharpening operation. Its default of 0 keeps the threshold low enough that the whole image gets sharpened. As you raise Level, low-detail regions of the image drop away one by one, so sharpening ends up confined to clearly defined outlines.
- Coring Softness: Once the Level slider sits at a suitable amount, increasing Coring Softness feathers the boundary separating the image areas that get sharpened from those that stay untouched.
