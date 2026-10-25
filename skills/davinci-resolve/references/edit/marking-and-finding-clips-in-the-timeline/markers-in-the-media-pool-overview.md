# Markers in the media pool overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](viewer-feedback-annotations.md) / [Next section](hiding-markers-by-color-and-deleting-markers-by-color.md)
<a id="source-marking-and-finding-clips-in-the-timeline-part-2"></a> <a id="source-using-markers-in-the-media-pool"></a>

### Using Markers in the Media Pool

Having attached markers, one or several, onto source clips sitting in the Media Pool, you can put them to work in editing far more directly than merely shuttling the playhead about with them. The Media Pool’s List view can surface markers; once surfaced, each one opens into the Source Viewer, edits into the Media Pool, or becomes a subclip just like any other clip. To surface markers within the Media Pool:

- Switch the Media Pool over to List view, then click the disclosure button sitting left of the clip whose markers you'd like to handle. The markers show up as a nested list beneath the clip they belong to.
- Press the Right Arrow key to expand a clip's marker hierarchy. The Up and Down arrows let you single out a given marker. Press the Left Arrow key to collapse the clip's marker hierarchy.

Markers revealed within the Media Pool while in List view Opening a Media Pool marker into the Source Viewer:

- Double-click any marker and that clip opens into the Source Viewer with the playhead parked where the marker sits.

To edit a clip defined by the marker into the Timeline:

- Drag any marker onto the Timeline. The clip gets edited into the Timeline with its In point set to the marker's frame, and its Out point set to either (a) the frame just ahead of that clip's next marker, or (b) the marker's duration, should that duration run past the default 1 frame.

To turn a marker in the Media Pool into a subclip:

- Pick one or more markers and drag the selection to a different spot in the Media Pool, or over to another Bin, and a sub clip gets made with its clip start set to the marker's frame, and its clip end set to either (a) the frame just ahead of that clip's next marker, or (b) the marker's duration, should that duration run past the default 1 frame.

To add metadata to a marker subclip in the Media Pool:

- Pick a marker subclip in the Media Pool, then fill in the name, notes, keywords and color fields over in the Media Metadata panel.
