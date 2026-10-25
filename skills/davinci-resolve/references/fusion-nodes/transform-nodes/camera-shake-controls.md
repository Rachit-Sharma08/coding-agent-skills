# Camera shake controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera shake.
[Chapter index](INDEX.md) / [Next section](camera-shake-and-crop-and-dve.md)
<a id="source-basic-node-setup"></a> <a id="source-camera-shake-csh"></a> <a id="source-camera-shake-node-introduction"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-the-camera-shake-controls-tab"></a> <a id="source-the-camera-shake-node"></a> <a id="source-transform-nodes"></a> <a id="source-transform-nodes-part-1"></a>

### Transform Nodes

The Transform nodes provided within Fusion are covered in this chapter.

Each node name carries an abbreviation beside it; those shorthand codes are what you type into the Select Tool dialog when hunting for a tool, and they also surface in scripting references. Throughout this document, treat any node tree that depicts MediaIn nodes under DaVinci Resolve as equivalent to Loader nodes under Fusion Studio, except where a note says otherwise.

### Camera Shake [CSh]

### The Camera Shake node

### Camera Shake Node Introduction

A range of camera-shake-style motion, anywhere from organic to mechanical, can be reproduced by this node. Do not confuse it with the Shake Modifier, whose role is to feed random numeric values into parameters. The Shake modifier is documented separately in Chapter 124, "Modifiers," within the DaVinci Resolve Reference Manual, or alternatively Chapter 64 of the Fusion Reference Manual. For better-quality processing, the Camera Shake node merges its output with neighboring transformation nodes.

### Inputs

A 2D image plus an effect mask attach to the Camera Shake node's two inputs, and the mask serves to confine where the shake takes effect. Input: The primary 2D image that will shake plugs into the orange input. Effect Mask: A mask shape—built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools—feeds the blue input. Wiring a mask here restricts the shake so that only pixels falling inside the mask are affected. The tool finishes processing first, and only then is an effects mask applied to it.

### Basic Node Setup

Feed the image you intend to transform into the Camera Shake background input. To flag regions that the shake ought to skip, run polygon masks into the occlusion mask input.

You can wire the Camera Shake node straight after a MediaIn node, or after any node that hands off a 2D output.

### Inspector

### The Camera Shake Controls tab

### Controls Tab

Offsets, strength, speed, and frequency for the simulated camera-shake movement are all dialed in from the parameters on the Controls tab. Deviation X and Y These two controls set how much shake hits the image horizontally (X) and vertically (Y). The accepted range runs from 0.0 to 1.0. At 1.0, shake positions can land anywhere inside the image's borders. Rotation Deviation This sets how much shake is applied to the rotational axis. The accepted range runs from 0.0 to 1.0. Randomness Raising this control makes the shake motion more erratic and random, while lowering it makes the motion more predictable. Overall Strength This scales the combined amplitude of every parameter, easing the whole effect in and out. At 1.0 the effect plays exactly as the rest of the controls specify. Speed Speed governs the frequency, or rate, at which the shake occurs. Frequency Method This picks the overall waveform of the shake. The frequencies on offer are Sine, Rectified Sine, and Square Wave. Compared to a Sine, a Square Wave yields motion that looks far more mechanical.

Filter Method While rescaling a pixel, nearby pixels are frequently consulted to yield a more believable outcome. The various methods of blending those pixels together are known as filters. The more elaborate filters tend to deliver better quality at the cost of slower computation. Which filter suits a given task usually comes down to how much scaling is involved and what the image itself contains.

- Box: A plain interpolation resize applied to the image.
- Linear: Relies on a basic filter that turns out fairly tidy, quick results.
- Quadratic: Delivers a middling outcome, striking a reasonable balance between

speed and quality.

- Cubic: Yields stronger results on continuous-tone images. Where an image holds fine detail,

the outcome can come out blurrier than you'd want.

- Catmull-Rom: Performs well on continuous-tone images that are scaled down.

On finely detailed images it returns sharp results.

- Gaussian: Roughly matches Bi-Cubic in both speed and quality.
- Mitchell: Resembles Catmull-Rom but handles finely detailed images more effectively. It runs

slower than Catmull-Rom.

- Lanczos: Closely tracks Mitchell and Catmull-Rom, though it is a touch cleaner and slower too.
- Sinc: A sophisticated filter delivering exceptionally sharp, detailed output; in certain cases, though, it can introduce

visible “ringing.”

- Bessel: Behaves much like the Sinc filter while running a little quicker.

Window Method (Sinc and Bessel Only) A handful of filters, Sinc and Bessel among them, would in theory need an unlimited count of pixels to compute precisely. A windowing function speeds this up by approximating the filter and capping how many pixels it has to touch. Whenever you pick a filter that needs windowing, this control becomes visible.

- Hanning: A plain tapered window.
- Hamming: A lightly adjusted variant of Hanning that stops short of tapering completely

down to zero.

- Blackman: A window whose falloff tapers more steeply.
- Kaiser: A more involved window landing somewhere between Hamming and Blackman.

For the most part these filters earn their keep only when you are enlarging an image. To downsize, the Bi-Linear filter is the usual pick; that said, the Catmull-Rom filter adds a touch of sharpening and can help hold onto detail as you scale an image down.
