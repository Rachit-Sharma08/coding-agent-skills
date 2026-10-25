# Applying effects and adding a node to the tree

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing layers in Fusion.
[Chapter index](INDEX.md) / [Next section](composite-edge-repair-and-merge-modes.md)
<a id="source-a-new-node-added-from-the-effects-library"></a> <a id="source-adding-a-node-to-the-tree"></a> <a id="source-adding-additional-media-to-compositions"></a> <a id="source-adjusting-fusion-sliders"></a> <a id="source-applying-effects"></a> <a id="source-automatically-creating-merge-nodes"></a> <a id="source-compositing-layers-in-fusion"></a> <a id="source-compositing-layers-in-fusion-part-1"></a> <a id="source-compositing-two-clips-together"></a> <a id="source-editing-parameters-in-the-inspector"></a> <a id="source-replacing-nodes"></a>

### Compositing Layers in Fusion

The aim of this chapter is to ground you well enough to shift comfortably from a layer-driven compositing program over to the node‑based workflow of Fusion. You will find down-to-earth guidance on how a node tree can be organized for straightforward layered composites.

### Applying Effects

Rather than jumping straight into composites built from many layers, we'll begin with a few really basic effects and grow our knowledge outward from there. When you open the Effects Library and click the disclosure control sitting to the left of Tools, a set of categories appears that holds every node Fusion offers. Recall that an individual node performs a single task, and when several of them work together you can assemble remarkably intricate output starting from modest pieces. Click the Effect category and its items appear. For this walkthrough we'll work with the TV effect.

Browsing the Effect category to find the TV node

### Adding a Node to the Tree

Suppose the MediaIn node on the Fusion page (or the Loader node in Fusion Studio) happens to be selected at that moment inside the Node Editor; a single click on, say, the TV node within the Effects Library drops that node into the tree just downstream of whatever was selected. Over on the Fusion page it shows up in the viewer right away, and that's because the MediaOut1 node is the one being viewed—so everything feeding into MediaOut1 from upstream gets processed and displayed.

### A new node added from the Effects Library

Within Fusion Studio you have to hit either the 1 or the 2 key to push the selected node into the viewer. Plenty of other techniques exist for placing nodes into a tree, yet learning your way around the Effects Library is a worthwhile starting point.

### Editing Parameters in the Inspector

If you want to refine an effect, head to the Inspector on the right and tweak that node's parameters. Whatever node is selected presents its controls there in the Inspector, where the majority of nodes carry a handful of control tabs shown as tiny icons sitting right below the node's title bar.

The Inspector displaying the TV effect's parameters Clicking the final panel on any given node brings up the Settings panel. A Settings panel belongs to every node, and it holds the parameters common to all nodes—things like the Blend slider together with the RGBA buttons. With these you decide which image channels get touched, and you can mix between the original picture and the applied effect.

The Settings panel, holding the channel-limiting plus mask-handling controls common to every node With the TV effect, as an instance, the output carries quite a bit of transparency, since the scan lines that get drawn in are likewise written into the alpha channel, which produces alternating transparent rows. Switching off the Alpha checkbox yields a more opaque picture, and if you open the Controls tab (that's the first tab) and push the Scan Lines slider rightward so its value climbs to 4 you'll get a stronger television look.

The TV effect as it started (left), alongside tweaks to the TV effect that render the clip more opaque (right)

### Replacing Nodes

Inside the Effect category of the Effects Library there's also a Highlight node, which scatters glints across an image's brightest spots. Rather than clicking the Highlight node—that would tack it on after whatever node is selected—you can drag a node out of the Effects Library and drop it directly onto a node inside the Node Editor, which swaps out the node there in the Node Editor.

Dropping a node out of the Effects Library over a node within the Node Editor so it gets swapped Here the Highlight1 node steps into the spot held by the TV node within the tree, and the fresh effect shows up in the viewer—in this case star-shaped highlights sitting over the image's lights. Now it's a matter of reaching for the Inspector controls to tailor the effect.

### Adjusting Fusion Sliders

As you drag any slider over in the Fusion Inspector—here that's the Number of Points slider—a small dot shows up below it. That dot marks where the slider's default value sits and additionally doubles as a reset control whenever you click on it.

Adjusting a slider reveals a reset button underneath it Every slider has its own particular span of minimum and maximum values, tied to whichever parameter is being changed. Here the Number of Points slider tops out at 24. That said, plenty of sliders (though not all of them) can have their range remapped if you type a bigger figure into the number field beside the slider. The moment you do, the slider's handle slides leftward as the range stretches to fit the value you just supplied.

Typing a bigger figure to widen the span across which a slider can work

### Compositing Two Clips Together

Fun as it may be to drop in single nodes for simple effects, sooner or later you'll want to bring in extra layers of footage so they can be merged into composites. Let's shift focus to a different scenario where a background clip needs to be combined with a foreground clip carrying a built-in alpha channel, so we can watch basic layering at work.

### Adding Additional Media to Compositions

It happens regularly that what begins as a fairly modest idea ends up requiring more media before you achieve the look you're after.

- Within Fusion Studio you handle this by bringing in more Loader nodes. Drop a fresh Loader node onto a blank spot in the Node Editor and you'll get a free-floating Loader2 node (numbered upward so it stays unique), which you can then wire up however you like.
- On the Fusion page you can pull up the Media Pool and drag clips straight onto the Node Editor to bring them into your tree. Drag a clip out of the Media Pool onto a blank region of the Node Editor and you'll get a free-floating MediaIn2 node (numbered upward so it stays unique), which you can then wire up in whatever fashion suits you.

The Media Pool as seen in the Fusion page

### Automatically Creating Merge Nodes

Should you want the arriving clip hooked up right away as the uppermost layer—the foreground—of a composite, then in Fusion Studio pick the Loader1 node and add a second Loader node. On the Fusion page, drag the new clip out of the Media Pool directly onto any connection line. Either way, the incoming MediaIn or Loader node turns automatically into the "foreground input".

Pulling a node out of the Media Pool over a connection (left), then releasing it so a Merge node composite forms (right) The Node Editor is packed with shortcuts of this sort so your compositions come together faster. Here's one for the case where a disconnected node needs compositing against a different node via a Merge node. Pull a connection out of the output of whichever node should be the foreground, and let go of it on top of the output of whichever node should be the background. That action spawns a Merge node automatically to assemble the composite. Don't forget: background inputs show up orange, while foreground inputs show up green.

Pulling a connection out of a disconnected node toward a second node's output (left), then releasing it so a Merge node composite forms (right) Adding Clips to a Fusion Composition From the File System Drag clips from your file system straight into the Node Editor and they get folded into the DaVinci Resolve Media Pool for you. So when you keep a collection of stock animated background textures and you've located one you'd like to use through your file system's search tools, just drag it directly into the Node Editor and it lands in whatever bin of the Media Pool is currently active.
