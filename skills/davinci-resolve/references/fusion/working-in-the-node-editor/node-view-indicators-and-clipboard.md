# Node view indicators and cut copy and paste in the node editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node view indicators, Cut copy and paste in the node editor.
[Chapter index](INDEX.md) / [Previous section](node-view-indicators-node-order-matters.md) / [Node View Indicators](node-view-indicators-deselecting-nodes.md) / [Next section](cut-copy-and-paste-in-the-node-editor-pasting-node-settings.md)
<a id="source-automatically-creating-a-merge-node-by-connecting-two-outputs"></a> <a id="source-connection-options-and-routers"></a> <a id="source-cut-copy-and-paste-in-the-node-editor"></a> <a id="source-cut-copy-and-paste-nodes"></a> <a id="source-extracting-and-inserting-nodes"></a> <a id="source-swapping-node-inputs"></a> <a id="source-using-routers-to-reshape-and-branch-connections"></a> <a id="source-working-in-the-node-editor-part-3"></a>

### Automatically Creating a Merge Node by Connecting Two Outputs

Here's a perpetually handy shortcut for when you've got a stray node you want composited over another. Pull a connection from the output of the node you mean to be the foreground layer and drop it onto the output of the node you mean to be the background layer, and a Merge node gets built automatically to assemble that composite.

Pulling a connection out of a stray node onto another node's output (top), then dropping it to spin up a Merge node composite (bottom).

### Connection Options and Routers

Out of the box, the Node Editor uses linear connections drawn as a straight line between any two wired nodes. Efficient as that is, it can sometimes leave connection lines crossing over nodes, which some folks feel clutters the view of the Node Editor.

Linear connections between nodes. If you prefer, you can switch how connections are drawn by turning on orthogonal connections, which auto-draws lines with right angles so connections steer clear of overlapping nodes.

Optional orthogonal connections between nodes. As far as your composition goes there's no difference; this only changes how your node tree looks. To switch how connections are drawn in the Node Editor:

- Right-click the Node Editor background and pick one of the following from the contextual menu.
- Options > Direct Pipes
- Options > Orthogonal Pipes

### Using Routers to Reshape and Branch Connections

When you want to push a given connection into an angle to keep your node tree neat, a router dropped onto either a linear or an orthogonal connection will impose that angle, so the line draws however you'd like.

A router dropped in to bend a connection into an angle. Routers are minuscule nodes sporting a lone input and an output, but with no parameters beyond a comments field (found in the Inspector), where you can jot notes about what's unfolding in that stretch of the composition. Even handier, you can branch a router's output across multiple nodes, which makes routers all the more useful for keeping node trees tidy when you want to branch one part of your node tree's output to other nodes sitting clear across at the far end of that same node tree.

A router branching its output to multiple nodes.

Ways to work with routers:

- To add a router to a connection: Option-click anywhere along a connection.
- To move a router: Drag the router somewhere new, and the connection reshapes itself as needed.
- To branch a router's output: Pull a connection out of the router output onto some other node's input. There's no cap on how often you can branch one router's output.
- To remove a router: Highlight any router and hit the Delete key, or else right-click a router and pick Delete off the contextual menu.

### Swapping Node Inputs

On multiple-input nodes like the Merge, Merge 3D, and Dissolve nodes, there's a fast way to swap the Primary and Secondary inputs—the foreground and background inputs of a Merge tool, for instance—when you realize you've wired them up backwards by mistake. Should a node have more than two of its inputs wired, only the foreground and background inputs trade places. To swap the primary inputs of a multi-input node, take one of these actions:

- Select a node and press Command-T to flip its inputs.
- Right-click a node and pick Swap Inputs from the contextual menu.

With node inputs before the swap (left) and after the swap (right), the connections stay put while the colors shift. Inputs can slide freely around the node, so swapping two of them leaves the connection lines in place; instead, the inputs switch color to show you've flipped the background (orange) and foreground (green) connections.

### Extracting and Inserting Nodes

As you build a composition, you'll regularly hit a point where nodes you've already laid down need rearranging so you can wire them differently for a better outcome. Happily, that's easy: extract one or more nodes from one stretch of a node tree and slot them into another stretch. To extract one or more nodes from where they sit in the node tree:

- To extract a single node: Hold the Shift key, drag a node up or down out of the node tree to disconnect it, then drop the node before you let go of the Shift key. That node is now loose, and the next upstream node's output auto-wires to the next downstream node's input to close the gap in the node tree.
- To extract multiple nodes: Select the nodes you mean to pull out, hold Shift, and move any one of those selected nodes upward or downward to cut them loose, then drop the node before you let go of the Shift key. Those nodes are now loose (though still wired to one another), and the next upstream node's output auto-wires to the next downstream node's input to close the gap in the node tree.

The view with a pair of nodes still in place (left), then with that pair pulled out (right). Once a node has been extracted, you can set it back down into another connection somewhere else. Only a single node goes in at a time. To wedge a disconnected node into the Node Editor between two compatible nodes: 1 Holding Shift, drag the disconnected node so it sits squarely over a connection joining two other nodes. 2 The instant that connection lights up, drop the node, then release the Shift key. That node is now wired into the nodes coming before and after it.

Before inserting a node (left), and after inserting a node (right). TIP: Hold the Shift key and you can extract a node and slot it in somewhere else in one single drag.

### Cut, Copy, and Paste Nodes

The familiar cut, copy, and paste operations are on hand in the Node Editor as well. You can lean on them to pull nodes out of the Node Editor for a moment, spin up duplicate nodes, or even lift the settings off one node and drop those settings onto another node whose settings are compatible.

### Cut, Copy, and Paste in the Node Editor

The usual commands all work, though with a few extra touches particular to the Node Editor. To copy one or more selected nodes, take one of these actions:

- Right-click a node and pick Copy from the contextual menu.
- Choose Edit > Copy from the Edit menu (Command-C).

To cut one or more selected nodes, take one of these actions:

- Right-click over the node and pick Cut from the contextual menu.
- Choose Edit > Cut from the Edit menu (Command-X).

Pasting into the Node Editor produces a copy of the last node or nodes you cut or copied. As you paste, a few different moves let you steer where the pasted nodes land. To paste one or more selected nodes, take one of these actions:

- To paste nodes to be inserted after another node: In the node tree, pick the node you want the pasted node(s) inserted after, then go to Edit > Paste (Command-V).
- To paste nodes so they sit apart from the remainder of the node tree: Clear every node selection, then go to Edit > Paste (Command-V), or right-click any spot in the Node Editor and pick Paste from the contextual menu.
- To paste disconnected nodes into a particular region of the Node Editor: Clear every node selection, then click the Node Editor spot where the pasted node(s) should land, and go to Edit > Paste (Command-V), or right-click any spot in the Node Editor and pick Paste from the contextual menu.
- To paste a node that takes the place of one already in the Node Editor: Right-click whichever Node Editor node you mean to replace, pick Paste from the contextual menu, and when a dialog pops up asking whether to replace that node, click OK. This works solely by way of the contextual menu command.

TIP: When you paste a MediaIn, Loader, or Generator node so that it lands after a selected node in the node tree, a Merge tool gets built automatically and used to composite the pasted node by hooking it into the foreground input. Though this can spare you a couple of steps, certain artists would rather carry out such merges by hand, and that preference can be set through the Defaults panel within the Auto tools section of the Fusion > Fusion Settings.
