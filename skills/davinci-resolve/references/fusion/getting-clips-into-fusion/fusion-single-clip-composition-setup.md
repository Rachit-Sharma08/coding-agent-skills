# Preparing compositions in the Fusion page and working on single clips in the Fusion page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md) / [Next section](referenced-compositions-and-generators.md)
<a id="source-adding-additional-referenced-clips"></a> <a id="source-creating-and-managing-referenced-compositions"></a> <a id="source-fusion-referenced-compositions"></a> <a id="source-getting-clips-into-fusion"></a> <a id="source-getting-clips-into-fusion-part-1"></a> <a id="source-how-nodes-are-named"></a> <a id="source-preparing-compositions-in-the-fusion-page"></a> <a id="source-the-reference-composition-thumbnail-in-the-media-pool"></a> <a id="source-the-sbspline-controls"></a> <a id="source-turning-one-or-more-clips-into-fusion-clips"></a> <a id="source-working-on-single-clips-in-the-fusion-page"></a>

### Getting Clips into Fusion

As you assemble your compositions, this chapter walks through the several routes for bringing clips into Fusion.

### Preparing Compositions in the Fusion Page

Most of the time, a clip reaches the Fusion page from the Edit or Cut page Timeline either on its own or as several layers wrapped inside a Fusion clip. Clips can also be dropped into a composition straight from DaVinci Resolve’s Media Pool. The route a clip takes into a Fusion composition can shape both how it behaves there and the resolution that composition hands back to the rest of DaVinci Resolve.

### Working on Single Clips in the Fusion Page

Set the playhead above a clip on the Edit or Cut page Timeline, press the Fusion page button, and that clip appears on the Fusion page as one MediaIn node wired to a MediaOut node. Fusion only pulls in the topmost visible clip. Any clip hidden because it sits on a lower track beneath others is skipped, unless you switch off the clips or tracks stacked above it. This manual informally calls these bare-bones default setups “single-clip compositions.” The MediaIn node stands for the picture handed to the Fusion page for more work, while the MediaOut node stands for the finished output passed along to the Color page for grading.

The default node tree shown the moment you open the Fusion page with the playhead resting on a clip. With this starting node layout, it’s simple to jump quickly onto the Fusion page and build fairly basic effects by leaning on the procedural freedom of node-based compositing. Say you have an establishing shot with no camera move that needs a touch of quick paint to hide some stray junk in the background; you can open the Fusion page, drop in a Paint node, and use the Stroke tool’s Clone mode to paint it away fast.

A basic paint pass laid over a static shot that has no camera move. TIP: When a single clip is pulled into Fusion through the Edit or Cut page Timeline, its resolution is that of the source clip rather than the Timeline resolution.

When you’re done, just return to the Edit or Cut page and keep cutting, since the whole Fusion composition stays bundled inside that clip, much the way Color page grades are also bundled inside a clip. Whether that clip gets slipped, slid, rippled, rolled, or resized, the Fusion effects you built along with the Color page grades you applied travel with it wherever it lands across your edited Timeline. TIP: Although you’ll generally want to handle all the compositing for a greenscreen-style effect on the Fusion page, you can also drop a keyer, like the superb DeltaKeyer node, on its own between the MediaIn and MediaOut nodes. Pulling a key this way attaches the alpha channel to the MediaOut node, so your clip on the Edit page gains transparency, which lets you put a background clip on a lower track of your Edit page Timeline.

### How Nodes Are Named

Even though the documentation calls nodes by their plain name, like “MediaIn,” the real node names in the Fusion Node Editor carry a number on the end, so you can tell one apart from another whenever several copies of the same node type are present.

### Turning One or More Clips into Fusion Clips

