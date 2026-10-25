# Setting in and out points in the timeline and mark clip and mark current selection

Version: DaVinci Resolve 20.3 Reference Manual. Context: Three and four point editing.
[Chapter index](INDEX.md) / [Previous section](three-point-editing-keyboard-shortcuts.md) / [Next section](three-point-and-split-edit-rules.md)
<a id="source-dragging-preview-marks-to-change-an-edit"></a> <a id="source-mark-clip-and-mark-current-selection"></a> <a id="source-preview-marks-during-threepoint-editing"></a> <a id="source-setting-in-and-out-points-in-the-timeline"></a>

### Setting In and Out Points in the Timeline

Much of the time, preparing a Timeline edit takes nothing more than parking the Timeline playhead on the frame where the incoming source clip should land. When no In or Out points exist, the playhead stands in as the In point. That said, marking specific In and Out points to carve out particular Timeline ranges opens the door to other kinds of edits. Ways to set and remove In and Out points in the Timeline:

- To set an In or Out point: give focus to the Timeline or Timeline Viewer with a click or the Q key, position the playhead using the transport controls, jog bar, or control panel buttons, then tap the I key for an In point or the O key for an Out point.
- To clear In or Out points: while the Timeline Viewer holds focus, hit Option-I to drop the current In point or Option-O to drop the current Out point.
- To clear both the In and Out points together: press Option-X.

In and Out points displayed on the Timeline, with the unmarked stretches beyond the selection dimmed Ways to move In and Out points in the Timeline:

- Reposition the playhead, then tap the I or O keys so the In or Out point jumps to wherever the playhead now sits.
- Drag an In or Out point along the Timeline ruler to shift it elsewhere.

Everything on the Timeline beyond the span your In and Out points currently bracket appears dimmed, drawing your eye to the stretch the next edit is going to touch.

When you want the playhead sitting on an In or Out point before tweaking something:

- Tap Shift-I to send the playhead straight to the current In point, or Shift-O to send it to the current Out point.

Even with Preview Marks switched off, the Go to In and Go to Out commands can drop the playhead onto the implicit (yet unmarked) In and Out points that a three point edit in progress implies. Say you mark In and Out points on the Timeline, then give a Source Viewer clip its own In point: a press of Shift-O (Go to Out) sends the Source Viewer playhead to the very frame that would become that clip's Out point if you ran the edit.

A three point edit comes together once In and Out points sit on the Timeline alongside an In point placed in the Source Viewer.

Relying on Go to Out to send the Source Viewer playhead onto the implicit Out point that a three point edit establishes

### Mark Clip and Mark Current Selection

Both of these commands lay down Timeline In and Out points at the same time automatically, borrowing the timing of clips already present. They shine when you need to bound an incoming edit against a clip on the Timeline that you mean to swap out, or a gap you intend to close. Put simply, Mark Clip reads the opening and closing frames of a target clip or gap on the Timeline and sets the editing In and Out points from them. So if a shot in your cut needs replacing with an alternate take of the same action, or a gap among your clips begs to be filled fast with B-roll, Mark Clip gets you there. Mark Current Selection instead takes the opening and closing frames across a span of selected clips to lay down the Timeline In and Out points. It fits nicely when a run of clips on the Timeline should all give way to one incoming source clip.

To use Mark Clip: 1 Slide the playhead so it crosses either the clip whose In and Out points you want, or the gap (empty stretch) between two clips you mean to target. Any frame of that clip will do for the playhead's location.

Parking the playhead over a clip you intend to mark 2 Should other clips on a multi-track timeline sit over the one you're aiming at, the clip riding the lowest video track becomes the target for setting the In and Out points. To target a clip on a higher track instead, either switch off the Auto Selection controls of every track beneath it, or Option-click the Auto Selection control of the targeted clip's track to solo it, which forces that track to serve as the target. 3 Hit the X key and the In and Out points snap automatically to the opening and closing frames of the target clip.

Applying Mark Clip so the In and Out points line up with a clip's length TIP: Pressing Option-X wipes both In and Out points and acts as the reverse of this command.

To use Mark Selection: 1 Pick one or several clips on the Timeline.

Choosing the clips whose span will mark the In and Out points 2 Tap Shift-A and the In and Out points jump automatically to the opening and closing frames of your selection. Whether the selected clips run continuously or have gaps between them, the outcome is identical.

Marking a selection so the In and Out points are set TIP: Mark Selection works on Timeline gaps as well.

### Preview Marks During Three‑Point Editing

So you can preview the outcome of a three-point edit before committing, preview marks show up in either the Source Viewer or the Timeline Ruler to report exactly how much Timeline the pending edit will touch. To keep them from getting in your way, they surface only after you've deliberately placed three edit points across the Source Viewer and Timeline, and you can toggle them with View > Show Preview Marks.

As an illustration, place In and Out points in the Source Viewer plus an In point on the Timeline, and a preview marker surfaces in the Timeline Ruler to reveal where the pending edit's implied Timeline Out point falls.

A preview marker on the Timeline reflects the Timeline Out point that DaVinci Resolve works out on its own from the Viewer's In and Out points together with the Timeline In point Conversely, when you place both In and Out points on the Timeline but only an Out point in the Source Viewer, a preview marker turns up in the Source Viewer's jog bar to point out the pending edit's implied In point there.

A preview marker in the Source Viewer reflects the Source Viewer In point that DaVinci Resolve derives on its own from the Timeline's In and Out points along with the Source Viewer In point When convenient, jump the playhead onto the preview mark with Shift-I for an In point or Shift-O for an Out point.

### Dragging Preview Marks to Change an Edit

Dragging a preview mark reshapes the edit you're about to commit. As you drag one, the matching In or Out point on the side opposite the focused Viewer shifts to suit the revised three-point edit. Picture an In point in the Source Viewer with In and Out points on the Timeline: a preview mark shows up in the Source Viewer indicating the Out point that will cut the Source Viewer clip into the Timeline. Drag that preview mark leftward in the Source Viewer and the Timeline Out point travels right along with it, because you're retiming the edit.

Pulling a preview mark within the Source Viewer reshapes the matching edit point over on the Timeline
