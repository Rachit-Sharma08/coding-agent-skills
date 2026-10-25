# Color corrector correction tab histogram menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color corrector.
[Chapter index](INDEX.md) / [Previous section](color-corrector-correction-tab-colors-menu.md) / [Next section](color-curves-and-color-gain.md) / [Color Corrector CC](color-corrector-correction-tab-colors-menu.md)
<a id="source-color-correction-in-histogram-mode"></a> <a id="source-color-corrector-controls"></a> <a id="source-color-corrector-luminance-controls"></a> <a id="source-color-corrector-suppression-controls"></a> <a id="source-common-controls"></a> <a id="source-correction-tab-histogram-menu"></a> <a id="source-correction-tab-suppress-menu"></a> <a id="source-options-tab"></a> <a id="source-ranges-tab"></a>

### Correction Tab Histogram Menu

With the menu switched to Histogram, the input image gets rendered as a histogram display. Supply a reference image as well and its histogram shows up too. This tab's controls mostly serve to match one image against another, drawing on either the Equalize or the Match modes of the Color Corrector. Channel With this menu you choose and view the histogram for any single color channel or for the Master channel.

### Color Correction in Histogram mode

Histogram Display Think of a histogram as a graph showing how color values are spread across the scene. You read it left to right, the values farthest left standing for the scene's deepest darks and the values farthest right for its brightest tones. Wherever more of an image's pixels share the same or a close value, that part of the graph climbs higher. Because luminance gets computed channel by channel, the red, green, and blue channels each carry their own histogram, and stacking them together yields the Master Histogram. To stretch the histogram up and down, set the mouse pointer within the control and drag it upward to zoom in or downward to zoom out. Display Selector Toolbar Sitting atop the histogram, the Display Selector toolbar gives you a way to switch parts of the histogram readout on and off. Rest the mouse pointer on a button and a tooltip pops up explaining what that button does.

- Input Histogram: Turns the readout of the input image's histogram on or off.
- Reference Histogram: Turns the readout of the reference image's histogram on or off.
- Output Histogram: Turns on or off the readout for the histogram of the post-colorcorrected image.
- Corrective Curve: Toggles a spline whose job is to make plain exactly how the auto color

corrections applied using a reference image are affecting the image. That comes in handy while you're evening out luminance across the input and the reference images. Float Images and Histogram Equalization or Matching Running the Histogram Match or Equalize methods on a float image converts the output image's color depth to 16-bit integer. Since two-dimensional histograms cope poorly with the wide dynamic range that float images carry, these operations always fall back to 16-bit integer processing.

Histogram Type Every one of these menu choices triggers a distinct kind of color correction operation.

- Keep: Keep leaves the image untouched, with the reference histogram disregarded.
- Equalize: Picking Equalize tweaks the source image so that every color value within it is

equally represented—which amounts to leveling the histogram so the image's spread of colors grows more uniform.

- Match: The Match mode reshapes the source image off the reference image's histogram. Its job is making two shots whose lighting and exposure differ end up looking alike.

Once chosen, the Equalize and Match modes expose the controls below.

- Match/Equalize Luminance: How hard the Color Corrector node leans on the image's luminance distribution is governed by this slider. At zero (the default), matching and equalization hit each color channel on its own, leaving luminance—the three color channels combined—alone. Give this control a positive value while equalizing and the input image's luminance distribution gets flattened ahead of any color equalization. Give it a positive value with the correction mode on Match and the input's luminance values are matched to the reference before any correction touches the R, G, and B channels. The Luminance and RGB controls can stack their effects, and as a rule you don't crank both to full (1.0) at once.
- Lock R/G/B: Tick this checkbox and color matching hits every color channel uniformly. Leave it unticked and a separate set of controls appears for each channel.

