# Deleting clips from the timeline and gaps in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Previous section](track-selection-locking-and-destinations.md) / [Next section](audio-video-linking-and-controlling-linked-selection.md)
<a id="source-deleting-clips-from-the-timeline"></a> <a id="source-deleting-multiple-timeline-gaps-at-once"></a> <a id="source-editing-basics-part-3"></a> <a id="source-gaps-in-the-timeline"></a> <a id="source-selecting-a-gap-on-track-v1"></a>

### Deleting Clips From the Timeline

Two routes exist for clearing out clips you no longer want in the Timeline. With the Delete key you can carry out what's often termed a "lift edit," pulling the unwanted clips and leaving behind a gap. With the Forward Delete key you can carry out a "ripple delete," pulling unwanted clips and sealing the gap by rippling whatever remains of the cut Timeline that sits to the right of the removed clip(s) leftward. Deleting clips as a "lift edit" operation:

- To pull one or more clips out of the Timeline while leaving a gap behind: Grab a clip in the Timeline, or Shift-click or Command-click to grab the clips you mean to pull, then press the Delete key (or right-click the selection and choose Delete).
- To pull a stretch of media off several Timeline tracks while leaving a gap behind: Place Timeline In and Out points marking the span of media you mean to clear, then switch off the Destination Track Selector controls for any tracks whose media you want kept, and hit Delete (or right-click the selection, choosing Delete).

Clearing a clip on V1, A1 with the Backspace or Delete key so a gap remains Deleting clips as a "ripple delete" operation:

- To pull one or more clips and seal the gap by rippling the Timeline leftward: Grab a clip in the Timeline, or Shift-click or Command-click to grab the clips you mean to pull, then press the Forward Delete key.
- To pull a stretch of media and seal the gap by rippling the Timeline leftward: Place Timeline In and Out points marking the span of media you mean to clear, then switch off the Sync locks for any tracks whose media you want kept, and press the Forward Delete key.

Clearing a clip with the Forward Delete key so that every clip carrying In points to the right ripples leftward in the Timeline and seals the gap. Observe that tracks A2, A3 don't ripple, since their Sync Locks were switched off in their track headers. Just as in any ripple operation, every clip whose Sync Locks are enabled ripples to seal the gap.

### Gaps in the Timeline

A gap means the empty space sitting between any two clips on a single track. Quite often gaps are what you want, since they let audio or video clips be set apart from each other with precision, but at other times they aren't. Should you need to hunt down stray gaps in your timeline that are too narrow to notice, a couple of commands handle it. To move the playhead to the next gap on the Timeline: 1 Switch off the Destination Track Selector controls for whatever tracks you'd like left out of this operation. 2 Do one of the following:

- Pick Playback > Previous Gap, or hit Option-Command-Semicolon (;), which jumps the playhead leftward to the nearest gap before wherever it currently sits.
- Pick Playback > Next Gap, or hit Option-Command-Apostrophe ('), which jumps the playhead rightward to the nearest gap after wherever it currently sits.

Now and then you'll deliberately want a gap added to the timeline, perhaps as a placeholder holding room for a clip, or to break a stretch into smaller chunks. To insert a gap: 1 Set the playhead at the edit point where you'd like the gap to show up. 2 Select Edit > Insert Gap. 3 As an alternative, right-click an empty stretch of the timeline and pick Insert Gap from the context menu to drop a gap at the playhead's current spot. To select or deselect a gap: One click grabs a gap, and clicking that same gap again drops it. Only a single gap can be grabbed at any one time. The chief reason to grab a gap is to delete it, which ripples the Timeline shut over it in the process. Take the following case, where a gap separates two clips on track V1 that you'd like to seal.

### Selecting a gap on track V1

To delete a gap: Press the Delete key to seal the gap. Every clip to its right on tracks whose Sync Locks are enabled gets rippled leftward to seal the gap. Clips on tracks whose Sync Locks are disabled stay put. Should you grab a gap in a timeline holding clips across several tracks, exactly which clips get deleted hinges on how each track's Sync Lock control is set within the Timeline.

- All tracks with Sync Lock enabled: Whatever range of media crosses the chosen gap gets deleted too. Clips on those tracks ripple leftward to fill the gap.
- All tracks with Sync Lock disabled: Whatever range of media crosses the chosen gap stays whole, and clips on those tracks won't ripple left, drifting out of sync with whichever clips do ripple..

### Deleting Multiple Timeline Gaps at Once

</invoke>

The Edit > Delete Gaps command lets you ripple-delete every video and audio gap throughout the Timeline in a single operation. It clears the gaps sitting between back-to-back clips across all tracks that have Sync Lock turned on. Whenever a portion of the Timeline holds a gap, that portion is rippled so that any clips lying to the right of the gap shift leftward and seal it. For the purposes of this command, a gap counts as an empty stretch between clips that runs across every track in the Timeline. The example that follows shows assorted audio/video, audio-only, and video-only clips separated by gaps. Applying Remove Gaps ripples the Timeline so those clips butt up against each other in one unbroken run, with none overlapping any of the rest.

(Top) Before removing gaps, (Bottom) After removing gaps This command is remarkably potent and far-reaching. That said, a set of firm rules makes it safer by keeping your overall A/V sync intact across timelines:

- A gap won't be closed beyond the spot where video and/or audio clips would begin to overlap each other.
- A gap won't be closed when superimposed video clips sit above it and span across it.
- A gap won't be closed when one or more uninterrupted audio clips span across it.
- By placing In/Out points on the Timeline, you can restrict which gaps get deleted to a chosen range.
- When a linked pairing of video and audio holds a gap containing an L or J split edit, the gap closes

only as far as the point where the audio or video — whichever reaches farthest — meets the closest clip beside it.

- Switching off a track's Sync Lock Control leaves that track out of the calculation for the rules above. That allows gaps on the remaining tracks to close even where clips end up overlapping whatever sits on the Sync Lock disabled track.

WARNING: Running Remove Gaps while one or more tracks have their Sync Locks switched off can throw your video/audio badly out of sync if you aren't cautious. As a safeguard, Shift-click a single video Sync Lock control (or press Option-F9) plus one audio Sync Lock control (or press Command-Option-F9) to flip every video and every audio Sync Lock control on together in one move.
