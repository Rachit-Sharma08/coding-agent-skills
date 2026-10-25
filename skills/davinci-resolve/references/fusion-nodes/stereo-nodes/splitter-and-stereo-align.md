# Splitter and stereo align

Version: DaVinci Resolve 20.3 Reference Manual. Context: Splitter, Stereo align.
[Chapter index](INDEX.md) / [Previous section](new-eye-and-splitter.md) / [Next section](stereo-align-and-z-to-disparity.md) / [Splitter Spl](new-eye-and-splitter.md)
<a id="source-apply-to"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-3"></a> <a id="source-mode"></a> <a id="source-outputs-3"></a> <a id="source-stereo-align-node-introduction"></a> <a id="source-stereo-align-sa"></a> <a id="source-the-stereo-align-controls-tab"></a> <a id="source-the-stereoalign-node"></a>

### Common Controls

Settings Tab Across the other Stereo nodes as well, this Inspector Settings tab is duplicated. A thorough description of these common controls appears at the chapter's end in the "The Common Controls" section.

### Stereo Align [SA]

### The StereoAlign node

NOTE: Access to the Stereo Align node is limited to Fusion Studio and DaVinci Resolve Studio.

### Stereo Align Node Introduction

Remarkably flexible for sorting out Stereo trouble, this node can carry out any of the following actions, or mixes of them:

- Vertical alignment of one eye to the other
- Changing the convergence
- Changing the eye separation

Folding these operations into a single node lets you run them with just one image resampling. At heart, picture this node as scaling and translating the disparities, then leaning on those modified disparities to interpolate across the views. NOTE: Shifting the eye separation can open up holes, and filling them may prove impossible when the needed information isn't present in either image. Even where that information exists, the disparity might have mismatched the holes. Filling the holes by hand may be necessary. Only the RGBA channels are touched by this node.

TIP: Instead of interpolating the aux channels, Stereo Align destroys them. The disparity channels especially get consumed/destroyed. Place another Disparity node after the StereoAlign whenever you want Disparity generated for the realigned footage.

### Inputs

You wire the left and right images into the two inputs on the Stereo Align node. Left Input: Either the left eye image or the stack image hooks into the orange input. Right Input: The right eye image hooks into the green input. That input is on hand only while the Stack Mode menu is set to Separate.

### Outputs

Differing from most Fusion nodes, Stereo Align carries two outputs, one per eye. Left Output: Out of this comes the left eye image fitted with a fresh disparity channel, or else a Stacked Mode image fitted with one. Right Output: Out of this comes the right eye image fitted with a fresh disparity channel. That output is visible only if Stack Mode sits on Separate.

### Basic Node Setup

In the example below, the Stereo Align takes in the left and right eye images along with disparity. After the adjustments are done, another Disparity node follows it to produce disparity for the realigned footage.

A Stereo Align node wipes out the disparity channel, hence another Disparity node sits downstream of it Inspector

### The Stereo Align Controls tab

### Controls Tab

Vertical Alignment This option sets how the vertical alignment gets divided between the two eyes. Customarily the left eye is held untouchable and the right eye is aligned to it so resampling artifacts are avoided. While doing per pixel vertical alignment, roughly pre-aligning the images with a global Y-shift ahead of disparity computation can help, because the disparity generation algorithm may struggle to resolve small objects that travel large distances. Mind the lens distortion as well: even two perfectly vertically aligned cameras still show vertical disparities owing to lens distortion. The sound practice is to strip the lens distortion out before the disparity is computed. Carry out a vertical alignment of the right eye and you've essentially pulled the Y-component of the lens distortion from the right eye, which then looks wrong later when you go to distort it once more.

### Apply to

- Right: Only the right eye is adjusted.
- Left: Only the left eye is adjusted.
- Both: Across both the left and right eyes, the vertical alignment is shared evenly.

### Mode

- Global: To match up, the eyes are merely nudged up or down by the Y-shift.
- Per Pixel: Leaning on the disparity, the eyes get warped pixel by pixel to bring them into vertical alignment.

