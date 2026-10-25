# Cut copy and paste in the node editor instanced nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cut copy and paste in the node editor.
[Chapter index](INDEX.md) / [Previous section](cut-copy-and-paste-in-the-node-editor-pasting-node-settings.md) / [Next section](cut-copy-and-paste-in-the-node-editor-underlay-boxes.md) / [Cut, Copy, and Paste in the Node Editor](node-view-indicators-and-clipboard.md)
<a id="source-changing-node-colors"></a> <a id="source-commands-to-clean-up-a-node-tree"></a> <a id="source-de-instancing-and-re-instancing-specific-parameters"></a> <a id="source-keeping-node-trees-organized"></a> <a id="source-moving-nodes"></a> <a id="source-renaming-nodes"></a> <a id="source-snapping-nodes-to-the-grid"></a> <a id="source-using-instanced-nodes"></a> <a id="source-using-sticky-notes"></a>

### Using Instanced Nodes

Instanced nodes are those created with the Paste Instance command, and they share their settings with the source node, so any change made to one instanced node automatically carries across to every other instance of that node (and to the original node you copied as well). Building an Instance goes as follows: 1 Pick a node you wish to instance and copy it (Command-C). 2 Carry out one of these: To make a stand-alone instance of a node: Right-click in the Node Editor background and choose Paste Instance from the contextual menu (Command-Shift-V). To drop an instanced node in between two existing nodes: Pick a node that lies upstream of the intended spot, then press Command-Shift-V. Or instead, rightclick squarely atop a connection line, where the contextual menu again offers Paste Instance. Whichever route you take to paste the instance, that instanced node’s name comes out in the form "Instance_NameOfNode." Paste several instances and each one is numbered "Instance_NameOfNode_01."

A green link line depicts how an instanced Blur node relates to the original Blur node it sprang from. Anytime a node tree contains instanced nodes, a green line denotes the tie binding the original node to its instances. If you prefer, you can switch those green link lines off so the Node Editor looks less cluttered. Showing or hiding the green instance link lines within the Node Editor works thus: 1 Right-click any point of the Node Editor background. 2 From the contextual menu, pick Options > Show Instance Links. After working with a node’s instance and then finding that it needs to take on its own separate adjustments, you can “de-instance” the node.

To de-instance a node, cutting it loose to stand alone: 1 Right-click an instanced node. 2 From the contextual menu, pick Deinstance. From then on that node is divorced from the original node. Once a node has been de-instanced you have no way to re-instance it, although the action remains undoable. NOTE: Where you have de-instanced a node and cannot undo because DaVinci Resolve has since restarted, the only path to a fresh instance is to copy the original and paste an instance once more.

### De-Instancing and Re-Instancing Specific Parameters

Out of the box, each parameter on an instanced node ties back to the original node, so every change you make propagates across. Now and then, though, you will need to adjust just one or two parameters on their own while leaving the rest of that node’s parameters linked. With that in mind, in place of de-instancing the entire tool, you can break the link on individual parameters. To de-instance a single parameter:

- In the Inspector, right-click a parameter’s name or value and choose Deinstance from the contextual menu. If only individual parameters were de-instanced, you can re-link those parameters later on should you have second thoughts.

To re-instance a single parameter: In the Inspector, right-click that parameter’s name or value and choose Reinstance from the contextual menu. The parameter at once takes on the original node’s setting.

### Keeping Node Trees Organized

Much as with the files on your desktop, even the most basic of composites calls for a degree of organization. Here we will run through a handful of fundamental node operations, several of which you may well recognize already from your computer’s operating system or from other software.

### Moving Nodes

Picking one or more nodes and dragging relocates them, which ranks among the simplest ways to tidy a node tree — grouping nodes by position according to the part they play in the whole composition. Bear in mind that where nodes sit in the Node Editor is purely cosmetic and has no bearing on a composition’s output. Arranging the node tree exists solely for your own peace of mind, and that of anyone collaborating with you. TIP: After you have laid out a composition’s nodes in some sensible fashion, the Sticky Note and Underlay tools let you add notes about what is going on and tie clusters of nodes together more firmly by sight. These tools come up later in this section.

### Snapping Nodes to the Grid

By default you are free to drop nodes wherever you please. That said, keeping nodes and connection lines tidy and aligned can make them simpler to read. To aid alignment, the nodes you are dragging can be set to snap onto the grid by themselves. To make dragged nodes snap onto the grid:

- Right-click on a bare patch within the Node Editor; from the contextual menu, pick Arrange Tools > To Grid. From then on every node you drag snaps to its closest grid coordinate.
- Right-click on a bare patch within the Node Editor; from the contextual menu, pick Arrange Tools > To Connected. From then on every node you drag snaps to the horizontal or vertical line of whatever nodes it ties to.

TIP: You can make “Arrange to Grid” or “Arrange to Connected” the standing default for new compositions: pick Fusion > Fusion Settings in DaVinci Resolve or File > Preferences in Fusion Studio, then tick the Fusion > Node Editor > Arrange To Grid or Arrange to Connected checkboxes.

### Commands to “Clean Up” a Node Tree

The grid sitting behind the Node Editor serves to align nodes, whether by eye or automatically.

- To “clean up” a disorderly node tree: Right-click a bare section of the Node Editor; from the contextual menu, pick Line Up All Tools to Grid. Every node in the Node Editor then shifts to align and center itself along the closest grid lines.
- To “clean up” just one or more selected nodes: Right-click any of the selected nodes; from the contextual menu, pick Line Up to Grid. The selected nodes shift to align and center themselves along the closest grid lines, while every unselected node stays put.

### Renaming Nodes

Each node created gets a name assigned to it automatically (drawn from its function) plus a number (drawn from how many nodes of that type already exist). To illustrate, the first Blur node placed in a composition is called Blur1, the next is Blur2, and onward from there. Helpful as that is at the outset, bigger compositions can gain from giving key nodes more telling names — easing the job of recognizing what they actually do, or of referencing those nodes within expressions. To rename a node: 1 Do one of the following:

- Right-click a node and choose Rename from the contextual menu.
- Select a node and press F2.

2 Once the Rename dialog opens, key in a fresh name, after which you click OK or hit Return.

NOTE: With several nodes selected at once, a separate dialog pops up for each, prompting a name per tool.

Because Fusion lends itself to scripting and expressions, node names have to obey a scriptable syntax. Stick to alphanumeric characters only (no special characters), and avoid spaces entirely. On top of that, a node name cannot open with a number. Should you slip and form a name that strays from these rules, spaces and invalid characters get stripped out automatically. When you would rather view the original node types in place of the node names, press and hold Command-Shift-E.

### Changing Node Colors

Any node’s color can be changed by selecting it, opening the Inspector, and picking a fresh color from the Node Color pop-up in that node’s Inspector header. As an alternative, right-click a node and select a color out of the Set Color submenu. To restore a node to its usual color, right-click it and, from the contextual menu, pick Set Color > Clear Color, or open that node’s Node Color pop-up in the Inspector and pick Clear Color.

### Using Sticky Notes

One fine way to keep track of notes on the various parts of a composition, client feedback on assorted details, and any other information you want on hand, is to drop Sticky Notes into the Node Editor.

A Sticky Note in the Node Editor. Sticky Notes are yellow boxes into which you can type any text you like. They can be resized, moved, and collapsed while not being edited, but once made they stay pinned to the Node Editor background at the spot where you placed them until you move or delete them. Methods of working with Sticky Notes:

- To create a Sticky Note: Click the Node Editor spot where you would like a Sticky Note to land. Then press Shift-Spacebar, type sticky, and once the Sticky Note turns up in the Select Tool window, hit the Return key. Failing that, open the Effects Library, head into the Tools > Node Editor category, and either click or drag the Sticky Notes node to spawn a fresh one.
- To open a Sticky Note to full size: Give a minimized Sticky Note a double-click and it grows into a larger, resizable yellow box.
- To edit a Sticky Note: Where needed, double-click a Sticky Note to bring it up full size, then click once within the note’s body to drop a text cursor. Text inside a Sticky Note is edited the same way as in any text editor.
- To rename a Sticky Note: Right-click a Sticky Note, pick Rename, key a fresh name into the Rename dialog, and click OK. Failing that, select a Sticky Note, hit F2 to summon the Rename dialog, and press Return to close it once done.
- To resize a Sticky Note: Bring a Sticky Note up to full size with a double-click, after which you drag any edge or corner to grow or shrink it.
- To minimize a Sticky Note: Click the close box up in the Sticky Note’s top left corner, and it folds down into a small tile.
- To delete a Sticky Note: Either right-click a Sticky Note and pick Delete from the contextual menu, or select the Sticky note within the Node Editor and tap the Delete key.
