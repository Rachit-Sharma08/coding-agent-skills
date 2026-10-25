# Keyboard shortcuts in this chapter and moving resizing and rolling clips in selection mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips in the timeline.
[Chapter index](INDEX.md) / [Next section](clip-duration-timecode-and-source-trimming.md)
<a id="source-for-more-information-see-chapter-44-trimming"></a> <a id="source-keyboard-shortcuts-in-this-chapter"></a> <a id="source-modifying-clips-in-the-timeline"></a> <a id="source-modifying-clips-in-the-timeline-part-1"></a> <a id="source-moving-resizing-and-rolling-clips-in-selection-mode"></a> <a id="source-trimming-gaps"></a>

### Modifying Clips in the Timeline

After a mix of clips has been assembled into the Timeline, the next phase is reworking them while you polish the cut. This chapter walks through straightforward ways to alter clips: changing their size, cutting them apart, reshuffling their order, switching them off, duplicating, and using copy and paste.

### Keyboard Shortcuts in This Chapter

Below is a set of keyboard shortcuts tied to the subjects covered here that may prove useful.

| Key Shortcut                     | Function                                                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| A                                | Selection tool/mode                                                                                                        |
| V                                | Grab the edit closest to the playhead                                                                                      |
| Shift-V                          | Grab the clip that the playhead is over                                                                                    |
| U                                | Grab the incoming, outgoing, or middle portion of an edit                                                                  |
| Option-U                         | Cycle the selection through video+audio, video alone, and audio alone                                                      |
| Up, Down Arrow Keys              | Shift the selection to the prior/following edit or clip                                                                    |
| Comma, Period                    | “Nudge” keys that shift a chosen edit or clip one frame to either side                                                     |
| Shift-Comma, Period              | “Fast Nudge” keys that shift a chosen edit or clip 5 frames to either side (customizable)                                  |
| Shift-Left, Right Bracket ([, ]) | Trim Start to Playhead and Trim End to Playhead, which crop a clip where the playhead sits                                 |
| E                                | Extend edit, which pulls a chosen edit point over to the playhead                                                          |
| B                                | Razor blade tool that drops cuts onto clips with the pointer                                                               |
| Command-Backslash (\)            | Insert edit; drops a cut into the clip(s) wherever the playhead is positioned                                              |
| Delete                           | Delete a clip while keeping the gap (lift edit)                                                                            |
| Forward Delete                   | Ripple delete; removes a clip and pulls everything to its right leftward to close the gap                                  |
| N                                | Switch timeline snapping on or off                                                                                         |
| Command-Shift-L                  | Switch linked selection on or off                                                                                          |
| Command-D                        | Change clip duration                                                                                                       |
| Command-Shift (modifier)         | Holding Command-Shift during a drag lets you “shuffle” or “swap” clips forward or backward to reorder them in the Timeline |
| D                                | Disable/Enable the chosen clips                                                                                            |
| Command-X                        | Cut the chosen clips while keeping a gap                                                                                   |
| Command-Shift-X                  | Ripple cut the selection; seal the gap the cut clip(s) leave behind                                                        |
| Command-C                        | Copy the chosen clips                                                                                                      |
| Command-V                        | Paste clips                                                                                                                |
| Command-Shift-V                  | Paste insert clips                                                                                                         |

### Moving, Resizing, and Rolling Clips in Selection Mode

Once you’ve dropped a run of clips into a timeline, even the most meticulous editor will soon need to begin adjusting things. The easiest of those adjustments happen in Selection Mode with the ordinary arrow pointer.

The Selection Mode button on the left is active, while the Trim mode button on the right is off. This is the mode you land in by default whenever DaVinci Resolve opens, and it lets you relocate clips elsewhere in the Timeline, stretch or shrink their length, and roll the edit points sitting between a pair of clips so the edit lands earlier or later on the Timeline. Exactly what this tool accomplishes hinges entirely on whatever you click to select while you work. Handling clips with the mouse: 1 Click the Selection Mode tool (the arrow), or hit A. 2 Carry out one of these: To relocate clips in the Timeline: Drag any clip somewhere else in the Timeline. Should you drag a clip so it overlaps another, the clip in your hand writes over the one you drop it on top of.

