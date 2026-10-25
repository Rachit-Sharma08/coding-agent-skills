# Copying clip settings using display node graph paste attributes on the color page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copying clip settings using display node graph.
[Chapter index](INDEX.md) / [Previous section](copy-forward-commands-and-copying-using-memories.md) / [Next section](display-node-graph-and-multiclip-ripple.md)
<a id="source-copying-clip-settings-using-display-node-graph"></a> <a id="source-copying-from-the-node-graph-of-other-clips-or-gallery-stills"></a> <a id="source-grade-management-part-3"></a> <a id="source-paste-attributes-on-the-color-page"></a> <a id="source-the-paste-attributes-window-on-the-color-page"></a>

### Paste Attributes on the Color Page

You can lift one node's settings and paste only a portion of them onto another selected node through Edit > Paste Attributes (Option-V). Up comes a Paste Attributes window that names the node you're copying from and the node you're pasting to, and hands you controls for whether keyframes should paste and how they line up (Start Frames or Source Timecode), plus a row of checkboxes picking which palettes, windows, and OFX/ResolveFX you want

to apply. A given palette pastes only in full; there's currently no facility for pasting individual parameters from inside a palette, the lone exception being specific windows along with their attached trackers.

### The Paste Attributes window on the Color page

### Copying from the Node Graph of Other Clips or Gallery Stills

As you build new grades, it can pay to lift existing nodes or node settings from another clip's grade or a gallery still. That's straightforward: expose the node tree of any still saved in the Gallery, or of any clip in the Thumbnail timeline, then use the floating node graph's controls to copy individual nodes or node adjustments onto the current clip's grade displayed in the Node Editor.

### Copying Clip Settings Using Display Node Graph

While in Clip mode, the floating Node Graph window gives you four control sets for deciding how nodes and adjustments copy:

- Clip Node Graph: The Clip node graph sits on the left by default. Drag any node out of the floating node graph onto the current grade shown in the Node Editor, dropping it on an existing node to overwrite that node's settings or on a connection line to slot it in as a new node.
- Timeline Node Graph: (Available only where a Timeline grade exists) Jump to a Timeline grade, when one is present, either by clicking the second title-bar button on the Node Graph or by choosing Timeline from the drop-down at the floating Node Graph window's top-right corner.
- Apply Color/PTZR/Source/All buttons: With the Clip panel active, four buttons let you copy across just the full grade, just the sizing, just the source settings, or everything at once onto the current clip.

Dragging one node out of another clip's node graph onto the grade of the clip currently selected in the Node Editor Copying Node Settings Using Display Node Graph While in Node mode, the floating Node Graph window lays out every Color Attribute living inside each node in place of the Apply Color/PTZR/Source/All buttons:

- Node Settings: The checkboxes let you mark which node adjustments copy and which stay behind. With the settings you want ticked, dragging a node from the floating node graph onto Node Editor nodes copies or appends only the marked attributes into the target node and leaves the rest untouched. For Windows and OpenFX, you can additionally bring along any motion tracking on offer.

The Node panel showing, with the Color Corrector and Blur attributes ticked for copying

Ability to Open Compound Nodes in “Display Node Graph” After right-clicking a Gallery still or thumbnail and choosing Display Node Graph for a grade built on compound nodes, right-click any compound node and pick “Show compound node” — or Command-double-click that compound node — to crack it open and view the individual nodes inside.

Bringing up a compound node inside a floating Node Graph window Copying Nodes by Way of Display Node Graph The steps that follow walk through opening the floating node graph under various circumstances. To pull individual nodes or settings out of any Gallery still: 1 In the Timeline, click the thumbnail of the clip you intend to copy nodes into. The Node Editor then displays its node graph. 2 Over in the Gallery, right-click a still you want to take nodes from and pick Display Node Graph. Up pops a floating Node Graph window holding that still's node tree. 3 (Optional) With the Gallery Node Graph window open, you may click any other still and the window refreshes to present whichever still is now selected, set for you to copy from. 4 Within the floating Node Graph window, pick Clip to copy a clip's attributes as a whole, or pick Node to copy attributes of one node. 5 Carry out one of the following to bring nodes or settings into the Node Editor.

- Under Clip mode, grab any node out of the floating node graph and drag it onto the Node Editor's current grade, dropping it over an existing node to replace that node's settings. Should you open the Node panel and pick out particular attributes, only those carry over to the node you drop onto.
- Under Clip mode, grab any node out of the floating node graph and drag it onto the Node Editor's current grade, dropping it on a connection line so it slots in as a new node. Should you open the Node panel and pick out particular attributes, only those carry over to the freshly made node.
- Under Clip mode, hit Apply Color to bring the whole grade across from the floating node graph and replace the Node Editor's current grade.
- Under Clip mode, hit Apply PTZR to bring the sizing across from the floating node graph and replace that of the current clip.
- Under Clip mode, hit Apply Source to bring the source settings across from the floating node graph and replace those of the current clip.
- Under Clip mode, hit Apply All to bring every setting across from the floating node graph onto the current clip.
- Under Node mode, mark which attributes to copy, then grab any node from the

floating node graph and drag it onto the Node Editor's current grade, dropping it over an existing node to replace, on that node, only the settings you marked.

- Under Node mode, mark which attributes to copy, then grab any node from the floating node graph and drag it onto the Node Editor's current grade, dropping it on a connection line so it slots in as a new node carrying only the settings you marked.

6 With the floating Node Graph window still open, you may likewise click any clip in the Thumbnail timeline to swap which grade the Node Editor shows, ready for copying onto. 7 Hit Close once you are done. To pull individual nodes or settings out of any Timeline clip: 1 In the Timeline, click the thumbnail of the clip you intend to copy nodes into. The Node Editor then shows its node graph. 2 Right-click the thumbnail of a different clip you wish to take nodes from and pick Display Node Graph. NOTE: The Display Node Graph command shows up in the contextual menu only for a Thumbnail timeline clip that is not the one currently selected. 3 (Optional) Inside the floating Node Graph window, pick Clip to copy a clip's attributes as a whole, or pick Node to copy attributes of one node. 4 Carry out one of the following to bring nodes or settings into the Node Editor.

- While in Clip mode, drag a node from the floating node graph over to the grade currently in the Node Editor and let it fall on an existing node, which overwrites that node's settings. Open the Node panel and select specific attributes, and just those attributes transfer to the node you dropped onto.
- While in Clip mode, drag a node from the floating node graph over to the grade currently in the Node Editor and let it fall on a connection line, where it is inserted as a brand-new node. Open the Node panel and select specific attributes, and just those attributes transfer to the new node that results.
- While in Clip mode, press Apply Color to carry the full grade from the floating node graph over, replacing the grade currently in the Node Editor.
- While in Clip mode, press Apply PTZR to carry the sizing from the floating node graph over, replacing that of the current clip.
- While in Clip mode, press Apply Source to carry the source settings from the floating node graph over, replacing those of the current clip.
- While in Clip mode, press Apply All to carry every setting from the floating node graph over onto the current clip.
- While in Node mode, choose the attributes to copy, then drag a node from the floating node graph over to the grade currently in the Node Editor and let it fall on an existing node, overwriting on that node just the settings you chose.
- While in Node mode, choose the attributes to copy, then drag a node from the floating node graph over to the grade currently in the Node Editor and let it fall on a connection line, inserting it as a new node holding only the settings you chose.

5 (Optional) With the floating Node Graph window still open, you may likewise click any clip in the Thumbnail timeline to swap which grade the Node Editor shows, ready for copying onto. 6 Hit Close once you are done.
