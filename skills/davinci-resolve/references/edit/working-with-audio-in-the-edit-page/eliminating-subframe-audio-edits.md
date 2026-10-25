# Eliminating subframe audio edits

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Previous section](subframe-editing-and-in-out-points.md) / [Next section](record-voiceover-tool-and-audio-settings-in-the-inspector.md)
<a id="source-eliminating-subframe-audio-edits"></a> <a id="source-working-with-audio-in-the-edit-page-part-2"></a>

### Eliminating Subframe Audio Edits


Should you be sitting on an assortment of subframe edits that you want cleared away, the route is Timeline > Trim Audio Edits to Frame Boundaries. That snaps every edit along the timeline onto frame boundaries for whichever clips were cut to subframe precision. A clip running past the nearest frame gets pulled back, while a clip whose start or end falls near a frame boundary — and which still has extra material to spare — gets stretched out to meet that nearest frame boundary.
