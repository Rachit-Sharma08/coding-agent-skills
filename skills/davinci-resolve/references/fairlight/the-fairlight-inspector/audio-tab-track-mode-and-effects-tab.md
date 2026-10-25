# Audio tab track mode and effects tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: The Fairlight inspector.
[Chapter index](INDEX.md) / [Previous section](inspector-speed-change-and-parametric-eq.md) / [Next section](6-mono-channel-media-pool-clip-and-audio-channel-source-menu.md)
<a id="source-6-channel-mono---media-pool-clip"></a> <a id="source-audio-configuration"></a> <a id="source-audio-tab---track-mode"></a> <a id="source-auto-select-next-unsorted-clip"></a> <a id="source-fairlight-fx-delay-controls-in-the-effects-tab"></a> <a id="source-file-information"></a> <a id="source-file-tab---file-information-section"></a> <a id="source-file-tab---file-metadata-section"></a> <a id="source-file-tab---media-pool-clip-selected"></a> <a id="source-for-more-information-see-chapter-180-audio-effects"></a> <a id="source-metadata"></a> <a id="source-the-effects-tab"></a> <a id="source-the-file-tab"></a> <a id="source-the-transition-tab"></a>

### Audio tab - Track mode

NOTE: You cannot edit parameters in the Inspector for locked tracks. To read more about locking audio tracks, turn to Chapter 175, “Editing Basics in the Fairlight Page.”

### The Effects Tab

This tab shows the Audio Effects you have placed on a track or bus through the Effects section of its Mixer channel strip, or onto a timeline clip out of the Effects Library.

### Fairlight FX Delay controls in the Effects tab

### For more information, see Chapter 180, “Audio Effects.”

### The Transition Tab

Should you have placed any Transitions (Crossfade) between clips on either the Edit or Fairlight pages, the Transition tab lets you adjust them; open it by double-clicking a Crossfade transition.

Crossfade controls in the Transition tab of the Inspector

These properties are open to editing:

- Transition Type: Whichever transition is presently chosen. Swap it for any other installed transition by picking one from the dropdown menu.
- Duration: How long the transition lasts, given in both seconds and frames.
- Alignment: A dropdown for setting where the transition lands in relation to the edit

point it is applied to. The picks are “Start on Edit,” “Center on Edit,” and “End on Edit.”

- Fade In: This dropdown lets you pick from -3dB to 3dB.
- Fade Out: This dropdown lets you pick from -3dB to 3dB.

To read more about adjusting crossfades, turn to Chapter 175, “Editing Basics in the Fairlight Page.”

### The File Tab

Across its various sections, the File tab lets you inspect or change how audio clips on the Timeline and in the Media Pool are set up and what properties they hold.

### File Information

Beyond the audio clip’s name, this part of the File tab supplies more details about the file, as the screenshot below shows.

### File tab - File Information section

### Metadata

Every text field, save for the embedded Timecode field, accepts whatever information you choose to type in.

### File tab - File Metadata section

### Auto Select Next Unsorted Clip

With this box ticked, hitting the Return key once you have filled a metadata field jumps to the next Media Pool clip while leaving the cursor in that same field. That makes for fast back-to-back metadata entry without clicking the Next Clip button or hand-selecting whichever Media Pool clip comes next. Auto Select Next Unsorted Clip checkbox and Next Clip button Any time a Media Pool clip is chosen, the name shown to the right of the Clip and Track and Mode buttons opens with “Media Pool – “.

### File tab - Media Pool clip selected

### Audio Configuration

This part of the File tab carries features and controls for changing an audio clip’s channel properties in a natural way. What you change here sets how many channels in the clip stay active and fixes each one’s source and volume level as the clip drops into the Timeline. How the Audio Configuration pane looks shifts with the format of the clip you are trimming. The screenshots below, for instance, show a 6-channel clip in the Media Pool under two distinct channel formats.

6-channel adaptive - Media Pool clip

### 6-channel mono - Media Pool clip

- Format: Pick an audio clip in the Media Pool and the Format dropdown shows its current channel format, the standard channel configurations, and a Custom option. You can hand the clip any of these channel configurations without going through Clip Attributes to customize it.

Format dropdown menu - for a 6-channel adaptive clip Pick a timeline clip instead and the Format dropdown shows its current channel format together with the Custom option. That timeline clip, though, is built from two mono channels, and you can swap the audio source on each channel. Picking the Custom option brings up the Audio tab of the Clip Attributes dialog.

To read more about working with the Clip Attributes dialog, turn to Chapter 22, “Modifying Clips and Clip Attributes.”

- Waveforms: With a Media Pool clip, the topmost waveform under the Format dropdown shows a composite of every channel in the audio file. The waveforms below it stand for the audio in each individual channel of the clip.

That composite waveform is missing when you work with timeline clips. Listen to the audio by skimming it under your mouse cursor, by clicking the Play button in the transport control beneath the last waveform, or by tapping the spacebar. Click anywhere inside any waveform and playback carries on from that spot. The Transport Controls section further down covers this idea in more depth.

- Channel Controls: With source clips in the Media Pool, each clip channel gets its own Enable/Disable checkbox and Mute button.
- Active/Inactive: Tick the checkbox to enable a channel, putting it in play and open to editing operations. Leave the checkbox empty and editing operations skip that channel, as though it were gone from the clip. Take a 6-channel mono clip in the Media Pool: switch channel 2 off and only five tracks (1, 3, 4, 5, and 6) come along when you drag it from the Media Pool to the Timeline.