Dragging a clip across the Timeline to write over part of a neighbor; a tooltip reports the frame count you’ve shifted To shift clips up or down onto other tracks in the Timeline while holding their timing steady: Keep the Shift key pressed as you drag clips up or down through the Timeline. Alternatively, press and hold Option and tap the Up or Down Arrow.

Sending a clip onto a different track without nudging its timing by keeping Shift pressed To trim or extend clips: Hover the Selection Mode pointer over a clip’s start or finish, and once it becomes the Resize cursor, drag the In or Out point either way to alter the clip’s length. While you do this, the audio scrubs together with the Resize cursor.

Shrinking a clip in the Timeline so a gap opens up; a tooltip reports the offset, while outlines reveal how much media remains in the clip you’re tweaking To roll any edit: Hover the Selection Mode pointer over any edit point, and once it becomes the Roll Edit cursor, drag it either way to relocate the edit point while at the same time reshaping the outgoing and incoming edit points of the two clips on each side. While you do this, the audio scrubs along with the In point of the clip on the right.

Rolling an edit; a tooltip reports the offset, while an outline marks the range within which rolling is possible

Handling clips with the keyboard: 1 Hit A to switch into Selection Mode. 2 Carry out one of these:

- To roll any edit step by step: Grab the edit point nearest the playhead with the V key, shifting the selection onto a different edit when needed via the Up Arrow and Down Arrow keys. After that, press Comma to shift it a single frame leftward, or Period to shift it one frame the other way, rolling the chosen edit. Add Shift to either key (Shift-Comma, Shift-Period) and the jump becomes 5 frames.
- To roll any edit with the playhead: Grab the edit point nearest the playhead with the V key, shifting the selection onto a different edit when needed via the Up Arrow and Down Arrow keys. After that, drive the playhead with the JKL keys to whichever frame you want the edit moved to, then hit E for an “extend” edit.
- To trim or extend clips step by step: Grab the edit point nearest the playhead with the V key, then flip the selection between the tail of the outgoing clip and the head of the incoming one using the U key. Next, press Comma to pull that side a single frame leftward, or Period to push it one frame the opposite way, trimming or extending it. Shift one end of a clip far enough to overlap a neighbor and the clip in motion writes over the one beside it. Holding Shift with either key (Shift-Comma, Shift-Period) moves 5 frames at a go. Under Selection mode, this either opens a gap or overwrites the adjacent clips.
- To trim clips with the playhead: Drive the playhead via the JKL keys onto the frame in the Timeline where you’d like a fresh In or Out point for that clip, then hit Shift-Left Bracket ([) for “trim start,” or Shift-Right Bracket (]) for “trim end.” You don’t need a selection. Under Selection mode, this opens a gap.
- To extend clips with the playhead: Grab the edit point nearest the playhead with the V key, then flip the selection between the tail of the outgoing clip and the head of the incoming one using the U key. Next, drive the playhead via the JKL keys to the frame you’d like that edit point pushed out to, then hit E for an “extend” edit. Under Selection mode, this overwrites the adjacent clips.
- To shift clips earlier or later in the Timeline: To pick a clip ahead of moving it, either click it, or run the Spacebar or JKL keys to park the playhead over it and hit Shift-V. After that, press Comma to slide the clip a single frame leftward, or Period to slide it one frame the other direction. Move a clip far enough to overlap another and the clip in motion writes over the one beside it. With Shift held, either key (Shift-Comma, Shift-Period) jumps 5 frames. Under Selection mode, this opens a gap.
- To shift clips up or down onto other tracks: To pick a clip ahead of moving it, either click it, or run the Spacebar or JKL keys to park the playhead over it and hit Shift-V. After that, press Option-Up Arrow to send that clip’s Video and Audio onto the next higher‑numbered track, or Option-Down Arrow to send the Video and Audio onto the next lower‑numbered track.

TIP: Keep Shift pressed as you nudge a selection to perform a “fast nudge.” How far a fast nudge travels can be set in the Editing panel of the User Preferences. The default sits at five frames, though you’re free to dial in any value.

### Trimming Gaps

Where a gap begins and ends can likewise be rippled with the Trim tool.

### For more information, see Chapter 44, “Trimming.”

Employing the Trim tool to ripple a gap’s Out point so it shrinks
