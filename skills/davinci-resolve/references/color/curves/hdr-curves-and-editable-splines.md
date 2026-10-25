# HDR grading using curves and enabling editable splines in the custom curves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Curves.
[Chapter index](INDEX.md) / [Previous section](introduction-to-curves-and-adjusting-curves-using-the-mouse.md) / [Next section](high-clip-adjustment-and-rgb-parade.md)
<a id="source-adding-default-anchors-to-the-custom-curves"></a> <a id="source-copying-custom-curves-from-one-color-channel-to-another"></a> <a id="source-curve-intensity-sliders"></a> <a id="source-custom-curve-with-default-anchors-exposed"></a> <a id="source-custom-curve-with-editable-splines-enabled"></a> <a id="source-enabling-editable-splines-in-the-custom-curves"></a> <a id="source-ganging-and-unganging-custom-curves"></a> <a id="source-ganging-and-unganging-soft-clip-controls"></a> <a id="source-hdr-grading-using-curves"></a> <a id="source-high"></a> <a id="source-soft-clip"></a> <a id="source-soft-clip-controls"></a> <a id="source-ysfx-sliders"></a>

### HDR Grading Using Curves

While reaching for various grading controls on the Color page to grade wide-latitude images bound for HDR output, you might find it handy to switch on the HDR mode of the node you’re on — right-click that node in the Node Editor and pick HDR mode from the contextual menu (offered only in Resolve Studio).

Switching a node into HDR mode by way of its contextual menu This setting reshapes that node’s controls so they operate across an expanded HDR range. In practical terms, this eases work on wide-latitude signals through controls that function by letting you adjust at various tonal ranges — Lift/Gamma/Gain, Custom Curves, Soft Clip, and so on among them.

### Enabling Editable Splines in the Custom Curves

With the Curve palette in Custom mode, picking Editable Splines from the option menu reveals Bezier spline handles on any selected control point, which let you fine-tune the curve more precisely as the need arises.

### Custom curve with editable splines enabled

NOTE: Take care with curve adjustments that turn too sharp, or with control points crowded too closely, since they can bring on unwanted contouring within the image, causing flattening or solarization in spots you might not intend.

### Adding Default Anchors to the Custom Curves

From the option menu of the Curve palette in Custom mode you can also pick Default Anchors to set three more control points on the curve, splitting it into five segments that act on the image’s shadows, low midtones, medium midtones, high midtones, and highlights.

### Custom curve with Default Anchors exposed

### Ganging and Unganging Custom Curves

Out of the box the Custom curves are ganged, so that a curve adjustment acts on a clip’s YRGB channels as one, giving an image-contrast change much like reaching for the Master Wheels in the Color Wheels palette. Make this kind of adjustment and raising contrast raises image saturation too, while lowering contrast lowers image saturation too. Since curves can be worked with finer specificity than the three Master Wheels allow, the YRGB curves let you make far subtler contrast adjustments than the Master Wheels alone. Switch ganging off and you unleash the full reach of the Custom curves on the image. Where the Color Balance controls each move all three color channels at once, the Curve controls let you work each channel on its own once Gang Custom Curves is switched off. To switch off Custom curve ganging: Click the Curve Edit button matching the curve channel you mean to edit. Clicking any Curve Edit button lifts that curve into focus so it’s simple to edit where curves overlap one another. Once one or more curves sits offset from the rest, you’re free to edit any curve by dragging its control points.

On the left you’ll find the Custom Curve Edit buttons, with the Gang button over on the right

To switch Custom curve ganging back on: Click the Gang button to the left of the Curve Edit buttons. Reaching each color channel by way of its own separate curve adjustment lets you craft smooth color-channel specific corrections — or, going the other direction, make wildly individual moves to conjure a broad range of creative effects.

Turning off curve ganging lets you independently adjust each curve TIP: With curve ganging switched off, the Luma curve lets you work the Y channel on its own — much like reaching for those Y-only Lift/Gamma/Gain knobs on the Micro, Mini, or Advanced Control Panels of DaVinci Resolve. Make this kind of adjustment and raising luma contrast brings a perceived drop in image saturation.

### Copying Custom Curves From One Color Channel to Another

Even once you’ve unganged the Custom curves, you can still echo one curve’s adjustments onto another: copy it using, from the Curve palette’s option menu, the “Copy to Red/Green/Blue” commands.

### Curve Intensity Sliders

To the right of the Curve Editor sit four Curve Intensity sliders, one per channel, letting you blend between the current curve’s effect on the clip and the image’s original state before you touched the curve. An Intensity left at its default of 100 has that curve press its full effect onto the image, while an intensity of 0 has that curve act on the image not at all. The Intensity sliders give you a simple route to “split the difference” between any curve adjustment and whatever state the image was in before.

Pulling the Curve Mix slider down eases how strongly that curve’s adjustment bears on the image.

### YSFX Sliders

Each of the Custom curves (Y’, R, G, and B) carries a vertical YSFX slider up in the Curve Editor’s upper left-hand corner, letting you invert any or all color channels by whatever amount you like, for conjuring different kinds of stylized effects.

Image with the Luma channel modified using the vertical YSFX slider Just like every other adjustment on the Color page, YSFX can be paired with Power Windows or HSL qualification to confine channel inversions to certain portions of the image for creative ends.

### Soft Clip

Four sliders beneath the Custom curves’ Curve controls make up the Soft Clip controls, handing you an interface for tuning highlight and shadow soft clipping either across the board, with Ganging on, or channel by channel. The Soft Clip controls are meant for clip-by-clip tuning, as against the Generate Soft Clip LUT settings, which let you fix one soft-clipping setting across the whole program. For more on the Soft Clip LUT setting, turn to Chapter 4, “System and User Preferences.”

High and Low Soft Clip controls within the Curves palette What soft clipping does is put a “knee” on any clipping happening at the image’s upper or lower extremes, and it can quickly take the edge off any unpleasantly harsh loss of detail that comes from blowing out the highlights or crushing the shadows too hard. In the example below, the top screenshot has had its highlights deliberately blown out by overdoing the highlight contrast. As you can tell, the edges of the clipped area carry no detail. The bottom screenshot shows the same image with soft clipping raised across all three color channels. The outcome pulls back detail, squeezing the highlights so the tops of each color channel come back inside the allowable range.

Using High Soft Clip to pull highlight details into the viewable range

### Ganging and Unganging Soft Clip Controls

You can apply soft clipping to all three color channels at once by switching on the Ganging control (on by default), or you can switch Soft Clip ganging off to tune each channel on its own. As an example, soft clipping per channel can help when you’re legalizing RGB out-of-gamut errors on channels that overshoot or undershoot the QC standards you work to. To switch off Soft Clip ganging and tune soft clipping per color channel: Click whichever channel control button matches the color channel you mean to edit, then drag the sliders until the adjustment is where you want it. To switch Soft Clip ganging back on: Just left of the Soft Clip channel controls, click the Ganging control. TIP: Lay too much soft clipping onto individual color channels and you may push an unwanted color tint into the matching highlights or shadows of an image. To steer clear of that, work the soft clipping parameters with ganging on so all three color channels clip equally.

### Soft Clip Controls

Ganged or not, soft clipping for each color channel is steered through two sliders plus two more parameters.

### High

What the High Clipping Point slider does is let you set the top signal level past which the signal gets clipped. Every pixel above the clipping level gets pinned to the clipping level.

By default, measured against the DaVinci Resolve internal video scopes, the High Clipping Point lands at a digital level of 1023. Drag this slider leftward and the image’s highlights clip at a lower level, which gives lower, dimmer maximum levels.
