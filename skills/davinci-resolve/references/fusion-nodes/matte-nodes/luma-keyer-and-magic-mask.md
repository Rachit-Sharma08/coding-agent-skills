# Luma keyer and magic mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Luma keyer, Magic mask.
[Chapter index](INDEX.md) / [Previous section](luma-keyer-controls-tab.md) / [Next section](magic-mask-and-matte-control.md) / [Luma Keyer LKy](difference-keyer-and-luma-keyer.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-magic-mask-magm"></a> <a id="source-magic-mask-node-introduction"></a> <a id="source-making-points-in-the-viewer"></a> <a id="source-the-magic-mask-node"></a>

### Common Controls

Settings Tab The Inspector’s Settings tab also appears in the other Matte nodes. These shared controls get a full write-up at this chapter’s close, under the “The Common Controls” section.

### Magic Mask [MagM]

The Fusion Magic Mask tool now defaults to Magic Mask v2. Its behavior lines up almost exactly with Magic Mask v2 on the Color page, apart from a few Fusion-specific interface differences. Should you want the older Magic Mask for the sake of compatibility with legacy projects, you can switch to it by ticking the Use Legacy Magic Mask checkbox down at the bottom of the tool’s inspector.

### The Magic Mask node

### Magic Mask Node Introduction

Driven by the DaVinci AI Neural Engine, the Magic Mask palette builds a mask automatically to single out one or more people or objects in the frame, steered by clicks the user applies to mark the subject to isolate. You can generate masks for a whole object or person, or for individual features of that person — their face, hair, arms, shoes, and so on. The images below illustrate these two kinds of masks with Highlight switched on in the Viewer. A red onionskin overlay reveals exactly what Magic Mask is singling out.

(Left) Magic Mask singling out skin tones alone and (right) the same tool singling out the apron alone. Notice that although the apron and the shirt are very similar in color, Magic Mask grasps the apron’s shape well enough to build the mask. Masks from Magic Mask are frequently solid enough to drive high‑quality isolated adjustments on their own, yet they won’t always come out perfect. When that happens, the Matte Finesse controls let you soften and loosen the resulting mask as much as you need in order to clean up the edge of a tricky subject you’re isolating, with help from another mask-generation method such as a qualifier key or window. For fast cleanup on a single frame, the paint tool is also there to add or take away regions of the mask by hand. When you’re isolating particular features of a person, you can additionally combine what you isolate to build precisely the mask you want. In the example above, you could isolate the face together with bare skin on the torso and arms, producing a mask for an overall skin tone adjustment that leaves out the subject’s hair and clothing. Clicks you place to identify the subject steer this entire process. The usual workflow has you making positive clicks (shown in blue) over the person or feature you want isolated. After that, if needed, you can place subtractive clicks (shown in red) over areas of the image that aren’t the person or feature you’re isolating, fixing any flaws you notice in the generated mask.

### Making Points in the Viewer

Magic Mask operates by dropping points right into the viewer. As soon as a point is laid down, the viewer immediately displays the mask you’ve built. Lay down several points to build a mask additively, and use negative points to subtract regions from the mask. Pick a frame to draw on where the object sits fully in view and unobscured. To make a positive point to add an object to a mask: Open the Magic Mask node in a viewer, then left-click and set a point on the object you want to pick. As an alternative, switch the Point Mode to Add in the Inspector and left-click to place a fresh positive point. A positive point appears in blue. To subtract an object from a mask with a negative point: Open the Magic Mask node in a viewer, then Option-left-click and drag to set a point on whatever object you want gone. As an alternative, switch the Point Mode to Subtract in the Inspector and left-click to place a fresh negative point. A negative point appears in red. To clear a point — or a whole cluster of them — out of the mask: Shift-drag around the point or cluster to select it (green), then hit the delete key. As an alternative, switch the Point Mode to Select in the Inspector, then left-click and drag a selection window across one or more points. Pressing the delete button clears them. Positive points pick out regions of like contrast and color, letting you tie intricate shapes together. Negative points subtract regions of the object you’d rather not isolate. That could be as plain as taking a car’s wheels out of a mask, or as involved as pulling specific books out of a mask of a bookshelf. Ideally you’d center both positive and subtractive clicks on the portion of the person or object you’re adding to the mask. A single point will usually pin down the object, or the part of it you mean to mask, correctly; you shouldn’t have to stack several points on one object unless it’s extraordinarily complex.

Just one blue click placed on her back masks her whole body — arms and hair included — accurately. Notably, Magic Mask v2 tells her apart from her mirror reflection, even where the two overlap.

### Inputs

In the Node Editor, the Magic Mask node carries four inputs: Input: This orange input takes a 2D image holding the luminance values you want keyed for transparency. Garbage Matte: This gray garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint points, or bitmaps masks. Wiring a mask here makes the image regions inside the matte transparent. The garbage matte goes straight onto the image’s Alpha channel. Solid Matte: This white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint points, or bitmaps masks. Wiring a mask here makes the image regions inside the matte fully opaque. Effect Mask: This optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint points, or bitmaps masks. Wiring a mask here confines the luminance key to certain pixels. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

Magic Mask accepts RGB inputs from other nodes and lets you single out particular objects in the frame for use as a mask. The tool has tracking of the mask as it shifts over time built right in. From there you can route the Magic Mask output into any mask input.

Here a Magic Mask node sends its matte into a Color Corrector that is wired to the foreground of a Merge node Inspector
