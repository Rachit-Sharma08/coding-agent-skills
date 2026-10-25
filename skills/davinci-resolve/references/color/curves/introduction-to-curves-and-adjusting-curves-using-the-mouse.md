# Introduction to curves and adjusting curves using the mouse

Version: DaVinci Resolve 20.3 Reference Manual. Context: Curves.
[Chapter index](INDEX.md) / [Next section](hdr-curves-and-editable-splines.md)
<a id="source-adjusting-curves-using-the-mouse"></a> <a id="source-clicking-on-a-feature-of-the-image"></a> <a id="source-curves"></a> <a id="source-curves-histograms"></a> <a id="source-curves-part-1"></a> <a id="source-custom-curves"></a> <a id="source-editing-the-top-and-bottom-control-points-of-curves"></a> <a id="source-introduction-to-curves"></a> <a id="source-sampling-images-to-place-control-points-on-curves"></a> <a id="source-showing-picker-rgb-values"></a> <a id="source-the-curve-control-at-its-original-state"></a>

### Curves

A capable curves interface on the Color page hands you controls for tuning color and contrast through the Custom Curves, plus an assortment of “Hue” or “HSL” curves that let you tackle more pinpointed adjustments to hue, saturation, and luminance in a number of ways.

### Introduction to Curves

You reach the Curves palette through one of the toolbar buttons sitting above the Center Palette panel of the Color page, and it carries six modes, each offering a different curve-based way of working an image’s color and contrast. Every curve lets you tune a customizable region of the picture, keyed to one of three things: image tonality (those zones running light or dark), hue (particular colors), or saturation (how intense the color is). You can adjust all of the curves with the pointer, or with knobs on the DaVinci Resolve Mini or Advanced control panel. Whenever you’re working in Resolve Color Management (RCM) or ACES, the Curves palette is color-space-aware. In practice that means each curve’s overall range fits the current clip’s overall data range better, whatever Timeline Color Space you happen to be in, across both SDR and HDR mastering. The upshot is curves adjustments that come more easily, land more precisely, and feel more consistent, whatever workflow you happen to be running. TIP: Every curve in DaVinci Resolve can act on the whole image, or be confined to just one portion of it as part of a secondary operation built from qualifiers, windows, imported mattes, or any mix of the three.

### Adjusting Curves Using the Mouse

For basic on-screen tweaking with the pointer — driven by your mouse, pen, or whatever input device you prefer — every Color curve in DaVinci Resolve relies on the controls below. Ways of adjusting curves through the on-screen interface:

- To add a control point: Click somewhere on a curve. Wherever the mouse sat when you clicked, a control point gets added, and the curve bends, where it must, to meet that new control point’s position.
- To add a control point without altering the curve: Keep the Shift key held and click anywhere on or near a curve. A control point lands on the curve wherever the pointer was when you clicked, yet the curve stays put.
- To make a control point snap onto the curve’s neutral diagonal: (Custom curve only) Keep the Option key held as you drag any control point on the curve. A diagonal line shows up marking the image’s neutral state, and the control point snaps onto it. Let go of the Option key and then press it once more afterward, and the diagonal guide line goes away.
- To remove a control point: Right-click any control point and it vanishes.
- To return one color channel curve to a fully neutral setting: To the right of that color channel’s intensity slider, click the reset button

there.

- To return every color channel curve at once: Up in the Curves palette’s upper right-hand

corner, click the Reset Custom Curve button. Out of the box, a control point governs the stretch of each curve lying between its two neighboring control points.

A control point’s adjustments act on the whole stretch of curve between adjacent control points. Up in the top screenshot, notice that the control point where the pointer sits governs the bigger part of the curve falling between the lower left-hand control point (present by default) and a user-created control point set up within the curve’s highlights. Down in the bottom screenshot, one more control point placed left of the one being moved narrows the area of curve that gets adjusted. Placing extra control points with care lets you make remarkably targeted adjustments to images via the Custom curves.

What this example drives home is how useful control points are for “locking off” stretches of a curve at a neutral or near-neutral position, so certain parts of an image stay unchanged even while you work other control points to make changes. NOTE: The HSL curves additionally carry an optional adjustment mode using Bezier curves, which those sections will get into.

