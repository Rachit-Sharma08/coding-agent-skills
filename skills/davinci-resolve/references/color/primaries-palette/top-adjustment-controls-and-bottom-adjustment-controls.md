# Top adjustment controls and bottom adjustment controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Primaries palette.
[Chapter index](INDEX.md) / [Previous section](primaries-palette-and-hdr-grading.md) / [Next section](log-wheels-for-log-encoded-media.md)
<a id="source-3-way-master-wheel-adjustments"></a> <a id="source-auto-correction"></a> <a id="source-color-bars-mode"></a> <a id="source-color-wheel-palette"></a> <a id="source-color-wheels-and-bars"></a> <a id="source-gain"></a> <a id="source-gamma"></a> <a id="source-lift"></a> <a id="source-offset-color-and-master-controls"></a> <a id="source-primaries-palette-part-2"></a> <a id="source-primary-grading-controls"></a> <a id="source-reset-controls"></a> <a id="source-the-bottom-adjustment-controls"></a> <a id="source-the-top-adjustment-controls"></a> <a id="source-waveform-display-shows-the-clips-contrast-range"></a>

### The top adjustment controls

- Temp: A tightly bounded Gain color balance move letting you shift the image along a warm/orange to cool/blue axis, matching the natural span of lighting color temperatures. Push it up and the Gain color balance leans toward orange; pull it down into negatives and the Gain color balance leans toward a blue/cyan split. Here 0 is unity, and values span –4000 to +4000.
- Tint: A tightly bounded Gain color balance move letting you shift the image along a magenta to green axis, matching the unnatural span of color temperatures from artificial lighting such as fluorescent and sodium vapor fixtures. Push it up and the Gain color balance leans toward magenta (often called “minus green” to fix fluorescent lighting); pull it down into negatives and it leans toward green (“plus green” to fix other lighting). 0 is unity. The range is –100 to +100.
- Contrast: The Contrast parameters let you swiftly tighten or widen image contrast around a user-definable pivot point. Whatever mode you’re in, these parameters behave the same. This single parameter lets you push apart or pull together the darkest and lightest values of an image, raising or lowering its contrast. The result resembles using the Lift and Gain master controls to make opposing moves at once. Bright and dark parts of the image are spread apart or drawn together around a center point that the Pivot parameter sets. Found in the Project Settings’ General Options panel and on by default, the “Use S-curve for contrast” setting tells the contrast control to lay an “S-curve” over the image, keeping a signal’s shadows and highlights from clipping as you raise the value. If you’d rather have these contrast moves made linearly, letting the signal clip once you hit the upper and lower limits of the video signal, you can switch this checkbox off.
- Pivot: Shifts the tonal center around which dark and bright parts of the image are stretched or compressed during a contrast adjustment. Darker images may need a lower Pivot value to keep the shadows from being crushed too hard when stretching contrast, while lighter images may gain from a higher Pivot value to build adequate shadow density.
- Midtone Detail (MD): Raise this parameter and the contrast of image regions carrying high edge detail goes up, heightening the sense of sharpness sometimes called definition. Lower it to a negative value and regions of the image with little detail get softened while the high-detail areas are left untouched. 0 is unity. The range is –100 through +100.

### The bottom adjustment controls

