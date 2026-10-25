# Rules of three point editing and editing rules for split in and out points

Version: DaVinci Resolve 20.3 Reference Manual. Context: Three and four point editing.
[Chapter index](INDEX.md) / [Previous section](timeline-in-out-points-and-clip-marking.md) / [Next section](overwrite-edits-overview.md)
<a id="source-backtiming-a-source-clip-when-editing-into-the-timeline"></a> <a id="source-different-types-of-three-and-fourpoint-edits"></a> <a id="source-editing-a-specific-range-of-the-source-clip-into-the-timeline"></a> <a id="source-editing-part-of-a-source-clip-to-fit-into-a-specific-range-of-the-timeline"></a> <a id="source-editing-rules-for-split-in-and-out-points"></a> <a id="source-switch-focus-to-timeline-after-edit"></a> <a id="source-the-rules-of-three-point-editing"></a>

### The Rules of Three-Point Editing

In the cases above, three-point editing worked because source In and Out points bounded the portion of the source clip headed for the Timeline while the Timeline playhead stood in as the acting Timeline In point; those three points pinned down the edit. Yet threepoint editing earns its keep just as much when you have to overwrite stretches of an already-cut timeline with fresh source clips in a measured way, for instance dropping an insert shot into a scene to mask a change that would otherwise break continuity. Which rules apply hinges on the mix of Source and Timeline In and Out points you've set:

- If there is no In point in the source clip: media's opening frame stands in as the acting source In point. A thick bar reaching left of the Out point in the Source Viewer's jog bar signals this.

A thick bar marks the portion of the source clip drawn upon when no Source In point exists

- If there is no Out point in the source clip: media's closing frame serves as the acting source Out point. A thick bar reaching right of the In point in the Source Viewer's jog bar signals this.

A thick bar marks the portion of the source clip drawn upon when no Source Out point exists

- With neither an In nor an Out point on the Timeline: the playhead serves as the acting Timeline In point.
- Given a Timeline In point yet no matching Out point on the Timeline: the entire span between the source clip's In and Out points goes into the Timeline with the Source In point lined up against the Timeline In point. A thick bar reaching right of the In point in the Timeline Ruler signals this.

A thick bar marks where the Source clip lands once no Timeline Out point is present

- Given a Timeline Out point yet no matching In point on the Timeline: the incoming source clip gets backtimed so its Out point lines up with the Timeline Out point. A thick bar reaching left of the Out point in the Timeline Ruler signals this.

A thick bar flags a backtimed edit whenever no Timeline In point is present

- Given both Timeline In and Out points plus a Source Out point alone: here too the incoming source clip is backtimed so its Out point meets the Timeline Out point, while the Timeline edit points fix how much of the source clip is used.
- Given the full set of Source In and Out plus Timeline In and Out edit points: the Timeline edit points govern how much source clip enters the Timeline, and the frame sitting at the Source In point meets the Timeline In point, except when you run a Fit to Fill or ripple overwrite edit, each of which can operate as a four-point edit.

TIP: When all four Source and Timeline edit points are in play to retime a source clip into a chosen Timeline range, reach for a Fit to Fill edit rather than an overwrite edit.

### Editing Rules for Split In and Out Points

Whenever split In and Out points exist in the Source Viewer or Timeline, these rules take effect:

- If the Source Viewer has split In and Out Points: when the clip is cut in, its leftmost split point — be it video or audio — meets the playhead, and the remaining split point sits offset to the right.
- If the Timeline has split In and Out Points: the incoming clip's In point meets the leftmost split point, whether that's video or audio, while the partner audio or video In point lands offset at the split point to its right.

### Editing a Specific Range of the Source Clip Into the Timeline

What follows are a few everyday three-point editing scenarios for cutting into the middle of an already-assembled timeline. In this first one, you've got a defined span of source media to place on the Timeline and aren't fussed about whatever the incoming clip overwrites there. 1 Mark In and Out points on a source clip, working from the Media Pool or the Source Viewer.

Placing In and Out points on the source clip

2 To establish the landing spot for the incoming clip, aim the destination control at the tracks you mean to edit onto, then take one of these steps:

- Park the Timeline playhead on whichever frame should act as the edit's Timeline In point.
- Mark a Timeline In point for the edit.

Letting the playhead stand in for a Timeline In point 3 To carry out the edit, hit the Overwrite Clip button on the toolbar, press F10, or drop a clip onto the matching overlay in the Timeline Viewer.

The finished edit; how long the source clip runs sets how long the edit runs

### Editing Part of a Source Clip to Fit Into a Specific Range of the Timeline

Here you've got a portion of a clip, or a gap within the cut sequence on the Timeline, that should soak up however much of the present source clip it takes to "plug the hole." 1 If needed, mark an In point on the source clip to fix the first frame of source media bound for the Timeline. Marking only a source clip In point 2 Place In and Out points on the Timeline to pin down both the incoming clip's landing spot and how much of it gets used.

Marking both Timeline In and Out points to bound a gap 3 To carry out the edit, hit the Overwrite Clip button on the toolbar, press F10, or drop a clip onto the matching overlay in the Timeline Viewer.

The finished edit; the span between the Timeline edit points decides how much source clip gets used

### Backtiming a Source Clip When Editing Into the Timeline

For this final scenario, a particular beat in the latter half of a source clip has to meet a Timeline Out point so that the clip's leftover length overwrites the cut sequence working from right to left. Lining a Source Out point up with a Timeline Out point to make an edit goes by the name backtiming, and there are two ways to arrange it. Backtiming method one: 1 Mark In and Out points on the source clip, from either the Media Pool or the Source Viewer. 2 Mark an Out point on the Timeline at the frame where the incoming source clip's matching Out point should line up.

Building a backtimed match-on-action edit from In and Out points in the Source Viewer plus a lone Out point on the Timeline 3 To carry out the edit, hit the Overwrite Clip button on the toolbar, press F10, or drop a clip onto the overwrite overlay in the Timeline Viewer.

The finished edit, with the source clip's Out point matched to the Timeline's Out point

Backtiming method two: 1 Mark an Out point on the source clip, from either the Media Pool or the Source Viewer. 2 Place In and Out points on the Timeline to pin down both the incoming clip's landing spot and how much of it gets used.

Building a backtimed edit by marking an Out point in the Source Viewer alongside In and Out points on the Timeline that set the edit's length 3 To carry out the edit, hit the Overwrite Clip button on the toolbar, press F10, or drop a clip onto the matching overlay in the Timeline Viewer.

The completed edit, where the source clip's Out point sits flush against the Timeline's Out point

### Switch Focus to Timeline After Edit

Found in the Edit menu, the “Switch focus to timeline after edit” option (Option-Shift-Q) governs whether DaVinci Resolve hands application focus from the Source Viewer over to the Timeline Viewer/ Timeline each time you cut an edit. It ships turned on. Suppose you're pulling clips out of many different source files into the Timeline and trimming as you go — keeping this on can save time, since focus hops from the Source Viewer to the Timeline after each edit, letting you grab the clip or edit point you want to trim, make adjustments, and only then load the next clip into the Source Viewer for the following edit. Conversely, when you're cutting several pieces out of one long interview clip, you might switch it off so you can keep playing forward in the Source Viewer, dropping In and Out points and sending clips to the Timeline as you go. With it off, focus stays put on the Source Viewer after each edit, so you carry on editing from the same source clip without a break.

### Different Types of Three‑ and Four‑Point Edits

What follows runs through the various edit types on offer for dropping source clips into whichever Timeline is currently open.
