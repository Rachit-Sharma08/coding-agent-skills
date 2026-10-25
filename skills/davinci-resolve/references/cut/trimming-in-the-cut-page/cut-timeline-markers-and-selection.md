# Marker button in the timeline track header and making selections

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming in the cut page.
[Chapter index](INDEX.md) / [Previous section](cut-timeline-tools-and-main-track-ripple.md) / [Next section](overwriting-the-edges-of-other-clips-and-swapping-clips.md)
<a id="source-clicking-clip-bb-to-begin-dragging-it"></a> <a id="source-making-selections"></a> <a id="source-moving-clips-in-the-timeline"></a> <a id="source-overwriting-the-middle-of-other-clips"></a> <a id="source-ripple-overwriting-an-entire-clip-in-track-1"></a> <a id="source-ripple-trimming-on-secondary-tracks"></a> <a id="source-the-marker-button-in-the-timeline-track-header"></a>

### The Marker button in the Timeline track header

Ways to work with markers:

- To add a marker: Park the playhead on a frame you want to flag, then click the Marker button in the Timeline header, or hit the M key. A marker can also be added via the Timeline Actions icon.
- To add a marker with a specific color: Park the playhead on a frame you want to flag, then click the Timeline Actions icon and pick Set Color and Add Marker. This both drops a marker and opens the Markers Edit window, where you can choose a particular color and type a comment.
- To jump the playhead among markers: Hold the shift key and tap the Up or Down Arrow keys to leap the playhead between markers.
- To edit a marker’s name, text, color, or keywords: Either double-click it, or send the playhead onto a marker and press M a second time. When the marker dialog appears, edit the Name, Notes field, Keyword field, or the marker's color, then hit Return or click Done to dismiss it. Markers carrying custom notes display a dot.
- To move a marker: Drag a marker onto a different frame within the Timeline Ruler.
- To delete a marker: Pick a marker and hit Delete. Or, line the playhead up with a marker and press Option-M. Or, send the playhead to a marker, press M to bring up the marker dialog, and click Remove Marker. CUT

Blue, red, and orange markers along the Timeline; only the red one carries text, while the rest have none

### Making Selections

The further you go on the Cut page, the more valuable it becomes to know how to form different sorts of selections, both within the Media Pool and within the Timeline. Most of these selection techniques will feel familiar if you've used other media applications or file managers before. Ways to select clips in the Media Pool:

- To select a single clip: Click a clip within the Media Pool. With a clip selected, the Up and Down arrow keys let you shift the selection to neighboring clips.
- To select a contiguous range of clips: Drag a selection box across every clip you mean to grab, or click the first clip in a run, then Shift-click the last to select those clips plus all in between.
- To select a noncontiguous range of clips: Command-click whichever clips belong in the selection. Or hold Command down as you drag bounding boxes — over clips not yet selected to bring them into the current selection, or over selected ones to take them out.
- To select all clips: Pick one clip, then go to Edit > Select All (Command-A).

Ways to select clips in the Timeline:

- To select one clip: Use the mouse to click a clip. Command-clicking that very clip de-selects it.
- To de-select all clips in the Timeline: Click any empty stretch of the Timeline to de-select everything, or hit Command-Shift-A.
- To select a continuous range of clips by dragging: Starting from an empty stretch of the Timeline, drag a bounding box that wraps a group of clips.
- To select a continuous range of clips by Shift-clicking: Click your first target clip, then Shift-click the final one; everything sitting between them gets selected on its own as well.
- To select a discontinuous range of clips: Command-click whichever clips you want to grab, wherever they sit on the Timeline. Command-clicking an already-selected clip deselects it.
- To select all clips under the playhead: Grab every clip beneath the playhead in one move, no matter how many tracks they span, via Trim > Select All Clips Under Playhead (Option-Shift-V).
- To grab every Timeline clip lying ahead of the playhead: Right-click the playhead's top handle; on the radial menu that pops up, click its right button.
- To grab every Timeline clip lying behind the playhead: Right-click the playhead's top handle; on the radial menu that pops up, click its left button.

The radial menu shown after a right-click on the playhead's top handle Ways to select edits in the Timeline with the pointer:

- To select an edit to roll: Bring the mouse to the middle of an edit point, and once the ripple cursor shows, click to grab the edit.
- To select just the incoming or outgoing half of an edit, ready to resize it: Bring the mouse left or right of an edit's center, and once the resize/ripple cursor shows, click to grab that portion of the edit.
- To select multiple roll points: Command-click the centers of several edit points. Command-click a selected edit point to deselect it.
- To select multiple resize points: Command-click on the left or right side of several edit points.
- To de-select all clips in the Timeline: Click any empty stretch of the timeline to de-select everything.

Keyboard shortcuts for selecting edits in the Timeline:

- To select an edit point from the keyboard: Press V to grab the edit point nearest the playhead.
- To change an edit selection from the keyboard: With an edit point selected, press U to cycle between selecting the outgoing half, the incoming half, or the whole edit.
- To de-select all edits in the timeline: Press Command-Shift-A.

### Moving Clips in the Timeline

After you've cut some clips into the Timeline, you'll likely want to start refining the edit by shuffling clips around. Which operation occurs depends on how you move those clips. Every one of these techniques functions in both the Upper Timeline and the Timeline Editor.

### Ripple Overwriting An Entire Clip in Track 1

Drag a clip in the Timeline or Upper Timeline across another Timeline clip so the pointer covers that clip, then quickly drop it onto another clip in Track 1. Your dragged clip takes over the clip you dropped it on, and every clip to the right shifts to either open space (if the dragged clip is longer) or close the gap (if it's shorter).

### Clicking clip BB to begin dragging it

Dragging clip BB onto clip DD to ripple overwrite it

Clip BB relocates and assumes clip DD's spot, as the remainder of the Timeline slides left to seal the gaps in Track 1 NOTE: Linger too long and this Ripple Overwrite turns into a plain overwrite. Drag a clip from Track 1 onto a clip on any other track and an overwrite is all you'll get, not a ripple overwrite.

### Ripple Trimming on Secondary Tracks

The Cut page's ripple editing works on secondary tracks too, but only where there's no underlying video on the primary video track (Track 1). Toggle this ripple behavior on or off with the Ripple On control in the Cut page timeline header.

Here the aim is to remove the selected clip and seal the gap, despite our clips sitting on a secondary track. Observe that the primary track (Track 1) holds nothing. With Ripple On switched off, removing a clip leaves behind a gap on the secondary track.

With Ripple On switched on, removing a clip seals the gap on the secondary track.

### Overwriting the Middle of Other Clips

Drag a clip in the Timeline or Upper Timeline across another Timeline clip so the pointer covers that clip, hold until your selected clip sits over the second clip, then release the mouse button. The target clip gets overwritten for the length of the clip you dragged and is split into two.

Dragging clip BB and pausing to overwrite part of clip DD

Clip BB relocates, writing over the middle of clip DD, which now sits in two pieces; the remainder of the Timeline slides left to fill the gap that moving clip BB opened in Track 1