- Color Boost: A non-uniform saturation operation that acts on low-saturation regions more strongly than high-saturation ones. This is sometimes called a vibrance operation. 0 is unity, leaving the original color values. Raising color boost from 0-100 lifts color intensity, but the low-saturation parts of the image are lifted more aggressively. Lowering color boost from 0 to -100 drops color intensity, but the low-saturation parts of the image are dropped more aggressively. 0 is unity, leaving saturation unchanged. The range is –100 through +100.
- Shadows: Lets you selectively brighten or darken shadow detail. Raising this value recovers shadow detail captured below 0 percent while leaving the midtones be. 0 is unity. The range is –100 through +100.
- Highlights: Lowering this parameter makes it simple to selectively bring back clipped highlight detail in high-dynamic-range media, easing smoothly between the recovered highlights and the untouched midtones for a natural look. 0 is unity. The range is –100 through +100.
- Saturation: A uniform saturation operation, lifting (above 50) or dropping (below 50) the color intensity of every color value in the image. 50 is unity, leaving saturation as-is. The range runs 0 (fully desaturated) through +100 (saturation doubled).
- Hue: Rotates every one of the image’s hues right around the color wheel’s rim. Its default of 50 leaves the original hue spread intact. Raise or lower the value and all hues turn forward or backward along the hue spread shown on a color wheel.
- Lum Mix: Lets you weigh the YRGB contrast adjustments made with the Master Wheels or ganged Custom curves against Y-only contrast adjustments made via the Primaries palette’s Y channel Lift/Gamma/Gain controls or the unganged Luma curve. With the default at 100, the YRGB and the Y-only contrast adjustments carry equal weight. Lower the value and the Y-only contrast moves matter less, until at 0 they’re off altogether.

On top of that, you’ll see that at the default Lum Mix setting of 100, individual moves to R, G, or B with the RGB sliders or unganged Custom curves trigger automatic moves to the other two color channels so as to hold Luma levels constant. At a Lum Mix setting of 0, individual color channel moves leave the other channels untouched.

### Auto Correction

The Auto Color command offers a fast way to automatically balance a clip’s blacks and whites from the current frame at the playhead’s position. From DaVinci Resolve 16 onward, both the A button within the Primaries palette and the Shot Match command reachable through the Thumbnail Timeline contextual menu lean on advanced algorithms — driven by the DaVinci Neural Engine — to produce better results when color balance and contrast are adjusted automatically. These controls were built to give optimal results when you work in the Rec. 709 color space at a gamma of 2.4, so they pair well with using Resolve Color Management (RCM) to normalize media first. For more on using these, see Chapter 127, “Automated Grading Commands and Imported Grades.”

### Reset Controls

The Reset control in the upper right-hand corner of the Primaries palette clears every single setting throughout the whole palette. There are also assorted parameter-specific reset controls for more targeted resets.

- Every Color Balance and Master Wheel pairing carries a reset control that clears the two together.
- Any single numeric parameter can be reset on its own by double-clicking that parameter’s name.
- The numeric parameters sitting beneath each Color Balance and Master Wheel pairing can be

cleared by double-clicking the color label shown below them.

### Color Wheels and Bars

Through the Color Wheel palette’s Primaries Wheels mode you can rebalance color and reshape contrast using the classic DaVinci controls, which govern three overlapping tonal ranges called Lift, Gamma, and Gain. Because the Lift/Gamma/Gain color balance and Master Wheel controls are bound to the YRGB Lift/Gamma/Gain sliders in the Primaries palette, adjusting either set is reflected in the other.

### Color Wheel palette

Different though they appear, the Wheels and Bars controls actually act on the very same components, only in different ways.

These tonal ranges are set by image lightness, on a scale running from 0 at absolute black to 1023 at absolute white. The illustration below approximates how the Lift, Gamma, and Gain tonal zones overlap broadly, and how each zone’s influence tapers off toward the opposite ends of image tonality.

### Lift

### Gamma

### Gain

Graphic charting how the Lift, Gamma, and Gain controls relate across the brightness range each one governs The Lift color balance control’s region of influence begins at black, then fades through the middle grays until it has no influence at white. The Gamma color balance control, meanwhile, exerts its strongest pull on the middle grays, with its influence falling away toward both black and white. Lastly, the Gain control inverts Lift: its greatest effect is at white, and its influence tapers off to nothing at black. Because these tonal ranges overlap so widely, you can make very soft, subtle, natural adjustments with them. You can also exploit that overlap by nudging an adjacent color balance control toward a color complementary to one you just applied, further restricting how much of the image is affected. The image below shows how extreme corrections interact on a grayscale image when all three Color Balance controls are used. Lift has been pushed toward green, Gamma toward blue, and Gain toward red.

