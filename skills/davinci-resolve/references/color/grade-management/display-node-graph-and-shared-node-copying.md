# Copying clip settings using display node graph copying shared nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copying clip settings using display node graph.
[Chapter index](INDEX.md) / [Previous section](display-node-graph-and-multiclip-ripple.md) / [Copying Clip Settings Using Display Node Graph](display-node-graph-and-paste-attributes.md) / [Next section](group-grading-versions-and-grade-export.md)
<a id="source-available-options-in-the-node-editor-modes-drop-down"></a> <a id="source-converting-shared-nodes-back-to-corrector-nodes"></a> <a id="source-copying-shared-nodes"></a> <a id="source-creating-and-managing-groups"></a> <a id="source-deleting-shared-nodes"></a> <a id="source-grade-management-part-4"></a> <a id="source-using-adjustment-clips"></a> <a id="source-using-group-modes-to-control-which-grades-ripple-and-which-dont"></a> <a id="source-using-groups"></a>

### Copying Shared Nodes

Since Shared nodes are at bottom just Corrector nodes living inside clip grades, handling them is painless. Having built one or more Shared nodes, you have several routes for copying them onto other clips' grades throughout your program so you can cash in on the linked adjustments they afford. Routes for copying Shared nodes across several clips: Adding a Shared node onto a different clip's grade through the Node Editor contextual menu: As soon as a node is saved as a Shared node, it turns up at the foot of the Node Editor contextual menu's Add Node submenu, so dropping any Shared node onto any clip is trivial. Give the Shared node a custom label and that label is what shows in the contextual menu, making it quicker to spot. Folding Shared nodes into a basic grade bound for copying onto other clips: Build one or more Shared nodes while first assembling a grade, and copying that grade onto other clips brings the Shared nodes along by default. Storing a Shared node as a Gallery still and putting it on other clips: Stash a grade containing a Shared node in the Gallery, and each time you copy that Gallery still onto another clip its Shared node rides along. Building a Shared node and tacking it onto a batch of further clips: If you have already graded a handful of clips in a scene, drop a Shared node at the tail of one clip's grade, keep it selected, then select every other clip in the scene and pick Append Node to Selected Clips. Leaning on Shared nodes to hold linked adjustments while copying remote grades onto local grades: Lay your base adjustments with Shared nodes while grading via Remote Versions to auto-copy those grades onto other clips sharing the same source media, and the adjustments hold their link once you copy the remote versions onto local versions for fine tuning. The Gallery also offers options governing what occurs when you copy a grade that holds shared nodes inside it.

### Converting Shared Nodes Back to Corrector Nodes

Now and then you have to halt a node's sharing. Say you want to copy a grade from another scene as the seed for a new one; odds are you do not want its shared nodes staying shared while you tailor that grade to the new scene. For that case, convert the Shared node back into a plain Corrector node, apply whatever tailoring the new scene calls for, and then promote that node into a fresh Shared node specific to the new scene. To convert a Shared node back into a Corrector node:

- Right-click any Shared node and pick Convert to Corrector from the contextual menu.

### Deleting Shared Nodes

When you have a Shared node in use across multiple clips and decide to sever the link binding them so each runs on its own, you can “delete” that particular Shared node. Doing so leaves the now-unlinked nodes sitting in every node tree where they appear yet wipes out their effect. The Shared node is also dropped from the Add Node submenu. To Delete a Shared node:

- Right-click any Shared node and pick a node to delete from the Delete Shared Node submenu.

### Using Adjustment Clips

Another way to put one grade onto multiple Timeline clips is with Adjustment clips laid over a number of other clips in the Timeline. Use them to drop one grade onto every clip in a scene, or to pile extra color tweaks or trims onto a stretch of clips through a second grade riding above the per-clip grades already in place.

An Adjustment clip (seen selected within the Mini Timeline) putting a cooler grade onto four further clips of a scene

Adjustment clips shine when you need to push adjustments onto a set of clips you expect to keep revising. Edit a grade inside an Adjustment clip and that edit lands automatically on every clip sitting below it in the Timeline. Grades coming from adjustment layers can also be switched off by disabling the layers, whether one by one or by disabling a whole track that contains adjustment layers. You edit Adjustment clips into the Timeline over on the Edit page, and they live in the Effects bin of the toolbox within the Effects Library. With an Adjustment clip stacked above one or more Timeline clips, every effect placed on the Adjustment clip carries down to all the clips beneath it. The kinds of effects Adjustment clips can apply are:

- ResolveFX and OpenFX plugins
- Inspector parameters, including Composite, Transform, Cropping, and Dynamic Zoom
- Fusion page effects
- Color page grading and sizing

Effects clips give you a fast, easily reworked means of laying one or more grades and effects across a band of clips. TIP: You can group several adjustment layers together so Group and Clip grades reach the adjustment layers, chaining multiple adjustment layers when you want the very same trim or stylistic move spread over multiple scenes scattered across noncontiguous parts of the Timeline.

### Using Groups

Among DaVinci Resolve's strongest tools for arranging grades across many clips is grouping. A group is a hand-built collection of clips bound by automatic linking, which lets you readily steer how grades ripple across the clip sets you mark out. With clips grouped, picking any one member surfaces a group “linked” badge at the top right of every group clip's thumbnail.

