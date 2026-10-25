# Dissolve node inputs and controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dissolve.
[Chapter index](INDEX.md) / [Next section](merge-node-inputs-and-composite-operators.md)
<a id="source-a-typical-dissolve-node-structure-in-fusion"></a> <a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-composite-nodes"></a> <a id="source-composite-nodes-part-1"></a> <a id="source-controls-tab"></a> <a id="source-dissolve-controls"></a> <a id="source-dissolve-dx"></a> <a id="source-dissolve-node-introduction"></a> <a id="source-gradientsmpte-wipe-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-resolution-handling"></a> <a id="source-the-dissolve-node"></a>

### Composite Nodes

This section covers the Dissolve and Merge nodes that Fusion offers.

Each node name is paired with an abbreviation; you can type these into the Select Tool dialog while hunting for tools and reference them when scripting. Throughout this document, treat node graphs that display MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a difference is called out.

### Dissolve [DX]

### The Dissolve node

### Dissolve Node Introduction

Most often the Dissolve node blends a pair of images so that one clip eases gradually into another. The blend ratio between foreground and background is governed by a Background/Foreground slider. Such dissolves are a staple of editing, letting you cross from one shot to the next. That said, pushing the Background/Foreground slider hard to either end lets you flip between inputs instead. The Dissolve node breaks from Fusion convention in that no image needs to be wired into the background; whichever of the two — background or foreground — gets output depends on where the Background/Foreground slider sits. Because of this trait, you can repurpose the Dissolve node as an automatic layer-switcher whenever it is fed background and foreground clips of unequal length. Wire each clip to its respective background and foreground input, then push the Background/Foreground slider toward the shorter clip to decide which one sits “on top.” Once that clip plays past its final frame, the Dissolve node hands off automatically to whatever is wired to the remaining input. Beyond the ordinary dissolve, choosing Gradient Wipe from the Operation menu lets you build freeform animated dissolve patterns driven by the luminance of an image fed into the optional Gradient Wipe input. Feed it anything — geometric shapes, assorted gradients, footage of fire, rippling water, or rain, the Fast Noise node, or particle systems built right on the Fusion page — to author all sorts of original transitions. Layering soft-edged effect masks on top widens the range of looks even further. In the end, keyframing the Background/Foreground control gives you authority over the transition that carries you from the foreground input across to the background, or the reverse.

### Inputs

Three optional image inputs are offered by the Dissolve node: Background: One of the two images you intend to mix or flip between. Contrary to how most nodes behave, you needn't wire the background input ahead of the foreground input. Foreground: The other of the two images you intend to mix or flip between. Results are best when the foreground and background inputs both receive images at matching resolution. Gradient Map: (Optional) You only need the Gradient Map when Gradient Wipe is the chosen mode.

### Basic Node Setup

A standard wiring for Dissolve nodes feeds two source images into the background and foreground inputs and routes the output onward to the next node in the comp.

### A typical dissolve node structure in Fusion

### Resolution Handling

Best practice is to keep every image fed to the foreground, background, and gradient map inputs of the Dissolve node at one shared resolution and one shared pixel aspect. None of that is mandatory, though. When you do mix resolutions, the outcome hinges on where the Background/ Foreground slider lands.

- Where the source images differ in size yet the Foreground/Background slider sits at full Foreground (pushed fully right) or full Background (pushed fully left), the output resolution matches the image resolution of whichever node input is selected.
- Where source images of unequal size are blended by parking the Background/Foreground slider somewhere in the middle, the output adopts the larger of the two input resolutions so that both images fit. Under those conditions, you may notice unwanted resolution shifts as the slider travels from full foreground or background toward an intermediate spot.

Say, for instance, you dissolve a 4K image (wired to the background) into an 8K image (wired to the foreground): the Dissolve node puts out 4K while the slider rests at full Background, then abruptly leaps to 8K once you set full Foreground or blend anywhere between the foreground and background.

### Inspector

### Dissolve controls

### Controls Tab

Here are the primary controls steering how the Dissolve node behaves.

- Operation Pop-Up: Seven distinct techniques for blending the Foreground and Background inputs live in the Operation menu. The pair of images blend according to the Background/Foreground slider value, which sets the contribution percentage of each.

Dissolve: The ordinary Dissolve mode behaves like a cross dissolve — as one clip fades out, the other fades in. Additive Dissolve: Resembling a classic film dissolve, an Additive dissolve first sums in the second clip and afterward fades the first one away. Erode: The Erode technique crosses between the two images by spreading the darkest regions of the background image until the foreground image shows through. Visually it resembles a strip of film burning away. Random Dissolve: The blend between images is carried out with a randomly created dot pattern. Random Noise Dissolve: The blend is carried out using a dot pattern that shifts randomly over time. Gradient Wipe: Here the dissolve follows the luminance values found in the image at the Gradient Map input. You can soften the edges of this dissolve, and both the border's density and its color are adjustable on their own. SMPTE Wipe: The SMPTE wipe mimics the elementary effect wipes seen on many video effects switchers. Both a horizontal wipe and a vertical wipe are supplied. These wipes accept soft edges and added borders, with the border's density and color each set independently.

- Background/Foreground Slider: Defaults to Foreground. This control decides whether what you get out is the background image, the foreground image, or some blend of the pair. Which kind of blend is dictated by the Operation control. Should either input image be unavailable at the moment, the remaining one is output no matter where this slider sits.

### Gradient/SMPTE Wipe Controls

These controls show up solely when Gradient Wipe or SMPTE Wipe is chosen.

- Wipe Style: (SMPTE Wipe only) Two wipe styles can be picked from this drop-down list: Horizontal - Left to Right and Vertical - Top to Bottom. Tick the Invert Wipe checkbox to flip the wipe's direction.
- Invert Wipe: (SMPTE Wipe only) Ticking this reverses the direction of the wipe.
- Softness: Reach for this control when you want to soften the transition's edge.
- Border: Turning on the Border lets you color the transition's edge and brings its related

controls into view. The result is a border drawn around the transition edge.

- Border Softness: (Appears only when Border is turned on) Both the width and density of the border are governed by the Border Softness slider.

Raising the value yields a denser border, while lowering it yields a thinner one.

- Border Color: (Appears only when Border is turned on) Pick the hue applied to the border via Border Color.

### Common Controls

Settings Tab The Inspector's Settings tab appears identically in both the Dissolve and Merge nodes. Full coverage of these shared controls comes later, in this chapter's “The Common Controls” section.
