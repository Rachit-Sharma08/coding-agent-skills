# Mandelbrot and multitext

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mandelbrot, Multitext.
[Chapter index](INDEX.md) / [Previous section](day-sky-and-fast-noise.md) / [Next section](multitext-text-tab.md) / [Continue MultiText MTxT / Layout Tab / Type](multitext-layout-tab-type.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-color-tab-2"></a> <a id="source-common-controls-3"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-2"></a> <a id="source-mandelbrot-man"></a> <a id="source-mandelbrot-node-controls"></a> <a id="source-mandelbrot-node-introduction"></a> <a id="source-multitext-mtxt"></a> <a id="source-multitext-node-introduction"></a> <a id="source-noise-tab-1"></a> <a id="source-on-screen-controls"></a> <a id="source-show-always-text-outline"></a> <a id="source-text-toolbar"></a> <a id="source-the-mandelbrot-node"></a> <a id="source-the-mandelbrot-node-color-tab"></a> <a id="source-the-multitext-node"></a>

### Mandelbrot [MAN]

### The Mandelbrot node

### Mandelbrot Node Introduction

Drawing on the Mandelbrot fractal theory set, this node builds an image pattern.

### Inputs

The Mandelbrot node's lone input serves an effect mask that bounds where the fractal noise lands. Effect Mask: This optional blue effect mask input accepts a mask shape drawn from polylines, simple primitive shapes, paint strokes, or bitmaps imported from other tools. Hooking a mask up here keeps the fractals to only the pixels within that mask.

### Basic Node Setup

Images turned out by the Mandelbrot node lend themselves to motion graphics and sci-fi effects. In the example below, it produces motion graphics that sit behind a title.

A Mandelbrot node applied as a background to the Merge node

### Inspector

### Mandelbrot node controls

### Noise Tab

The Mandelbrot node's noise shape and pattern are steered from the Noise tab. Position X and Y This sets the image's horizontal and vertical position, or its seed point. Zoom Zoom drives the pattern larger or smaller. Each level of magnification is recomputed, so the zoom has no real ceiling. Escape Limit Marks the point at which the iteration's calculation halts. Low values bring on blurry halos. Iterations This dictates how repetitive the set is. Animate it and it mimics the set growing. Rotation This spins the pattern. Each fresh angle forces the image to be recomputed.

### Color Tab

From the Color tab you tune both the gradient and how the gradient colors repeat across the produced pattern. Grad Method Reach for this control to decide which kind of gradation applies along the pattern's borders. Continuous Potential This makes the pattern's edges fade into the background color. Iterations This makes the pattern's edges come out solid.

### The Mandelbrot node Color tab

Gradient Curve This governs how wide the gradation runs as the pattern transitions into the background color. R/G/B/A Phase and Repetitions These controls assign the color values for the pattern generators.

### Common Controls

Image and Settings Tabs Other generator nodes reproduce the same Image and Settings tabs seen in the Inspector. A detailed account of these shared controls follows at the chapter's close, in the “The Common Controls” section.

### MultiText [MTxT]

### The MultiText node

### MultiText Node Introduction

Built on the Text+ tool, Fusion's MultiText node is a sophisticated character generator that handles multiple styles, 3D transformations, and several shading layers. You can arrange text within a userdefined frame, around a circle, or along a path. The image this node turns out is 2D. When you need extruded 3D text with optional beveling, turn instead to the Text 3D node.

### Inputs

The MultiText node's single input takes an effect mask for cropping the text. Effect Mask: This optional blue effect mask input takes a mask shape fashioned from polylines, simple primitive shapes, paint strokes, or bitmaps brought over from other tools. Wire a mask in here and the text is held to just the pixels lying within that mask.

### On-Screen Controls

A range of editing tasks can be carried out right on MultiText within the Viewer overlay — among them editing text, showing a cursor, and selecting text. The workflow feels natural: with MultiText selected, a double-click anywhere in the Fusion viewer switches on the in-viewer text editing mode.

### Text+ toolbar

Allow Typing in Viewer Once this is on, you can enter and revise text straight in the viewer. Clicking the text there drops the insert cursor inside the text. The Left and Right Arrow keys walk the insert cursor from one character to the next, while the Up and Down Arrows jump between text lines. Allow Manual Positioning The Manual Positioning button takes over from the automatic kerning that text normally receives. Click the little red handle beneath any character to select it for kerning. Alternatively, drag a selection rectangle around whichever characters you mean to kern. With characters selected, keep the Option (macOS) or Alt key (Windows) held while tapping the Left or Right Arrow key to fine-tune the kerning of the chosen characters. Holding Alt + Shift (Windows) or Option + Shift (macOS) along with the arrow keys shifts the character in bigger steps. To keyframe each character's position, right-click the control label Manual Font Kerning under the Inspector's Advanced Controls and pick Animate from the contextual menu. Every time a character moves, a fresh key lands on the animation spline. As with polyline mask animation, all characters ride the same spline. No Text Outline Turning this button on stops any outline from being drawn around the text edges. That outline belongs not to the text but to the onscreen controls, helping you spot where the text sits. It makes up a three-way toggle, paired with two more buttons: Text Outline Outside Frame Only plus Show Always Text Outline. Text Outline Outside Frame Only Activating this draws a text-edge outline lying outside the visible frame, handy for tracking down text that has drifted offscreen and no longer renders a visible result. It is a threeway toggle paired with the No Text Outline and Show Always Text Outline buttons.

### Show Always Text Outline

No matter whether the text shows inside the frame or not, this button draws an outline around its edges. It is a three-way toggle together with the No Text Outline and Text Outline Outside Frame Only buttons.

The on-screen MultiText editing controls sit at the top-left corner inside the Fusion viewer The Fusion viewer also surfaces pivot points for your Character, Word, and Line transforms. To keep them within reach, the popup toolbar now sports a Pivot Points icon that flips their visibility on and off while you work rotation and scaling transformations. Character-level styling has been polished to make offset and translation transformations more intuitive. The upshot is less reliance on manual positioning and a uniform result across several distinct character selections.

### Basic Node Setup

Pairing the MultiText node with plenty of other nodes lets you build motion graphics. In the example below it feeds in as the foreground of a Merge node.

MultiText node connected as the foreground to a Merge node
