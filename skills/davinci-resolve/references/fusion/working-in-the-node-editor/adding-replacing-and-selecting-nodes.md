# Adding replacing and selecting nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working in the node editor.
[Chapter index](INDEX.md) / [Previous section](bookmarks-and-underlays-as-bookmarks.md) / [Next section](node-view-indicators-deselecting-nodes.md)
<a id="source-adding-inserting-and-replacing-nodes-using-the-contextual-menu"></a> <a id="source-adding-nodes-from-the-effects-library"></a> <a id="source-deleting-nodes"></a> <a id="source-disconnected-nodes"></a> <a id="source-selecting-and-deselecting-nodes"></a> <a id="source-selecting-nodes"></a> <a id="source-the-active-node"></a>

### Adding Nodes from the Effects Library

Where the toolbar surfaces many of the most common nodes you'll reach for in any composition, the Effects Library holds every tool Fusion has, sorted by category, each one ready to drop quickly into the Node Editor. When you want extra help tracking down a node, or you'd just like to poke around and see what's on hand, the Effects Library makes an ideal starting point. To open the Effects Library:

- Click the Effects Library button on the UI toolbar across the top of the Fusion window. The Effects Library opens in the Fusion window's upper-left corner and is built from two panels. The category list on the left presents every available category of nodes and presets, while the list on the right reveals everything inside whichever category you've selected.

The Tools bin of the Effects Library exposing 3D nodes. Out of the box, the category list displays the main effect groups: Tools, Open FX, Templates, and LUTs; with disclosure controls on the left that reveal, in a hierarchy, every subcategory nested in each one.

Here are the categories:

- Tools: This holds all the effects nodes you draw on to assemble compositions, grouped under headings like 3D, Blur, Filter, Mask, Particles, and the rest.
- Open FX: Everything from Resolve FX plus any third party Open FX plugins you've installed lands here.
- Templates: While you're on the Fusion page in DaVinci Resolve, templates take the form of presets,

macros, and utilities built to get you up and running fast. Backgrounds, for one, gathers an assortment of tweakable generators assembled from a mix of Fusion tools. Lens flares serves up a broad range of multi-element lens flares you can drop into any composition. Particles offers a selection of ready-made particle systems you can adapt to your own needs. Shaders supplies an array of materials usable as texture maps for the 3D text and geometry you build in Fusion. And countless further categories hold useful presets and macros you can study and put to work in your own projects.

- LUTs: Here you'll find a collection of pre-installed Look Up Tables covering gamma, gamut, and colorspace conversions. Dropping a LUT into the Node Editor spawns a new FileLUT (FLUT) node with the chosen LUT file already loaded.

For more on stocking this list with your own LUTs, the place to look is Chapter 150, “Using LUTs.” Now, regarding how to add, insert, and replace tools by means of the Effects Library: when you pull nodes into the Node Editor out of the Tools category in the Effects Library, the process closely mirrors adding them from the toolbar. Ways to add nodes by clicking in the Effects Library:

- To place a node following a selected one: Pick a node in the Node Editor, then click a node within the Effects Library browser.
- To drop a disconnected node into the Node Editor: Clear all selections in the Node Editor, then click a node within the Effects Library browser.

Ways to add nodes by dragging out of the Effects Library:

- To slot a new node into the node tree: Drag a node out of the Effects Library browser into the Node Editor and over the connection line joining any two compatible nodes. Once that connection lights up beneath the node, release it and the node gets inserted.
- To make a disconnected node: Drag a node out of the Effects Library browser to a vacant spot in the Node Editor. Dragging a toolbar button into the Inspector likewise produces a disconnected node.
- To slot a new node after one loaded into a viewer: Drag a node out of the Effects Library browser onto a viewer, and a new node is inserted after whatever node is being viewed, whether or not any nodes happen to be selected.

To swap a node in the Node Editor for one from the Effects Library: 1 Drag a node out of the Effects Library browser until it hovers right on top of the Node Editor node you want replaced. As that node lights up, release it. 2 Click OK in the dialog to approve the swap.

