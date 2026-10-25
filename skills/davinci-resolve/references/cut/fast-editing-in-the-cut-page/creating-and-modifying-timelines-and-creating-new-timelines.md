# Creating and modifying timelines and creating new timelines

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Next section](source-clip-and-viewer-showing-source-clip.md)
<a id="source-about-tracks-in-the-cut-page-timeline"></a> <a id="source-adding-tracks"></a> <a id="source-creating-and-modifying-timelines"></a> <a id="source-creating-new-timelines"></a> <a id="source-deleting-tracks"></a> <a id="source-enlarging-tracks"></a> <a id="source-fast-editing-in-the-cut-page"></a> <a id="source-fast-editing-in-the-cut-page-part-1"></a> <a id="source-navigating-clips-in-the-viewer-and-timeline"></a> <a id="source-opening-timelines"></a> <a id="source-viewer-options"></a>

### Fast Editing in the Cut Page

The Cut page's editing methods have been streamlined to make editing fast,

and this page's interface, along with the ways clips are assembled together using

various edit types, is built to be quick to pick up and quick to work with.

### Creating and Modifying Timelines

Once you've imported and organized the media your program needs, the next step is to create a timeline. Timelines are the organizational entities holding the edited sequences of clips that make up your program. Your project can carry as many timelines as you'd like, each one an independent arrangement of clips. Like clips, timelines live in the Media Pool and can be organized with bins.

### Creating New Timelines

The moment you edit your first clip into the Timeline, a timeline is created automatically. An icon for the new timeline shows up in the Media Pool, where it can be renamed.

A new timeline can also be created by either picking File > New Timeline (Command-N), or by right-

clicking the Media Pool background and choosing Create New Timeline. A dialog opens

letting you choose a start timecode (01:00:00:00 is the default), a name, the count of video and

audio tracks it should carry, the kind of audio (stereo is the default), and whether or not you

want an empty timeline, or one automatically holding every clip in the Media

Pool with or without selected In/Out points (a quick, easy route to a stringout of all the clips

you've imported).

By default, every timeline takes the same frame rate, resolution, and monitoring settings as the project overall. Should you prefer, you can click the Use Custom Settings button to pick individual frame rate, resolution, and monitoring settings for that timeline.

After a new timeline is created, double-clicking it opens it into the Timeline Editor.

### Opening Timelines

When your project holds only one timeline, the Timeline Editor always shows that timeline. Where several timelines exist, double-clicking any of them in the Media Pool opens it into the Timeline Editor, set for editing. Shifting from one timeline to another is also possible via the drop-down list near the top of the Cut page Viewer. Doing so aligns Viewer Timeline Selection behavior across the Cut, Edit, Color, and Deliver pages.

The Timeline Selection drop-down near the top of the Cut page Viewer

A timeline track's header carries the Enlarge, Lock, Audio Enable, and Video Enable buttons

### About Tracks in the Cut Page Timeline

For convenience, tracks in the Cut page timeline merge a clip's audio and video into one track, which makes keeping audio and video organized and in sync simple as many clips get superimposed together. So tracks carry both video and audio enable controls in the track header controls, letting you selectively disable video and mute audio when you need to. Each track additionally has a lock control, which stops clips on that track from being changed in any way.

### Enlarging Tracks

Clicking the Track Sizing icon on the left side of the track header enlarges or minimizes a track. An expanded video track displays a full size video and audio track, where one is attached. This makes focusing on just the track you want easier. Only one track at a time can be expanded.

A click on the Track Sizing icon enlarges the track so the clip's full audio track is shown

### Adding Tracks

When your timeline is short on tracks, click the Timeline Actions menu and pick Add Video/Audio/Subtitle track, or right-click anywhere on the Timeline and choose "Add Track," and a fresh track joins above whatever tracks are already present.

TIP: A new clip dragged onto the undefined gray region atop the Timeline likewise adds a fresh track.

### Deleting Tracks

To remove one specific track together with all of its clips, right-click somewhere in that track's header and choose "Delete Track." Should your timeline hold too many empty tracks, right-click somewhere in the track header and choose "Delete Empty Tracks," and every empty track is cleared away.

### Navigating Clips in the Viewer and Timeline

Before editing can begin, you need to find which parts of which clips to use and define where in the currently open timeline to make an edit. The Single Viewer on the Cut page offers different options that let you choose which media to play through using the transport controls along the bottom.

### Viewer Options

Three options, picked through buttons sitting at the Viewer's upper left, govern what gets displayed in the Viewer.

The Viewer option buttons, reading left to right: Source Clip, Source Tape, Timeline, and Multi Source
