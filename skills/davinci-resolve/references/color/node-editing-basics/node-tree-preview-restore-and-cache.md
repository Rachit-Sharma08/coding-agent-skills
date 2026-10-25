# Previewing and restoring node trees and caching specific nodes to improve performance

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node editing basics.
[Chapter index](INDEX.md) / [Previous section](labeling-nodes-and-selecting-nodes.md) / [Next section](extracting-a-node-and-inserting-a-node.md)
<a id="source-adding-nodes"></a> <a id="source-adding-nodes-with-windows-turned-on"></a> <a id="source-caching-specific-nodes-to-improve-performance"></a> <a id="source-connecting-and-disconnecting-nodes"></a> <a id="source-deleting-nodes"></a> <a id="source-editing-node-trees"></a> <a id="source-node-editing-basics-part-2"></a> <a id="source-previewing-and-restoring-node-trees"></a>

### Previewing and Restoring Node Trees

There are two more ways to swiftly handle unwanted changes you've applied to node trees, with no need to lean on undo. Preview Memory: Gives you a preview of how any saved grade would look on the current clip. For a preview, pick Color > Preview Memory (Option-Shift-P), then right-click whatever saved still sits in the Gallery (or Memory) and pick Add Correction. You can in fact lean on Add Correction to sample as many stills as you wish. Should you like any still's look, just leave it as is. If none of the stills you sampled appeal to you, then picking Color > Preview Memory once more returns the clip to its original grade. Original Memory: This command lets you swiftly send a clip's grade back to the state it had when you first picked that clip. You reach it by choosing Color > Original Memory (OptionShift-O). It's handy for jumping straight back to a clip's original grade after you've made a run of changes you now regret. Picking a different clip in the Timeline and then reselecting the clip you changed resets what counts as the current grade.

### Caching Specific Nodes to Improve Performance

You can mark particular nodes for caching, together with every node sitting upstream of them in that node tree. By caching nodes that run processor-heavy effects, you reclaim real time headroom for the remaining downstream nodes in a grade. Picking Playback > Render Cache > User caches only the nodes you've marked for caching. Pick Playback > Render Cache > Smart mode and DaVinci Resolve handles caching on its own for any nodes running Motion Blur, Noise Reduction, or OFX plugins, with no effort on your part. To mark a node, plus every correction in upstream nodes, for caching:

- Right-click whatever node you want and pick Node Cache > On out of the contextual menu.

### Editing Node Trees

You face no cap on how many nodes you can build and wire to one another, and you can dial in as many or as few parameter adjustments as you please inside each node. The procedures below describe how you can add nodes to the node graph while assembling each grade's node tree.

### Adding Nodes

The most basic way to grow a node tree's complexity is to tack on more nodes, so you can heap further adjustments onto the current grade. You can add nodes such that they automatically attach to nodes already in the tree, ready for immediate tweaking, or you can drop unattached nodes into empty spots of the tree while gearing up to build a particularly complex and specific node tree for a tough job.

Ways to drop nodes into the tree with a mouse, tablet, or trackpad:

- To place any sort of node into the graph with the mouse: Right-click a node within the tree, then pick the node type you'd like from the contextual menu's Add Node submenu.
- To place a disconnected node into the graph: Right-click on the empty backdrop of the node graph, then pick Add Node > Corrector out of the contextual menu. A disconnected node does nothing to a tree until it's wired in.

Ways to add a node onto a currently selected node in the tree by keyboard:

- For a serial node placed after the selected node: hit Option-S key, or via the menu pick Color > Nodes > Add Serial.
- For a serial node tacked onto the tree's very end: hit Option-K, or via the menu pick Color > Nodes > Append Node.
- For a serial node placed ahead of the selected node: hit Shift-S, or pick Color > Nodes > Add Before Current.
- For nodes set in parallel with the selected node: hit Option-P, or via the menu pick Color > Nodes > Add Parallel.
- To layer a node onto the selected node: hit Option-L, or via the menu pick Color > Nodes > Add Layer.
- For an outside node attached to the selected node: hit Option-O, or via the menu pick Color > Nodes > Add Outside Node.

### Adding Nodes with Windows Turned On

For convenience, there are also dedicated commands that drop in serial nodes with Circular/Linear/Polygon/Curve windows already switched on. To place a node into the tree with its Window turned on automatically: pick whichever Nodes menu entry lines up with the following:

- Node + CPW: Circular Power window (Option-C)
- Node + LPW: Linear Power window (Option-Q)
- Node + PPW: Polygonal Power window (Option-G)
- Node + PCW: PowerCurve window (Option-B)

Any time you add a node to a tree, it gets numbered in sequence right after the most recent node you'd added, no matter where it lands in the tree. As an example, if you've already placed three nodes, and you then decide to slot another one between Nodes 1 and 2, the fresh node becomes Node 4, and the node order reads 1, 4, 2, and 3.

### Deleting Nodes

When there's a node you no longer want, you can opt to strip it out of the tree entirely to wipe out its effect for good. To delete a node, do one of the following:

- Select a node, then press the Forward-Delete key.
- Right-click a node, and choose Delete Node.

Once you've deleted a node, the nodes on either side of the one you removed get wired together automatically so the tree stays unbroken. On top of that, every node in a tree gets renumbered following any node's deletion, so there's no gap in node order. For instance, if a tree holds three nodes numbered in sequence and you delete the second, the node that used to be number 3 becomes 2.

### Connecting and Disconnecting Nodes

For a node tree to function, every node in the Node Editor has to be wired into a working node tree, running from the Source input, through each node along the way, to the Node Tree output. Any node left disconnected will cause that clip's grade to be disabled. Even so, you may find you need to detach parts of a node tree so you can rewire them differently. To connect two disconnected nodes:

- Drag a connection out from one node's RGB or key output across to the matching RGB or key input on another node, and once the line lights up, let go of the mouse button.

To change the connection from one node to another:

- Hover the pointer above the latter half of any connection line joining two nodes until it lights up blue, then click and drag to wire it instead into a different input, whether on that same node or a different one.

To disconnect two nodes, do one of the following:

- Place the pointer above the right-hand portion of a node connection so it lights up, then click it to remove it.
- Click a link to select it (a selected link turns orange), then hit the Delete or Forward-Delete key.
- Right-click a link and choose Delete Link.

To overwrite a node’s previous connection:

- A connection can be dragged onto a node input or output that already has one, and doing so replaces the existing connection with whatever new one you're dragging in. As you do, the connection due to be replaced lights up in orange.
- Any node's RGB or Key output can feed as many inputs as you please, yet a node's input takes only a single connection. The lone exception is a node carrying multiple inputs, built to merge the output of several nodes. Among these are the Parallel, Mixer, and Key Mixer nodes.
