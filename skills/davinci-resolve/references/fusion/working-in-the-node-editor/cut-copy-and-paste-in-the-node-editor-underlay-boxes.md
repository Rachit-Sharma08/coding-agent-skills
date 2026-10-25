# Cut copy and paste in the node editor underlay boxes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cut copy and paste in the node editor.
[Chapter index](INDEX.md) / [Previous section](cut-copy-and-paste-in-the-node-editor-instanced-nodes.md) / [Next section](switching-thumbnails-between-images-and-icons.md) / [Cut, Copy, and Paste in the Node Editor](node-view-indicators-and-clipboard.md)
<a id="source-choosing-which-nodes-show-thumbnails"></a> <a id="source-force-active-tile-pictures"></a> <a id="source-force-all-tile-pictures"></a> <a id="source-force-mask-tile-pictures"></a> <a id="source-force-source-tile-pictures"></a> <a id="source-manually-showing-tile-pictures-and-node-options"></a> <a id="source-node-thumbnails"></a> <a id="source-using-underlay-boxes"></a>

### Using Underlay Boxes

Underlay Boxes give you a tidy way to associate a group of nodes that cooperate on one particular task in your composition. They amount to nothing more than colored rectangles you can drop nodes inside. After you set nodes within an Underlay, moving the Underlay carries every node inside it along too.

An Underlay in the Node Editor. Underlay Boxes can be given names to mark the purpose of that group of nodes, and can be colored so as to stand apart from other Underlay Boxes or to follow some color scheme across your compositions. Methods of working with Underlay Boxes:

- To create an Underlay Box: Click the Node Editor spot where you would like the Underlay Box to land. Then press Shift-Spacebar, type under, and once the Underlay Box turns up in the Select Tool window, hit the Return key. Failing that, open the Effects Library, head into the Tools > Node Editor category, and either click or drag the Underlay Box node to spawn a fresh one.
- To create an Underlay Box around specific nodes: Within the Node Editor, select the nodes that the Underlay Box should wrap. Then press Shift-Spacebar, type under, and once the Underlay Box turns up in the Select Tool window, hit the Return key. Failing that, open the Effects Library, head into the Tools > Node Editor category, and click the Underlay Box node, which gets added and sized so it wraps each selected node.
- To resize an Underlay Box: Drag any edge or corner to grow or shrink it.
- To rename an Underlay Box: Option-click the Underlay Box so just the box, not its contents, is picked, then right-click it and pick Rename (or hit F2). Key a fresh name into the Rename dialog and click OK or press Return.
- To recolor an Underlay Box: Option-click on it so just the box, not its contents, is picked, then right-click it and select a color out of the Set Color submenu.
- To put nodes inside of an Underlay Box: Pick the nodes you want set within an Underlay Box, then drag them so they sit inside. The Underlay Box has to be big enough to hold every node. As an alternative, set an Underlay Box beside a cluster of nodes you want enclosed, then resize the Underlay Box to enclose all of them.
- To move an Underlay Box and all its nodes: After nodes have been set inside an Underlay Box and then deselected, you can shift the whole cluster of nodes at once by dragging the Underlay Box by its title bar.
- To remove nodes from an Underlay Box: There are a couple of ways to take nodes back out of an Underlay Box. With both the Underlay Box and the nodes deselected, drag a bounding box or Command-click to pick every node in the box you want out, then drag them clear.

Shrink the Underlay Box until it is smaller than the cluster of nodes it first enclosed. The moment an Underlay Box gets so small that even the final node pokes past its edge, those nodes drop out of the Underlay Box automatically, and you are free to move or delete the Underlay Box without those nodes following.

- To delete an Underlay Box together with every node within: Pick an Underlay Box and tap the Delete key to wipe out both the Underlay Box and each node housed inside. Should you want the nodes spared, drag them clear of the box beforehand.
- To delete an Underlay Box yet retain every node within: Option-click the Underlay Box so it alone, not the nodes, is picked, then tap the Delete key. The enclosed nodes stay right where they sat.

### Node Thumbnails

After a source or an effect joins the Node Editor, a node stands in for it. By default nodes are thin rectangles, which makes it simpler to pack reasonably complicated grades into a fairly small space. Still, if you prefer, node thumbnails can be displayed instead.

A node in the Node Editor shown without and with a thumbnail. A node can appear as a small rectangle or as a larger square. In the rectangular form the node’s name runs through its middle, whereas the square form displays the tool’s icon or else a thumbnail of whatever image the node puts out. TIP: Even with node thumbnails switched off, you can swiftly pull up detailed information about a node and the data it is handling by hovering your pointer over it in the Node Editor and reading the tooltip bar below.

### Choosing Which Nodes Show Thumbnails

Should you want node thumbnails to help you pick out media and operations by sight within your node trees, the contextual menu that appears on a right-click anywhere in the Node Editor background offers an assortment of options for which nodes ought to display thumbnails.

### Force All Tile Pictures

Picking this option puts a thumbnail on every last node in the Node Editor. It can render simple node trees easier to read, yet it makes every node tree occupy a good deal more space. NOTE: With Show Thumbnails enabled, nodes might not refresh until the playhead is nudged in the Time Ruler.

### Force Active Tile Pictures

You also have the choice to show thumbnails only on the nodes currently selected, which can clarify which node you are working on. Once nodes are deselected, their thumbnails hide away again.

### Force Source Tile Pictures

This switches on thumbnails for all MediaIn and Loader nodes in the Node Editor, along with every generator, and offers a great way to spot at a glance where all the clips sit within a composition.

### Force Mask Tile Pictures

This switches on thumbnails for all Mask nodes throughout a composition, which can make them simpler to tell apart while you build intricate shapes assembled from several Mask nodes.

### Manually Showing Tile Pictures and Node Options

You also have the choice of picking by hand which nodes should show thumbnails. As an example, at certain key junctures of the node tree you might want a compact visual cue of how the composition is shaping up. Turning thumbnails on or off for one or more particular nodes works thus: 1 Within the Node Editor, select one or more nodes. 2 Right-click any of those selected nodes, and from the contextual menu pick one of these:

- Show > Show Tile Pictures
- Show > Show Modes/Options

Once you have switched thumbnails on by hand for various nodes, they stay visible regardless of whether those nodes are selected.
