# Grid warp and lens distort and perspective positioner

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grid warp, Lens distort, Perspective positioner.
[Chapter index](INDEX.md) / [Previous section](drip-and-grid-warp.md) / [Next section](perspective-positioner-and-vector-distortion-and-vortex.md) / [Grid Warp Grd](drip-and-grid-warp.md)
<a id="source-basic-node-setup"></a> <a id="source-clipping-mode"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-contextual-menu-options"></a> <a id="source-controls-tab"></a> <a id="source-grid-warp-contextual-menu-options"></a> <a id="source-grid-warp-toolbar"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-lens-distort-lens"></a> <a id="source-lens-distort-node-introduction"></a> <a id="source-perspective-positioner-node-introduction"></a> <a id="source-perspective-positioner-ppn"></a> <a id="source-the-grid-warp-viewer-toolbar"></a> <a id="source-the-lens-distort-controls-tab"></a> <a id="source-the-lens-distort-node"></a> <a id="source-the-perspective-positioner-node"></a>

### Contextual Menu Options

Within the viewer's contextual menu, the Grid Warp node adds a submenu covering both the source and destination grids. The two menus carry the identical name, and only whichever grid is active gets its menu filled with options. The remaining menu stays empty. Those contextual menu options also turn up on the toolbar shown in the viewer.

### Grid Warp Contextual Menu options

Modify Only/Done These pair of options place the mesh into Modify Only and Done modes, respectively. Pick Modify Only when you want to edit the mesh, or Modify Done to lock a mesh against further change. Smooth/Linear Reach for the Smooth and Linear options to add smoothing to selected vertices or strip it away.

Auto Smooth Points With Auto Smooth Points turned on, the grid's vertices smooth themselves automatically anytime they get moved. As a rule this stays on by default. Z Under/Z Same/Z Over Where two vertices in a grid sit on top of each other, one of them ends up clipped by the other. You use Z Under, Z Same, and Z Over to decide which vertices render in front and which render behind. Select All Choosing this selects every point in the mesh. Show Key Points, Handles, Grid, and Subdivisions Across the viewers, these four options toggle on or off whether you see the grid, the key points (vertices), the Bézier handles, plus the subdivisions. Reset Selected Points This returns the Selected Points (vertices) to their default positions. Reset All Points This returns every point (vertices) in the mesh to its default position. Stop Rendering Picking this halts rendering, disabling all rendering of the Grid Warp node until you turn the mode back off. It often helps while you make a run of fine adjustments to a complex grid.

### Grid Warp Toolbar

Anytime the Grid Warp node is selected and sits in Edit Grid mode, the views show the Grid Warp toolbar. A range of options for manipulating and adjusting the grid is offered by this toolbar. The preceding "Contextual Menu Options" section already covers the buttons that appear on this toolbar.

### The Grid Warp viewer toolbar

### Common Controls

Settings Tab Other Warp nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.

### Lens Distort [Lens]

### The Lens Distort node

### Lens Distort Node Introduction

You can use this node either to strip lens distortion from an image or to add it. How much lens distortion an image carries hinges on the lens, its quality, the count of elements, and plenty of other factors. One motive for removing lens distortion is compositing against an undistorted layer. As an example, dropping a 3D element over a distorted live-action layer produces unwanted artifacts such as straight lines failing to line up between the foreground and background. That composite ends up looking unconvincing.

### Inputs

The Lens Distort node's two inputs serve to hook up a 2D image plus an effect mask, which you can use to bound the distorted region. Input: The orange input takes the primary 2D image that gets distorted. Effect Mask: A mask shape from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools goes into the blue input. Hooking a mask here confines the distortion to just the pixels inside the mask. That effects mask is applied to the tool once the tool finishes processing.

### Basic Node Setup

In the streamlined example below, the Lens Distort runs in Undistort mode over the MediaIn1 live-action layer, the 3D elements get composited, and finally the Lens Distort runs once more at the end with identical settings, only this time in Distort mode so the image regains its original look and distortion.

Lens Distort placed twice on the live-action media: once where the node tree starts and once more right at its end

### Inspector

### The Lens Distort Controls tab

### Controls Tab

Several routes for customizing or constructing the lens distortion model you want appear on the Controls tab. Camera Settings let you state which camera captured the content. Mode Undistort strips the lens distortion to yield a flattened image. Distort restores the original lens distortion into the image. Edges Decides how samples landing beyond the frame get treated.

- Canvas: Pixels beyond the frame take on the default canvas color. Usually that is black with no alpha.
- Duplicate: Pixels beyond the frame get duplicated. The upshot is "smeared" edges, yet that proves handy when, for instance, applying a blur, because black pixels would otherwise cause unwanted blurring between the real image and the black canvas.

### Clipping Mode

- Domain: Holds onto every pixel that might be pushed out of the frame, ready for later re-distorting.
- Frame: Pixels pushed beyond the frame are discarded.

Output Distortion Map Puts out the locations of pixels as a warped screen-coordinate map. Camera Settings The options familiar from the Camera 3D are duplicated here. You can either dial them in manually or link them to an existing Camera 3D.

Lens Distortion Model From this control, pick whichever 3D Equalizer Lens Distortion model fits — your choices being 3DE Classic Model, 3DE4 Anamorphic, 3DE4 Radial Fisheye, and 3DE4 Radial. For more explanation, consult the 3D Equalizer manual. When no lens data has been imported, the sliders in the 3DE Classic LD Model are likely the best fit for applying (un)distortion by hand. Supersampling [HiQ] Sets how many samples decide each destination pixel. As ever, more supersampling drives render times up. Usually 1×1 bilinear delivers adequate quality, though with heavy lens distortion close to the lens edges, the gap to higher settings becomes noticeable. Supersampling Mode [HiQ] Which kind of sample gets taken for every supersample. Nearest produces a sharper image, though one that is more aliased. A blurrier outcome comes from Bi-Linear. Load Distortion Data Lets the user pull in a Lens Distortion profile authored, say, by the 3D Equalizer. How to Manually Determine Lens Distortion Ideally you would hold exact lens parameters for every lens used during the shoot and could feed those values in to undistort the image. In reality, though, those parameters either were never recorded on set or fail to match. Another route is software like 3D Equalizer, which studies the footage and hands back a dataset you can import straight into the Lens Distort node. And lastly, you could attempt to eyeball the lens distortion amount manually with the control sliders. To do so, you might either hunt for horizontal or vertical lines in the footage that ought to be straight and straighten them out via the controls, or shoot a full-frame checkerboard pattern on set to serve as a reference.

### Common Controls

Settings Tab Other Warp nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.

### Perspective Positioner [PPn]

### The Perspective Positioner node

### Perspective Positioner Node Introduction

The Perspective Positioner serves as the counterpart to the Corner Positioner node. By dropping corner points onto a perspective distorted area, it "unpins" an image and thereby pulls the perspective off it. You can also turn this function to wobbling and warping the image by animating the points over time.
