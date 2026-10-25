# Focus mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](range-mode-and-multiclip-selection.md) / [Next section](audio-selection-extension-and-track-locks.md)
<a id="source-editing-basics-in-the-fairlight-page-part-2"></a> <a id="source-using-focus-mode"></a>

### Using Focus Mode


Focus mode acts as a Multi Tool built for quick pointer-driven selections and edits, paired with a range of commands — fired off through customizable keyboard shortcuts — for stretching and reshaping those selections. For anyone editing with a mouse and keyboard, the mode aims to keep you moving fast by lighting up assorted functions depending on which part of a Timeline clip you click. One more thing sets Focus mode apart: it alone lets you edit the Timeline mid-playback, something Pointer and Range modes won't allow.

- If no tracks have been selected: Make a selection with the hand and the Timeline In and Out points snap to that selection's edges. Make one with the crosshairs and the Timeline In and Out points snap to the edges of the region you dragged. Either way, whichever tracks hold the selected clips and clip regions get selected too.
- If tracks have been selected: Any clip on a chosen track that crosses the playhead lights up brightly on its own, while clips on de-selected tracks are passed over. Drag the crosshairs across one or more clips with the pointer and you override every automatic selection, grabbing instead the clip regions you drag over along with their tracks.
- If In and Out points have been set: Click the lower half of a Timeline clip to select that clip and its track, and the In and Out points shift to wrap around that clip.

To choose Range mode:

- In the toolbar, click the Range Selection tool — the crosshairs sitting at a track's bottom.
- Choose Trim > Range mode.
- The keyboard shortcut is pressing - R.

To grab a whole clip with Focus mode's Hand tool:

- Bring the pointer to a clip's lower half until the hand cursor shows, then click once to grab that whole clip.

Selecting a clip in Focus mode by clicking its lower half

- With the Hand, Command-click several clips to build either contiguous or noncontiguous selections.
- With the Hand, Shift-click several clips to build contiguous selections.

To grab a range with Focus mode's I-beam cursor:

- Bring the pointer to a clip's upper half until the I-beam cursor shows, then drag to select a region spanning one or more clips. The playhead trails the Out point as you drag.

Selecting a region in Focus mode by dragging across a clip's upper half

- With the crosshairs, Shift-click to widen or narrow the selected region across one or more clips.
- With the crosshairs, double-click to grab a whole clip.
- A partial edit selection holding a fade will copy along with that fade intact.

To grab a single frame with Focus mode's I-beam cursor:

- Bring the pointer to a clip's upper half until the I-beam cursor shows, then click once to drop a point selection on the frame you clicked. The playhead jumps to that frame as well.

Making a single-frame selection by clicking inside a clip's upper half

- With the I-beam cursor, Command-click clips on tracks above and below to fold them into the single-frame selection, all lined up on the same frame — handy, for example, for splitting several clips together. Single-frame selections can sit on tracks that aren't adjacent.

Command-clicking inside the upper halves of several clips across several tracks to drop single-frame selections all on one frame To reposition a selection with Focus mode's Hand tool: With a selection of one or more clips or regions made via the Hand or I-beam cursor of Focus mode, you can bring the pointer to the lower half of any selected clip and drag the whole selection somewhere else on the Timeline.
