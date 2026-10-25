# Inspector opened and showing a clips parameters and timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](source-audio-waveforms-and-cinema-viewer.md) / [Next section](toolbar-selecting-the-timeline-view-options.md) / [Continue Toolbar / Selecting the Timeline View options](toolbar-selecting-the-timeline-view-options.md)
<a id="source-an-edited-timeline"></a> <a id="source-enabling-and-disabling-audio-scrubbing"></a> <a id="source-fixed-playhead-mode-in-the-timeline"></a> <a id="source-inspector"></a> <a id="source-playback-post-roll"></a> <a id="source-show-playhead-shadow"></a> <a id="source-switching-among-multiple-timelines"></a> <a id="source-the-inspector-opened-and-showing-a-clips-parameters"></a> <a id="source-timeline"></a> <a id="source-timeline-options"></a> <a id="source-toolbar"></a>

### Inspector

Opening the Inspector gives you a place to tailor a clip’s compositing, transform, and cropping parameters, plus its clip-specific retime and scaling options. On top of that, the Inspector is where you adjust the parameters of any transitions, titles, and generators in the Timeline so as to shape their effect.

### The Inspector, opened and showing a clip’s parameters

While the Inspector is open, the Source and Timeline viewers shift leftward to sit beside it as it shows the chosen clip’s parameters. That said, if your monitor’s resolution falls short, opening the Inspector can push the Source Viewer out of sight. Ways to bring up parameters in the Inspector:

- To reveal a video or audio clip’s transform settings while the Inspector is shut: Highlight the clip, then click the Inspector button over at the far right end of the Edit page toolbar.
- When the Inspector already stands open: Merely selecting a clip or effect exposes its controls there.
- When the Inspector is shut: Double-clicking any transition opens it on its own.

Across its top the Inspector carries assorted buttons for jumping between different parameter pages. For instance, select a clip holding both audio and video parts and the Inspector puts Video and Audio buttons up top so you can move between each batch of controls.

### Timeline

The Timeline displays whichever timeline you double-clicked over in the Timelines browser. This is where you build programs from the ground up or pull in sequences created elsewhere. With imported programs, the Timeline gives a visual picture of the cut that helps you confirm the project came in correctly, inspect the media behind each clip in the program, and carry out any editorial steps needed to ready a project for grading (replacing or adding clips, layering composites, and tweaking composite modes or transitions, say).

### An edited timeline

- Timeline Ruler: Along the Timeline Ruler you see the program’s timecode, while the playhead points to the present frame of the present clip. The clip that the playhead crosses is the one you will tackle on the Color page. Drag inside the Timeline Ruler to slide the playhead. Markers you add to the timeline turn up within the Timeline Ruler as well.
- Playhead: This playhead stays synchronized with several others — the one on the Timeline Viewer’s jog bar, those riding the Mini-Timeline and Thumbnail timeline of the Color page and Cut page, and the playhead on the Deliver page. Beyond that, the Edit Index event matching the clip the playhead crosses is highlighted for you automatically.
- Timecode field: Reports the present timecode value that goes with where the playhead sits.
- Video Tracks: Multiple video tracks are supported by DaVinci Resolve. To the left of each track sits a header

area holding several controls.

- Track Header: Within the Track Header sit the various controls for selecting tracks, locking or unlocking them, and switching them on or off. Each track header additionally notes the clip count on that track. The Track Header holds these five controls, reading left to right:

The Track Header area, where each track’s controls reside Track Color: Any track can be tinted with one of 16 distinct colors. Those color codes carry over to the Edit page Mixer along with the Fairlight page Mixer and Audio Meters. To assign a fresh color to a track, right-click its track header and pick from the Change Track Color submenu. Source Track Selector: A pair of rectangular icons under columns marked V1, A1, A2 and so on. The blue left-hand column stands for the tracks inside source clips chosen in the media pool or open in the source viewer. The red right-hand column stands for the destination tracks on your timeline. The Source Track Selector is how you map a given source-clip track onto a particular timeline track. Click a track’s number to flag that track for various editing operations; a flagged track glows red or blue, whereas an unflagged one carries no highlight. Lock Track button: White while on, dark grey while off. Once a track is locked, its clips cannot be swapped, repositioned, or otherwise edited, though clips on locked tracks remain gradable. The track then shows a grey mesh pattern laid over it in the timeline, a cue that it is off-limits to changes. Sync Lock: On out of the box, white when that track is flagged and dark grey when it is not. The icon governs how that track’s clips behave during a ripple edit. Switched on, it ripples alongside the other tracks (say an item is ripple deleted, and the remainder of the timeline slides left to close the gap); switched off, ripple acts solo on that track and skips the ripple from edits on other tracks. Solo (Audio Track Only): Clicking this “S” icon silences every other audio track and plays only the chosen one. Several Solo tracks can be flagged at once so you hear just that selection. Enable Track/Mute button: A small film icon sits on (enabled) by default; a slash across it plus a grey wash over the track itself flags a disabled track. The control switches tracks on and off. Clips on a switched-off track stay out of the viewer, are absent from the Color page, and cannot be rendered or output. On Audio tracks this becomes the Mute button (M). Audio Channel Type indicator: Audio tracks additionally reveal which channel layout the track runs, citing the channel count for mono, stereo, 5.1, 7.1, and adaptive. Track Name: Every track carries a name that starts out as the track type plus its number, like Video 1, Audio 1. You are free, though, to click any track’s name and rewrite it however you wish. As an example, you might retitle each audio track by the kind of audio going onto it — Production, Ambience, SFX, or Music. Those track names also serve to label each track’s channel in the Edit page Mixer and the Fairlight page Mixer. Number of clips: How many clips occupy that specific Timeline track is shown, but only when the track stands tall enough to make room.

