# Delta keyer node introduction starting point for a delta keyer setup

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delta keyer node introduction.
[Chapter index](INDEX.md) / [Previous section](chroma-keyer-and-delta-keyer-node-introduction.md) / [Delta Keyer Node Introduction](chroma-keyer-and-delta-keyer-node-introduction.md) / [Next section](delta-keyer-node-introduction-delta-keyer-key-tab.md)
<a id="source-basic-node-setup-5"></a> <a id="source-inputs-5"></a> <a id="source-key-tab-view-mode"></a> <a id="source-matte-nodes-part-2"></a> <a id="source-starting-point-for-a-delta-keyer-setup"></a> <a id="source-the-delta-keyer-view-mode-menu"></a>

### Inputs

Inside the Node Editor the Delta Keyer node carries five inputs. Input: The orange input takes a 2D image holding the color you want keyed for transparency. Garbage Matte: The gray garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and any image areas inside the matte turn transparent. The garbage matte goes straight onto the image's alpha channel. Solid Matte: The white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and any image areas inside the matte become fully opaque. Clean Plate: Takes in whatever image the Clean Plate node produces. Effect Mask: The optional blue input anticipates a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines the keying to certain pixels. An effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

Getting going with the Delta Keyer starts by opening it in the Inspector; from there, click and drag the background color eyedropper tool over into the Viewer to pick the color you want keyed out. That color then goes gray in the Viewer. One Delta Keyer rarely nails perfect results, since most green- or blue-screen shots carry issues the keyer wasn't built to take on. Keyers commonly need a hand from garbage mattes or solid mattes drawn with a Polygon or B-Spline node. Some shots also call for more than a single keyer to reach perfect results. That's shown in one of the examples below, where the first Delta Keyer builds a hard inner white matte while a second Delta Keyer captures the soft edges. The core matte below then wires into the solid matte input on the second Delta Keyer. Color correction, spill suppression included, is best run as its own branch in your node tree. Keeping your matte separate from your color correction through underlays makes plain which branch of nodes is doing what.

### Starting point for a Delta Keyer setup

A larger key setup using two Delta Keyers, Polygon and B-Spline nodes to supply mattes, plus a separate branch handling color correction Inspector

### The Delta Keyer View Mode menu

### Key Tab View Mode

The View Mode menu sits at the top of the Inspector. Its default pick shows the final result. You can switch the view to inspect various midway stages of the keying process.

- Pre Matte: Shows the output of the Pre Matte key.
- Matte: Shows the key's alpha before it's combined with the solid and garbage masks.

To view the matte, switch the viewer over to the alpha channel.

- Tuning Ranges: Paints a false color across the image's Shadow, Midtone, and Highlight ranges. The red channel carries Shadows, the green channel carries Midtones, and the blue channel carries Highlights.
- Status: Surfaces detail marking which regions are solid, transparent, or somewhere between. It likewise reveals zones touched by matte tweaks like thresholding or erode/dilate, plus zones the solid mask reached.
- Intermediate Result: The original source image color channels merged with the finished matte. If you like, feed this output into further Delta Keyer nodes.
- Final Result: The completed keyed image, spill-suppressed and set to merge onto a scene.
