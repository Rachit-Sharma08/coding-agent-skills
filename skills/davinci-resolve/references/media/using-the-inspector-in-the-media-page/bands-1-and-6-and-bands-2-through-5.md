# Bands 1 and 6 and bands 2 through 5

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the media page.
[Chapter index](INDEX.md) / [Previous section](lens-correction-and-retime-and-scaling.md)
<a id="source-audio-configuration"></a> <a id="source-bands-1-and-6"></a> <a id="source-bands-2-through-5"></a> <a id="source-file"></a> <a id="source-image"></a> <a id="source-metadata"></a> <a id="source-the-file-inspector-controls"></a> <a id="source-the-image-inspector-controµls-for-braw-footage"></a> <a id="source-timecode"></a> <a id="source-using-the-inspector-in-the-media-page-part-2"></a>

### Bands 1 and 6

When required, the outermost two sets of band controls give you high-pass and low-pass adjustments.

- Band enable button: Switches each band of EQ on and off.
- Band filter type: Bands 1 and 6 can be flipped among five specific filtering options for

handling the lowest or highest frequencies in the signal. On Band 1 these run (top to bottom): Lo-Shelf, Bell, Notch, Hi-Shelf, and Hi-Pass. On Band 6 the options run (top to bottom): Lo-Pass, Lo-Shelf, Bell, Notch, and Hi-Shelf.

- Freq: Sets the center frequency of the EQ adjustment.
- Gain: Sets how strongly the affected frequencies are impacted. Negative values

cut those frequencies, while positive values lift them.

- Q Factor: This parameter sets the width of affected frequencies and shows up whenever the Bell option is chosen. Lower values take in a wider range of frequencies; higher values take in a narrower range of frequencies.

### Bands 2 through 5

These band controls let you make a broad spread of equalization adjustments.

- Band enable button: Switches each band of EQ on and off.
- Band filter type: These Bands carry four filtering options (top to bottom): Lo-Shelf, Bell,

Notch, and Hi-Shelf.

- Frequency: Sets the center frequency of the EQ adjustment.
- Gain: Sets how strongly the affected frequencies are altered. Negative values

cut those frequencies, while positive values lift them.

- Q Factor: This parameter shows up when the Bell setting is chosen. It sets the width of

affected frequencies. Lower values pull in a broader span of frequencies; higher values tighten that span. NOTE: The Audio FX library holds plenty of more sophisticated plugins and effects for audio clips. Apply any of them and their controls turn up within the Inspector’s Effects tab Audio section rather than here.

### Image

The Image panel holds groups of parameters matching every camera raw media format DaVinci Resolve supports. By means of these Image panel parameters, the original camera metadata written when the footage was recorded can be overridden, and you can adjust camera raw media simultaneously across your whole project. For a thorough rundown of every RAW camera parameter DaVinci Resolve supports, refer to Chapter 7, “Camera Raw Settings.”

### The Image Inspector controµls for BRAW footage

### File

### The File Inspector controls

### Metadata

The File panel of the Inspector offers a consolidated route to view and edit a slice of a clip’s most commonly used media file metadata. From the Inspector it’s readily reached on the Media, Cut, Edit, and Fairlight pages alike. This tab breaks down into these parts:

- Clip Details: Lays out data about the clip’s data format (codec, resolution, frame rate, etc.).
- Metadata: Lays out a trimmed set of common metadata fields for quick user entry.

Timecode: The clip’s start timecode. This field is editable when you want to change the clip’s starting timecode by hand. Date Created: The date the clip was created. This field is editable when you want to change the clip’s creation date by hand. Camera: Writes the Camera # metadata. Reel: Writes the Reel/Card ID. Scene: The clip’s Scene number. Shot: The clip’s Shot letter/number. Take: The clip’s Take number. Good Take: This checkbox marks whether the clip is a good or circled take. Clip Color: Hands a particular color to a clip that shows up in the Timeline. Name: This can be typed in by hand and changes a clip’s name only within that specific timeline. Comments: Tack a text description onto the clip.

Auto Select Next Unsorted Clip: With this box ticked, the next clip in the Media Pool is selected once you press the Return button after filling in a metadata field, and the cursor drops automatically into that same field. That enables rapid sequential metadata entry, sparing you from clicking by hand to load each separate clip within the Media Pool. Regardless of the checkbox status, the Next Clip button moves to the next clip in the Media Pool.

### Audio Configuration

