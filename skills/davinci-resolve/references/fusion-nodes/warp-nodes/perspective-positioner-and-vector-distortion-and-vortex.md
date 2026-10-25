# Perspective positioner and vector distortion and vortex

Version: DaVinci Resolve 20.3 Reference Manual. Context: Perspective positioner, Vector distortion, Vortex.
[Chapter index](INDEX.md) / [Previous section](grid-warp-and-lens-distort-and-perspective-positioner.md) / [Next section](vortex-and-common-controls.md) / [Perspective Positioner PPn](grid-warp-and-lens-distort-and-perspective-positioner.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-the-perspective-positioner-controls-tab"></a> <a id="source-the-vector-distortion-controls-tab"></a> <a id="source-the-vector-distortion-node"></a> <a id="source-the-vortex-node"></a> <a id="source-vector-distortion-dst"></a> <a id="source-vector-distortion-node-introduction"></a> <a id="source-vortex-node-introduction"></a> <a id="source-vortex-vtx"></a>

### Inputs

The Perspective Positioner node's two inputs serve to hook up a 2D image plus an effect mask, which you can use to bound the transformed region. Input: The orange input takes the primary 2D image that gets transformed. Effect Mask: A mask shape from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools goes into the blue input. Hooking a mask here confines the transform to just the pixels inside the mask. That effects mask is applied to the tool once the tool finishes processing.

### Basic Node Setup

In the example below, the Perspective Positioner unpins a perspective distorted area of the MedianIn2 so you can paint on the flat texture. Afterward the MediaIn2 gets corner pinned back into position. Because the Perspective Positioner and Corner Positioner do not concatenate, these nodes introduce some softness.

The Perspective Positioner unpins an image to paint on a texture map.

### Inspector

### The Perspective Positioner Controls tab

### Controls Tab

Parameters for choosing vector channels and governing how much distortion they apply to an image appear on the Controls tab. Mapping Type The Mapping Type menu serves to pick which kind of transform distorts the image. Bi-Linear remains for supporting older projects. Keeping this on Perspective is strongly advised, since the Perspective setting models the real world more faithfully. Corners X and Y These are the four control points of the Perspective Positioner. Drag them interactively in the viewers to set each corner of the image. You can fine-tune their positions through the Top, Bottom, Left, and Right controls in the Inspector.

### Common Controls

Settings Tab Other Warp nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.

### Vector Distortion [Dst]

### The Vector Distortion node

### Vector Distortion Node Introduction

The Vector Distortion node warps the main source image independently along the X- and Y-axis, drawing on the vector channel data within the source image or on vector channels from a second reference image.

### Inputs

The Vector Distort node carries three inputs covering the primary 2D image, the distort image holding vector channels, and an effect mask. Input: The orange image input must be connected and carries the primary image you want to distort. Should that image hold vector channels, the distortion uses them. Distort: An optional distort image input, the green one warps the background image off its vector channels. Once it is connected, whatever vector channels the input image held get overridden. Effect Mask: For a mask shape, the optional blue effect mask input expects polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Hooking a mask here confines the displacement to just the pixels inside the mask. That effects mask is applied to the tool after it gets processed.

### Basic Node Setup

In the example below, the MediaIn1 node leans on an Optical Flow node to produce the vector channels, which then pass along to the Vector Distort node. MediaIn2 gets distorted and composited over the background. For the Vector Distort node to work, the image must carry vector channels or an Optical Flow node must generate them.

### Inspector

### The Vector Distortion Controls tab

### Controls Tab

Parameters for choosing vector channels and governing how much distortion they apply to an image appear on the Controls tab. X Channel and Y Channel These two menus pick which channel of the (green) distort image input distorts the X and Y channels. Should no distort reference image be connected, the main orange input's channels stand in instead. Flip Channel X and Flip Channel Y Through these checkboxes you reverse which way the distortion runs along the picked axis. Lock Scale X/Y Ticking this checkbox divides the Scale slider into a pair, namely Scale X and Scale Y. Scale With the Scale slider you multiply whatever values come off the distortion reference image. Lock Bias X/Y Ticking this checkbox divides the Bias slider into a pair, namely Bias X and Bias Y. Center Bias The Center Bias slider shifts or nudges the distortion down a given axis. Edges How the image's edges get treated is set by this menu.

- Canvas: This makes the edges uncovered by the shake take on the canvas color—usually transparent or black.
- Duplicate: This duplicates the edges, yielding a slight smearing effect along the edges.

Glow Use this slider to lay a glow over the result of the vector distortion.

### Common Controls

Settings Tab Other Warp nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.

### Vortex [Vtx]

### The Vortex node

### Vortex Node Introduction

The Vortex effect shows up as a swirling whirlpool across designated regions of the image. By animating its various controls, you can make the Vortex move and grow.

### Inputs

Two inputs sit on the Vortex node — one for the primary 2D image, one for the effect mask. Input: A required connection, the orange image input holds the primary image you want to swirl. Effect Mask: The optional blue effect mask input wants a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Hooking a mask here confines the swirling vortex to just the pixels inside the mask. That effects mask is applied to the tool after it gets processed.

### Basic Node Setup

Below, the Vortex runs on text to build motion graphics. Since the Vortex would swirl the text outside the text boundary, a Set Domain node serves to widen the text boundary, making sure the text is not cropped once the Vortex applies.

The Vortex is used to create swirling whirlpool effects.
