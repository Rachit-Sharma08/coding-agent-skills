# Track header and zooming audio waveform height

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](fairlight-page-user-interface-and-fairlight-page.md) / [Next section](toolbar-and-timeline-view-options.md)
<a id="source-audio-editing-modes"></a> <a id="source-flatten-audio-layers"></a> <a id="source-layered-audio-editing"></a> <a id="source-overwrite-mode"></a> <a id="source-resulting-overlap"></a> <a id="source-smart-zoom-timeline-view"></a> <a id="source-smart-zoom-track-height"></a> <a id="source-standard-timeline-view"></a> <a id="source-switching-among-multiple-timelines"></a> <a id="source-track-header"></a> <a id="source-zooming-audio-waveform-height"></a>

### Track header

Controls in the track header let you toggle lock, toggle solo and mute, and record-arm the track. Beyond a level meter, the header carries informational readouts listing the track type, the track's number and name, its volume, and how many clips it holds.

The track header controls of the Fairlight page timeline

- Track color: Any track can be tagged with one of 16 colors, and that color also shows up on the Fairlight and Edit page Mixers, the Tracks Index, and the Audio Meters. To color a track, right-click its header and pick a color out of the Change Track Color submenu. The same color goes onto several tracks at once if you drag across neighboring headers, or Command-click headers that aren't adjacent, then choose a color from the Change Track Color submenu.
- Track number: Shows the number assigned to each track.
- Track name: Every track carries a name that initially matches its track number, like Track 1, Track 2.

That said, you can click any track's name and change it to anything you want. For instance, label each track by the kind of audio you're cutting onto it — Production, Ambience, SFX, or Music. Those same names label each track's channel in the Mixer, centered in each channel strip (with the channel strip's track number shown up top at the same time).

- Audio channel type indicator: Audio tracks also report the channel configuration in use, spelling out the channel count for mono, stereo, 5.1, 7.1, Atmos, adaptive, and the rest.
- Fader value: A readout reports the fader's present setting at the playhead's spot, in dB. It mirrors the track's fader level over on the Mixer panel. Drag the figure upward or downward and the fader tracks along with it.
- Lock Track button: A locked track won't let its clips be swapped, repositioned, or otherwise altered, though clips on locked tracks can still be graded over in the Color page. The lock appears shut while the track's contents are locked and appears open when they aren't.
- Arm button: Pressing this arms that track for recording.
- Solo button: Silences every track except the active one so you can isolate and listen to a single track quickly. Because this carries into rendering, soloing one or more tracks means the muted ones aren't output or rendered.
- Mute button: Briefly silences a track's audio so it isn't monitored or output. Since this carries into rendering, muting one or more tracks keeps them out of the rendered result.
- Audio meters: Every track carries audio meters in its header so you can watch levels as playback runs.
- Toolbar editing tools: The toolbar holds both modal buttons and command buttons to help you work through your projects. The section that follows covers them in greater depth.
- Vertical and horizontal scroll bars: When your project runs longer than the Timeline's current width, or when there are more audio tracks than its current height can show, these scroll bars let you drag your way around the program. Scrolling sideways carries the playhead along with the track waveforms, so for a moment it can slide out of sight; starting playback snaps it back into view. You can also scroll up and down with your mouse's scroll wheel (or other scroll control), and scroll sideways by holding the Command key while you do so.
- Individual Timeline track resizing: You can resize any one Timeline track on its own by right-clicking somewhere inside that track's header control region and picking a height out of the Lock Track Height To submenu in the contextual menu. The fixed sizes on offer are Micro, Mini, Medium, Large, Extra Large, and Custom. Once you set a fixed height, vertical zoom stops affecting that track until you switch its “Lock Track Height to” setting back to None. You can also select several tracks, or all of them, and set them to a single height; every selected track adopts that size until you change it again, whether globally or one at a time.

Resizing an individual audio timeline track using contextual menu options

### Zooming Audio Waveform Height

