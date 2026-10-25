# Extracting a node and inserting a node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node editing basics.
[Chapter index](INDEX.md) / [Previous section](node-tree-preview-restore-and-cache.md) / [Next section](copying-node-stack-layers-and-post-group-node-stack-layer.md)
<a id="source-beforeafter-using-cleanup-node-graph"></a> <a id="source-copying-and-pasting-all-settings-from-one-node-to-another"></a> <a id="source-extracting-a-node"></a> <a id="source-inserting-a-node"></a> <a id="source-keeping-node-trees-organized"></a> <a id="source-node-context-menu-actions-can-have-assigned-shortcut-keys"></a> <a id="source-rearranging-node-order"></a> <a id="source-track-node-changes-using-color"></a> <a id="source-using-node-stack-layers"></a>

### Extracting a Node

Now and then you'll want to pull a node out of where it currently sits in the node tree, so that whatever nodes flank it on the left and right rejoin one another on their own, sparing you a manual reconnect. The term for this is extracting a node. To extract a node, do one of the following:

- Select a node, and choose Color > Nodes > Extract Current Node.
- Select a node, and press E.

Bear in mind that a disconnected node in the node tree halts grading entirely, so you'll want either to rejoin that node to some other part of the node tree or to delete it; leaving it disconnected in the Node Editor isn't an option.

### Inserting a Node

Whenever a disconnected node sits in the Node Editor, dropping it into the node tree between any two other nodes is straightforward. The same holds for nodes you drag in from elsewhere — say, out of a Gallery still's exposed node tree. Here's how to slot a disconnected node in between two others:

- Drag a disconnected node, or one out of a different node tree, onto the connection that joins two other nodes within a node tree; the moment a plus icon shows over the node under your cursor, let go to drop it in.

### Rearranging Node Order

How your tree's nodes are wired in sequence shapes what a grade produces. Suppose, for instance, you lift the highlights in the first node, then go to isolate a region of the picture in a second node only to realize it's already been clipped; you might have to rework your order of operations to get the best corrections. To swap the contents of two nodes:

- Command-drag any node and let it fall onto another node so the operations inside each one trade places. The nodes themselves seem not to budge, but the node badges below should make clear that the operations have been swapped.

Relocating a node anywhere else within the node tree goes like this: 1 In the node tree, Double-click a node and hit E to extract it, lifting it out of the tree so it sits unattached. 2 Drag that now-loose node onto the connection line between any two other nodes in the tree, and as a small plus icon shows, drop it so the node wires itself into that spot in the node tree.

### Copying and Pasting All Settings From One Node to Another

The most basic move is to copy every one of a node's settings and paste them into a different node. That makes it painless to replicate things such as windows, qualifier settings, keyframing, or motion tracking you'd like to reuse in another node as the starting point for a fresh operation. It's likewise a fast route to manually rippling a tweak you made in a node out to that same node in a different clip's grade. Copying a node's settings between one clip and another can be done in either of these ways:

- Option-drag one node onto another. On release, the dragged node's settings replace those of the node you dropped onto.
- Select a node holding settings you'd like to copy and choose Edit > Copy (Command-C). Next, select a node to receive those settings — within the current grade or within another clip's grade — or build a new node, then choose Edit > Paste (Command-V) to drop in the settings you copied. These pasted node settings supersede whatever settings that node carried before.

NOTE: There are additional methods of copying nodes and individual node settings.

For more information, see Chapter 142, “Grade Management.”

### Node Context Menu Actions Can Have Assigned Shortcut Keys

Shortcut keys can be tied to frequently used Node Context menu actions such as Lock Node, HDR Mode, Clean Up Selected Node Graph, and so on. Head to Keyboard Customization > Commands > Panels > Color Nodes to set those shortcuts up.

### Keeping Node Trees Organized

Keeping how your nodes sit in the node graph tidy and orderly pays off. A neat tree is far easier to read should you come back to a grade down the road, and it also helps other colorists on the same project make sense of your work. The procedures that follow lay out how to shuffle the nodes in your tree, plus the node tree working area, so you stay on top of your grades. To move nodes within the Node Editor:

- Drag any node to a new position.
- Command-click or pull a bounding box around several nodes you'd like to move, then drag the lot to a new position. Naturally, it's all too easy to overdo it. After a frenzied stretch on a complex grade, if you wind up gazing at a jumble of disorganized nodes, putting your node graph back in order is quick thanks to a pair of commands in the Node Editor contextual menu.

For tidying up the node graph, right-click within the Node Editor and pick:

- Cleanup Node Graph: Shifts every node in the node graph into an evenly spaced grid. Connection lines get rerouted around nodes so clutter is kept down.

### Before/after using “Cleanup Node Graph”

Should your grading have drifted only a little out of hand, the Cleanup Node Graph command can run across several clips at once. To do that, pick the clips whose node graphs need tidying in the thumbnail timeline, then right-click inside one of those node graphs and, off the drop-down menu, choose “Cleanup Selected Node Graphs.” That carries out a Cleanup Node Graph operation across all the selected clips together.

### Track Node Changes Using Color

On the Color Page node graph (3-dot) option menu sits an option labeled Track Node Changes Using Color. It's a per system setting where you pick the node color to be applied to nodes that are newly created or modified. Within a multi-user collaboration environment, every colorist can assign their own preset node color. From there, the node color tells you at a glance who last touched a given node. For single user cases, the feature works to track which nodes and grades changed past some moment in time, such as a client review session.

Picking Track Node Changes Using Color off the Node Graph option menu will, going forward, recolor a node's color bar after any change you make to it. Here, the Highlights node's color bar has turned Violet now that the Violet user has altered it.

On top of that, timeline clips can be filtered by their node colors too. For this, just click the Down Arrow in the Clips tab, move over Node Color, and click the color you'd like to filter by. Run through the same steps again to filter several colors. Once set, the timeline shows only the clips bearing the chosen node colors. Resetting node colors across several selected clips at once is possible too, rather than doing each one on its own. For that, pick the clips whose node colors need clearing and, off the Node Graph Option (3-dot) Menu, choose “Reset all node colors.” You'll get a warning dialog to confirm the choice.

### Using Node Stack Layers

Node Stack Layers make complex grading workflows manageable by spinning up multiple sequential node graphs that let you carve grades into distinct sections. Users can thereby split apart related functions — stabilization, corrections, hero grades, and display trims — into separate node layers. Grade operations such as ripple, reset, and editing can run on a per-layer basis as well. Grab a still to the Gallery and every one of the Node Stack Layers is stored along with that still. Because Node Stack Layers apply in sequence (from lowest up to highest), you can also wield them as highly customizable, reusable filters for your grades.

The Node Stack Layers number and naming options in the Project Settings By way of Project Settings > General Options > Node Stack Layer Count, users set how many clip node layers there are. Custom names for the layers — “primaries,” “secondaries,” “finishers,” and the like — are an option too. NOTE: Should you for any reason go back to the settings and reduce the count of node stack layers afterward, every grade in those layers is wiped across your whole project. Recovering them is just a matter of restoring the layer numbers.

You navigate the Node Stack Layer by clicking the dots above the node graph or choosing the active layer's name from the drop-down menu on the right. From there users can pick individual layers either via the navigation dots over the node graph or through that layer drop-down menu on the right. IMPORTANT: Every node layer hits the clip in this order — pre-clip, L1, L2, L3, L4, post‑clip, and then Timeline.
