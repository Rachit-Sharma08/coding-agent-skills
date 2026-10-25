# Rectangle mask and triangle mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rectangle mask, Triangle mask.
[Chapter index](INDEX.md) / [Previous section](ranges-mask-fusion-and-rectangle-mask.md) / [Next section](triangle-mask-and-wand-mask.md) / [Rectangle Mask Rec](ranges-mask-fusion-and-rectangle-mask.md)
<a id="source-basic-node-setup-1"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-inputs-1"></a> <a id="source-inspector-1"></a> <a id="source-rectangle-mask-controls"></a> <a id="source-the-triangle-node"></a> <a id="source-triangle-mask-node-introduction"></a> <a id="source-triangle-mask-tri"></a>

### Rectangle Mask controls

### Controls Tab

The Controls tab serves to fine-tune how the rectangle looks once you’ve drawn it in the viewer. Show View Controls The Show View Controls checkbox switches the display of the mask’s onscreen controls in the viewer on or off. With this checkbox off, onscreen controls — center position, polylines, angles, and the rest — stay hidden, even while the node is selected. Level The Level control fixes the transparency level of the pixels within the mask channel. At a value of 1.0, the mask is fully opaque (barring a soft edge). Lower values make the mask partly transparent. The outcome matches turning down an effect’s Blend control.

NOTE: Dropping a mask’s level pulls down the values of every pixel the mask covers within the mask channel. As an example, when a Circle mask sits over a Rectangle mask, lowering the Circle mask’s level pulls down the values of all the pixels in the mask channel, even while the Rectangle mask underneath stays opaque. Filter This control picks the filtering algorithm put to work when Soft Edge is applied to the mask.

- Box: The quickest method, though quality suffers. Box fits best where blur amounts are minimal.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a fair balance of speed against quality.
- Multi-box: Choosing this filter brings up the Num Passes slider, handing you control of the quality. At 1 and 2 passes, the results match Box and Bartlett, respectively. From 4 passes upward, the results are typically on par with Gaussian, faster and free of edge “ringing.”
- Gaussian: Drawing on a true Gaussian approximation, the Gaussian filter delivers excellent results, albeit a touch slower than the rest. Now and then it can leave a faint edge “ringing” on floating-point pixels.

Soft Edge Reach for the Soft Edge slider to blur (feather) the mask through the chosen filter. Raising the value makes the edge fade off well past the mask’s boundaries. A value of 0.0 yields a sharp, crisply-defined edge. Border Width The Border Width control tunes how thick the mask’s edge is. With the solid checkbox switched on, the border swells or thins the mask. When the mask isn’t solid, the mask shape renders as an outline, its width set by the Border Width setting. Paint Mode Wiring a mask into the effect mask input reveals the Paint mode menu. The Paint mode decides how the mask coming into the effect mask input and the mask the node builds get combined.

- Merge: Merge is the default across all masks. The new mask blends into the input mask.
- Add: The new mask’s values pile onto the input mask’s values.
- Subtract: Across the overlapping areas, the new mask values come off the input mask’s values.
- Minimum: Weighing the input mask’s values against the new mask, this shows the lowest

(minimum) value.

- Maximum: Weighing the input mask’s values against the new mask, this shows the highest

(maximum) value.

- Average: Works out the mean (half the total) across the new mask together with the input mask.
- Multiply: Takes the input mask’s values and multiplies them by those of the new mask.
- Replace: Wherever the two overlap, the new mask stands in fully for the input mask. Any spot sitting

at zero (completely black) within the new mask makes no difference to the input mask.

- Invert: Wherever the new mask covers the input mask, those areas flip: white becomes

black and back again. Gray regions of the new mask come out partly inverted.

- Copy: This mode throws out the input mask altogether and draws every value from the new mask.
- Ignore: This mode throws out the new mask altogether and draws every value from the input mask.

Invert Ticking this checkbox flips the whole mask. Unlike the Invert Paint mode, this checkbox reaches every pixel, no matter whether the new mask covers it. Solid With the Solid checkbox on, the mask is filled to be transparent (white) unless it has been inverted. Switch it off and the spline renders as just an outline, its thickness governed by the Border Width slider. Center X and Y The position of the Rectangle mask is adjusted through these controls. Width and Height Lean on these controls to adjust, independently of one another, the X or Y scale of the rectangular effect mask. As an alternative, drag the rectangle’s edges in the viewer to size it interactively. Corner Radius Corner Radius lets the corners of the Rectangle mask be rounded off. A value of 0.0 means no rounding whatsoever, leaving the rectangle with sharp corners. A value of 1.0 rounds the corners as much as possible. Angle Shift the rotation angle of an effect mask by sliding the Angle control left or right. Values may be keyed into the input boxes provided. As an alternative, use the onscreen controls, dragging the little circle at the tip of the dashed angle line to spin the ellipse interactively.

### Common Controls

Image and Settings Tabs Other mask nodes carry the same Image and Settings tabs found here in the Inspector. A full account of these shared controls appears at this chapter’s end within “The Common Controls” section.

### Triangle Mask [Tri]

### The Triangle node

### Triangle Mask Node Introduction

What the Triangle mask makes are plain triangular masks. What sets it apart is its lack of any Center, Size, or Angle control. Unlike most other mask types, all three of the triangle’s points can latch onto a tracker or motion path.

### Inputs

A single effect mask input sits on the Triangle mask node. Effect Mask: Into the optional blue input goes a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here merges the masks. Just how they merge is governed by the Paint mode menu over in the Inspector.

### Basic Node Setup

For turning out triangular shapes, the Triangle mask node comes in handy. Below, the Triangle mask serves to make a colored triangle by carving a triangular shape out of a background node.

### Inspector

A Triangle mask node carving a colored Triangle shape out of a Background node