The File tab in the Inspector now carries an Audio Configuration pane that takes over the controls once handled by Clip Attributes in the Media Pool (although that option remains available). The Audio Configuration pane gives a more intuitive, visual route to changing an audio clip’s track properties. Just click an audio clip in the Media Pool or Timeline, then the File Inspector, to bring up this interface. The pane sports a per-channel waveform display for every track inside a multichannel audio file. Where the tracks were named in the audio recorder, those names show up over their respective tracks as well. The Audio Configuration panel can preview as many as 36 tracks of audio. Across the top of the pane sits a composite waveform of all the tracks, refreshed according to the mute status of individual tracks. By default this composite plays when the Play button is engaged, and every channel is audible.

The Audio Configuration panel. Here Track 3 sits muted while Track 5 sits disabled. By way of a format menu you pick common configurations for your source audio file, skipping any clumsy manual re-routing. Custom routing is still catered for by choosing custom in the drop-down, which surfaces the older clip attributes for situations calling for less common configurations. To play or skim the audio of a chosen source or timeline clip, glide the cursor across the waveform; the particular track is solo’ed as you skim or play. You can likewise shift, mid-playback, the play position or the track under monitor. For instance, you might begin playback on track one, then simply click track two, and playback carries on from that point. These controls let you swiftly skim through and pin down exactly which audio sits on which track for further adjustment.

Two adjustments accompany each track: an Enable/Disable checkbox plus a Mute button. Enable/Disable: When a track is enabled, it becomes available for editing operations. When a track is disabled, it drops out of editing operations. As an example, if you disable Track 2 of a 4-track audio file, then dragging that audio file from the Media Pool into the timeline brings over only 3 tracks (1, 3, and 4). These adjustments can be made on Media Pool clips alone; audio clips already in the timeline will have these options disabled. Mute: A click on this icon silences the track so it isn’t heard, but the track itself stays present during editing operations and when dragged into the timeline. Option clicking a channel’s mute button solos it by silencing all the other channels. Beneath the track layout sits a plain transport control of Play and Stop buttons for starting and halting audio playback. Adjusting Trim Levels of Individual Channels in a Source File Inside the audio inspector, a trim control lets you set the level of individual source clip channels. With it, audio in one source clip channel can be pushed up or pulled down in level, as the situation calls for. That trimmed level stays internal to the source clip in the Media Pool and carries over wherever that source clip configuration appears on a timeline, until you change it. NOTE: Trim level has nothing to do with clip gain over in the timeline — the two are wholly distinct. Keep in mind that pushing trimmed levels too high can make them clip.

The trim levels of separate audio channels within a multichannel clip are yours to adjust.

Using the Trim slider 1 Within the Audio Configuration section of the File Inspector, pick one or more channels 2 Drag the Level slider along the bottom to whatever audio level you’re after. The waveform shifts dynamically with the level value and shows a trimmed value in dB on the channel itself. With several lanes selected, all channels get trimmed together. Relative levels aren’t stored, so adjusting one then forces any others in the selection to match. With no channel lanes selected, the Level control is grayed out. Multiple Clip Selection and Adjustments Several audio clips can be selected and their properties adjusted in the Audio Configuration pane. For instance, you can pick a batch of audio files and strip Track 2 from every one at once. Bear in mind, though, the following:

- Within a multiple clip selection, only the last selected clip turns up in the track layout of the Audio Configuration pane. The top composite waveform, however, gets named “Multiple Clips” to flag that more than one clip is selected.
- Any adjustment, such as muting or enabling/disabling a track, lands on all the selected clips at once.

### Timecode

The File tab in the Inspector now carries a Timecode pane that assumes the sorts of controls Clip Attributes in the Media Pool used to manage (though that route stays open). From here the timecode details of a clip, or several clips, in the Media Pool can be overridden.

- Current Frame: Use this to stamp a fresh time onto the timecode at whichever frame of the clip you're presently looking at.
- Slate: When footage originates from a shoot that used a timecode slate on set, you can store that slate's timecode as a second timecode track for assorted tasks, leaving the clip's primary timecode untouched in case it's already serving program sync. To dial in the right Slate timecode, pick a clip in the Media Pool that shows a visible timecode slate, then nudge the playhead onto a frame where the slate's timecode reads clearly. Next, bring up the Timecode panel inside the Clip Attributes window and key the timecode value you read off the image into the Slate Timecode field.
- Offset Source: When a whole batch of clips carries timecode that is simply shifted, you can fix that timecode offset across as many of the selected clips as you want.
