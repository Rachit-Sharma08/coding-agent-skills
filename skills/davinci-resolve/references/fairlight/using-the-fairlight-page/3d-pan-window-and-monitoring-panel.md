# 3D pan window and monitoring panel

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](playhead-modes-and-visible-video-tracks.md) / [Next section](media-pool-preview-and-bin-types.md)
<a id="source-absolute-and-relative-measurement-scales"></a> <a id="source-importing-media-into-the-media-pool-on-the-fairlight-page"></a> <a id="source-media-pool-preview-player"></a> <a id="source-the-3d-pan-window"></a> <a id="source-the-double-row-monitoring-panel"></a> <a id="source-the-media-pool"></a> <a id="source-the-monitoring-panel"></a> <a id="source-the-monitoring-panel-1"></a> <a id="source-the-monitoring-panel-2"></a> <a id="source-viewer"></a>

### The 3D Pan window

- Bus Outputs: With these buttons you route a track or bus to one or several of the output busses.
- VCA: These buttons route that track’s channels to VCAs 1-10, or, through a secondary dialog box,

draw from the wider pool of 128 VCAs in total.

- Track name: This echoes the track name shown in the Timeline’s header controls. To rename a track from the Mixer, double-click and type into the name field.
- Arm, Solo, and Mute buttons: The same as the controls in each timeline audio track’s header. Arm turns on recording for a track. Solo silences every other track so that one plays on its own (together with any other Soloed tracks). Mute switches off audio playback from that track. You’ll find these controls in the Tracks Index as well.
- dB display: Reports the volume level, expressed in decibels, the track currently sits at.
- Automation Arm: Arms the automation control for each track. Switched on, it captures automation in Latch

mode while the transport rolls. The control also turns red as soon as a fader moves. You can set automation to “Safe” or “Off” by right-clicking this control.

- Level Meter: A live readout that tracks a channel’s signal level across the -60db to 0db range. How the audio metering displays and decays is configured under Project Preferences > Fairlight > Audio Metering.
- Fader: A track’s main vertical faders set that track’s level and let you record automation. Double-click the fader handle and it snaps back to the default level of 0. Keep Shift held while moving a fader for fine level control at .1 dB resolution.

TIP: Bus routing, VCAs, plugins, and the enable/disable of automation safe can all be set in a hurry across a chosen group of channel strips — or across every channel strip — by holding the Option key (Mac) or the Alt key (Windows) for all the selected tracks, or Command-Option (Mac) or Control-Alt (Windows) for every mixer channel strip, before you carry out the action. Shortcuts like these can shave considerable time off your workflow.

### The Monitoring Panel

Stretching across the top of the Fairlight page, the Monitoring panel presents every audio meter that maps to the Timeline’s tracks, plus the Master Output meter, the Control Room meters, and a video viewer.

### The Monitoring panel

On the left sits a row of audio meters tied to the Mixer’s channel strips — one meter per audio track in the Timeline. A given track meter shows however many channels match that track’s audio format: a single audio meter for mono tracks, two for stereo, six for 5.1, and so forth. Every one of these track and bus meters — the Loudness meters aside — plots both peak and RMS (root mean square) levels against a dB scale. Just right of the Track meters come the Bus meters, where all the busses are grouped by type, each showing a meter whose channel count matches that bus’s audio format. That way you can read the combined total of every track routed into a given bus. Farthest to the right of all is the final group, the Loudness meters, made up of two meter sets and a numeric readout area. The Control Room meter mirrors the program’s main output level, while the Loudness meter gauges the mix’s loudness on whichever scale the user selected. This keeps you abreast of the overall mix’s “integrated loudness,” the benchmark every present-day mixing specification cites when laying out client deliverables. You can change the monitoring panel’s height by dragging its bottom edge.

### Absolute and Relative Measurement Scales

Some people like reading their levels on a relative scale anchored at “0,” much as a VU meter’s needle sits above the “0,” whereas others want the amplitude’s absolute reading in LUFS and true peak. Out of the box, the Loudness meter uses the relative scale, yet you can now switch the Loudness meter between relative scale and absolute scale.

That setting within the Loudness panel surfaces the different measure types along with the absolute scale choice.

