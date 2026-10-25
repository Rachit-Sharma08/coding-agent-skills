# Serial parallel and layer nodes and serial parallel and layer node tree structures

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grading overview.
[Chapter index](INDEX.md) / [Previous section](image-processing-order.md) / [Next section](converting-layer-mixers-to-parallel-mixers-overview.md)
<a id="source-adjusting-layer-node-strength-using-key-output-gain"></a> <a id="source-controlling-what-feeds-a-nodes-rgb-input"></a> <a id="source-converting-parallel-mixers-to-layer-mixers"></a> <a id="source-layer-mixer-node-structures"></a> <a id="source-layer-mixer-prioritization"></a> <a id="source-parallel-node-structures"></a> <a id="source-serial-node-structures"></a> <a id="source-serial-parallel-and-layer-node-tree-structures"></a> <a id="source-serial-parallel-and-layer-nodes"></a> <a id="source-serial-parallel-and-layer-nodes-1"></a> <a id="source-the-parallel-mixer-blends-all-input-nodes-together"></a> <a id="source-using-composite-modes-with-the-layer-mixer"></a>

## Serial, Parallel, and Layer Nodes

### Serial, Parallel, and Layer Nodes

Here we go over the four core node structures available for merging Color page adjustments in still more nuanced ways. With these approaches you can steer your order of operations and recombine several versions of the graded image far more precisely.

### Serial, Parallel, and Layer Node Tree Structures

A node tree can be laid out in a number of ways. Every approach gives you a distinct way of steering a set of image processing operations toward particular results. What follows explains how to put Serial nodes, Parallel nodes, and Layer nodes to work, plus how to apply LUTs, how to handle HDR media that lets you blend two separate exposures via two separate Source inputs, and how to layer on extra project-wide tweaks through the Timeline grade.

### Serial Node Structures

The plainest and most widely used node structure is a serial cascade of nodes, in which a straight chain of nodes is wired together one behind the next.

Serial nodes, in which one node's output hands a modified image along to the following node A good deal of the time, this way of building a tree of several operations is all that's required. It offers a plain, intuitive means of arranging your adjustments, akin in spirit to the layer stacks that other grading and compositing programs rely on to pile several operations onto a clip.

### Controlling What Feeds a Node’s RGB Input

Building a grade out of serially arranged nodes means each node's output becomes the input for the one after it, so how you order the nodes dictates the order of image processing operations. In the screenshot below, the node tree presents a run of three operations applied to a log-exposed, low-contrast clip. Node one broadens clip contrast and pushes saturation up. Node two singles out the sky and deepens its color. Node three pulls saturation down and warms the image. Over on the right, the outcome of this node tree is visible.

Working from the image data that Node 1 hands it, Node 2 extracts a clean key Had we instead swapped the positions of Nodes 2 and 3, the resulting key would be weaker.

Set against that, Node 3 extracts a weaker key from the image data passed to it by Node 2 Since the secondary operation samples from the image after it's been desaturated instead of from the source, the HSL Qualifier is left with thinner image data to work from, which can leave you with a poorer result.

### Parallel Node Structures

A different approach to laying out your corrections is the Parallel node structure, which lets you stack two or more overlapping adjustments at one point in a node tree. The Parallel node structure works well organizationally whenever you've got a cluster of secondary corrections to apply together in one go. It's also worth using for its distinctive way of blending overlapping image adjustments. What makes it possible is the Parallel Mixer node, which carries several RGB inputs and one RGB output. That arrangement lets the Parallel Mixer fold multiple Corrector nodes together and put out a single image as the result. The moment you attach a Parallel node to an existing node, DaVinci Resolve drops one Corrector node beneath the current node on its own and hangs a Parallel Mixer node off its output.

Attaching a Parallel node onto Node 2 brings the Parallel Mixer along on its own TIP: To build a run of Parallel nodes that tie into the output of whichever node is selected, lay down a Serial node before creating the first Parallel node. When you wire another node into a Parallel Mixer node by hand, you can drag from that node's output across to the Parallel Mixer node, and an input gets added for you automatically.

To add a further, unconnected input onto a Parallel Mixer node:

- Right-click a Parallel Mixer node and choose Add One Input.

Normally, the RGB input of each Corrector node tied to a Parallel node feeds from that same node's output. The upshot is a stack of nodes that all take the identical state of the image as their input. That makes it painless to apply several secondary operations without fretting over whether tweaking one will disturb the keys of the rest.

You may keep tacking on more Parallel nodes at will, every one drawing from a shared source Each time you drop in another node in parallel, the Parallel Mixer tacks on another input. There's no cap on how many nodes you can run in parallel. Every node hooked to a Parallel Mixer has its adjustments blended on equal footing, no matter which nodes sit highest. For the example coming up, each of three parallel nodes lays down its own overlapping window.

