# Combiner and disparity and disparity to z

Version: DaVinci Resolve 20.3 Reference Manual. Context: Combiner, Disparity, Disparity to z.
[Chapter index](INDEX.md) / [Previous section](anaglyph-and-combiner.md) / [Next section](disparity-to-z-outputs.md) / [Continue Disparity To Z D2Z / Camera Tab](disparity-to-z-outputs.md) / [Combiner Com](anaglyph-and-combiner.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-disparity-dis"></a> <a id="source-disparity-node-introduction"></a> <a id="source-disparity-to-z-d2z"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-outputs"></a> <a id="source-the-disparity-controls-tab"></a> <a id="source-the-disparity-node"></a> <a id="source-the-disparitytoz-node"></a>

### Inputs

The Combiner node's pair of inputs receive the two images that will be merged into a stacked stereo image. Image 1 Input: Wire the orange input to the 2D picture standing for the left eye within the stereo comp. Image 2 Input: Wire the green input to the 2D picture standing for the right eye within the stereo comp.

### Basic Node Setup

In the example below, both a left eye image and a right eye image feed the Combiner node so it can produce one stacked stereo image. Writing the stacked stereo images out as EXR files is often more efficient than computing the disparity on the fly.

Feeding a Combiner node both a left-eye and a right-eye image produces one stacked stereo image.

### Inspector

### Controls Tab

For stacking, route the left eye image into the orange input and the right eye image into the node's green input. Combine Three choices in the Combine menu govern how the two images become a stacked stereo image.

- None: Nothing happens here. What comes out matches the left eye input exactly.
- Horiz: The two images stack horizontally, side by side, with whatever feeds the

left eye input placed on the left. The result is an output image twice as wide as the input.

- Vert: The two images stack vertically, one over the other, with whatever feeds

the left eye input placed at the bottom. The result is an output image twice as tall as the input.

- Layers: This reveals layer name fields so you can rename the layers.

Swap Eyes Lets you trade the left and right eye input without fuss. Add Metadata Metadata travels alongside the images, and this checkbox lets you append it to whatever metadata already exists. To inspect Metadata, point the viewer's SubView menu at Metadata.

### Common Controls

Settings Tab This same Inspector Settings tab recurs on the other Stereo nodes too. A thorough walkthrough of these shared controls lives at the end of this chapter, within the “The Common Controls” section.

### Disparity [Dis]

### The Disparity node

NOTE: You'll find the Disparity node solely within Fusion Studio and DaVinci Resolve Studio.

### Disparity Node Introduction

Disparity computes the left/right offset across the frames of a stereo pair. It additionally computes the vertical disparity between the left/right images, which normally runs far smaller than the horizontal disparity and ideally should be 0 to keep viewing discomfort to a minimum. While inspecting the Disparity node's output in the views, your eye picks out quality and detail in the Disparity map more readily from either the grayscale X disparity or Y disparity than from the combined XY disparity shown as a Red/ Green color image.

The disparity that gets generated is kept in the output image's Disparity aux channel: the left image holds the left > right disparity while the right image holds the right > left disparity. Since disparity operates by pairing regions in the left eye with regions in the right eye through comparison of colors and color gradients, the colors in both eyes need to be as alike as you can make them. For that reason, color correcting beforehand is wise. It is equally wise to trim off any black borders ringing the frames, because those throw off the disparity tracking (and they also cause trouble if you lean on the Color Corrector's histogram match feature for the color matching). Under Stack mode, the left and right outputs hand back the same image. Should the left and right images carry an overall vertical offset of more than a handful of pixels, the disparity tracking algorithm benefits when you pre-align features across the left/right eyes vertically with a Transform node. Fine details are prone to vanishing during tracking whenever a sizable vertical offset separates the left/right eyes. Think about running a SmoothMotion node over your disparity channel. Doing so can cut the time-dependent flickering that shows up when you warp an eye. Weigh, too, whether to strip lens distortion before the disparity is computed. Skip that and your Disparity map turns into a blended Disparity and Lens Distortion map. There are upsides and downsides to this. A downside is that performing a vertical alignment afterward also undoes the lens distortion effects. To trim the computation time, begin by tweaking the Proxy and Number of Iterations sliders. The Disparity node offers no support for RoI or DoD.

### Inputs

The Disparity node's two inputs receive the left and right images. Left Input: Route either the left eye image or the stacked image into the orange input. Right Input: Route the right eye image into the green input. You only get access to this input when the Stack Mode menu sits on Separate.

### Outputs

