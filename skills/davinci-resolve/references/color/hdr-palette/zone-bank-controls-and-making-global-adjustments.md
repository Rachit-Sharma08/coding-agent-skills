# Zone bank controls and making global adjustments

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR palette.
[Chapter index](INDEX.md) / [Previous section](hdr-palette-controls.md) / [Next section](making-zone-based-adjustments.md)
<a id="source-black-offset-explained"></a> <a id="source-making-global-adjustments"></a> <a id="source-the-zone-bank-controls"></a>

### The Zone bank controls

Because you’ll nearly always have more zones on hand than you have space to adjust them, this interface reveals which zones you’re working with at the moment, which zones are mapped to a control panel, and which other zones you can swap to. By default, three active zones appear up top, matching the three sets of Zone controls positioned to the left of the Global controls. Zones that exist but are hidden show up in gray on the left and/or right of the zones currently visible, which appear in color. By this means, you can bank back and forth across three zones at once while keeping the Global controls always on hand for adjustment. The HDR palette’s Option menu also holds a setting, “Bank Global With Color Wheels,” that puts all four GUI control clusters in the palette to work showing Zones controls, speeding up how quickly you can hop between tonally-specific adjustments. Under that mode, four active zones appear up top, matching the four sets of Zone controls on display. In this mode, though, you have to page all the way over to the right to surface the Global controls, since they’re banked together with every other zone.

The Zone bank controls configured to display four zones when the Global controls are banked together with all the other zones. With these controls you can move your visible control across every available zone, much the way audio mixers shift between banks of tracks using a fader panel. Ways to switch between different Zone controls:

- Clicking any gray zone button sitting to the left of the zones now visible shifts all zones so that the leftmost visible zone lands on that one.
- Clicking any gray zone button sitting to the right of the zones now visible shifts all zones so that the rightmost visible zone lands on that one.
- Clicking the Left or Right Arrow buttons on either side of the zones indicators nudges all zones one step to the left or one step to the right.

### Making Global Adjustments

As a rule, when you’re leaning on the HDR palette for primary grading, the Global controls are where you’ll most likely want to start. Out of the box, they live at the right of the Controls panel.

The graphical Global control cluster, positioned at the right of the HDR palette. With these controls you take that first step of applying an overall adjustment to the image. For color, you’re given a color balance wheel, temp and tint sliders (flanking the wheel on the left and right, and numerically below it too), and saturation adjustments. For image contrast, a Global Exposure control lets you stretch overall image contrast upward to lighten the image, or squeeze it downward to darken it, relative to the present Black Offset level, which holds pixels at minimum black in place. At the bottom of the palette, a pair of Contrast/Pivot controls let you work overall color contrast by spreading highlights and shadows outward or inward relative to the pivot point, measured in stops. Global color adjustments bear some resemblance to the offset, temp, and tint controls in the Color Wheels or Log Wheels controls, yet there are meaningful differences, laid out in detail below. The Global Exposure control, by contrast, works in a very different fashion from Master Offset. A closer look at the Global controls:

- Global Color Balance: A color balance control that lets you shift the red, green, and blue channels together, more or less linearly through the image’s tonal range, to rebalance the color freely. That said, RCMv2 keeps a smooth saturation and exposure rolloff going automatically in the maximum highlights and minimum shadows, so the effect fades in the blackest blacks and the whitest whites of the image (the effect looks stronger in test gradients than in real world images). Adjustments via this control won’t push the darkest pixels in the image below the Black Offset level, though individual color channels can drop beneath that level to hold onto colorfulness within darker shadows. The color changes this control produces resemble the way optical color filters mounted over a lens would alter an image.

(Top) The original image, (Bottom) A Global Color Balance adjustment acting on the whole image, with a rolloff visible in the shadows and highlights of the superimposed ramp gradient

- Global Exposure: Lightens or darkens the whole image. Dragging rightward stretches image contrast by lifting the highlights while holding the shadows fixed relative to the Black Offset value. Dragging leftward reduces image contrast by lowering the highlights while holding the shadows fixed relative to the Black Offset value. For a fuller account of how Black Offset works, refer to the next section.

Bear in mind that every contrast move in the HDR palette holds saturation steady whether contrast rises or falls. The upshot is that, even with sizeable contrast moves on HDR images, the image’s saturation stays perceptually unchanged.

(Top) The original image, (Bottom) Raising Global Exposure

- Global Saturation: Boosts or cuts the intensity of color across the whole image. Because contrast moves leave saturation alone, any changes you want in image saturation you’ll have to make by hand.
- Global Color Balance Value Fields: Two numeric values capture how the color balance control’s center handle position is expressed. There are two numeric representations available: X and Y, or Angle and Strength. You pick whichever you like from the HDR palette’s Option menu; the method you select governs how the center handle of every color balance control behaves when you edit these values directly.

Down at the bottom of the HDR palette, you’ll find further Global Temp and Tint, Hue, Midtone Detail, and Contrast/ Pivot controls; these apply other sorts of global adjustments to the image’s color, detail, and contrast, in ways closely mirroring the same-named controls in the Color Wheels or Log Wheels controls. There’s also a Black Offset control for setting the lowest permitted black level in the current shot.

Global controls located at the bottom of the HDR palette. A closer look at the additional Global controls:

