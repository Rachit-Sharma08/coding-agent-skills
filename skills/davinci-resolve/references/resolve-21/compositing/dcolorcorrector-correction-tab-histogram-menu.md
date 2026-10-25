# Dcolorcorrector correction tab histogram menu

Version: DaVinci Resolve 21 New Features Guide. Context: Dcolorcorrector.
[Chapter index](INDEX.md) / [Previous section](reliefmap-and-dcolorcorrector.md) / [Next section](dcolorcorrector-and-speedwarp.md) / [dColorCorrector dCC](reliefmap-and-dcolorcorrector.md)
<a id="source-correction-tab-histogram-menu"></a> <a id="source-correction-tab-suppress-menu"></a> <a id="source-getting-started"></a> <a id="source-improved-lens-distort-tool"></a> <a id="source-options-tab"></a> <a id="source-ranges-tab"></a> <a id="source-settings-tab"></a> <a id="source-the-fusion-variables-map-preference"></a> <a id="source-user-defined-metadata-variables-in-paths-expressions-and-scripts"></a>

### Correction Tab Histogram Menu

Setting the menu to Histogram generates a histogram display from the input image. When a reference image is supplied as well, that reference image gets its own histogram shown too. This tab’s controls mainly serve to match one image against another, by way of the Equalize or Match modes of the dColor Corrector.

dColor Correction in Histogram mode Channel With this menu you choose which color channel — or the Master channel — to select and show the histogram for. Histogram Display A histogram is a graph showing how color values are distributed throughout the scene. Reading from one side to the other, the leftmost values represent the scene’s deepest darks while the rightmost ones represent its brightest tones. Wherever many pixels in an image carry the same or a similar value, that portion of the graph climbs higher. Since luminance gets computed for each channel separately, red, green, and blue all maintain individual histograms, and the three together make up the Master Histogram. Scaling the histogram up and down is done by holding the mouse pointer inside the control and dragging up to zoom in or down to zoom out. Display Selector Toolbar Found across the top of the histogram, the Display Selector toolbar offers a means of turning components of the histogram display on or off. Pause the mouse pointer over a button and its tooltip describes the button’s purpose.

- Input Histogram: Turns the showing of the input image’s histogram on or off.
- Reference Histogram: Turns the showing of the reference image’s histogram on or off.
- Output Histogram: Turns on or off the showing of the histogram drawn from the

post-color-corrected image.

- Corrective Curve: Switches a spline display on or off so you can see exactly how the automatic color

corrections, applied through a reference image, are altering the image. It proves handy as you even out luminance between the input and reference images.

### Correction Tab Suppress Menu

Color Suppression gives you a way to strip an unwanted color component out of the image. The Color Wheel control resembles the one in the node’s Colors section, except this version has six controls ringing it, one for each specific color around the wheel. To knock down a color in the chosen range, drag the control standing for that color in toward the center of the color wheel. The nearer that control sits to the center, the more strongly its color is suppressed from the image.

dColor Corrector Suppression controls Suppression Angle The Suppression Angle control turns the controls on the suppression wheel so you can home in on one particular color. Reset All Suppression Clicking this control sets the suppression colors back to 1.0, which is their default.

### Ranges Tab

Inside the Ranges tab live the controls that define which of an image’s pixels count as shadows and which count as highlights. The midrange is always whatever pixels weren’t already swept into the shadows or the highlights. Range This menu picks the tonal range shown in the viewers. They make it easier to see the pixels within that range. With the Result menu option chosen, the image the color corrector puts in the viewers is the color-corrected image. That’s the default. Pick one of the other menu options and the display flips to a grayscale image marking which pixels belong to the selected range. The white pixels are the ones counted as part of the range, while black pixels lie outside it. Choosing Shadows, for instance, would render pixels regarded as shadows white and everything else black. Mid-gray pixels are only partway in the range and won’t take the full effect of any color adjustments aimed at that range.