Departing from the way most Fusion nodes work, Disparity provides two outputs, one per eye. Left Output: This carries the left eye image plus a fresh disparity channel, or a Stacked Mode image plus a fresh disparity channel. Right Output: This carries the right eye image plus a fresh disparity channel. The output only shows up when Stack Mode is set to Separate.

### Basic Node Setup

Down below, a left eye image together with a right eye image feed the Disparity node. From there the Disparity node sends each eye onward to Saver nodes. Writing the stereo images out as EXR files is often more efficient than computing the disparity on the fly.

Feeding a Disparity node both a left-eye and a right-eye image lets it build and render a stereo image

### Inspector

### The Disparity Controls tab

Proxy (for Tracking) The input images get scaled down by the proxy factor, tracked to derive the disparity, and then the resulting disparities get scaled back up again. Its sole purpose is to accelerate the disparity calculation, which can run slow. Computation time scales roughly with how many pixels the image holds. So a proxy scale of 2 yields a 4x speedup, and a proxy scale of 3 yields a 9x speedup. Broadly, a 1:1 proxy produces the most detailed flow, though bear in mind this hinges heavily on how much noise and film grain are present. With noise in heavy amounts, it can wipe out any benefit you'd gain stepping from 2:1 down to 1:1 proxy. In certain cases it can even degrade things. Picture the Proxy setting as behaving like a crude low-pass filter that strips noise and grain. Advanced The Advanced settings region holds parameter controls for fine-tuning how the Disparity map is calculated. Its defaults were settled on as the best starting values after experimenting across a wide variety of shots, and they make a sound baseline. Most of the time, no fiddling with the Advanced settings is called for. Smoothness This governs how smooth the disparity is. Raise it to better cope with noise; lower it to coax out additional detail. Edges This slider is a further smoothness control, but one keyed to the color channel. Its usual effect is to dictate how closely the disparity's edges trace the color images' edges. At a lower value the disparity grows smoother and is apt to overshoot edges. At a higher value the disparity's edges hug the color images' edges more tightly, and detail from the color channels begins bleeding into the disparity, which is rarely what you want. As a loose rule of thumb, lean toward higher values when the disparity feeds a Z channel for post effects such as depth of field, but lean toward lower values when the disparity drives interpolation. Broadly, an Edges slider set too high can bring on streaked-out edges where the disparity is used for interpolation.

Match Weight This dictates how neighboring pixels in the left image are paired up with neighboring pixels in the right image. A lower value matches large structural color features. A higher value matches small, sharp shifts in the color. A sound choice for this slider usually lands in the [0.7, 0.9] range. Pushing this option higher tends to sharpen the matching wherever differences arise from gently varying shadows or local lighting changes between the left and right images. You should nonetheless color match the starting images so they resemble each other as closely as possible; this option mainly assists with local variations (e.g., lighting differences from light passing through a mirror rig). Mismatch Penalty This dictates how steeply the penalty for mismatched regions climbs as those regions grow more unlike. The slider lets you balance between Quadratic (lower values) and Linear (higher values) penalties. Lower Quadratic settings come down hard on large dissimilarities, whereas higher Linear settings hold up better against dissimilar matches. Dragging this slider lower tends to leave the disparity peppered with small random variations, while higher values give smoother, more pleasing results. Warp Count Lowering the Warp Count speeds up the disparity computations. Notably, computation time rises linearly with this option. To grasp what it does, recognize that the Disparity algorithm warps the left image step by step until it lines up with the right image. Past a certain point, convergence is reached and further warps merely burn computation time. Fusion's default is set high enough that convergence should always occur. You may trim this value to hasten the computations, but keep an eye on how the disparity's quality slips as you do. Iteration Count Lowering the Iteration Count speeds up the disparity computations. Again, computation time rises linearly with this option. As with the Warp Count, raising this option past a certain threshold delivers diminishing returns and won't meaningfully improve the outcome. Out of the box, this value is set to something expected to converge on any conceivable shot and can frequently be dialed down without harming the disparity's quality. Filtering This menu sets which filtering operations run while the flow is generated. Catmull-Rom filtering gives finer results, yet it drives the computation time up sharply. Stack Mode This menu sets how the input images are stacked. With Separate chosen, the Right Input and Output appear, and distinct left and right images have to be wired in. Swap Eyes Ticking this checkbox makes the left and right images trade places.

### Common Controls

Settings Tab The Inspector's Settings tab likewise shows up on the rest of the Stereo nodes. You'll find these shared controls covered fully toward the end of this chapter, in the “The Common Controls” section.

### Disparity To Z [D2Z]

### The DisparityToZ node

NOTE: You'll find the Disparity to Z node solely within Fusion Studio and DaVinci Resolve Studio.
