# Custom lum vs sat and hue vs hue sat vs sat

Version: DaVinci Resolve 20.3 Reference Manual. Context: Curves.
[Chapter index](INDEX.md) / [Previous section](additional-controls-in-the-hue-and-sat-curves.md)
<a id="source-custom-lum-vs-sat"></a> <a id="source-hue-vs-hue"></a> <a id="source-hue-vs-hue-sat-vs-sat"></a> <a id="source-hue-vs-lum"></a> <a id="source-hue-vs-lum-1"></a> <a id="source-hue-vs-sat"></a> <a id="source-hue-vs-sat-sat-vs-lum"></a> <a id="source-lum-vs-sat"></a> <a id="source-sat-vs-lum-curve"></a> <a id="source-sat-vs-sat"></a> <a id="source-the-sat-vs-lum-curve"></a>

### Custom Lum vs. Sat

### Hue vs. Hue Sat vs. Sat

### Hue vs. Sat Sat vs. Lum

### Hue vs. Lum

### Hue vs. Hue

With the Hue vs. Hue curve you can convert any hue into a different one. In the example below, the left-hand picture is the untouched original, while the right-hand version shows the orange jacket pushed toward an olive green by way of three control points.

Shifting the hue of the woman's jacket with the Hue vs. Hue curve; Left–original image, Right–altered image A great application of the Hue vs. Hue curve is rapidly and gently nudging elements that only call for slight changes. A sky reading a touch too cyan, for instance, can be deepened into a richer blue using a modest tweak.

The Hue vs. Hue curve also helps when you need bolder changes to elements too noisy for a clean key with the HSL qualifier controls. Red autumn leaves shifting in the breeze, for example, may yield a flickering matte, yet the Hue vs. Hue curve lets you swap reds to greens without aliased matte edges betraying the correction.

### Hue vs. Sat

The Hue vs. Sat curve gives you selective control over the saturation tied to any hue in the picture. It's a wonderful creative instrument: you can swiftly lift the saturation of elements meant to grab attention while pulling down the saturation of things you'd rather the audience overlook. That makes it handy for reining in over-saturated overshoots or undershoots while running a QC pass, such as toning down reds that sit far off the charts while everything else stays untouched.

Reducing the saturation of the woman's jacket with the Hue vs. Sat curve; on the left sits the untouched frame, on the right the modified one. The Hue vs. Sat curve doubles as a strong way to build color contrast in pictures that look dull and flat. Raising the saturation of vivid elements that stand apart from a scene's prevailing palette injects variety into an image that would otherwise feel monochromatic.

### Hue vs. Lum

The Hue vs. Lum curve allows you to brighten or darken elements that carry particular colors.

Darkening the woman's jacket with the Hue vs. Lum curve; Left–original image, Right–altered image It's a delicate curve when paired with heavily compressed footage, since it can swiftly expose artifacts unless you tread carefully. With very high-quality footage, though, it becomes an excellent way to deepen specific hues for added richness and depth, or to brighten colorful elements you want to spotlight.

### Lum vs. Sat

The Lum vs. Sat curve resembles the Custom curves, since here saturation changes key off user-definable ranges of image tonality rather than off hue. In the example that follows, the Lum vs. Sat curve selectively lowers the saturation of everything sitting in the highlights and shadows while lifting saturation across the midtones. Take another example where a richly saturated grade leaves shadows looking unnaturally colorful: the Lum vs. Sat curve makes it simple to ease saturation down below a chosen point with a pleasant, smooth falloff. This curve shines for creative work, say, nudging midtone saturation up a little while cutting shadow saturation to deepen the darkest areas of the picture. It's equally valuable for clearing QC violations. Should illegal saturation appear in an image's highlights, the Lum vs. Sat curve can neatly and smoothly bring down the precise values triggering the trouble.

Targeted shadow-and-highlight desaturation produced with the Lum vs. Sat curve; here the right frame is the source and the left frame is the reworked result.

### Sat vs. Sat

With the Saturation vs. Saturation curve you can selectively work image saturation inside particular regions set by the picture's own original saturation. Points placed toward the left of this curve act on zones of steadily lower saturation, so you can raise or lower the saturation of less-saturated features. Points placed toward the right act on zones of steadily higher saturation, letting you raise or lower a picture's most saturated features.

As with every curve, this is tremendously handy for stylizing the picture. You can build bespoke vibrance moves, selectively raising the saturation of weakly saturated regions in varied ways to lend the image extra "pop." It's likewise a fine tool for handling oversaturated patches when you must meet strict QC rules. You're able to desaturate only the most over-saturated portions of the picture, leaving similar hues at lower saturation untouched. The next example shows the most saturated stretch of the image desaturated while the remainder is left alone.

Pulling saturation only out of the picture's most saturated elements by dropping control points along the right side of the Sat vs. Sat curve

### Sat vs. Lum Curve

As the opposite of the Lum vs. Sat curve, Sat vs. Lum lets you swiftly tweak the luminance of pixels sitting within a specific saturation range. It comes in handy when the regions you'd like to lighten or darken happen to overlap with a recognizably consistent band of saturation. To assist your work, the histogram plotted for this curve reveals how many pixels exist at each saturation level present in the picture, the leftmost edge of the curve standing for minimum saturation and the rightmost for maximum saturation. Knowing where the saturation levels sit in the present image lets you quickly aim luminance changes after you sample the area you wish to adjust to drop points onto this curve.

### The Sat vs. Lum curve

In the next example, the right portion of this curve is dropped so the most saturated areas of the image grow darker. You might apply a change like this to mimic one trait of film, where heavily saturated colors hold back more light from crossing the emulsion than less saturated ones do. Alternatively, you may use it to desaturate bright highlight colors that could otherwise clip beyond maximum white, or simply to rapidly darken intensely saturated skies.

(Top Left) The unprocessed frame, (Top Right) Its intensely saturated blue sky together with the sea's reflections deepen into a stronger blue once the right portion of the Sat vs. Lum curve is brought down (Bottom).
