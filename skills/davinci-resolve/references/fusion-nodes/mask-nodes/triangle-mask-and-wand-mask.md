# Triangle mask and wand mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Triangle mask, Wand mask.
[Chapter index](INDEX.md) / [Previous section](rectangle-mask-and-triangle-mask.md) / [Next section](wand-mask-and-common-controls.md) / [Triangle Mask Tri](rectangle-mask-and-triangle-mask.md)
<a id="source-basic-node-setup-2"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-2"></a> <a id="source-the-wand-node"></a> <a id="source-triangle-mask-controls"></a> <a id="source-wand-mask-node-introduction"></a> <a id="source-wand-mask-wnd"></a>

### Triangle Mask controls

### Controls Tab

The Controls tab serves to fine-tune how the triangle looks once you’ve drawn it in the viewer. Show View Controls The Show View Controls checkbox switches the display of the mask’s onscreen controls in the viewer on or off. With this checkbox off, onscreen controls — center position, polylines, angles, and the rest — stay hidden, even while the node is selected.

Level The Level control fixes the transparency level of the pixels within the mask channel. At a value of 1.0, the mask is fully opaque (barring a soft edge). Lower values render the mask partly transparent. The outcome matches turning down an effect’s Blend control. NOTE: Dropping a mask’s level pulls down the values of every pixel the mask covers within the mask channel. As an example, when a Circle mask sits over a Rectangle mask, lowering the Circle mask’s level pulls down the values of all the pixels in the mask channel, even while the Rectangle mask underneath stays opaque. Filter This control picks the filtering algorithm put to work when Soft Edge is applied to the mask.

- Box: The quickest method, but quality drops off. Box suits best where blur amounts stay minimal.
- Bartlett: Known too as a Pyramid filter, Bartlett lands a sound trade-off of speed versus quality.
- Multi-box: Choosing this filter brings up the Num Passes slider, letting you steer the quality. At 1 and 2 passes, the results match Box and Bartlett, respectively. From 4 passes upward, the results usually rival Gaussian, in less time and with no edge “ringing.”
- Gaussian: Relying on a true Gaussian approximation, the Gaussian filter gives excellent results, though it runs a bit slower than the others. On occasion it can throw an extremely slight edge “ringing” onto floating-point pixels.

Soft Edge Reach for the Soft Edge slider to blur (feather) the mask through the chosen filter. Raising the value makes the edge fade off well past the mask’s boundaries. A value of 0.0 produces a sharp, crisply-defined edge. Border Width The Border Width control tunes how thick the mask’s edge is. With the solid checkbox switched on, the border swells or thins the mask. When the mask isn’t solid, the mask shape renders as an outline, its width set by the Border Width setting. Paint Mode Wiring a mask into the effect mask input reveals the Paint mode menu. The Paint mode decides how the mask coming into the effect mask input and the mask the node builds get combined.

- Merge: Merge is the default across all masks. The new mask blends into the input mask.
- Add: The new mask’s values pile onto the input mask’s values.
- Subtract: Across the overlapping areas, the new mask values come off the input mask’s values.
- Minimum: Weighing the input mask’s values against the new mask, this shows the lowest

(minimum) value.

- Maximum: Weighing the input mask’s values against the new mask, this shows the highest

(maximum) value.

- Average: Works out the mean (half the total) across the new mask together with the input mask.
- Multiply: Takes the input mask’s values and multiplies them by those of the new mask.
- Replace: Wherever the two overlap, the new mask stands in fully for the input mask. Wherever the new mask reads zero (completely black), the input mask carries on unchanged.
- Invert: Wherever the new mask covers the input mask, those areas flip: white goes to black and the other way round. Gray portions of the new mask wind up partly inverted.
- Copy: This mode throws out the input mask altogether and draws every value from the new mask.
- Ignore: This mode throws out the new mask altogether and draws every value from the input mask.

Invert Ticking this checkbox flips the whole mask. Unlike the Invert Paint mode, this checkbox reaches every pixel, no matter whether the new mask covers it. Solid With the Solid checkbox on, the mask is filled to be transparent (white) unless it has been inverted. Switch it off and the spline renders as just an outline, with the Border Width slider setting how thick it is. Point 1, Point 2, Point 3 These controls report the position coordinates of the triangle’s three corners. Any point can be published, wired to other controls, animated along a path, or latched onto trackers. You carry these tasks out by right-clicking the Position control or by clicking the point directly in the viewer.

### Common Controls

Image and Settings Tabs Other mask nodes carry the same Image and Settings tabs found here in the Inspector. A full account of these shared controls appears at this chapter’s end within “The Common Controls” section.

### Wand Mask [Wnd]

### The Wand node

### Wand Mask Node Introduction

The Wand mask masks an image off a wand-style selection, much like the Magic Wand tool that Adobe Photoshop offers. Just as with a Bitmap mask, whatever image lives in the composition can serve as the mask’s source. As a rule the default proves handiest, where the source image is the input of the node the mask gets applied to. Adding a Wand mask to a node brings a crosshair up in the viewers. Position this crosshair over the image to pick the color used to build the Wand mask. The mask comes together by reading the pixel color beneath the selection point and folding that color into the mask. From there the mask grows outward, reading the pixels around the selection point. Surrounding pixels join the mask when their color matches. The mask quits growing once no connecting pixels remain inside the mask’s color range.

### Inputs

In the Node Editor, the Wand mask node carries two inputs. Input: The orange input takes a 2D image out of which the mask is built. Effect Mask: Into the optional blue input goes a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here merges the masks. Just how they merge is governed by the Paint mode menu over in the Inspector.

### Basic Node Setup

You don’t actually need the Wand mask node to wire an image into the effect mask input, yet like the Bitmap node it offers options you couldn’t otherwise reach. It lets you choose channels beyond RGBA for the mask, along with softness and clipping. In the node tree below, the Wand node pulls the composite off the merge, building a mask for the color correction.

A Wand node picks out a particular region of the image so as to build a mask.
