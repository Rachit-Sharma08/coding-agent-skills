# Node view indicators node order matters

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node view indicators.
[Chapter index](INDEX.md) / [Previous section](node-view-indicators-drag-and-drop-nodes-into-a-viewer.md) / [Next section](node-view-indicators-and-clipboard.md) / [Node View Indicators](node-view-indicators-deselecting-nodes.md)
<a id="source-automatically-creating-a-merge-node-when-adding-nodes"></a> <a id="source-branching"></a> <a id="source-connecting-merge-nodes"></a> <a id="source-disconnecting-and-reconnecting-nodes"></a> <a id="source-node-order-matters"></a> <a id="source-tracing-connections-through-the-node-tree"></a> <a id="source-upstream-and-downstream-nodes"></a>

### Node Order Matters

The sequence in which nodes get wired together sets the sequence in which each image-processing operation hits the image. In the example below, a MediaIn node brings a clip into the composition, a Defocus node softens the image, and then a TV node lays in scanlines and vertical distortion. Those effect nodes then feed into the MediaOut node on the Fusion page in DaVinci Resolve, or into a Saver node in Fusion Studio.

Adding a Defocus effect first, then the TV node second. As the figure shows, wiring the Defocus node first and the TV node after means the base image is softened while the TV effect stays sharp. Flip the order of these two nodes, though, and the TV effect warps the image, after which the Defocus node now blurs the whole result, leaving the TV effect every bit as soft as the image it lands on. The deliberate order of operations you set up makes an enormous difference.

Adding a TV effect first, and a Defocus second. As you can tell, the node tree behind each composition is a schematic of operations carrying enormous flexibility. On top of that, the node tree's structure aids compositing by letting you steer each node's output into its own branch, which can be processed on its own and later rejoined in countless ways, building ever more intricate composites while sparing you the need to precompose, nest, or otherwise lump layers together—any of which would muddy your composition's readability. In the example below, several graphics layers are transformed one by one and joined with a string of Merge nodes. The final Merge node's result is then transformed, letting you shift the whole stack of earlier layers at once. Because the node tree spells out each of these operations plainly, it's simple to see all that's going on, and why.

A single Transform node reworks the merged output of five Text nodes that Merge nodes have joined.

### Upstream and Downstream Nodes

Because nodes can sit anywhere in the Node Editor and get added in any direction, they're spoken of as being upstream and downstream of each other. Once you select a node, every other node that ties into its input, directly or by way of others, counts as upstream. Any nodes hooked to its output, directly or indirectly, are said to be downstream. This distinction carries weight because, unlike layer-based systems, where you visually place nodes in your node tree has no effect on that composition's order of operations. What counts is solely whether nodes sit upstream or downstream of one another.

Tools upstream (left) and downstream (right) of the Merge node. TIP: To keep yourself organized, the Node Editor contextual menu offers Select > Upstream/Downstream commands for grabbing every upstream or downstream node so you can move them, group them, or handle other organizational chores.

### Disconnecting and Reconnecting Nodes

Node trees stay perpetually in flux, calling for steady revision and reshuffling as you turn up fresh details that want finessing, or things you can pull off better once the whole composition has come together. To make quick edits easy, each connection between two nodes is split into two halves: the output half (tied to the upstream node's output) and the input half (tied to the downstream node's input). You only catch sight of this while you hover the pointer over a connection. Whichever half your pointer sits over lights up in blue.

A connection line's two halves, brought into view as your pointer hovers above it. Through clicking and/or dragging those two halves, you can swiftly disconnect, reconnect, and overwrite node connections, which is vital to reshuffling your node tree quickly and efficiently. To disconnect two nodes, take one of these actions:

- Click once on the input half of the connection running between two nodes.
- Click the input arrow that a connection lands on, then drag to peel the connection off the tool and drop it anywhere on an empty stretch of the Node Editor.

To overwrite an existing connection:

