# Eyedropper with color swatch and gradients

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing parameters in the inspector.
[Chapter index](INDEX.md) / [Previous section](picking-colors-from-an-image.md) / [Next section](modifiers-and-animating-parameters-in-the-inspector.md)
<a id="source-1x1-2x2-3x3-4x4-5x5"></a> <a id="source-angle-gradient"></a> <a id="source-cross-gradient"></a> <a id="source-gradient-colors-bar"></a> <a id="source-gradient-contextual-menu"></a> <a id="source-gradients"></a> <a id="source-interpolation-space"></a> <a id="source-linear-gradient"></a> <a id="source-offset"></a> <a id="source-oncerepeatping-pong"></a> <a id="source-radial-gradient"></a> <a id="source-reflect-gradient"></a> <a id="source-square-gradient"></a> <a id="source-start-and-end-position"></a> <a id="source-the-default-gradient-controls"></a> <a id="source-the-eyedropper-with-color-swatch"></a>

### The Eyedropper with color swatch

### Gradients

You use the Gradient Control bar to build a smooth transition from one color to another. Along the Gradient bar you'll see a preview of the colors running from beginning to end. Out of the box, two triangular color stops are present: the left-hand one fixes the start color while the right-hand one fixes the end color.

### The default Gradient controls

Gradient Type The Gradient Type button array lets you pick the form in which the gradient is rendered. Linear gradient: Linear lays the gradient out along a straight path running from the starting color stop to the ending one.

### Linear gradient

Reflect gradient: Reflect produces the gradient by mirroring the linear gradient on both sides of the starting point.

### Reflect gradient

Square gradient: Square renders the gradient with a square pattern, taking the starting point to be the center of the image.

### Square gradient

Cross gradient: Cross renders the gradient with a cross pattern, taking the starting point to be the center of the image.

### Cross gradient

Radial gradient: Radial renders the gradient as a circular pattern, taking the starting point to be the center of the image.

### Radial gradient

Angle gradient: Angle sweeps the gradient counter-clockwise, taking the starting point to be the center of the image.

### Angle gradient

### Start and End Position

A pair of X and Y edit boxes makes up the Start and End Position controls, handy for precisely tuning where the gradient begins and ends. Those same position values also show up as two crosshair onscreen controls in the viewer, which can be the handier way to do your first rough placement.

### Gradient Colors Bar

The Gradient Colors bar is where you pick the colors that blend together in the gradient. Its two default color stops define the start and end colors. To swap a color in the gradient, click its color stop and then set a fresh color with the Eyedropper or color wheel. The Colors bar also lets you add, reposition, duplicate, and remove gradient colors. To add a fresh stop onto the Gradient Colors bar: 1 Click at any spot across the lower edge of the Gradient Colors bar. 2 Pick the stop's color using either the Eyedropper or the color wheel. To reposition a stop along the Colors bar:

- Drag a color stop left or right along the Gradient Color bar.

To copy a color stop on the Colors bar:

- Hold Command while you drag a color stop.

To remove a stop from the Colors bar, take either of these approaches:

- Drag the color stop up past the Gradient Colors bar.
- Choose the stop and then hit the red X button to remove it.

### Interpolation Space

Via the Gradient Interpolation Method pop-up menu you choose which color space is used when computing the colors that fall between color stops.

### Offset

Moving the Offset control shifts the gradient's placement with respect to the start and end markers. It comes into its own when paired with the repeat and ping-pong modes covered just below.

### Once/Repeat/Ping-Pong

This trio of buttons dictates what the gradient does once the Offset control pushes it beyond its start and end positions. Once is the default, holding the color steady for offset. Repeat wraps back around to the start color the moment the offset passes the end color. Ping-pong plays the color sequence back in reverse.

### 1x1, 2x2, 3x3, 4x4, 5x5

These buttons govern how much sub-pixel accuracy is applied once the gradient's edges show through in Repeat mode, or while the gradient is being animated. Cranking the setting up makes rendering far slower but yields greater precision.

### Gradient Contextual Menu

Each gradient carries its own contextual menu, which you summon by right-clicking the Gradient bar. The Gradient contextual menu holds choices for animating, publishing, and linking one gradient to another. It also includes a gradient-only modifier that constructs a custom gradient by drawing colors from the output of a node in the Node Editor.
