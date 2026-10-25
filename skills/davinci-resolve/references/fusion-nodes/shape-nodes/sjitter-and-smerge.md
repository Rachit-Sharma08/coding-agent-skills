# Sjitter and smerge

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sjitter, Smerge.
[Chapter index](INDEX.md) / [Previous section](sellipse-and-sexpand-and-sgrid-and-sjitter.md) / [Next section](sngon.md) / [sJitter](sellipse-and-sexpand-and-sgrid-and-sjitter.md)
<a id="source-basic-node-setup-6"></a> <a id="source-basic-node-setup-7"></a> <a id="source-common-controls-4"></a> <a id="source-common-controls-5"></a> <a id="source-controls-6"></a> <a id="source-controls-7"></a> <a id="source-external-inputs-5"></a> <a id="source-external-inputs-6"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-smerge"></a> <a id="source-the-sjitter-controls-tab"></a> <a id="source-the-smerge-controls-tab"></a> <a id="source-the-smerge-node"></a>

### External Inputs

Within the Node Editor, this node's tile shows the single input listed here. Input1: [orange, required] This input takes the output of another Shape node. Whatever shape you wire here is offset, distorted, and animated per the sJitter node settings.

### Basic Node Setup

Fed an array of shapes out of a sGrid or sDuplicate node, the sJitter node randomly shuffles their position, size, and rotation. The sExpand's output may then head onward to a further Shape node, or into a sRender node, for viewing or for compositing within the wider node tree.

A sGrid-generated array of shapes fed into an sJitter node, which then randomly offsets or scales them

### Inspector

### The sJitter Controls tab

### Controls

The Controls tab provides range sliders that set the variation amount for offset, size, and rotation. The Point Jitter parameters serve to offset the invisible points making up the vector shapes. Jitter Mode The Jitter Mode menu lets you choose between static position and size offsets or switching on an auto-animation mode. Leaving the default Fixed selection lets you offset a grid of shapes, animating with keyframes or modifiers when needed. The Random menu selection auto-animates the parameters according to the range you set with the range sliders. Leave every range slider in its default position and no random animation arises. Widen the range on any single parameter and it animates randomly across the span those range sliders define. Shape X and Y Offset These parameters fix the horizontal plus vertical offset away from the shape array's starting placement. Because it's random, the shapes throughout the array don't all offset by an equal amount. Shape X and Y Size Here you set, horizontally and vertically, the scaling applied to every shape across an array. The left range value pulls the scale down, while the right range value pushes it up. Being random, the array's shapes won't all scale by the same degree. Shape Rotate This parameter rotates every shape across an array. Point Jitter With the X and Y Point Jitter parameters you draw on the vector control points to warp the shape. The result can give ellipses a distressed look or hand other shapes a wobbly animation.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sMerge

### The sMerge node

The sMerge node merges shapes much like a standard Merge node, except the sMerge node can take more than two shape inputs. As with nearly every Shape node, the sMerge node's output is only viewable through a sRender node.

### External Inputs

The node shows only two inputs at first, but as each shape node hooks up, a fresh input appears on the node, making sure one is always free to bring a new shape into the composite. Input[#]: These multi-colored inputs serve to connect multiple Shape node. There is no ceiling on how many inputs this node will take. The node dynamically tacks on more inputs as needed, ensuring at least one input stays available at all times.

### Basic Node Setup

The sMerge node serves to fuse two Shape nodes. As for layering, each subsequent input lands over the previous one. For instance, the first shape wired to the orange input sits as the bottom-most shape, the green input layers over it, and a third shape on the pink input becomes the topmost layer.

A trio of shapes merged within an sMerge node, then sent on to an sRender for viewing and further processing.

### Inspector

### The sMerge Controls tab

### Controls

The sMerge node's single control is the Override Axis checkbox, which takes over the shape's axis.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.
