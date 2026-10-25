# Labeling nodes and selecting nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node editing basics.
[Chapter index](INDEX.md) / [Previous section](node-editor-basics-and-thumbnail-optional-nodes.md) / [Next section](node-tree-preview-restore-and-cache.md)
<a id="source-disabling-all-nodes"></a> <a id="source-disabling-individual-nodes"></a> <a id="source-disabling-multiple-nodes-all-at-once"></a> <a id="source-disabling-nodes"></a> <a id="source-labeling-nodes"></a> <a id="source-resetting-nodes"></a> <a id="source-selecting-nodes"></a> <a id="source-selecting-three-nodes-by-dragging-a-bounding-box"></a> <a id="source-the-node-editors-selection-tool"></a> <a id="source-turning-grades-andor-fusion-effects-off"></a>

### Labeling Nodes

You can give nodes labels to mark what a given node does within your grade. That can make revisiting a grade months down the line far simpler. Node labels also get stored whenever you save a still, so labels can likewise make a saved grade easier to read much later. At each node's default size in the Node Editor, nodes can show up to 12 characters of text, though bigger nodes can hold more.

To label a node: 1 Right-click a node and pick Change Label. 2 Enter whatever label text you'd like, then hit Return. What you typed appears above that node within the Node Editor. To edit a node's label:

- After a node carries a label, you're free to revise that label whenever you like by double-clicking it.

### Selecting Nodes

Whichever node is currently chosen in the Node Editor gets highlighted in orange, and goes by the name current node. Whenever you tweak any parameter or setting on the Color page, you're tweaking parameters inside the current node. Only a single node can be selected at once. To pick a node, turning it into the current node, do one of the following:

- Click any node in the node graph.
- For the prior one, pick Color > Nodes > Previous Node (Option-Shift-Semicolon); for the following one, pick Color > Nodes > Next Node (Option-Shift-Apostrophe). Used this way, the final node loops back to the first, and likewise in reverse.

The chosen node shows up highlighted in orange. You're also able to pick several nodes at once, getting ready to do things such as relocating them or building compound nodes (covered later in this chapter). To select multiple nodes:

- Command-click each of the nodes you want to simultaneously select.
- With the Node Editor Selection tool active (found at the editor's top-left corner), just drag a bounding box across the nodes you want to select.

### The Node Editor’s Selection tool

When several nodes are selected, each shows up highlighted in white, save for the current node, which stays orange.

### Selecting three nodes by dragging a bounding box

Whenever you pick a different clip in the Timeline, the standard behavior has the last node that was active when you last worked that clip become the one selected when you revisit it. That said, a setting named "Switching clips," found both in the Node Editor's option menu and in the User Preferences Color panel, lets you change how this works. To learn more about this setting, refer to Chapter 4, “System and User Preferences.”

### Disabling Nodes

As you build a node tree, it's frequently handy to switch one or more chosen nodes off so they stop affecting your grade. It's likewise handy to switch the whole node tree off and on so you can view "before and after" looks at the current clip. Disabled nodes get skipped during rendering, and they stay disabled when you store that grade with a still in the Gallery and then apply that grade to a different shot.

### Disabling Individual Nodes

Switching off a single node comes in handy for temporarily parking adjustments you suspect you won't keep but aren't ready to throw away (though bear in mind it's frighteningly easy to accidentally switch these nodes back on). It's also great for showing your client a before and after look at the most recent adjustment. To flip a single node off and on, try one of these:

- Click any node's number in the node graph to switch off that one node on its own.
- Pick one node, then choose Color > Nodes > Enable/Disable Selected Nodes (Command-D).

### Disabling Multiple Nodes All At Once

When you've selected more than one node in the node tree, using any of the techniques for switching nodes off and on covered above (Command-D included) toggles Enable/Disable Selected Nodes. Keep in mind that the current node ringed in orange always counts as part of the selection. This makes before/after comparisons easy for any mix of nodes doing intricate adjustments by selecting them, while leaving the un-selected nodes that handle base adjustments you want kept enabled untouched.

### Disabling All Nodes

Beyond the Bypass All Grades command, switching off every node in a grade at once is another simple route to disabling a grade so you get a before and after of the clip's original state (or its color managed state if Resolve Color Management (RCM) is turned on). More to the point, it's a solid way to switch off all of a grade's nodes ahead of guiding your client through each operation in that grade node by node, switching each one on in sequence as you describe how it's enhancing the image. To flip every node off and on simultaneously, try one of these:

- Pick Color > Nodes > Enable/Disable All Nodes (Option-D), which flips every node off and on.

IMPORTANT: When you switch every node off and then back on, every node gets re-enabled, including ones you'd previously disabled one at a time.

### Turning Grades and/or Fusion Effects Off

Living in the Viewer's title bar, the Bypass Color Grades and Fusion Effects button/drop-down commands can likewise be reached via the View > Bypass Color and Fusion menu commands. Switching off Fusion effects over on the Color page is a simple way to boost playback performance on underpowered machines when all you need is to knock out a few quick grading adjustments. Flipping grades off and on is also a handy way to grab a fast before and after view of a shot where the "before" goes right back to the source itself. Picking Toggle Bypass, or clicking the Viewer control, disables whatever happens to be checked in the optional menu, leaving you to decide whether to bypass both Color and Fusion together, or only one of the pair.

(Left) The menu commands that bypass Color and Fusion; (Right) the Timeline Viewer controls on the Edit page

### Resetting Nodes

When you're unhappy with your present operations and want a fresh start, there are three approaches to resetting nodes in the Node Editor. These show up as entries in the Color menu.

- Reset Selected Node Grade: Returns whichever node is currently selected to its default parameter settings, wiping out every keyframe along the way.
- Reset Grades and Keep Nodes: Sends every node across the current tree back to the default parameter settings while leaving the tree's structure untouched; each node stays put right where it sat, just reset.
- Reset All grades and Nodes: Wipes out every node and keyframe and brings back one lone node set to the default parameter settings. Resetting nodes via the mouse is another option, and it's a fast move if you happen to already be in the Node Editor handling other tasks.

Methods of resetting nodes with the mouse:

- To reset a selected node: Right-click the node in question, then pick Reset Node Grade out of the contextual menu.
- To reset all grades and nodes: Right-click on any empty backdrop of the Node Editor, then pick Reset All Grades and Nodes out of the contextual menu.

Methods of resetting nodes with the keyboard:

- To reset a selected node: Press (Shift-home).
- To reset all grades and nodes: Press (Command-home).
- To reset all grades and keep nodes: Press (Shift-Command-home).
