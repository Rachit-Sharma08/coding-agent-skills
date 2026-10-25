# Color curves and color gain

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color curves, Color gain.
[Chapter index](INDEX.md) / [Previous section](color-corrector-correction-tab-histogram-menu.md) / [Next section](color-gain-gain-tab.md) / [Continue Color Gain Clr / Gain Tab](color-gain-gain-tab.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-color-curves-ccv"></a> <a id="source-color-curves-controls"></a> <a id="source-color-curves-node-introduction"></a> <a id="source-color-gain-clr"></a> <a id="source-color-gain-node-introduction"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-the-color-curves-node"></a> <a id="source-the-color-gain-node"></a>

### Color Curves [CCv]

### The Color Curves node

### Color Curves Node Introduction

For carrying out Lookup table (LUT) color manipulations, the Color Curves node is a spline-driven node. Every color channel gets its own separate spline. You can animate or dissolve the effect, and it can be brought to the image through the RGB, YUV, YIQ, CMY, or HLS color spaces.

You can scale the Color Corrector's LUT view with the + and - keys on the numeric keypad. The color curves LUT has full support for out-of-range values—that is, pixels whose color values run above 1.0 or below 0.0. Should you need finer precision while adjusting the controls, the splines on show in this LUT view can also be reached from the Spline Editor.

### Inputs

Three inputs come with the Color Curves node in the Node Editor. Input: Standing as the lone mandatory connection, this orange input. It feeds in a 2D image that the color curves act upon. Effect Mask: The optional effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the color curves adjustment to just the pixels falling inside the mask. An effect mask gets applied to the tool once it has been processed. Reference Image: The optional green input serves to connect a second 2D image usable for reference matching. Match Mask: This optional white input takes any mask, much as an effect mask does. This mask, though, marks out the area to match during a Match. Shape-wise it gives you more leeway than the Inspector's built-in Match reference rectangle.

### Basic Node Setup

Like a great many 2D image-processing nodes, the Color Curves node takes in a 2D image such as a Loader node or the MediaIn1 pictured below. Its output carries the node tree onward by wiring into a further 2D image-processing node or a Merge node.

### Inspector

A Color Curves node applied to a MediaIn1 node

### Color Curves controls

### Controls Tab

Two sections split up the color curves' Controls tab. Up in the Inspector's top half live the curves and LUT controls. The lower half is given over mainly to matching the reference image. Mode The Mode choices switch among Animated and Dissolve modes. No Animation is the default mode, where curve adjustments stay static. Setting the mode hands each channel a change spline, so the color curve can be animated across time. Dissolve mode is for all intents obsolete and ships purely for compatibility's sake. Color Space The LUT view's splines stand for color channels drawn from an assortment of color spaces. Red, Green, and Blue is the default. This menu's choices let a different color space be picked. Below is a thorough rundown of the color spaces on offer here:

- RGB (Red, Green, Blue): Working in the RGB color space, Fusion has most of its nodes and displays read an image's primary channels as Red, Green, and Blue.
- YUV (Luma, Blue Chroma, and Red Chroma): PAL video's analog broadcast relies on the YUV color space. In years past this format saw frequent use for color correcting images, owing to how familiar it was to a great many video engineers. Each pixel gets spelled out by its Luminance, Blue Chroma, and Red Chroma components.
- HLS (Hue, Luminance, and Saturation): Within the HLS color space, every pixel gets spelled out by its Hue, Luminance, and Saturation components.
- YIQ (Luma, In Phase, and Quadrature): NTSC video's analog broadcast relies on the YIQ color space. Far scarcer than YUV, this format is almost never met with in production. Each pixel gets spelled out by its Luminance, Chroma (the in-phase or red-cyan channel) and Quadrature (magenta-green) components.
- CMY (Cyan, Magenta, and Yellow): More usual in print though it is, the CMY format turns up often in computer graphics out of other software packages. Each pixel gets spelled out by its Cyan, Magenta, and Yellow components. CMY is nonlinear.

Color Channels (RGBA) The Color Channel controls let you choose which channel's spline is open for editing right now. These controls' labels shift to mirror the channel names belonging to the current color space. As a rule they read as Red, Green, and Blue. Should the Color Curves node be running in YUV color space, they read as Y, U, and V instead. These controls don't pen the node's effect to one particular channel. All they pick is whether that channel's spline can be edited. Most often you reach for these controls to make certain that adding or shifting points on one channel's spline doesn't accidentally disturb a different channel's spline. Spline Window A conventional curve editor for each RGBA channel is what the Spline Window shows. Depending on which color channels you've selected above, these splines can be edited one by one or together as a set. The spline starts off as a linear range, running from 0 in/0 out down at the bottom left up to 1 in/1 out at the top right. At that default, a color comes out at the same value as the output. Drop a point into the middle at 0.5 in/0.5 out and lift it, and you brighten the image's mid color. The spline curves grant fine command over color ranges, so targeted tweaks can land without disturbing other color values.

In and Out The In and Out controls let you fine-tune a chosen point's exact values. To alter a value, pick a point and key in the in/out values you want. Eyedropper (Pick) Click the Eyedropper icon—also known as the Pick button—and grab a color off an image in the display to have control points set automatically on the spline for the chosen color. Drawn with a triangular shape, the new points can shift only up and down (where a point is locked, only its Out value can change). Points land solely on enabled splines. To drop points on just one channel, switch the other channels off before you make the pick. White balancing an image is one place this technique pays off. Reach for the Pick control to grab a pixel from the image that ought to read as pure gray. Tune the points that turn up so the Out value is 0.5, recoloring the pixels gray. Use the contextual menu's Locked Pick Points option to free points made with the Pick option, turning them into ordinary points. Reference Inside the Reference section sit controls that manage matching to sample patches of the connected reference image.

- Match Reference: The Match Reference button drops points onto the curve to match an image wired into the green reference image input. How many points get used to match the image rides on the Number of Samples slider underneath.
- Sample Reference: A click of the Sample Reference button samples the background image's center scanline and builds a LUT out of its color values. How many points get used to match the sampled scanline rides on the Number of Samples slider underneath.
- Number of Samples: How many points serve to match the curve against the range within the reference image is set by this slider.
- Show Match Rectangle: Tick this checkbox to put a rectangle in the viewer marking the patch of the reference image drawn on during the match process. The match rectangle bears only on the outcome of the Match Reference operation. The Sample reference always runs off the image's center scaling.
- Match Center: Repositioning the match rectangle to sample a different patch when matching is what the X and Y parameters let you do.
- Match Width: Width controls the width of the match rectangle.
- Match Height: Heigh controls the height of the match rectangle.
- Pre-Divide/Post-Multiply: Ticking this checkbox has the image's pixel values divided

by the Alpha values ahead of the color correction, then re-multiplied by the Alpha value afterward. This helps head off illegally additive images, especially around the fringes of a blue/green key or while handling 3D-rendered objects.

### Common Controls

Settings Tab The Inspector's Settings tab shows up in other Color nodes as well. These shared controls get a thorough write-up at this chapter's close, in the "The Common Controls" section.

### Color Gain [Clr]

### The Color Gain node

### Color Gain Node Introduction

Within the Color Gain node sit options for tuning the image's gain, gamma, saturation, and hue. Plenty of the controls the Color Gain node hands you also turn up in the Color Corrector node, yet this plainer node may render faster. What sets the Color Gain node apart from the Color Corrector is its balance tab controls. With them you can adjust how the colors get tinted across the highs, mids, and lows.

### Inputs

Two inputs come with the Color Gain node: one feeding the main image and the other an effect mask. Input: Standing as the lone mandatory connection, this orange input. It feeds in a 2D image that the color gain acts upon. Effect Mask: The optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the color gain adjustment to just the pixels falling inside the mask. An effect mask gets applied to the tool once it has been processed.

### Basic Node Setup

Like a great many 2D image-processing nodes, the Color Gain node takes in a 2D image such as a Loader node or the MediaIn1 pictured below. Its output carries the node tree onward by wiring into a further 2D-image processing node or a Merge node.

A Color Gain node applied to a MediaIn1 node
