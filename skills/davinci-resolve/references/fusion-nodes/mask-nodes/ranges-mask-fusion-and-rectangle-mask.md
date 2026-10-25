# Ranges mask Fusion and rectangle mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ranges mask Fusion, Rectangle mask.
[Chapter index](INDEX.md) / [Previous section](ranges-mask-fusion-controls.md) / [Next section](rectangle-mask-and-triangle-mask.md) / [Ranges Mask RNG FUSION](polygon-mask-and-ranges-mask-fusion.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-rectangle-mask-node-introduction"></a> <a id="source-rectangle-mask-rec"></a> <a id="source-the-rectangle-node"></a>

### Common Controls

Image and Settings Tabs Other mask nodes carry the same Image and Settings tabs found here in the Inspector. A full account of these shared controls appears at this chapter’s end within “The Common Controls” section.

### Rectangle Mask [Rec]

### The Rectangle node

### Rectangle Mask Node Introduction

What the Rectangle mask makes are plain square or rectangular masks. Out of the box it builds a rectangle matching the comp’s aspect ratio, yet you get separate control over width, height, and angle, opening up a broad range of rectangular shapes.

### Inputs

A single effect mask input sits on the Rectangle mask node. Effect Mask: Into the optional blue input goes a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here merges the masks. Just how they merge is governed by the Paint mode menu over in the Inspector.

### Basic Node Setup

For turning out rectangular shapes, the Rectangle mask node comes in handy. Below, the Rectangle mask serves to make a colored square by carving a square shape out of a background node.

### Inspector

A Rectangle mask node carving a colored square out of a Background node