When you already know you’re building a more elaborate composited effect that needs several layers cut together with exact timings, you can spin up a “Fusion clip” straight off the Timeline. For instance, given a foreground greenscreen clip, a background clip, and one more graphic clip, you can pile them all onto the Timeline as superimposed clips. From there the Edit page slip and slide features let you line up their timings so they work together however you need. You can likewise cut several back-to-back clips together that you mean to use in a composition as a string of clips. With that done, you can select every clip in the stack to build a Fusion clip, making it simple to draw on all these layered tracks inside a Fusion composite. To create a Fusion clip: 1 Cut every clip you intend to use into the Edit page Timeline. 2 Highlight, all at once, each clip you want in the same composite. 3 Right-click any one of the highlighted clips and pick New Fusion Clip off the contextual menu. 4 A fresh clip called “Fusion Clip X” (with X being a number that climbs automatically) shows up in the Media Pool’s currently selected bin and on the Timeline, taking the place of the clips you had selected. 5 Rest the playhead above that clip and open the Fusion page to view how those clips are now laid out in the Fusion page Node Editor.

A pile of clips destined for a composite (Top), with that pile converted into a Fusion clip on the Edit page (Bottom). What’s great about building a Fusion clip is that every layered clip in a stack gets wired automatically into a cascading chain of Merge nodes that produce the layout of clips you want. Keep in mind that whichever clips sat at the bottom of the stack on the Edit page show up at the top of the Node Editor on the Fusion page, yet the layout of background and foreground input connections is set up to rebuild the very same compositional order.

The starting node tree built from the three clips we converted into a Fusion clip.

TIP: Fusion clips switch the working resolution of the individual clips so it lines up with the Timeline resolution. Say two 4K clips are layered one above the other in an HD Timeline; building a Fusion clip drops the clips down to HD. Fusion won’t give you the full resolution of the individual 4K clips. To keep the full resolution of source clips, take just one clip into the Fusion composition off the Edit or Cut page Timeline, then pull the rest into the Fusion composition through the Media Pool.

### Fusion Referenced Compositions

A newer, capable approach to putting Fusion composites on your clips goes by the name “Referenced Composition.” With this approach you can recycle your work across many clips or even across timelines. You build a referenced composition on the Edit page by picking one clip, or a stack of clips, then choosing “Create Referenced Composition” from the contextual menu. Doing so spawns a Fusion Referenced Composition in the Media Pool. You can step into the Fusion page and begin compositing, or give the Referenced Composition in the Media Pool a double-click to open it. To link referenced comps to other clips in any timeline, select the referenced comp, then right-click the target clip and pick “Link to Referenced Composition.” Whatever edits you make spread to every connected clip, because they’re all “referred” or “linked” to that one composition. Referenced Compositions offer a reliable, safe way to keep your work backed up and tidy, since they sit in the Media Pool and stick around even after the original referenced clip is removed from the timeline.

### Creating and Managing Referenced Compositions

To create a Referenced Composition: 1 Pick one or more timeline clips that sit “stacked” across tracks in an Edit window timeline (the clips must overlap in time at least to some degree). 2 Right-click and choose “Create Referenced Fusion Composition.” 3 The fresh reference composition, tied to the top selected clip, now turns up in the Media Pool. Double-clicking it in the Media Pool opens the referenced composition on the Fusion page. The Media nodes line up with where the source track clips sat relative to one another in the Edit timeline. Whatever the video track holds is handled as a source, so clips can be shaped creatively before they head onward to Fusion for compositing. Right-clicking a referenced composition in the Media Pool and picking the Usage option lets you survey and jump to its target linked clips. For iterating, you can also duplicate your referenced composition. The example that follows builds a basic reference composition from three clips, swapping out a logo on a truck.

Building a reference composition by picking several overlapping clips, then choosing Create Referenced Composition off the contextual menu.

### The Reference Composition thumbnail in the Media Pool

A double-click on the Reference Node takes us into Fusion, where we drop in a few Corner Positioner nodes to align the green stripe and logos so they fit.

With the referenced composition now in place, swapping the logo is easy; we just run a replace edit putting the new logo onto V3 in the timeline. That fresh logo is applied to the Fusion comp on its own, carrying the same settings.

### The sBSpline controls

### Adding Additional Referenced Clips

Once a referenced composition is established, you can hook on clip(s) that lean on the referenced composition to act on the other clips. To add clip references to a referenced composition: 1 Pick the referenced composition you’d like to tie to another clip. 2 Pick a target clip on the timeline, then right-click and choose “Link to Referenced Composition.” 3 Bring in further clips, one at a time if you prefer, drawing even from other timelines.
