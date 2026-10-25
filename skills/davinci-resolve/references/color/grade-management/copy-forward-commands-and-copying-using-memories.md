# Copy forward commands and copying using memories

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grade management.
[Chapter index](INDEX.md) / [Previous section](rendering-versions-and-copying-grades.md) / [Next section](display-node-graph-and-paste-attributes.md)
<a id="source-aligning-keyframes-to-a-specific-frame-while-copying-grades"></a> <a id="source-append-node-graph"></a> <a id="source-appending-grades-places-them-after-the-original-nodes"></a> <a id="source-copy-forward-commands"></a> <a id="source-copying-and-pasting-all-settings-from-one-node-to-another"></a> <a id="source-copying-from-stills-in-the-gallery"></a> <a id="source-copying-individual-nodes-and-settings"></a> <a id="source-copying-using-memories"></a> <a id="source-copying-using-preview-memory"></a>

### Copy Forward Commands

Yet another easy approach uses the equals (=) and minus (–) keys to pull a grade forward from one or two clips back of the one currently selected. It works beautifully in shot-reverse-shot scenes, where you cut between two coverage angles that share the same grade. To copy grades forward:

- To pull a grade forward from the clip one back: use the Color > Apply Grade From One Clip Prior menu item, or just press Equals (=).
- To pull a grade forward from the clip two back: use the Color > Apply Grade From Two Clips Prior menu item, or just press Minus (–).

### Copying Using Memories

Memories are all but the same as stills, save that each one wears a letter (A–Z) for quick recall through keyboard shortcuts. A memory bank above the Gallery browser shows at a glance which saved grade is tied to which letter. That keeps a pile of saved memories straight when you're spreading them across many clips throughout a scene or program. You might, say, stash a memory per coverage angle in a knotty scene so grades copy forward effortlessly. Or you might stash a memory holding the grade on each interview subject's headshot in a documentary, then copy that grade forward as the documentary unfolds. To stash the current clip's grade in a memory for later, do one of the following:

- Choose Color > Memories > Save Memory A–H (Option-1–8).

Save a grade into a memory that's already occupied and the old memory is overwritten.

To drop a memory onto one or several timeline clips, take any of these routes: 1 Over in the Thumbnail timeline, choose the destination clip or clips — the current one, or a range gathered through Command-Clicking or Shift-Clicking. 2 Then copy a grade onto the selected clips one of these ways:

- Right-click a memory and choose Apply Grade.
- Choose Color > Memories > Load Memory A–H (Command-1–8).

To clear a memory:

- Right-click a memory, then choose Clear.

### Copying Using Preview Memory

You can also trial a memory or saved grade on the current clip, then keep it if it lands or fall back to the prior grade if it doesn't. To Preview Memory: 1 Park the playhead on the clip where a memory is to be trialed. 2 Pick Color > Preview Memory (Option-Shift-P). 3 Take one of these routes:

- Right-click any saved still in the Gallery and choose Apply Grade.
- Choose Memories > Load > Memory A–H (Command-1–8). Your chosen grade or memory is now showing as a preview. 4 Now, take one of these two paths to accept or reject the memory:
- Pleased with the look? Leave it be and move along to the next clip.
- Unconvinced? Choosing Color > Preview Memory (Option-Shift-P) once more rolls

the clip back to its original grade.

### Copying from Stills in the Gallery

As noted earlier, every still kept in the Gallery holds the grading information together with a picture of the frame it was grabbed from. That saved grade can land on any Timeline clip. IMPORTANT: A copied grade overwrites whatever grades already sit on the clip or clips you copy onto. To drop a still's grade onto one or several selected timeline clips: 1 Over in the Thumbnail timeline, choose the destination clip or clips — the current one, or a range gathered through Command-clicking or Shift-clicking. 2 Then copy a grade onto the selected clips one of these ways:

- Drag the still out of the Gallery and into the Viewer.
- Right-click a still in the Gallery and choose Apply Grade.
- Middle-click a still in the Gallery.
- Double-click a still so it wipes against the current Timeline clip inside the Viewer, then right‑click

the Viewer and pick whichever entry you need from the Apply Grade submenu.

### Append Node Graph

A saved grade can also be appended to any timeline clip. Doing so tacks the saved still's whole node graph onto the tail of the current clip's node tree. Put differently, the current clip's grade survives intact and the applied grade simply joins on at its end. With a little forethought you can stash partial grades that pull off specific effects or adjustments out of just a handful of nodes. Those fragments then become a toolkit you bolt onto other grades to mix and match assorted adjustments and effects. You might, for instance, build a three-node glow effect, save it, and later drop that effect onto the end of an entirely different clip's grade.

### Appending grades places them after the original nodes

To tack a saved grade or memory on as separate nodes, take either route:

- Drag a still or memory out of the Gallery onto a connection line within the Node Editor; once the plus icon shows, let go and its nodes append into the node tree beginning at that connection.
- In the Gallery, right-click a still or memory and pick Append Node Graph. Normally, appending a memory or still's node graph onto another node graph dumps a whole pile of fresh nodes in. That may be precisely what you're after, yet when you'd rather keep things tidier, you can instead append node graphs as compound nodes.

To append a saved grade or memory as a compound node:

- Command-drag a still or memory out of the Gallery onto a connection line within the Node Editor; once the plus icon shows, let go and its nodes append to the node tree as one compound node.

NOTE: When you append a gallery still's nodes onto a grade, how the keyframes land depends on the Gallery's “Apply Grades Using” setting. For more information, see Chapter 141, “Using the Gallery.”

### Aligning Keyframes to a Specific Frame While Copying Grades

When you need a keyframed grade copied so its opening keyframe sits on one particular Timeline frame, the steps below get you there: To copy a grade and pin its keyframes to a specific Timeline frame: 1 Right-click the Viewer, choose Grab Still, and a keyframed grade is stashed as a Gallery still. 2 In the Thumbnail timeline, pick the clip that should receive the saved grade. 3 Double-click the Gallery still to wipe it in the Viewer against the current clip. 4 Park the playhead on the frame of this clip where you want the saved grade's first keyframe to fall. 5 Right-click in the Viewer and walk through Apply Grade > Align Keyframes to Current Frame.

### Copying Individual Nodes and Settings

Copy a grade between clips and everything transfers but the keyframes and motion tracking. There is, though, a single way to bring motion tracking from one clip to another: by copying and pasting individual node settings. The trick saves time while you assemble intricate node trees, since you can reuse particular nodes or node settings drawn from earlier grades.

### Copying and Pasting All Settings From One Node to Another

The most basic move is to grab all of one node's settings and drop them onto another node. That makes it painless to clone things like windows, qualifier settings, keyframing, or motion tracking you want to reuse in another node as the footing for a fresh operation. It's also a fast manual way to ripple a change made in a node out to that same node within another clip's grade. To shift a node's settings across from clip to clip, take either route:

- Option-drag one node atop another. On release, the dragged node's settings overwrite those of the node you dropped onto.
- Pick a node whose settings you want and choose Edit > Copy (Command-C). Then pick a destination node — in the current grade, in another clip's grade, or a node you create fresh — and choose Edit > Paste (Command-V) to lay the copied settings in. The pasted node settings replace whatever that node held before.