dColor Corrector Ranges controls Channel This tab’s Channel menu lets you inspect the range of one specific color channel. Out of the box, Fusion shows the luminance channel whenever the color ranges are being examined. Spline Display You pick the ranges by working the spline handles. Four spline points exist, each carrying a single Bézier handle. The upper two handles mark where the shadow and highlight ranges begin, while the lower two mark where the range ends. Falloff is governed through the Bézier handles. The midtones range carries no controls of its own, since its span is understood as whatever falls in between the highlight and shadow ranges. The X and Y text controls beneath the spline display let you key in precise coordinates for whichever Bézier point or handle is selected. Output the Range You See Now as Final Render Ticking this checkbox makes the monochrome view of the range shown in the viewers become the final render. Ordinarily the Color node sends out the complete RGBA image, even when the node was set to show one of the color ranges in the view. This control lets you put the dColor Corrector node to work generating a range’s matte for use as an effect mask elsewhere among the nodes. Preset Simple/Smooth Ranges These two buttons return the spline ranges to either Smooth (default) or Simple (linear) settings.

### Options Tab

The Options tab carries a handful of very important processing operations, among them an easy fix for color correcting premultiplied Alpha channels. dColor Options controls Histogram Proxy Scale How much precision is used when histograms are built and computed is set by the Histogram Proxy Scale. Lower values mean greater precision, whereas higher ones give a coarser, more generalized histogram. Process Order This menu decides whether tweaks to the image’s gamma happen before or after any changes applied to the image’s levels. Apply Mask Inverted Turning on the Apply Mask Inverted option flips the tool’s entire mask channel. That mask channel is the merged result of every mask either connected to or created within a node.

### Settings Tab

Clipping Mode This option governs how edges get treated during domain of definition rendering. It matters most for nodes such as Blur, which can need samples from parts of the image beyond the current domain.

- Frame: Frame is the default; it makes the node’s domain of definition span the image’s full frame on its own, which in effect disregards the current domain of definition. Where the upstream DoD comes in smaller than the frame, whatever frame area is left over reads as black/transparent.
- Domain: Choose Domain and the node honors the upstream domain of definition while its effect is applied. In cases where the node uses a large filter, this can produce unwanted clipping.
- None: Choose None and no clipping of the source image happens whatsoever. So any data the node’s effect needs that would ordinarily fall beyond the upstream DoD reads as black/transparent.

Other nodes carry a duplicate of this Inspector Settings tab as well. Full descriptions of these shared controls appear at this chapter’s end under “The Common Controls.”

### User Defined Metadata Variables in Paths, Expressions, and Scripts

Fusion has gained a new variables system. The feature extends Fusion’s already capable scripting layer and makes it more flexible still. There are three sides to it. 1 Setting it up in the Fusion Preferences. 2 Putting variables to work inside Expressions. 3 Putting variables to work in Saver paths.

### Getting started

A fresh category, Variables Map, now sits in preferences. You’ll find it under Global and Comp Preferences. You can author and edit variables globally, covering every comp, or on a per‑comp basis. They’re also allowed to hold expressions and to reference other variables.

### The Fusion Variables Map preference

Within an expression, Global Variables are reachable through fu.vars.[variable name] and Comp Variables through comp.vars.[variable name] in expressions. Both Global and Comp variables can be used in a Saver to build a save location or a file name. Inside a Saver’s Filename control, type %{name}. That call pulls up the list of categories on offer — among them custom variables (drawn from Prefs), clip metadata, and Resolve metadata (over on the Fusion Page). In a Saver, Input Metadata variables take the form %{metadata.metadataname}, while Resolve variables take the form %{resolve:Resolve Metadata}

Using a mapped variable in a text field. Within expressions, metadata coming from an upstream clip is reachable with fu.vars.metadata. [name] or comp.vars.metadata.[name] On top of that, on the Fusion Page you can pull metadata from Resolve inside an expression using fu.vars.resolve[“Name”]. Example fu.vars.resolve[“Timeline Name”].

### Improved Lens Distort Tool

Checkerboard calibration has been added to the Lens Distort tool, and the tool can now run with GPU acceleration.
