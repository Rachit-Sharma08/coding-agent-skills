# Enabling and disabling subframe editing and subframe editing of in and out points

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Previous section](audio-track-layouts-and-clip-attributes.md) / [Next section](eliminating-subframe-audio-edits.md)
<a id="source-enabling-and-disabling-subframe-editing"></a> <a id="source-subframe-editing-of-in-and-out-points"></a>

### Enabling and Disabling Subframe Editing

Found in the Editing panel of the DaVinci Resolve User Preferences, the “Align audio edits to frame boundaries” preference decides whether an audio clip’s In and Out points snap to whole frame boundaries the way video clips do. Leave this option on and subframe audio edits are off-limits; turn it off (its default) and they are allowed.

### Subframe Editing of In and Out Points

Though the playhead itself will not move in subframe steps, you can resize audio clips in subframe steps by dragging an audio clip’s In or Out point on the Timeline, or by dragging an audio edit to roll it. That helps when trimming tiny audio bits like pops, clicks, or vocalizations.

An audio item’s Out point being resized in subframe steps, viewed inside a one-frame playhead shadow Be aware that with Linked Selection on, trying to resize a selected Video+Audio pair runs into the whole-frame resizing video demands, which stops you from resizing the audio on its own. The fix is simple: Option-Click to grab the linked audio item by itself, after which subframe resizing is yours to do freely. On top of that, with snapping enabled, a subframe move may prove impossible when you sit too near another edit point, a marker, or the playhead; here, pressing the N key to switch snapping off clears the trouble.