Adding, Inserting, and Replacing Templates Using the Effects Library Bringing in items from DaVinci Resolve's Fusion page Templates category often plays out a little differently. At times, like when you add a Lens Flare, a lone node can be added or inserted into the Node Editor. In that situation, adding nodes behaves exactly as it does from the Tools category. Adding a Lens Flare effect. At other times, like when what you're adding comes out of the “How to” category, hauling one lone item from the Node Editor pulls a whole node tree into the Node Editor. Helpfully, every node of that incoming node tree is selected automatically when you do this, making it easy to drag the whole tree to a roomier spot in the Node Editor. When that occurs, the incoming effect's nodes are laid bare so you can rewire and reconfigure it however you need to fold the effect into the rest of your composition.

Pulling in a LightWrap effect out of the “How to” bin within the Effects Library's Templates category.

### Adding, Inserting, and Replacing Nodes Using the Contextual Menu

Yet another approach for adding, inserting, and replacing nodes leans on the Node Editor's contextual menu, whose dedicated submenus let you spin up any sort of node Fusion provides. It's handy when your pointer is already in the Node Editor busy selecting, moving, or wiring nodes. Ways to add nodes through the contextual menu:

- To add a node: Right-click a blank area of the Node Editor and pick a node from the Add Tool submenu.
- To insert a node: Right-click an existing node in the Node Editor and pick a node from the Insert Tool submenu.
- To replace a node: Right-click an existing node in the Node Editor and pick a node from the Replace Tool submenu.

TIP: Replacing one node with a different one carries over whatever settings the pair have in common into the replacement. Swapping a Transform node out for a Merge, say, brings the Transform's current center and angle values along to the Merge.

### Deleting Nodes

To remove one or several selected nodes, hit Delete (macOS) or Backspace (Windows), or right-click the selected node(s) and pick Delete from the contextual menu. The node leaves the Node Editor, and whatever was wired to its primary input and output gets joined to each other. Anything tied to its other inputs (mask inputs, for example) ends up disconnected.

A node tree shown just before one node is deleted (top), and afterward once the upstream and downstream nodes have rejoined on their own (bottom).

### Disconnected Nodes

There's nothing wrong with leaving disconnected nodes, or even whole disconnected branches of a node tree, sitting in the Node Editor next to the rest of a composition. Every disconnected node is just passed over yet kept around in case it proves useful down the road. That helps when you're holding onto nodes you tailored but later concluded you don't need. It also serves for keeping tree branches you've since exported as self-contained media that gets re-imported to stand in for the original effect, while you preserve the original nodes in case you ever have to redo the work.

### Selecting and Deselecting Nodes

Before you can do anything with nodes in the Node Editor, or tweak node parameters over in the Inspector, you first have to get the hang of selecting whichever node or nodes you mean to work on.

### Selecting Nodes

Selecting nodes ranks among the most basic moves for repositioning them or singling them out for various operations. Several techniques are at your disposal. Ways to select nodes: To grab a single node: Click any node in the Node Editor. To grab several nodes one by one: Command-click each node you'd like included. To grab an entire region of nodes: Drag a bounding box around every node you want. To grab all upstream or downstream nodes: Right-click a node and pick Select > Upstream Nodes/Downstream Nodes from the contextual menu. To grab every node in the Node Editor: Press Command-A. To grab a node by way of the Keyframe Editor: Click any layer there, and the matching node in the Node Editor is selected.

### The Active Node

Pick a single node through any of the techniques above and that node becomes the active node, glowing orange to signal its parameters are right then editable in the Inspector (assuming the Inspector is open). The orange also tells you that node is the one certain operations (like inserting new nodes) will act on. You can have many nodes selected, but only ever one active node. To keep them distinct, the active node stays orange while every other selected node turns white. Nodes that aren't selected wear plain black outlines.

Orange marks the active node, whereas the other selected nodes show white. To designate the active node while several nodes are selected:

- Option-click one of the selected nodes in the Node Editor, and that one becomes active.
- Open the Inspector if you must, then click a node's header bar to promote it to active.
