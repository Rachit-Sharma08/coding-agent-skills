# Range mode and range selection by command clicking multiple clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](audio-selection-and-edit-modes.md) / [Next section](focus-mode.md)
<a id="source-range-selection-by-command-clicking-multiple-clips"></a> <a id="source-using-range-mode"></a>

### Using Range Mode

Range mode likewise draws on where the playhead sits to select a partial span of clips on the Timeline when you work through the Fairlight Editing console or keyboard shortcuts. This mode can also team up with the pointer and keyboard shortcuts to make partial clip selections.

- When no tracks are selected: Clips the playhead crosses stay unselected. With the pointer you can click a clip to select all of it plus the track beneath it. You can also drag the pointer across one or more clips to grab a partial span ahead of various editing actions. Each time you select with the pointer, Timeline In and Out points snap to the edges of that selection.
- When tracks are selected: The chosen tracks brighten on the Timeline, and any clip the playhead crosses on a chosen track lights up brighter automatically. Clips on deselected tracks are passed over. Dragging a crosshairs across one or more clips with the pointer

overrides every automatic selection and grabs the regions of the clips you drag across, plus the tracks they belong to.

- When you set In and Out points: On every chosen track, the partial regions of clips sitting between the In and Out points brighten. Clips on unselected tracks are passed over. With In and Out points in place, the playhead stops making automatic selections; in this mode you must lay down new In and Out points to alter the selection. To switch on Range mode:
- Click the Range Selection tool (the crosshairs) on the toolbar.
- Choose Trim > Range mode.
- Press R.

To have the playhead position auto-select clips in Range mode: 1 Press R to drop into Range mode. 2 Select whichever tracks carry the clips you’re after. 3 Move the playhead so it crosses those clips. Every clip the playhead crosses, on the tracks you chose, marks out a selected span running from the start of the first selected clip to the end of the last.

In Range mode, a clip the playhead crosses on a chosen track is picked without any prompting To build your own clip ranges with In and Out points on the Timeline: 1 Press R to drop into Range mode. 2 Select whichever tracks carry the clips you’re after. 3 Move the playhead and tap the I (Mark In) and O (Mark Out) keys to mark out a range on the Timeline.

Each clip segment that lands inside the span of your In and Out points on the chosen tracks gets selected.

Range mode picking out clip segments across chosen tracks by way of In and Out points Ways to select clips in Range mode by clicking and dragging:

- To grab one clip: Click any clip to select both it and its track, and to mark out a Timeline range equal to that clip’s length.

A click grabs one clip together with the track beneath it

- To grab several clips: Command-clicking several clips to take them all at once marks out a Timeline range covering the combined overlapping length of every clip in the selection, from the start of the first selected clip to the end of the last.

### Range selection by Command-clicking multiple clips

- To drag out a range inside one clip: With the Range Selection tool active, drag anywhere across a clip so the bounding box covers whatever segment of that clip (or of one or more clips) you want, selecting both that clip segment and the track it sits on. It’s a handy way to grab part of a recording you mean to move or delete.

Ranged selection within a clip using a bounding box

- To drag out a range across several clips: Click and drag a bounding box across whatever segment of one or more clips you want, selecting both those clip segments and their tracks. Or, Command-click and drag anywhere across any clip so the bounding box spans whatever region of clips and tracks suits you.

Ranged selection across multiple clips using a bounding box Under Range mode, each selection you make refreshes the In and Out point fields with the range you’ve built.

The range fields displaying which In and Out point values pin down the present range Those ranges can be wiped out when needed. Ways to clear In and Out points and so drop the current range:

- Press Option-I to wipe the current In point.
- Press Option-O to wipe the current Out point.
- Press Option-X to wipe both the In and Out points.
