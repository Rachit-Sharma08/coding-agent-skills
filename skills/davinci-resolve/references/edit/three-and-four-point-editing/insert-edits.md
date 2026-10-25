# Insert edits

Version: DaVinci Resolve 20.3 Reference Manual. Context: Three and four point editing.
[Chapter index](INDEX.md) / [Previous section](overwrite-edits-overview.md) / [Next section](replace-edits-and-empty-tracks.md)
<a id="source-insert-edits"></a> <a id="source-three-and-four-point-editing-part-2"></a>

### Insert Edits


At the playhead's location, an insert edit divides whatever media already sits in the Timeline, then shoves that media rightward to open space for the incoming clip. The result of an insert edit is that nearly every clip in the Timeline lying to the right of the insert edit point you're making gets rippled, driven farther right by the duration of the incoming source clip. Clips on any Timeline tracks that overlap to the left of the insert edit point, however, aren't rippled and stay put. As an example, if you insert edit a clip into the middle of a run of clips on track V1 and A1 of the Timeline, and a music clip on track A2 also overlaps well to the left of the insert edit point, that music clip holds its spot, while the other clips on track V1 and A1 sitting to the right of your edit point are driven rightward. To insert edit one or more clips into the Timeline: 1 Bring the playhead to the Timeline frame where the clip should be inserted. 2 In the Source Track Selector, click the relevant audio and video destination controls of whichever tracks the incoming source clip should land on. Create new tracks if you need them. 3 If required, use the controls of the Media Pool or the Source Viewer to set In and Out points on the clip or clips you intend to insert edit into the Timeline. 4 Do one of the following:

- In the Media Pool, select one or more clips, right-click any of the selected clips, and pick "Insert Selected Clips to Timeline."
- Pick Edit > Insert, click the Insert Edit button on the toolbar, hit the F9 key, or drag any clip onto the Insert overlay within the Timeline Viewer.

The chosen clips are insert edited onto the selected track at the playhead's location, driving all other media on the destination track back by the chosen clips' combined duration, save for clips sitting on other tracks whose overlap falls to the left of the edit point (illustrated by the overlapping music clip in the example below).

Before and after an insert edit, the Timeline grows longer as the non-overlapping clips to the left of the edit point ripple to the right
