# Overwrite edits overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Three and four point editing.
[Chapter index](INDEX.md) / [Previous section](three-point-and-split-edit-rules.md) / [Next section](insert-edits.md)
<a id="source-overwrite-edits"></a>

### Overwrite Edits

Your go-to edit and the one you'll reach for most, an overwrite edit wipes out whatever media occupied the Timeline before and drops the incoming source clip in its place. It's the natural choice while first assembling clips or working through three-point editing, and it leaves the Timeline unrippled. To overwrite one or more Timeline clips: 1 Park the playhead on the Timeline frame where the clip should go. 2 In the Source Track Selector, click the right audio and video destination controls for the tracks that will receive the incoming source clip, adding new tracks if you must. 3 Open a single Media Pool clip into the Source Viewer, then mark In and Out points to bound the media range you want to drop in. 4 To carry out the edit, choose Edit > Overwrite, hit the Overwrite Clip button on the toolbar, press F10, or drop a clip onto the Overwrite overlay in the Timeline Viewer.

Before and after an overwrite edit, total Timeline length is unchanged The chosen Media Pool clips overwrite onto the chosen track from the playhead's position outward, replacing whatever sat there before while bringing the incoming clip in. Nothing else on the Timeline ripples during the operation.