Equalize/Match R/G/B Whether you've gone with Equalize or Match mode decides what this control gets named. Use the slider to dial back how strongly the image is corrected for equalizing or matching. Set it to 1.0 and the Equalize or Match runs at full strength, while lower settings temper the outcome. Precision The color fidelity used while sampling the image to build the histogram is set by this menu. 10-bit yields better fidelity than 8-bit, and 16-bit yields better fidelity than 10-bit. Smooth Correction Color equalization and matching jobs frequently bring on posterization, which happens because the image's gradients get stretched or squeezed until the dynamic range between colors falls short of showing a clean transition. This control can soften the correction curve, mixing a portion of the original histogram back into the result so the transition comes out smoother. Snapshot Match Time A click of this button freezes a snapshot of the current reference histogram, banking its present state in memory. Skip snapshotting the reference histogram and it refreshes frame by frame. That can produce flickering and phasing in the correction as the node strains to match a shifting source against a shifting reference.

Release Match A click of this button drops the histogram's current snapshot and goes back to the live reference input. Reset All Histogram Changes Pressing this button wipes out every change made to the histogram, restoring the controls to their defaults and putting the mode back on Keep.

### Correction Tab Suppress Menu

Color Suppression gives you a way to strip an unwanted color element out of the image. Its Color Wheel control resembles the one in the node's Colors section, except this one is ringed by six controls, each standing for one particular color around the wheel. To knock back a color within the chosen range, drag the control for that color in toward the wheel's middle. The nearer that control sits to the center, the harder that color gets suppressed from the image.

### Color Corrector Suppression controls

Suppression Angle The Suppression Angle control spins the controls around the suppression wheel so you can home in on one specific color. Reset All Suppression A click of this control returns the suppression colors to 1.0, their default value.

### Ranges Tab

Within the Ranges tab sit the controls that define which of an image's pixels count as shadows and which count as highlights. The midrange is always worked out as whatever pixels aren't already swept into the shadows or the highlights.

### Color Corrector Luminance controls

Range Use this menu to pick which tonal range the viewers display. They make the pixels in the range easier to see. Choose the Result menu option and the color corrector shows the color corrected image in the viewers. That's the default. Pick any of the other menu options and the display flips to a grayscale image marking which pixels belong to the chosen range. White pixels stand for those counted as inside the range, and black pixels fall outside it. Picking Shadows, for example, would paint pixels deemed shadows white and pixels that aren't shadows black. Mid gray pixels sit only partway inside the range and won't catch the full force of any color tweaks aimed at that range. Channel This tab's Channel menu lets you inspect the range of one particular color channel. Out of the box, Fusion shows the luminance channel whenever the color ranges get examined. Spline Display You select the ranges by working the spline handles. Four spline points exist, each carrying one Bézier handle. The pair up top mark where the shadow and highlight ranges begin, while the pair at the bottom mark where the range ends. The Bézier handles let you steer the falloff. The midtones range gets no dedicated controls, since its span is read as the gap separating the shadow range from the highlight one. Below the spline display, the X and Y text controls let you key in exact coordinates for whichever Bézier point or handle you've chosen. Output the Range You See Now as Final Render Tick this checkbox and the monochrome range shown in the viewers gets sent out as the final render. As a rule the Color node puts out the full RGBA image even when it's been left displaying one of the color ranges in the view. This control opens the door to using the Color Corrector node to build a range's matte for use as an effect mask elsewhere. Preset Simple/Smooth Ranges These two buttons let you reset the spline ranges to either Smooth (default) or Simple (linear) settings.

### Options Tab

The Options tab holds a handful of weighty processing operations, among them a tidy fix for color correcting premultiplied Alpha channels.

### Color Corrector controls

Pre-Divide/Post-Multiply Choosing this option divides the color channels by the Alpha value ahead of the color correction. Once the color correction is done, the color values get re-multiplied by the Alpha to yield a correctly additive image. That matters a great deal during an additive merge or when handling CG images built with premultiplied Alpha channels. Histogram Proxy Scale How precise the creating and calculating of histograms is gets decided by the Histogram Proxy Scale. Lower settings mean greater precision, while higher ones turn out a coarser, more general histogram. Process Order This menu lets you decide whether tweaks to the image's gamma take effect before or after any edits to the image's levels.

### Common Controls

Settings Tab The Inspector's Settings tab shows up in other Color nodes as well. These shared controls get a thorough write-up at this chapter's close, in the "The Common Controls" section.