- Vertical and horizontal scroll bars: When your project runs wider than the Timeline’s present width, or the video-track stack rises above the Timeline’s present height, these scroll bars let you drag your way around the program.
- Individual Timeline track resizing: You can resize any single Timeline track on its own by dragging the top divider in its Track Header area.

Dragging a single timeline track’s top border within the Track Header to resize it

### Timeline Options

A range of methods exists for tailoring particular Timeline elements and behaviors.

### Fixed Playhead Mode in the Timeline

The fixed playhead mode is chosen from the Edit page’s Timeline View options. With this option active the playhead stays pinned at the timeline’s center while the timeline’s tracks glide beneath it, much as on the Cut page.

Choosing Fixed Playhead mode from within the Timeline View options Selection Follows Playhead Starting with DaVinci Resolve 17, the Clip selection ceased to travel automatically with the playhead. In its place, a fresh batch of commands lets you form and shift a selection by holding the Command key while tapping the Up, Down, Left, and Right Arrow keys. That makes it possible to grab clips above and below the present track as well as to either side, all separate from the playhead. To restore the Clip Selection mode to its old habit of automatically grabbing the top clip it crosses, choose Timeline > Selection Follows Playhead.

### Show Playhead Shadow

By default the Timeline draws the playhead as a lone line marking the start of the frame on view in the Timeline Viewer. You can, however, pick Show Playhead Shadow from the User Preferences UI Settings to wrap the playhead in an orange-ish backdrop. The shadow makes the playhead’s spot easier to read, and it doubles as a gauge on projects where you care to picture a particular offset, measured in frames, on either side of where the playhead currently sits. Adjust that offset using the Pre- and Post-Playhead Shadow Length parameters; you will find them under the User Preferences’ Editing panel, where they govern how many frames get shadowed ahead of and behind the playhead. Out of the box the playhead shadow runs 5 frames long.

(Left) the playhead in its default form; (Right) the same playhead with the optional shadow turned on TIP: Dial the “Pre-playhead shadow length” down to 0 while pushing the “Post-playhead shadow length” up to 1, and you get a “Media Composer-style” playhead that conveys the current frame’s duration.

### Enabling and Disabling Audio Scrubbing

Audio scrubbing comes switched on by default, so dragging the playhead to and fro with the mouse plays audio. That helps while you hunt for audio cues, yet it can be a nuisance when your attention is solely on the picture. To switch audio scrubbing on or off: Choose Timeline > Audio Scrubbing (Shift-S)

### Playback Post-Roll

Lets the playhead keep running beyond the Timeline’s final clip for a span matching the “Post-roll time” Project Setting in the Editing panel. It suits editors who want a brief stretch of playback once they cut or fade to black past the last frame of audio and video on the Timeline. To switch playback post-roll on or off: Choose Timeline > Playback post-roll

### Switching Among Multiple Timelines

Timelines sort just like any other clip in the Media Pool. The procedures below cover opening timelines and moving between them. To change timelines, do any one of these:

- Double-click a timeline in the Media Pool on any page.
- Switch on Stacked Timelines from the Timeline View Options menu in the Edit page toolbar, and every timeline you open shows up as a tab. Click a tab to jump to that timeline.
- On the Edit page Timeline Viewer, grab a timeline from the Timelines drop-down menu at the viewer’s top.
- On the Color page, grab a timeline from the Timelines drop-down menu at the Viewer’s top.
- On the Fairlight page, grab a timeline from the Timelines drop-down menu sitting left of the transport controls.

### Toolbar

Mid-way along the toolbar above the Timeline, a cluster of buttons gives you the various tools and options for carrying out different editing functions.
