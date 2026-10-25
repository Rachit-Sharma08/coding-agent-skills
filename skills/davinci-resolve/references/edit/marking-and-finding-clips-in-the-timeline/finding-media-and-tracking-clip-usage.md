# Finding media and tracking clip usage

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](timeline-track-colors-and-search.md)
<a id="source-finding-a-clip-in-the-media-pool-using-a-timeline-clip"></a> <a id="source-list-view-clip-usage-column"></a> <a id="source-thumbnail-clip-usage-indicators"></a> <a id="source-tracking-media-usage"></a> <a id="source-using-a-clip-in-the-source-viewer-to-find-a-media-pool-clip"></a> <a id="source-using-a-clip-in-the-timeline-to-find-a-media-pool-clip"></a>

### Finding a Clip in the Media Pool Using a Timeline Clip

You've got two ways to use a clip in the Timeline to track down a clip in the Media Pool.

### Using a Clip in the Source Viewer to Find a Media Pool Clip

To pin down the original Media Pool clip that matches a Timeline clip: 1 Load a Timeline clip into the Source Viewer through one of these steps:

- Double-click a clip in the Timeline.
- Drive the playhead onto a Timeline clip, hit Shift-V to select that clip, and then hit the Return key.

2 Press Option-F to track down, in the Media Pool, the source clip that matches whatever's open in the Source Viewer. That clip shows up highlighted in the Media Pool.

### Using a Clip in the Timeline to Find a Media Pool Clip

To track down the Media Pool clip matching one on the Timeline, right-click that Timeline clip and pick Find in Media Pool off the contextual menu. That clip shows up highlighted in the Media Pool.

### Tracking Media Usage

As clips join timelines, two mechanisms kick in to keep tabs on which clips are used in which timelines.

### Thumbnail Clip Usage Indicators

Every time you open a timeline, all the thumbnails in the Media Pool refresh on their own to display highlighted usage bars, signaling which parts of that clip get used in that timeline.

Two colored highlights along the bottom of the thumbnail mark which parts of a clip the currently open Timeline uses Right-click a thumbnail showing usage and a Usage submenu hands you a list of every instance of that clip in the timeline that's currently open. Pick an instance from this list and the playhead jumps to that clip in the Timeline.

### List View Clip Usage Column

While in List view, a Usage column can optionally appear in the Media Pool. By default this column stays empty, but right-click in the Media Pool and pick the Update Usage command, and the project gets analyzed, with every use of that clip across every timeline in the whole project logged into this column.

Once analysis runs, a Usage column reports the tally of how often a clip appears across each timeline NOTE: The usage column ticks up for each clip item that turns up in the Timeline. So if a clip is one video item and one audio item linked together, the usage column reads the number 2.
