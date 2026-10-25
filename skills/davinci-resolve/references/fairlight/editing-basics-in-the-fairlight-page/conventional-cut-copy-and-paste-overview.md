# Conventional cut copy and paste overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](trim-start-and-trim-end-and-trim-to-selection.md) / [Next section](clip-attributes-and-dialogue-matching.md)
<a id="source-conventional-cut-copy-and-paste"></a> <a id="source-editing-basics-in-the-fairlight-page-part-3"></a>

### Conventional Cut, Copy, and Paste

The familiar cut, copy, and paste commands every application offers are present on the Fairlight page too, but with a distinctive twist that especially rewards users of the Fairlight control surface, or anyone driving the Timeline through the JKL transport-key shortcuts for keyboard-led editing. To cut, or copy, and then paste a clip in whole or in part: 1 For a whole clip, switch to either Selection (press A) or Range Selection (press R) mode. For only part of a clip, be sure you're in Range mode (press R).

2 To build a clip selection with the playhead, first select the track holding the clip you intend to copy or cut. When one or more tracks are already selected, the Control-Option-Up or Down Arrow shortcuts shift the track selection up or down onto the track carrying the clip you're after.

Picking the track that carries the clip you want to cut 3 Take either route: a) For a whole clip, slide the playhead until it crosses the clip you want to cut or copy. Should the playhead cross a clip on a selected track, that clip ought to become selected. Note that even when you click a clip with the mouse before selecting a track, you should still run the playhead across the clip you're copying or pasting, since that establishes a key reference point for the operation. b) For a segment of a clip, slide the playhead until it crosses the clip you want to cut or copy. Should the playhead cross a clip on a selected track, that clip ought to become selected. Then, with JKL plus the I (In) and O (Out) keys, mark out a Timeline range covering the segment you want, and that segment should highlight as a result.

Using In and Out points to cut or copy one segment of a clip

4 With the playhead sitting over the part of the waveform you’ll treat as the frame for moving the clip, press Command-X to cut or Command-C to copy that clip (right-clicking a clip and choosing Copy or Cut works too). The clip lights up right away.

Cutting or copying a clip at the position of the playhead 5 From here, you have two routes for getting the cut or copied clip to the spot in the Timeline where you mean to paste it: a) Moving the playhead now drags the clip you cut or copied along with it, drawn as a ghost clip with waveform “attached” to the playhead at the frame you picked. Whether you drag the playhead with your mouse or work JKL to run the playhead through the Timeline, the cut or copied clip travels in step, so shifting the playhead repositions the cut or copied clip on that track. b) Should you want the cut or copied clip on a different track, lean on the Control-Option-Up or Down Arrow key shortcuts to switch the selected track; the ghost clip follows the change in track selection.

Positioning the cut or copied clip before you paste it

In this way, the playhead lets you line the ghost waveform up against the other audio clips around it ahead of pasting. 6 With the clip sitting where you want it, press Command-V to paste it at the spot you’ve picked (right-clicking a track and choosing Paste from the contextual menu works too). The clip turns solid, and that’s it.
