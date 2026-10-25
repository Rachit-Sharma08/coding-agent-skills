# Bookmarks and underlays as bookmarks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working in the node editor.
[Chapter index](INDEX.md) / [Previous section](fusion-1338-and-learning-to-use-the-node-editor.md) / [Next section](adding-replacing-and-selecting-nodes.md)
<a id="source-adding-inserting-and-replacing-nodes-using-the-toolbar"></a> <a id="source-adding-nodes-quickly-using-the-select-tool-window"></a> <a id="source-adding-nodes-to-a-composition"></a> <a id="source-make-sure-youre-adding-compatible-nodes"></a> <a id="source-using-bookmarks"></a> <a id="source-using-underlays-as-bookmarks"></a>

### Using Bookmarks

Reaching a Bookmark view is a matter of picking a bookmark from the Options menu or selecting Go To Bookmarks to bring up the Go To Bookmarks dialog. That dialog shows every bookmark in the sequence it was made within the current composition. A double-click on any entry there shifts the Node Editor to that view and shuts the Go To Bookmarks dialog. When your bookmark list runs long, the search field along the bottom of the dialog lets you type the name of whichever bookmark you're hunting for.

Changing the Sort Order and Assigning Keyboard Shortcuts Both the Options menu and the Go To Bookmarks dialog present bookmarks in creation order. Whichever nine sit at the top get keyboard short cuts. Reordering the list is something you do in the Manage Bookmarks dialog. That comes in handy when you want certain bookmarks tied to particular keyboard shortcuts, or when you'd rather a bookmark you made early on not carry a shortcut at all. To rearrange the listed bookmarks, follow these steps: 1 From the Options menu at the Node Editor's upper right, pick Manage Bookmarks. 2 Within the Manage Bookmarks dialog, drag a bookmark higher or lower in the list. 3 An insert line shows where the bookmark will land. Let go of the mouse button once that insert line is at the spot you want the bookmark listed. The keyboard short cuts then refresh to match the new order. TIP: Holding the Shift key lets you grab several bookmarks at once and shift them together up or down within the Manage Bookmark list.

### Using Underlays as Bookmarks

Any Underlay you drop into the Node Editor becomes a bookmark automatically. The Options menu lists them beneath your custom bookmarks. To keep Underlays out of the bookmark list, open the Go To Bookmarks dialog and switch off its Show Underlays checkbox. With that checkbox off, Underlays stay absent from the Go To Bookmarks dialog and won't turn up in the Options menu either.

### Adding Nodes to a Composition

Several routes exist for placing nodes into the Node Editor, the right one hinging on which kind of node you're after and how much help you need locating it. Beyond that, the method you use to add a node to a composition can also come down to how that node needs to attach to the existing node tree.

### Make Sure You’re Adding Compatible Nodes

A solid habit is to confirm, any time you add or insert fresh nodes into the node tree, that the nodes you're adding will work with the ones you mean to hook them onto. As an example, dropping a Blur, Color, Filter, Paint, or Position node in after almost any 2D operation gives you no trouble. Try to place a Merge3D node after a Glow node, though, and it won't link up on its own, since those two nodes can't join directly.

### Adding, Inserting, and Replacing Nodes Using the Toolbar

Above the Node Editor sits the Fusion toolbar, which lays out a set of frequently-used nodes as buttons each bearing its own icon. Through these buttons you can quickly drop in Merge, Background, Paint, Mask, Transform, and plenty of other everyday nodes with a single click or a drag of your pointer. The Fusion page toolbar. TIP: When you're unsure which node an icon stands for, simply rest your pointer on any toolbar button and a tooltip spells out that tool's full name. Ways to add nodes by clicking toolbar buttons:

- To place a node following a selected one: Pick a node in the Node Editor, then click a toolbar button.
- To drop a disconnected node into the Node Editor: Clear all selections in the Node Editor, then click a toolbar button.

Ways to add nodes by dragging toolbar buttons:

- To slot a fresh node into your node tree: Drag a toolbar button across into the Node Editor, landing it over the connection line that joins any two compatible nodes. Once the connection lights up beneath the node, release it and the node gets inserted.
- To make a disconnected node: Drag a toolbar button to a vacant spot in the Node Editor. Dragging a toolbar button into the Inspector likewise produces a disconnected node.
- To slot a new node after one loaded into a viewer: Drag a toolbar button onto a viewer, and a new node is inserted after whatever node is being viewed, whether or not any nodes happen to be selected.

To swap a node in the Node Editor for one from the toolbar: 1 Drag a toolbar button until it hovers right on top of the Node Editor node you intend to replace. The moment the node beneath lights up, release it.

Hauling a toolbar node over so it takes the place of a tool already there. 2 Click OK in the dialog to approve the swap. TIP: Whenever one node takes the place of another, any settings the two nodes share carry over into the new node. Swap a Transform node for a Merge, for instance, and the current center and angle values move from the Transform across to the Merge.

### Adding Nodes Quickly Using the Select Tool Window

After that, the quickest route for adding or inserting nodes into the Node Editor is the Select Tool window, which lets you find any node Fusion offers by typing just a few characters. Once it clicks for you, this will likely turn into one of your go-to methods for adding nodes. To add nodes via the Select Tool window: 1 Take one of the following actions to decide whether you're inserting a node or making a disconnected one:

- For an inserted node, pick a node compatible with the one you're about to make, and the new node slots in right after it.
- For a disconnected node, clear every selection.

2 Hit Shift-Spacebar to bring up the Select Tool dialog. 3 As the window opens, type characters that spell out part of the node's name you're after. A list of probable matches surfaces on its own, and the Up and Down arrow keys let you land on the right node (unless it's already chosen). If the exact tool's name escapes you, you can instead enter familiar keywords and categories (keyer, materials, and so on) to pull up a set of tools matching what you typed. 4 With the correct node chosen, press the Return key (or click OK), and that node gets inserted or added.

The Select Tool dialog finds any node in a flash when you know its name. TIP: Each time you call up the Select Tool window, it holds onto the text you typed for the next time you open it, so to add a second node of the same type—say you want two Blur nodes back to back—you can simply press Shift-Spacebar followed by Return to drop in that second Blur node.
