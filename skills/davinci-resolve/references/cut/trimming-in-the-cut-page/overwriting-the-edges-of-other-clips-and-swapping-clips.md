# Overwriting the edges of other clips and swapping clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming in the cut page.
[Chapter index](INDEX.md) / [Previous section](cut-timeline-markers-and-selection.md) / [Next section](resize-clips-while-rippling-the-timeline-and-rolling-an-edit.md)
<a id="source-a-disabled-clip-in-the-timeline"></a> <a id="source-a-muted-clip-in-the-timeline"></a> <a id="source-copy-cut-and-paste"></a> <a id="source-deleting-clips"></a> <a id="source-deleting-parts-of-clips"></a> <a id="source-disabling-and-deleting-clips"></a> <a id="source-disabling-and-muting-clips"></a> <a id="source-disabling-clips"></a> <a id="source-muting-clips"></a> <a id="source-overwriting-the-edges-of-other-clips"></a> <a id="source-selecting-clip-dd-to-delete-it"></a> <a id="source-splitting-clips"></a> <a id="source-swapping-clips"></a> <a id="source-trimming-clips"></a>

### Overwriting The Edges of Other Clips

Drag a clip in the Timeline or Upper Timeline onto a neighboring clip's edge without letting your pointer overlap it, then drop the clip. The overlapped piece of that neighboring clip gets overwritten.

Dragging clip CC so it partly overlaps clip DD, with the goal of overwriting it

Once clip CC has been dropped to partly overwrite clip DD's start, clip DD becomes shorter and the Timeline's remaining clips shift left to seal the gap in Track 1

### Swapping Clips

Drag one or more clips from one spot in the Timeline or Upper Timeline to another so the pointer lands on an edit between two clips (the edit point goes purple), then drop. The clip(s) you dragged are now relocated and slotted in at the edit point you aimed for.

(Top) Dragging clip CC so as to swap it in between clip II and JJ. (Bottom) Once clip CC is dropped, the Timeline reorganizes, sealing every gap and pushing clips rightward as needed; superimposed clips stay synced to the Track 1 clips that shifted

### Copy, Cut, and Paste

Just as you'd handle words in a word processor, clips can be cut, copied, and pasted within the timeline or Upper Timeline to duplicate or relocate them. To cut/copy and paste in the Timeline: 1 Pick one or more clips in the Timeline. 2 Do one of these: a) Hit Command-C to copy them (the chosen clips stay put). b) Hit Command-X to cut them (the chosen clips vanish and the Timeline auto-ripples to seal the gap). c) Move elsewhere in the Timeline, then hit Command-V to paste. The clips land at the playhead frame, on the same track they came from, overwriting whatever clips already sit at that point in the Timeline.

### Splitting Clips

Any clip can be split into two pieces — effectively dropping an edit point at the midpoint — to set up moving one section of a clip, removing one section, slotting another clip in at that edit point, or putting some effect on a single section of a clip rather than the rest.

To split a clip: 1 Park the playhead on the clip frame where the split should occur. 2 Do one of these:

- Click the Edit Actions icon and pick split from the drop-down menu.
- Right-click the playhead's top handle and click the Split button that shows on

the radial menu.

- Press Command-Backslash.
- Click the Split Clips (scissor) icon at the far left of the Cut page Edit commands.

(Left) A clip prior to splitting, (Right) Afterward, a fresh edit point divides it into a pair of pieces

### Disabling and Deleting Clips

Clips you no longer need can be either disabled or deleted.

### Disabling and Muting Clips

You can switch off a Timeline clip's audio and/or video without removing the clip itself. This comes in handy when you want to use a clip's audio or video selectively, or when you'd like to disable both the audio and video of a clip you don't intend to use without removing it from the Timeline entirely in case you reconsider.

### Disabling Clips

Switch off a clip's video while keeping it in the Timeline by selecting it and pressing D, or by right-clicking it and clearing Enable on the contextual menu. The clip goes dull to signal it's disabled. Its audio keeps playing unless you mute it too.

### A disabled clip in the Timeline

### Muting Clips

Switch off a clip's audio while keeping it in the Timeline by right-clicking it and picking Mute on the contextual menu. A mute icon overlays the clip's start to signal the audio is off. Its video keeps playing unless you disable it too.

### A muted clip in the Timeline

### Deleting Clips

When you want one or more clips gone from the Timeline entirely, pick them and hit the Delete key. The clip(s) disappear. Delete a clip on Track 1 and the Timeline ripples to close the gap on its own.

### Selecting clip DD to delete it

Removing clip DD sends clips EE through NN sliding left to seal the Track 1 gap; superimposed clips travel along to stay synced with whatever sits beneath them

### Deleting Parts of Clips

To remove only part of one or more clips, place In and Out points around the Timeline section you want gone, then hit the Delete key. The stretch of Timeline between the In and Out points is removed. Delete part of a clip on Track 1 and the Timeline ripples to close the gap on its own.

Setting In and Out points to remove that stretch of the Timeline Once everything between the In and Out points is gone, every clip sitting right of the marked stretch slides left to seal the Track 1 gap

### Trimming Clips

You can also reshape your edited timeline in a hurry by resizing any clip's In and Out points, shifting the edit points between clips, and slipping a clip's contents.
