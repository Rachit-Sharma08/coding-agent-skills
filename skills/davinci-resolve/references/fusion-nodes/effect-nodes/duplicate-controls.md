# Duplicate controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Duplicate.
[Chapter index](INDEX.md) / [Next section](duplicate-angle-adjustment-with-centered-pivot.md)
<a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-duplicate-controls"></a> <a id="source-duplicate-dup"></a> <a id="source-duplicate-node-introduction"></a> <a id="source-effect-nodes"></a> <a id="source-effect-nodes-part-1"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-the-duplicate-node"></a>

### Effect Nodes

Here you will find documentation covering the Effect nodes in Fusion.

You can type the short abbreviation shown beside each node name into the Select Tool dialog while looking up tools, and these abbreviations also serve scripting purposes. Throughout this text, any node tree that depicts MediaIn nodes inside DaVinci Resolve should be read as equivalent to Loader nodes within Fusion Studio, except where a difference is called out.

### Duplicate [Dup]

### The Duplicate node

### Duplicate Node Introduction

Much like its counterpart the Duplicate 3D node, this Duplicate node lets you rapidly clone any 2D image while feeding each clone an incremental transform, which builds tiling patterns and intricate object arrays. Controls found under the Jitter tab make uneven transforms possible, for instance randomized placement or scaling.

### Inputs

This node exposes a pair of inputs: one for a 2D image and one for an effect mask that confines where the cloned objects show up. Input: The orange input takes the principal 2D image to be cloned. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask here keeps the cloned objects visible solely within the masked pixels. Such a mask is processed after the tool itself has run.

### Basic Node Setup

There are many possible ways to wire and apply this node, with assorted inputs feeding it. In the example below, which produces motion graphics, a masked Background node yields a round shape that the Duplicate node then clones.

A Duplicate node used to create a repeating circular object

### Inspector

### Duplicate controls

### Controls Tab

Within the Controls tab sit every parameter for generating, shifting, and resizing copies of whatever object feeds the node's input. Copies This slider governs how many copies get produced. Every copy is derived from the previous one. With a setting of 5, the parent gets copied, that copy is then copied, the copy of that copy is copied next, and the chain continues. Such chaining yields intriguing results once you apply transforms to each copy through the parameters that follow. Time Offset Drag the Time Offset slider to shift any animation on the source image by a fixed step for each copy. As a demonstration, dial the value to -1.0 with a square rotating on the Y-axis serving as the source. Your first copy displays the animation one frame back. The next copy displays it a frame earlier still, continuing in sequence. On textured planes this is especially powerful, since consecutive clip frames can be displayed at once. Center The X and Y Center fields establish the positional offset given to every copy. Setting an X offset of 1 nudges each copy one unit along the X-axis away from the prior one.

Pivot The Pivot fields fix where the pivot point lands when you alter the size, position, or angle of each copy. That pivot stays put rather than traveling with either the source object or the cloned array. If you want the pivot to track the array, you must adjust the Pivot fields yourself. Size The Size field dictates the scaling amount given to each copy. Angle The Angle field specifies the degree of Z rotation given to each copy. This angular change scales linearly according to where the pivot point sits.