### The Parallel Mixer blends all input nodes together

As the image on the right shows, the three tints produced by the overlapping windows all combine on equal terms; the colors merge into one another as though optically blended. In most situations, that's precisely the behavior you're after when blending overlapping naturalistic color adjustments.

### Converting Parallel Mixers to Layer Mixers

Conversely, when you want your overlapping color adjustments to take precedence over one another, or you'd like to fuse several adjustments through composite modes, the Layer Mixer node is the better choice. If you've already built a Parallel Mixer structure and decide to turn it into a Layer Mixer, that's possible. Here's how to convert your Parallel Mixer over to the layered variety: right-click the node, then from its menu pick Morph Into Layer Mixer Node.

### Layer Mixer Node Structures

In its structure, the Layer Mixer closely mirrors the layout the Parallel Mixer uses. There are, though, two important distinctions. To begin with, the Layer Mixer node fuses multiple adjustments while granting priority to the image adjustment sitting at the lowest overlapping node input. On top of that, you can join all of the Corrector nodes wired to a Layer Mixer through any of several composite modes, opening up a broad range of visual effects. Owing to these parallels, stacking nodes with the Layer Mixer plays out much like building a Parallel node structure.

### Layer Mixer Prioritization

For the example below, the very same node structure from the Parallel Mixer example reappears, only now the three overlapping color adjustments are combined through the Layer Mixer.

By giving precedence to nodes wired into lower inputs, the Layer Mixer lets each node's output fully hide whatever sits behind it This time, rather than the three adjusted color tints blending, notice that the blue tint, tied to the lowest input of the Layer Mixer, takes the lead and masks the overlapping zones of the other two adjustments. The green tint, meanwhile, tied to the middle input of the Layer Mixer, blankets the overlapping stretch of the orange tint, which is tied to the highest input of the Layer Mixer.

Shuffling which connections land on which Layer Mixer inputs alters each node's priority, and just as with the Parallel Mixer, you can add further inputs by hand or by dragging a node's output onto the Layer Mixer. Where the Layer Mixer's prioritization really pays off is when you have an overlapping adjustment that must override everything else on that stack. For the example coming up, a pair of nodes feed into the Layer Mixer node. Node 2 lays a high-contrast, cool look across the whole clip. Node 3 singles out the skin tone, which clashes with the stylized background, and gives it a different, more natural adjustment.

With the layer mixer in play, the grade on Node 3 outranks the one on Node 2, so the end result marries the high contrast off Node 2 to the reworked skin tone off Node 4 Thanks to the Layer Mixer's prioritization, the change made to the woman's skin tone entirely overrides the change made by the node above it, delivering the best of both worlds through one straightforward adjustment.

### Using Composite Modes With the Layer Mixer

You're free to merge the adjustments from every node tied to a Layer Mixer node by way of the very same Composite modes you'd find when compositing clips in the Timeline. That lets you fuse various overlapping image adjustments through compositing math, whether for creative looks or for practical repairs. The straightforward example below presents two overlapping Corrector nodes hooked to a Layer Mixer node set to the Add composite mode. Node 3 carries no adjustment, while Node 5 has an extremely high-contrast curve adjustment in place, plus a blur, which in effect picks out the image's highlights and softens their edges.

Merging a pair of nodes through the Layer Mixer with its mode at Add to build a glow Summing both treatments together produces a hot glow that blows out the image's highlights. A great many further effects are achievable with the assorted composite modes on offer. To read more about composite modes, turn to Chapter 50, “Compositing and Transforms in the Timeline.”

### Adjusting Layer Node Strength Using Key Output Gain

No matter whether you're stacking overlapping corrections or blending separate adjustments through Composite modes, you'll hit moments where you want to dial down one overlapping adjustment's sway relative to the other nodes feeding the Layer Mixer node. You pull this off through each overlapping node's Key Output Gain parameter, found in the Key palette.

Using the Output Gain parameter in the Key palette

The default for Key Output Gain is 1.00, and dropping it below that weakens how much that node feeds into the Layer Mixer. Carrying on from the earlier example, picking Node 4 (the high‑contrast image behind the glow), opening the Key palette, and pulling the Key Output Gain parameter down to 0.50 cuts the Glow effect's intensity in half. Key Output Gain can be used to balance the proportion of any number of overlapping adjustments so you land on the ideal mix for whatever you're doing. TIP: That same Key Output Gain parameter also works for balancing the proportion of adjustments being merged through the Parallel Mixer node.
