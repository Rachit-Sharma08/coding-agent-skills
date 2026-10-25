# Scale and transform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Scale, Transform.
[Chapter index](INDEX.md) / [Previous section](resize-example.md) / [Next section](transform-and-common-controls.md)
<a id="source-basic-node-setup-1"></a> <a id="source-controls-tab-1"></a> <a id="source-example-1"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-scale-node-introduction"></a> <a id="source-scale-scl"></a> <a id="source-the-scale-controls-tab"></a> <a id="source-the-scale-node"></a> <a id="source-the-transform-node"></a> <a id="source-transform-node-introduction"></a> <a id="source-transform-xf"></a>

### Scale [SCL]

### The Scale node

### Scale Node Introduction

The Scale node runs nearly identical to the Resize node, the difference being that Resize works in exact dimensions whereas the Scale node works in relative dimensions to spell out the change to the source image's resolution. What this node does is genuinely alter the image's resolution. NOTE: Since this node alters the image's physical resolution, animating its controls isn't advised.

### Inputs

A single input on the Scale node exists for hooking up a 2D image to scale. Input: The orange input takes the primary 2D image you intend to scale.

### Basic Node Setup

In the example below, the Scale node is dropped in between the MediaIn1 node and the background input of the Merge. In contrast to a Transform tool, scaling MediaIn1 alters the clip's resolution. With the resized MediaIn1 node wired into the orange background input, it also fixes the resolution of the Merge output.

Through the Scale node, an image can be scaled and its resolution altered.

### Inspector

### The Scale Controls tab

### Controls Tab

Parameters for changing the image's resolution live on the Controls tab. It works through a multiplier of size to set the fresh resolution. An Edges menu lets you settle how the frame's edges get handled should the scaling shrink. Lock X/Y When ticked, a single Size control alone appears, and any change to the image's scale applies equally to both axes. Clearing the checkbox brings up a separate Size control apiece for X and Y Size. Size What the Size control sets is the scale applied while adjusting the source image's resolution. At a value of 1.0 the image stays untouched, whereas 2.0 doubles the image's current resolution. Set to 0.5, the value cuts the image's resolution in half. Only Use Filter in HiQ For any non-HiQ renders, where speed counts for more than full accuracy, the Scale node will usually fall back on the fast Nearest Neighbor filter. Switch this checkbox off to force Scale to use the chosen filter across all renders. Change Pixel Aspect Switch this checkbox on to reveal a Pixel Aspect control that serves to alter the image's pixel aspect. Filter Method When a pixel is being rescaled, the pixels around it often get drawn on to yield a more realistic result. A range of algorithms exists for combining these pixels, called filters. The more intricate filters can yield better results yet usually take longer to compute. Which filter suits the job best tends to hinge on how much scaling is involved and on the contents of the image itself.

- Box: A plain interpolation-based resize of the picture.
- Linear: Leans on a bare-bones filter that turns out fairly clean, fast results.
- Quadratic: Turns out a middling result from this filter. Between

speed and quality it strikes a fair balance.

- Cubic: Turns out stronger results on continuous-tone pictures. Where the pictures hold fine detail,

the outcome can come out blurrier than you'd want.

- Catmull-Rom: Turns out solid results on continuous-tone pictures scaled down. On finely detailed pictures it yields sharp results.
- Gaussian: Sits very close to Bi-Cubic in both speed and quality.
- Mitchell: Resembles Catmull-Rom yet turns out stronger results on finely detailed pictures. It is

slower than Catmull-Rom.

- Lanczos: Sits very close to Mitchell and Catmull-Rom, just a touch cleaner and a touch slower as well.
- Sinc: A high-end filter delivering exceptionally sharp, detailed results; however,

it can throw visible "ringing" under certain conditions.

- Bessel: Resembles the Sinc filter though it may run a shade faster.

Window Method (Sinc and Bessel Only) Certain filters, Sinc and Bessel among them, would need an endless supply of pixels to compute precisely. To hasten this operation, a windowing function steps in to approximate the filter and cap the count of pixels needed. This control shows up once a filter calling for windowing is chosen.

- Hanning: A plain tapered window.
- Hamming: Hamming is a lightly adjusted take on Hanning that stops short of tapering all the

way down to zero.

- Blackman: A window whose falloff tapers more sharply.
- Kaiser: A more intricate window yielding results between Hamming and Blackman.

The bulk of these filters earn their keep only when you're enlarging an image. For shrinking images, the Bi-Linear filter is the common pick; the Catmull-Rom filter, though, lends a measure of sharpening to the results and can help hold onto detail while scaling an image down.

### Example

A spread of resize filters, reading left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic, followed by Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel. NOTE: Since this node alters the image's physical resolution, animating its controls isn't advised.

### Transform [XF]

### The Transform node

### Transform Node Introduction

You can put the Transform node to work for straightforward 2D transformations of the image, including moving, rotating, and scaling. The image's aspect, too, can be reshaped through the Transform node. The Transform node concatenates whatever it produces with neighboring Transformation nodes. The Transform node leaves the image's resolution alone.

### Inputs

A pair of inputs on the Transform node serve to hook up a 2D image and an effect mask, which can serve to confine the transformed area. Input: The orange input takes the primary 2D image that gets transformed. Effect Mask: The blue input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the transform area to nothing but the pixels inside the mask. An effects mask gets applied to the tool after the tool has been processed.
