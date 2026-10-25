# Node editor basics and thumbnail optional nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node editing basics.
[Chapter index](INDEX.md) / [Next section](labeling-nodes-and-selecting-nodes.md)
<a id="source-a-simple-serial-arrangement-of-corrections"></a> <a id="source-node-badges-and-labels"></a> <a id="source-node-editing-basics"></a> <a id="source-node-editing-basics-part-1"></a> <a id="source-node-editor-basics"></a> <a id="source-the-components-of-a-node-tree"></a> <a id="source-the-node-editor-interface"></a> <a id="source-the-node-editors-pan-hand-tool"></a> <a id="source-thumbnail-optional-nodes"></a>

### Node Editing Basics

This chapter walks through the essentials of working with the Node Editor in DaVinci Resolve to organize every adjustment you choose to make to a clip, plus the core routines for editing and arranging nodes inside a tree, which form the foundation for building more elaborate effects.

### Node Editor Basics

Out of the box, each clip starts with a single node in the Node Editor that holds the initial corrections you apply. That said, nothing stops you from adding more nodes, with each one holding one or several corrections that act on the image.

The Node Editor showing a reasonably full-featured grade The particular way you lay out your nodes gives you fine control over the sequence in which your grade's operations run, and that brings plenty of benefits. The discussion here walks through assorted approaches to building, editing, and laying out node trees so you can tap the full capability of DaVinci Resolve.

### Thumbnail-Optional Nodes

Within the Node Editor option menu there's a Show Thumbnails entry that lets you turn off or turn on the thumbnails sitting on each Corrector node.

Turning thumbnails off through the Node Editor option menu shrinks the height of nodes How Many Nodes Do I Need to Use? Throughout this chapter and the ones to follow, you'll pick up a wide range of methods for blending adjustments and nodes in assorted ways to reach very particular results. Naturally, people new to DaVinci Resolve frequently ask themselves, just how far should I take this? No single correct answer exists, but it's fair to say that a handful of the planet's top colorists pull off gorgeous work in as few as three or four nodes, while others habitually assemble carefully structured stacks of ten to twenty nodes, or even more. How many nodes you reach for tends to hinge on the quality of footage you've been handed, since well-lit material generally demands less effort than run-and-gun footage shot with whatever light was around, which usually calls for far more tweaking before it looks acceptable. On top of that, the count of nodes you might reach for can also hinge on the type of project at hand, where commercial spots give the colorist enough room in the budget to construct enormous grades tuning every tiny detail, while narrative features and TV shows push you to move quicker and accomplish more inside fewer adjustments so you keep pace. So what's the true answer? Every grade calls for exactly as many nodes as it needs. Not one more, not one fewer.

### The Node Editor Interface

While working inside the Node Editor, you might want to zoom in or out for a closer or wider view of the node tree, and to scroll around the canvas when handling sizable groups of nodes. To grow the Node Editor's working canvas:

- Drag the divider between the Node Editor and the Viewer leftward or rightward to widen or narrow it.
- Right-click somewhere inside the Node Editor (anywhere but on a node) and pick Toggle Display Mode; that conceals the Viewer and shifts the Node Editor over to the right of the Gallery, growing it substantially. Right-click again and pick Toggle Display Node to go back to the standard layout.

To lay out the node tree so it fits your present working canvas:

- Right-click somewhere in the Node Editor (anywhere but on a node) and chose Cleanup Node Graph out of the contextual menu. That reshuffles your node tree to suit whatever sized canvas you've got at the time.

To zoom plus pan inside the Node Editor, try one of these:

- Drag the Node Editor's zoom slider to make the nodes smaller or bigger.
- Click the Pan tool (the hand icon) over at the top-left corner of the Node Editor, then drag inside the gray region of the editor to scroll the view.
- Hit the H key to flip between selection and pan modes.
- Middle-click and drag inside the editor to scroll the view.
- Right-click and choose Zoom In or Zoom Out.
- Right-click and pick Zoom to Window to size the node tree to the node graph's present dimensions.
- Right-click and pick Original Size to send the node graph back to its default scale.

### The Node Editor’s Pan (Hand) tool

### The Components of a Node Tree

