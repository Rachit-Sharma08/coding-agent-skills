# Deleting keyframes and copying keyframes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing in the color page.
[Chapter index](INDEX.md) / [Previous section](resolvefx-keyframe-tracks-and-sizing-keyframing-tracks.md) / [Next section](keyframes-and-saved-stills-and-adding-edl-marks.md)
<a id="source-copying-keyframes"></a> <a id="source-deleting-keyframes"></a> <a id="source-keyframing-in-the-color-page-part-2"></a>

### Deleting Keyframes

You may remove keyframes one by one, or wipe out every keyframe inside a particular grade in one go. To delete individual keyframes, do one of the following:

- Park the playhead over the keyframe you want gone, then choose Mark > Delete Keyframe (Option-]). Every keyframe sitting at the playhead's position is removed.
- Using the pointer, select a keyframe over in the Keyframe Editor by clicking it; next, right-click on that keyframe and pick Delete Selected Keyframe. Only the keyframe you chose disappears.

To delete every keyframe for the current clip:

- Choose Mark > Delete All Keyframes.

### Copying Keyframes

You can duplicate a batch of keyframes from one node onto another, whether inside the current grade or over in an entirely different clip. Copying a whole grade complete with keyframes from one clip to another is also doable. To copy a set of keyframes from one node to another: 1 Pick a node to copy keyframes from, then choose Edit > Copy (Command-C). 2 Do one of the following:

- If you want every keyframe, pick the node you intend to paste the keyframes and other tweaks into, then go to Edit > Paste (Command-V).
- When your goal is to bring across only the keyframe data from one particular keyframe track, go to Edit > Paste Attributes (Option-V), tick the “Copy Keyframes and Align Using” checkbox, and pick which parameters you want carried over.

TIP: The same approach applies to tracking data you would like to move between nodes, whether inside the current clip or in some other clip entirely. To transfer a full grade along with its keyframes from one clip onto another: 1 In the Thumbnail timeline, click the thumbnail of the clip that should receive the grade. 2 Right-click the thumbnail of the clip you are pulling the grade from, then pick Apply Grade out of the contextual menu. NOTE: As a grade with keyframes moves from one clip onto another, Resolve drops the keyframes onto the frames that line up with the source timecode of the clip they came from. That makes it simple to reuse a keyframed grade on the same clip somewhere else in the Timeline, though the outcome may not be what you want if the destination is a completely unrelated clip.
