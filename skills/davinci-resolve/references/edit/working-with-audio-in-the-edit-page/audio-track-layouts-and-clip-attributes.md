# Audio track layouts and clip attributes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Previous section](edit-fairlight-audio-and-format-support.md) / [Next section](subframe-editing-and-in-out-points.md)
<a id="source-changing-audio-clip-attributes-after-editing"></a> <a id="source-contextual-menu-for-changing-audio-track-types"></a> <a id="source-creating-timelines-with-audio-mixer-presets"></a> <a id="source-defining-timeline-audio-track-channels-at-creation"></a> <a id="source-displaying-waveforms-in-the-timeline"></a> <a id="source-editing-audio-clips-into-the-timeline"></a> <a id="source-editing-audio-in-the-timeline-using-in-and-out-points"></a> <a id="source-resizing-audio-clips-in-subframe-increments"></a> <a id="source-switch-mono-audio-channels-of-a-clip-on-the-timeline"></a>

### Defining Timeline Audio Track Channels at Creation

As you make a brand-new audio track, you must decide what type of audio track it should be. A right-click down in the lower audio area of the Timeline track header opens a contextual sub-menu offering three distinct kinds of audio track to create.

- Mono: Holds a single channel.
- Stereo: Holds stereo left and right channels. Stereo tracks can be panned.
- 5.1: Carries the six channels that make up a 5.1 surround mix. On the broadcast side, SMPTE lays out

Left, Right, Center, LFE, Left Surround, Right Surround. For cinema distribution the order of these tracks is Left, Center, Right, Surround Left, Surround Right, and LFE.

- 7.1: Carries the eight channels that make up a 7.1 surround mix. On the broadcast side, SMPTE arranges them as Left, then Right, then Center, followed by LFE, next Left Surround with Right Surround, and lastly Back Surround Left plus Back Surround Right. For cinema distribution the sequence runs Left, then Center, then Right, followed by Left Surround alongside Right Surround, then LFE, and closing with Back Left Surround plus Back Right Surround.
- Adaptive: Able to carry as many as 24 audio channels. An adaptive audio track accepts clips bearing assorted channel combinations, up to the ceiling set for that track. How many channels a particular Adaptive track permits is something you define (1–24) at the moment the track is made. Cut a clip carrying more channels into an Adaptive track built for fewer, and the surplus channels get muted.

A set of four audio tracks of differing kinds, reading top to bottom as Mono, then Stereo, then Adaptive, then 5.1 Changing How Many Channels an Audio Track Has Should you have laid out your timeline with one type of audio track only to realize you really want another, you can switch any audio track’s type whenever you wish. Simply right-click anywhere in that audio track’s timeline header and pick an option from the contextual menu’s Change Track Type To submenu.

### Contextual menu for changing audio track types

### Creating Timelines With Audio Mixer Presets

To support advanced audio workflows and smoother use with Fairlight, you can now spin up a timeline whose audio tracks are pre-assigned from a Fairlight Configuration preset you built earlier. To do so, start a new timeline and tick the “Use Fairlight Configuration Preset” box. A drop-down then shows up, letting you pick the exact preset for the Timeline. You build Fairlight Configuration presets from the Fairlight Presets Library, reached through the Fairlight menu. To read more, turn to Chapter 171, “Setting Up Tracks, Busses, and Patching.”

### Editing Audio Clips Into the Timeline

Cut a video clip that has audio with it, or an audio-only clip, into the Edit page Timeline, and what shows up hinges on how the audio’s inner tracks and channels were laid out in the Media Pool through Clip Attributes. Define a clip to surface several audio tracks, each carrying a different channel, and you trade the ease of handling many audio channels as a single item for the latitude to edit each audio channel on its own, as separate clips in the Timeline. Suppose you were handed a multi-channel recording made of two boom microphones, two separate lavaliere microphones, and a mixdown track all captured at once: through the Audio panel of the Clip Attributes window you can set that clip’s audio as 5-channel Adaptive audio across 5 tracks of one channel apiece. Cut that into the Timeline and you end up with five separate audio items spread over five tracks. Cutting a multi-channel production recording into five distinct audio tracks This way, once you cut the clip into the Timeline, each audio channel arrives as its own clip on its own Timeline audio track, editable on its own so you can work the scene to pick the best dialog off each microphone.

Cutting multi-track audio to single out the strongest dialog from each microphone

### Changing Audio Clip Attributes After Editing

