# Append to end and insert selected clips to timeline using timecode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Three and four point editing.
[Chapter index](INDEX.md) / [Previous section](replace-edits-and-empty-tracks.md) / [Next section](media-pool-to-timeline-assembly-example.md)
<a id="source-append-to-end"></a> <a id="source-insert-selected-clips-to-timeline-using-timecode"></a> <a id="source-insert-selected-clips-to-timeline-with-handles"></a> <a id="source-three-point-editing-from-the-media-pool"></a>

### Append to End

With append to end, the edited clip lands every time at the tail of the current Timeline. As an edit type it's tremendously handy while you rapidly chain a series of clips together. To apply append to end when editing a clip into the Timeline: 1 Lay In and Out points on a source clip you'd like tacked onto the end of the current Timeline. Where required, reorder the Media Pool's sort so these clips fall into the sequence you want them joined to the Timeline. 2 In the Source Track Selector, click the audio and video destination controls for whatever tracks the incoming source clip should sit on. Build new tracks if you require them. 3 Pick Edit > Append to End of Timeline; alternatively drag the clip to the Timeline Viewer's Append at end overlay, or hit Shift-F12. Incoming video clips join in directly past the very tail of the Timeline's last clip.

### Insert Selected Clips to Timeline Using Timecode

Clips can be edited straight from the Media Pool into a timeline so that each clip's source timecode lines up with a matching record timecode value in the Timeline. This is handy for long form multi-camera events, weddings or concerts say, where each camera runs the same timecode so every edit stays flawlessly synced. The Source Overwrite edit on the Cut page is what this function corresponds to. IMPORTANT: This edit only works where the Timeline's timecode overlaps the clip(s)' timecode. That gets set within the Start Timecode field of the New Timeline settings.

To insert selected clips to timeline using timecode: 1 In the Media Pool, select one or more clips to edit into the Timeline. If In and Out points are set on the clip, the edit respects those bounds. If no In/Out points are set, each selected clip gets edited in full. 2 Set a destination control to settle which Timeline track gets edited to. 3 Right-click any one of the selected clips and, off the drop-down menu, pick "Insert Selected Clips to Timeline Using Timecode." 4 Every selected clip gets overwritten into the Timeline at its appropriate timecode location onto the destination track. IMPORTANT: If multiple selected clips share overlapping timecode, no edit happens.

### Insert Selected Clips to Timeline With Handles

Reachable from the Media Pool contextual menu, "Insert Selected Clips to Timeline With Handles" is a command that edits one or more selected clips onto the open timeline while trimming the default handle length off both the head and tail of each clip. Its purpose is to simplify chaining together a run of clips you'd like joined by transitions, doing so by automatically reworking the In and Out points of every clip edited into the Timeline so that handles come into being. To apply insert selected clips to timeline with handles when editing one or more clips into the Timeline: 1 In the Media Pool, pick one or more clips you'd like joined to the Timeline. Where required, reorder the Media Pool's sort so these clips fall into the sequence you want them joined to the Timeline. 2 In the Source Track Selector, click the audio and video destination controls for whatever tracks the incoming source clip should sit on, and park the playhead at the spot the incoming clips should begin. Build new tracks if you require them. 3 Right-click any one of the selected clips in the Media Pool and, off the contextual menu, pick "Insert selected clips to timeline with handles." Those selected clips join the Timeline beginning at the playhead's location. To alter how long the handles being removed are, open the Editing panel of the User Preferences and adjust the "Default handles length" setting. There are two cases in which handles won't be added:

- Should any of the chosen Media Pool clips already bear handles from In and Out

points you've placed, then further handles get skipped.

- Should the span of the frames slated for removal to form handles in this operation exceed

the span of one or more clips you've chosen in the Media Pool, then no handles get added whatsoever.

### Three-Point Editing From the Media Pool

Three-point edits can also be run straight from the Media Pool, with no need for the Source Viewer.