### Sampling Images to Place Control Points on Curves

A further way to drop control points onto curves is to bring the pointer over to the Viewer and click to sample a color value, which sets a control point on whichever curve is currently open at the spot matching that value. This holds for Custom, Hue, and HSL curves.

### Clicking on a feature of the image

Creates a control point on the currently open curve

### Showing Picker RGB Values

As you drag the pointer across the Viewer hunting for a feature to sample, you can switch on a tooltip showing the RGB Value of the pixel beneath the pointer — right-click the Viewer and pick Show Picker RGB Value to flip this feature on and off. Switch it on and the Show RGB Picker Values In submenu inside the Viewer’s option menu offers a choice of displaying either 8or 10-bit tristimulus values.

Switch on Show RGB Picker Values and this color picker tooltip shows up

### Curves Histograms

Both the Custom curves and the HSL curves carry a histogram standing in for the input of the currently selected Correction node, handy for steering your adjustments. Through the Histograms submenu of the Curves palette’s Option menu you can switch these histograms off, or flip them between showing the node’s input and its output. Flip to Output and the histograms refresh to show the result of your adjustments — at the cost of seeing the image data the curve is actually acting on.

The Custom curves show a YRGB histogram:

A YRGB histogram analysis is what the histogram below the Custom Curves shows Every Hue or HSL curve carries a histogram analysis of whichever two color channels that Curve works on — say, to give three examples, saturation level set against hue, saturation level set against luminance, or saturation level set against saturation level. With Hue or HSL curves, these histograms make it simple to spot which stretches of the Curve controls will genuinely act on image data.

The histogram below the Hue vs Sat curve plots every saturation level at each value of hue

### Custom Curves

DaVinci’s Custom curves deliver smooth tuning of each clip’s Y, R, G, and B channels. Two areas split the Curves palette’s Custom curve mode: on the left the Curve Editor, on the right the Curve controls. The editor houses the actual Curve controls you reach for to adjust the image. The right-hand controls let you pick which curves you’re working and dial in their intensity.

Here the Custom curves build a gentle “S” curve adjustment, with four extra control points set down What the Custom curves are good for is making more tonally specific, channel-by-channel adjustments to an image than the Color Balance controls can manage. They’re also good for strange and wonderful stylistic moves through unusual tweaks to different combinations of color channels. Though the ganged Custom curves look like one curve control, the Custom curve editor is really laid out as a stack of overlaid curves, and the YRGB curves all turn up inside one editor. Out of the box, the Custom curves rest neutral as a diagonal line running from the image’s lower-left black point up through its upper-right white point.

The curve resting at its neutral diagonal, where nothing is being adjusted

Running left to right, the horizontal axis maps how the original image’s tonality spans out — black sitting at the left, white at the right — whereas the span of change you’re able to make is what the vertical axis maps. By dropping control points onto the curve’s surface and raising or lowering it at various regions, you’re effectively remapping a color channel’s original horizontal “input” value to whatever “output” value you like. Further controls turn up to the right of the curve editor itself. Across the top sits a row of buttons that let you pick the curve tied to an individual color channel for isolated tweaking, while a vertical stack of four sliders lets you dial in the intensity of each color channel’s curve.

Off to the curve editor’s right sit the channel-editing buttons together with the curve intensity sliders

### Editing the Top and Bottom Control Points of Curves

Curves can also be edited through the two default control points that the curve control begins with in the Curve Editor. The Black Point control (down at the lower-left) and the White Point control (up at the upperright) let you stretch and squeeze the video signal much as the Lift and Gain Master Wheel controls in the Color Wheels palette would.

### The Curve control at its original state

Here the Black and White Point controls are dragged rightward and leftward so as to stretch the signal

There are these ways to put the Black and White Point controls to use: Using the Black Point control: Drag this control upward and you make a lift adjustment that raises the signal’s black point. Drag this control rightward and you make a lift adjustment that lowers the signal’s black point. Using the White Point control: Drag this control downward and you make a gain adjustment that lowers the signal’s white point. Drag this control leftward and you make a gain adjustment that raises the signal’s white point.
