# Gamut and hue curves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Gamut, Hue curves.
[Chapter index](INDEX.md) / [Previous section](gamut-basic-node-setup.md) / [Next section](ocio-cdl-transform-and-ocio-color-space.md) / [Gamut Gmt](copy-aux-and-gamut.md)
<a id="source-032-069-006-0351--"></a> <a id="source-a-gamut-node-applied-to-a-mediain1-node"></a> <a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-custom"></a> <a id="source-fusion-2158"></a> <a id="source-gamut-controls"></a> <a id="source-hue-curves-controls"></a> <a id="source-hue-curves-hcv"></a> <a id="source-hue-curves-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-settings-tab"></a> <a id="source-settings-tab-1"></a> <a id="source-the-hue-curves-node"></a>

### Inspector

### A Gamut node applied to a MediaIn1 node

### Gamut controls

### Controls Tab

Every conversion happens on the Controls tab. The panel is split into one zone for arriving imagery and another for what the node sends downstream. The zone you reach for hinges on your intent: are you peeling a gamma curve off an image to render it linear, or are you taking a linear image and assigning it a particular color space plus gamma curve on the way out? Source Space Source Space sets the incoming color space of the image. With the node placed straight behind a Loader node in Fusion or a MediaIn node in DaVinci Resolve, pick whichever color space suits the way the image originated, then tick the Remove Gamma checkbox. What leaves the node will then be a linearized image. Keep this control set to No Change whenever you are layering gamma back on through the Output Space control and seating the node just upstream of either the Saver node (in Fusion) or the MediaOut node (in DaVinci Resolve). DCI-P3 People most often reach for the DCI-P3 color space when DLP projectors are involved. It commonly ships as a color space offered by DLP projectors, and it also shows up as an emulation mode on 10-bit LCD monitors like the HP Dreamcolor and Apple’s Pro Display XDR. The SMPTE-431-2 standard is what defines this color space.

### Custom

With the Custom gamut, you spell out the color space using CIE 1931 primaries together with a white point — both given as XY coordinates — plus gamma, limit, and slope. As an illustration, were the DCI-P3 gamut covered earlier instead written out as a Custom color space, it would carry the values below.

Red Primary Green Primary Blue Primary White Point Gamma Linear Limit

0.68 0.265 0.15 0.314 2.6 0.0313

### 0.32 0.69 0.06 0.351 – –

A good way to get a feel for these controls is to hook the node to a gradient background, switch to Waveform mode, and watch how the output shifts as you tweak each setting. Output Space Output Space remaps the gamut into whatever color space you are after. As an example, while handling linearized images inside a composite, you would drop the Gamut node right ahead of the Saver node and let the Output Space remap to the gamut your final delivery file calls for. Set this control to No Change when your goal instead is to peel off gamma by means of the Source Space control.

NOTE: For output that meets the HD spec Rec. 709, Fusion labels a gamma of 2.4 as Scene and labels a gamma of 2.2 as Display.

Remove/Add Gamma Tick these checkboxes to run the gamut conversion under either a linear or nonlinear gamma, or merely to strip or apply the relevant gamma values while leaving the color space untouched. Pre-Divide/Post-Multiply Turning on this checkbox divides each pixel value by its Alpha value ahead of the color correction, then multiplies it back by that same Alpha value once the correction is done. The benefit is that it keeps illegally additive images from forming, which tends to happen along the fringes of a blue/green key or with 3D-rendered objects.

### Settings Tab

You will find the Settings tab of the Inspector mirrored across the other Color nodes as well. A full account of these shared controls sits at this chapter’s close, under the “The Common Controls” section.

### Hue Curves [HCv]

### The Hue Curves node

### Hue Curves Node Introduction

With the Hue Curves node you reshape an image’s color through a family of spline curves. There are splines for steering the image’s hue, saturation, and luminance, plus one for each separate color channel. A further group of curves lets you apply suppression channel by channel. What sets the Hue Curves node apart from Fusion’s other color correction nodes is how far the splines can be pushed: you can clamp the node’s reach down to a tiny slice of the image or stretch it across a broad swath. On top of that, the curves can be keyframed so they track how the image evolves frame to frame. Because the spline’s main axis follows the image’s hue, pulling out one particular color for tweaking becomes far simpler.

### Inputs

Two inputs sit on the Hue Curves node: one carries the primary image, and the other takes an effect mask that confines where the color correction lands. Input: Orange in color, this is the sole mandatory hookup, feeding a 2D image into the Hue Curves color correction. Effect Mask: This optional blue input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps generated by other tools. Wiring a mask here restricts the Hue Curves operation to the pixels the mask covers. The effect mask gets applied once the tool has finished its processing.

### Basic Node Setup

As is true of many 2D image-processing nodes, the Hue Curves node takes in a 2D image — supplied here by a Loader node or the MediaIn1 pictured below. From there its output carries on down the node tree into a further 2D image-processing node or a Merge node.

A Hue Curves node applied to a Loader node in Fusion Studio

### Inspector

### Hue Curves controls

### Controls Tab

A row of color attribute checkboxes on the Controls tab governs which splines appear inside the Spline window. That spline graph stretches sideways, with control points seated at each primary color along the horizontal. Dragging those control points alters whichever color attribute you have chosen. Mode The Mode setting flips between No Animation and Animated Points. By default it sits on No Animation, in which your curve edits hold steady across the whole clip. Switch the Mode over to Animated Points or Dissolve and the color curve can then change across time. Dissolve has effectively been retired and remains only so older comps still open. Color Channel Checkboxes These boxes mark which splines you can edit and which ones respond when you sample a color with the Eyedropper. You may edit several active splines at once, yet it is usually tidier to keep only the spline you are working on active so the others stay untouched. Click the Eyedropper icon and a point lands on every active spline to mark the color you grabbed. Spline Window Acting as the central interface piece of the Hue Curves node, this graph display holds all the splines. It looks much like the Color Curves node, except here hue runs along the horizontal axis while the amount of adjustment runs up the vertical. Curves for the separate channels appear in the Spline window, which behaves as a compact Spline Editor — indeed, the very curves drawn here turn up and stay editable inside the full Spline Editor too. Every component’s spline starts out flat, its control points lined up across the primary colors, which read from left to right as Red, Yellow, Green, Cyan, Blue, and Magenta. Since the hue gradient wraps around in a cycle, each curve’s leftmost control point ties back to its rightmost one. A right-click within the graph pops a contextual menu offering choices to reset curves, bring in external curves, tune the smoothness of the chosen control points, and more.

### FUSION 2158

In and Out Reach for the In and Out controls when you need to dial in exact figures for a chosen point. To revise a value, highlight a point and type the In/Out figures you want. Eyedropper Press and drag from the Eyedropper icon and your pointer turns into an Eyedropper. Keep the button held while you sweep over a viewer to sample a pixel out of whatever image is shown. Doing so drops control points — pinned along the horizontal axis — onto the curves that are currently active. Each control point marks where the sampled color falls on the curve. The Lock Selected Points toggle in the contextual menu releases points again so they regain horizontal freedom. Only enabled splines receive new points; to confine points to one channel, switch off the rest before you sample. Pre-Divide/Post-Multiply Ticking this checkbox divides the image’s pixel values by their Alpha values before the color correction runs, then multiplies them back by that Alpha value afterward. It comes in handy when you are correcting images carrying a premultiplied Alpha channel.

### Settings Tab

This same Settings tab shows up in the Inspector for the rest of the Color nodes too. Each of these common controls gets a thorough write-up where the chapter ends, in the “The Common Controls” section.
