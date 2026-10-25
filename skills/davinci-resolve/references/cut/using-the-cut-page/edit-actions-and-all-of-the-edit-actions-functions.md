# Edit actions and all of the edit actions functions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the cut page.
[Chapter index](INDEX.md) / [Previous section](audio-meter-showing-an-audio-signal-and-timeline.md) / [Next section](mute-and-solo-tracks-for-output-and-replay.md)
<a id="source-all-of-the-edit-actions-functions"></a> <a id="source-audio-mixer"></a> <a id="source-audio-mixer-controls"></a> <a id="source-audio-only-tracks"></a> <a id="source-audio-only-tracks-in-the-cut-page-timeline"></a> <a id="source-edit-actions"></a> <a id="source-editing-a-scene-with-multiple-superimposed-clips"></a> <a id="source-gaps"></a> <a id="source-the-cut-page-timeline-controls"></a> <a id="source-timeline-controls"></a> <a id="source-track-header-controls"></a> <a id="source-tracks"></a> <a id="source-tracks-2-and-above"></a> <a id="source-using-the-cut-page-part-2"></a>

### Edit Actions

The tools beneath this icon serve to adjust clips on the Timeline.

### All of the Edit Actions functions

- Trim Start to Playhead: Removes the whole portion of the clip sitting left of the playhead.
- Trim End to Playhead: Removes the whole portion of the clip sitting right of the playhead.
- Resync Clip: Should a clip drift out of sync with the rest of the program, this operation resyncs it.

### Tracks

Multiple tracks divide up the Timeline, each one able to hold a sequence of clips so as to form a program. The main tracks, labeled by number, fold a clip's video and audio into one item on the Timeline for simplicity. Editing the In or Out point of such a clip edits its video and audio in tandem.

Tracks on the Cut Page Timeline. A subtitle track sits on Track ST1. Track V1 displays Video only clips as well as combined Video+Audio clips, shown enlarged. A standalone audio track sits on Track A4.

TIP: Over on the Edit page, Video+Audio clips appear as separated Video and Audio items on different tracks. Open the Fairlight page and audio shows up on tracks with lanes, each audio channel visible. This way each page hands you different sets of controls over what's in the Timeline, fitted to that page.

### Track Header Controls

The track controls, in their order, let you enlarge a track, lock it against edits, mute its audio, and turn its video on or off.

Controls for enlarging a track, locking it, muting its audio, and disabling its video The Importance of Track 1 Every track in the Cut page Timeline is built to carry particular parts of your program. Track 1 holds the program's main video+audio, often dubbed the "A-roll," since these are the chief shots that set the timing and pacing of the story you're telling. Add, delete, insert, trim, or otherwise reshuffle clips on Track 1 and the rest of the edited timeline ripples on its own to take in your change, with clips right of the altered spot sliding left to fill the gap left by a deleted or shortened clip, or sliding right to open room for an inserted or lengthened one.

### Tracks 2 and Above

Tracks 2 and up are meant for "B-roll," the extra footage you layer over other clips on Track 1 to show what someone in the Track 1 audio is talking about, or for superimpositions that composite two images together in inventive ways. Moving or resizing a clip on Track 2 and above shifts or resizes only that single clip; the Timeline's other clips stay put and no rippling happens when you do it. Where several video clips overlap one another across multiple tracks, the one on the highest track hides those beneath it, so only the topmost clips show during playback. That helps when you're experimenting with rearranging several clips in a busy scene. You might, say, be editing a scene where an interview clip rests on the bottom track and various b-roll clips are edited onto tracks above it, leaving you free to shuffle them around at will, while it stays easy to reveal the speaker on the bottom track by opening a gap in the superimposed b-roll.

### Editing a scene with multiple superimposed clips

That said, if you superimpose video-only or video+audio clips for compositing, the composite modes and the opacity slider in the Composite section of the Viewer Tools controls let you blend several images together in different ways for artistic effects.

(Left) Stacking the clips you intend to composite, (Right) Building compositing effects out of several superimposed clips When you need them, you can add further Video+Audio tracks, either by dragging a clip to the empty gray region of the Timeline above the existing tracks to spawn a new one automatically, by clicking the New Track button at the Timeline's top-left corner, or by right-clicking the timeline header area and picking "Add Video Track" from the contextual menu.

### Audio-Only Tracks

Audio-only clips such as music, narration, or sound effects can likewise be edited onto separate audio-only tracks below, which then get labeled A1, A2, A3, and so on. Drag an audio clip into the empty gray region of the Timeline beneath the existing tracks and an audio-only track is created automatically.

### Audio-only tracks in the Cut page Timeline

### Gaps

Since Track 1 is built to carry your program's principal clips, the Timeline ripples itself automatically to seal gaps that would otherwise open when you move or rearrange clips on Track 1, while superimposed clips on Tracks 2 and above shift to stay in sync with the clips they sit over. You can, however, move superimposed clips on Tracks 2 and above to put them wherever you like, and gaps stay open between several clips sharing one superimposed track, letting them be edited at particular spots.

### Timeline Controls

Up in the Timeline's top-left corner, the Timeline controls let you toggle Rippling on Track 1, enter Dynamic Trim mode, Split a clip where the playhead sits, make Markers, and bring up the Keyframe Editor.

### The Cut page Timeline controls

### Audio Mixer

A full Audio Mixer can be shown on the Cut page, reaching every track and bus of your mix, plus shortcuts to any audio Track FX, Dynamics, and Equalizer tools. To turn on the Audio Mixer, click the Mixer tab up top of the Cut page.

The Audio Mixer in its expanded state, which keeps every audio track in view as you go on editing in the Cut page's Upper Timeline.

### Audio Mixer Controls

The channel strip of each track carries these controls:

- Track Number: Shown here is the number of the timeline audio track that each channel strip maps to.
- Track Effects: To open one of the track effects sitting above the fader controls, double-click it.

FX: Opens the Track Effects controls in the Inspector.

EQ: Opens the Track Equalizer.

DY: Opens the Track Dynamics.

- Pan control: Allows you to slide a Mono track’s audio between left and right, to swap the left and right audio channels of a Stereo track, or to carry out surround mixing.
- Name: This is the name of the audio track tied to the channel strip. Should you have renamed the audio tracks back in the Timeline, those revised names show up here.
- Solo: Silences every track apart from the ones you have soloed.
- Mute: Switches that audio track off.
- dB: Displays the current volume of that track, expressed in decibels.
- Fader: Drag each track’s vertical fader using a mouse or another pointing device to set that track’s volume and to capture automation recording. Pushing it upward raises volume, while pulling it downward lowers volume.
- Audio meters: Sitting to the right of each fader, the Audio meters show the audio volume of every channel on that track as it plays. The individual meters on each channel strip match the count of channels the track has been configured to hold.