You're able to zoom the audio waveforms inside the clips of one or more tracks larger or smaller, making them taller or shorter, or send them back to their default sizes. None of this touches the actual audio levels of the clips in those tracks — it simply makes the waveforms easier to read. To resize waveform height with your scroll wheel: hold Command-Option down and roll the scroll wheel or control either way to resize every waveform across all tracks. There are menu commands too, reached at the top under View > Zoom Audio Waveform, for any Timeline track. Pick one track or several to resize their waveforms together. The menu offers three groups of commands:

- Reset
- Zoom Increase Height
- Zoom Decrease Height

Right-click any clip in the Timeline and you can open the Track Waveform Zoom submenu, which carries still more zoom choices.

### Smart Zoom Track Height

Select a track in the Timeline or Mixer and hit Command-Option-E, and Smart Zoom grows that track's height while centering your selection so it fills the entire visible region of the Timeline. When your edits are done, press Command-Option-E once more to leave Smart Zoom. Like the rest of DaVinci Resolve's keyboard shortcuts, Smart Zoom can be reassigned in the Keyboard Customization dialog. To learn more about Keyboard Customization, refer to Chapter 4, “System and User Preferences.”

### Standard Timeline view

### Smart Zoom Timeline view

### Audio Editing Modes

Two audio editing modes live on the Fairlight page: Overwrite Mode and Layered Audio Editing Mode.

### Overwrite Mode

True to the name, when part of a clip lands over another clip during an edit, the overlapped region of the lower clip is removed non-destructively to make room for the arriving clip. Should you move or delete that overlapping clip, the clip beneath it stays trimmed. Whatever this removed is still held in the original clip and can be brought back by trimming the head or tail (whichever side you affected). Overwrite is the mode set by default and suits most everyday editing best.

(Left) Overwrite edit showing original clips, (Right) Right hand clip dragged left

### Resulting overlap

### Layered Audio Editing

Layered Audio Editing is a dedicated mode that lets you stack several audio clips on the same track, where clips placed on the upper layers silence the overlapping parts of clips sitting on lower layers. With this enabled (Timeline > Layered Audio Editing), stacked audio clips behave much like stacked video clips set to 100% opacity, the upper clips hiding (or muting) whatever lies beneath. You can flip this on or off independently under the View menu > Show Audio Track Layers. The mode shines whenever you're stitching pieces of several takes together (“comping”) into one voiceover, vocal track, ADR, or dramatic read, since you decide which pieces to keep by where they stack in that track, all while the other takes stay safe underneath should you want them down the line. Bear in mind, though, that deleting any clip resting “above” another lets the lower layer “poke through.” That extra bookkeeping during editing is among the reasons Overwrite Editing mode is the default. TIP: You can also use Layered Audio Editing mode on audio tracks over in the Edit page.

Layered Audio Editing and Show Audio Track Layers enabled

Layered Audio Editing while Show Audio Track Layers is off — every layer collapses down into one combined view.

### Flatten Audio Layers

Once you've worked through Layered Audio Editing, building a “comp” (composite) of a performance is handy when you want one element that captures the finished result you're after. Timeline > Flatten Audio Track Layers lets you produce a single layer-free edit while keeping the clip boundaries intact. Picking this command slices across each layered clip at its in/out points and merges them down into one layer.

After choosing Flatten Audio Layers, audio layers showing (so blank space above) When you're heading out to an AAF, switch layered audio editing off, because only the lowest, first layer makes it into the export. If you'd been working with layered audio editing already, run Flatten Audio Layers first and then do your AAF export. Note too that with any layered crossfades, only the fades on the incoming clip survive.

### Switching Among Multiple Timelines

Like any other clip, timelines can be organized within the Media Pool. Use the steps below to open one or move between them. Every Timeline holds onto whatever view settings were last set inside it, track heights and zoom among them. To change timelines, do any of these:

- On the Edit, Cut, or Fairlight page Media Pool, double-click a timeline.
- On the Edit page Timeline Viewer, pick a timeline from the Timelines dropdown menu atop the viewer.
- On the Color page, pick a timeline from the Timelines drop-down menu atop the viewer.
- On the Fairlight page, pick a timeline from the Timelines dropdown menu sitting left of the transport controls.
