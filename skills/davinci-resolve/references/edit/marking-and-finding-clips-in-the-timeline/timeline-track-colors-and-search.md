# Color coded timeline tracks and finding clips media markers gaps and timelines

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](hiding-markers-by-color-and-deleting-markers-by-color.md) / [Next section](finding-media-and-tracking-clip-usage.md)
<a id="source-color-coded-timeline-tracks"></a> <a id="source-finding-clips"></a> <a id="source-finding-clips-in-the-timeline"></a> <a id="source-finding-clips-media-markers-gaps-and-timelines"></a> <a id="source-finding-clips-using-markers-or-flags"></a> <a id="source-finding-edit-index-events-using-clips-in-the-timeline"></a> <a id="source-finding-gaps"></a> <a id="source-finding-media-using-match-frame-operations"></a> <a id="source-finding-offline-clips-in-the-timeline"></a> <a id="source-finding-the-currently-open-timeline-in-the-media-pool"></a> <a id="source-matching-from-a-source-clip"></a> <a id="source-matching-from-the-timeline"></a>

### Color-coded timeline tracks

Color a track and that track's color shows up as a slim strip left of the track's header controls. Every clip you drop onto that track takes on that color, unless it's been given its own clip color, in which case the individual clip color wins out over the track color. That makes track colors a fine route to visual organization, since no prep is needed up front; just dropping a clip onto a particular track color codes it to match that track's intended role.

In a timeline using color-coded tracks, the clips on each track pick up its tint on their own

### Finding Clips, Media, Markers, Gaps, and Timelines

DaVinci Resolve gives you several ways to track down clips, markers, and gaps, helping you troubleshoot troublesome timelines or hunt up media you'd like to edit into a timeline another way.

### Finding Clips in the Timeline

By way of the Edit Index, DaVinci Resolve makes pinpointing one or more Timeline clips that fit certain criteria easy. Tracking down a Timeline clip runs like this: 1 Open the Edit Index. 2 Hit the magnifying glass button so the search controls appear. 3 Pick a criteria off the Filter By drop-down menu. 4 Enter a search term in the Search field over at the top right of the Edit Index. The moment you begin typing, every edit event that fails the search criteria gets hidden for the time being. To bring all the Edit Index clips back into view, click the X at the right end of the search field. 5 Click any event in the Edit Index and the playhead jumps to that clip in the Timeline.

### Finding Offline Clips in the Timeline

The Edit Index also makes turning up any offline clips that might sit in the Timeline simple. Turning up offline media in the current Timeline through the Edit Index goes like this: 1 Open the Edit Index. 2 From the Edit Index, open its Option menu and pick Show Offline Clips Only. The Edit Index narrows to display only the offline clips in the timeline that's currently open, and clicking any list item jumps the playhead straight to that clip in the Timeline. 3 Click any event in the Edit Index and the playhead moves to that clip in the Timeline.

### Finding Edit Index Events Using Clips in the Timeline

The Timeline playhead can also pinpoint particular Edit Index events. To locate a clip in the Edit Index from the Timeline:

- Run the Timeline playhead so it crosses a clip you'd like to find in the Edit Index. That clip's matching event (or events, if the playhead crosses several clips) light up on their own in the Edit Index.
- To drive the playhead onto a Timeline clip by way of the Edit Index.
- Click any event in the Edit Index to send the Timeline playhead to that clip's In point.

### Finding Clips

While you work, a range of methods is open to you for tracking down clips, whether in the Media Pool or out in your file system. Ways to locate clips across the Media Pool or File System:

- To find a clip in the Media Pool: Open the Media Pool, then use the drop-down beside the Search button to decide whether the search covers every bin in the current project or only the bin or bins picked in the Bin List. If you need to, select the bin or bins to search, then click the magnifying glass button to bring up the search controls. Optionally pick a criteria off the Filter By drop-down menu, then enter a search term in the Search field. The instant you begin typing, every clip that fails the search criteria gets hidden for the time being.
- To pin down a Timeline clip within the Media Pool: Right-click any clip in the Timeline and pick Find in Media Pool. That clip shows up highlighted in the Media Pool.
- To pin down a Source Viewer clip within the Media Pool: With a clip loaded in the Source Viewer, hit Option-F.
- To pin down a media file in the Finder, working from the Media Pool: right-click a Media Pool clip and pick Reveal in Finder. A Finder window, or whatever stands in for it on Windows and Linux, opens to the directory holding that clip, which appears highlighted.
- Reveal Media Pool Bin from Multi-Bin or Search Displays: When a clip search returns hits spread over several bins, you can now surface where that clip lives in the Media Pool by right-clicking the clip and picking Reveal Media Pool Bin off the contextual menu.
- To turn up the audio clip a video clip got synced with: Right-click a video clip synced to audio and pick "Reveal synced audio in Media Pool" off the contextual menu. The bin that holds the synced audio clip opens and that clip gets selected.

### Finding Clips Using Markers or Flags

