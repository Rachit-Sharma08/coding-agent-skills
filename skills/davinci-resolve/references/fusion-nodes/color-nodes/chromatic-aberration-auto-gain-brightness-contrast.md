# Chromatic aberration removal and auto gain and brightness contrast

Version: DaVinci Resolve 20.3 Reference Manual. Context: Chromatic aberration removal, Auto gain, Brightness contrast.
[Chapter index](INDEX.md) / [Previous section](chromatic-aberration-removal-controls.md) / [Next section](brightness-contrast-and-channel-booleans.md) / [Chromatic Aberration Removal CAR](chromatic-aberration-removal-controls.md)
<a id="source-auto-gain-ag"></a> <a id="source-auto-gain-controls"></a> <a id="source-auto-gain-node-introduction"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-brightness-contrast-bc"></a> <a id="source-brightness-contrast-node-introduction"></a> <a id="source-brightness-control-controls"></a> <a id="source-color"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-example"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-the-auto-gain-node"></a> <a id="source-the-brightness-contrast-node"></a>

### Common Controls

Settings Tab The Inspector's Settings tab is repeated across the other Color nodes as well. Full coverage of these shared controls appears at this chapter's end, within the “The Common Controls” section.

### Color

A grouping nested under Fusion's Color tools that opens up an assortment of color-processing utilities.

### Auto Gain [AG]

### The Auto Gain node

### Auto Gain Node Introduction

On its own, the Auto Gain node remaps an image's tonal range, driving the darkest and brightest pixels to values you specify. Out of the box, the darkest pixels are sent to black, the brightest to white, and everything between is stretched so the tonal range fills evenly. It comes in handy for evening out lighting differences, working with low-contrast footage, or previewing the entire color range of float images (though the viewer's View Normalized Image option usually serves that purpose better).

### Inputs

A pair of inputs sit on the Auto Gain node, the input and the effect mask. Input: The orange input takes the main 2D picture that the auto gain works on. Effect Mask: The blue input expects a mask shape built from polylines, simple primitive forms, paint strokes, or bitmaps originating in other tools. Wiring a mask here keeps the auto gain adjustment to just the pixels lying inside that mask. The effect mask is applied to the tool once the tool has finished processing.

### Basic Node Setup

Much as with many 2D image-processing nodes, the Auto Gain node is fed a 2D image from something like a Loader node or the MediaIn1 pictured below. From its output, the node tree carries on into a further 2D image-processing node or a Merge node.

An Auto Gain node applied to a MediaIn1 node

### Inspector

### Auto Gain controls

### Controls Tab

Within the Controls tab live the handful of main controls you need to tailor the AutoGain operation. NOTE: As the input image shifts over time, the levels of the result shift along with it. Say a bright object exits an otherwise dark shot: the scene that's left abruptly brightens, since the remaining darker values get stretched toward white. The same holds for abrupt depth shifts whenever Do Z is in play; objects already present can be pushed nearer or farther as a close or distant object enters or exits the scene. Do Z Tick the Do Z checkbox to extend the Auto Gain effect onto the Z or Depth channels. This proves useful for aligning the ranges of one Z-channel with another, or for inspecting a float Z-channel within the RGB values. Range The Range control fixes the image's black point and white point. Every tonal value in the image is rescaled to sit inside that range.

### Example

Build a horizontal gradient using the Background node. Make one color dark gray (RGB Values 0.2). Make the other color light gray (RGB Values 0.8). Drop in an Auto Gain node and put the Low value at 0.0 and the High value at 0.5. As a result, the brightest pixels are dropped to 0.5 while the darkest pixels are driven to black. Everything else among the pixel values scales between those two bounds.

### Common Controls

Settings Tab This same Inspector Settings tab recurs on the other Color nodes too. A thorough walkthrough of these shared controls sits at the end of this chapter, within the “The Common Controls” section.

### Brightness Contrast [BC]

### The Brightness Contrast node

### Brightness Contrast Node Introduction

