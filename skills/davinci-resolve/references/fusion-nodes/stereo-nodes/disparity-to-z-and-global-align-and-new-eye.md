# Disparity to z and global align and new eye

Version: DaVinci Resolve 20.3 Reference Manual. Context: Disparity to z, Global align, New eye.
[Chapter index](INDEX.md) / [Previous section](disparity-to-z-outputs.md) / [Next section](new-eye-and-splitter.md) / [Disparity To Z D2Z](combiner-and-disparity-and-disparity-to-z.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-global-align-ga"></a> <a id="source-global-align-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-new-eye-ne"></a> <a id="source-new-eye-node-introduction"></a> <a id="source-outputs"></a> <a id="source-rotation"></a> <a id="source-the-global-align-controls-tab"></a> <a id="source-the-globalalign-node"></a> <a id="source-the-new-eye-node"></a> <a id="source-translation-x-and-y"></a>

### Common Controls

Settings Tab The Inspector's Settings tab is mirrored on the other Stereo nodes as well. A full rundown of these common controls sits at this chapter's end inside the "The Common Controls" section.

### Global Align [GA]

### The GlobalAlign node

NOTE: You'll only find the Global Align node within Fusion Studio and DaVinci Resolve Studio.

### Global Align Node Introduction

Unlike Stereo Align, this node makes no use of optical flow whatsoever. Its purpose is to give you a quick, handy means of basic stereo alignment across X and Y plus rotation. Slotting Global Align in at the start of the node chain helps you visually fix big gaps between the left and right eye ahead of computing Disparity. Hand-correcting large left-right discrepancies, along with laying down an initial color match, lets Disparity turn out more accurate results.

### Inputs

You wire the left and right images into the two inputs on the Global Align node. Left Input: Either the left eye image or the stack image hooks into the orange input. Right Input: The right eye image hooks into the green input. That input shows up only while the Stack Mode menu is set to Separate.

### Outputs

Differing from most Fusion nodes, Global Align carries two outputs, one per eye. Left Output: Out of this comes the freshly aligned left eye image. Right Output: Out of this comes the freshly aligned right eye image.

### Basic Node Setup

The usual home for Global Align is right at the top of the node tree. In the example below it goes in between the left and right eye images and the Disparity node so major differences can be visually corrected.

A Global Align node put to work hand-fixing mismatches between the left and right eyes

### Inspector

### The Global Align Controls tab

### Controls Tab

Translation and rotation controls for hand-aligning the stereo images live in the Controls tab.

### Translation X and Y

- Balance: Sets how the global offset gets laid onto the stereo footage.
- None: No translation is applied.
- Left Only: Only the left eye moves; the right eye stays put.
- Right Only: Only the right eye moves; the left eye stays put.
- Split Both: The two eyes shift in opposing directions.

Snap to Nearest Pixel As you turn the X or Y shift dial, this option keeps the image shifting in whole-pixel steps alone so quality stays at its best. Doing so sidesteps sub-pixel rendering of the image, which could bring on faint blurring.

### Rotation

- Balance: Sets how the global rotation gets laid onto the stereo footage.
- None: No rotation is applied.
- Left Only: Only the left eye turns; the right eye stays put.
- Right Only: Only the right eye turns; the left eye stays put.
- Split Both: The two eyes rotate in opposing directions.

Angle The rotation's angle gets set with this dial. Remember the outcome hinges on the Balance settings. Rotate only one eye by, say, 10 degrees and that eye receives the full 10-degree turn. Rotate in Split mode and one eye picks up a -5 degree turn while the other gets a +5 degree one. Translation Filter Method Depending on what your footage contains, this menu picks the filter method that yields the best results.

Visualization This control offers various color encodings of the left and right eye, a convenient way to inspect what the controls above did without tacking on an extra Anaglyph or Combiner node. Switch it to None for the final output. Stack Mode Sets the way the input images stack. Switched to Separate, the right input and output surface and you must connect distinct left and right images. Swap Eyes Under Stacked Mode, the left and right images of stereo pairs can be exchanged.

### Common Controls

Settings Tab This Inspector Settings tab also turns up on the rest of the Stereo nodes. You'll find these common controls covered thoroughly toward the chapter's close in the "The Common Controls" section.

### New Eye [NE]

### The New Eye node

NOTE: Only Fusion Studio along with DaVinci Resolve Studio offers the New Eye node.

### New Eye Node Introduction

By interpolating between two existing stereo images via the embedded disparity channels, the New Eye node builds a brand-new image. The node can also swap one view for a warped rendition of the other. Under Stack Mode, the L and R outputs put out the same image. Mapping the left eye onto the right eye to replace it is possible. That can come in handy while clearing errors from particular regions of the frame. Rather than interpolate the aux channels, New Eye wipes them out. The disparity channels in particular get consumed/destroyed. Tack on another Disparity node after the New Eye whenever you need Disparity generated for the realigned footage.
