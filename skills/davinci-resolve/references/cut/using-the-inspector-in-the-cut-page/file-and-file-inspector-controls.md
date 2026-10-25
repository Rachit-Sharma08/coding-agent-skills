# File and file inspector controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the cut page.
[Chapter index](INDEX.md) / [Previous section](bands-2-through-5-and-effects.md)
<a id="source-audio-configuration"></a> <a id="source-file"></a> <a id="source-metadata"></a> <a id="source-the-file-inspector-controls"></a> <a id="source-timecode"></a>

### File

### The File Inspector controls

### Metadata

The Inspector's File panel offers one consolidated place to view and edit a slice of a clip's most-used media file metadata. Reaching it from the Inspector is easy on any of the Media, Cut, Edit, and Fairlight pages. These are the parts the tab breaks down into:

- Clip Details: Lays out particulars of the clip's data format (codec, resolution, frame rate, etc.).
- Metadata: Lays out a trimmed-down set of common metadata fields for fast user entry.

Timecode: The clip's start timecode. Edit this field when you want to change the clip's starting timecode by hand. Date Created: The date the clip came into being. Edit this field when you want to change the clip's creation date by hand. Camera: Sets the Camera # metadata.

Reel: Sets the Reel/Card ID. Scene: The clip's Scene number. Shot: The clip's Shot letter/number. Take: The clip's Take number. Good Take: This checkbox marks whether the clip is a good or circled take. Clip Color: Hands a clip a specific color that carries through to the Timeline. Name: Entered by hand, this changes a clip's name within that one timeline only. Comments: Attach a text description to the clip. Auto Select Next Unsorted Clip: With this box ticked, hitting Return after filling a metadata field selects the next clip in the Media Pool and drops the cursor straight into that same field. That allows rapid sequential metadata entry without manually clicking to load each individual clip in the Media Pool. Regardless of the checkbox's state, the Next Clip button selects the next clip in the Media Pool.

### Audio Configuration

The Inspector's File tab now carries an Audio Configuration pane covering the controls that Clip Attributes in the Media Pool used to handle (though that option remains). A more intuitive, visual route for altering an audio clip's track properties is what the Audio Configuration pane provides. Just click an audio clip in the Media Pool or Timeline, then on the File Inspector, to expose this interface.

The Audio Configuration panel, with Track 3 muted while Track 5 sits disabled. For every track inside a multichannel audio file, the pane shows a per-channel waveform display. Where the tracks carry names from the audio recorder, those names ride over their respective tracks as well. As many as 36 tracks of audio can be previewed in the Audio Configuration panel.

A composite waveform of all the tracks sits at the pane's top and updates with the mute status of individual tracks. By default this composite plays when the Play button is engaged, and every channel is audible. Through a format menu you can settle on common configurations for your source audio file without tedious manual re-routing. Custom routing stays possible via custom in the drop-down, which surfaces the older clip attributes for situations needing less common configurations. Audio on a selected source or timeline clip can play or skim as you move the cursor along the waveform, and that specific track is solo'ed while skimming or playing. The play position or monitored track can also switch on the fly during playback. As an example, start playback on Track 1, then just click Track 2, and playback carries on from that point. These controls let you quickly skim through and pin down exactly which audio sits on which track for further tweaking.

Each track carries two adjustments, an Enable/Disable checkbox and a

Mute button.

Enable/Disable: Once a track is enabled, it becomes available to editing operations.

Disabling a track pulls that track out of use in editing operations. So, disable

Track 2 of a 4-track audio file, and dragging that audio file out of the Media Pool into the

timeline brings over only 3 tracks (1, 3, and 4).

These adjustments work solely on Media Pool clips; audio clips already on the timeline have these options grayed out.

Mute: Clicking this icon mutes the track so it goes unheard, yet leaves the actual track in place for editing operations and when dragged into the timeline. Option-clicking a Mute button on a channel lets you solo it by muting every other channel.

Beneath the track layout sits a simple transport control — Play and Stop buttons for starting and halting audio playback. Adjusting Trim Levels of Individual Channels in a Source File Within the audio inspector, a trim control adjusts the level of individual source clip channels. That lets source clip audio in one channel be raised or lowered in level as the situation calls for. Internal to the source clip in the Media Pool, the trimmed level carries over anytime that source clip configuration lands on a timeline, unless you change it.

NOTE: That trim level stands wholly apart from clip gain in the timeline. Watch out, since trimmed levels can clip if you push them too high.

The trim levels of individual audio channels in a multichannel clip can be adjusted. Using the Trim slider 1 In the File Inspector's Audio Configuration section, pick one channel or several. 2 At the bottom, set the Level slider to the audio level you want. The waveform shifts dynamically to that level value and shows a trimmed value in dB inside the channel itself. With multiple lanes selected, every channel trims together. Relative levels go unstored, so adjusting one then forces any others in the selection to match. With no channel lanes selected, the Level control grays out. Multiple Clip Selection and Adjustments You can pick several audio clips and tune their properties in the Audio Configuration pane. As an example, select a batch of audio files and pull Track 2 out of all of them in one move. Still, mind the following:

- Within a multiple clip selection, only the last selected clip shows in the track layout of the

Audio Configuration pane. The top composite waveform, though, gets named "Multiple Clips" to signal that more than one clip is selected.

- Whatever adjustments you make — muting, say, or enabling/disabling a track — land on every selected clip at once.

### Timecode

The Inspector's File tab now carries a Timecode pane covering the kinds of controls that Clip Attributes in the Media Pool used to handle (though that option remains). From here, the timecode details of a clip or clips in the Media Pool can be overridden.

- Current Frame: Lets you hand a fresh time to the timecode at whatever frame of the clip is on view.
- Slate: Where source media comes off a shoot that used a timecode slate, you can hand that slate timecode over as a second timecode track usable for various operations, all without touching the clip's primary timecode, which may already serve program sync.

To set appropriate Slate timecode, pick a clip in the Media Pool whose timecode slate is visible, and shift the playhead to a frame where the slate's timecode reads clearly. Then open the Timecode panel of the Clip Attributes window, and key in the timecode value you read off the image into the Slate Timecode field.

- Offset Source: Where a whole set of clips carries timecode that is simply offset, you can correct that

timecode offset across as many selected clips as you wish.
