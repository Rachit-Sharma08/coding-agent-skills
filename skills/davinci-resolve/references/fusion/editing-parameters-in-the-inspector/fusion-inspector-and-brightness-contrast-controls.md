# Overview of the inspector and inspector displays the brightness contrast controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing parameters in the inspector.
[Chapter index](INDEX.md) / [Next section](inspector-node-selection-and-versioning.md)
<a id="source-a-nodes-inspector-header"></a> <a id="source-control-preferences-in-the-user-interface-category"></a> <a id="source-customizing-the-inspector"></a> <a id="source-editing-parameters-in-the-inspector"></a> <a id="source-editing-parameters-in-the-inspector-part-1"></a> <a id="source-hiding-inspector-controls"></a> <a id="source-inspector-display-preferences"></a> <a id="source-inspector-displays-the-brightness-contrast-controls"></a> <a id="source-inspector-height"></a> <a id="source-modifiers-displayed-in-the-modifiers-panel"></a> <a id="source-opening-multiple-nodes-in-the-inspector"></a> <a id="source-opening-nodes-in-the-inspector"></a> <a id="source-overview-of-the-inspector"></a> <a id="source-pinning-multiple-nodes-in-the-inspector"></a> <a id="source-the-tools-and-modifiers-panels"></a> <a id="source-using-the-inspector-header"></a>

### Editing Parameters in the Inspector

Each node's parameters are tuned inside the Inspector to accomplish whatever a given task requires. The various parameters carried by nodes, and the ways you work with the controls on offer, are the subject of this chapter.

### Overview of the Inspector

Building and wiring nodes within the Node Editor sets which tools, and in what order, form a composition; tuning the settings held inside each individual node, however, happens over in the Inspector so the result matches your intent.

### Inspector displays the Brightness Contrast controls

How you open a node's parameters in the Inspector, and edit them through whichever controls a node exposes, is covered here. To display the Inspector: Click the Inspector button on the UI toolbar.

### The Tools and Modifiers Panels

Two main panels make up the Inspector.

- The Tools panel is the spot where a selected node's parameters surface for editing.
- The Modifiers panel is where you adjust optional add-ons that extend a tool past its built-in feature set, plus

scripted expressions you can bind to single parameters in order to drive animated results. Beyond that, some nodes (the Paint node, for instance) produce data like Strokes, and that data lives in the Modifiers panel.

### Modifiers displayed in the Modifiers panel

### Customizing the Inspector

Several options let you change the way the Inspector is laid out.

### Inspector Height

Off at the far-right end of the UI toolbar sits a small arrow button that switches the Inspector between its full-height and half-height layouts, according to how much vertical space your parameter editing demands.

The Maximize button at the Inspector's left edge In maximized height mode, the Inspector claims the whole right edge of the UI, so every control a node offers is visible, or so there's room enough to expose the parameters of two or three pinned nodes simultaneously. With half-height mode active, the Inspector's top edge lines up with the tops of the viewers, which widens the horizontal area left over for the Node Editor.

### Inspector Display Preferences

Out of the box, the Inspector shows only the nodes you've selected, and only the Active node has its controls expanded. To alter that behavior, head to Fusion > Fusion Settings while in the Fusion page (or File > Preferences over in Fusion Studio) and bring up the User Interface panel. Within the User Interface, a set of checkboxes governs how controls are shown.

### Control preferences in the User Interface category

- Auto Control Open: When enabled (the default), the active node, whichever one that is, opens its controls in the Inspector on its own. When disabled, choosing an active node reveals that node's Inspector header in the Inspector, yet the parameters stay tucked away until you click the Inspector header.
- Auto Control Hide: When enabled (the default), the Inspector shows only selected nodes, and any node you deselect is dropped from the Inspector automatically so things stay tidy. When disabled, the parameters of selected nodes stick around in the Inspector even after you deselect those nodes, which lets the Inspector pile up the parameters of every node selected over the course of your work.
- Auto Control Close Tools: When enabled (the default), only the active node's parameters are allowed to be open. When disabled, you're free to expose the parameters of several nodes in the Inspector at once.
- Auto Controls for Selected: When enabled (the default), choosing more than one node opens a control header per node in the Inspector. When disabled, the Inspector shows only the active node; the other multi-selected nodes, marked in white, stay hidden.

### Opening Nodes in the Inspector

A node has to be opened in the Inspector before you're able to edit its parameters. To display a node's controls in the Inspector: From the Node Editor, the Keyframes Editor, or the Spline Editor, pick one node or several. Selecting one node on its own, such that the Node Editor highlights it orange, brings every one of its parameters into the Inspector. Select several nodes together and an Inspector header shows up for each one (marked white in the Node Editor), while the parameters belonging to the active node (marked orange) are the ones available to edit.

### Opening multiple nodes in the Inspector

Because only a single node's parameters can be edited at once, clicking a different node's Inspector header reveals that node's parameters and shuts the parameters of whichever node you had open before. Doing so also turns the freshly opened node into the active one, marking it orange in the Inspector.

### Pinning Multiple Nodes in the Inspector

When speed matters and you want to tune the parameters of several nodes together, the Pin button in a node's Inspector header keeps those parameters on display in the Inspector no matter whether that node happens to be selected and active right then. The Pin button on a node's Inspector header As long as the Pin button stays on, that node's parameters stay open in the Inspector. Selecting a different node back in the Node Editor causes that node's parameters to show up below any pinned ones.

A pinned node shown beneath a selected node up top There's no cap on how many nodes you pin in the Inspector, though a larger number raises the odds that you'll be scrolling up or down within the Inspector to reach every parameter you mean to edit. Switching off a node's Pin button in its Inspector header is all it takes to unpin it from the Inspector.

### Hiding Inspector Controls

Should you wish, the Inspector parameters of particular nodes can be concealed so they stay out of sight even while that node is selected. That's handy for guarding against unintended edits by you or by fellow compositors on a shared composition whenever locking the node outright isn't what you want. To Toggle the Inspector controls for a node or or off: Either the node itself in the Node Editor, or its Inspector header, can be right-clicked; then pick Modes > Show Controls off the contextual menu.

### Using the Inspector Header

Selecting a node fills the Inspector with a title bar, known as the Inspector header, showing both that node's name and the rest of the controls that manage it. Although a node's Inspector header carries an assortment of controls in its own right, clicking (or double-clicking) it also reveals that node's parameters.

### A node's Inspector header

Select several nodes together and the Inspector shows a header for each. By default only the active node's parameters (marked orange in the Node Editor) may be opened at any one moment, though Fusion's Preferences let you alter that behavior.
