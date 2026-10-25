# Copying node stack layers and post group node stack layer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node editing basics.
[Chapter index](INDEX.md) / [Previous section](extracting-a-node-and-inserting-a-node.md)
<a id="source-adding-inputs-and-outputs-to-compound-nodes"></a> <a id="source-beforeafter-creating-a-compound-node"></a> <a id="source-clip-vs-timeline-grading"></a> <a id="source-copying-node-stack-layers"></a> <a id="source-grading-compound-nodes"></a> <a id="source-identifying-nodes"></a> <a id="source-nesting-compound-nodes"></a> <a id="source-post-group-node-stack-layer"></a> <a id="source-putting-nodes-into-hdr-mode"></a> <a id="source-selecting-track-mode-in-the-node-editor"></a> <a id="source-using-compound-nodes"></a>

### Copying Node Stack Layers

It's possible to copy — not just apply — a Gallery Timeline Clip's Active Node Stack layer. To do so, right-click a Timeline Clip in the Gallery and pick Copy Active Layer.

### Post Group Node Stack Layer

Inside Project Settings beneath General Options > Color sits a checkbox named Post Group Node Stack Layer. Tick this checkbox and the final node stack layer gets processed after the Group PostClip node graph. The function lets you reserve that last node stack layer for post group grades and transforms.

Checking the Post Group Node Stack Layer box in Project Settings > Color

With the order revised, the node stack now runs Layer 3 Special Sauce after the Group Post-Clip layer (the one spun up automatically when you group clips). Ordinarily the Group Post-Clip layer would come last.

### Using Compound Nodes

One more node structure handy for keeping complex node trees in order is the compound node. Command-click to pick any number of nodes in the node tree (the picked nodes turn white), then invoke the “Create Compound Node” command to tuck all the selected nodes inside a single node.

### Before/after creating a compound node

The compound node that comes out of this carries however many inputs and outputs are needed to take on the connection lines that joined your selected nodes to the rest of the node tree. Compound nodes help you tidy complicated node trees by tucking groups of nodes that cooperate on one task inside a single node. You can likewise convert a set of nodes you're using to build a specific effect into a compound node before saving it to the Gallery. Assembling an effects library this way makes reusing them via the Append Grade command simple, sparing you the burden of piling lots more nodes into your grade later. Methods for creating and working with compound nodes:

- To create a compound node: Command-click every node bound for the compound node so each takes a white highlight, or drag a bounding box over a cluster of nodes. Next, from the contextual menu opened by right-clicking one of those selected nodes, pick Create Compound Node.
- To edit a compound node: Either double-click whichever compound node you mean to open, or, from the contextual menu reached by right-clicking any compound node, pick Show Compound Node. That node's contents appear in the Node Editor, standing in for the overall node tree.
- To exit a compound node you're editing: Returning to the top level node tree takes a double-click on the leftmost entry in the path control along the bottom of the Node Editor, or a click on the compound node's name. You can instead, from the contextual menu opened by right-clicking in the compound Node Editor, pick “Exit Compound Node.”
- To label a compound node: With a compound node right-clicked, pick Change Label off the contextual menu and type a fresh label for it. Tap the Return key once finished.
- To decompose a compound node: From the contextual menu raised by right-clicking whichever compound node is to be decomposed, pick “Decompose Compound Node.” The compound node vanishes, giving way to the original nodes it held. Note that any adjustment you'd made on the compound node itself gets discarded the moment you decompose it back into its component nodes. To keep that compound node adjustment, copy it first, decompose the node, then build a new node and paste in what you copied.

### Adding Inputs and Outputs to Compound Nodes

Once you open a compound node's contents using the Show Compound Node command, you're free to make whatever changes you wish to the node tree inside, but you also get the choice of rightclicking within the Node Editor and choosing Add Source to attach an input to the compound node, or Add Output to attach an output. Tacking on more inputs and outputs lets you wire the node into the rest of your node tree in more involved ways. Inputs and outputs that stay disconnected don't affect your grade. Beyond that, the Add Alpha Source and Add Alpha Output contextual menu commands let you tack KEY inputs and outputs onto a compound node, making it simple to route key or alpha channel data to other connections in the surrounding node tree.

### Nesting Compound Nodes

Compound nodes can also be nested within other compound nodes, if necessary.

### Grading Compound Nodes

Once a compound node exists, selecting it lets you apply one or several adjustments by way of the compound node itself, which in effect layers those adjustments after every other adjustment carried out by the nodes housed inside it. That gives you the chance to “trim” the impact that compound node has on your grade, or to confine it with a qualifier or window. To adjust the individual nodes tucked inside a compound node, you must first open the compound node. After that, you can select and adjust any node just as you normally would.

### Identifying Nodes

As you apply various adjustments to nodes, small badges show up beneath them signaling what each node is up to. Because nodes can hold several adjustments, any one node may carry multiple badges; how many a node displays hinges on the Node Editor's zoom level. Bigger nodes display more badges, while smaller ones display fewer, concealing whichever badges won't fit. Another handy organizational touch in the Node Editor is an automatic tooltip that pops up whenever you rest the pointer on a given node, presenting a tidy rundown of every operation applied to that node.

(Left) Beneath every node, badges signal which adjustments it holds. (Right) Driving a node into HDR mode through that node's contextual menu

### Putting Nodes into HDR Mode

While using the Color page's various grading controls to grade wide-latitude images for HDR output, switching on the HDR mode of the node at hand can prove handy: right-click the node within the Node Editor, then off the contextual menu choose HDR Mode. The setting retunes that node's controls so they operate across an expanded HDR range. In practice, that eases work on wide-latitude signals via controls letting you adjust separate tonal ranges — Lift/Gamma/Gain, Custom Curves, Soft Clip, and the like.

### Clip vs. Timeline Grading

As a rule, the Node Editor offers two modes. The default Clip mode lets you build separate grades for each clip or group in the Timeline. The Timeline grade mode, by contrast, lets you lay a single grade over every clip in the Timeline at once, as the Thumbnail timeline shows in the screenshot that follows.

A paragon of sophisticated grading, the author lays a red edge vignette over every clip across the project at once by way of the Timeline grade Plenty of reasons might lead you to do this. Working on a commercial spot, for instance, you could lean on Clip grades for general correcting and scene-to-scene balancing, then turn to the Timeline grade to lay one stylistic grade over the whole spot at once. That way, whatever style changes the client requests can land across the entire spot in an instant.

A further case would be reaching for the Timeline grade to apply corrections aimed at QC issues that thread through a whole program — desaturating highlights or selectively darkening one particular shade of red anywhere it shows up. To switch between Clip and Timeline grading modes:

- Pick the mode out of the drop-down menu over at the Node Editor's top right.

### Selecting Track mode in the Node Editor

- Click whichever dot on the Node Editor toolbar maps to the Clip or Timeline mode

Two dots indicate whether you're in Clip or Timeline mode, and clicking them switches between the two NOTE: Resetting the Timeline grade via the Color > Reset All Grades and Nodes command resets the Output Sizing parameters along with it. A pair of dots atop the Node Editor lets you flip between Clip and Timeline modes with one click. Working on a clip that belongs to a group, you'll see four dots instead, granting quick access to the Pre-Clip and Post-Clip Group modes as well.

Group grading gets a fuller account in Chapter 142, “Grade Management.” Timeline Grades and Saved Stills Saving a Gallery still stores both the Clip and Timeline grades. When you apply a grade out of that still, though, only one lands — either the Clip grade or the Timeline grade — according to which mode the Node Editor happens to be in. Saving and applying grades is documented in greater detail in Chapter 143, “Node Editing Basics.”
