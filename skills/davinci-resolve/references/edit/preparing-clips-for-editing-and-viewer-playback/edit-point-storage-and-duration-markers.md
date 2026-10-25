# Clip edit points are saved and turning in and out points into markers with duration and back again

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing clips for editing and viewer playback.
[Chapter index](INDEX.md) / [Previous section](gang-viewers-playhead-ganging-and-adding-markers.md)
<a id="source-clip-edit-points-are-saved"></a> <a id="source-create-a-timeline-subclip-from-in--out-range"></a> <a id="source-organizing-media-by-creating-subclips"></a> <a id="source-removing-or-changing-subclip-limits"></a> <a id="source-the-edit-subclip-dialog"></a> <a id="source-the-new-subclip-dialog"></a> <a id="source-turning-in-and-out-points-into-markers-with-duration-and-back-again"></a>

### Clip Edit Points Are Saved

After you set them, In and Out points stay put inside each source clip or timeline until fresh ones replace them. Should you quit DaVinci Resolve and later open that same project again, every clip’s In and Out points are preserved for later use.

### Turning In and Out Points into Markers With Duration and Back Again

Should you want to log the key stretches of clips with In and Out points, only one stretch can be logged at any moment, since In and Out points serve to flag the next portion of a clip headed into a three point edit. That said, a pair of commands in the contextual menu of the Source Viewer jog bar team up to let you swap In and Out points for Markers with Duration, and back the other way:

- Convert In and Out to Duration Marker: Converts a pair of In and Out points into a duration marker. Out of the box, no key shortcut is tied to this command, although you’re free to assign one.
- Convert Duration Marker to In and Out: Converts a duration marker into a pair of In and Out points, all while keeping the marker. Out of the box, no key shortcut is tied to this command, although you’re free to assign one.

With these two commands, markers with duration become an easy way to flag regions of clips you’d like to log for later, each region turning into an In and Out point whenever editing calls for it. These commands ship with no keyboard shortcuts attached, but you can attach your own if you reach for them often.

To turn In and Out points into a duration marker: 1 On the Source Viewer jog bar, drop In and Out points that bound a region you wish to log for later reference. Placing the bounds of that clip section ahead of logging it 2 Do one of the following:

- Right-click the jog bar, then pick Convert In and Out to Duration Marker.
- Go to Mark > Convert In and Out Into Duration Marker. A duration marker now appears just above where the In and Out points sit. To revise its name or notes, double-click the marker, hit Shift-M, or head to Mark > Modify Marker.

A duration marker is created from the In and Out points That’s the way to log several separate regions within a lone clip for later use.

One clip carrying several logged sections, each flagged by a duration marker To turn a duration marker into an In and Out point: 1 Track down whichever duration marker you’d like turned into In and Out points..

Locating the duration marker that’s to become In and Out points 2 Do one of the following,

- Right-click the jog bar, then pick Set In and Out from Duration Marker.
- Bring the playhead onto the duration marker, then go to Mark > Set In and Out from Duration Marker.

In and Out points show up beneath the duration marker.

In and Out points are created from the duration marker This is how a duration marker you’ve logged becomes In and Out points, readying you to run a three-point edit. Three things make these logging techniques especially valuable. To begin with, markers with duration are searchable in the Media Pool through the All Fields, Marker Name, and Marker Notes Filter by options. On top of that, Smart Bins can filter on them via the Marker Name and Marker Notes Media Pool Properties options. Finally, once a clip carries one or more duration markers, they offer a fast route to three-point edits into the timeline.

### Organizing Media by Creating Subclips

Subclips hand you yet another approach to organizing media in the Media Pool, letting you carve overly long clips down into shorter pieces. Suppose a project’s director leans on “rolling takes,” recording several takes inside one clip; you can pull those takes apart by turning each into its own subclip. Building a subclip on the Edit page goes like this: 1 Ahead of making any subclips, load a clip into the Source Viewer from either the Media page or the Edit page, by one of these means.

- Double-click any clip in the Media Pool.
- With a single click on any clip in the Media page’s Media Library, build a subclip without first having

to bring that clip into the Media Pool. 2 Lay down In and Out points in the Source Viewer to mark out the section you mean to turn into a subclip. 3 Do one of the following:

- Choose Mark > Create Subclip.
- Press Option-B.
- Right-click the jog bar, then pick Create Subclip out of the contextual menu.
- Drag a clip out of the Source Viewer and into the Media Pool.

4 A new subclip dialog opens, where you can name the subclip and, by ticking the checkbox, opt to use its full extents.

### The New SubClip dialog

Subclips, once made, show up and behave just like every other clip in DaVinci Resolve. You can build subclips on the Media page as well, while you’re busy with other organizational chores there.

### Removing or Changing Subclip Limits

After it’s made, right-clicking any subclip in the Media Pool or a timeline and choosing Edit Subclip brings up a dialog where you can tick a checkbox to use the subclip’s full extents, or revise the subclip’s start or end timecode through the timecode fields, then click Update to apply your changes to the subclip.

### The Edit Subclip dialog

### Create a Timeline Subclip from In / Out Range

You can also build a subclip spanning several clips out of the active timeline on the Edit page. That lets you grab just one section of a timeline and set it apart in a brand-new timeline of its own for more work, leaving the original untouched. To create a Timeline Subclip in the Edit page: 1 Lay down the In and Out points marking where the subclip should start and stop on the timeline. 2 Right-click the selected range along the bottom of the Timeline viewer or on the Timeline ruler bar, and choose Create Subclip from the context menu. You could instead press Option-B.

Doing so spawns a fresh timeline holding only the range you grabbed from the original timeline. In the Media Pool it’s labeled “&lt;timeline name&gt; Subclip” so it stands apart from the original.

Right-clicking the ruler bar within the timeline likewise offers Create SubClip among the list of options.
