# Node view indicators drag and drop nodes into a viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node view indicators.
[Chapter index](INDEX.md) / [Previous section](node-view-indicators-deselecting-nodes.md) / [Next section](node-view-indicators-node-order-matters.md) / [Node View Indicators](node-view-indicators-deselecting-nodes.md)
<a id="source-attaching-connections-to-specific-inputs"></a> <a id="source-automatically-and-manually-attaching-mask-nodes"></a> <a id="source-clearing-viewers"></a> <a id="source-connecting-and-disconnecting-nodes"></a> <a id="source-createplay-preview"></a> <a id="source-drag-and-drop-nodes-into-a-viewer"></a> <a id="source-dropping-connections-on-top-of-nodes"></a> <a id="source-how-to-connect-nodes"></a> <a id="source-identifying-node-inputs"></a> <a id="source-node-basics"></a> <a id="source-using-the-contextual-menu"></a>

### Drag and Drop Nodes into a Viewer

Should the View indicators be too tiny a target to click dependably, and you're not the keyboard type, there's another route for loading a node into a viewer: drag it and drop it straight onto the viewer you mean to fill. This gives a fast, deliberate way to hand a node off to a viewer, handy above all for pen and tablet users. Bear in mind that during the drag the node looks like it's moving at first, yet it snaps right back to where it started the instant the pointer exits the Node Editor.

### Using the Contextual Menu

Another option is to right-click a node and then pick View On > Left or Right to throw the node onto the right viewer.

### Clearing Viewers

Each time you load a node into a viewer, you trigger a render of that node, every node upstream of it, and other related nodes too. Load nodes into both viewers and that workload doubles. To stop your computer from grinding through views you don't currently need, you can empty each viewer. Ways to clear viewers:

- Press 1 or 2 to clear the left or right viewers when they're loaded.
- Press ` (the Accent key) to clear both viewers.

### Create/Play Preview

You can right-click a node and pick an entry from the contextual menu's Create/Preview Play On submenu to render and play back a preview of any node's output on one of the viewers on hand. Up comes the Render Settings dialog, and once you accept the settings, the tool renders and the frames it produces get held in RAM for snappy playback on that view. TIP: Hold the Shift key as you choose the viewer from the menu to skip the Render dialog and kick off the preview straight away using the default settings or whatever settings you last used to build a preview.

### Connecting and Disconnecting Nodes

After you've begun dropping nodes into your composition, they have to be connected before they can carry out what you intend.

### Node Basics

Every node shows little colored knots ringing its edges. The arrows, one or more, mark inputs, while the square marks the tool's processed output, of which there's never more than one. An output reads white when it's wired up correctly, gray when it's left unconnected, or red to flag that something's off and the node can't process as it should.

A Blur node with a Foreground Input, Mask Input, and Output. Every node feeds on the output handed to it by the node ahead of it. Wire a MediaIn node's output into a Blur node and you push image data from the MediaIn node across to the Blur node, which works on the image before the Blur node's own output gets relayed onward to the next node in the tree.

Two nodes connected together.

### How to Connect Nodes

To hook one node to another by hand, click a node's output and pull a connection line across, dropping it onto another node's input. Which way you drag the node connections doesn't matter; pulling a connection from one node's input to another node's output works exactly as well and lands the same result.

The view before (top) and after (bottom) a connection line is pulled and dropped to join two nodes.

### Dropping Connections on Top of Nodes

To save yourself a little effort, you can instead pull a connection line and let it fall right onto a node's tile to auto-wire it to that node's default input, which usually carries the label "background" or "input." In the example below, a connection is pulled from a MediaIn node's output and dropped onto a Blur1 node's tile, and the background input gets connected first.

The view before (top) and after (bottom) a connection line lands atop a node. Drop a connection onto a node whose background input is already wired, and the next-most-important connection gets attached instead, which on multi-input nodes is the foreground input, while on other single-use nodes it may be the Effects Mask input.

The view before (previous page) and after (above) a connection line is dropped onto a node whose background input is already wired up. A few multi-input nodes can grow extra inputs to take on many connections, the Merge3D node among them. Such nodes simply spawn another input each time you drop a connection onto them.

The result once a connection line has been dropped atop a Merge3D node.

### Attaching Connections to Specific Inputs

When you want to be sure you don't land a connection on a node's default input, you have to drop it squarely onto the particular node input you're after. Spot the input's label in the tooltip bar and you know you're lined up to make a clean connection. There's a fallback method, though, for when several inputs compete and you need to be certain you're picking the right one. Hold the Option key while you pull a connection out of one node's output and drop it onto the body of another node. That brings up a pop-up menu where you can name the exact input you want to wire to. Keep in mind this menu shows up only once you've dropped the connection on the node and let go of your pointing device's button.

Pulling a node connection with Option held and dropping it onto another node surfaces a node input menu.

### Automatically and Manually Attaching Mask Nodes

Mask nodes—the Polygon, B-Spline, Ellipse, or Rectangle, say—behave differently on their own when you wire them to other nodes. Pull a connection from a Mask node onto the body of another node and it auto-wires itself to the default mask input, typically the effect mask input. The presumption is that you're using the mask to rein in the node's effect somehow. That's not always so, though, so stay mindful of this behavior to be sure your mask lands on the input that truly delivers the effect you're chasing.

The view before (top) and after (bottom) a connection from a Mask node is pulled and dropped atop a MatteControl node.

### Identifying Node Inputs

While you're still getting the hang of all the nodes and their inputs, resting the pointer over any knot brings up a node tip carrying the knot's name. TIP: Instead of memorizing the various knot types, hold the right mouse button, press Option, and drag from a node's output to the center of another tool. Let go of the mouse and a tooltip surfaces, letting you pick the knot you want to connect to.
