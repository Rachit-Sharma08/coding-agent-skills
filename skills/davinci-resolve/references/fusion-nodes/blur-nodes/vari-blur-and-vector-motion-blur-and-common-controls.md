# Vari blur and vector motion blur and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vari blur, Vector motion blur, Common controls.
[Chapter index](INDEX.md) / [Previous section](soft-glow-and-unsharp-mask.md) / [Next section](common-controls-common-blur-settings.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-the-common-controls"></a> <a id="source-the-vari-blur-node"></a> <a id="source-the-vector-motion-blur-node"></a> <a id="source-vari-blur-controls"></a> <a id="source-vari-blur-node-introduction"></a> <a id="source-vari-blur-vbl"></a> <a id="source-vector-motion-blur-introduction"></a> <a id="source-vector-motion-blur-node"></a> <a id="source-vector-motion-blur-vmb"></a>

### Vari Blur [VBL]

### The Vari Blur node

### Vari Blur Node Introduction

A genuine per-pixel variable blur comes from the Vari Blur node, which leans on a second image to drive how much blur each pixel gets. Its effect resembles the Depth Blur node somewhat, yet it takes a different route that often yields cleaner results.

### Inputs

For the primary image, the Vari Blur node has two inputs: the blur map image plus an effect mask. Input: The gold image input must be connected and carries the primary image you want to blur. Blur Image: The green input must be connected too, though as the blur map image it accepts any of these: a spline shape, text object, still image, or movie file. After connecting it, you pick the red, green, blue, Alpha, or luminance channel to define the blur's shape. Effect Mask: The optional blue effect mask input wants a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Hooking a mask here confines the Vari Blur to just the pixels inside the mask. That effect mask is applied to the tool once it has been processed.

### Basic Node Setup

A 2D image like the MediaIn1 below feeds the Vari Blur node. A gradient Background tool wires into the Blur image input to steer which regions the blur touches. From the output, the node tree carries on by linking to another 2D image-processing node or a Merge node.

### Inspector

A Vari Blur node sitting on a MediaIn1 node, with a gradient background steering which regions blur

### Vari Blur controls

### Controls Tab

Every primary control you need for tailoring the Vari Blur operation lives on the Controls tab. Method Pick the Blur method for the filter from this menu. The choices appear below.

- Soften: This method ranges from a plain Box shape through a Bartlett triangle up to a respectable Smooth blur as Quality climbs. It holds onto detail in less-blurred regions a touch better than Multi-box.
- Multi-box: Like Soften, it delivers a stronger Gaussian approximation at higher Quality settings.
- Defocus: Gives blurred pixels a flat, circular shape that can mimic the

look of a defocus. Quality Raising Quality yields smoother blurs at the cost of speed. With Quality set to 1, a very fast yet plain Box blur drives every Method setting. For low Blur Size values, a Quality of 2 generally does the job. A Quality of 4 usually suffices for most work unless Blur Size runs especially high.

Blur Channel This picks which channel of the Blur Image governs how much blurring lands on each pixel. Lock X/Y When chosen, only one Blur Size control shows, and any change to the blur amount lands on both axes alike. Clearing the checkbox brings up separate controls for X and Y Blur Size. Blur Size Pushing this control up raises the total blur applied to every pixel. Wherever the Blur image is black or absent, those pixels still blur, regardless of the Blur Size. Blur Limit This slider caps the usable range drawn from the Blur image. Certain Z-depth images carry values running to infinity, which throw off blur size. The Blur Limit serves to hold values inside range.

### Common Controls

Settings Tab Other Blur nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.

### Vector Motion Blur [VMB]

### The Vector Motion Blur node

### Vector Motion Blur Introduction

You use this node to build directional blurs driven by a Motion Vector map or by AOV (Arbitrary Output Variable) channels exported out of 3D-rendering software such as Arnold, Renderman, or VRay. Alternatively, the Optical Flow node in Fusion can generate motion vectors for you. Typically the vector map comprises two floating-point images: one channel states how far the pixel travels in X, the other how far it travels in Y. Those channels might sit inside OpenEXR or RLA/RPF images, or arrive as separate images through the node's Vectors input. To carry + and – values, the vector channels ought to use a float16 or float32 color depth. In the X channel, a value of 1 signals that pixel has shifted one pixel rightward, whereas a value of –10 marks ten pixels of movement leftward.

### Inputs

The Vector Motion Blur node carries three inputs covering a 2D image, a motion vector pass, plus an effect mask. Input: The required orange input handles a 2D image that takes on the motion blur. Vectors: The green input is required as well. Wire in here a motion vector AOV that a 3D application rendered, or else an EXR file the Optical Flow node in Fusion produced. Vector Mask: The optional white Vector Mask input masks the image ahead of processing. Effect Mask: A mask shape from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools feeds the shared blue input. Hooking a mask here keeps the motion blur's source confined to just the pixels inside the mask. That effect mask is applied to the tool after it gets processed.

### Basic Node Setup

A 2D image like the IMAGE shown below feeds the Vector Motion Blur node. A MediaIn or Loader node holding motion vectors wires into the Vector's input. From its output, the node tree carries on by linking to another 2D image-processing node or a Merge node.

### Inspector

A Vector Motion Blur node sitting on a MediaIn or Loader node, its motion vectors wired into the Vectors input

### Vector Motion Blur node

### Controls Tab

Every primary control you need for tailoring the Vector Motion Blur operation lives on the Controls tab.

X Channel From this menu, pick which channel of the image supplies the vectors driving pixel movement along the X-axis. Y Channel From this menu, pick which channel of the image supplies the vectors driving pixel movement along the Y-axis. Flip Channel Use these checkboxes to flip, or invert, the X and Y vectors. As an example, a value of 5 for a pixel in the X-vector channel turns into –5 once the X checkbox is on. Lock Scale X/Y Ticking this checkbox unlocks separate sliders for X and Y Scale. By default a single Scale slider appears. Scale Each pixel's X and Y vector channel values are multiplied by this slider's value. Say the scale is 2 and the vector value is 10; you would get 20. This slider divides into Scale X and Scale Y when the Lock Scale X/Y checkbox is off.

### Common Controls

Settings Tab Other Blur nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits in the following "The Common Controls" section.

### The Common Controls

A handful of identical controls in the Inspector are shared across nodes that perform blur operations. The controls common to Blur nodes are covered in this section.
