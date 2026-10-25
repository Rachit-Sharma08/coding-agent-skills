# A disabled clip on track v2 and copying and pasting clips in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](clip-duration-timecode-and-source-trimming.md) / [Next section](audio-channel-pasting-and-auto-alignment.md)
<a id="source-a-disabled-clip-oµn-track-v2"></a> <a id="source-copying-and-pasting-clips-in-the-timeline"></a> <a id="source-copying-and-pasting-clips-to-a-different-track"></a> <a id="source-cutcopypaste-of-partial-clip-segments-using-in-and-out-points"></a> <a id="source-modifying-clips-in-the-timeline-part-2"></a> <a id="source-paste-insert"></a>

### A disabled clip oµn track V2

For a different case, suppose you’ve cut a run of titles onto track V3 and now must switch off the whole of track V3 to deliver a textless version of the film. Once a clip or track is switched off, the clips inside it look dimmed, those disabled clips stay out of the Color page, and they won’t go out to tape or render to disk in the Deliver page until that track is switched back on first.

Track V3 has been switched off, which renders the Timeline textless To switch one or more clips on or off in the Timeline:

- Pick one or more clips, then right-click the selection and tick or untick Enable Clip in the contextual menu, or hit D to flip a clip’s enabled state.

To switch a whole track on or off:

- Click the track enable button.

Over in the Edit page, a number of the Track Header controls — among them Auto Track Selection, Visibility, and Lock Track — can all be set in one pass: click an icon and drag the pointer up or down across the track headers. The catch is that only a single kind of control responds at a time, and the sweep won’t cross between Audio and Video tracks.

Click the Lock icon on A1 and then drag the pointer down to A3, and every audio track in that span gets locked.

### Copying and Pasting Clips in the Timeline

There are numerous ways to cut, copy, and paste clips through the usual keyboard shortcuts. Cutting or copying can act on a single clip or a group of several, and you’re also free to copy or cut only the video or only the audio media of a clip. When it’s time to paste, you can drop the result into the same timeline, or into a different one if your goal is to move media across timelines. Ways to perform a basic cut, copy, and paste:

- To cut one or more clips and leave a gap behind: Build a selection, then go to Edit > Cut (Command-X). The chosen clip or clips disappear from the Timeline and sit in memory ready for pasting.
- To ripple cut one or more clips and ripple the Timeline shut over the gap: Build a selection, then go to Edit > Ripple Cut (Command-Shift-X). The chosen clip or clips leave the Timeline and wait in memory for pasting. Every clip on a track with Auto Select on ripples leftward to seal the gap the cut clips leave.
- To copy one or more clips: Build a selection, then go to Edit > Copy (Command-C). The chosen clip or clips remain in the Timeline while copies are held in memory for pasting.
- To paste one or more clips back onto the same track: Park the playhead at the frame where the pasted selection should begin, then go to Edit > Paste (Command-V). By default each copied clip lands on the very track it came from.
- The pasted clips appear wherever the Playhead sits.
- The pasted clips write over whatever clips on that track stand in their path.
- The pasted clips arrive already selected, set for nudging in either direction or for whatever else you need.
- To paste one or more clips onto a different track: Sending clips to another track calls for a slightly altered approach. Park the playhead at the frame where the pasted selection should begin, then either Option-click any vacant spot on the destination track or Option-click that track’s Auto Select control to solo it, and afterward go to Edit > Paste (Command-V).
- The pasted clips appear wherever the Playhead sits.
- The pasted clips write over whatever clips on that track stand in their path.
- Once dropped, the pasted clips come up pre-selected, primed for nudging side to side or any further operation.

### Paste Insert

There’s a second paste command, Edit > Paste Insert (Command-Shift-V), which drops clips you cut or copied in as an insert edit, adding an edit at the playhead among the clips already sitting in the Timeline, while everything to the right of the playhead ripples even farther right to clear space for the clip or clips coming in. Just like every other ripple edit, this touches only the clips on tracks whose Auto Select control is switched on. The pasted clips arrive already selected, set for nudging in either direction or for whatever else you need.

### Cut/Copy/Paste of Partial Clip Segments Using In and Out Points

As a default, pasted clips drop in at the playhead position. The Timeline’s In and Out points give you several ways to cut and copy just part of a longer clip. It’s an invaluable trick for detailed audio and dialog work, though it serves equally well for copying partial chunks of any clip in the Timeline. IMPORTANT: Before In and Out points will work for pasting, you have to head to Preferences > User > Editing first and tick the box “Prioritize pasting to the in and out range.”

To cut or copy a portion of a clip for pasting somewhere else: 1 Place In and Out points to fence off the part of the clip you mean to cut or copy. While doing so, the Auto Select controls let you take in or leave out clip segments on particular tracks. 2 For that clip segment, press Command-X if you’re cutting it, or Command-C if you’re copying. 3 Wipe the In and Out points with Option-X. If you skip this, the segment will simply paste straight back where it began. 4 Park the playhead on the Timeline frame where the pasted clip should start, then run the Paste or Paste Insert commands to drop the segment there. Once positioned, the pasted clips come up pre-selected, primed for nudging side to side or any further operation. In and Out points can likewise let you paste only a slice of a far longer clip you’ve cut or copied. To paste just a part of a clip: 1 Pick a clip and hit Command-X to cut or Command-C to copy it. 2 Place In and Out points to mark out the Timeline region you intend to paste into. 3 Run the Paste or Paste Insert commands to lay down only as much of the Cut or Copied clip as fits between the In and Out points you set. Once positioned, the pasted clips come up pre-selected, primed for nudging side to side or any further operation.

### Copying and Pasting Clips to a Different Track

When every track has its Auto Select control switched on, clips always return to the same track they were copied from, beginning at the playhead’s spot. That’s handy in the many cases where you keep copying and pasting clips you want repeated, particularly during audio editing. But if your aim is to paste the cut or copied clips onto an entirely different track, you’ll need the Auto Select controls to designate which track receives them. The rules go as follows:

- To force what you copied onto one particular track, Option-click that track’s Auto Select control so it’s soloed before you paste.
- With one or more Auto Select controls switched off, clips land on the lowestnumbered track whose Auto Select control is on.
- Where you’ve copied clips spanning several tracks, whatever sat on the lowest copied track goes to the lowest Auto Select enabled track, while the rest move to higher tracks, fresh ones being made automatically when needed.
- Should Auto Select be off on every track without exception, a new track is built above all the other video tracks and/or beneath all the other audio tracks, and the clip drops into that new track, where Auto Select is on.
