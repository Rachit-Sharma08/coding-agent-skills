# Media pool browsing and selection

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing clips for editing and viewer playback.
[Chapter index](INDEX.md) / [Previous section](viewer-and-logging-shortcuts.md) / [Next section](single-viewer-and-source-clip-preparation.md)
<a id="source-browsing-clips-in-the-media-pool"></a> <a id="source-duplicating-clips-in-the-media-pool"></a> <a id="source-selecting-a-contiguous-range-of-clips"></a> <a id="source-selecting-a-noncontiguous-range-of-clips"></a> <a id="source-selecting-clips-in-the-media-pool-to-edit"></a> <a id="source-source-and-timeline-viewers"></a> <a id="source-source-and-timeline-viewers-vs-single-viewer-mode"></a> <a id="source-thumbnail-hover-scrubbing"></a> <a id="source-viewer-playback-and-navigation"></a>

### Browsing Clips in the Media Pool

The steps below explain how to pick one or several clips inside the Media Pool for different editing jobs — whether you open a clip in the Source Viewer or gather a batch of clips for drag-and-drop work. We begin by covering the various ways to look through what the Media Pool holds, so you can locate the clips you want before settling on a selection for the next step. Ways to browse clips in the Media Pool: while Metadata View mode is active, every clip appears as its own card carrying a thumbnail alongside essential clip metadata. The intent of this view is to surface richer metadata than a plain thumbnail yet stay more focused than the List view. Paired with its Sort modes, this becomes a strong tool for arranging and rearranging the clips held in your Media Pool.

- Hover-scrubbing a thumbnail in the Media Pool’s Metadata view: slide the pointer across a thumbnail and its frames scrub past.

The Metadata View icon view (its icon lit up in the top bar), with the scrubbed thumbnail sitting beside that clip’s metadata

- Hover-scrubbing a thumbnail in the Media Pool’s Thumbnail view: move the pointer over a thumbnail and you’ll scrub through what it contains.

### Thumbnail hover scrubbing

- Working with the Media Pool Filmstrip in List view: turn on “Show Filmstrip” from the Media Pool’s option menu. Click a clip and it appears in the Filmstrip running along the top of the Media Pool; pass the pointer over the Filmstrip to see it play. Whenever you like, double-clicking a clip in the Filmstrip opens it into the Source Viewer.

Using the Filmstrip when the Media Pool is in List view

TIP: As you browse footage, a double-click in the Media Pool opens any clip you’d like to inspect more closely in the Source Viewer. At the same time, a single clip can keep loading other clips in the Filmstrip, letting you weigh several clips against the main one still sitting in the Viewer.

### Selecting Clips in the Media Pool to Edit

After locating one or more clips you intend to use, the next move is to highlight them so you can carry out an edit. Ways to choose clips in the Media Pool with the mouse:

- To grab a single clip: Click a clip in the Media Pool.
- To grab an unbroken span of clips: From Metadata, Thumbnail, or List view, drag a marquee across every clip you want, or click the first clip of a run and then Shift-click the last one to capture both ends plus everything between them.

### Selecting a contiguous range of clips

- To grab a scattered set of clips: Command-click every clip you’d like in the group. Alternatively, keep the Command key held while dragging marquees across unselected clips to fold them into the group, or across already-selected clips to drop them back out.

### Selecting a noncontiguous range of clips

Ways to choose clips from the keyboard:

- To move through the Bin list: Click any bin in the Bin list sitting left of the Media Pool, or hit Command-1 so the Bin list becomes the Edit page’s active pane, then run the Up and Down Arrow keys to travel through the bins on offer. The Right Arrow key reveals a closed bin, while the Left Arrow key shuts it again.
- To pick a single clip: Hit Command-1 so the Media Pool Bin list takes focus, and use the arrow keys to highlight and open bins. Next press Command-2 to jump into the clip browser area and step from clip to clip with the Arrow keys. With a clip highlighted, any of the edit keyboard shortcuts will cut that Media Pool clip directly into the Timeline that’s currently open.
- To pick several clips: Keep the Shift key held as you tap the Arrow keys, growing or shrinking an unbroken selection inside the Media Pool.
- To pick every clip in the Media Pool: Give the Media Pool focus by clicking a clip or clicking anywhere in its empty background, then press Command-A to take them all.
- To send a highlighted clip or timeline into the Source Viewer: Press the Return key. After a clip lands in the Source Viewer, the transport controls let you play right through it.

### Duplicating Clips in the Media Pool

To make copies of clips within the Media Pool, Option-drag one or several clips into a different bin. You can equally highlight the clip or clips you wish to copy and then choose Edit > Duplicate Clips. Those copies land in the same bin that holds the original media. Each duplicate keeps its own separate link back to the source media stored on disk.

### Viewer Playback and Navigation

Out of the box, the Edit page gives you a classic source/record editing setup. With the Source Viewer you inspect single clips drawn from the Media Pool and ready them for cutting. The Timeline Viewer, by contrast, plays your program back and displays whichever frame the Timeline’s playhead currently sits on.

### Source and Timeline Viewers

### Source and Timeline Viewers vs. Single Viewer Mode

Should you wish to rearrange the Edit page so the Source Viewer disappears, pick Workspace > Single Viewer Mode; one viewer then stands in, showing either a chosen Source Clip or the Timeline’s present frame depending on context.
