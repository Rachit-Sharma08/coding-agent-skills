# Set canvas color and white balance

Version: DaVinci Resolve 20.3 Reference Manual. Context: Set canvas color, White balance.
[Chapter index](INDEX.md) / [Previous section](ocio-color-space-and-ocio-display-and-ocio-file-transform.md) / [Next section](white-balance-inputs.md) / [Continue White Balance WB / Inputs](white-balance-inputs.md)
<a id="source-basic-node-setup-5"></a> <a id="source-controls-tab-5"></a> <a id="source-inputs-5"></a> <a id="source-inspector-3"></a> <a id="source-set-canvas-color-controls"></a> <a id="source-set-canvas-color-node-introduction"></a> <a id="source-set-canvas-color-scv"></a> <a id="source-settings-tab-5"></a> <a id="source-the-set-canvas-color-node"></a> <a id="source-the-white-balance-node"></a> <a id="source-white-balance-node-introduction"></a> <a id="source-white-balance-wb"></a>

### Set Canvas Color [SCv]

### The Set Canvas Color node

### Set Canvas Color Node Introduction

You reach for Set Canvas Color to assign a color to the region beyond the domain of definition (DoD). Normally that is the workspace stretching past the raster, and it stays unseen because anything outside the raster goes unrendered. The DoD can also fall inside the raster, though — something that crops up when you composite images smaller than the raster, or apply transforms. The default canvas color is black with no Alpha (transparent). Yet because certain nodes will alter an image’s canvas color — inverting a mask, for instance, flips the mask’s canvas from black to white — Set Canvas Color hands you control to make the canvas any color you need. So the Set Canvas Color node assigns the color of the workspace lying outside the domain of definition (DOD). Build a circular gradient, say, and the DoD becomes a square framing that gradient in the viewer. Whatever sits beyond the DoD is taken as black and thus skips rendering. To recolor the region past the DoD, hook the Set Canvas Color node up after the background and pick a new color. NOTE: Hover the pointer over a black region outside the raster and the RGB canvas color shows in the status bar down at the lower left of the Fusion window.

### Inputs

The Set Canvas Color node carries a pair of inputs — the first for your primary image, the next for a foreground. Input: Colored orange, this is the only connection you must make, taking a 2D image that exposes the canvas color whenever the image’s DoD comes up smaller than the raster. Foreground: The optional green foreground input lets the canvas color be sampled from whatever image you wire into it.

### Basic Node Setup

You position the Set Canvas Color node downstream of the transform that exposes a slice of the raster beyond the domain of definition.

A Set Canvas Color node placed on a transformed MediaIn 1 node Here the footage out of MediaIn1 has been scaled down with the Transform1 node, which leaves blank space surrounding the image inside the frame. Route that output through the SetCanvasColor node and you can recolor the blank space that rings the frame.

### Inspector

### Set Canvas Color controls

### Controls Tab

On Set Canvas Color, the Controls tab serves nothing more than picking a color. Wire up the green foreground, however, and this tab shows nothing at all.

Color Picker These controls set the Color along with the Alpha value of the image’s canvas, starting out at black with an Alpha of zero.

### Settings Tab

Across the other Color nodes the Inspector presents an identical Settings tab. You can read about each of these common controls in depth at the chapter’s end, within the “The Common Controls” section.

### White Balance [WB]

### The White Balance node

### White Balance Node Introduction

Turn to the White Balance node to clear out color casts automatically — the kind that arise from a camera being set up wrong or from poor lighting. You correct them either by dialing in a color temperature or by sampling a neutral color out of the original image where the cast shows. IMPORTANT: While sampling neutral colors with the Custom method, be certain you draw from the source image rather than from what the White Balance node outputs. That keeps the image steady as you sample, and it lets the White Balance node read the true original colors it has to fix.
