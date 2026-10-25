# Node editor and adding nodes to your composition

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](customizing-the-toolbar.md) / [Next section](navigating-the-node-editor-and-vertical-node-editor-layouts.md)
<a id="source-adding-nodes-to-your-composition"></a> <a id="source-identifying-node-inputs-and-node-outputs"></a> <a id="source-node-editing-essentials"></a> <a id="source-node-editor"></a> <a id="source-removing-nodes-from-your-composition"></a> <a id="source-three-nodes-connected-together"></a>

### Node Editor

At the core of Fusion sits the Node Editor, since this is where you assemble the tree of nodes behind each composition. Every node you drop into the node tree contributes one specific operation that yields a single effect—be that blurring the picture, tweaking color, laying down paint strokes, drawing and adding a mask, pulling a key, generating text, or merging two images into one.

The Node Editor displaying a node tree creating a composition It can help to picture each node as a layer in an effects stack, save that you're free to steer image data any which way to branch off and recombine parts of your composite in thoroughly nonlinear fashion. That makes intricate effects easy to assemble, and just as easy to follow, because the node tree works as a flowchart too, plainly laying out everything going on once you've learned how to read it.

### Adding Nodes to Your Composition

However you feel like working, there are several routes for bringing nodes out of the Effects Library into your composition. With most of these routes, when a single node is selected in the Node Editor, fresh nodes get tacked on after it automatically, but when nothing is selected or several nodes are, then fresh nodes arrive disconnected from everything else.

Methods of adding nodes include:

- Click a button in the toolbar.
- Open the Effects Library, track down the node you want in its category, and click once on

a node you'd like to add.

- Right-click a node and pick Insert Tool from the drop-down menu to drop it in after the

node you right-clicked. Or you can right-click the Node Editor's background and lean on that submenu to drop in a disconnected node.

- Hit Shift-Spacebar to bring up a Select Tool dialog, type letters matching the name of the node you're after, and press the Return key (or click OK) once it surfaces. After you've picked this route up, it'll likely turn into one of your go-to ways of adding nodes.

As long as you know its name, the Select Tool dialog turns up any node in a flash.

### Removing Nodes from Your Composition

Getting rid of nodes is just a matter of selecting one or more of them, then hitting the Delete or Backspace keys.

### Identifying Node Inputs and Node Outputs

Every node shows small colored connections ringing its edges. Inputs are shown by one or more arrows, while the square connection stands for the tool's processed output—of which there's never more than one. Hover the pointer over any of a node's inputs or its output and that input or output's name pops up in the Status bar right away. Hold there a few seconds longer and a floating tooltip shows the same name directly above the node.

### Node Editing Essentials

Each node carries inputs and outputs that get "wired together" through connections. Arrows stand for the inputs, marking how image data travels from one node onward to the next, with each node laying down its effect and passing the result (by way of the square output) along to the next node in the tree. This way, you can swiftly assemble intricate results out of a chain of fairly simple operations.

### Three nodes connected together

A single node's output can be wired into the inputs of several nodes (this is termed "branching").

A single node branching out to a pair, sending the image down two separate operations You can then merge images together by routing the output from several nodes into certain nodes such as the Merge node, which folds multiple inputs down into one output.

Two nodes being merged together into one to create a composite Out of the box, fresh nodes get laid out left to right in the Node Editor, yet they can equally run top to bottom, right to left, bottom to top, or every direction at once. Connections reorient themselves automatically across all four sides of each node, holding the tidiest possible look as you reshuffle other connected nodes.

A node may face whichever way you like; tracing the input arrows shows you how image data flows through.
