# Copying clip settings using display node graph rippling adjustments among multiple clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copying clip settings using display node graph.
[Chapter index](INDEX.md) / [Previous section](display-node-graph-and-paste-attributes.md) / [Next section](display-node-graph-and-shared-node-copying.md) / [Copying Clip Settings Using Display Node Graph](display-node-graph-and-paste-attributes.md)
<a id="source-appending-a-node-to-multiple-clips"></a> <a id="source-creating-shared-nodes"></a> <a id="source-locking-shared-nodes"></a> <a id="source-rippling-adjustments-among-multiple-clips"></a> <a id="source-using-shared-nodes"></a> <a id="source-what-are-shared-nodes-good-for"></a>

### Rippling Adjustments Among Multiple Clips

Having graded a run of clips, if you discover you need a fast change pushed across several of them at once, the Color > Ripple Node Changes to Selected Clips/Current Group commands let you swiftly copy one clip's changes onto a number of others. These commands do, though, demand that you observe a few rules to land the outcome you are after. Rippling keys off each node's number to work out which changes flow to which nodes. Put differently, a change on Node 3 flows to the matching Node 3 on each remaining selected clip, or alternatively onto Node 3 across the rest of the current group's clips (which of the two depends on the command you pick). For changes to ripple from one clip onto several, all the clips must carry the same node count, at least for whichever nodes you are rippling. Attempt to ripple a change onto one or more clips lacking a node whose number matches the one you are rippling, and those clips receive no change at all. To ripple one node's change onto several selected clips: 1 Pick the clip you will use to make the change so it becomes the current clip, outlined in orange. 2 Then Command-click or Shift-click to pick the span of clips you want the change rippled onto, leaving them all selected in red.

The orange-outlined clip is the current one you are modifying, while the red-highlighted clips are those receiving the rippled change There is no requirement to pick the destination clips before you make the change, yet staging it all ahead of time can make it simpler to track what you are doing. The clip under modification ought to be outlined in orange, and the clips taking the rippled change ought to be highlighted in red. 3 Choose a node to alter. Ideally each selected clip carries a node whose number matches the one you are altering. Where a clip lacks that, it will not pick up the change you are about to ripple. 4 Apply whatever changes are needed, working any of the Color page's palette controls you require, apart from Camera Raw, Sizing, and Data Burn, which are not node‑specific. 5 Once the change satisfies you, pick Color > Ripple Node Changes to Selected Clips.

Your change ought to ripple onto every other selected clip that has a node of that same number, and within moments those clips' thumbnails ought to refresh to reflect it. Where you have built a group, rippling node tweaks onto the group's other clips is easier still. To ripple one node's change onto the current group: 1 Pick the clip you will use to make the change so it becomes the current clip, outlined in orange. For this to function it has to belong to a group. 2 Choose a node to alter. Ideally each selected clip carries a node whose number matches the one you are altering. Where a clip lacks that, it will not pick up the change you are about to ripple. 3 Apply whatever changes are needed, working any of the Color page's palette controls you require, apart from Camera Raw, Sizing, and Data Burn, which are not node‑specific. 4 Once the change satisfies you, pick Color > Ripple Node Changes to Current Group. Your change ought to ripple onto every other clip in the current group that holds a node of that same number, and within moments those clips' thumbnails ought to refresh to reflect it.

### Appending a Node to Multiple Clips

When you have tweaked a node on one clip and would like that tweak on several others, the Color > Append Node to Selected Clips command gets it done in a hurry. Run it ahead of one of the Ripple Node Change commands as a fast way to ensure several as-yet-ungraded clips share the same nodes, or run it on its own as a fast way to push the same node change onto several clips whether or not their node trees line up. To append a node onto other selected clips: 1 Pick the clip you will use to make the change so it becomes the current clip, outlined in orange. 2 Pick the node you wish to append onto other clips. 3 Then Command-click or Shift-click to pick the span of clips you want the change rippled onto, leaving them all selected red. The clip you copy from ought to be outlined in orange, and the clips taking the rippled change ought to be highlighted in red. 4 Pick Color > Append Node to Selected Clips. The chosen node ought to land at the tail of each selected clip's node tree, and within moments those clips' thumbnails ought to refresh to reflect it.

### Using Shared Nodes

Shared nodes exist to bring the payoff of automatically rippled changes across clips to colorists who favor a node layout flatter than Group Grading permits. Convert individual Corrector nodes into Shared nodes and copy them onto multiple clips, and you switch on linked adjustments straight from inside the clip grade. What that means is the clip grade is free to blend both clipspecific nodes and Shared nodes together inside one node tree. That keeps Shared nodes quick to work with, since you need not build groups or jump to a group node tree (the next section's topic) to enjoy linked adjustments across several clips.

A grade carrying an Unshared node (at left) and a Shared node (at center); a badge flags the Shared node, which is locked as well

### What Are Shared Nodes Good For?

A Shared node resembles a group grade, save that it asks for no grouping and drops into any ordinary grade. Whatever you change on a Shared node ripples on its own to every other copy of that node sitting in other clips' grades. On top of that, you may add as many Shared nodes to a grade as you wish and order them however you like to govern the sequence in which their operations run. And naturally you can scatter them among run-of-the-mill Corrector nodes Shared nodes are tremendously flexible. As examples, Shared nodes let you:

- Place a Color Space Transform Resolve FX or a LUT at the front of every clip drawn from one particular source
- Place a base correction on every talking-head shot of one particular interviewee
- Place a shot-matching tweak on each clip shot from one particular coverage angle

within a scene

- Place a stylistic tweak on every clip in one specific scene
- Lay down your base adjustments while grading with remote versions, so those adjustments

stay linked once you copy your remote versions onto local versions for fine tuning You can in truth mix and match Shared nodes across differently overlapping clip sets to pull off any or all of the above in one go. For instance, add one Shared node to adjust every clip from a given camera, add a second onto whichever of those clips fall in a given scene, then add a third onto whichever of those happen to be closeups of the lead actress, before tacking on one or two regular, unshared Corrector nodes for clip-specific tweaks.

### Creating Shared Nodes

Making a Shared node is simple, provided you have already built a node holding an adjustment you would like spread across several clips. To make a Shared node:

- Right-click any Corrector node and pick Save as Shared node.

### Locking Shared Nodes

The moment you convert a node into a Shared node, it locks on its own, which stops you from inadvertently adjusting it in ways that would hit every other grade relying on that same Shared node. To flip a Shared node's lock state, take one of these routes:

- Right-click any Shared node and pick Lock Node from the contextual menu.
- Bring up the Keyframe Editor, then within that node's keyframe track click the Lock icon sitting in its track header.