Settling on which audio tracks and channels get assigned is best done before you start editing. The reason is that after a clip lands in a timeline, the Clip Attributes window can no longer change how many audio tracks and audio channels surface in the Timeline. You can, however, still turn to Clip Attributes to alter which channels are assigned and/or muted among the tracks and channels you have already cut into the Timeline. Say you are cutting clips holding five channels of source audio (channels 1 and 2 form a stereo mix and channels 3 through 5 are three separate microphones): you might have configured your synced source clips with a single audio track holding five audio channels, channels 3–5 left muted. Down the line, a handful of clips would sound far better drawing on channel 4 alone, the isolated lavaliere microphone for that actor, so you can pick those clips and use the Audio panel of Clip Attributes to mute every channel but channel 4. If for any reason you must surface more audio tracks in the Timeline than the clip was first set to use, here is the procedure. To re-cut an audio clip so it surfaces more audio tracks than were available at first: 1 On the Timeline, right-click the clip whose audio track mapping needs changing; from the contextual menu, choose Find in Media Pool. 2 Over in the Media Pool, right-click that clip; from the contextual menu, choose Clip Attributes. 3 Bring up the Audio panel within the Clip Attributes dialog and decide how many audio tracks and audio channels that clip should get. Click OK. 4 That settled, cut the revised audio clip out of the Media Pool onto the Timeline to swap out the original by whatever method suits.

### Displaying Waveforms in the Timeline

Through a button at its top, the Timeline View options palette flips the Audio Waveform display on and off. The Audio View options then let you decide how your waveforms appear on the Timeline.

- Audio View Options: When waveforms are visible, three buttons steer their appearance in the Timeline. Non-Rectified Waveform: Switches between drawing the waveform upward from the audio track’s bottom or centering and mirroring it on itself. Full Waveform: Drops the divider bar that separates the waveform from each audio clip’s file name area, letting the waveform fill the whole height of each audio bar in the Timeline. Waveform Border: Outlines every waveform with a dark border so they stand out more.
- Video track height slider: Resizes all video tracks together, apart from the audio tracks.
- Audio track height slider: Resizes all audio tracks together, apart from the video tracks.

Within the Timeline View drop-down, the Audio Waveform display option is ringed in red. Reading left to right, the Audio View Options run Non-Rectified Waveforms, Full Waveform, then Waveform Border.

By default a clip shows one averaged audio waveform standing for all its channels, but you can flip any clip to a vertical stack of each separate waveform by right-clicking that audio clip and choosing Display Individual Audio Channels. Cut an audio clip and every audio channel in it gets cut along with it. Audio channels packed inside one track cannot be edited individually.

Enabling the display of multiple channel waveforms in the Timeline

### Switch Mono Audio Channels of a Clip on the Timeline

On mono channel lanes in the Edit page, you can swap your mic (or other) audio sources either from a context menu or through the Inspector. This helps when you are cutting with a mix track and notice a lav mic carrying noise that you would rather replace with boom audio. Two routes exist for swapping a mono audio source: through the timeline or through the Inspector. Changing mono audio sources via context menu on the timeline: When you sit on a mono timeline track whose parent audio file holds several mono tracks, right-click it and an Audio Channel choice turns up at the foot of the context menu. From the hierarchical menu you can then pick any mono source.

A right-click on an audio clip surfaces the available source audio channel choices for you to pick

Command right-clicking an audio clip on the timeline surfaces nothing but the source audio channels

For an even tidier workflow, press Command right-click instead and you get a drop-down listing only the mono sources: Changing mono audio sources via the Inspector: Once a timeline clip is open through the File Inspector, you can swap mono track/lane sources via a drop-down on the channel waveform.

To swap the audio channel, work the drop-down menu sitting on the channel within the File Inspector’s Auµdio Configuration section.

### Editing Audio In the Timeline Using In and Out Points

Every command and tool that works on video clips works on audio clips as well. Worth knowing, though, is that one of the most widespread audio-editing techniques from other environments is here in DaVinci Resolve too: marking off a span of audio to cut, copy, or delete with Timeline In and Out points, which lets you readily remove, shift, or duplicate partial audio stretches with no need to reach for the Razor Edit or Split Clip commands. Deleting an audio section by means of In and Out points: 1 In the Timeline, lay down In and Out points that mark the audio span you mean to remove. Where needed, switch off the Auto Select controls on tracks to leave out overlapping audio clips you do not want deleted in this pass. 2 Tap the Backspace key to remove the audio span and leave a gap, or tap the Forward Delete key to remove the span and ripple the Timeline shut over the gap.

Laying down In and Out points to mark off a span of audio for deletion

Removing the audio with the Backspace key so a gap remains

Copying an audio section by means of In and Out points: 1 Lay In and Out points in the Timeline to mark the audio span you mean to copy. Where needed, switch off the Auto Select controls on tracks holding overlapping audio you do not want copied; Option-click the Auto Select control of the audio track you are copying from to solo it, and Shift-click any video track’s Auto Select control to switch them all off. Here we are copying a bit of background ambience to keep building an ambience track.

Laying down In and Out points to mark off a span of audio for copying 2 Tap Command-C to copy that audio span. 3 Tap Option-X to wipe the Timeline In and Out points, then bring the playhead to wherever you want the copied audio span pasted. 4 Tap Command-V to paste the copied audio. When looping a span of audio, paste repeatedly to loop whatever you copied.

Pasting the background ambience several times to loop it

### Resizing Audio Clips in Subframe Increments

As an option, DaVinci Resolve permits subframe audio tweaks to the In and Out points of Timeline audio clips.
