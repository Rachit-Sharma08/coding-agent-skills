# Blur and defocus

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blur, Defocus.
[Chapter index](INDEX.md) / [Next section](defocus-and-directional-blur-and-glow.md)
<a id="source-a-blur-node-applied-to-a-mediain1-node"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-blur-blur"></a> <a id="source-blur-controls"></a> <a id="source-blur-node-introduction"></a> <a id="source-blur-nodes"></a> <a id="source-blur-nodes-part-1"></a> <a id="source-controls-tab"></a> <a id="source-defocus-dfo"></a> <a id="source-defocus-node-introduction"></a> <a id="source-examples"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-the-blur-node"></a> <a id="source-the-defocus-node"></a>

### Blur Nodes

The pages here go through the Blur nodes that Fusion offers. The short abbreviation shown beside each node name works in the Select Tool dialog while you hunt for tools, and it also serves in scripting references. Throughout this document, node trees that show MediaIn nodes in DaVinci Resolve stand in equally for Loader nodes in Fusion Studio, except where a note says otherwise.

### Blur [Blur]

### The Blur node

### Blur Node Introduction

Just as its name promises, the Blur node softens the image fed into it. It ranks among the most frequently reached-for image-processing operations.

### Inputs

A Blur node carries two inputs, one for a 2D image and one for an effect mask that can restrict where the blur lands. Input: The orange input takes the main 2D image that gets blurred. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask here confines the blur to the pixels inside that mask. An effect mask gets applied once the tool itself has finished processing.

### Basic Node Setup

Like a great many 2D image-processing nodes, the Blur node accepts a 2D image such as the MediaIn1 pictured below. Its output carries the node tree onward by feeding another 2D image-processing node or a Merge node.

### Inspector

### A Blur node applied to a MediaIn1 node

### Blur controls

NOTE: Because an ideal Gaussian filter would need to look at an endless number of pixels, every workable Gaussian is, by necessity, an approximation. Fusion's algorithm takes a heavily-optimized route that brings real advantages, yet in a few extreme situations it can produce visible ringing along the edges. That ringing shows up only when you blur float-depth images and normally sits well under what the eye can detect, particularly in final renders or HiQ mode, though it may surface in later processing. Should you run into it, the Multi-box filter can be a sound pick.

### Controls Tab

Inside the Controls tab live the main controls you need for shaping the blur, among them five filter algorithms. Filter The Filter menu is the place where you pick which kind of filter builds the blur.

- Box Blur: This choice runs quicker than the Gaussian blur but yields a coarser outcome.
- Bartlett: This choice gives a gentler, anti-aliased blur filter.
- Multi-box: Multi-box runs a Box filter across several layered passes to mimic a Gaussian shape.

Use a fair number of passes (four, say) and you get a high-quality blur, frequently quicker than the Gaussian filter and free of any ringing.

- Gaussian: Gaussian lays down a smooth, symmetrical blur filter built on a refined constant-time Gaussian approximation algorithm.
- Fast Gaussian: Gaussian lays down a smooth, symmetrical blur filter built on a refined constanttime Gaussian approximation algorithm. This mode is the filter method used by default.

Color Channels (RGBA) Out of the box the filter works on the R, G, B, and A channels. You can filter channels selectively by clicking each channel button to turn it on or off. NOTE: This isn't the same thing as the RGBA checkboxes sitting under the common controls. These picks are honored before the node processes the image, so turning off a channel makes the node bypass it during processing, which speeds the effect's render. The channel controls on the Common Controls tab, by contrast, kick in after the node has processed. Lock X/Y Ties the X and Y Blur sliders together so the blur stays symmetrical. It's on by default. Blur Size Sets how much blur lands on the image. Deselect the Lock X and Y control and you get separate command over each axis.

Clipping Mode This setting governs how edges get treated during domain-of-definition rendering. It carries real weight for nodes such as Blur, which may need to sample parts of the image lying beyond the current domain.

- Frame: Frame is the default, and it automatically forces the node's domain of definition to span the image's whole frame, in effect disregarding the present domain of definition. Where the upstream DoD falls short of the frame, the leftover frame area is taken as black/ transparent.
- Domain: Choosing Domain honors the upstream domain of definition as the node's effect is applied. This can lead to unwanted clipping wherever the node reaches for a large filter.
- None: Choosing None skips source image clipping altogether. So whatever data the node's effect needs that would normally fall outside the upstream DoD is taken as black/transparent.

Blend The Blend slider sets what share of the affected image is blended with original image. The nearer the value gets to 0, the more of the original image it folds back in. This control is a cloned copy of the Blend slider over on the Common Controls tab; adjusting one adjusts the other in lockstep.

### Examples

Below is a side-by-side of the Blur filters drawn as “cross-sections” through a filtered edge. Notice that Box yields a straight ramp, whereas Bartlett yields a somewhat gentler ramp. Multi-box and Gaussian look identical unless you magnify the slopes way in. Both deliver still gentler ramps, yet, as noted above, Gaussian overshoots a touch and can push values negative when used on floating-point images.

The Blur filters rendered as edge “cross sections” showing how each filters a single edge Common Controls Settings Tab The Settings tab inside the Inspector likewise repeats on the other Blur nodes. A full account of these shared controls waits at the chapter's end, under the “The Common Controls” section.

### Defocus [Dfo]

### The Defocus node

### Defocus Node Introduction

The Defocus node imitates what happens with an out-of-focus camera lens, blooming and image flaring among the effects. It supplies a quick Gaussian mode plus a more lifelike though slower Lens mode.

### Inputs

A Defocus node has two inputs, for wiring up a 2D image and an effect mask that can hold the simulated defocus to a chosen region. Input: The orange input takes the main 2D image for defocusing. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask here confines the defocus to the pixels inside that mask. An effect mask gets applied once the tool has processed.

### Basic Node Setup

A Defocus node accepts a 2D image such as the MediaIn1 pictured below. Its output carries the node tree onward by feeding another 2D image-processing node or a Merge node.