Extreme moves that reveal how the Lift, Gamma, and Gain color balance controls overlap See how, extreme as these corrections are, the colors still blend smoothly. That comes from the broad overlap among all three controls, and it’s why Lift, Gamma, and Gain work so well for correcting a scene’s ambient color temperature to account for inconsistencies in lighting or camera settings.

### 3-Way Master Wheel Adjustments

The Master Wheels beneath the Color Balance controls let you precisely reshape image contrast through YRGB adjustments that separately alter the black point, the white point, and how the midtones in between are distributed. Lift: Lets you reshape the image’s perceived shadow density by altering its black point. Drag the Lift master wheel left and the image’s darkest values darken, opening the gap between its black and white points while every midtone value between them is stretched. Drag the Lift master wheel right and those darkest values lighten, dropping contrast and compressing the midtone values between the black and white points. Gamma: Lets you reshape the image’s overall perceived lightness by altering how the midtones between the Lift and Gain master wheel settings are distributed. Dragging the Gamma master wheel left darkens the whole image, while dragging it right brightens it. Most Gamma contrast moves barely affect the image’s black and white points, but large ones can push either lightness boundary farther out. This interaction is detailed further below. Gain: Lets you reshape the lightness of the highlights by altering the image’s white point. Dragging the Gain master wheel left darkens the image’s lightest values, squeezing the midtones between its white and black points. Dragging Gain right brightens those lightest values further, eventually clipping at maximum white.

### Waveform display shows the clips contrast range

These contrast moves don’t constrain one another. A large move on the Gamma master wheel, for example, can drive the image’s highlights up or its shadows down no matter what the current Lift or Gain contrast setting happens to be. These controls therefore interact to a degree, and you may find yourself bouncing between them as you finalize your contrast moves. That’s one reason a control panel is so valuable: it lets you adjust all three settings at the same time.

### Offset Color and Master Controls

That fourth set of Color Balance and Master Wheel controls is actually held in common with the Log controls and with the Primaries palette’s Offset sliders. They are the Offset controls, and they let you make linear moves that rebalance the whole tonal range of the RGB channels. There’s no Y-only control for Offset — only a Master RGB adjustment.

The Offset color balance control: Acts as a simultaneous move across all three Offset sliders in the Primaries palette; changes to the Offset color balance control likewise shift the Offset sliders. Used subtly, it makes neutralizing color imbalances in the image’s darkest part easy while rebalancing every other part at the same time. Used more boldly, this control makes it easy to lay a color wash across the whole image. The Offset master wheel: Functions as a global move on image lightness — an operation sometimes called setup — raising or lowering all RGB channels together.

On a DaVinci Micro or Mini control panel, you get at the Offset color balance and master controls through the third trackball and ring while in Offset mode; on the DaVinci Advanced Panel it’s the fourth trackball and ring, again in Offset mode.

### Color Bars Mode

Bars mode holds DaVinci Resolve’s original color adjustment sliders. Those sliders serve two purposes. First, they’re highly visible readouts of the individual YRGB channel moves made with a grading control panel’s trackballs, rings, and knobs. Second, they provide control of individual YRGB Lift/Gamma/Gain parameters with a mouse, tablet, or trackpad.

### Primary grading controls

Bars mode's principal controls are the separate Luma (or Y), Red, Green, and Blue sliders, with four of each spanning Lift, Gamma, and Gain. Through these sliders you get exact Lift/Gamma/Gain-style command over every one of the image's YRGB channels. Paired with a Parade Scope video analysis of the picture, they let you correct lopsided color imbalances in particular channels in a hurry. On top of that, the Luma (Y) Lift/Gamma/Gain sliders make Y-only contrast tweaks simple, where pushing contrast up reads perceptually as reduced color saturation. They line up with the trio of knobs stacked vertically just left of the Trackball panel on the DaVinci Advanced control panel, or with the three leftmost knobs on the DaVinci Micro or Mini control panels. Y-only contrast tweaks are a fine path to more contrast when you're chasing muted saturation or a gritty feel. The same tweak also helps wherever you want to deepen shadow density while leaving the image's colorfulness alone.
