# Grain and light trim and remove noise and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grain, Light trim, Remove noise, Common controls.
[Chapter index](INDEX.md) / [Previous section](film-grain-and-grain.md) / [Next section](common-controls-common-film-settings-inspector.md) / [Continue The Common Controls / Settings Tab](common-controls-common-film-settings-inspector.md) / [Grain Grn](film-grain-and-grain.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-chroma-method-controls"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-controls-tab-3"></a> <a id="source-controls-tab-4"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector-2"></a> <a id="source-light-trim-controls"></a> <a id="source-light-trim-lt"></a> <a id="source-light-trim-node-introduction"></a> <a id="source-remove-noise-controls"></a> <a id="source-remove-noise-node-introduction"></a> <a id="source-remove-noise-rn"></a> <a id="source-setting-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-light-trim-node"></a> <a id="source-the-remove-noise-node"></a>

### Common Controls

### Setting Tab

Since the Settings tab controls show up the same way on every Film node, you will find each one explained in the chapter's closing “The Common Controls” section.

### Light Trim [LT]

### The Light Trim node

### Light Trim Node Introduction

What this node reproduces is the light trims of a film scanner. It is built to perform best on logarithmic data, the kind held in Cineon, Arri, or Blackmagic RAW files. Hand the Light Trim node logarithmic data and you can use it to raise or lower the image's apparent exposure level.

### Inputs

You get two Inputs here: the Light Trim node devotes one to the 2D image while reserving the other for the effects mask. Input: Feed the primary Log 2D image whose exposure needs tweaking into the orange input. Effect Mask: A mask shape goes into the blue input, built from polylines, simple primitive shapes, paint strokes, or bitmaps imported from other tools. Wiring a mask here holds the exposure change to only the pixels under the mask. As usual, the tool runs its processing before the effects mask is applied.

### Basic Node Setup

Set the Light Trim node downstream of a LOG clip, yet upstream of wherever a Cineon LOG node converts that Log clip.

A Light Trim node tuning the exposure of a LOG clip

### Inspector

### Light Trim controls

### Controls Tab

A lone slider in the Controls tab handles the image's exposure. Lock RGBA Enabling the Lock RGBA control folds every image channel under a single slider; it ships turned on. Clear this checkbox whenever you need to drive the individual color channels on their own. Trim This slider moves the color in terms of film, optical printing, and lab printing points, where 8 points equals one stop of exposure.

### Common Controls

Settings Tab Every Film node carries the same Settings tab controls, which is why a single description of them lives in the “The Common Controls” section wrapping up this chapter.

### Remove Noise [RN]

### The Remove Noise node

### Remove Noise Node Introduction

For straightforward noise control, reach for the Remove Noise node. Under the hood it blurs the image channels and then weighs that blurred version against the original to isolate the noise. Afterward it sharpens the image everywhere except the spots where noise turned up. In practice, display the image and study the red channel, then push Red Softness up until the grain looks gone. Now raise the sharpness until detail returns, halting just before the grain creeps back. Carry out the same steps for the green and blue channels.

### Inputs

A pair of inputs sits on the Remove Noise node, one handling the 2D image and one handling the effects mask. Input: The orange input receives the primary 2D image that is to have its noise stripped. Effect Mask: Into the blue input goes a mask shape, made from polylines, basic primitive shapes, paint strokes, or bitmaps drawn from other tools. Connecting a mask there pins the noise-removal change to nothing beyond the mask's pixels. The effects mask kicks in only once the tool itself has finished processing.

### Basic Node Setup

Any noisy clip is fair game for the Remove Noise node. In the example below, for instance, it clears noise ahead of keying the clip with the DeltaKeyer.

A Remove Noise node clearing noise ahead of a keying pass Inspector

### Remove Noise controls

### Controls Tab

From the Controls tab you flip the noise removal between its two methods, Color and Chroma. Pick Color and the Controls tab lets you tune blur and sharpness separately on each RGB channel. Pick Chroma and blur and sharpness are governed instead through the Luma and Chroma controls. Method This menu decides whether the node handles color via the Color method or the Chroma method, and your pick also swaps in a different set of control sliders.

Lock Ticking this checkbox ties each channel's Softness and Detail sliders to one another. Softness Red, Green, and Blue These Softness sliders fix how much blur each channel of the image receives; switch to Chroma mode and they turn into softness sliders for the Luminance channel and the Chrominance channel. Detail Red, Green, and Blue These Sharpness sliders fix how much detail is restored to a channel after it has been softened, and under Chroma mode they become a Luminance slider and a Chrominance slider.

### Chroma Method controls

### Common Controls

Settings Tab Across all Film nodes the Settings tab controls stay the same, so you will read about them in the “The Common Controls” section that comes next.

### The Common Controls

A set of matching Inspector controls is shared across the Film nodes, and this section walks through those controls the Film nodes hold in common.