In the Loudness menu, relative scale is gauged against whichever scale you picked, so a loudness unit of 0 lines up with the target of the selected measure type. As an example, choose EBU R128, whose target measure is -23dB LUFS, and the “0” LU (Loudness Unit) equals -23dB. Pick ATSC A/85 instead, whose target is -24dB, and that value becomes the equivalent of the relative LU of 0. On the absolute scale, the Loudness meter labels its increments to suit the chosen measure type. Under absolute scale the EBU R128 meter reads -23 rather than the 0 of relative scale. With high track counts, a right-click on the panel opens a contextual menu offering single or dual rows plus narrow or wide meters. Double-clicking the bus master meters along the right side likewise gives you a double row view of them.

### The double row Monitoring panel

### Viewer

Tucked at the far-right end of the Monitoring panel, a compact viewer lets you watch video playback; it consistently displays the video frame that matches the playhead’s position.

- Resize the viewer inside the monitoring panel by dragging the left or bottom edge of its window.
- A button down in the lower-right corner pops the Viewer out into its own floating window.
- The Fairlight page supports Cinema Mode viewing (Command-F), or you can reach it from the Workspace menu,

Workspace > Viewer Mode > Cinema Viewer.

- Clean Feed mode view is also available on a second monitor: choose Workspace >

Video Clean Feed and pick the target monitor for dedicated video playback.

- The Viewer can be shut off altogether via the Workspace > Fairlight Viewer submenu.

### The Monitoring panel

### The Media Pool

On the Fairlight page, the Media Pool acts as the storehouse for every audio clip in your project — both the clips sitting in the Timeline and those you’ve brought into the project but haven’t used yet. Record audio into the Timeline and the clips it produces land in the Media Pool too, ready for later. The Media Pool turns up on every DaVinci Resolve page and holds all the video clips and timelines belonging to your project. Off to the left, the Bin list lays out a nested set of folders called bins for arranging your media, and they serve just as well for arranging your timelines. By default the Media Pool has just one bin, called “Master,” though you can add more whenever you need to sort timelines and clips: right‑click any empty spot in the Media Pool and pick Add Bin. Rename a bin by double-clicking its name and typing a fresh one, or by right-clicking the bin’s name and picking Rename Bin. Show or hide the Bin list with the button in the top-left corner of the Fairlight page toolbar.

The Media Pool in Thumbnail mode showing audio clips Over on the right, the browser area presents what’s inside whichever bin is currently chosen in the bin list. Here you’ll see every clip you bring in, every timeline you build, and every AAF, XML, EDL, and other importable file type. Within a single project you may make or import as many timelines as you like. Just as in other places, the Media Pool can appear in Metadata view, Thumbnail view, or List view. List view lets you order the contents by any one of a subset of the full metadata available in the Media page’s Metadata Editor. Audio editors will especially care about columns such as Clip Name, Reel Name, the various timecode streams, Audio Channels, Format, Audio Codec, Date Added, Flags, and Duration.

To learn about putting every Media Pool feature to use, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.” The sections that follow recap a handful of the Media Pool’s main features for easy reference.

### Importing Media Into the Media Pool on the Fairlight Page

Bringing clips into the Media Pool from the Media page gives you the richest organizational options and tools, but when you’re over on the Fairlight (or another) page and need a few clips in a hurry for immediate use, several routes get you there. Bring in media by dragging one or more clips out of the Finder onto the Fairlight page Media Pool (macOS only): 1 Pick one or more clips in the Finder. 2 Drag them into DaVinci Resolve’s Media Pool, or onto a bin in the Bin list. They join your project’s Media Pool. Use the File > Import > Media command: 1 With the Fairlight page showing, go to File > Import > Media. 2 In the Import dialog, pick one or more clips to bring in and click Open. Lean on the Import Media command sitting in the Media Pool of the Fairlight page: 1 While that page is up, right-click somewhere inside the Media Pool and select Import Media. 2 Within the Import dialog, choose the clip or clips you want and press Open. They join your project’s Media Pool.

For deeper coverage of importing media through the Media page’s many features, consult Chapter 18, “Adding and Organizing Media with the Media Pool.”

### Media Pool Preview Player

Atop the Media Pool sits a preview player, a spot to open chosen source clips from the Media Pool, run them, drop marks to log them, and lay down In and Out points ahead of dragging them into the Timeline as an edit. In practice the Media Pool Preview Player stands in as a Source monitor for editing on the Fairlight page.
