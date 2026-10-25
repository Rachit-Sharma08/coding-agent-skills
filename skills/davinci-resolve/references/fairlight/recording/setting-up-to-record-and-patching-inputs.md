# Setting up to record and patching inputs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Recording.
[Chapter index](INDEX.md) / [Next section](layered-takes-and-vsti-recording.md)
<a id="source-arming-tracks"></a> <a id="source-automatic-input-patching"></a> <a id="source-choosing-where-to-record-audio-clips-to"></a> <a id="source-manual-input-patching"></a> <a id="source-patching-inputs"></a> <a id="source-record-name-prefix"></a> <a id="source-recording"></a> <a id="source-recording-1"></a> <a id="source-recording-using-the-onscreen-controls"></a> <a id="source-setting-up-to-record"></a> <a id="source-user-selectable-input-monitoring-options"></a>

### Recording

On the Fairlight page you can record onto one track or several, covering workflows as diverse as editors laying down scratch voiceover or temporary sound effects, recording engineers capturing narration, ADR, or foley while finishing the audio, music studios tracking orchestras for the score, or garage bands committing their newest masterpiece to disk. DaVinci Resolve may be a full-featured post-production suite for film and video, but the Fairlight page suits whatever audio recording need you bring to it, whether books on tape, live music, feature films, or television.

### Setting Up to Record

How your workstation is configured determines whether you can record onto several tracks at once in the Fairlight page. Exactly how many tracks you can capture to hinges entirely on the hardware you have on hand. The steps in this section cover how recording onto tracks in the Fairlight page works.

### Patching Inputs

Ahead of recording any audio, you have to open the Patch Input/Output window and route an available audio input to a track. DaVinci Resolve lets you nominate a permanent default input that gets patched to the track input on its own once the R (Record Arm) button is pressed, or you can patch an audio input in by hand before record-arming. Lacking a connected audio interface, you can fall back on your workstation’s own inputs to hook whatever device is configured as your system’s default audio input up to the track you intend to record on.

### Automatic Input Patching

This section’s steps describe how to set DaVinci Resolve up so it automatically patches a chosen default audio input in the moment you press the R (Record-Arm) button on the track header or mixer channel belonging to your intended recording track. Here is how you configure Automatic Input Patching: 1 Click the Fairlight menu > Patch Input/Output. 2 Once the Patch Input/Output panel has opened, pick Setup I/O Names from the Options menu in the upper-right corner. Doing so brings up the I/O Setup panel.

The Patch Input/Output Options menu 3 Put a checkmark in the Default column beside the audio input you wish to make the default track input source, then close the I/O Setup panel.

Default audio input selection in the I/O Setup panel That input then gets patched in on its own whenever you record-arm any audio track via the R button on the Track header or Mixer channel. Up in the channel strip’s input section, the audio input name will show.

### Manual Input Patching

The steps below let you pick an input source by hand without disturbing whatever default audio input you may already have configured. To patch in an auto input by hand: 1 Open the Patch Input/Output pane this way: on the Mixer channel you mean to record on, click the Input button up top and choose Input. Or else, you can pick Patch Input/Output off the Fairlight menu.

Mixer channel strip Input button menu 2 Once the Patch Input/Output panel opens, choose both the audio input source and the destination track input. Repeat as often as needed until every input you want to record from is patched to every track you want to record to. As many inputs as your system allows can be patched to as many tracks. 3 Click the Patch button down in the panel’s lower-right corner.

Showing the Patch Input/Output panel once an Audio Input plus a Track Input have been chosen

### Arming Tracks

The moment you are set to record on a track, press the R (Record Arm) button on either the Track header or the matching Mixer channel. An audio track can only be record-armed after it has been patched by one of the methods covered above.

(Left) A Track header showing the Record Arm button engaged; (Right) a channel strip with that same Record Arm button engaged

### Record Name Prefix

Right-clicking the chosen record track header offers an option to assign a recording name prefix to that track’s recordings. It is a handy way to stay on top of the assorted recordings your project calls for. When recording ADR, for instance, you might add a prefix per character’s recordings, as shown below for a character named Pilot.

Right-clicking a track header reveals the Set Track Record Name option

Example of a recording name prefix for a character called Pilot

### Choosing Where to Record Audio Clips To

Recording in the Fairlight page produces fresh clips and writes more media to disk. You can set the on-disk spot where these recordings are saved by opening the Capture and Playback panel of the Project Settings. Within the Capture section, the Browse button sitting beneath the “Save clips to” field lets you pick a new spot (the default is a folder called “Capture” on your scratch disk). To decide where the newly created clips land in the Media Pool, simply open the Media Pool, then click any bin within the Bin list; alternatively, create a fresh bin and select it should you want your recordings kept in their own spot.

### User-Selectable Input Monitoring Options

Five choices governing how you monitor inputs during recording sit in the Fairlight > Input Monitor Style submenu.

- Input: All you hear is the live signal coming in; the contents of tracks never reach you.
- Auto: While one or more tracks sit armed for recording, you hear the live input signal; come

playback you hear the contents of each track.

- Record: The live input signal reaches you only during active recording, that is, once the Record button

has been hit with one or more tracks armed for recording. While tracks merely sit armed, the input signal stays silent to you.

- Mute: You hear nothing.
- Repro: During recording, all you hear is what was just laid down, replayed off the track. Put differently, you are not monitoring the live input but instead reviewing the freshly recorded material as it records.

### Recording Using the Onscreen Controls

You can record wherever you like on the currently armed track or tracks by parking the playhead at the point recording should start. That way, you can drop recordings into particular spots in your program as you capture voiceover, sound effects, foley, or other timed performances meant to slot into a specific stretch of the edit. To begin recording: 1 Park the playhead at the point recording should begin. 2 Click the Record button among the transport controls. Recording starts right away, and the incoming material immediately begins painting a waveform live, giving you instant confirmation of whether the input you are recording is hooked up properly, plus where on the currently armed track material is going down. To stop recording, do one of the following:

- Click the Stop button in the transport controls.
- Press the Spacebar.
