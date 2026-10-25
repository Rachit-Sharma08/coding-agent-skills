# Onscreen controls and viewer toolbars

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](playing-flipbook-previews-and-removing-flipbook-previews.md) / [Next section](viewer-subview-selection.md)
<a id="source-ab-buffers"></a> <a id="source-customizing-the-node-toolbar"></a> <a id="source-enablingdisabling-onscreen-controls-in-specific-nodes"></a> <a id="source-flipping-between-buffers"></a> <a id="source-making-fine-adjustments-to-onscreen-controls"></a> <a id="source-moving-the-wipe-divider"></a> <a id="source-node-toolbars"></a> <a id="source-showing-and-hiding-subviews"></a> <a id="source-split-wipes-between-buffers"></a> <a id="source-subviews"></a> <a id="source-the-buffer-menu-lets-you-switch-between-buffers"></a> <a id="source-the-contextual-menu-for-the-node-toolbar"></a> <a id="source-the-node-toolbar-shown-for-the-paint-node"></a> <a id="source-the-subview-menu-with-the-histogram-subview-displayed"></a> <a id="source-the-viewer-toolbar"></a> <a id="source-toolbars"></a> <a id="source-viewer-toolbar"></a>

### Enabling/Disabling Onscreen Controls in Specific Nodes

Certain nodes, masks among them, let you switch their onscreen controls off node by node, given that you often lean on several Polygon nodes to arrange and animate masks.

You can switch certain nodes, the Polygon node among them, off on a per-node basis.

### Making Fine Adjustments to Onscreen Controls

To pair the visual steer of onscreen controls with the precision of the Inspector, you can call on assorted keyboard modifiers.

- The Up and Down Arrow keys serve to nudge an onscreen control's vertical position in small steps.
- Holding the Command key down as you work the Up and Down Arrow keys shrinks each step's scale tenfold. Holding Shift grows each step's scale tenfold.

### Toolbars

The viewer carries two toolbars: a viewer toolbar, which sits at the top of every viewer and hands you control over what that viewer shows, plus an optional node toolbar appearing beneath it that hands you contextual controls keyed to whichever node you've selected in the Node Editor.

### Viewer Toolbar

A viewer toolbar stretches across the top of every viewer, opening up many of the most frequently used viewer-related settings while also signaling the state of many of the most important ones. The bulk of the menus and buttons on this toolbar get a full treatment across this chapter.

### The viewer toolbar

### Node Toolbars

Alongside the viewer toolbar, a node toolbar shows up beneath it, at the top of the viewer display area, any time you select a node that surfaces special nodes. Among the nodes that surface a toolbar are the text, masks, paths, paint strokes, and the 3D environment.

### The node toolbar shown for the Paint node

### Customizing the Node Toolbar

To resize the buttons sitting in the Node toolbar, or to switch on text names for each node, right-click any empty patch of the toolbar and pick fresh settings out of the Icon Size and Button Style submenus in the contextual menu.

### The contextual menu for the node toolbar

### A/B Buffers

Every viewer carries two buffers, each able to hold images from different nodes, which makes comparing two separate nodes within one viewer simple, whether by flipping between buffers or through an adjustable split-wipe. You can treat each buffer as a full, independent viewer living inside the same viewer pane. The A buffer always shows by default, so the first node you load into a viewer lands its image in the A buffer.

### Flipping between Buffers

Moving from one buffer to the other is simple, whether to view a different image while keeping another close at hand, or to flip between the original image and the affected one for comparison. To switch between buffers, do one of the following:

- Select a viewer, then press comma (,) for the A buffer or period (.) for the B buffer.
- Click the Buffer menu and pick either Switch to A View or Switch to B View.

### The Buffer menu lets you switch between buffers

TIP: Each buffer can carry its own display settings — say, showing different channels or different viewing LUTs, whether applied to different nodes or to two buffered versions of one node.

### Split Wipes between Buffers

You can also wipe across both buffers, which gives you a more direct way to compare. To wipe between buffers, take one of these routes: 1 Get ready to wipe across two images, either by placing separate nodes into each buffer or by placing one node — carrying differing viewer options — into each buffer. 2 To flip the split wipe on or off, pick either of these: a) Hit the Switch to Split Wipe View button. b) Tap Forward Slash (/). 3 To tune the wipe, pick from among these: a) Move the wipe's center by dragging the wipe divider's center handle. b) Hold Command-Option and click somewhere in the viewer, which snaps the wipe divider over to that spot. c) Change the wipe's angle by dragging the wipe divider. With the Shift key held while you drag the wipe divider, it snaps to the closest 45-degree angle. d) When you pan or zoom the viewer, both buffers pan and zoom together.

4 (Optional) To swap the image shown on that side of the split, you can drag fresh nodes onto either half of the viewer. 5 To switch the wipe off, click the Switch to Split Wipe View button once more (or press /).

The wipe divider is adjustable for comparing different stretches of the A and B images Even while wiping, you can pick different display channels, view LUTs, or other display options per buffer by clicking the half of the wipe you'd like to change, then choosing the options you want that buffer to use. That makes comparing different channels, LUTs, or other viewer settings simple as you wipe across one image, or across different images.

### Moving the Wipe Divider

Every so often you'll have zoomed in or panned so far off the viewer divider that it's slipped out of view in the viewer. Holding Command-Option down and clicking anywhere in the image makes the viewer divider jump to where the pointer currently sits.

### Subviews

A subview is a "mini" viewer turning up inside the main viewer. As a rule, a subview serves to show different information about the image.

### The Subview menu with the Histogram subview displayed

As an instance, you can view the RGB channels in the main viewer while the alpha channel shows in a subview. For the most part the subview is a fully working miniature viewer, carrying its own contextual menu and options. It answers to the same keyboard shortcuts and navigation controls any other viewer does. Even so, a handful of view types are meant for the subview alone, among them the Navigator, Magnifier, Color Inspector, and Image Info.

### Showing and Hiding Subviews

Subviews come up and go away easily. To switch on whichever subview is currently selected in a viewer's Subview menu, do one of the following:

- Click the Subview button in the View toolbar.
- Choose Views > Subview > Enabled from the contextual menu.
- Click a viewer, and press the V key.