Bear in mind this may bring on sampling artifacts and edge artifacts. Y-shift Y-shift is on hand only while the Mode menu sits on Global. To land a match you can either tune the Y-shift by hand, or else drag the Sample button onto the viewer so it draws from the left eye's disparity channel. Recall too that, if you use this node to alter disparity, the Sample button is off-limits while you view the node's output. Snap to Whole Pixels Turning this option on snaps the global shift to whole pixels. With it on, no resampling of the image occurs; instead a plain shift happens, so there's no softening or image degradation. Convergence Point The Convergence Point section serves as a global X-translation of the L/R images. Apply to This menu decides which eyes convergence touches. You may aim the convergence at the left eye, the right eye, or split it between the two. Usually this ends up on Split. Set the eyes to Split and the convergence gets shared 50-50 across both eyes. Splitting the convergence over both eyes hands you half the shift in each, which in turn yields smaller holes and artifacts to clean up later. The cost is that you've resampled both eyes rather than holding one eye as a pure reference master. X-shift You can either move the slider to tune the X-shift by hand for a match, or use the Sample button to draw from the disparity channels for easy point-to-feature alignment. Snap This option lets you snap the global shift to whole pixels. In this mode, no resampling of the image happens; rather a plain shift takes place, so there's no softening or image degradation. Eye Separation Eye Separation alters the gap between the left/right eyes, making objects in the left/right eyes converge or diverge more according to how far they sit from the camera. The effect matches the Eye Separation option found in the Camera 3D node.

Separation This is a scale factor for eye separation.

- At 0.0, the eyes go untouched.
- Push it to 0.1 and, in each eye, every scene object's shift grows by 10%.
- Push it to 0.1 and every object's shift is scaled down by 10%.

In contrast to the Split option for vertical alignment, which shares the alignment effect 50-50 over both eyes, the Both option lays 100-100 eye separation onto both eyes. While altering eye separation, turning on per-pixel vertical alignment is frequently wise; without it, interpolation drawing on both frames can produce a doubled-up result. Left/Right Eye Options Independently for the left and right eye, the left and right eye options hold depth ordering and warp direction controls. Depth Ordering Depth Ordering decides which portions of the image render on top. Warping images often produces overlap. Where the image overlaps itself, two choices govern which values draw on top.

- Largest Disparity On Top: In the sections that overlap, the higher disparity values get drawn frontmost.
- Smallest Disparity On Top: In the sections that overlap, the lower disparity values get drawn frontmost.

Clamp Edges Under some conditions this option removes the transparent gaps that can appear at the edges of interpolated frames. Clamp Edges introduces a stretching artifact near the frame's edges, especially noticeable as objects move through it or as the camera moves. On account of those artifacts, it's smart to apply Clamp Edges only for patching small gaps around an interpolated frame's edges. Edge Softness Tones down the stretchy artifacts that Clamp Edges might introduce. With more than one of the Source Frame and Warp Direction checkboxes on, the stretching effect near the edges can double up. In that case keep softness fairly low, around 0.01. With only one checkbox on, a larger softness near 0.03 is fine. Source Frame and Warp Direction Blending up to four different warps yields this node's output. You may use the color values from the left or right frame together with the Forward (left > right) Disparity or the Backward (right > left) Disparity. Now and then you'll want to replace an eye that's already there. To regenerate the right eye, say, you'd use left eye warps alone. Experimenting with the various options to see which gives the best effect pays off. Calling on both the left and right eyes can plug gaps along the left/right side of images. Calling on both the Forward/Backward Disparity, meanwhile, can yield a doubled-up effect wherever the disparities disagree with one another.

- Left Forward: Draws on the Left frame and the Forward Disparity to interpolate the resulting frame.
- Right Forward: Draws on the Right frame and the Forward Disparity to interpolate the resulting frame.
- Left Backward: Draws on the Left frame and the Back Disparity to interpolate the resulting frame.
- Right Backward: Draws on the Right frame and the Back Disparity to interpolate the resulting frame.

Stack Mode Under Stack Mode, the L and R outputs put out the same image. With High Quality off, the interpolations rely on nearest-neighbor sampling, giving a "noisier" result. To be sure High Quality is on, right-click beneath the viewers near the transport controls and pick High Quality off the pop-up menu. Swap Eyes Makes exchanging the left and right eye outputs effortless.
