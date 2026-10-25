# Underlay flow organizational nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Underlay.
[Chapter index](INDEX.md) / [Previous section](sticky-note-and-underlay.md) / [Next section](underlay-and-fuses.md) / [Underlay UND](sticky-note-and-underlay.md)
<a id="source-a-pipe-router-usage-example"></a> <a id="source-an-opened-node-group"></a> <a id="source-flow-organizational-nodes"></a> <a id="source-flow-organizational-nodes-1"></a> <a id="source-groups"></a> <a id="source-groups-introduction"></a> <a id="source-macro"></a> <a id="source-macro-editor"></a> <a id="source-macro-introduction"></a> <a id="source-pipe-router"></a> <a id="source-router"></a> <a id="source-router-introduction"></a> <a id="source-select-the-nodes-to-include-in-the-macro"></a> <a id="source-selecting-nodes-to-group"></a> <a id="source-the-final-macro"></a> <a id="source-the-group-node"></a> <a id="source-the-macro-editor"></a> <a id="source-the-macro-editor-save-dialog"></a> <a id="source-usage-2"></a> <a id="source-usage-3"></a> <a id="source-usage-4"></a>

## Flow Organizational Nodes

### Flow Organizational Nodes

This chapter covers the Groups, Macro, and Pipe Router nodes, all built to help you keep compositions tidy and to render the node tree clearer to view and grasp.

Throughout this document, node trees that display MediaIn nodes in DaVinci Resolve may be read as equivalent to Loader nodes in Fusion Studio, except where a note states otherwise.

### Groups

### The Group node

### Groups Introduction

Groups serve to keep tangled node trees in order. Pick out however many nodes you want from the node tree, then group them so they collapse into one node icon in the Node Editor. Because Groups are nondestructive, you can reopen them whenever you like.

### Usage

- To group nodes, pick them out in the Node Editor, then right-click on any node in the selection and pick Group from the contextual menu.

### Selecting nodes to group

- To work on the separate nodes inside a group, right-click and pick Expand Group from the contextual menu. Every node held in the group then shows up in a floating node tree window. Opened groups float above whatever's already there, letting you edit the nodes they enclose.

### An opened node group

- To dissolve a group while holding onto its separate nodes, right-click the group and pick Ungroup.

### Macro

Strictly speaking, a Macro isn't a node. Rather, it's a cluster of nodes that behaves as though it were one node.

### Macro Introduction

With Macros you can merge several nodes together and surface a set of controls you get to define yourself. The idea behind them is to make crafting custom nodes quick and painless.

### Usage

To build a Macro, pick the nodes you want it to contain. Whatever sequence you select them in sets the sequence they'll show up in within the Macro Editor. Right-click any node in the selection and pick Macro > Create Macro from the contextual menu.

### Select the nodes to include in the macro

### Macro Editor

The Macro Editor is where you pick out and rename the controls that the finished macro tool surfaces. In the sample shown below, the tool carries the name Light_Wrap at the top. The Blur slider belonging to Matte Control 1 is switched on and given the new name Softness, which is how it'll read in the Inspector.

### The Macro Editor

Once the macro is arranged the way you want, click the Close button down in the dialog's lower-right corner. After that, the Save dialog offers Yes to store the macro, No to exit Macro Editor while discarding your edits, or Cancel to head back into the Macro Editor.

### The Macro Editor save dialog

Dropping the macro into your node tree is a matter of right-clicking anywhere on the node tree and picking Macro > [NameOfYourMacro] via the contextual menu. (How to store a macro as an Edit Page title template in DaVinci Resolve.) Within DaVinci Resolve, the only place macros surface is the Fusion page. That said, should the macro happen to be a title animation, you're able to stash it in the Titles Templates folder so it turns up over in the Edit page Effects Library. For a title macro to appear there in the Edit page Effects Library, drop the macro into this location — on macOS: `Users > UserName > Library > Application Support > Blackmagic Design > DaVinci Resolve > Fusion > Templates > Edit > Titles` and on Windows: `C Drive > Users > UserName > AppData > Roaming > Blackmagic Design > DaVinci Resolve > Support > Fusion > Templates > Edit > Titles`

### The Final Macro

Your finished macro appears and operates exactly like any other Fusion node. For a second example, you might grab one Channel Boolean, switch it to Add mode, and turn it into a macro that surfaces no controls whatsoever, which gives you something equivalent to an Add Mix node of the sort found in applications such as Nuke.

### Pipe Router

Pipe Routers are yet another organizing aid that helps you clean up how the node tree is laid out and how it looks.

### Router Introduction

Routers let you tidy up your comps by adding “elbows” to the node tree, which keeps connection lines from crossing over nodes and makes everything clearer to follow. They have no bearing whatsoever on render times.

### Usage

### A Pipe Router usage example

### Router

Adding a router onto a connection line takes an Option- or Alt-click directly on that line. From there you can drag the router around to lay out the connections however suits you. Routers carry no real controls of their own, yet they still come in handy for attaching comments to a comp.
