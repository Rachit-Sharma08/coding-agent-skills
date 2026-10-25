# Manually selecting clips in the timeline overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Previous section](inserting-clips-timecode-handles-and-audio-tracks.md) / [Next section](marker-flag-color-and-edit-selection.md)
<a id="source-editing-basics-part-2"></a> <a id="source-manually-selecting-clips-in-the-timeline"></a>

### Manually Selecting Clips in the Timeline

Plenty of operations have you make a selection first, to mark out the scope of what you're about to do. There are many routes to that. Selections you can make using the mouse:

- To select one clip: Click a clip with the mouse.
- To select all clips under the playhead: You can pick every clip under the playhead at once, no matter how many tracks they're spread across, by choosing Trim > Select All Clips Under Playhead (Option-Shift-V).
- To select a continuous range of clips by dragging: Starting from a vacant patch of the Timeline, draw a bounding box that encloses a cluster of clips.

Drawing a bounding box to grab a continuous stretch of clips across the Timeline

- To select a continuous range of clips by Shift-clicking: Begin by clicking the run's first clip, then Shift-click the last; everything between them gets selected on its own as well.
- To select a discontinuous range of clips: Command-click whatever clips you like to grab them no matter where they sit on the Timeline. A Command-click on an already-selected clip drops it from the selection.

Using Command-clicks to grab a discontinuous stretch of clips across the Timeline Selecting clips using the keyboard or menu commands:

- To select one clip: From the keyboard, confirm that the Source Track Selector button is on for whichever track holds the clip, position the playhead above that clip, and then press Shift-V.
- To select a clip using keyboard navigation: While holding the Command key, tapping the Up, Down, Left, and Right Arrow keys lets you jump the selection to clips on the tracks above and below, as well as those to either side, without regard to where the playhead sits.
- To select all clips forward of the playhead on the current track: Position the playhead over the first clip you'd like in your selection, then hit the Y key (Timeline > Select Clips Forward > On This Track), which grabs that clip plus everything to its right on the same Timeline track.
- To select all clips forward of the playhead on all tracks: Position the playhead over the first clip you'd like to include, then hit Option-Y (Timeline > Select Clips Forward > On All Tracks), which grabs that clip along with everything to its right across every Timeline track.
- To select all clips backward from the playhead on the current track: Position the playhead over the final clip you'd like in the selection, then hit Command-Y (Timeline > Select Clips Backward > On This Track), which grabs that clip plus everything to its left on the same Timeline track.
- To select all clips backward from the playhead on all tracks: Position the playhead over the final clip you'd like included, then pick Command-Option-Y (Timeline > Select Clips Backward > On All Tracks), which grabs that clip along with everything to its left across every Timeline track.
- To select all clips in the Timeline: Confirm the Timeline holds focus, then hit Command-A.

To change which clip is selected using the keyboard:

- Pick a clip, then apply the Command-Up/Down/Left/Right Arrow keys to shift the selection to whichever clip sits above, below, before, or after it across all tracks.
