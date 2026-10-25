# Image processing order of operations and overall image processing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grading overview.
[Chapter index](INDEX.md) / [Next section](serial-parallel-and-layer-node-structures.md)
<a id="source-image-processing-order-of-operations"></a> <a id="source-image-processing-order-of-operations-1"></a> <a id="source-image-processing-order-of-operations-serial-parallel-and-layer-nodes"></a> <a id="source-image-processing-within-grades"></a> <a id="source-overall-image-processing"></a> <a id="source-overview"></a>

## Overview

What's inside: the Image Processing Order of Operations, plus Serial, Parallel, and Layer Nodes.

## Image Processing Order of Operations

### Image Processing Order of Operations

Once the HDR palette and Color Warper arrived in DaVinci Resolve 17 the diagram showing the sequence of every image processing operation in DaVinci Resolve, from input all the way to output, had to be revised. Laying it out in full now takes two charts, both shown in this chapter; the first lays out the broad order of operations happening across every page, whereas the second drills down into the precise order of operations inside each node of the Pre-Clip, Clip, Post-Clip, and Timeline grades you build on the Color page. Once you grasp the order of operations laid out here, harnessing the full might of the DaVinci Resolve toolset becomes much more manageable.

### Overall Image Processing

Within the chart below, every image processing operation in DaVinci Resolve appears in the sequence in which it gets processed. The operations are color-coded to mark which page their controls live on, since page order frequently has no bearing on image processing order. The reason? It comes down either to keeping each operation as clean as it can be, or to handing the user the greatest possible control over the image. On both counts, image processing order has been weighed carefully, and at times the best outcome calls for operations on separate pages to take turns with one another. Usually, this order of operations doesn't matter to a user who only cares about the final result. Even so, if you're after something highly specific, or puzzling over why a certain result shows up when you lean on the Cut, Edit, Fusion, and Color pages all together at once, this chart ought to clear things up. Finishing artists, especially, should find it enlightening.

### Image Processing Within Grades

Across Pre-Clip, Clip, Post-Clip, and Timeline grades on the Color page, the majority of Color page operations are on hand inside every Corrector node you drop into the Node Editor. Inside each node, those operations occur in the precise order below.

How image processing operations are sequenced inside every Corrector node on the Color page Because the Node Editor works in a modular way, if two image processing operations you need aren't sitting in the ideal order for your goal, you can run each one through a separate node to push those operations into whatever order suits you. In the same vein, with Layer, Parallel, or Key mixer nodes, the order of operations is readable straight from how the nodes are laid out in your node graph. All the same, most colorists lean toward spreading different operations over several nodes, whether it's strictly necessary or not, either to stay organized or to “sandbox” certain shaky decisions they may want to revisit on their own later. Nothing stops you, though, from stacking multiple operations inside one node if you'd rather keep a leaner node structure for your grading. Given how flexible the Color page is, the call is yours.