- Drag the output or input half of a connection and drop it squarely onto another node's input or output. That both severs the old connection and wires up the one you're dragging in one motion.

To reroute a connection from one node to another:

- Drag the output or input half of a connection to peel it off one node, and let the connection fall right on another node's input or output.

### Tracing Connections Through the Node Tree

Resting the pointer over a node lights up the connections tied to that node, making it plainer which nodes it links to. What's more, lit-up connections take on the color of the input they feed, so it's easy to tell whether they run to a foreground, a background, or some particular kind of mask.

Resting the pointer on a node lights up every connection in its color, revealing which kinds of inputs are wired in.

On top of that, parking the pointer over a connection summons a tooltip spelling out the output and input that connection joins.

Resting the pointer on a node lights up the connection running between it and the other nodes.

### Branching

A node's input can hold just one connection. A tool's output, on the other hand, can run to inputs on as many nodes as you like. Splitting a node's output across inputs on several nodes is what's called branching. Countless reasons exist for wanting to branch a node's output. One easy example is processing an image in a handful of different ways before bringing those results back together further down the node tree.

A MediaIn node split across two node operations and afterward rejoined by way of a Merge node. As another use, it lets you put one image to several different purposes—say, sending the RGB down one branch for keying and compositing while routing the A channel into another node's Effects Mask input to rein in its effect, or feeding RGB to a tracker to pull out motion data.

A MediaIn node branched to two different kinds of inputs, used separately.

### Connecting Merge Nodes

The Merge node is the chief tool on hand for compositing images together. Each Merge node can fold two inputs into a third, drawing on standard compositing methods and composite modes. For a fuller account of the Merge node, consult Chapter 105, "I/O Nodes," within the DaVinci Resolve Reference Manual, or else Chapter 45 over in the Fusion Reference Manual. Here, the only thing to grasp is that if you attach a background image to the Background input (a landscape, say) and a foreground image with an alpha channel to the Foreground input (a graphic with an alpha channel, say), the Merge node folds them into a single image ready for further compositing.

A pair of MediaIn nodes plus a DeltaKeyer node wired into a Merge node, building a composite. Every Merge node carries three inputs:

- Background (orange): The default input. Whatever image lands on this input sets the Merge node's output resolution.
- Foreground (green): The secondary input, intended for whatever image you want sitting "on top."
- Effect Mask (blue): An optional input where you can attach a mask or matte to rein in the Merge node's effect.

Getting the right nodes onto the right inputs matters if you want the result you're after, so keep these inputs front of mind whenever you wire to a Merge node. You can of course always drag a connection to a specific input to be sure you're wiring things the way you need. But if you're rushed and just drop connections straight onto a Merge node:

- The first connection lands on the background input.
- The second connection lands on the foreground input.
- The third connection lands on the effect mask input.

TIP: Whether you append a Merge node to a selected node via the toolbar's Merge button, via the Effects Library's Merge icon, or by right-clicking a node within the node tree and picking Insert Tool > Composite > Merge off the contextual menu, that fresh Merge node always shows up with its background tied to the upstream node sitting ahead of it.

### Automatically Creating a Merge Node When Adding Nodes

There's a tidy shortcut for wiring Merge nodes when you want the incoming clip slotted into your node tree right away as a composite's top layer: drag a clip out of an Operating System window—or pull a Generator out of the Effects Library—straight onto any connection line. Drop the resulting node and a Merge node is built automatically, its background input wired to the next node left of the connection you dropped onto, and its foreground input wired to the new node standing for the clip or Generator you just added.

Pulling a node out of the Media Pool onto a connection (left), then dropping it to spin up a Merge node composite (right). What's more, pull two or more nodes out of an OS window into the Node Editor all at once and Merge nodes get built automatically to tie them all together, making this a quick way to lay down a composite at the start.

Pull three nodes from an OS window into the Node Editor (left) and Merge nodes spring up on their own to tie them all together (right).