The green link icon indicates this clip is in a group Build as many groups inside a single project as you require. You may add or pull shots out of the current group, and the current group is set by the last shot you selected (should it belong to a group, that becomes the new current group).

With clips grouped, you have four Node Editor modes to pick from when grading the current clip. Your pick decides whether that grade ripples automatically to every other member of the group or stays confined to that single clip. By that route you can stack several node trees — some that ripple, one that does not — to arrive at each group clip's final look. As one example, you might group every clip shot from the same coverage angle in a scene. You might equally group every clip from a stretch of B-roll bound for the same treatment. Done this way, any time you change or otherwise update one group member through one of the rippled Node Editor modes, every clip in the group shifts together. This section covers building and managing groups, how to get the most from them, and the pitfalls to watch for so groups serve you best.

### Creating and Managing Groups

The steps below cover building, loading, editing, and removing groups. To build a new group: 1 Mark one or more clip thumbnails in the Timeline. Grab a contiguous stretch of clips by clicking one and Shift-clicking another, or assemble a noncontiguous set by Command-clicking individual thumbnails anywhere across the Timeline. 2 Right-click one of the marked thumbnails and pick Add Into New Group. 3 Enter a name in the Group Name dialog's field and click OK. The new group comes into being, and the clips you had marked now carry the “linked” group badge above their thumbnails. To bring up a different group, take one of these routes:

- Slide the playhead onto another clip that belongs to that group.
- Right-click any clip in any group and pick Group > “Name of group” > Load. That group now becomes the current one. The Add Into Current Group command will then drop a clip into the just-loaded group.

To drop one or more clips into an existing group: 1 Bring up the group you want to add clips to. 2 Mark one or more clip thumbnails in the Timeline. Grab a run of adjacent clips by clicking one then Shift-clicking another, or build a scattered set by Command-clicking individual thumbnails anywhere in the Timeline. 3 Right-click one of the marked thumbnails and pick Group > “Name of group” > Assign to Group. The marked clips now show the “linked” group badge above their thumbnails. To pull one or more clips out of an existing group: 1 Mark, in the Timeline, one or more clip thumbnails you want gone from a group. Grab an unbroken span of clips by clicking one and Shift-clicking another, or form a discontiguous set by Command-clicking individual thumbnails wherever they sit in the Timeline. 2 Right-click one of the marked thumbnails and pick Remove From Group.

To rename a group: 1 Right-click any clip in any group and pick Group > “Name of group” > Rename. 2 Enter a fresh name in the Group Name dialog's field and click OK. The group takes the new name. That name turns up as a new submenu under the Timeline contextual menu. To remove a group:

- Right-click a clip in the group you want gone and pick Group > “Name of group” > Delete.
- This wipes the group while holding onto the last grade applied within each clip.

DaVinci Resolve builds a default smart filter covering every clip in the current group. You will find it in the Clips drop-down beneath Grouped > Current Group.

### Using Group Modes to Control Which Grades Ripple and Which Don’t

After you build a group and then click any clip belonging to it, extra Node Editor modes open up that let you layer several tiers of grades onto that group's clips.

### Available options in the Node Editor modes drop-down

When a clip is not grouped, two dots atop the Node Editor let you flip between Clip and Timeline modes with one click. When you are on a clip that belongs to a group, four dots appear instead, opening quick access to the Pre-Clip and Post-Clip Group modes too.

The four dots up top in the Node Editor are where you pick the mode you want to work in

Any node tree you build in the Group Pre-Clip and Group Post-Clip modes ripples its changes automatically onto every member of a group. A node tree built in Clip mode stays tied to its own clip. A node tree built as the Timeline grade hits the whole Timeline in one stroke. Stacking node trees from these various modes makes it easy to fuse clip-specific changes with group-wide ones and speed up grading.

- Group Pre-Clip: A node tree built under this mode touches every clip across the group at the same time. Pre-Clip work pays off when you want one overarching grade to serve as a launch point for the scene, like when a batch of log-encoded clips needs normalizing a certain way, or when you’re after a base grade that lifts every clip in a scene across the board.
- Clip: The Clip grade maps to whichever local or remote version is tied to that particular clip. A node tree assembled in Clip mode reaches only the single clip you’ve selected. Each Local and Remote version you build lives in Clip mode. Clip work earns its place when you’re matching clips against one another within a scene, running clip-specific secondary moves, or doing any other adjustment meant for the current clip alone rather than the whole group. Clip moves land after the Pre-Clip moves do.
- Group Post-Clip: A node tree built under this mode likewise reaches every clip across the group at once, though these moves apply once the Clip moves have. Post-Clip work comes in handy for laying a creative look across a whole scene, so that down the road, reworking a scene’s look takes just one set of moves that ripple automatically across the entire group.
- Timeline: A node tree built under this mode touches each and every clip throughout the whole Timeline. Timeline work serves you well whenever a single change is meant to hit every single clip in one go.

Because each Node Editor mode processes its image work in sequence, staying on top of the order of operations shaping any given clip is straightforward.