The Brightness Contrast node tweaks an image's gain, brightness, contrast, gamma, and saturation. How the controls are laid out reflects the sequence in which their operations run. To illustrate, gamma runs ahead of contrast yet behind gain. Brightness Contrast can also be undone via the Forward and Reverse buttons, so a color correction already applied can be rolled back later down the chain. For the best outcome here, image processing ought to run in 32-bit floating point.

### Inputs

A pair of inputs sit on the Brightness Contrast node, the input and the effect mask. Input: The orange input takes the main 2D picture that the brightness contrast works on. Effect Mask: The blue input expects a mask shape drawn from polylines, simple primitive forms, paint strokes, or bitmaps coming out of other tools. Wiring a mask here keeps the Brightness Contrast adjustment to just the pixels lying inside that mask. The effect mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

As with so many 2D image-processing nodes, the Brightness Contrast node is handed a 2D image from a source such as a Loader node or the MediaIn1 shown below. Its output extends the node tree onward into another 2D image-processing node or a Merge node.

A Brightness Contrast node applied to a MediaIn1 node

### Inspector

### Brightness Control controls

### Controls Tab

Inside the Controls tab you'll find every main control needed to tailor the brightness and contrast operations. Color Channels (RGBA) By default the filter works across the R, G, B, and A channels. To filter channels selectively, click each channel button to toggle it on or off. NOTE: Do not confuse this with the RGBA checkboxes sitting under the common controls. Because the node weighs these picks before it processes the image, switching a channel off makes the node bypass that channel during processing, which speeds up rendering the effect. By contrast, the channel controls on the Common Controls tab take hold after the node has done its processing. Gain The gain slider multiplies the pixel value. A Gain of 1.2 turns a pixel reading R0.5 G0.5 B0.4 into R0.6 G0.6, B0.48 (i.e., 0.4 \* 1.2 = 0.48) and leaves black pixels untouched. Since Gain bites harder on higher values than on lower ones, its impact peaks across the image's midrange and upper range. Lift Where Gain pivots the color values about black, Lift pivots them about white. Each pixel value is multiplied by this control's setting. A Lift of 0.5 turns a pixel reading R0.0 G0.0 B0.0 into R0.5 G0.5, B0.5 and leaves white pixels untouched. Since Lift bites harder on lower values than on higher ones, its impact peaks across the image's midrange and lower range. Gamma Settings above 1.0 lift the Gamma (mid-gray), while settings below it pull Gamma down. This node's behavior is non-linear, and the existing black or white points stay completely untouched. Pure gray tones feel it the most.

Contrast Contrast measures the spread between the bright and dark regions. Raising this slider boosts the contrast, driving color out of the midrange toward black and white. Lowering it draws the image's colors back in toward midrange, narrowing the gap between its darkest and brightest pixels. Brightness Whatever the Brightness slider reads is added onto the value of every pixel in the image. This control acts linearly on an image, so it hits all pixels the same way no matter their value. Saturation Reach for this control to raise or lower how much Saturation the image carries. A saturation of 0 strips all color, leaving a grayscale image. Low and High In certain ways this range control resembles the Gain control. Pinning Low at 0.0 and trimming the High value down from 1.0 produces the same outcome as raising the gain. High values are multiplied by the reciprocal of the high value. (e.g., a high of 0.75 means each pixel is multiplied by 1/0.75, or 1.3333). Keeping the high pinned at 1.0 while lifting the low amounts to inverting the image colors, raising the gain, then inverting once more. That shoves more of the image toward black while leaving the whites entirely alone. Direction Forward runs all values as normal. Reverse essentially flips every value. Clip Black/White The Clip Black and Clip White checkboxes trim off out-of-range color values that can crop up in an image while processing at floating-point color depth. Out-of-range colors fall under black (0.0) or over white (1.0). These checkboxes do nothing on images processed at 8-bit or 16-bit per channel, since such images can't hold out-of-range values. Pre-Divide/Post-Multiply Ticking the Pre-Divide/Post-Multiply checkbox divides the image's pixel values by the Alpha values ahead of the color correction, then multiplies them by the Alpha value again afterward. This guards against producing illegally additive images when you color correct material with premultiplied Alpha channels.