When markers serve to track notes, issues, or to-do items, a handful of ways exist to find them and move between them. Methods of finding markers or flags:

- To find all markers or flags via the Edit Index: Open the Option menu of the Edit Index and pick Show Markers or Show Flags. Every clip carrying one or more markers turns up in a list, its columns matching the color(s) and notes of each timeline and clip marker.
- To pin down one particular marker or flag in the Edit Index: Within the Edit Index, click the magnifying glass button, pick Notes in the Filter by drop-down, then enter a search term in the Search field.
- To send the playhead onto the next marker ahead or behind: go to Playback > Previous Marker (Shift-Up Arrow); for the other direction, Next Marker (Shift-Down Arrow).

### Finding Gaps

Gaps — the empty spaces between two clips on the Timeline — render as black by default. Stray gaps can flash up as black frames while your program plays, and are best steered clear of. DaVinci Resolve makes turning up gaps in particular tracks of your timeline easy.

To find gaps in the Timeline: 1 See to it that the Auto Select control is on for any track you mean to scan for gaps. Switch Autoselect off on any tracks you'd rather not scan for gaps (title tracks, for example, where gaps are expected). 2 Do one of the following:

- Choose Playback > Previous Gap or press Option-Command-Semicolon.
- Choose Playback > Next Gap or press Option-Command-Apostrophe. The playhead moves on its own to the first frame of the next gap in the Timeline.

To delete gaps in the Timeline: 1 See to it that the Auto Select control is on for any track you mean to clear gaps from. Switch Autoselect off on any tracks you'd rather leave gaps in (title tracks, for example, where gaps are expected). 2 Choose Edit > Delete Gaps. To hold the deleted gaps to a certain range, note that this command honors both In/Out ranges and clip selections on the Timeline.

### Finding the Currently Open Timeline in the Media Pool

When you aren't leaning on one of the available ways to keep timelines organized apart from clips, losing track of where your timeline sits is easy. To pin down where the open Timeline sits within the Media Pool, choose Timeline > Find Current Timeline in Media Pool.

### Finding Media Using Match Frame Operations

Match frame operations save real time when you have to line the original source clip up with a clip in the Timeline, or when you want a clip in the Source Viewer to lead you to that same clip in the Timeline. One command matches one clip to another so you can set up a fresh edit and handle all sorts of tasks.

### Matching From the Timeline

A textbook case for Match Frame is when you first edited a video clip into the Timeline without its matching audio, then later decide you want that audio in the Timeline after all. The quick fix: run the Timeline playhead so it crosses the clip you need to mend, then use the Match Frame command to pull the original source media for that clip into the Source Viewer on its own, setting Source In and Out points that line up with the Timeline clip's and parking the Source playhead on the same frame as the Timeline playhead. From there you simply edit the source audio and video back onto the Timeline to overwrite the video-only clip you began with, sure you're editing precisely the same span of media in precisely the same spot. Match Frame from the Timeline to a source clip using the pointer: Holding Option, double-click the Timeline clip. That clip's original source media loads into the Source Viewer by itself, its In and Out points lining up with the targeted Timeline clip's; the Source playhead settles on the same frame as the Timeline playhead.

Match Frame from the Timeline to a source clip using keyboard shortcuts or Viewer controls: 1 Run the Timeline playhead so it crosses the clip you mean to target.

Placing the playhead over a clip to Match Frame 2 When other clips on a multi-track timeline overlap the one you're targeting for this operation, the clip on the highest video track becomes the target for Match Frame operations. To target a clip on a lower track instead, click the specific clip beneath the playhead to highlight it. Or you can switch off the Auto Selection controls of every timeline above, or Option-click the Auto Selection control on the track holding your target clip to solo that one. 3 Hit the F key, or click the Match Frame button down at the lower right of the Timeline Viewer (it sits left of the In and Out buttons).

The frame matched against the one under the Timeline playhead; In and Out points get aligned to those of the Timeline's clip That clip's original source media loads into the Source Viewer by itself, its In and Out points lining up with the targeted Timeline clip's; the Source playhead settles on the same frame as the Timeline playhead.

### Matching From a Source Clip

Match Frame runs the other way around as well. You can open into the Source Viewer a source clip you know matches a clip in the Timeline, then use Match Frame to turn up any Timeline clip that matches media held inside the source clip on its own. Putting Match Frame to work in the Source Viewer to turn up a Timeline clip goes like this: 1 Into the Source Viewer, open a clip covering a stretch of media that's already gone into the Timeline. Should none of the source clip have been edited onto the Timeline, source match framing comes up empty. 2 Drive the Source Viewer playhead to whatever frame you're after in the Timeline. Again, should the frame beneath the Source Viewer's playhead not yet sit on the Timeline, the Source Match Frame command comes up empty. 3 Hit the Match Frame button down at the lower right of the Source Viewer (it sits left of the In and Out buttons), or press the F key. By itself the Timeline playhead jumps to the clip and frame beyond its current spot that matches whatever's in the Source Viewer.
