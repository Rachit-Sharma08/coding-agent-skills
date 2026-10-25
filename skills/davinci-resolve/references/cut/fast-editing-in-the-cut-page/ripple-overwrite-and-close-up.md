# Ripple overwrite and close up

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](cut-viewer-duration-editing.md) / [Next section](create-subtitles-from-audio-and-source-tape-editing.md)
<a id="source-close-up"></a> <a id="source-copy-paste-and-remove-attributes-from-timeline-clips"></a> <a id="source-overwrite-1"></a> <a id="source-place-on-top"></a> <a id="source-ripple-overwrite-1"></a> <a id="source-source-overwrite"></a> <a id="source-subtitles"></a> <a id="source-subtitles-in-the-cut-timeline"></a>

### Ripple Overwrite

In its plainest form, Ripple Overwrite swaps out a Timeline clip for an incoming one. Apply Ripple Overwrite to a clip on Track 1 and every clip lying to the right of the affected one in the Timeline shifts on its own — forward to open space when the incoming clip is longer, or backward to wipe out gaps when it is shorter.

Carrying out a Ripple Overwrite that replaces a whole clip sitting at the playhead (BB) with the incoming clip (DD)

That said, Ripple Overwrite behaves another way once you have laid In and Out points in the Timeline to mark a range. Then the incoming clip takes the place of whatever stretch of the Timeline lands inside that range, and every other clip to the right of the affected range slides — forward to open space when the incoming clip is longer, or backward to erase gaps when it is shorter.

Carrying out a Ripple Overwrite that swaps an In/ Out range of the Timeline (part of clips BB and CC) for the incoming clip DD

### Close Up

Lets you cut a clip into the Timeline as a zoomed-in close up, compensating for the absence of genuine close ups that would have called for longer lenses or for moving the camera nearer the subject. The function earns its keep especially when, say, 4K media sits in a 1080 timeline, or 8K footage in a 4K timeline; you can then push into existing wide shots to fashion medium shots, or into medium shots to fashion close up shots, all without quality loss. Running this edit brings the incoming clip in scaled to roughly 150% as a close up, runs a face detection too, and, where a face or faces turn up, repositions the face within the frame on its own. The Timeline frame the incoming clip lines up with rests on the following:

- With no In or Out points on the Timeline, the incoming clip takes the Timeline playhead for its In point.
- Where a timeline In point exists, the incoming clip snaps to it.
- Should only a timeline Out point be set, with no In point, the incoming clip’s Out point meets it, which “backtimes” the clip.

(Top) Ahead of a Close Up edit, (Bottom) Once clip DD has been cut into the Timeline via a Close Up edit

### Place On Top

Lets you cut the incoming clip in as a superimposition over whatever else occupies the Timeline; it always rides on top, so when clips already fill tracks 1, 2, and 3, the incoming clip drops onto track 4 by itself, no matter which track happens to be selected. The frame the incoming clip lines up with rests on the following:

- Should the playhead sit close to an edit point (five frames or fewer away), and no timeline In or Out points exist, the incoming clip snaps to the nearest timeline edit point by the playhead (marked by the Smart Indicator).
- Should the playhead be nowhere near an edit point, and no timeline In or Out points exist, the incoming clip snaps to the playhead.
- Where a timeline In point exists, the incoming clip snaps to it.
- Should only a timeline Out point be set, with no In point, the incoming clip’s Out point meets it, which “backtimes” the clip.

(Top) Ahead of placing a clip on top, (Bottom) Once clip DD has been cut into the timeline via a Place On Top edit

### Source Overwrite

For this edit to behave, several clips have to carry overlapping timecode — the situation you get when synced timecode is recorded to multiple cameras on a multi-cam shoot. Where no overlapping timecode exists, the edit accomplishes nothing. When your footage comes from several cameras whose timecode is synced, the simplest path is to lay In and Out points across a Timeline clip at the spot you want to cut away to a different angle. Take this example: a wide shot of a cooking show holds on the instant the chef begins slicing a chili. Marking out a cutaway by laying Timeline In and Out points. From the Media Pool you then choose a clip matching the angle you want as your cutaway, one whose synced timecode overlaps the Timeline clip. Leave In and Out points unset; should any already exist, clear them with Option-X.

Choosing a Media Pool clip from another camera that has overlapping timecode

Press the Source Overwrite button and a synced portion of the chosen Media Pool clip gets cut into the Timeline across the In and Out points you laid, layered over the top. What you get is a flawlessly timed cutaway.

Putting Source Overwrite to work, cutting a layered, synced portion of the source clip onto the Timeline across the In/Out points

As another option, Source Overwrite can on its own drop a source clip bearing a marked In/

Out region over a Timeline clip so its timecode falls in step with the timeline clip’s timecode — handy for those times you are unsure just how much of the incoming source clip belongs in the

Timeline and simply want it synced the right way.

### Overwrite

No button exists for an overwrite edit, yet the F10 key will carry one out, painting the incoming clip over a stretch of the Timeline while leaving every other clip exactly where it is. The frame the incoming clip lines up with rests on the following:

- With no timeline In or Out points defined, the incoming clip snaps to the playhead.
- Where a timeline In point exists, the incoming clip snaps to it.
- Should only a timeline Out point be set, with no

In point, the incoming clip’s Out point meets it, which “backtimes” the clip.

(Top) Beforehand, parking the playhead on the frame you mean to serve as the incoming clip’s In point, (Bottom) Afterward, with the end of clip CC overwritten by incoming clip DD

### Copy, Paste and Remove Attributes from Timeline Clips

On the Cut page timeline you can copy, paste, and strip attributes from clips, much as the Edit page lets you. The way to do it: right-click the timeline clip whose attributes you want to grab and choose copy. Next, pick the timeline clip you mean to change, right-click, and choose Paste Attributes. Up comes a check box menu where you single out exactly which attributes to paste. So, by way of the context menu’s controls, clip attributes can be cut, copied, and pasted from the Cut page timeline.

### Subtitles

### Subtitles in the Cut Timeline

Subtitle support on the Cut page now matches what the Edit page provides, the automatic Create Subtitles from Audio feature included. For a fuller account of how to handle subtitles, turn to Chapter 52, titled “Subtitles and Closed Captioning.” Adding a Subtitle Track to the Cut Timeline goes like this:

- Click on the Timeline Actions icon.
- Select Add Subtitle Track from the drop-down menu.

To free up room for Audio and Video tracks, Subtitle Tracks can be shrunk on the Cut page by clicking the Timeline Options icon and choosing Minimize Subtitle Track.