Elaborate grades can call for trees built from several nodes to produce the desired result. This part of the chapter covers how nodes get assembled into the arrangements detailed more fully later on. Each node you place is a "Corrector" node, able to perform either primary or secondary correction, based on whether you switch on the Qualifier/Window/Matte controls. Even so-called "Serial" and "Parallel" nodes are really just Corrector nodes connected in series or in parallel relative to the prior node in the tree; their labels simply reflect how they got added. Every Corrector node carries two inputs and two outputs, allowing you to handle the RGB image-processing channel apart from the Key channel, which marks regions of isolation for image processing or transparency used in compositing. The RGB connections show up as light green and sit at a node's upper left and right. Blue marks the Key connections, which sit along a node's lower left and right. A node's inputs take the form of triangles, while its outputs are squares. These inputs and outputs are how you steer the flow of image and isolation channels in and out of every node throughout the tree.

A lone node, where the RGB (green) plus key (blue) triangular inputs and square outputs stand out plainly

Nodes link to each other through "connections," which show up as lines joining one node to another. Image data travels left to right, beginning at the Source input way over on the left side of the Node Editor, passing through each node in turn, and finishing at the Node Tree output over on the right side of the Node Editor.

### A simple serial arrangement of corrections

Below is a rundown of the various pieces of a simple node tree in which every node sits in serial, one following the next, and how they cooperate:

- Source Input: The green source node way over on the left is the clip's image data after the Sizing and Source decode settings have processed it, ungraded. The Source input supplies RGB data into the grade, and links to the RGB input of the first node in your tree. When needed, you can wire the Source input into several Corrector nodes at once, spawning multiple parallel image-processing streams that branch off the image's original source state and that you can later merge back together in assorted ways with the Parallel or Layer Mixer nodes.
- Nodes: Every node in the node graph stands for a set of image processing operations that you can switch on or off independently of any other node in the graph. By splitting operations across multiple nodes, you gain precise command over the sequence of every image processing operation in DaVinci Resolve, letting you build many distinct corrections and effects. The green RGB inputs and outputs serve to wire these nodes to one another. Each node's thumbnail image reveals how the clip appears at that specific point in the grade, offering a visual cue about what each node accomplishes, and small badges beneath each node tell you which particular operations that node is applying.
- RGB Inputs and Outputs: Sitting at each node's upper right and left, the green inputs and outputs let you carry the RGB image coming out of one node into the next node's RGB input. For a Corrector node to do anything, you have to wire both its RGB input and its RGB output to adjacent nodes in the tree. On top of that, every single node in the Node Editor has to be connected for a grade to function; leaving any node disconnected in the tree shuts that grade off until everything is wired up.
- Key Inputs and Outputs: Sitting at each node's lower right and left, the blue inputs and outputs route the key channel produced by a node's Qualifier or Window controls, or pulled in via a Matte clip you'd earlier paired with a clip on the Media page. Wiring the key output of one node into the key input of another essentially duplicates the first node's key onto the second. You can additionally merge the key outputs from several nodes in assorted ways using the Key Mixer node.
- Node Tree Output: A tree's final node must have its RGB output wired into the green Node Tree output node, the step that "completes the circuit" of image processing and passes that correction along to the next stage of the DaVinci Resolve image processing pipeline. When the output stays unconnected, the node tree is shut off and does nothing to the clip. Only one RGB output can be wired into the Node Tree output at any given time.
- Second Source Input (for RED HDRx): You can reach the alternate highlight exposure of RED HDRx media by revealing this optional second Source input.

For further detail on “Mulit‑Channel RED HDRx Support,” turn to Chapter 147, “Channel Splitting and Image Compositing,”

- Second Source Input (from Fusion page): You're also able to spin up extra sources that route in masks or mattes built on the Fusion page so they can serve as keys over in the Color page.
- Alpha Output: You can carve out areas of transparency for compositing right inside DaVinci Resolve by wiring a key output into an optional Alpha output.

For more information, see Chapter 146, “Combining Keys and Using Mattes.”

### Node Badges and Labels

Nodes show up with assorted labels and badges that help you tell what each one is adding to the overall grade. The length of a label and the count of badges shown hinge on how big each node is, which is governed by the Node Editor's Zoom slider.

Nodes displaying the sorts of labels and badges on offer for telling which operations each node carries out Node number: Each node bears a number matching the order in which it appears in the node graph. Adjustment badges: As you run various operations inside a node, small badges show up below the thumbnail marking which palettes were used on that node. The number of badges you can see hinges on how far in or out you've zoomed into the Node Editor, and whether Color Space or HDR labels are already eating up some of that space. With bigger nodes, more badges fit across the node's width. Every palette on the Color page carries its own distinct badge. Should you run more operations than a node has room to show, one lone "downward arrow" badge shows up. Animation badge: Nodes carrying animated parameters show a keyframe badge.