- Temp: This global temp adjustment warms or cools the image across a range running from -4000 to +4000 on a kelvin scale. The adjustment tracks the spectral locus line of the CIE graph, so the strength of the move stays naturalistic. To hold visual artifacts down, this control can warm the image more aggressively than it cools it.
- Tint: This global tint adjustment applies “plus green” or “minus green” shifts over a range from -100 to +100 on an arbitrary scale.
- Hue: Spins every hue in the image around the entire rim of the color wheel. At its default of 50 the original hue distribution is shown. Pushing this value up or down rotates all hues forward or backward along the hue distribution as it appears on a color wheel.
- Midtone Detail: Raising this parameter lifts the contrast of image regions carrying high edge detail, heightening the sense of image sharpness. People sometimes call this effect definition. Pushing the parameter into negative territory softens image regions with little detail, while leaving high-detail areas untouched. 0 is unity. The range runs –100 through +100.
- Contrast: This single parameter widens or narrows the gap between an image’s darkest and lightest values, raising or lowering image contrast. It behaves much like driving the Lift and Gain master controls in opposing directions at the same time. Bright and dark portions of the image are spread apart or drawn together about a center point set by the Pivot parameter. In contrast to the Contrast control in the Primaries palette, the HDR palette’s Contrast control disregards whatever the “Use S-curve for contrast” checkbox is set to, found within the General Options panel of the Project Settings.

Remember that all contrast moves in the HDR palette keep saturation fixed as contrast climbs or drops. So even with substantial contrast moves on HDR images, the image’s saturation looks perceptually identical to your eye, with tiny tweaks made to the image’s actual saturation to sustain that perception. Note that the tone mapping settings in RCMv2 will influence how much saturation survives in the topmost highlights and bottommost shadows of the image, as opposed to being rolled off automatically at the outer edges of the signal.

(Left) The original image, (Right) Raising Contrast; saturation holds perceptually constant, apart from the signal’s outer edges within the highest highlights and lowest shadows (subject to however your RCM tone mapping is configured).

- Pivot: Shifts the tonal center about which the image’s dark and bright portions get spread or pulled in during a contrast move. This lets you reshape how contrast falls across the shadows and highlights. At its default of 0, it lifts highlights above 50% gray higher and drops shadows below 50% gray lower, in equal measure to each other. Moving the pivot point alters the percentage of image tonality about which contrast gets expanded or compressed.

Darker images can call for a lower Pivot value to lift more levels upward and keep from crushing the shadows too hard when stretching image contrast, whereas lighter images may gain from a higher Pivot value to drive levels down and build shadow density.

(Top) Changing contrast by raising Pivot, which shifts most of the contrast expansion downward toward the shadows, (Bottom) Changing contrast by lowering Pivot, which shifts most of the contrast expansion upward toward the highlights

- Black Offset: Sets the darkest permitted part of the image. No move by any other control in the HDR palette will ever drop below this level, apart from the occasional color channel when the shadows grow extremely saturated. For fuller detail on this enormously important control, turn to the very next section.

### Black Offset Explained

Among all the Global controls, the Black Offset control ranks as one of the most quietly important. Black Offset lets you set the image’s darkest pixels. Moves applied to Black Offset don’t offset the whole signal; they touch only the very darkest stretch of the signal, letting you lift or lower the image’s black point while smoothly feathering the resulting move into the untouched part of the image. As a result, you’re able to squeeze or stretch the bottom of your signal. Lift Black Offset and you can introduce “flaring” to the image, akin to how light flaring inside a lens might brighten the image’s darkest area.

(Left) The original image, (Right) Raising Black Offset so as to add flaring to the image’s darkest pixels. As an alternative, you can drop Black Offset to lower the very darkest pixels in the image. When the source image is dark enough, this control can take the darkest pixels below 0, yet that image detail is retained within the color image processing pipeline. The key thing to grasp about this control is that whatever level you set Black Offset to becomes the new level at which Global exposure adjustments occur. In the example that follows, the first image presents the original color of a clip exposed dark. In the second image, Black Offset is tuned to lift the image’s darkest parts, compressing them relative to the midtones and lending the shadows a pleasing flaring effect.

(Left) The original image; (Right) Black Offset raised on that same image. Now look at the next image, where Global Exposure is lifted, and the Waveform scope reveals how the exposure change stretches the image’s contrast upward, with the darkest pixels “locked” to the Black Offset you defined.

(Left) Before, (Right) After raising Global Exposure to stretch image contrast outward from the Black Offset level; observe that the bottom of the signal keeps “touching” the same level once global exposure is lifted.

The Black Offset level you choose likewise becomes the minimum picture level whenever you bring exposure down, whether through Global Exposure changes or by way of the “darkening” zone controls — Shadow, Dark, and Black among them. The next image illustrates what happens when you lower Global Exposure; the image’s shadows compress more aggressively than the highlights as exposure drops, leaving the image’s minimum value parked at the Black Offset level you defined. While shadow detail stays impressively intact, this compression rolls off smoothly and nonlinearly through the midtones so the image keeps looking as natural as it can.

(Left) Before, (Right) After Global Exposure is dropped, squeezing image contrast downward until it reaches the Black Offset level; observe how the signal never dips below the Black Offset level. The same holds when you use other darkening zone exposure controls, like the Shadow control, which selectively drives the exposure of the image’s darker region down while leaving the highlights untouched. As you reduce Shadow exposure, the darkest pixels still compress such that nothing falls below the Black Offset level you defined. In short, you can tweak Black Offset whenever you like, before or after any other Global or Zone adjustment, to fine tune the image as needed.
