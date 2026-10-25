# Day sky and fast noise

Version: DaVinci Resolve 20.3 Reference Manual. Context: Day sky, Fast noise.
[Chapter index](INDEX.md) / [Previous section](background-color-tab.md) / [Next section](mandelbrot-and-multitext.md)
<a id="source-advanced-tab"></a> <a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-color-tab-1"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab"></a> <a id="source-day-sky-advance-tab-controls"></a> <a id="source-day-sky-controls"></a> <a id="source-day-sky-ds"></a> <a id="source-day-sky-node-introduction"></a> <a id="source-fast-noise-controls"></a> <a id="source-fast-noise-fn"></a> <a id="source-fast-noise-node-color-tab"></a> <a id="source-fast-noise-node-introduction"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-noise-tab"></a> <a id="source-the-day-sky-node"></a> <a id="source-the-fast-noise-node"></a>

### Day Sky [DS]

### The Day Sky node

### Day Sky Node Introduction

What the Day Sky node sets out to do is simulate the daylight occurring at a given time and place on earth, outputting a high dynamic range image that maps that light. It does not generate a sky on its own, though pairing it with a cloud generator or Noise node would let you build one. NOTE: This generator puts into practice the research paper A Practical Analytical Model for Daylight, authored by Preetham, Shirley, and Smits. You can find a copy of that original paper on the Visual Simulation Group's website at the University of Utah [https://www.cs.utah.edu].

### Inputs

The Day Sky node has just one input, for an effect mask that restricts where the day sky simulation gets applied. Effect Mask: This optional blue effect mask input takes a mask shape made from polylines, simple primitive shapes, paint strokes, or bitmaps brought in from other tools. Hook a mask up here and the Day Sky is held to just the pixels lying inside that mask.

### Basic Node Setup

Being a generator, the Day Sky node usually opens a branch in a node tree and feeds into another node, such as a Merge node.

### Inspector

A Day Sky connected as the background to a Merge node

### Day Sky controls

### Controls Tab

You set the location and time of the daylight simulation from the Controls tab, which in turn drives the overall look that emerges.

Location You name the location behind the Day Sky simulation with the Latitude and Longitude sliders. Date and Time You pick the exact moment for the Day Sky simulation through the Day, Month, and Time controls. Turbidity Turbidity makes light scatter and get absorbed within the simulation rather than traveling in straight lines. Raising the turbidity lends the sky simulation a murky quality, as though smoke or atmospheric haze hung in the air. Do Tone Mapping Because the simulation runs in 32-bit floating-point color space, it puts out color values far above 1.0 and far below 0.0. Tone mapping is the step that takes the simulation's full dynamic range and squeezes it into your target exposure range, all while trying to hold onto as much highlight and shadow detail as it can. Clear this checkbox to switch off any tone mapping on the simulation. As a rule, leave it cleared only when the resulting image will be color corrected afterward inside a floating-point color pipeline. Exposure Turn to this control to choose the exposure that tone mapping uses.

### Day sky Advance tab controls

### Advanced Tab

More targeted controls over the brightness and width of the various ranges within the produced sky live on the Advanced tad. Horizon Brightness Reach for this control to tune the horizon's brightness against the sky. Luminance Gradient Reach for this control to tune how wide the gradient is that divides the horizon from the sky.

Circumsolar Region Intensity Reach for this control to tune the intensity or brightness of the sky closest to the sun. Circumsolar Region Width Reach for this control to tune the width or extent of the sky region the sun affects. Backscattered Light Reach for this control to raise or lower the backscatter light within the simulation.

### Common Controls

Image and Settings Tabs A great many Generator nodes carry the very same Image and Settings tabs in the Inspector. Full descriptions of these shared controls appear later, in the “The Common Controls” section that closes this chapter.

### Fast Noise [FN]

### The Fast Noise node

### Fast Noise Node Introduction

As a Perlin Noise generator, the Fast Noise node is both quick and adaptable. It lends itself to a broad span of effects — clouds, drifting fog, waves, water caustics, stylized fire and smoke, plus other organic textures. It also serves brilliantly as a noise feed for further effects like heat shimmers, particle systems, and dirtiness maps.

### Inputs

By way of the Fast Noise node's two map inputs, you can deploy masks to steer the noise detail and brightness control values on a per-pixel basis. These two optional inputs open the door to some intriguing, inventive effects. A standard effect mask input is present as well, used to bound the Fast Noise size. Noise Detail Map: Feed a soft-edged mask into the gray Noise Detail Map input and you get a flat noise map (zero detail) wherever the mask reads black, full detail wherever it reads white, and a smooth taper of detail at the values in between. It takes effect ahead of any gradient color mapping. This proves handy when you want peak noise detail concentrated in one spot, easing off gently everywhere else. Noise Brightness Map: Wire a mask to this white input to take full command of the noise map — lifting it in select regions, fusing it with other textures, or, when Detail sits at 0, swapping out the Perlin Noise map entirely. Effect Mask: Into this optional blue effect mask input goes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Attach a mask here and the Fast Noise is confined to only the pixels within that mask.

### Basic Node Setup

You call on the Fast Noise node to produce images that downstream nodes can put to work. In the example below, for instance, it supplies the bitmap feeding a Particle Emitter. A Fast Noise node serving as the bitmap origin driving a Particle Emitter Inspector

### Fast Noise controls

### Noise Tab

The Fast Noise node's noise shape and pattern are governed from the Noise tab. Discontinuous Ordinarily the noise function interpolates across values to yield a smooth, unbroken gradient of results. Tick this checkbox to carve hard discontinuity lines along some of the noise contours, which produces a strikingly different look. Inverted Tick this checkbox to flip the noise, turning out a negative of the original pattern. It works best with Discontinuous switched on too. Center Pan and reposition the noise pattern through the Center coordinate control. Detail Push this slider up to draw out finer detail in the noise result. Bigger values stack on more layers of ever-finer noise without disturbing the broad pattern. High values render more slowly yet can deliver a more natural outcome.

Brightness Ahead of any gradient color mapping, this control tunes the noise map's overall brightness. Under Gradient mode it behaves much like the Offset control. Contrast This control raises or lowers the noise map's overall contrast before any gradient color mapping kicks in. It can heighten the noise's impact and broaden the spread of colors used in Gradient mode. Lock and Scale X/Y You resize the noise map via the Scale slider, dialing it from soft variations spread across the whole image to a tighter, denser texture. Ticking the Lock X/Y checkbox just above splits the Scale slider into separate X- and Y-axis scale sliders, which comes in handy for a brushed-metal look. Angle Spin the noise pattern with the Angle control. Seethe Nudge this thumbwheel control to interpolate the noise map toward a different noise map, producing a creeping shift in the noise as though it were drifting or flowing. You must animate this control for the gradient to evolve over time, or instead lean on the Seethe Rate control below. Seethe Rate Like the Seethe control above, the Seethe Rate likewise drives the noise map to evolve and shift. The Seethe Rate fixes how fast the noise changes from frame to frame, automatically generating an animated drift without any need for spline animation.

### Fast Noise node Color tab

### Color Tab

From the Color tab you tune the gradient colors that paint the produced noise pattern.

Two Color A plain two-color gradient colors the noise map, with the noise function easing smoothly from the first color across to the second. Gradient Fusion's Advanced Gradient control hands you finer command over the color gradient applied to the noise map.

### Common Controls

Image and Settings Tabs Numerous Generator nodes share identical Image and Settings tabs within the Inspector. These shared controls get their full write-up toward the chapter's end, under “The Common Controls.”
